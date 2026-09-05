---
day: 60
paper: "doi:10.1145/214451.214456"
title: "Distributed snapshots: determining global states of distributed systems"
ids: ["AG-22"]
level: production
prerequisites: ["../parts/02-the-log-is-the-run/2.5-the-cut-that-includes-the-message-in-the-air.md"]
prev: "../parts/07-in-production/7.2-what-a-reviewer-asks.md"
next: "../LESSON.md"
---

# Distributed snapshots: determining global states of distributed systems

> **Citation.** *Distributed snapshots: determining global states of distributed systems* ·
> `doi:10.1145/214451.214456` · ACM Transactions on Computer Systems **3**(1), 63–75 · 1985 ·
> <https://doi.org/10.1145/214451.214456>
>
> Verified on 2026-09-05 against the Crossref record for that DOI, which supplied the title,
> subtitle, journal, volume, issue, page range and year. Row added to `docs/PAPERS.md`.

## One-line answer

A system can record a global state that it could genuinely have been in **without stopping**, by
sending markers along its channels and letting each part decide from the markers what belongs in
the snapshot — and the demo shows the alternative losing two tokens out of six.

## The story

A shop takes stock once a year, and to do it, it closes.

The shutter comes down on a Sunday morning, everybody counts, and the shop opens again on Monday
with a number. The number is good. Nobody disputes it, because while it was being produced,
nothing moved: no sales, no deliveries, no returns. One moment, frozen, counted.

The owner would rather not close. A Sunday is a Sunday, and the annual count is the only reason
the shutter ever comes down. So he tries counting while trading, and it does not work — not
because his staff are careless, but for the reason
[2.5](../parts/02-the-log-is-the-run/2.5-the-cut-that-includes-the-message-in-the-air.md)
already showed: two counts taken at two moments produce a total that belongs to neither.

And here is where he is genuinely stuck, and it is worth sitting with, because for a while
everybody was. He can have a number he trusts, by closing. Or he can stay open and have a number
he does not trust. What he cannot see is any third option — and *"count it while it is running,
and be able to prove the number is real"* does not sound like something that has an answer. It
sounds like wanting two contradictory things.

## The idea in plain language

The paper's claim is that the third option exists.

Some background first, in plain words. A **distributed system** here is a set of parts that each
hold some state and send each other messages. The parts do not share a clock and cannot see each
other's insides; the only thing that happens between them is a message, sent at one moment and
arriving at a later one. Between those two moments the message is **in transit**: it has left the
sender and has not reached the receiver, and it belongs to neither of them.

A **global state** is what all the parts hold, plus everything in transit, at one moment.

The problem is that "at one moment" is not available. No part can see the others; no part can
freeze the others; and by the time a part has told you what it holds, it holds something else.

The paper's answer has two halves, and the first is the one that makes the second possible.

**Half one: change the goal.** Do not try to record the state at *an actual instant*. Try to
record a state the system **could have been in** — one that is consistent with everything that
happened, where no message is received before it was sent. Such a state is a legitimate answer to
"what did the system look like?" even though there may have been no instant at which it was
literally true.

That sounds like a weakening and it is the whole trick. The recorded state is good enough for the
questions people actually ask of a snapshot — is anything deadlocked, has the money balanced,
where do we restart — and unlike an instantaneous state, it is *achievable*.

**Half two: use the messages themselves to mark the boundary.** A special message, the **marker**,
is sent along every channel. Because channels deliver in order, a marker arriving on a channel
divides that channel's messages cleanly into *before* and *after*. The parts never need a shared
clock; they need only agree on what to do when a marker arrives.

## Why Sutra needs it

Directly:
[2.5](../parts/02-the-log-is-the-run/2.5-the-cut-that-includes-the-message-in-the-air.md) is built
on this idea. It measured a desk that always holds ten tickets reporting eleven, every time, and
gave the reason — a moving ticket counted on the shelf it had left and the shelf it had not
reached.

Indirectly, and more importantly, it is why
[5.2](../parts/05-triage-made-durable/5.2-where-the-boundary-goes.md) makes the argument it does.
Once you know what a consistent cut costs to obtain, you can see why production systems arrange
their checkpoint boundaries at moments when nothing is in flight: they are not solving this
problem, they are **avoiding needing to**. You cannot make that choice knowingly without knowing
what the choice is between.

And it is the vocabulary. "Consistent cut", "in transit", "a state the system was never in" are
the words this paper put into the field, and they are the words a reviewer will use when they ask
why your checkpoint does not include the outstanding request.

## The mechanism

The algorithm is three rules. Every part follows them and no part needs to know the whole graph.

**Rule 1 — starting.** Any part may start a snapshot at any time. It records its own state, and
then, **before sending any further ordinary message**, sends a marker on each of its outgoing
channels.

**Rule 2 — receiving your first marker.** A part that receives a marker on channel *c*, and has
not yet recorded its own state, records its state now and records **channel *c* as empty**. Then
it sends a marker on all of its own outgoing channels.

**Rule 3 — receiving a later marker.** A part that has already recorded its state, receiving a
marker on channel *c*, records as *c*'s state **every message it received on *c* between
recording its own state and the marker's arrival**.

Rule 3 is the paper. Rules 1 and 2 record what the parts hold; rule 3 records what was in the air,
and it does so without anybody knowing what was in the air — the messages simply arrive, are
noticed because they arrived after the part recorded itself, and stop being noticed when the
marker comes.

Why the marker separates cleanly: channels deliver in order. The sender recorded its state and
*then* sent the marker, so everything that sender put on that channel before recording is ahead of
the marker, and everything after is behind it. The receiver therefore knows that every message it
sees before the marker was sent before the snapshot began.

The order of the two actions in rule 1 is the whole correctness argument, and it is exactly
[3.1](../parts/03-doing-it-twice/3.1-the-uncertainty-gap.md)'s ordering question in another
costume. Record first, then send the marker. Reverse it and an ordinary message can slip ahead of
the marker after the state was recorded, and land in neither the sender's state nor the channel's.

```mermaid
sequenceDiagram
    participant A
    participant B
    Note over A: rule 1: record my state
    A->>B: MARKER
    B->>A: token (sent before B knew)
    Note over B: rule 2: first marker —<br/>record state, channel A→B empty
    B->>A: MARKER
    Note over A: this token arrived after A recorded:<br/>it is in transit, log it
    Note over A: rule 3: marker on B→A —<br/>stop logging; that is the channel's state
```

## The paper in one demo

Two files, and neither of them does anything except this paper. Two processes pass tokens; the
number of tokens is conserved, so a correct snapshot totals six and an incorrect one does not.

```text
lab/papers/distributed-snapshots/
├── snapshot.py   the three rules
└── demo.py       a run, an invariant check, and the ablation switch
```

`snapshot.py` — the algorithm:

```python
@dataclass
class Process:
    name: str
    tokens: int
    outgoing: Channel | None = None
    incoming: Channel | None = None
    recorded_tokens: int | None = None
    recorded_channel: list[object] = field(default_factory=list)
    logging_channel: bool = False

    def start_snapshot(self, use_markers: bool) -> None:
        """Rule 1: record my state, then send a marker before any further message."""
        self.recorded_tokens = self.tokens
        if use_markers and self.outgoing is not None:
            self.outgoing.send(MARKER)
        self.logging_channel = use_markers

    def step(self, use_markers: bool) -> None:
        """Receive one item, applying rules 2 and 3 when it is a marker."""
        item = self.incoming.receive()
        if item is None:
            return
        if item == MARKER:
            if self.recorded_tokens is None:
                self.recorded_tokens = self.tokens
                self.recorded_channel = []
                self.logging_channel = False
                if self.outgoing is not None:
                    self.outgoing.send(MARKER)
            else:
                self.logging_channel = False
            return
        self.tokens += 1
        if use_markers and self.recorded_tokens is not None and self.logging_channel:
            self.recorded_channel.append(item)
```

**Line by line:**

- `recorded_tokens` is `None` until the process has recorded itself, so `is None` is exactly the
  test rule 2 needs — *have I recorded my state yet?* No extra flag is required.
- `start_snapshot` records **before** sending the marker. Swapping those two lines is the bug the
  ordering argument above is about.
- `self.logging_channel = use_markers` at the end of rule 1: from this instant until a marker
  comes back, anything arriving on my incoming channel was in transit when I recorded, so it is
  part of the cut. This is rule 3 armed.
- In `step`, the first branch is rule 2: record my state, record this channel as **empty** — which
  is correct, because the marker was the first thing to arrive on it since the snapshot began —
  and then propagate a marker onward so the snapshot spreads.
- `self.logging_channel = False` inside rule 2 is easy to omit and matters: a process that has
  just recorded via rule 2 must not log the channel the marker came in on, because that channel is
  already recorded as empty.
- The `else` branch is rule 3: the marker has come back, so stop logging. Whatever was collected
  in `recorded_channel` **is** the channel's state.
- The last two lines are the ordinary case. Take the token, and log it only if I have recorded
  myself and am still logging — which is precisely "this token was in transit at the cut".

`demo.py` — the run and the ablation:

```python
def main() -> None:
    alice, bob, a_to_b, b_to_a = build()
    print(f"markers: {USE_MARKERS}")
    print(f"start: A={alice.tokens} B={bob.tokens} in transit=0 total={TOTAL}")

    alice.send_token()
    alice.start_snapshot(USE_MARKERS)
    bob.send_token()

    if not USE_MARKERS:
        bob.recorded_tokens = bob.tokens

    for _ in range(4):
        bob.step(USE_MARKERS)
        alice.step(USE_MARKERS)

    recorded_channel = len(alice.recorded_channel) + len(bob.recorded_channel)
    recorded = (alice.recorded_tokens or 0) + (bob.recorded_tokens or 0) + recorded_channel
    print(
        f"recorded: A={alice.recorded_tokens} B={bob.recorded_tokens} "
        f"in transit={recorded_channel} total={recorded}"
    )
    print(f"live now: A={alice.tokens} B={bob.tokens} total={alice.tokens + bob.tokens}")
    verdict = "consistent" if recorded == TOTAL else f"IMPOSSIBLE (lost {TOTAL - recorded})"
    print(f"verdict: {verdict}")
    sys.exit(0 if recorded == TOTAL else 1)
```

**Line by line:**

- `alice.send_token()` then `alice.start_snapshot(...)` puts a token on the A→B channel *before*
  the snapshot begins, so it is a message that was already in flight — the case that makes the
  naive method double-count.
- `bob.send_token()` after the snapshot starts puts a token on B→A while A has already recorded.
  That is the token rule 3 has to catch, and it is why the demo has traffic in both directions.
- The `if not USE_MARKERS` block is the **ablation**: B records itself whenever it likes, with no
  marker to say when *now* is and no rule telling it to log the channel. That is what
  "take a snapshot by asking each part what it holds" actually amounts to.
- The loop runs the system **while the snapshot is being taken**. Nothing is paused. That is the
  paper's claim, and a demo that paused would prove nothing.
- `sys.exit(0 if recorded == TOTAL else 1)` makes this an eval that can go RED (Principle 11):
  conservation is the invariant, and the exit code is the verdict.

The command, and the real output:

```bash
cd days/day-60-durable-execution/lab/papers/distributed-snapshots
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- The demo runs from its own directory so that `snapshot.py` imports as a sibling. Two files, no
  package, no installation step — the subtractive test from §17.4.2 applied.
- `echo "exit: $?"` prints the exit code, because the conservation check is the verdict and a
  verdict you cannot see is a verdict you will not act on.

Measured on 2026-09-05:

```text
markers: True
start: A=4 B=2 in transit=0 total=6
recorded: A=3 B=2 in transit=1 total=6
live now: A=4 B=2 total=6
verdict: consistent
exit: 0
```

Look at the middle two lines together, because that is the paper's whole idea in two rows of
numbers.

**Recorded: A=3, B=2, one in transit — total 6. Live now: A=4, B=2 — total 6.**

The recorded state is *not* the live state. A holds four tokens now and the snapshot says three.
There may have been no instant at which the system looked exactly like the recorded state. And the
recorded state is nevertheless **correct**: six tokens, accounted for, with the sixth recorded as
being in the channel rather than at either end. It is a state the system could have been in, which
is exactly what half one of the idea asked for.

Now turn the markers off:

```bash
uv run python demo.py --no-markers; echo "exit: $?"
```

**Line by line:**

- `--no-markers` is the ablation switch. It does not remove the snapshot — both processes still
  record what they hold — it removes the three rules that decide *when* they record and what
  belongs to the channel.
- Everything else is identical: same starting tokens, same sends, same loop, same invariant.

```text
markers: False
start: A=4 B=2 in transit=0 total=6
recorded: A=3 B=2 in transit=0 total=4
live now: A=4 B=2 total=6
verdict: IMPOSSIBLE (lost 2)
exit: 1
```

**Total 4, against a system that has 6.** Two tokens are in neither part's count and there is no
column for them, because without markers nothing tells either process when to start logging its
channel or when to stop. The exit code is `1`.

Same processes, same traffic, same number of tokens, one flag. The difference between the two runs
is the three rules.

## When it breaks

The paper's claim is exact, and reading past its conditions is the usual way to be disappointed
by it.

**It assumes channels deliver in order and lose nothing.** The marker's whole power is that it
partitions a channel's messages into before and after, and that requires FIFO delivery. On a
channel that reorders — plain UDP, or a load-balanced HTTP path with retries — a marker can arrive
before a message that was sent earlier, and the partition is wrong. Modern systems get this back
with sequence numbers, which is a real cost the paper does not pay.

**It assumes the parts do not fail.** There is no rule for a process that dies mid-snapshot. The
snapshot simply never completes, and the algorithm has no way to notice. Everything in
[1.2](../parts/01-what-a-run-is/1.2-died-or-failed.md) about telling a crash from a failure is
outside its scope, which matters a great deal for the use everybody actually wants it for.

**It records a state, and says nothing about what to do with it.** The paper is careful here and
its readers often are not. A recorded state is useful for **stable properties** — properties that,
once true, stay true, like deadlock or termination. Asking a snapshot a question about something
that changes, such as *"is this queue full?"*, gets an answer that was true of a state the system
possibly never occupied and certainly is not in now.

**It does not stop the world, and it does not stop the snapshot spreading.** Every process
receiving a marker sends markers onward, so a snapshot touches everything reachable. On a two-node
demo that is invisible. On a large system it is a burst of traffic proportional to the number of
channels, at a moment nobody scheduled, because rule 1 says *any* part may start a snapshot at any
time.

## In production

**What survived.** The vocabulary and the mental model, completely. "Consistent cut" is the term
of art, and the ability to say *"that snapshot is a state the system was never in"* is a working
engineer's tool that came from here. The idea that you change the goal from *the actual instant*
to *a state consistent with history* is now simply how people think about distributed observation,
including in systems whose authors have never read the paper.

The **marker mechanism itself also survived**, in one specific place: stream processing. Systems
that checkpoint a running dataflow send barriers through the stream and use their arrival to
decide what is in the checkpoint, which is rules 1 to 3 with different nouns. If you have
configured checkpointing in a stream processor, you have configured this algorithm.

**What did not survive** is the marker algorithm as the way to checkpoint an ordinary application,
and the reason is the one
[5.2](../parts/05-triage-made-durable/5.2-where-the-boundary-goes.md) gave. Real systems mostly
**arrange not to need it**: they checkpoint at points where nothing is in flight, which turns a
hard distributed problem into writing down a dictionary. That is not a criticism of the paper —
knowing that the general problem is solvable is what makes it safe to notice that you have the
easy case.

The half the field quietly dropped, and replaced with something blunter, is the **assumption that
the parts do not fail**. Everything in this day about at-least-once and idempotency exists because
production systems have to handle exactly what this algorithm excludes. The modern stack is: take
the easy checkpoint at a clean boundary, accept that a crash can land where it should not, and
make the effects idempotent so it does not matter. That is a weaker mechanism and a stronger
system, and it is a fair summary of forty years of engineering on top of a correct idea.

**Where you meet it next in Sutra.** Day 61 formalises checkpoints, and Day 65 kills a run at a
moment of its choosing — which is a test of whether Sutra's boundaries are the clean ones this
paper lets you recognise.

## Check yourself

```bash
cd days/day-60-durable-execution/lab/papers/distributed-snapshots
uv run python demo.py; echo "exit: $?"
uv run python demo.py --no-markers; echo "exit: $?"
```

Now open `snapshot.py` and disarm rule 3: change the last line of `start_snapshot` from
`self.logging_channel = use_markers` to `self.logging_channel = False`, so the process records
itself and the channels but never logs what arrives in between. Run the marker arm again — it
reports `in transit=0`, `total=5`, `IMPOSSIBLE (lost 1)`, and exits `1`. Rules 1 and 2 alone are
not the algorithm.

Then try the other edit: swap the two statements in `start_snapshot` so the marker is sent
*before* the state is recorded. Run it again and note that this trace still reports `consistent`
— then work out what A would have to do between those two statements for it to fail, and say why
the ordering is still wrong even though this run does not catch it.

**Out loud, without scrolling up:** what did this paper actually claim, and what do we do
differently now? A good answer names the changed goal — a state the system *could* have been in
rather than the state at an instant — and says that today's systems mostly avoid needing the
algorithm by checkpointing where nothing is in flight, and pay for that shortcut with idempotency.

**Next:** back to [the hub](../LESSON.md) for the build brief and the ledger.

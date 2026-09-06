---
day: 72
paper: "doi:10.1145/360248.360253"
title: "Ethernet: distributed packet switching for local computer networks"
ids: ["OPS-13"]
level: production
prerequisites: ["../parts/01-the-ladder/1.1-why-doubling.md"]
prev: "../parts/05-in-production/5.2-what-to-alert-on.md"
next: "../LESSON.md"
---

# Ethernet: distributed packet switching for local computer networks

> *Ethernet: distributed packet switching for local computer networks* · `doi:10.1145/360248.360253`
> · Communications of the ACM, Volume 19, Issue 7, pages 395–404, July 1976 ·
> <https://doi.org/10.1145/360248.360253>

> Record checked live on 2026-09-06 via `https://api.crossref.org/works/10.1145/360248.360253`. The
> journal, volume, issue, pages and year above are copied from that record. **The title is assembled
> from two fields** — the record carries `title: ["Ethernet"]` and
> `subtitle: ["distributed packet switching for local computer networks"]`, and a citation that
> silently merges them without saying so is a citation nobody can check. The record carries **no
> abstract**, and this document is explicit below about which claims come from the record, which come
> from the standard that followed it, and which are the field's shorthand rather than either.

## One-line answer

The idea this day is built on is not "wait longer each time" — it is **draw the wait at random from a
range that doubles after each collision**, and the randomness is not an improvement somebody added
later: switching the widening off in the demo below takes sixteen senders from **16 of 16 delivered
on 95 attempts** to **0 of 16 on 4,269 attempts**.

## The story

Four of you are on a call and the connection is not good — the kind where everything arrives about a
second late.

Someone finishes a sentence. You start to answer, and so does the person in the other office, and for
a moment you are both talking. You both stop. You both say *"sorry — go ahead"*. You both stop again.
Then, because you are both being polite in exactly the same way at exactly the same speed, you both
start again, and you are back where you began.

The fourth time it happens one of you does something slightly different: waits a beat longer than
feels natural, for no reason, unevenly. And that works. Not because the pause was longer, but because
it was *different from the other person's*.

Nobody could have fixed this by being more polite. Two people following the same rule at the same
instant will keep colliding for as long as the rule is the same. What broke the deadlock was
**disagreement about how long to wait**.

## The idea in plain language

The 1976 paper describes a local network in which many machines share one cable. There is no
scheduler, no token, no central allocator handing out turns. A machine that wants to send listens
first, and if the cable is quiet it transmits.

That gets you most of the way and leaves one hole that cannot be closed by listening harder: two
machines can hear the same silence and start in the same instant. Both signals are on the wire, both
packets are destroyed, and both senders now know it. This is a **collision**, and it is not a rare
edge case — it is the normal cost of letting everyone decide for themselves.

So the question the paper has to answer is: *what does a sender do after a collision?* There are
three answers and only the third works.

| Rule after a collision | What happens |
| --- | --- |
| retry immediately | the two senders collide again in the same instant, forever |
| retry after a fixed delay `d` | both wait `d`, both retry together, collide again, forever |
| retry after a random delay from a **widening** range | the senders disagree, and disagree more the worse it gets |

The first two fail for the same reason, and it is the reason from the story: **identical rules produce
identical behaviour, and identical behaviour is what caused the collision.** Determinism is the bug.

The third answer has two ingredients and both are load-bearing.

- **Randomness** breaks the tie. Two senders drawing from the same range will usually draw different
  numbers, so one goes first and the other finds the wire busy.
- **Doubling the range** makes it adaptive. With two senders contending, a narrow range is enough and
  recovery is quick. With fifty, a narrow range means fifty senders drawing from a handful of slots
  and colliding again — so each collision widens the range, and the network spreads itself out in
  proportion to how congested it actually is, without anybody measuring the congestion.

The second point is the one worth sitting with. **The doubling is not a punishment; it is an
estimator.** A sender that has collided six times has evidence that the channel is busy, and its own
collision count is the only evidence it has. Doubling the range is how it acts on that evidence.

**What this document claims about the source, and what it does not.** That the mechanism is
randomised retransmission whose interval widens with repeated collisions is what the paper is
universally cited for, and it is the substance of the section below. The precise formulation the
field now recites — *truncated binary exponential backoff*: draw uniformly from `[0, 2**k)` slots,
stop widening after ten collisions, abandon the frame after sixteen — is written out in the **IEEE
802.3** standard that followed, and this document attributes those constants there rather than
putting them in the paper's mouth. The Crossref record carries no abstract, so nothing here is a
paraphrase of one.

## Why Sutra needs it

Because of Principle 4, at the scale of a day. Section 1 built a ladder by hand and section 4
discovered a herd and fixed it with one multiplication. Reading the paper now — and not first —
reverses which of those two feels important, and the reversal is the lesson.

The day's ladder is `1, 2, 4, 8`: deterministic, with jitter arriving in part
[4.2](../parts/04-everyone-at-once/4.2-one-multiplication.md) as a fix for a problem the ladder
created. In the paper there is no such sequence. The wait was **random from the beginning**, because
the paper's whole setting is many senders sharing one resource, where a deterministic wait is
transparently useless.

So the honest reading is uncomfortable and worth saying plainly: **this day's ladder is a degraded
copy of the paper, and part 4.2 is not an enhancement but a restoration.** Every retry loop that
sleeps exactly `2**k` seconds has dropped the ingredient the mechanism was named for and kept the one
that is easier to implement.

That matters for `sutra/backoff.py` specifically. Addendum 02's providers meter per project, and Day
70 part 5.3 established that a Sutra worker pool is many senders sharing one quota — which is the
paper's setting, not the single-client setting section 1 measured in.

## The mechanism

The paper's contribution, written as code, is one function. Everything else in the demo exists to
make it observable.

```python
@dataclass
class Station:
    """One sender with a packet to get out."""

    name: int
    collisions: int = 0
    sent_at: int | None = None
    attempts: int = 0

    def backoff(self, rng: random.Random) -> int:
        """Slots to wait after a collision.

        Binary exponential backoff: pick uniformly from `[0, 2**k)` where `k` is the number of
        collisions so far. With `DOUBLE` off the range is fixed, so the pick never spreads out.
        """
        window = 2**self.collisions if DOUBLE else 2
        return rng.randrange(window)
```

**Line by line:**

- `collisions: int = 0` is the sender's entire model of the network. It does not know how many other
  stations exist, whether load is rising, or who it collided with. Its own collision count is the only
  signal available, and the mechanism's elegance is that this turns out to be enough.
- `window = 2**self.collisions` is the doubling: after one collision the range is `[0, 2)`, after
  three `[0, 8)`, after six `[0, 64)`. The **range** doubles, not the wait.
- `if DOUBLE else 2` is the ablation switch, and `2` rather than `1` is deliberate: a fixed range of
  `[0, 2)` still has randomness in it, so the run with doubling off is not a straw man that fails
  merely because it became deterministic. It fails with randomness present and only the widening
  removed, which isolates the paper's actual claim.
- `rng.randrange(window)` draws uniformly. Two stations that have collided the same number of times
  share a *range* and will still usually pick different numbers — the disagreement comes from the
  draw, and the widening only makes disagreement more likely as contention rises.

Now compare that with the ladder this day built:

```python
def ladder_wait(attempt: int) -> float:
    """The delay before attempt `attempt`, counting from 1."""
    return LADDER[min(attempt, len(LADDER)) - 1]
```

**Line by line:**

- No `rng` parameter, and that absence is the whole difference. `ladder_wait(3)` is `4.0` for every
  caller in the fleet, every time — precisely the condition part
  [4.1](../parts/04-everyone-at-once/4.1-the-herd.md) measured as six instants with forty requests in
  each.
- `min(attempt, len(LADDER))` is the truncation, and it is the one place where the day's ladder and
  the standard agree: both stop doubling rather than doubling forever. Part
  [1.3](../parts/01-the-ladder/1.3-the-last-rung.md) reached that by measuring where the doubling goes
  silly; 802.3 fixes it at ten.

The two functions describe the same shape, and only one of them is safe in a fleet.

## The paper in one demo

A shared wire, sixteen senders, and one switch that turns the widening off.

```text
lab/papers/binary-exponential-backoff/
├── channel.py   # the mechanism: Station.backoff, and a wire where two senders in one slot collide
└── demo.py      # sixteen stations, run with the doubling on or off
```

The rest of `channel.py` is the wire itself — `Station` is above, and the two one-line readers
`delivered()` and `last_delivery()` are omitted here because they only total up what `run` recorded:

```python
"""The paper's one idea: on a collision, double the range you pick your next wait from."""

from __future__ import annotations

import random
from dataclasses import dataclass, field

# The one switch. With doubling off, a station retries after a fixed random delay in a range that
# never grows - which is the state of every retry loop written as `sleep(1)` in a `while`.
DOUBLE = True

SLOTS = 400


@dataclass
class Channel:
    """A shared wire: one sender per slot succeeds, two or more collide."""

    stations: list[Station]
    collisions: int = 0
    log: list[tuple[int, int]] = field(default_factory=list)

    def run(self, seed: int = 11) -> None:
        rng = random.Random(seed)
        ready = {s.name: 0 for s in self.stations}
        by_name = {s.name: s for s in self.stations}
        for slot in range(SLOTS):
            due = [n for n, t in ready.items() if t == slot and by_name[n].sent_at is None]
            if not due:
                continue
            for n in due:
                by_name[n].attempts += 1
            if len(due) == 1:
                by_name[due[0]].sent_at = slot
                continue
            self.collisions += 1
            self.log.append((slot, len(due)))
            for n in due:
                station = by_name[n]
                station.collisions += 1
                ready[n] = slot + 1 + station.backoff(rng)
```

**Line by line:**

- `SLOTS = 400` is time. The paper's wire is continuous and this model is slotted, which is a
  simplification *When it breaks* is honest about; it costs realism and buys a model you can read in
  one screen.
- `ready = {s.name: 0 for s in self.stations}` starts every station at slot 0. All sixteen want to
  send in the same instant — the same starting gun as part 4.1's herd, and the condition the paper
  exists to survive.
- `due = [...]` is every station scheduled for this slot and not yet finished. Its **length** is the
  entire physics: one is a delivery, more than one is a collision.
- `by_name[n].attempts += 1` counts every transmission whether it lands or not, so the ablation's cost
  is measurable. Same accounting rule as the day's `Provider.attempts` — the wire counts what was
  sent, not what succeeded.
- `if len(due) == 1: ... sent_at = slot` — a lone sender gets through. Nothing else is needed for
  success; the wire has no capacity limit in this model, only an exclusivity rule.
- `station.collisions += 1` comes **before** `station.backoff(rng)`, so the widened range applies to
  the wait that follows this collision rather than to the one after it. Get that order wrong and the
  adaptation lags by one step while the demo still mostly works, which is why it is worth pointing at.
- `slot + 1 + station.backoff(rng)` — the `+ 1` is the floor: a station always waits at least until
  the next slot, so a backoff draw of `0` means *try again immediately after*, not *try again in the
  slot you just collided in*.

`demo.py` runs it and reports:

```python
"""Sixteen stations, one wire, with the doubling on and off."""

from __future__ import annotations

import sys

import channel
from channel import SLOTS, Channel, Station

STATIONS = 16


def main() -> int:
    if "--off" in sys.argv:
        channel.DOUBLE = False

    wire = Channel([Station(name=i) for i in range(STATIONS)])
    wire.run()

    print(f"doubling: {'ON' if channel.DOUBLE else 'OFF (ablation)'}")
    print(f"{STATIONS} stations, {SLOTS} slots, identical seed in both runs")
    print()
    print(f"  packets delivered       {wire.delivered()} of {STATIONS}")
    print(f"  collisions              {wire.collisions}")
    print(f"  transmit attempts       {sum(s.attempts for s in wire.stations)}")
    last = wire.last_delivery()
    print(f"  last delivery at slot   {last if last is not None else 'never'}")
    print()
    worst = max(wire.stations, key=lambda s: s.collisions)
    print(f"  the worst-hit station collided {worst.collisions} times")
    if wire.delivered() < STATIONS:
        missing = STATIONS - wire.delivered()
        print()
        print(f"  {missing} stations never got their packet out in {SLOTS} slots")
    return 0 if wire.delivered() == STATIONS else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

**Line by line:**

- `import channel` **as well as** `from channel import ...` is not redundant. `channel.DOUBLE = False`
  has to rebind the attribute on the module object; a `from channel import DOUBLE` would have copied
  the value at import time and the switch would silently do nothing.
- `Channel([Station(name=i) for i in range(STATIONS)])` builds a fresh wire per run, so no state leaks
  between the two invocations.
- `wire.run()` takes the default seed in both runs. Same stations, same slots, same random stream —
  the only difference between the two outputs below is the width of the range.
- `return 0 if wire.delivered() == STATIONS else 1` makes this an eval rather than a report (P11).
  "Every packet got out" is the claim, and the exit code is where it goes red.

The paper's claim, with the mechanism on:

```bash
cd days/day-72-backoff-with-honesty/lab/papers/binary-exponential-backoff
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- `cd` first: `demo.py` imports `channel` by plain name, so the working directory has to be the demo's
  own folder.
- `echo "exit: $?"` prints the exit code, because the claim *is* the exit code.

Measured on 2026-09-06:

```text
doubling: ON
16 stations, 400 slots, identical seed in both runs

  packets delivered       16 of 16
  collisions              17
  transmit attempts       95
  last delivery at slot   89

  the worst-hit station collided 7 times
exit: 0
```

Sixteen senders that all started in the same instant, on a wire that lets exactly one through at a
time, all got out — in 89 slots, having collided seventeen times between them. No coordinator, no
schedule, and no station knowing that any other station existed.

Now the ablation. Same everything, with the range fixed instead of widening:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` sets `channel.DOUBLE = False`. Randomness is still present — the fixed range is `[0, 2)` —
  so what is removed is *only* the widening.

Measured on 2026-09-06:

```text
doubling: OFF (ablation)
16 stations, 400 slots, identical seed in both runs

  packets delivered       0 of 16
  collisions              400
  transmit attempts       4269
  last delivery at slot   never

  the worst-hit station collided 278 times

  16 stations never got their packet out in 400 slots
exit: 1
```

**Zero of sixteen.** Not "slower" — nothing at all got through, for four hundred slots, at a cost of
4,269 transmissions against the 95 the working version needed. Every slot was a collision, because
sixteen stations drawing from two possible waits cannot avoid each other for long, and every failure
fed the next one.

| | Doubling on | Doubling off |
| --- | --- | --- |
| packets delivered | **16 of 16** | 0 of 16 |
| collisions | 17 | 400 |
| transmit attempts | 95 | 4,269 |
| last delivery | slot 89 | never |
| worst station's collisions | 7 | 278 |
| exit code | 0 | 1 |

That is the paper's contribution isolated: randomness alone is not enough, and the range has to widen
with the evidence. It is also the same finding as part
[4.1](../parts/04-everyone-at-once/4.1-the-herd.md) approached from the other side — there, forty
clients agreeing on a schedule produced four bursts of forty; here, sixteen stations with too little
room to disagree produced total collapse.

## When it breaks

**The widening is unfair, and the paper's setting hides it.** The station that has collided most has
the widest range, so it draws the longest waits, so it is most likely to collide again while a
newcomer with `k=0` goes straight through. Real Ethernet has a name for the pathological version —
the **capture effect**, where a station that has just transmitted successfully resets its counter and
repeatedly beats one that has been backing off. Backoff optimises for the channel, not for the
individual, and the individual it treats worst is the one already doing worst.

**The range cannot double forever**, which is why the standard truncates it. Unbounded, `2**k` reaches
waits nobody intended within twenty collisions — the same arithmetic part
[1.3](../parts/01-the-ladder/1.3-the-last-rung.md) ran on the day's own ladder, arriving at the same
conclusion from a completely different direction. Truncation is not a detail; a mechanism that doubles
without a ceiling has replaced a fast failure with a slow one.

**And this model is not Ethernet.** It has slots rather than continuous time, no propagation delay, no
carrier sense (a station here does not listen before sending), no minimum frame size, and no
abandonment after sixteen attempts. Each omission makes the demo smaller and none of them changes the
claim being tested, which is the standard the demo is held to — but a reader who takes this file as a
description of the protocol will be wrong about the protocol.

**Where the claim does not hold at all:** when the contending parties are not symmetric. Backoff
assumes every participant runs the same algorithm and defers when it loses. A participant that does
not back off wins everything, permanently, while the well-behaved ones back further and further out of
its way. That is a real limitation of the whole family, and it is why a shared resource with untrusted
users needs a server-side limiter rather than client-side politeness — Day 70's argument, in 1976's
terms.

## In production

**What survived: the mechanism, completely.** Exponential backoff with randomisation is in TCP's
retransmission timers, in DNS resolvers, in every major cloud provider's SDK retry policy, in HTTP
client libraries, and in the `sutra/backoff.py` this day asks you to write. It is one of the small
number of ideas from 1970s networking that a working engineer touches constantly without ever being
told where it came from. The demo above is fifty lines, and it is the same fifty lines in shape that
ship inside those libraries.

**What did not survive: the setting.** Nobody has run a shared-medium Ethernet in a data centre in a
very long time. Switched, full-duplex Ethernet gives every host its own collision domain, and the
collision — the entire problem the mechanism was invented for — simply does not occur. CSMA/CD is a
compatibility mode in modern hardware and is effectively never exercised. **The solution outlived its
problem by decades**, because the shape of the problem turned out to be general: any set of
independent actors contending for a resource they cannot coordinate over has exactly this structure,
and a rate-limited API is that, with the wire replaced by a quota.

**What the field changed on the way.** The paper's randomised retransmission became the standard's
truncated binary exponential backoff with fixed constants, and then — in the API-client world —
mutated again into the *full jitter* variant part
[4.2](../parts/04-everyone-at-once/4.2-one-multiplication.md) weighed, which draws from `[0, base]`
rather than scaling a deterministic delay. That last step is arguably a return to the original: the
paper's wait was a draw from a range, and the deterministic-ladder-plus-jitter formulation most code
uses today is the detour.

**The failure this history predicts, which you will meet.** A retry loop written as `sleep(2**k)` with
no randomness passes every test, because tests run one client. It fails only under contention, only in
production, and it fails in the direction of *making the contention worse*. That bug has been solvable
since 1976 and is written fresh every week, which is the strongest argument this curriculum can make
for reading the paper after building the thing rather than before.

**The review comment a senior engineer leaves:** *"Backoff without jitter isn't backoff, it's a
synchronised schedule. This is the oldest fix in networking — Ethernet, '76 — and the randomness was
the point rather than a refinement. Draw the wait from a range, widen the range on each failure, cap
the range, and give up at a fixed attempt count. If you want to see why, take the widening out and run
it with sixteen concurrent callers."*

**The interview question:** *"Where does exponential backoff come from, and what do people get wrong
about it?"* An honest answer: *"The 1976 Ethernet paper in CACM. Many machines share one cable, two
that transmit in the same instant destroy each other's packet, and there's no coordinator — so the
answer had to be something each sender could do alone. The mechanism is: wait a random number of
slots, drawn from a range that doubles with each successive collision. What people get wrong is which
half is essential. They keep the doubling and drop the randomness, because a deterministic
`sleep(2**k)` is easier to write and passes single-client tests. I ran the ablation: sixteen senders
with the widening removed but the randomness kept delivered nothing at all in four hundred slots and
burned four thousand transmissions, against ninety-five for the working version. Both ingredients are
load-bearing. The other thing worth knowing is that the setting is dead — switched Ethernet has no
collisions — and the mechanism outlived it, because 'independent actors contending for a resource they
can't coordinate over' describes a rate-limited API just as well as it described a wire."*

## Check yourself

```bash
cd days/day-72-backoff-with-honesty/lab/papers/binary-exponential-backoff
uv run python demo.py
uv run python demo.py --off
```

Then change `STATIONS` to `4` and run both again. Record the four numbers. The ablation does far
better with four stations than with sixteen — say why, in terms of how many distinct waits a range of
`[0, 2)` can produce, and at what station count you would expect it to collapse.

Now cap the widening: change `window` to `2 ** min(self.collisions, 4)` and run with sixteen again.
Report what happens to `last delivery at slot` and to the worst station's collision count, then say
which of those two numbers the IEEE truncation trades away and which it protects.

**Out loud, without scrolling up:** the ablation kept the randomness and removed only the widening,
and it delivered nothing. What does the widening do that a fixed random range cannot?

---

That is the day: the ladder, the header, the escalation, the herd and the alarm — and the 1976 paper
that had all of it, with one ingredient this day had to rediscover in section 4.

**Next:** [back to the hub](../LESSON.md).

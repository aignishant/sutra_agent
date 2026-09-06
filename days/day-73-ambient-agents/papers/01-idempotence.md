---
day: 73
paper: "doi:10.1145/2181796.2187821"
title: "Idempotence Is Not a Medical Condition"
ids: ["AG-24"]
level: production
prerequisites: ["../parts/02-when-it-dies-at-three-am/2.2-stages-you-can-iterate.md"]
prev: "../parts/05-in-production/5.2-what-a-real-ambient-system-adds.md"
next: "../LESSON.md"
---

# Idempotence Is Not a Medical Condition

> *Idempotence Is Not a Medical Condition: An essential property for reliable systems* ·
> `doi:10.1145/2181796.2187821` · Queue, Volume 10, Issue 4, pages 30–46, April 2012 ·
> <https://doi.org/10.1145/2181796.2187821>

> Record checked live on 2026-09-06 via `https://api.crossref.org/works/10.1145/2181796.2187821`.
> The journal, volume, issue, pages and year above are copied from that record. **The title is
> assembled from two fields** — the record carries
> `title: ["Idempotence Is Not a Medical Condition"]` and
> `subtitle: ["An essential property for reliable systems"]` — and a citation that merges them
> silently is one nobody can check (§17.4.1 rule 5). Unlike most records this one **does** carry an
> abstract, and the paragraph quoted below is from it verbatim rather than paraphrased.

## One-line answer

The property that makes every retried system possible is **idempotence** — applying an operation
twice leaves the same state as applying it once — and it is not a nicety: switching it off in the
demo below leaves a recorded total of **28** where the truth is **10**, with no error raised, nothing
lost, and nothing anywhere reporting a problem.

## The story

You are paying a bill on your phone, on a bad connection.

You press *pay*. The little circle turns. It keeps turning. Then the page gives up and shows you an
error that could mean anything: the payment never left, or it went through and the confirmation did
not come back.

So now you have to decide something you have no information about. Press it again and you might pay
twice. Do not press it, and the bill might still be unpaid — and you will find that out from a
reminder letter.

What you actually do is refresh, hunt through the transactions list, and try to work out from the
outside what happened on the inside. Which is a strange thing to have to do, and it happens because
one side of that conversation was built without an answer to *"what if this arrives twice?"*.

## The idea in plain language

Here is the paragraph the record itself carries, quoted rather than summarised:

> *"The definition of distributed computing can be confusing. Sometimes, it refers to a tightly
> coupled cluster of computers working together to look like one larger computer. More often,
> however, it refers to a bunch of loosely related applications chattering together without a lot of
> system-level support. This lack of support in distributed computing environments makes it difficult
> to write applications that work together. Messages sent between systems do not have crisp guarantees
> for delivery. They can get lost, and so, after a timeout, they are retried. The application on the
> other side of the communication may see multiple messages arrive where one was intended. These
> messages may be reordered and interleaved with different messages. Ensuring that the application
> behaves as intended can be very hard to design and implement. It is even harder to test."*

Read the third-from-last sentence again, because it is the whole thing: **the application on the
other side may see multiple messages arrive where one was intended.**

That is not a bug in the network and it is not something better engineering removes. It follows from
a fact with no way around it: a sender that gets no reply cannot tell *"the request never arrived"*
from *"the request arrived and the reply was lost"*. Those are the two states of your bill payment,
and from outside they look identical. The sender's only options are to retry — accepting that the
work might happen twice — or to give up, accepting that it might not have happened at all.

The industry's name for choosing the first option is **at-least-once delivery**: the system promises
your message will arrive, and admits it may arrive more than once. It is the default nearly
everywhere, because the alternative promise — *at-most-once* — is achieved by not retrying, which
means losing work whenever anything goes wrong.

**Idempotence** is what makes at-least-once survivable. An operation is idempotent when applying it
twice leaves the same state as applying it once. Given that, duplicates stop being a problem to
detect and become a thing you can simply ignore.

And the practical test for whether an operation has the property is short: **does it name the result,
or does it name a change?**

| Operation | Names | Applied twice |
| --- | --- | --- |
| *"set the total for ticket 4610 to 3"* | the result | still 3 |
| *"add 3 to the total for ticket 4610"* | a change | 6 |
| *"rebuild the index from the archive"* | the result | the same index |
| *"append a line to the run log"* | a change | two lines |

A change has no memory of having been applied. That is the entire failure, and it is why the demo
below can go so badly wrong while every individual step is doing exactly what it was told.

## Why Sutra needs it

Because this day quietly relied on the property four times before naming it.

Part [2.2](../parts/02-when-it-dies-at-three-am/2.2-stages-you-can-iterate.md)'s resume re-runs
whichever stages did not finish. Part [2.1](../parts/02-when-it-dies-at-three-am/2.1-the-run-that-dies.md)
noted that an operator will re-run a bad night by hand. Part
[2.4](../parts/02-when-it-dies-at-three-am/2.4-the-lock-nobody-released.md) ended by observing that if
the stages were safe to run twice, the lock would be an optimisation rather than a correctness
requirement. And part [4.1](../parts/04-what-wakes-it/4.1-what-adk-offers.md) found that an
event-driven trigger delivers at-least-once, which is this paper's premise arriving through the front
door.

Every one of those is the same assumption: **a stage may be applied an unknown number of times.** It
happens to hold for the nightly job, and it holds by luck rather than by design unless somebody
checks. So check:

| Stage | Idempotent? | Why |
| --- | --- | --- |
| `reindex` | yes | it is a pure function of `ARCHIVE` and writes a full replacement |
| `run_evals` | yes | it recomputes every case from the index and writes a full replacement |
| `write_digest` | yes | it writes the whole file from the eval scores |
| `append_run` | **no**, deliberately | a run log that dropped duplicates could not record two runs |

The last row is the important one. Idempotence is not a virtue to apply everywhere — the run log is
*supposed* to accumulate, because part
[3.1](../parts/03-the-morning-after/3.1-the-run-log.md)'s whole argument is that history is a fact
rather than a summary. What matters is knowing which of your operations is which, and the way to find
out is to ask each one whether it names a result or a change.

## The mechanism

The paper's property, written as the smallest code that has it and can lose it:

```python
    def apply(self, key: str, amount: int) -> None:
        """Record `amount` for `key`.

        Idempotent form: assign. Applying it twice with the same arguments leaves the same state,
        because the operation names the *result* rather than a change to it.

        Non-idempotent form: accumulate. Applying it twice doubles the effect, because the operation
        names a delta and a delta has no memory of having been applied.
        """
        self.appends.append((key, amount))
        if IDEMPOTENT:
            self.rows[key] = amount
        else:
            self.rows[key] = self.rows.get(key, 0) + amount
```

**Line by line:**

- `self.appends.append((key, amount))` runs on **both** branches and records every write, including
  the duplicated ones. That is what lets the demo report *writes attempted* separately from *distinct
  keys*: the duplicates genuinely happened, and the question is only whether they left a mark.
- `self.rows[key] = amount` is the idempotent form. It is an **assignment**, and an assignment is
  idempotent for the same reason the table above gives — it names the state you want, so repeating it
  is a no-op.
- `self.rows[key] = self.rows.get(key, 0) + amount` is one `+` different and it is the entire
  ablation. It reads the current value and adds to it, which makes the outcome depend on how many
  times it has run.
- Neither branch is wrong in isolation. The accumulate form is exactly what you want for a counter
  that is incremented once per real event. It becomes a bug the moment the same event can be
  delivered twice — which is the paper's premise, not an unusual case.

## The paper in one demo

Two files. One night's work, applied the way a scheduler and an operator actually apply it.

```text
lab/papers/idempotence/
├── ledger.py   # the property: apply() assigns, or accumulates when the switch is off
└── demo.py     # the retried operation stream, with the property on and off
```

`ledger.py` in full:

```python
"""The paper's one idea: an operation you can apply twice and get the same state."""

from __future__ import annotations

from dataclasses import dataclass, field

# The one switch. With idempotence off, `apply` appends instead of setting, which is what almost
# every "record what happened" implementation does by default.
IDEMPOTENT = True


@dataclass
class Ledger:
    """What the job has recorded so far.

    Attributes:
        rows: the recorded facts, keyed by the id of the thing they are about.
        appends: every write, in order, including the ones that duplicated an existing fact.
    """

    rows: dict[str, int] = field(default_factory=dict)
    appends: list[tuple[str, int]] = field(default_factory=list)

    def apply(self, key: str, amount: int) -> None:
        """Record `amount` for `key`."""
        self.appends.append((key, amount))
        if IDEMPOTENT:
            self.rows[key] = amount
        else:
            self.rows[key] = self.rows.get(key, 0) + amount

    def total(self) -> int:
        return sum(self.rows.values())
```

**Line by line:**

- `IDEMPOTENT = True` is a module-level flag rather than a constructor argument so that `demo.py` can
  flip it from the command line without the `Ledger` having to know a switch exists. The mechanism
  under test stays clean.
- `rows` is the state anybody would read afterwards; `appends` is the audit trail of what was
  attempted. Keeping both is what makes the ablation legible — without `appends`, a run that applied
  eight operations and a run that applied three would be indistinguishable from the outside.
- `field(default_factory=dict)` is how a dataclass gives each instance its own container. A bare
  `= {}` would share one dictionary between every `Ledger` ever created, which is a different bug and
  a famous one.
- `total()` is the number the demo compares against the truth. It is deliberately the crudest possible
  summary, because the point is that a wrong total is all you would ever see.

`demo.py` in full:

```python
"""One night's work, retried the way a scheduler retries it, with the property on and off."""

from __future__ import annotations

import sys

import ledger
from ledger import Ledger

# What the job records: three tickets and how many index rows each produced. The truth is 3 + 5 + 2.
WORK = [("ticket:4610", 3), ("ticket:4633", 5), ("ticket:4652", 2)]

# The stream as it actually happens. The first run dies after two operations; the resume redoes the
# whole night because it has no record of where it stopped; then an operator runs it once more.
STREAM = WORK[:2] + WORK + WORK
TRUTH = sum(amount for _key, amount in WORK)


def main() -> int:
    if "--off" in sys.argv:
        ledger.IDEMPOTENT = False

    book = Ledger()
    for key, amount in STREAM:
        book.apply(key, amount)

    print(f"idempotent: {'ON' if ledger.IDEMPOTENT else 'OFF (ablation)'}")
    print(f"{len(STREAM)} operations applied, covering {len(WORK)} distinct facts")
    print()
    print(f"  writes attempted    {len(book.appends)}")
    print(f"  distinct keys       {len(book.rows)}")
    print(f"  recorded total      {book.total()}")
    print(f"  the truth           {TRUTH}")
    print()
    for key, value in book.rows.items():
        want = dict(WORK)[key]
        mark = "" if value == want else f"   <- should be {want}"
        print(f"    {key:<14} {value}{mark}")
    print()
    correct = book.total() == TRUTH
    if correct:
        print("  Applying an operation three times left the same state as applying it once.")
    else:
        print("  Nothing errored and nothing was lost. The number is simply wrong, by exactly")
        print("  the number of times the job was retried.")
    return 0 if correct else 1


if __name__ == "__main__":
    raise SystemExit(main())
```

**Line by line:**

- `STREAM = WORK[:2] + WORK + WORK` is the honest part of this demo and deserves reading slowly. It is
  not an adversarial sequence; it is exactly the three things this day already established happen: a
  run that died part-way (`WORK[:2]`), a re-run that starts from the beginning because it did not know
  where it stopped (`WORK`), and an operator running it once more by hand (`WORK`). Eight operations
  covering three facts.
- `import ledger` **as well as** `from ledger import Ledger` is required, not redundant.
  `ledger.IDEMPOTENT = False` must rebind the attribute on the module object; a
  `from ledger import IDEMPOTENT` would copy the value and the switch would silently do nothing.
- `TRUTH = sum(...)` is computed from `WORK`, not written down as `10`, so the demo cannot drift out of
  agreement with itself if somebody edits the work list.
- `mark = "" if value == want else f"   <- should be {want}"` annotates each wrong row inline. A total
  that is wrong tells you something failed; a per-row comparison tells you *how* it failed, and the
  pattern in the ablation's output is the argument.
- `return 0 if correct else 1` makes this an eval rather than a report (Principle 11). The claim is
  "the state is right", and the exit code is where it goes red.

The property on:

```bash
cd days/day-73-ambient-agents/lab/papers/idempotence
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- `cd` first: `demo.py` imports `ledger` by plain name, so the working directory has to be the demo's
  own folder.
- `echo "exit: $?"` prints the exit code, because the claim *is* the exit code.

Measured on 2026-09-06:

```text
idempotent: ON
8 operations applied, covering 3 distinct facts

  writes attempted    8
  distinct keys       3
  recorded total      10
  the truth           10

    ticket:4610    3
    ticket:4633    5
    ticket:4652    2

  Applying an operation three times left the same state as applying it once.
exit: 0
```

Eight writes, three facts, and a total that matches the truth. Nothing deduplicated anything; the
duplicates all landed, and they simply did not matter.

Now the ablation — the same eight operations, in the same order, with `apply` naming a change instead
of a result:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` sets `ledger.IDEMPOTENT = False`. Nothing else changes: same stream, same order, same
  arguments.

Measured on 2026-09-06:

```text
idempotent: OFF (ablation)
8 operations applied, covering 3 distinct facts

  writes attempted    8
  distinct keys       3
  recorded total      28
  the truth           10

    ticket:4610    9   <- should be 3
    ticket:4633    15   <- should be 5
    ticket:4652    4   <- should be 2

  Nothing errored and nothing was lost. The number is simply wrong, by exactly
  the number of times the job was retried.
```

**28 against 10**, and look at the shape of the error. `ticket:4610` was applied three times and is
three times too big. `ticket:4652` was applied twice and is twice too big. The corruption is not
random; it is a faithful record of the retry history, which is exactly what you get when an operation
remembers being applied by accumulating.

| | Idempotent | Ablation |
| --- | --- | --- |
| writes attempted | 8 | 8 |
| distinct keys | 3 | 3 |
| recorded total | **10** | 28 |
| the truth | 10 | 10 |
| errors raised | none | none |
| exit code | 0 | 1 |

The row that matters most is **errors raised: none, in both runs**. Nothing was lost, nothing timed
out, nothing threw. Every individual operation did precisely what it was asked. The state is simply
wrong, and the only thing that could have detected it is a comparison against a truth you would not
normally have.

## When it breaks

**Idempotent is not the same as commutative, and the paper's premise includes reordering.** The
abstract says messages "may be reordered and interleaved". An assignment is idempotent, but two
*different* assignments to the same key are order-dependent: `set x = 3` then `set x = 5` leaves 5,
and the same two messages arriving in the other order leave 3, with both runs perfectly idempotent
and one of them wrong. Idempotence protects you from duplicates. It does nothing about order, and
systems that need both usually attach a version or a sequence number and ignore anything older than
what they already have.

**"Applied twice" needs a definition of *the same operation*.** In the demo it is easy, because the
key and the amount are both in the message. In the general case *"charge this customer £40"* twice is
either one retried payment or two genuine purchases, and no amount of care on the receiving side can
tell them apart from the message alone. This is why the practical mechanism is an **idempotency key**:
the sender generates a unique id for the *intent*, sends it with every retry of that intent, and the
receiver keeps a record of the ids it has already applied. That converts a non-idempotent operation
into an idempotent one at the cost of a store you now have to keep, prune and reason about.

**And it only covers what is in your store.** The nightly job's stages are idempotent because their
effects are files it owns. Send an email, post to a webhook, or move money, and re-running the stage
re-does the effect no matter how carefully your own state is assigned rather than accumulated. Part
[1.1](../parts/01-the-agent-nobody-watches/1.1-nobody-is-watching.md) argued that an ambient job which
only reads and writes its own files is safe to get wrong; this is the technical version of that
argument, and it is why "may this job act on the outside world" is a different review from "is this
job correct".

**The claim's real limit is testing, and the abstract says so itself:** *"It is even harder to test."*
A duplicate delivery is not a state your tests reach unless you deliberately construct it. The
`STREAM` line in the demo exists precisely because the interesting stream never occurs by accident —
and a test suite that never applies an operation twice will pass on both branches of `apply`.

## In production

**What survived: all of it, and the vocabulary most of all.** Idempotency keys are a documented,
first-class feature of every serious payment and messaging API; at-least-once is the default delivery
guarantee of the common queues and event buses; and "is this handler idempotent?" is a question asked
in ordinary code review rather than by specialists. The word in this document's title is now something
a working engineer is expected to know, which is a fair measure of an essay that set out to teach it.

**What did not survive: exactly-once, as anything but a phrase.** Systems that advertise it are
almost always doing at-least-once delivery plus deduplication at the receiver — which is idempotence
with a store attached, sold as a stronger guarantee than it is. Knowing that the strong-sounding
promise is built out of the weak one plus your own care is the difference between using such a system
and being surprised by it.

**What the field did not take up.** The essay argues for designing the property in at the application
level, where the code knows what an operation *means*. Much of the industry instead bolts a
deduplication layer underneath and hopes, which works until two messages are the same at the transport
level and different in intent, or the same in intent and different in bytes. The gap between "the same
message" and "the same operation" is where deduplication layers leak, and it is exactly the gap the
essay was pointing at.

**What a professional does with this on a nightly job.** Goes through the stages one at a time and
labels each *result* or *change* — the table in *Why Sutra needs it* is that exercise done for this
job. It takes very little time and it is the only way to find out that resume, the lock, the operator
re-run and the event trigger have all been relying on the same unstated property.

**The review comment a senior engineer leaves:** *"Before we schedule this: which of these stages is
safe to run twice? Write the answer next to each one. Re-index and evals look fine — they're pure
functions of their input and they write full replacements — but I want it stated, because the resume
logic and the operator re-running a bad night both depend on it and neither of them says so. The run
log is the exception and that's correct; just make sure nothing 'helpfully' deduplicates it later. And
if a stage ever starts sending anything outside this box, that's a different conversation, because
idempotent-in-our-store isn't idempotent-in-the-world."*

**The interview question:** *"What does idempotent mean and why do you care?"* An honest answer:
*"Applying an operation twice leaves the same state as applying it once. I care because retries are
unavoidable — a sender that gets no reply can't tell 'it never arrived' from 'it arrived and the reply
was lost', so the only safe assumption is at-least-once delivery, where your handler may see the same
thing more than once. The quick test is whether the operation names a result or a change: 'set the
total to 3' is idempotent, 'add 3 to the total' isn't, because a delta has no memory of having been
applied. I measured it on a retried nightly job — eight operations covering three facts, which is just
a run that died, a resume, and an operator re-running it. With assignment the total was 10, which is
the truth. With accumulation it was 28, no exception raised, nothing lost, and each row wrong by
exactly the number of times it had been retried. The caveats I'd raise are that idempotence doesn't
give you ordering, that 'the same operation' needs an idempotency key once the message alone can't
tell a retry from a genuine second request, and that it only covers state you own — re-running a stage
that sends an email sends the email again."*

## Check yourself

```bash
cd days/day-73-ambient-agents/lab/papers/idempotence
uv run python demo.py
uv run python demo.py --off
```

Change `STREAM` to `WORK` alone — one clean run, no retries — and run both again. Both pass. Say in
one sentence why that is the most dangerous property of this whole class of bug, and what it implies
about the test suite you would have written.

Then take the four stages in the *Why Sutra needs it* table and do the same exercise for something you
have actually built: list its operations and label each one *result* or *change*. If any of them is a
change that could arrive twice, write down what its idempotency key would be.

**Out loud, without scrolling up:** the ablation raised no errors and lost no data. What exactly went
wrong, and what would have had to exist for anyone to notice?

---

That is the day. An agent nobody is watching, a run that dies, a lock that outlives it, a digest that
reassures, a silence nobody hears — and the 2012 essay naming the one property all of it was quietly
standing on.

**Next:** [back to the hub](../LESSON.md).

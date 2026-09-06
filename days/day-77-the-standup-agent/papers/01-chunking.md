---
day: 77
paper: "doi:10.1037/h0043158"
title: "The magical number seven, plus or minus two: Some limits on our capacity for processing information."
ids: ["AG-25"]
level: production
prerequisites: ["../parts/02-the-order-is-the-product/2.3-words-before-it-matters.md"]
prev: "../parts/04-in-production/4.3-what-a-real-one-adds.md"
next: "../LESSON.md"
---

# The magical number seven, plus or minus two

> *The magical number seven, plus or minus two: Some limits on our capacity for processing
> information.* · `doi:10.1037/h0043158` · Psychological Review, Volume 63, Issue 2, pages 81–97 ·
> American Psychological Association · <https://doi.org/10.1037/h0043158>

> Record checked live on 2026-09-06 via `https://api.crossref.org/works/10.1037/h0043158`. The
> title, journal, volume, issue, pages and publisher above are copied from that record. **The
> record's `published-print` field is empty**; its `issued` and `published` fields both give
> **March 1956**, and that is where the year in this document comes from — said out loud because a
> citation that quietly picks a field is a citation nobody can check (§17.4.1). The record carries
> **no abstract**, and this document has not read the full text: what it states about the result is
> the form in which the field carries it, and the section below says so plainly.

## One-line answer

A listener cannot hold a long list, and the useful part of that is not the limit — it is what the
limit is **measured in**. It is not information and not words; it is **units**, and how much
information you put inside each unit is up to you. Twelve ticket references are twelve units and
nobody keeps them; *"two needing you, then four sign-in, four billing, four export"* is **4 units**
carrying the same twelve tickets.

## The story

You are at a counter and somebody reads you a reference number.

*"Four six eight five five two one seven."* Eight digits, said at a normal speed, and by the time
they finish you have lost the middle. So you ask them to say it again, and this time — without
anybody teaching you to — they say it differently: *"Four six eight … five five … two one seven."*

Same eight digits. Same speed. And now you have it, because you are no longer holding eight things.
You are holding three: a four-six-eight, a double five, and a two-one-seven.

Nobody made the number shorter. Somebody made it into fewer pieces.

## The idea in plain language

The number in the title is the one everybody remembers, and it is the less useful half of the paper.
The useful half is the unit.

**What the field takes from this paper**, and this document is careful to present it as that rather
than as a quotation: that the amount a person can hold in mind at once is small and roughly fixed —
around seven items, give or take — and, more importantly, that the limit applies to **chunks** rather
than to information. Recode the same information into fewer, larger chunks and more of it fits,
because the constraint was never on how much you were carrying. It was on how many separate things
you were carrying it in.

That distinction is the whole reason this paper belongs at the end of a day about a spoken report.

A standup is a list of things said to somebody who is holding them in their head, because on a voice
channel there is nowhere else to hold them. Day 74's paper established that a wait past a threshold
loses a listener's attention; this one establishes that even a listener who is paying complete
attention has a bounded number of slots. Both are limits you are designing against whether or not you
know it.

And the move the paper offers is not compression. Nothing is thrown away:

| The same twelve tickets | Units the listener holds | Information lost |
| --- | --- | --- |
| "4610, 4633, 4652, 4671, 4688 …" | twelve | none, and none retained either |
| "two needing you, four sign-in, four billing, four export" | four | the individual references |

The second row does lose the references — but it was never going to keep them, and it gains something
the first does not have: a *shape*. The listener now knows the queue is evenly spread and that two
things are theirs, which is a fact about the queue that no individual ticket contains.

## Why Sutra needs it

Because this day has been arguing about order and never once about *length*, and that gap needs
naming. Part [2.3](../parts/02-the-order-is-the-product/2.3-words-before-it-matters.md) was explicit
that shorter is not the goal — earlier is — and that is right as far as it goes. This paper is the
other constraint: even a perfectly ordered report has a point past which the listener is no longer
accumulating, only hearing.

It also explains something in the lab that would otherwise look like a stylistic choice. The
attention-first standup says *"The queue is 4 sign-in, 4 billing, 4 export, 12 open in total"* rather
than reading out twelve references. That one sentence is a recoding — four units where there could
have been twelve — and it is the reason the whole standup fits in five sentences without omitting
anything a listener could have kept.

## The mechanism

The paper's idea, written as code, is a function that turns items into units:

```python
def chunks(items: list[tuple[str, str, bool]]) -> list[str]:
    """Turn `(ref, category, needs_person)` rows into the units a listener has to hold."""
    if not CHUNKED:
        return [f"{ref} ({category})" for ref, category, _ in items]
    units: list[str] = []
    blocked = [ref for ref, _, needs in items if needs]
    if blocked:
        units.append(f"{len(blocked)} needing you: {', '.join(blocked)}")
    counts = Counter(category for _, category, _ in items)
    units += [f"{n} {category}" for category, n in counts.items()]
    return units
```

**Line by line:**

- The `if not CHUNKED` branch is one unit per item, which is what a report generated straight from a
  list looks like. It is not a straw man — it is the default output of every loop over a collection.
- `blocked` is recoded **first**, and into a single unit that names the references inside it. That is
  the paper's move applied where it matters most: two references inside one unit are two references
  the listener might actually keep, because they are attached to a reason to keep them.
- `Counter(category for ...)` collapses twelve rows into three counts. Nothing is discarded from the
  input; the individual references simply stop being separate units.
- The function returns a list of strings, so "how many units" is `len(...)` rather than a judgement.
  That is the only reason this is measurable at all — and it is worth saying that counting units in a
  *report* is a very different thing from measuring what a person retains.

## The paper in one demo

Twelve tickets, reported as twelve units and as four.

```text
lab/papers/chunking/
├── report.py   # the recoding, the budget, and the one switch
└── demo.py     # twelve tickets, run both ways
```

The budget, from `report.py`:

```python
# The number of units this demo treats as the budget. The figure the paper is known for is seven
# plus or minus two, and the lower end is the honest one to design against for something heard once,
# in the morning, by somebody who is also making tea.
LIMIT = 5
```

**Line by line:**

- `LIMIT = 5` is a **design choice made from a cited range**, not a measurement, and the comment says
  so. Taking the bottom of "seven plus or minus two" is a judgement about the situation — heard once,
  no chance to re-read, a listener doing something else — and a reader who disagrees should change it
  and re-run rather than argue with this page.
- Putting the budget in the module rather than in the demo means the report knows what it is being
  measured against, which is the same argument part 2.1 makes about the ordering living in one place.

With the recoding on:

```bash
cd days/day-77-the-standup-agent/lab/papers/chunking
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- `cd` first: `demo.py` imports `report` by plain name, so the working directory has to be the demo's
  own folder.
- `echo "exit: $?"` prints the exit code, because the claim is the exit code — the report fits inside
  the budget, or it does not.

Measured on 2026-09-06:

```text
chunking: ON
12 tickets, budget of 5 units

    2 needing you: 4688, 4740
    4 sign-in
    4 billing
    4 export

  units the listener has to hold   4
  the budget                       5
  tickets covered                  12

  The same twelve tickets, inside the budget. Nothing was left out - the items were
  recoded into fewer units, and each unit now carries more than one ticket.
exit: 0
```

Now the same tickets, one unit each:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` sets `report.CHUNKED = False`. The tickets, the budget and the categories are untouched.

Measured on 2026-09-06:

```text
chunking: OFF (ablation)
12 tickets, budget of 5 units

    4610 (sign-in)
    4633 (billing)
    4652 (export)
    4671 (sign-in)
    4688 (billing)
    4700 (billing)
    4712 (export)
    4718 (sign-in)
    4726 (export)
    4731 (billing)
    4740 (sign-in)
    4744 (export)

  units the listener has to hold   12
  the budget                       5
  tickets covered                  12

  7 units over the budget, and every one of them is a ticket reference nobody
  will remember. Nothing is missing and nothing is wrong. It simply does not fit.
```

| | recoded | one unit per ticket |
| --- | --- | --- |
| units the listener holds | **4** | 12 |
| the budget | 5 | 5 |
| tickets covered | 12 | 12 |
| anything omitted | no | no |
| exit code | 0 | 1 |

**The third and fourth rows are the argument.** Twelve tickets in both. Nothing omitted in either. The
ablation is not a worse report because it left something out — it is a worse report because it asks
the listener for three times the budget, and a listener who cannot hold twelve units does not hold the
first five and drop the rest in a tidy way. They hold a couple and a general impression.

**And look at what the recoded version bought with its first unit.** *"2 needing you: 4688, 4740"* is
one unit containing two references and the reason they are together. That is the paper's claim used
deliberately rather than accidentally: the references survive **because** they are inside a unit that
means something, not despite it.

## When it breaks

**This demo counts units in a report; it does not measure a person.** No human was involved, nothing
was recalled, and the exit code is a statement about the report's structure against a number this
curriculum chose. That is a real demonstration of the *recoding*, which is the paper's mechanism, and
it is not evidence about anybody's memory. A document that let the exit code imply otherwise would be
doing the thing Principle 10 forbids.

**Chunking has a cost, and the demo does not show it.** Recoding into categories throws the
references away for eleven of the twelve tickets. If the listener needed a specific reference, the
recoded report has failed them and the flat one has not — it has merely failed them slowly. What makes
the recoding right *here* is that the standup's job is to hand over decisions rather than data, which
is a fact about this report and not about reports.

**"Seven plus or minus two" is a number the field repeats more confidently than it should.** It is
widely cited, widely qualified, and the subject of a long literature arguing for smaller figures and
for the limit depending heavily on the material. This document uses it the way the lab does: as a
reason to design against a small number rather than as a constant. Anybody putting a specific figure
into a specification should read the arguments rather than this page.

**And the honest limit on the whole document:** the record has no abstract and the full text was not
read. The two claims used here — that immediate capacity is small and fixed, and that it is measured
in chunks so recoding increases what fits — are how the result is universally cited. The paper also
covers material this document does not touch at all, and a reader who needs the experiments, the
figures or the paper's own hedges must read it.

## In production

**What survived: the word "chunk", and the design instinct.** The term is now ordinary vocabulary well
outside psychology, and the practice — group before you list, name the group, put the count on the
group — is in every style guide for writing something that will be heard or skimmed. Very few people
applying it could name the paper.

**What did not survive: the number, as a number.** Seven is quoted in interface guidelines and has
been argued down, qualified and contextualised for decades. Treating it as a constant is the common
misuse, and the useful reading — the limit is on units, so choose your units — is the part that has
held up.

**What this changes about building a spoken report.** It gives you a lever that is not "say less". A
standup that must cover twelve tickets can either say twelve things or say four things that account
for twelve, and only the second is available to a listener. That is a different move from cutting
scope, and it is the one to reach for first, because cutting scope is a decision about what matters
and recoding is not.

**What a professional does with a report that has grown.** Counts its units, not its words. A report
that has acquired a section every quarter is a report whose unit count has been rising while every
individual addition looked small — the same slope Day 76 part 4.1 described for a metric nobody
graphs. Units are countable, cheaply, by anyone, at any time.

**The review comment a senior engineer leaves:** *"Count the units in this, not the sentences. Twelve
references is twelve things to hold and nobody holds twelve — group them and put the count on the
group, and keep the two that need a decision named individually, because those are the ones worth a
slot. And don't quote seven at me as though it were a limit we measured; use it as a reason to keep
this to a handful and let somebody ask for the detail."*

**The interview question:** *"How do you decide how much to put in a spoken summary?"* An honest
answer: *"Not by length — by how many separate things the listener has to hold. That's the useful
half of the 1956 result everybody quotes for 'seven plus or minus two': the limit isn't on
information, it's on chunks, so the same information recoded into fewer, larger chunks fits when the
raw version doesn't. Concretely, twelve ticket references is twelve units and nobody keeps them; 'two
needing you, then four sign-in, four billing, four export' is four units carrying the same twelve,
and it adds a shape the individual tickets never had. The move is recoding rather than cutting, which
matters because cutting is a decision about what's important and recoding isn't. The caveats I'd
state are that seven is quoted far more confidently than the literature supports, and that chunking
genuinely throws away the individual references — which is right for a report whose job is handing
over decisions, and wrong for one whose job is handing over data."*

## Check yourself

```bash
cd days/day-77-the-standup-agent/lab/papers/chunking
uv run python demo.py
uv run python demo.py --off
```

Change `LIMIT` to `9` — the top of the cited range — and run the ablation again. It still fails. Say
by how much, and then say what that tells you about whether the argument in this document depends on
which end of the range you picked.

Then take the standup from part 2.3 and count *its* units rather than its words. Compare that count
with the one this demo reports, and explain the difference: they are reports of the same queue and
they do not have the same number of units.

**Out loud, without scrolling up:** the ablation omitted nothing and covered every ticket. In what
sense was it a worse report?

---

That is the day, and the phase's second half. The nightly job runs while nobody is watching; the
standup is said to somebody who is, and this day found that its correctness was never the question —
what needed a decision had to be **first**, because a listener stops it when they like, and it had to
arrive in few enough pieces to be held.

**Next:** [back to the hub](../LESSON.md).

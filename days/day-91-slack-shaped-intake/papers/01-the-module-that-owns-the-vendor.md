---
day: 91
paper: "doi:10.1145/361598.361623"
title: "The module that owns the vendor"
ids: ["AG-30"]
level: production
prerequisites: ["../parts/01-what-an-integration-is/1.1-somebody-elses-shape.md"]
prev: "../parts/05-in-production/5.2-what-a-real-integration-layer-adds.md"
next: "../LESSON.md"
---

# Paper 01 — The module that owns the vendor

> **On the criteria to be used in decomposing systems into modules**
> Communications of the ACM, volume 15, issue 12, 1972, pp. 1053–1058.
> `doi:10.1145/361598.361623`
>
> The contribution: modules should be chosen around **design decisions that are likely to change**,
> and each such decision should be hidden inside one module. The obvious alternative — a module per
> step of the processing flowchart — spreads every changeable decision across all of them.

## One-line answer

The question "what are the modules?" has an answer that is not the sequence of things that happen,
and the difference shows up as a number: when a vendor renames four fields, the flowchart
decomposition needs four modules edited and the decision-hiding one needs one.

## The story

The kitchen where everyone can reach the salt.

A small restaurant kitchen, laid out by watching the work: chopping here, then the pans, then
plating, then the pass. It is a sensible layout and it matches what actually happens, in order.

The salt is on a shelf everyone can reach, because everyone uses it. So is the oil, and the box of
spare containers, and the roll of tape for labelling.

Then the supplier changes the containers — same food, slightly different lid. And it turns out that
four stations had learned the old lid: the one that portions, the one that stacks, the one that
labels, and the one that loads the trolley. Nothing was written down anywhere about lids. Four
people had simply absorbed the shape of the thing, because the thing was within reach.

The layout was correct about the order of the work and silent about who knew what.

## The idea in plain language

The paper takes one small program and decomposes it twice.

The first decomposition is by processing step: the modules are the stages the data passes through,
in order. This is what a flowchart gives you, and the paper's word for the criterion is that it
follows the *sequence of events in processing*.

The second is by hidden decision: each module is built around one thing that might change — a data
representation, an input format, an algorithm choice — and no other module is allowed to know it.

Both work. Both produce the same output. The paper's argument is about what happens when something
changes, and it is entirely about the *second-order* property: not how the system runs, but how it
is modified.

Two ideas do the work.

**A module is an assignment of responsibility, not a subprogram.** It is a decision about who knows
what, and it happens to be implemented as code. A decomposition is therefore a distribution of
knowledge, and the question to ask about any boundary is "what does this side know that the other
side does not?"

**The changeable decisions have to be enumerated first.** You cannot hide a decision you have not
identified, so the method starts with a list — what about this system is likely to change? — and the
modules follow from it. Skipping the list is why the flowchart decomposition feels natural: it needs
no such judgement, because a flowchart is already in front of you.

The phrase that came out of this — *information hiding* — has drifted in common use towards "make
fields private", which is a much smaller idea and misses the point. Hiding a field is
encapsulation. Hiding *the decision that a vendor calls the sender `user` and might one day call it
`author.id`* is what the paper is about, and no access modifier expresses it.

## Why Sutra needs it

Because Phase 14 connects this repository to systems it does not control, and every one of them owns
decisions that will change without notice. The survey in part
[1.2](../parts/01-what-an-integration-is/1.2-the-ways-in.md) lists ten such systems.

And because the flowchart decomposition is *specifically* seductive for an intake. The processing
really is a sequence — receive, verify, parse, decide, act — and each step really is a good unit of
work. It reads well, it tests well, and it distributes the vendor's payload shape across every
module that touches it.

## The mechanism

The paper's method, written out as the steps rather than as its conclusion:

**One: list the decisions likely to change.** Not everything — the things with a history of
changing, or an owner who is not you. For an intake: the vendor's payload shape, the signature
scheme, the transport, and which desk skill a message routes to.

**Two: give each one a module whose purpose is to contain it.** The module's interface is expressed
in terms that survive the change. `Message` has `sender`, `words`, `place` and `at` — four things the
desk needs — and none of the vendor's vocabulary.

**Three: check that no other module knows it.** This is the step that gets skipped, and it is the
only one that can be automated. If the decision has leaked, the decomposition has silently reverted
to the first kind.

The paper is explicit that step three is where decompositions decay: a boundary is a claim, and a
claim that nothing enforces is a comment.

**What the paper does not claim**, and is worth stating because it is routinely over-applied: it
does not say that more modules are better, that every dependency should be inverted, or that
interfaces should be general. A general interface is a *worse* hiding of a decision, because
generality leaks the shape of what varies. The criterion is one decision per module, and a module
that hides nothing has no reason to exist.

## The paper in one demo

A small project implementing the paper's contribution and nothing else. One intake, decomposed both
ways, and a measurement of what a vendor's rename costs under each.

```text
days/day-91-slack-shaped-intake/lab/papers/modules/
├── _payloads.py  # the same message in the vendor's old and new shapes
├── steps.py      # decomposition one: a module per processing step
├── hidden.py     # decomposition two: a module per hidden decision
└── demo.py       # counts what knows the vendor, and what breaks
```

The change is the vendor's, and it is the only thing that varies:

```python
V1 = {"type": "event_callback", "event": {"user": ..., "text": ..., "channel": ..., "ts": ...}}
V2 = {
    "type": "message_event",
    "message": {"author": {"id": ...}, "body": ..., "conversation": ..., "sent_at": ...},
}
```

**Line by line:**

- Same information in both: who sent it, what they said, where, and when. The desk's job is
  unchanged.
- Four renames and one extra level of nesting — `user` becomes `author.id`. That is a realistic
  release, not a worst case.
- `type` changes too, so the envelope check moves as well as the fields. This is what makes the
  flowchart version's `parse` step break first.

The demo measures two things and asserts neither. First, what each module knows, read from its own
source:

```python
def vendor_names_in(module_file: str, function: str) -> set[str]:
    """Vendor field names appearing inside one function, read from the source itself."""
    tree = ast.parse((HERE / module_file).read_text(encoding="utf-8"))
    found: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == function:
            for inner in ast.walk(node):
                if isinstance(inner, ast.Constant) and isinstance(inner.value, str):
                    if inner.value in VENDOR_NAMES:
                        found.add(inner.value)
    return found
```

**Line by line:**

- `ast.parse` on the file rather than a regular expression over it, so a vendor name inside a comment
  or a docstring does not count. What is being measured is what the code *uses*.
- The outer walk finds the named function; the inner walk searches only inside it. That gives a
  per-module number instead of a per-file one, which is what the paper's claim is about.
- `ast.Constant` with a `str` value catches `event["user"]` — the subscript is a string constant —
  and does not catch `message.sender`, an attribute access on a type this repository owns. The
  distinction the measurement draws is exactly the distinction the paper draws.
- It returns the set of names, not a count, so the report can print which ones and a reader can
  check the tool is not fooling itself.

Second, whether the thing still runs:

```python
def breaks_on(callable_, *args) -> str | None:
    """Run it against the new payload and report the failure, if there is one."""
    try:
        callable_(*args)
    except (KeyError, ValueError, TypeError, AttributeError) as error:
        return f"{type(error).__name__}: {error}"
    return None
```

**Line by line:**

- The static count could be gamed; running it cannot. Both are reported, and they agree.
- A named tuple of exception types rather than bare `Exception`, so a genuine bug in the demo
  surfaces instead of being counted as "the payload changed" (Principle 10).
- Returning the message rather than a boolean, so the output shows *how* it broke.

Run it:

```bash
cd days/day-91-slack-shaped-intake/lab/papers/modules
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- No flag: both decompositions, so the two counts appear side by side and the comparison is the
  output rather than something the reader has to hold in their head.

Measured on 2026-09-07:

```text
the same intake, two decompositions
  on the old payload they agree: True

  by processing step (parse, authorize, route, reply)
    module        vendor names  breaks on the new payload
    parse                    2   ['event', 'event_callback']
    authorize                1   ['user']
    route                    2   ['channel', 'text']
    reply                    2   ['channel', 'ts']
    handle(V2) -> ValueError: not a message

  by hidden decision (adapt, authorize, route, reply)
    module        vendor names  breaks on the new payload
    adapt                    6   ['channel', 'event', 'event_callback', 'text', 'ts', 'user']
    authorize                0
    route                    0
    reply                    0
    handle(V2) -> ValueError: not a message

  modules that know the vendor's field names: 4 by step, 1 by hidden decision
  rewriting only `adapt` for the new payload: refunds@G8PSS9T3V re 1531420618.000200 in G8PSS9T3V
  the same answer as before: True
```

**Four modules against one.** Read the two `handle(V2)` lines: both decompositions fail on the new
payload, identically, which is the honest result — hiding a decision does not make a system immune
to the decision changing. What it changes is **where you have to go to fix it**, and the last two
lines measure that: rewriting only `adapt` recovers the exact answer the old payload produced.

And the ablation, which removes the comparison:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` removes the second decomposition and nothing else. The measurement it does run is
  unchanged, which is what makes it an ablation rather than a different experiment.

Measured on 2026-09-07:

```text
  by processing step (parse, authorize, route, reply)
    module        vendor names  breaks on the new payload
    parse                    2   ['event', 'event_callback']
    authorize                1   ['user']
    route                    2   ['channel', 'text']
    reply                    2   ['channel', 'ts']
    handle(V2) -> ValueError: not a message

  the ablation stops here: there is one decomposition and nothing to compare it
  against, so 'four modules know the vendor' is a number without a claim in it
exit: 1
```

Same four modules, same seven vendor names, same failure — and no finding, because *four* is only a
result next to *one*. A single decomposition measured against itself is the shape part
[2.3](../parts/02-verifying-it/2.3-checked-against-the-vendor.md) spent a document on.

## When it breaks

The claim does not hold everywhere, and the boundaries are what separate using this paper from
quoting it.

**It needs the decision to actually change.** Hiding something stable buys an indirection and pays
for it in every read of the code. The test is historical: does this thing have versions, migration
guides, or an owner outside your team? A vendor payload does. A function you wrote last week does
not, and wrapping it is the anti-pattern this repository's own guidelines name — *no abstractions
for something used once*.

**Guessing wrong is not free.** The paper assumes you can enumerate the likely changes, and when the
guess is wrong you have hidden the wrong thing: the boundary is now in the way of the change that
actually happened. That failure is quieter than the one it was meant to prevent, and it is why the
enumeration is a step rather than an instinct.

**The measurement is a proxy.** Counting vendor names is a good proxy in this demo because the
vendor's decision is expressed as field names. A decision expressed as *ordering*, or as an implicit
unit, or as a timezone assumption leaks with no string to count. The AST walk would report zero and
the coupling would be total.

**And the boundary decays silently.** Part
[1.1](../parts/01-what-an-integration-is/1.1-somebody-elses-shape.md)'s **When it breaks** section
has the specific mechanism: pass the original payload through on the neutral type, "just in case",
and every module can reach the vendor again while the adapter still stands there looking correct.

## In production

**What survived.** The core, completely, and largely without the citation. Every adapter, port,
anti-corruption layer and driver in modern practice is this argument; so is the advice to define
your own domain type at a system boundary rather than passing a third party's object inward. The
step-three discipline — *enforce that nothing else knows* — survived in the specific form of
architecture tests and lint rules that forbid an import.

**What did not.** The paper's own worked example, a KWIC index, is of its time and nobody teaches
from it now. Its assumption that a module is a compile-time unit is gone — modules are now processes,
services and repositories as often as they are files, and the criterion applies across all of them
while the mechanics differ entirely. And the phrase itself has been worn down: *information hiding*
is now widely used to mean private fields, which is the small version of the idea.

**What it means here, concretely.** This day's endpoint has four decisions that could change
independently, and only one of them currently has a module:

| Decision | Owner | Hidden in |
| --- | --- | --- |
| the vendor's payload shape | the vendor | `adapt` (the demo), `TODO` in `sutra/` |
| the signature scheme | the vendor | `_events.py`'s `base_string` and `sign` |
| the transport | this repository | the FastAPI route |
| which desk skill a message routes to | this repository | not hidden — it is in `route` |

The second row is worth noticing: `base_string` and `sign` already hide the signature scheme, and
that was not done for the paper's reasons — it was done because two callers needed the same
assembly. Convenience and information hiding pointed the same way, which is common and is why the
principle often looks like it does not need arguing for.

**The review comment a senior engineer leaves:** *"Add the test that asserts no module outside the
adapter mentions a vendor field name. The decomposition is right today, and without the test it will
be wrong within a year and nobody will notice the commit that did it."*

**The interview question:** *"How do you decide what the modules are?"* The answer that shows
experience does not describe layers or the shape of the code. It asks what is likely to change, says
that each of those gets a module, and then names the enforcement — because the first two thirds of
that answer are quotable and the last third is what makes it true six months later.

## Check yourself

```bash
cd days/day-91-slack-shaped-intake/lab/papers/modules
uv run python demo.py; echo "exit: $?"
uv run python demo.py --off; echo "exit: $?"
```

Both decompositions fail on `V2`. Say why that is the honest result, and what the paper actually
claims given that both fail.

Now do the repair the demo describes: edit `adapt` in `hidden.py` so it reads the `V2` shape, and
run `hidden.handle(V2)`. Then do the same for `steps.py` and count the edits. The ratio is the
paper's claim, measured by you.

Finally, find a decision in this day's lab that is *not* hidden anywhere — the table in **In
production** names one — and say what module it would get.

**Out loud, without scrolling up:** what is the criterion for a module, what is the step everybody
skips, and why is a general interface a worse hiding of a decision than a specific one?

**Next:** back to the hub — [`LESSON.md`](../LESSON.md).

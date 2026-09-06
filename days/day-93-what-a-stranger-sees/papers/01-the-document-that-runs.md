---
day: 93
paper: "doi:10.1093/comjnl/27.2.97"
title: "The document that runs"
ids: []
level: production
prerequisites: ["../parts/03-the-docs-pass/3.3-the-index-that-regenerates-broken.md"]
prev: "../parts/05-the-demo/5.2-what-a-real-public-repo-adds.md"
next: "../LESSON.md"
---

# Paper 01 — The document that runs

> **Literate Programming**
> *The Computer Journal*, volume 27, issue 2, 1984, pages 97–111.
> `doi:10.1093/comjnl/27.2.97`
>
> The claim this day borrows: a program should be written as a document addressed to human beings,
> in the order that explains it, with the machine-readable form **derived** from that document rather
> than maintained beside it.

## One-line answer

Prose and code drift apart because they are two artefacts that have to be kept in step by hand — and
the paper's answer is to stop having two, so that a sentence claiming the ledger leaves nineteen units
is a sentence that gets executed and can fail.

## The story

The recipe on the back of the packet, and the one your aunt wrote out.

The packet's version is precise: quantities, temperature, timings. It is also the version that goes
wrong, because it omits the two things the person who wrote it does not think of as steps — that the
batter must rest, and that the oven runs hot.

Your aunt's version is a paragraph with the quantities inside it, and it works, because she wrote it
the way she would say it to somebody standing next to her. The order is the order of *doing*, the
reasons are attached to the actions, and the two things the packet left out are in there, because in
a paragraph there is nowhere for them to fall out of.

The packet has a list and a separate note of tips. Your aunt has one thing.

## The idea in plain language

The paper's proposal is a reversal. The conventional arrangement is: write the program, then write
documentation about it. Two artefacts, in two places, describing one thing — and the second one is
always slightly out of date, because updating it is a separate act of will.

The proposal is to write **one** artefact: a document, in whatever order best explains the program to
a person, with the code embedded in it. Two tools then process that document — one extracts the code
for the compiler, the other typesets the prose for the reader. The names given to those two
operations were *tangle* and *weave*.

Three consequences follow, and it is the third that matters most here.

**The order of explanation is freed from the order of compilation.** You can introduce the interesting
idea first and the boilerplate last, because a tool reassembles it for the machine.

**The prose and the code cannot be separated**, because they are the same file. There is no
opportunity to update one and forget the other.

**And the document is executable, so it can be wrong.** Once a claim in the prose sits next to the
code that supports it, and both are run, a sentence that no longer matches the program is a *failure*
rather than a stale sentence nobody notices. Documentation joins the set of things that can go red.

That third consequence is what this day is about, and it is a direct answer to what parts
[1.3](../parts/01-the-stranger/1.3-the-readme-that-documents-the-design.md) and
[3.3](../parts/03-the-docs-pass/3.3-the-index-that-regenerates-broken.md) measured — a README whose
claims drifted from the enforcer, and an index whose links break in the copying.

## Why Sutra needs it

Because this repository is a literate-programming artefact and has never been described as one. A
`days/day-NN/` folder is a document in the order a person needs, with the code embedded in it, and a
build brief that says which parts of it the reader extracts by hand. `./m depth` is a partial *weave*
— it enforces that every code block has an explanation next to it. There is no *tangle*: the reader
is the tangler, deliberately, which is Principle 4.

And because the failure the paper prevents is the one this day found twice. Part 1.3's README says a
part has ten sections and the enforcer requires eleven; nothing executed the claim, so the claim was
free to be wrong for two plan versions. That is precisely the drift a woven document makes impossible.

## The mechanism

The paper's method, written out rather than paraphrased:

**One source file.** The document contains prose and named chunks of code, interleaved in the order
that explains the program.

**Tangle** reads it and emits compilable source, resolving the chunk references and ordering them as
the compiler requires. The output is not meant to be read by anybody.

**Weave** reads the same file and emits a typeset document — the prose, the code as the author wrote
it, and cross-references built from the chunk names so a reader can navigate the program the way they
navigate a book: an index, and a pointer from every use to its definition.

The insight the paper leans on is that these two orders are genuinely different, and that forcing the
human order to match the machine order is what makes conventionally-organised programs hard to read.

What the paper does *not* claim, and is often assumed to: it does not propose testing. Executable
examples came later, from the same premise. The paper's own argument is about explanation and order,
and the demo below takes the descendant idea because that is the half that shipped.

## The paper in one demo

A small end-to-end project implementing the claim and nothing else: a document whose code is
executed, against the same document merely read.

```text
days/day-93-what-a-stranger-sees/lab/papers/literate/
├── doc.md      # the document: prose, and three examples of the module it describes
├── ledger.py   # the tiny module the document is about
├── weave.py    # extract the code from the document and run it
└── demo.py     # inject one wrong digit; ask each mode whether it notices
```

`doc.md` is the artefact. Here is the whole of its first claim:

```text
Spending one unit from a fresh allowance of twenty leaves nineteen:

    >>> from ledger import Ledger
    >>> book = Ledger(allowance=20)
    >>> book.spend(1)
    >>> book.remaining
    19
```

**Line by line:**

- The sentence and the example are one thing. The prose states the claim in words, the block states it
  in a form that can be run, and there is no version of this file where one has been updated and the
  other has not.
- The `>>>` form carries the expected output *inside* the example, which is what makes a plain
  paragraph executable at all — the claim and its evidence are the same characters.

The weaver runs every block, threading state through, because a document is one program:

```python
        # The document is ONE program, so each block inherits what the previous ones defined.
        # doctest copies the globs it is handed, so the copy is carried forward by hand.
        test = parser.get_doctest(source, globs, f"{document.name}#block{index}", str(document), 0)
        if not test.examples:
            continue
```

**Line by line:**

- `doctest` rather than a hand-written executor. It is the shipped descendant of the paper's idea, and
  reimplementing it would make the demo about running Python instead of about whether the document is
  run at all — which is the paper's claim and the only thing this demo may test.
- `get_doctest` **copies** the globals it is given, so block two would not see block one's `import`
  without the carry-forward on the next line. The first version of this demo failed six of ten
  examples for exactly that reason, and the failure was in the harness rather than the document.
- Blocks with no `>>>` are skipped, so ordinary illustrative code in a document does not have to
  pretend to be a test.

The demo injects the smallest possible drift — one digit — and asks each mode whether it notices:

```python
    original = DOC.read_text(encoding="utf-8")
    drifted = original.replace(f"\n{DRIFT[0]}\n", f"\n{DRIFT[1]}\n", 1)
    assert drifted != original, "the drift was not injected"
```

**Line by line:**

- The document on disk stays correct; the drift is injected into a copy. So the reader can run the
  weaver against `doc.md` directly and see it pass, and the demo is not shipping a broken document.
- `19` to `18` — the prose now claims one unit less remains than the code leaves. One character, and
  it is exactly the kind of edit that happens when a default changes and the sentence is not revisited.
- The `assert` guards the demo against silently testing nothing, which would make both arms agree for
  the wrong reason.

Run it:

```bash
cd days/day-93-what-a-stranger-sees/lab/papers/literate
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- No flag: the document is treated as a program and executed.

Measured on 2026-09-07:

```text
document : doc.md, with one digit changed (19 -> 18)
blocks   : 3
mode     : woven - every block executed

**********************************************************************
1 items had failures:
   1 of   4 in doc.md#block1
***Test Failed*** 1 failures.

  examples attempted : 10
  examples failed    : 1

  drift caught: yes
  one digit, and the document stopped agreeing with the program it describes
exit: 0
```

Now the ablation — the same drifted document, read rather than run:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` removes the execution and nothing else. Same file, same drift, same three blocks.

Measured on 2026-09-07:

```text
mode     : prose - read, not run

  93 words read, 3 examples, 0 executed
  the sentence still reads correctly and the number still looks like a number

  drift caught: no
  a document nobody executes is consistent with every program, including a wrong one
exit: 1
```

**Caught, and not caught, from one wrong digit.** The prose arm is not lazy or badly written — it read
the whole document. It cannot detect the drift because *reading has no failure mode*, and that is the
paper's point stated as a measurement.

## When it breaks

The idea does not hold everywhere, and knowing where it stops is what separates using it from quoting
it.

**It needs a claim that can be executed.** *"Zero budget, by construction"* is a true and important
sentence in this repository's README, and no weaver can check it. The technique covers the subset of
documentation that makes mechanical claims — which is a minority of most documents, and the majority
of the ones that go wrong quietly.

**Examples are not the program.** A document whose ten examples all pass describes a system that works
for those ten inputs. It is documentation with tests in it, not a test suite, and treating it as
coverage is a mistake the technique invites.

**The order argument aged badly.** The paper's premise is that a program is best presented as a single
narrative in one order chosen by the author. Readers of large systems do not read in one order at all
— they arrive at a symbol from a search result and navigate by cross-reference. Hyperlinked reference
documentation won that argument, and this repository's own day format concedes it: plan §17's
standalone test requires every part to be readable **cold**, which is the opposite of a single
narrative order.

**And a woven document can be green and useless.** Ten examples passing says the document's claims
hold; it says nothing about whether the document explains anything. Part
[2.3](../parts/02-running-the-readme/2.3-what-a-readme-owes.md)'s five reader questions are not
checkable by any of this.

## In production

**What survived.** The premise, almost completely, in a form the paper would recognise but did not
build. Docstrings put the explanation inside the artefact. Doc-tests make the examples executable —
Python shipped `doctest` in the standard library, which is why this demo needed no dependency.
Notebooks interleave prose, code and output in one file. Documentation-as-code puts the docs in the
repository, under review, in the same pull request as the change. Every one of those is *one artefact
instead of two*, which is the paper's actual argument.

**What did not.** The specific toolchain — a source format with named chunks, processed by *tangle*
and *weave* into compilable source and a typeset document — is a specialist interest today. Two
reasons: the tangled output is unreadable, which breaks every tool that expects to read source
(debuggers, profilers, version control diffs); and the single-narrative-order premise lost, as above.
The idea shipped; the format did not.

**What it means for this repository, concretely.** Three of this day's findings are drift between a
document and the thing it describes, and each has a different weave available:

| Finding | The drifted claim | What weaving it would mean |
| --- | --- | --- |
| part 1.3 | README says ten sections | generate the list from `depth_check.PART_SECTIONS` |
| part 1.3 | README's `./m` command list | generate it from the driver's own case labels |
| part 3.3 | wiki copies a part's prose | rewrite relative links during the copy |

The third is not documentation drift at all — it is a generator moving text between directories — and
it is on this list because it is the same failure at one remove: **an artefact derived from another
artefact, where the derivation loses something.** A weaver is exactly the tool that has to get that
right.

**The review comment a senior engineer leaves:** *"Generate the README's section list and command
list from the code that owns them. They are the two claims that have already drifted and they are the
two that can be derived — the rest of the README is prose and stays prose."*

**The interview question:** *"How do you keep examples in documentation correct?"* The answer that
shows experience makes them executable and runs them in CI, and then — unprompted — notes the limit:
that this covers only claims a machine can check, and the sentences that matter most to a new reader
are usually not those.

## Check yourself

```bash
cd days/day-93-what-a-stranger-sees/lab/papers/literate
uv run python demo.py; echo "exit: $?"
uv run python demo.py --off; echo "exit: $?"
```

Same document, same drift, opposite results. Say in one sentence what the second run did wrong — the
honest answer is "nothing", and explaining why that is the finding is the exercise.

Now run the weaver against the clean document and confirm ten of ten pass:

```bash
uv run python -c "from pathlib import Path; from weave import check; print(check(Path('doc.md'))[:2])"
```

Then open `doc.md` and add a fourth claim in prose only, with no example. Re-run. Say why the count
does not move, and what that tells you about what this technique does and does not cover.

**Out loud, without scrolling up:** state the paper's proposal in one sentence, name the half of it
that shipped and the half that did not, and say which of this repository's README claims could be
woven.

**Next:** back to the hub — [`LESSON.md`](../LESSON.md).

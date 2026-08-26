# ADR-0008 — A paper is taught in a part of its own, and cited by identifier

- **Date:** 2026-08-25
- **Day:** 5 (applied retroactively to Days 0–5)
- **Phase:** 1
- **Status:** accepted
- **Amends:** master plan v2.1.0 → **v2.2.0** (§17.4 row 6, §17.4.1 rule 5, **§17.4.2**, §17.7, §17.9, §16, §18.1 rule 5)
- **Related:** ADR-0003 (the depth contract this extends)

## Context

The depth contract already forces a part to answer *what is this*, *why does Sutra need it*, *how
does it work*, *how does it break* and *what changes in production*. It never asks **where the idea
came from**, and for a large fraction of this curriculum that question has a precise, public answer.

The reader is not learning generic software engineering. They are learning a field roughly eight
years old in which most of the load-bearing ideas can be traced to one document each: the
reason-then-act loop hand-rolled on Day 3, the sampling dial turned on Day 2, the tokenizer whose
receipt Day 2 reads, the tool-calling round trip built on Day 4. A reader who meets these only as
framework features learns the framework. A reader who meets the origin learns the field, and — more
usefully — learns **which half of the original proposal actually survived contact with
production**, because in every one of these cases some of it did not.

There is a second, sharper reason. This curriculum's parts are drafted with an assistant, and a
language model asked for "the paper behind X" will produce a *fluent* citation whether or not it
exists. A wrong version pin fails loudly the moment someone runs `uv sync`. A plausible arXiv ID
attached to the wrong title fails **silently, for years**, and the reader who follows it into a
search engine is the one who discovers it. Principle 7 — never invent a version number — has an
exact analogue in the literature, and it needed writing down before the citations started arriving
rather than after.

Third, a naming conflict had to be resolved before the first citation was written. §18.1 rule 5
forbids naming a person — no instructor, no author, no channel, no academy. Ordinary scholarly form
is *"Author et al., 2017"*. Taken literally, the rule bans the conventional citation.

## Decision

**1 — A paper is taught in a part of its own (§17.4.2).**

The first draft of this amendment put the paper inside the part that uses it, as one more section.
That was wrong, and it was wrong by this plan's own rules. §17.1 says one idea per document; a paper
is an idea. A part that teaches the sampling dial *and* the paper that proposed nucleus sampling
teaches two things, and the second one gets whatever room is left after the first — which is the
mechanism by which a curriculum ends up citing documents it never explains. §17.7 says split by
idea boundaries, and there is an idea boundary here.

So: **one part per paper**, written to the same eleven-section contract as every other part, at the
same depth, with the same story-before-abstraction opening. Its frontmatter declares `paper:`
(singular — the one-idea test again). On a paper part the required sections take their natural
meanings: *The story* is the problem the field had before the document existed, *The mechanism* is
the method written out rather than the abstract paraphrased, *When it breaks* is where the claim
does not hold, and *In production* is **what survived and what did not**.

**2 — Paper parts go in the day's last section.**

This is **Principle 4 at the scale of a day**. P4 already says hand-roll the mechanism, then adopt
the framework, so the framework is a convenience and never a mystery. The same argument applies to
the literature: a reader who has just written the reason-then-act loop by hand can be told which
half of the proposal they reinvented and which half the field dropped. A reader who meets the paper
first has nothing to hang it on, and the section degrades into a reading list they skip.

**3 — §17.4 row 6, *The paper behind it*, is an address and nothing more.**

The concept part that leans on a paper still owes the reader the origin — §17.4's no-shortcut test
is explicit that a deferred explanation must have an address. So the citing part carries a short
conditional section between *Why Sutra needs it* and *The mechanism*: the citation block, one
sentence of what the paper claimed, and a **link to the paper part**. The reader who wants the
origin follows the link; the reader who wants the mechanism reads on. Nothing is duplicated, and
nothing dangles.

It is conditional, and the condition is **declared, not guessed**: the section is required exactly
when the frontmatter carries `papers:`, and vice versa. *"Does this idea have a paper?"* is not a
question a script can answer. *"Do these two agree?"* is.

**4 — A paper is taught once in the whole curriculum.**

Ninety-seven days will cite the same handful of documents repeatedly. The day that **first** needs a
paper carries its part; every later day cites it in row 6 and links to that part. Re-teaching it on
Day 66 is exactly the duplication the standalone test asks you to solve with a link rather than a
copy. `./m depth` enforces uniqueness: two parts declaring the same `paper:` is a failure.

**5 — §17.4.1 rule 5, never invent a citation.**

The record is looked up live on the day the part is written, the title copied from the record rather
than from memory, and the identifier lands in the new append-only `docs/PAPERS.md` with the date it
was checked. `./m depth` rejects an identifier with no ledger row, and rejects a citation whose
shape is not a real arXiv ID or DOI. An unverifiable paper leaves a `TODO` containing the exact
lookup command, exactly as an unverifiable version does.

**6 — A paper is cited by title and identifier, never by its authors.**

§18.1 rule 5 stands unamended. `arXiv:1706.03762` is a stricter handle than a surname and a year —
it resolves to exactly one document, it is what a reader types, and it keeps the curriculum's
promise that it promotes nobody.

## Options considered

| Option | Why not |
| --- | --- |
| **The paper as a section inside the part that uses it** (this ADR's own first draft) | Two ideas in one document, against §17.1. The paper gets whatever space is left after the mechanism, which in practice is a paragraph. Superseded by §17.4.2 before any day was written to it. |
| Paper parts **first** in the day, before the mechanism | Nothing to hang them on. "What survived and what did not" is meaningless to a reader who has not yet built the thing, and Principle 4 already settled this argument for frameworks. |
| A *Further reading* list at the foot of each part | Optional by construction, therefore skipped, therefore unread. It also invites the exact failure this ADR exists to prevent: an unverified list nobody checks. |
| One `docs/PAPERS.md` bibliography and no teaching at all | Puts the origin somewhere other than where the idea is taught. A reader on Day 3 does not go looking in `docs/`. The ledger is kept — as the verification record, not as the teaching. |
| Make row 6 unconditional | Two thirds of the parts written so far are about a tool, a command or a repo convention. Forcing a paper onto `2.2-gitignore-before-secrets-exist.md` guarantees an invented one. |
| A new principle (P19) rather than §17 rows | The principles are about how the project is run; this is about how a document is shaped. §17 is where the shape lives. |
| Amend §18.1 to permit author names | Unnecessary. The identifier attributes the work more precisely than a surname does, and the rule's promise stays whole. |

## Consequences

- Days 0–5 are retrofitted in place: the days whose ideas came from papers gain a final paper
  section, the parts that lean on those ideas gain row 6, and every hub moves to
  `plan_version: "v2.2.0"` with its §2 map and `parts:` count updated.
- Days 0 and 5 are expected to gain nothing. Their subjects are a toolchain and a framework's
  surface, and neither has a literature.
- Part counts rise. That is the intended direction — §17.7 sets no target count, and a day that
  gains a paper part has gained a subject, not padding.
- `docs/PAPERS.md` joins the hand-written ledgers in §16. Like the others, the day document ends
  with the exact rows to paste.
- Every future day pays a verification cost per citation — the same cost Principle 7 already imposes
  on every version pin, and what separates a citation from a recollection.
- **The risk this does not remove:** a correctly-verified paper cited for a claim it does not
  actually make. No ledger catches that. It is caught by reading, like everything in §17.8.

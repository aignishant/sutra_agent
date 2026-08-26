# ADR-0003 — Days are rewritten as a hub plus one document per subtopic, and Day 0 is added

- **Date:** 2026-08-23
- **Day:** 0 (pre-curriculum)
- **Phase:** 0
- **Status:** accepted
- **Amends:** master plan v1.2.1-R → **v2.0.0**
- **Related:** ADR-0001 (plan reconstruction) · ADR-0002 (deployment implementation track)

## Context

v1.2.1-R defined a day as one file: `docs/days/day_NNN.md`. 107 of those were written. Measured on
2026-08-22, before this amendment:

| Measure | Value |
| --- | --- |
| Day documents written | 107 |
| Total lines across them | ~50 400 |
| Mean lines per day | ~471 |
| Largest (`day_099.md`) | 600 lines |
| Day documents carrying an "estimated hours" header field | 107 of 107 |

Three problems followed from the format, not from the writing:

1. **A subject cannot be revisited alone.** Day 53 teaches the graph Workflow Runtime — nodes,
   edges and the 2.x composition model — under one `##` heading. A reader who wants to re-read
   *only* "what is an edge" re-reads the node model and the trap-#1 discussion to get there.
2. **A thin subtopic is invisible.** With one file per day there is no artifact that says "this day
   covered six subtopics and one of them got two paragraphs". Nothing in the repo could distinguish
   a subtopic that was covered briefly from one that was skipped.
3. **The header field authorised the worst edit.** Every day carried "estimated hours". A time
   estimate at the top of a document is a standing instruction to cut the explanation when the
   document gets long — which is the one edit a teaching document must never make.

The learner's stated goal is to work on production systems at a product company directly from these
documents, starting from no prior knowledge of the subject. The v1 format could not carry that: it
assumed the previous day, and it stopped at the working example rather than the production one.

A sibling curriculum in this workspace (`setu`) had already hit the same wall at a larger scale —
40 668-character single-file lessons — and had amended to a hub-plus-parts architecture with a
machine-checkable depth contract. That architecture is proven in practice, and it is what this ADR
adopts.

## Options considered

| Option | Pros | Cons |
| --- | --- | --- |
| **A. Keep one file per day, write longer files** | No migration; no tooling to build. | Does not fix any of the three problems. The largest files are *already* the worst to read; making them larger makes it worse. Thin subtopics stay invisible. |
| **B. Split each day into unnumbered topic files** | Cheap; fixes problem 1 partially. | No contract means no enforcement. Splitting a long page into short pages without adding story, failure text and a production section is reformatting, not depth — and nothing would catch it. |
| **C. Hub + `parts/<section>/<section>.<sub>-<slug>.md`, with a ten-section part contract, a `level` ladder, a no-clocks rule, and a script that enforces the mechanical half** | Fixes all three. Part count per day becomes a visible depth signal in the tracker. The contract is reviewable and partly automatable. Proven in the sibling curriculum. | Every existing day must be regenerated. Requires new tooling (`depth_check.py`, `tracker.py`, the `./m` driver). Days take substantially longer to write. |
| **D. Option C, but also renumber the 96-day map to make room for setup** | Would let Day 0's material live inside Day 1. | Renumbering invalidates every ID→day mapping in `TRACEABILITY.md` and violates the plan's own "never reorder days without an ADR" for no benefit. Rejected. |

## Decision

**We adopt Option C**, and we add **Day 0** in front of Day 1 as a day that closes **no curriculum
IDs**.

Concretely:

1. A day becomes `days/day-NN/{LESSON.md, CHECKLIST.md, parts/<NN>/…, lab/}`. `parts/` is
   mandatory; a day without it is not written.
2. Every part carries ten sections in a fixed order, ending in **In production** and **Check
   yourself**. The full contract is master plan §17.
3. New Principles **16** (depth over density), **17** (a day is a unit of subject, not of time) and
   **18** (assume no prior knowledge, finish at production).
4. **No time estimate may appear anywhere in a day folder.** `scripts/depth_check.py` fails the day
   on one, including the `estimated hours` field every v1 day carried.
5. Day **0** is added: toolchain, skeleton, the `./m` driver, the first commit. It closes no IDs, so
   §14's day→ID map and `TRACEABILITY.md` are untouched by the amendment.
6. Repo tooling moves `tools/` → `scripts/`; `make check` becomes `./m check` with a two-line
   `Makefile` shim; the ledgers move `docs/days/` → `docs/`.
7. The 107 v1 day documents move to `legacy/days/` with `git mv`. Nothing is deleted.

### Why Day 0 closes no IDs

This is the load-bearing detail. The obvious alternative — giving Day 0 some of Day 1's OPS IDs —
would have re-opened those IDs in `TRACEABILITY.md` and made the amendment a curriculum change
rather than a format change. Day 0's subject (which Python runs, who owns the environment, why
`.gitignore` precedes `.env`, what makes a gate refuse) is a **precondition** for the curriculum,
not a member of it. Day 1 keeps AG-01, OPS-01, OPS-02 and OPS-03 exactly as v1.2.1-R assigned them.

## Consequences

**Easier.** A reader can open one idea. A reviewer can see part counts per day in `docs/TRACKER.md`
and spot a thin day without reading it. `./m depth N` catches a missing *In production* section, a
code block nobody explained, a numbering gap and a smuggled-in clock. Every part is readable cold,
because the standalone test requires it to name and link its prerequisite.

**Harder.** Writing a day is now substantially more work — Day 0 alone is sixteen documents. That
is the intended trade: the plan's own Principle 16 says a wall of text is depth's disguise, and the
cost of the real thing is that it takes longer to write.

**Committed to.** Regenerating all 96 remaining days in this shape. Every regenerated day must
*gain* the story, the mechanism, the real failure text, the production face and the check that its
legacy version did not have — reformatting a legacy day is explicitly not regenerating it
(§17.8).

**Not changed.** No curriculum ID, no phase boundary, no gate, no model policy, no dataset, and no
principle 1–15. The 96-day arc and all 199 IDs are identical to v1.2.1-R.

## What would make us change our minds

- If `./m depth` starts passing days that read badly, the mechanical half is measuring the wrong
  thing and the contract needs a different check — not a relaxed one.
- If the median day exceeds roughly twenty-five parts, sections are being used as a substitute for
  day boundaries, and the day map itself needs an amendment (with its own ADR) rather than more
  parts.
- If a regenerated day turns out to be *shorter* on substance than its legacy version, the mining
  rule in §17.8 is not being followed and the regeneration should be reverted, not accepted.

## Cold read

*(Re-read this with a reviewer's hat on. Sign here.)*
Reviewed on 2026-08-23 — still stands.

---
name: day-sutra
description: Generate the hub, the parts/ sub-documents, the lab scaffold and the checklist for a given day of the Sutra plan
argument-hint: [day-number]
---

# Generate Day $ARGUMENTS of the Sutra plan (v2.2.1 — hub + `parts/` + paper parts)

> **Read `docs/00_MASTER_PLAN.md` §17 before writing a single line.** It is the depth contract this
> skill implements. This skill is the procedure; §17 is the standard.

## The three commitments (§17.1 — everything below follows from these)

1. **One idea per document.** If it needs "also" to introduce its second half, it is two documents.
2. **No clocks.** Never write a time estimate, a duration, an "estimated hours" field, or a pace —
   not in frontmatter, not in prose, not in the checklist. A topic is finished when it is
   understood, and a reader may spend five sittings on one part. **Never trim an explanation
   because the day is getting long — split it into another part instead.**
3. **Zero to production, in one document.** Open where a reader who has never heard of the idea can
   stand. End where a professional stands: the real-system version, what breaks at scale or under
   concurrency, what a senior reviewer says, what an interviewer probes.

---

## Step 1 — gather

4. Read the plan: **§2** (principles), **§5 + §5.1** (the ADK 2.x baseline and the four 1.x→2.x
   traps), **§14** (the day map — the authoritative ID list for day $ARGUMENTS), **§17** (the depth
   contract), **§18** (the style guide). Collect every ID slotted to day $ARGUMENTS, the phase
   theme, and the gate that phase feeds.
5. Read `docs/PROGRESS.md`. **Confirm $ARGUMENTS is exactly one more than the last row.** If it is
   not, say so and stop — do not generate out of order (plan §15: never skip, merge or reorder a
   day without an ADR).
6. Read `docs/TRACEABILITY.md`. Any open ID from a completed phase is a bug — report it, don't
   paper over it.
7. Read the previous day's `days/day-NN-<slug>/LESSON.md` and `CHECKLIST.md`. If the checklist has
   unticked boxes, warn me and ask before proceeding. Build on the code the previous days told the
   learner to write in `sutra/` — never duplicate it, never rewrite it.
8. **Mine the legacy day.** If `legacy/days/day_NNN.md` exists (zero-padded to three digits), read
   it. It is the v1.2.1-R draft: **take its correctness, discard its structure.** Everything it
   covered must survive into the parts, and each surviving topic must *gain* the story, the
   mechanism, the real failure text, the production face and the check it did not have. Never copy
   a legacy section across wholesale, and **never carry its "estimated hours" header field** —
   Principle 17 removed it and `./m depth` fails the day on it.
9. Read the addenda that bind this day: `02_ADDENDUM_ZERO_BUDGET_MODELS.md` §5 for any day it
   amends, and `01_MASTER_PLAN_ADDENDUM_GAPS.md` for MCP days and ADK-73..78.

## Step 2 — verify reality before you write (Principles 7, 8, 14)

10. **Never invent an API.** For every ADK symbol the day will use, fetch the live **adk.dev** page
   and note the URL and the date. The part that uses the symbol states the page checked. If the
   live docs disagree with the plan, **stop and propose an amendment** — do not silently adapt.
11. **Never invent a version.** For every package the day installs, read the version live
   (`curl -s https://pypi.org/pypi/<pkg>/json`, or `uv pip compile` for a resolved answer). Record
   package, version and date in `docs/PACKAGES.md`. If a lookup fails, leave a
   `TODO(<exact command>)` — never a guess.
12. **Never invent a model name.** Any day that names a model looks up the provider's current free
   list first (Gemini AI Studio · console.groq.com/settings/limits · openrouter.ai filtered to
   `:free`) and records model + date. Free rosters move.
13. **Never invent a citation** (§17.4.1 rule 5). For every paper the day will teach or cite,
    **open the record live** — `arxiv.org/abs/<id>`, or the DOI — and copy the title from it rather
    than from memory. Record title, identifier, year and the date checked in `docs/PAPERS.md`. This
    is Principle 7 pointed at the literature, and it bites harder: a wrong version pin fails loudly
    on the next `uv sync`, while a plausible arXiv ID attached to the wrong title fails **silently
    for years**. If the record cannot be opened, leave `TODO(<exact lookup command>)` — never a
    remembered citation. Cite by **title and identifier, never by authors**.
14. **MCP days:** check the spec revision on the spec page before writing. If it moved, Addendum 01
    Part 2 is the standing rule — amend first.

## Step 3 — plan the split (do this before writing prose)

15. List the day's subtopics. Group them into **sections** that share one mental model — usually one
    section per curriculum ID, per lifecycle stage, or per phase of a mechanism. State the
    grouping; an unexplained numbering is a bug.
16. Split by **idea boundaries, never by length or pace** (§17.7). There is no target part count.
    Four parts if the subject needs four; twenty-two if it needs twenty-two. `setup` days split per
    tool or file; `lab` days per mechanism → behaviour → edge case → failure mode → production use;
    `concept` days one claim per part; `gate` days one acceptance criterion per part.
17. **Ask what the day's ideas came from.** For each subtopic: is there a public, citable origin
    document — a research paper, a numbered spec revision, a formal technical report? If so, the day
    gets **one document per paper in `days/day-NN-<slug>/papers/`** (§17.4.2) — beside `parts/`, not
    inside it — and every part leaning on that idea carries §6 *The paper behind it*. A subtopic about a tool, a command, a repo
    convention or an SDK surface has no paper; do not manufacture one. **A paper already taught on
    an earlier day is not re-taught** — cite it and link that part.
18. **Every day gets at least one part whose subject is a deliberate failure** — v1's *💥 Failure
    lab*, promoted to a part of its own, usually at `production` level.
19. Assign each part a `level` — `foundation` (knows what it is), `working` (can use it on their own
    problem), `production` (knows what changes in a real system). A day should climb. A day that is
    all `foundation` is a tutorial; a day opening at `production` has skipped the reader.
20. Apply the **one-idea test**, the **standalone test** and the **no-shortcut test** (no "for now,
    just accept that" without a forward link) to each planned part *before* writing.
21. **Print the planned part list to me before writing.** If it looks thin, I will say so.

## Step 4 — write the parts (`days/day-NN-<slug>/parts/<NN>-<slug>/<section>.<sub>-<slug>.md`)

> **Name the day folder `days/day-NN-<slug>/`** — the number zero-padded, then a kebab-case slug of
> 1–4 words taken from the hub's `title` with articles dropped: `days/day-01-bootstrap-and-map/`.
> A number alone is an address, not an answer, and 97 of them are indistinguishable in a file tree.
> The number stays the identity — `./m`, `depth_check.py`, `tracker.py` and `trace.py` all resolve a
> day by number and accept any slug — so a folder can be renamed to a better slug at any time.
> `./m depth` rejects a bare `days/day-NN/`.

22. **One folder per section**, two zero-padded digits **then a kebab-case slug of 1–3 words saying
    what the section is about** — `parts/01-what-is-an-agent/`, `parts/03-keys-and-env/`. Take the
    slug from the section's heading in the hub's §2 map. A bare `parts/01/` is rejected by
    `./m depth`. Every part lives inside its section's folder; none is ever loose in `parts/`, and
    the folder number must match the number before the dot in the filename.
23. One file per subtopic, named `<section>.<subtopic>-<kebab-slug>.md`. The slug says what the part
    *teaches*, never where it sits. Numbering starts at `1` and has no gaps.
24. **Links are relative to the part's own folder**: a sibling in the same section is
    `1.2-<slug>.md`; a part in another section is `../01-<slug>/1.5-<slug>.md`; the hub is
    `../../LESSON.md`. `prev` and `next` in the frontmatter use the same form. The hub's §2 map
    links the full path from the day folder: `parts/01-<slug>/1.1-<slug>.md`.
25. Every part carries all twelve sections of §17.4, **in this order**. Three are **conditional**
    — *The paper behind it*, *Line by line* and *The paper in one demo* — each required exactly when
    its trigger is present:
    - **frontmatter** — `day`, `part`, `title`, `ids`, `level`, `prerequisites`, `prev`, `next`.
      **No duration field of any kind.**
    - **One-line answer** — the claim in one sentence, before anything else.
    - **The story** — a concrete scene first: a person, a machine, a failure, a decision. **No
      jargon at all** in this section. This is the hook the definition hangs on. Four rules on top
      of that, and the first is the one that gets broken:
      1. **A scene the reader has plausibly lived.** Ordering a parcel, a repair-shop job card, a
         bus route map, getting a used car checked, a tailor's shop, a monthly generator test,
         learning to drive on an empty ground. **Not** a nautical chart, a model railway, a theatre
         programme, a controlled forestry burn, a projection booth or a 1904 city fire. Test: could
         the reader have been standing in this scene themselves? If they would have to be told what
         the setting *is* before the analogy lands, it is the wrong setting.
      2. **Simple words.** If a twelve-year-old could not follow the first sentence, rewrite the
         first sentence. Short sentences beat clever ones here.
      3. **Realistic, and load-bearing.** The scene must contain the actual failure or decision the
         part teaches, not a pretty image the part then abandons. Every later section that reaches
         back for the metaphor must still fit it.
      4. **No metaphor collisions within a day.** Before choosing, grep the day's other parts and
         the hub's §1: two parts reaching for the same family — two restaurants, two receptionists —
         reads as one idea repeated. One family, one part.
    - **The idea in plain language** — the concept assuming zero prior knowledge; every term defined
      on first use, **including terms from earlier days**, with a link to the part that introduced
      them. No code.
    - **Why Sutra needs it** — the concrete later day that breaks without this. Never "this is
      important".
    - **The paper behind it** — *conditional: present exactly when the frontmatter declares
      `papers:`.* An **address, not an explanation**: the citation block (exact title · arXiv ID or
      DOI · year · URL, **no authors**), **one sentence** of what it claimed, and a **link to the
      paper part that teaches it** — in this day or an earlier one. Nothing more.
    - **The mechanism** — how it actually works: runnable code, the protocol exchange written out,
      or the diagram. Nothing skipped as "obvious".
    - **Line by line** — a `**Line by line:**` list **immediately after each code block**: every
      non-obvious token, and *why that line and not another*.
    - **The paper in one demo** — *conditional: paper parts only, i.e. the frontmatter declares
      `paper:`.* A small end-to-end project implementing the paper's contribution **and nothing
      else**, with an ablation switch. See item 27.
    - **When it breaks** — the **real** error text verbatim, what it means, the smallest fix.
    - **In production** — the real-system version: what a professional writes instead of the
      teaching version, what degrades at scale or under concurrency, the failure that only shows
      with real traffic, the review comment a senior engineer leaves, and the interview question
      that finds out whether you have actually used it. **Not optional. This is the section that
      makes the document professional rather than introductory.**
    - **Check yourself** — one command to run now, one question to answer out loud.
26. Apply **Sutra's five additional part rules** (§17.4.1): name the adk.dev page checked · state
    the verified version or a `TODO` with the lookup command · every model mention obeys Addendum
    02 including 429 handling · **name the 1.x→2.x trap** the part is avoiding, if it touches one ·
    **never invent a citation** — verified live, with a dated row in `docs/PAPERS.md`.
27. **Write the papers last, into `days/day-NN-<slug>/papers/`** (§17.4.2) — a directory beside
    `parts/`, never a section inside it. They are *read* after the parts too: the hub's map says so
    and the final part's *Next* points at them. That order is **Principle 4 at the scale of a day**:
    the reader hand-rolls the mechanism, *then* reads the proposal, so "what survived and what did
    not" lands on something they built rather than on nothing. One document per paper, named
    `NN-<paper-slug>.md` from `01` with no gaps (`papers/01-attention-is-all-you-need.md`).
    Frontmatter is a part's **minus `part`** and **plus `paper:` (singular)** — the one identifier it
    teaches — and `level` is almost always `production`. Links run one level up: a part is
    `../parts/01-<slug>/1.1-<slug>.md`, the hub is `../LESSON.md`. It carries the same twelve
    sections as any other part, which here mean:
    - **The story** — the problem the field had *before this document existed*. A scene, plain
      words, no jargon and no equations. Someone was stuck; this is what stuck looked like. The
      four story rules in item 25 apply here too: a setting the reader has lived in, simple words,
      load-bearing, and no collision with another story in the same day.
    - **The idea in plain language** — the claim, stated so a reader who has never opened a paper
      can hold it and repeat it. Define the terms the paper's own title uses.
    - **Why Sutra needs it** — the part of this day, linked, that runs on this idea.
    - **The mechanism** — the method itself, written out at the depth the rest of the day is written
      at. **Not the abstract, paraphrased.**
    - **When it breaks** — where the claim does **not** hold: what it assumed, the benchmark it was
      measured on, the scale it was never tried at, the follow-up that narrowed it. A paper part
      with no limits section has taught a press release.
    - **In production** — **what survived and what did not**: which half of this document is in
      shipped systems today, which half the field quietly dropped, and what replaced it. This is
      the section that makes a paper part worth reading rather than citing.
    - **The paper in one demo** — the paper **made runnable and stripped to nothing but itself**.
      Four rules, and the third is the one that makes it honest:
      1. **Only the paper's feature.** Not a small app that uses the idea — a small project whose
         entire reason to exist *is* the idea. Subtractive test: if a file could be deleted and the
         claim still lands, delete it. Two or three files is normal.
      2. **End to end and actually runnable.** Give the whole file tree, every file's contents, the
         one command, and its **real pasted output**. If the demo needs a live model and you have
         not run it, leave the output block as a `TODO(me)` naming the exact command — **never an
         invented transcript.** Principle 10 outranks the document's shape: a missing output is
         fixed by one run, a fabricated one is undetectable.
      3. **An ablation switch** — one flag that turns the paper's contribution **off**, with **both
         runs' output shown**. A demo that cannot be switched off proves that code ran, not that
         this idea changed the outcome. It is also an eval that can go RED (Principle 11).
      4. **Zero-budget** (Addendum 02): free tier or local, model string looked up live, 429
         handled. It lands in `lab/papers/<paper-slug>/` and is given **complete** — teaching
         material, not a rep. `TODO(me)` exercises stay in the hub's build brief.
    - **Check yourself** — one thing to run or find in the paper now, and one question out loud:
      *what did this paper actually claim, and what do we do differently now?*
28. Mermaid diagram whenever the concept is spatial, sequential, or a state machine — a graph
    runtime, a protocol handshake, a retry ladder, an approval gate.

## Step 5 — write the hub (`days/day-NN-<slug>/LESSON.md`)

29. The hub orients and assembles; **it never teaches**. No `Line by line:` in the hub. Required
    sections, in order (§17.5):
    - YAML frontmatter (`day`, `phase`, `phase_name`, `title`, `ids`, `principles`, `kind`,
      `plan_version: "v2.2.1"`, `parts`, `generated`, `status`, `lab_scaffolded`, `commit`)
    - a **yesterday / today / tomorrow** blockquote — no time estimate
    - `## §1 Where we are` — a scene and an analogy, plain language, NO code, NO jargon
    - `## §2 The map` — a table of every part: number, linked title
      (`parts/01-<slug>/1.1-<slug>.md`), what
      it answers, `level`, grouped by section with one line saying what each *section* means.
      **No minutes column, ever.** If the day has a `papers/` directory, the map ends with a table
      of those too (`papers/01-<slug>.md`), marked as read-after-the-parts.
    - `## §3 Setup — run this` — every `mkdir`, `touch`, `uv add` the day needs, pinned
    - `## §4 Build brief` — files to create, with `TODO(me)` markers left unsolved
    - `## §5 The eval that must be able to fail` — the check that is RED before the TODOs are done
    - `## §6 Request budget` — model calls per provider in RPM/RPD (`0` is an answer; state it)
    - `## §7 Traps` — the mistakes that eat an evening, including the named 1.x→2.x trap
    - `## §8 Verify before you code` — live docs URLs, actually fetched, never from memory
    - `## §9 Say it in an interview` — one paragraph, spoken voice
    - `## §10 Done when` — pointer to `CHECKLIST.md`, defined by understanding and green checks
    - `## §11 Ledger & commit` — the verbatim `PROGRESS.md` row, any `PACKAGES.md`, `PAPERS.md`
      and `SKILL_PROVENANCE.md` rows, and the commit message `day NN: <title> — closes <IDs>`.
      **The hub ends here.**

## Step 6 — the checklist (`days/day-NN-<slug>/CHECKLIST.md`)

30. Demo command, setup boxes, **one box per part document** (read it, run its check-yourself,
    answer its out-loud question), build-brief boxes, a test box per test **including at least one
    "break it, watch it go red, fix it"**, the request budget, the ledger rows pasted, and the
    commit box. No time estimates.

## Step 7 — verify

31. Run `./m depth $ARGUMENTS`. **Fix every failure; never hand-wave past one.**
32. Run `./m trace` — the day's IDs must match §14 exactly, no more and no fewer.
33. Run `./m tracker`.
34. Finish by printing: today's IDs, the part count, the demo command, the request budget, and the
    adk.dev / spec pages you actually fetched.

---

## Always

- Honor `CLAUDE.md`: exact pins · doc-first · build-first-compare-after · read-only by default ·
  at least one check that can go red · zero-budget model calls with 429 handling.
- **Grammar and punctuation are part of the deliverable, in every section and not just the story.**
  Full stops and commas where they belong, no run-on sentences, and no long chain of em-dashes
  where two ordinary sentences would read better. The reader is reading in a second language and
  learns from these documents alone; a sentence they have to parse twice is a sentence that failed.
- Do **not** solve the `TODO(me)` sections, and do **not** write project code. The learner types
  every line of `sutra/`. Teach; don't do the reps.
- Never name a person, instructor, author, channel, academy, bootcamp or training company anywhere
  in the output. The plan is self-contained and cites no external course; do not invent a lineage
  for it. Tool and library names are required and fine, as is citing a specification by its
  revision date and **a paper by its exact title and arXiv ID or DOI** — which is precisely why a
  Sutra citation names the work and never its authors.
- The failures this format exists to prevent (§17.8): splitting without deepening · summary in
  place of explanation · **stopping at the toy example** · assuming the previous day · code without
  failure · **trimming to fit** · solved reps · carrying a legacy clock across. If a part gained no
  story, no mechanism, no failure text and no production section versus the legacy prose, it is not
  done.

# 📓 Plan Changelog — Project Sutra

Principle 14: *if reality changes, the plan is amended first.* Every amendment lands here before
any day or any code changes. **Append-only. Newest last.**

*(Rows dated 2026-08-12 … 2026-08-21 are carried forward verbatim from `legacy/ledgers/CHANGELOG_PLAN.md`,
which is frozen. This file continues that history.)*

---

- 2026-08-12 — Addendum 01 merged (MCP 2026-07-28 spec; AG-31..34; ADK-73..78).
- 2026-08-12 — Addendum 02: zero-budget model policy (free tiers only; Days 9/16/70/74-78/86-88 amended).
- 2026-08-13 — Plan file lost and reconstructed as v1.2.0-R from CLAUDE.md, Addendums 01–02, ledgers, and sibling-plan structure. Both addendums folded in; ID total fixed at 199. See ADR-0001.
- 2026-08-13 — Model repin: `gemini-2.5-flash` is closed to new accounts (live call returns 404 "no longer available to new users" even though the model still appears in the docs and in `models.list()`). Primary → `gemini-3.5-flash`; lite lane → `gemini-3.5-flash-lite` (the stable Flash pair this project's key can call; `gemini-3.5-flash` verified by live call + usage metadata, still a thinking-by-default model). Plan §14 Day 5 amended (Addendum 02 left as its dated 2026-08-12 baseline — read its `gemini-2.5-flash` mentions as the repinned model); plan v1.2.0-R → v1.2.1-R.
- 2026-08-21 — Phase 16 (Days 97+, free multi-cloud deployment *implementation*, hands-on) added
  as an extension appended after the plan's Day 96 end — not a change to §14's 199 IDs or 15
  phases, which are unchanged and unedited. Own ledger (`DEPLOY_TRACK_TRACKER.md`), own ID prefix
  (`DEPLOY-NN`), own ADR. See ADR-0002.

---

## v2.0.0 — 2026-08-23 — the depth contract

**Trigger.** Review of the 107 written v1.2.1-R day documents found the single-file format had
failed the plan's own Principle 3. Days averaged ~471 lines with an entire subject under one `##`
heading; every one of the 107 carried an `estimated hours` header field, which is a standing
invitation to cut an explanation when a day runs long. A reader could not revisit one subtopic
without re-reading its neighbours, and nothing in the repo distinguished a thinly-covered subtopic
from a missing one. Full analysis and the options rejected: `docs/adr/ADR-0003-depth-contract.md`.

**Amendment.**

- New **Principle 16 — depth over density.** A day is taught as a hub plus one document per
  subtopic, never as one long page.
- New **Principle 17 — a day is a unit of subject, not a unit of time.** No document carries a time
  estimate, an `estimated hours` field, a duration or a pace. Nothing is ever trimmed to fit a
  schedule; a day that runs long gets another part, not a shorter explanation.
- New **Principle 18 — assume no prior knowledge, finish at production.** Every subtopic opens
  where a reader who has never met the idea can stand — jargon defined on first use, including
  jargon from earlier days, with a link back — and closes with the real-system version: what a
  senior engineer writes instead, what breaks at scale or under concurrency, the review comment,
  the interview question.
- **§17 replaced** — was *The Day Document Contract* (the eight-section single file), now
  *The Depth Contract*: the three commitments, the folder shape, the `<section>.<subtopic>`
  numbering rule, the **ten** required sections of a part document (adding *The story* and a
  mandatory *In production*), Sutra's four additional part rules (never invent an API · never
  invent a version · every model mention obeys Addendum 02 · name the 1.x→2.x trap), the **eleven**
  required hub sections, the `level` ladder (`foundation → working → production`), splitting by
  idea boundary rather than length, the eight failure modes this replaces, and enforcement.
- **§18 rewritten** to match: the register, the scene format (kept from v1.2.1-R unchanged), code
  and command rules, fact rules, the two things that are never written, and the closing ritual.
- **Day 0 added** (§14, new Phase 0): toolchain, skeleton, the `./m` driver, the first commit.
  **It closes no curriculum IDs**, which is what keeps `TRACEABILITY.md` valid across the
  amendment. Day 1 keeps AG-01, OPS-01, OPS-02, OPS-03 unchanged. Plan is now 97 days, 16 phases.
- **Days move** from `docs/days/day_NNN.md` to `days/day-NN/{LESSON.md, CHECKLIST.md, parts/, lab/}`.
- **Ledgers move** from `docs/days/` to `docs/`, because `docs/days/` no longer exists.
- **Tooling moves** `tools/` → `scripts/`, and gains `depth_check.py` (enforces §17 mechanically,
  including a hard failure on any time estimate found in a day folder) and `tracker.py` (reports
  the part count of every written day, so a thin day is visible from the progress table alone).
- **`make check` → `./m check`.** New `./m` driver script — `check`, `depth`, `start`, `parts`,
  `scaffold`, `tracker`, `status`, `done`. A two-line `Makefile` shim keeps `make check` working.
  `./m done N` refuses to commit while `CHECKLIST.md` has an unticked box.
- **New skill** `.claude/skills/day-sutra/SKILL.md` replaces the freeform "generate day N" prompt.

**Explicitly unchanged.** No curriculum ID, no phase boundary for Days 1–96, no gate, no model
policy, no addendum and no principle 1–15 is touched. The 96-day arc and all 199 IDs are identical
to v1.2.1-R. This is a documentation-format and documentation-depth amendment only.

**On the day count.** Principle 17 does not shorten or lengthen the curriculum — it removes the
*clock* from it. Day numbers remain an index into the subject. A day whose subject is large is not
compressed to fit an evening; it is read across as many sittings as it needs, and `./m done N` is
gated on a ticked checklist and green checks, never on elapsed time.

**Migration.** All 107 v1.2.1-R day documents were moved with `git mv` to `legacy/days/` on
2026-08-22 (nothing deleted; `git log --follow` intact), together with the v1 ledgers
(`legacy/ledgers/`), the deployment guide (`legacy/deployment/`, still factually current), the v1
product code written on days 1–8 (`legacy/code/`) and a frozen copy of the plan at v1.2.1-R
(`legacy/docs/`). `sutra/.adk/session.db` — a committed SQLite runtime artifact — was removed from
tracking and added to `.gitignore`. Days are regenerated in the v2.0.0 shape from Day 0 forward.

- 2026-08-23 — Day 0 written: **17** parts across 4 sections. Toolchain versions verified live that
  day (`git 2.54.0.windows.1`, `uv 0.12.3`, CPython 3.12.13, `ruff==0.16.4`, `pytest==9.1.1`); rows
  in `docs/PACKAGES.md`. Day 0 adds **no runtime dependency** — `dependencies = []` — because
  packages arrive on the day they are first used.
- 2026-08-23 — §17.4/§17.9 clarified while writing Day 1: *Line by line* is the contract's only
  **conditional** section. It is required exactly when a part holds a code block that needs a
  walkthrough, and is not asked for when the part holds none — a `concept` part (§17.7) may
  legitimately carry no code at all, and demanding a walkthrough there produced empty ceremony
  rather than depth. `scripts/depth_check.py` updated to match. No other section became optional.

---

## v2.1.0 — 2026-08-23 — folder names that say what is inside

**Trigger.** With two days on disk the tree already read as `days/day-00/parts/01/`,
`days/day-01/parts/03/` — eight folders whose names carry no information at all. Extended to 97
days that is ~400 numbered folders, none of which answers *what is in here?* without opening a file.
The number is a good key and a bad label, and the cost lands exactly where the repo is supposed to
be strongest: Principle 2 says the repo is the memory, and a memory you have to open to read is a
weak one.

**Amendment.** §17.2 only. **No principle, ID, phase boundary, gate, model policy or part-document
rule changed.**

- Every day folder is `days/day-NN-<slug>/`; the slug is the hub's `title`, kebab-cased, articles
  dropped, 1–4 words.
- Every section folder is `parts/NN-<slug>/`; the slug is the section's heading in the hub's §2 map,
  1–3 words.
- **The number stays the identity.** Every tool resolves a day by number and accepts any slug after
  it, so a folder can be renamed to a better slug without breaking `./m`, `scripts/depth_check.py`,
  `scripts/tracker.py` or `scripts/trace.py`. Slug-tolerance is what makes this safe to apply to
  days that are already written.
- Part *filenames* are unchanged — `1.1-<slug>.md` already carried a full slug.
- `scripts/depth_check.py` now requires the slug on both folder kinds and rejects a bare `parts/01/`.

**Migration.** `days/day-00/` → `days/day-00-toolchain-skeleton-driver/` and `days/day-01/` →
`days/day-01-bootstrap-and-map/`, with their eight section folders, moved by `git mv` (history
intact). Hub §2 maps, cross-part relative links and `prev`/`next` frontmatter rewritten to match.
`docs/CURRICULUM_INDEX.md` and `docs/TRACEABILITY.md` regenerate their links from disk. See
ADR-0004.

---

## 2026-08-24 — ADR number collision: provider-roles renumbered 0004 → 0005

**Not a plan change.** No section of `docs/00_MASTER_PLAN.md` moved, and the depth contract is
untouched. This records a numbering correction, logged here because an ADR number is an identity and
Principle 14 says a change of this kind is written down before it is acted on.

**What happened.** Day 1 was generated on 2026-08-23 and its build brief named
`docs/adr/ADR-0004-provider-roles.md`. Later the same day, plan v2.1.0's folder-slug decision was
recorded as `ADR-0004-folder-slugs.md` and committed. Two decisions then held one number, and Day 1's
checklist grepped a filename that pointed at the wrong document.

**Resolution.** The committed ADR keeps its number:

- `ADR-0004-folder-slugs.md` — unchanged. `00_MASTER_PLAN.md` §revision-history and this changelog's
  v2.1.0 entry still refer to it correctly.
- `ADR-0004-provider-roles.md` → **`ADR-0005-provider-roles.md`**. Every reference inside
  `days/day-01-bootstrap-and-map/` updated: `LESSON.md` §4 and §11, `CHECKLIST.md` (four boxes),
  `parts/02-repo-as-memory/2.3-the-adr-that-survives-a-cold-read.md`, and
  `parts/03-keys-and-env/3.1-the-three-free-doors.md`.

**Why this way round.** The folder-slug ADR was committed first and is cited from the plan itself;
renumbering it would invalidate a reference in the plan's revision history. The provider-roles ADR
was still untracked, so it was the cheaper of the two to move.

**Guard for next time.** ADR numbers are allocated when the file is created, not when the day that
needs it is written. A day document generated ahead of time must re-check `ls docs/adr/` before
claiming a number.

---

## 2026-08-24 — the model roster moved, and so did the API surface

**Trigger.** Day 2 (AG-02) is the first day Sutra calls a model, so it is the first day that had to
look the provider up rather than inherit an assumption. Five lookups, all on 2026-08-24, all
recorded in `days/day-02-llm-mechanics/LESSON.md` §8:

1. `pypi.org/pypi/google-genai/json` → **2.19.0** (uploaded 2026-08-19), not the 2.18.0 the
   v1.2.1-R legacy day pinned.
2. `ai.google.dev/gemini-api/docs/models` → the Flash roster now lists **`gemini-3.7-flash`** and
   **`gemini-3.6-flash`** above the `gemini-3.5-flash` this project pinned on 2026-08-13.
3. `ai.google.dev/gemini-api/docs/quickstart` → the entire Python sample is now
   **`client.interactions.create(...)`**, and the `generate_content` pages have been retitled
   **"Gemini Generate Content API (Legacy)"**.
4. `ai.google.dev/gemini-api/docs/interactions` → Interactions **runs on the free tier**; the
   free/paid difference is retention (one day versus fifty-five), not access. `store=True` is the
   default.
5. ADK release notes → **`gemini-2.5-flash` shuts down 2026-10-16**, and ADK v2.2.0 has already
   moved `LlmAgent`'s default off it; ADK reaches the new surface with `use_interactions_api=True`.

**Amendment.**

- **Primary model repin: `gemini-3.5-flash` → `gemini-3.7-flash`.** The model Google's own current
  quickstart uses. Plan §14 Day 5's parenthetical pin and Addendum 02 §5's Days 5–8 row are read as
  repinned; neither file is edited, because both are dated baselines and Principle 7 keeps the
  observation, not the guess. The standing rule from 2026-08-13 is unchanged and now doubly earned:
  **listed ≠ callable — only a live call proves access.**
- **`gemini-2.5-flash` is recorded as end-of-life 2026-10-16.** Addendum 02 §3's table still names
  it as a free workhorse; that table is its dated 2026-08-12 baseline and stays frozen. Read every
  `gemini-2.5-flash` mention in the addenda as the current repin.
- **Teaching surface: the Interactions API, from Day 2 onward.** `client.interactions.create(...)`,
  `interaction.output_text`, `interaction.usage`. Sutra's house shape is **`store=False` with an
  explicit history**, so context management stays visible and Day 3's hand-rolled loop keeps its
  reason to exist. `previous_interaction_id` is taught and then declined, with the reason recorded.
- **`generate_content` becomes a 🅿️ parked part** — awareness-level, interview-ready, not built on
  — because the learner will meet it in every tutorial and older repository they open. It names
  `use_interactions_api=True` as the bridge forward to Day 5.
- **No change to §14's IDs, phases or day count.** Day 2 still closes AG-02 and only AG-02. This is
  an amendment to *which surface a day teaches*, not to what it teaches.

**Rationale and the options rejected:** `docs/adr/ADR-0006-interactions-api-first.md`.

**Consequences for later days.** Day 3's hand-rolled loop is unaffected — `store=False` makes the
history list explicit, which is precisely what the loop iterates. Day 8 (ADK-06, ADK-07) gains a
comparison it did not previously have: ADK's session service against the Interactions API's
server-side state, two answers to one question. Day 24's budget arithmetic reads
`interaction.usage.total_thought_tokens` rather than the old `thoughts_token_count`.

---

## 2026-08-25 — the Interactions API has its own error hierarchy, and Day 2's door missed it

**Trigger.** Implementing Day 2's lab against the pinned `google-genai==2.19.0`. The day's own
promise — *every model call goes through one door that backs off using the delay the server stated* —
was tested against a real 429 from `gemini-3.7-flash` and **did not hold**. Four facts, verified on
2026-08-25 against the installed package and one live response:

1. `client.interactions.create(...)` raises from `google.genai._gaos.lib.compat_errors`, a hierarchy
   rooted at `GeminiNextGenAPIClientError`, with `RateLimitError` (429), `AuthenticationError` (401)
   and `BadRequestError` (400) below it.
2. **It is not the legacy hierarchy.** `issubclass(compat_errors.RateLimitError,
   google.genai.errors.APIError)` is `False`, so part 1.5's `except errors.APIError` caught nothing.
   Reproduced with a fake client: a 429 escaped after **one** call, with zero retries.
3. The status attribute is **`.status_code`**; `.code` does not exist on those classes.
4. The live 429 body carries **`Please retry in 52.320368558s.`** and no `retryDelay` field, so
   `_retry_wait` returned **1.0 s** — the 1-2-4 backoff the part exists to argue against.

Checked and cleared: `gemini-3.7-flash` is callable on this key, and `temperature` still reaches the
wire despite being absent from 2.19.0's typed `GenerationConfigParam`, because `GenerationConfig` is
declared `extra: "allow"`.

**Amendment.**

- **Sutra's door catches `compat_errors.APIError` and branches on `error.status_code`.** The import
  is a private path (`google.genai._gaos.lib`); the SDK publishes no public alias in 2.19.0, so the
  path is named in the code and **pinned by a test** that goes red if the SDK moves it.
- **`_RETRY_DELAY` accepts both phrasings** — `retryDelay: '47s'` and `Please retry in 52.3s` — same
  capture, same `+ 1.0` margin. The exponential fallback stays the last resort.
- **`days/day-02-llm-mechanics/` updated:** `parts/01-first-contact/1.5-the-only-door-429.md` (the
  mechanism, its line-by-line, the real 429 body in *When it breaks*, and *Check yourself*),
  `LESSON.md` §5, §7 and §8, and `CHECKLIST.md`. Day 2's test count goes from four to six, so the
  suite reports **10 passed** rather than 8.
- **The `google.genai.errors.ClientError` tracebacks elsewhere in Day 2 are kept and relabelled** as
  the *legacy* surface's shapes, which is what they are — and which is now a live argument for why
  part 6.1 parks that surface instead of deleting it.
- **No change to §14's IDs, phases or day count.** Day 2 still closes AG-02 and only AG-02.

**Rationale and the options rejected:** `docs/adr/ADR-0007-interactions-error-hierarchy.md`.

**Consequences for later days.** Day 3's loop calls `ask` and inherits a door that now actually
retries. Day 9 (ADK-08, ADK-09) benchmarks four providers and will meet three more error
taxonomies — the private import and the single-phrasing regex are the first evidence that Day 72's
retry work needs a provider-neutral error classifier, not just jitter. Day 72 (SEC-15, OPS-13)
inherits both.

**Guard for next time.** A day document written the day before its lab is written is a day whose
error shapes are **claims, not observations**. Principle 8 says verify the API on the day it is used;
this is the first case where the gap between those two days produced a defect, and the tell was
cheap — one fake client and one real 429.

---

## v2.2.0 — 2026-08-25 — the paper behind it

**Trigger.** The depth contract asks a part what an idea *is*, why Sutra needs it, how it works, how
it breaks and what changes in production. It never asks **where it came from** — and for much of
this curriculum that question has one precise, public answer per idea. The reason-then-act loop
hand-rolled on Day 3, the sampling dial on Day 2, the tokenizer whose receipt Day 2 reads, the
tool-calling round trip built on Day 4: each traces to a document a reader can open. Meeting them
only as framework features teaches the framework; meeting the origin teaches the field, and shows
**which half of the original proposal survived contact with production** — because in each of these
cases some of it did not. Rationale and the options rejected:
`docs/adr/ADR-0008-paper-provenance.md`.

**Amendment.**

- **New §17.4.2 — the paper part.** A paper is an idea, and §17.1 gives one idea one document, so a
  paper this curriculum leans on is taught in **a part of its own**: one part per paper, written to
  the same eleven-section contract as every other part, declaring `paper:` (singular) in its
  frontmatter. On a paper part the sections take their natural meanings — *The story* is the problem
  the field had before the document existed, *The mechanism* is the method written out rather than
  the abstract paraphrased, *When it breaks* is where the claim does not hold, and *In production*
  is **what survived and what did not**.
- **Paper parts are the day's last section.** Principle 4 at the scale of a day: hand-roll the
  mechanism, *then* read the proposal. A reader who has just written the loop by hand can be told
  which half of the paper they reinvented; a reader who meets the paper first skips it.
- **§17.4 gains row 6, *The paper behind it*** — an **address, not an explanation**. Between *Why
  Sutra needs it* and *The mechanism*, a citing part carries the citation block, one sentence of the
  claim, and a **link to the paper part**. Nothing duplicated, nothing dangling — which is the
  no-shortcut test satisfied rather than waived.
- **The section is conditional and declared, not guessed.** It is required exactly when the
  frontmatter declares `papers:`, and vice versa. `./m depth` checks that the pair agrees — a
  question it can answer, unlike "does this idea have a paper?", which it cannot.
- **A paper is taught once in the whole curriculum.** The day that first needs it carries the part;
  every later day links to it. Two parts declaring the same `paper:` is a depth-check failure.
- **New §17.4.1 rule 5 — never invent a citation.** Principle 7 pointed at the literature, and
  stricter than the version case: a wrong pin fails loudly on the next `uv sync`, while a plausible
  arXiv ID attached to the wrong title fails silently for years. The record is looked up live on the
  day the part is written, the title copied from the record and not from memory. An unverifiable
  paper leaves a `TODO` with the exact lookup command.
- **New ledger `docs/PAPERS.md`** — append-only, one dated row per paper, joining PROGRESS, PACKAGES
  and SKILL_PROVENANCE in §16. `./m depth` rejects an identifier with no row.
- **§18.1 rule 5 is unchanged in force and clarified in scope.** A paper is cited by title and
  identifier, **never by its authors**. `arXiv:1706.03762` resolves to exactly one document, which
  is stricter attribution than a surname and a year, and the promise that this curriculum promotes
  nobody stays whole.
- **No ID, phase boundary, gate, model policy, folder rule or principle changed.** 199 IDs, 15
  phases, 97 days, all as they were.
- **Days 0–5 retrofitted in place** and moved to `plan_version: "v2.2.0"`.

---

## v2.2.1 — 2026-08-26 — the story must be one the reader has lived

**Trigger.** A read-through of Days 0–5 as far as part 3.3 found every *The story* section
technically compliant with §17.4 row 3 — a concrete scene, no jargon, placed first — and landing
badly all the same. The settings were a nautical chart, a 1904 city fire, a theatre programme, a
projection booth, a model railway and a controlled forestry burn. Each one is a scene the reader has
to have explained to them before the analogy can do any work, which places a second unfamiliar thing
in front of the unfamiliar thing they came for, and spends exactly the attention the hook was meant
to buy. Two further faults showed up in the same read: Day 5 reached for a restaurant in part 1.1 and
again in 5.2, and for a receptionist in 2.2 and again in 4.2, so two pairs of parts read as one idea
repeated; and the prose across all sections leaned on long chains of em-dashes where full stops would
have carried the sentence, which is expensive for a reader working in a second language.

**Amendment.**

- **§17.4 row 3 — four rules added to *The story*.** (a) A scene the reader has **plausibly lived
  in**: a parcel and a courier, a repair-shop job card, a bus route map, a used car checked by a
  mechanic, a monthly generator test. The test is whether the reader could have been standing in the
  scene themselves. (b) Simple words and short sentences. (c) **Load-bearing** — the scene holds the
  actual failure or decision the part teaches, and it still fits wherever a later section reaches
  back for it; a metaphor abandoned after its own section was decoration. (d) **One metaphor family
  per day**, checked against the day's other parts and the hub §1 before choosing.
- **§18.1 rule 1a — the same rule stated in the register**, with the reason: an unfamiliar setting is
  a second thing to learn, put in front of the first.
- **§18.1 rule 2 — grammar and punctuation are part of the deliverable**, in every section of every
  document rather than in the story alone. Full stops and commas where they belong, no run-on
  sentences, and no long chain of em-dashes where two ordinary sentences would read better. A
  sentence the reader has to parse twice has failed, however correct its content.
- **`.claude/skills/day-sutra/SKILL.md` and `CLAUDE.md` carry the same rules**, so a day written
  through the skill and a day written without it are held to one standard.
- **No ID, phase boundary, gate, model policy, folder rule, principle or required section changed.**
  199 IDs, 15 phases, 97 days, twelve sections, all as they were. Nothing about `./m depth` changed:
  this is a review-enforced rule, like the rest of §18, because no script can judge whether a reader
  has lived in a scene.
- **Day 5 parts 4.1–7.1 rewritten** under the new rule, and its 5.2 and 4.2 metaphor collisions
  resolved. **Days 0–4 are compliant as written and were not touched** — their stories are ordinary
  settings already.
- **Days 0–5 moved to `plan_version: "v2.2.1"`.**
- **No ADR.** This sharpens an existing row rather than adding a section, a kind of document or a
  ledger. ADR-0003 and ADR-0008 remain the record for the format itself.

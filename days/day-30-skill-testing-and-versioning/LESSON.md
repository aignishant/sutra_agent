---
day: 30
phase: 4
phase_name: "Agent Skills"
title: "Skill testing & versioning"
ids: ["SK-17", "SK-18", "SK-19"]
principles: [1, 2, 7, 8, 10, 11, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-04"
status: written
lab_scaffolded: true
commit: ""
---

# Day 30 — Skill testing & versioning

> **Yesterday (Day 29):** sourcing and auditing third-party skills — five passes with zero model calls,
> a poisoned fixture caught on three planted traps, provenance rows so the audited bytes are the bytes
> that run, and a security-clean pack that wrecked the routing gate anyway.
> **Today:** the shelf gets tests. Pure check functions over a skill folder, a suite that enumerates
> `skills/` live and can go red, skills built in memory so every rule can be proved to fire, and the
> versioning rule Day 27 left unwritten — with a content digest so a change to a reference file cannot
> slip past the version.
> **Tomorrow (Day 31):** the Phase 4 gate — `./m check` gains a skills linter built on today's
> functions and a `:free`-suffix linter, and the whole phase has to go green.

---

## §1 Where we are

Four days of skills, and every single thing they built rests on the contents of some Markdown files
staying correct.

Day 25 said a skill is a folder whose `name` must match it. Day 26 wired a shelf into the agent and
showed that one broken folder stops the whole thing starting. Day 27 moved the triage procedure out of
the agent's instruction and into a file, on purpose, so that somebody who writes no Python can fix a
severity rule. Day 28 proved the description is a routing decision, so a shortened one changes which
tasks reach which skill. Day 29 pinned sourced skills so the text you audited is the text that runs.

Every one of those is a property of a text file. None of them is protected by anything.

There is a card taped to the lid of the rice tin in a shared kitchen, and six people cook from it. One
evening somebody changes `four cups` to `three cups`, because four boiled over on them and they were
right — for their pot. They do not add "if you are using the small pot". The next four people cook hard,
dry rice and blame the rice. Nothing broke, nothing made a noise, and the card still looks exactly like
a card.

Today the card gets checked. Three moves, and they build on each other.

**A skill folder is source, so it gets checks that run on every commit.** Pure functions in
`tools/skill_checks.py` that take a folder and return findings — never print, never exit, never raise
because a skill is bad — so the same rules serve a test suite today and Day 31's merge gate tomorrow.
Three of the six rules are already enforced by ADK's own loader, so the checker calls the loader and
reports what it says rather than owning a second copy of the specification.

**The checks are proved to fire, using skills built in memory.** A green suite over a clean shelf means
either the shelf is clean or the checks do nothing, and only a test that hands a rule something broken
can tell those apart. `Skill(frontmatter=Frontmatter(...), ...)` builds the case without a folder, in
one line — and the rules that genuinely need a folder are named, kept in their own lane, and never
faked.

**A version is a name for one exact version of the text, and a digest makes it honest.** The version
is inert — ADK never reads it — and it is the only handle an audit, a log line and a bug report have
for naming which text answered. Day 27 named the hole: the version sits in `SKILL.md` and the skill is
a whole folder, so editing a rubric changes behaviour and moves nothing. Today a short hash of the
folder sits beside the version, so any content change forces somebody to look at the version field and
decide.

And the day ends where it should: a suite built to be wrong, run beside the honest one, reporting
success on a shelf holding a skill that will not load.

**Zero model calls. All of it.**

---

## §2 The map

Nineteen parts in six sections, plus **one paper**. The day climbs `foundation → working →
production`: section 1 is what a test over prose can and cannot know, section 2 builds the checks as
pure functions, section 3 turns them into a suite, section 4 is the in-code skill path, section 5 is
versioning, and section 6 is the synthesis and the deliberate failure.

### Section 1 — `01-testing-prose`: what a test over a skill can know (SK-17)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [Prose with consequences](parts/01-testing-prose/1.1-prose-with-consequences.md) | Why a Markdown file needs a test | `foundation` |
| 1.2 | [Shape and sense](parts/01-testing-prose/1.2-shape-and-sense.md) | The line the whole day sits on | `foundation` |
| 1.3 | [The rules worth a test](parts/01-testing-prose/1.3-the-rules-worth-a-test.md) | Three filters, six rules | `working` |

### Section 2 — `02-checks-as-functions`: the checks (SK-17)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [A finding is a return value](parts/02-checks-as-functions/2.1-a-finding-is-a-return-value.md) | The pure contract, and `tools/` | `working` |
| 2.2 | [Let the loader be the oracle](parts/02-checks-as-functions/2.2-let-the-loader-be-the-oracle.md) | Never re-implement the spec | `working` |
| 2.3 | [One bad folder must not stop the shelf](parts/02-checks-as-functions/2.3-one-bad-folder-must-not-stop-the-shelf.md) | Fail-fast runtime, complete checker | `working` |
| 2.4 | [Pointers that go nowhere](parts/02-checks-as-functions/2.4-pointers-that-go-nowhere.md) | Dead references, silently | `working` |

### Section 3 — `03-the-suite`: turning checks into tests (SK-17)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Enumerate the shelf, never a list](parts/03-the-suite/3.1-enumerate-never-list.md) | The failure mode that is a pass | `working` |
| 3.2 | [A failure must name the file](parts/03-the-suite/3.2-a-failure-must-name-the-file.md) | Messages a stranger can act on | `working` |
| 3.3 | [The test for the checker](parts/03-the-suite/3.3-the-test-for-the-checker.md) | A rule that never fired | `working` |

### Section 4 — `04-skills-built-in-code`: the in-code skill path (SK-18)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [One valid skill, one changed field](parts/04-skills-built-in-code/4.1-a-skill-without-a-folder.md) | The fixture factory | `working` |
| 4.2 | [The model is the spec](parts/04-skills-built-in-code/4.2-the-model-is-the-spec.md) | `Frontmatter` as an executable rule | `working` |
| 4.3 | [What memory cannot test](parts/04-skills-built-in-code/4.3-what-memory-cannot-test.md) | The three folder-bound rules | `production` |

### Section 5 — `05-versioning`: naming the text that ran (SK-19)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [A name for the text that ran](parts/05-versioning/5.1-a-name-for-the-text-that-ran.md) | What a version is, and is not | `foundation` |
| 5.2 | [The bump rule](parts/05-versioning/5.2-the-bump-rule.md) | Three bumps, three obligations | `working` |
| 5.3 | [The change the version missed](parts/05-versioning/5.3-the-change-the-version-missed.md) | The folder digest | `production` |

### Section 6 — `06-in-production`: where the three IDs meet

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The drill in the other building](parts/06-in-production/6.1-the-drill-in-the-other-building.md) | A green suite on a broken shelf | `production` |
| 6.2 | [Writing down what green means](parts/06-in-production/6.2-writing-down-what-green-means.md) | The boundary, as a passing test | `production` |
| 6.3 | [Fix the skill, never the check](parts/06-in-production/6.3-when-the-suite-goes-red.md) | Triage, in the right order | `production` |

### The paper — read after the parts

| Paper | What it argues | Read from |
| --- | --- | --- |
| [Hints on Test Data Selection](papers/01-hints-on-test-data-selection.md) | Judge a suite by whether it notices a deliberately broken program, not by what it executes | [3.3](parts/03-the-suite/3.3-the-test-for-the-checker.md), [6.2](parts/06-in-production/6.2-writing-down-what-green-means.md) |

**Read the paper last.** Principle 4 at the scale of a day: build the suite by hand, then read the
1978 result that tells you how to find out whether it would notice anything.

---

## §3 Setup — run this

**No package is added today.** `pytest==9.1.1` arrived on Day 23, `google-adk==2.7.1` on Day 5, and
`pydantic` comes with ADK. `git diff pyproject.toml uv.lock` must be empty when you finish.

```bash
# 1 - tools/ is a new top-level package, created today. Days 31 and 45 add modules to it.
mkdir -p tools
touch tools/__init__.py
touch tools/skill_checks.py

# 2 - the suite
touch tests/test_skills.py

# 3 - the paper demo, given whole (teaching material, not a rep)
cd days/day-30-skill-testing-and-versioning
mkdir -p lab/papers/hints-on-test-data-selection
touch lab/papers/hints-on-test-data-selection/checks.py
touch lab/papers/hints-on-test-data-selection/suite.py
touch lab/papers/hints-on-test-data-selection/demo.py
cd -

# 4 - confirm the shelf you are about to protect is the one Day 27 and Day 28 left
ls skills/
```

**`tools/` is not `sutra/`.** Nothing in it ships: `pyproject.toml` lists only `sutra` and `sutra_mcp`
as wheel packages, so `tools/` is repository machinery that checks the product and is never part of
it.

**Nothing under `sutra/` changes today.** The only edits to `skills/` are to the frontmatter of your
own skills — adding `metadata.digest` beside the version that is already there — and one paragraph
appended to `skills/README.md`, which is [5.2](parts/05-versioning/5.2-the-bump-rule.md)'s bump table
and the `TODO(me)` Day 27 left open.

**Everything runs on static analysis, hashing and the filesystem.** There is no live model call
anywhere in this day.

---

## §4 Build brief

**`tools/__init__.py`** — empty, and it stays empty. It exists so `from tools.skill_checks import ...`
resolves from anywhere in the repository rather than only from the root
([2.1](parts/02-checks-as-functions/2.1-a-finding-is-a-return-value.md)).

**`tools/skill_checks.py`** — the module, given complete across section 2 and
[5.3](parts/05-versioning/5.3-the-change-the-version-missed.md). Public surface, and Day 31's linter
imports exactly this:

| Symbol | What it is |
| --- | --- |
| `Finding(skill, rule, detail)` | a frozen dataclass; `__str__` fixes the three-column layout |
| `load(folder) -> (Skill \| None, list[Finding])` | the ADK loader, wrapped, never raising |
| `check_description(skill)` | the description says **when** |
| `check_references(folder, skill)` | every resource path in the body resolves |
| `check_version(skill)` | `metadata.version` present, a string, `N.N` or `N.N.N` |
| `check_body_length(skill)` | the body is under 500 lines |
| `folder_digest(folder) -> str` | a twelve-character hash over the whole folder |
| `check_digest(folder, skill)` | the recorded digest still covers the folder |
| `check_skill(folder)` | every check over one folder, cheapest first |
| `check_shelf(shelf)` | every check over every folder, enumerated live |
| `MAX_BODY_LINES`, `RESOURCE_DIRS`, `WHEN_WORDS`, `DIGEST_KEY`, `DIGEST_LENGTH` | the thresholds, importable |

**`tests/test_skills.py`** — three lanes, named in the module docstring
([6.2](parts/06-in-production/6.2-writing-down-what-green-means.md)): the shelf lane
([3.1](parts/03-the-suite/3.1-enumerate-never-list.md)), the checker lane
([3.3](parts/03-the-suite/3.3-the-test-for-the-checker.md), built on
[4.1](parts/04-skills-built-in-code/4.1-a-skill-without-a-folder.md)'s `a_skill` factory), and the
boundary lane.

**`skills/*/SKILL.md`** — each first-party skill gains `metadata.digest` beside its existing
`metadata.version` and `metadata.changed`. Stamp the value by running the command in
[5.3](parts/05-versioning/5.3-the-change-the-version-missed.md); the value is yours and there is
nothing to copy from these documents.

**`skills/README.md`** — the bump table from [5.2](parts/05-versioning/5.2-the-bump-rule.md), beside
the four-container table Day 28 put there. This closes Day 27's open `TODO(me)`.

**The paper demo** — `lab/papers/hints-on-test-data-selection/`, given whole in the
[paper part](papers/01-hints-on-test-data-selection.md): three files, nine mutants, an ablation
switch, no model.

**`TODO(me)` markers left for you:**

- **1.3** — propose one seventh rule for the list, run it through the three filters in writing, and
  record the verdict in `skills/README.md` whether it passes or fails.
- **2.2** — decide what `check_skill` should do about a skill folder that ADK loads but whose
  `license` field is absent, given Day 29's *no licence, no run*, and say which of the three filters
  your answer rests on.
- **2.4** — write the mirror check: files under `references/` that no body mentions. Run it on your
  shelf and decide whether an orphan is a finding or a warning.
- **3.1** — decide the point at which enumerating the whole shelf on every commit stops being free,
  and write down what you would change first.
- **3.3** — pick one rule and delete a single token from its implementation, then find out which test
  goes red. If none does, write the test.
- **4.2** — the frontmatter model allows extra keys, so `licence:` is silently kept and ignored.
  Decide whether Sutra wants a rule about unknown frontmatter keys, and what it would cost.
- **4.3** — decide when Sutra should start committing broken fixture folders under
  `tests/fixtures/skills/` for the three folder-bound rules, and what the trigger is.
- **5.2** — apply the bump table to the last three commits that touched `skills/` and record, for
  each, the bump it should have had and whether the obligation was met.
- **5.3** — decide Sutra's policy on generated files inside a skill folder, given that any of them
  makes the digest churn.
- **6.1** — find one other check in this repository whose inputs are a hand-maintained list rather
  than an enumeration, and say what would happen when it goes stale.
- **The paper** — add one test to the demo's `suite.py` and watch a named survivor disappear. Then
  write down which of the seven survivors you would fix first and why.

---

## §5 The eval that must be able to fail

Three checks, each red or green, none of them spending a generation.

**One — the shelf lane, which must be green and must be able to go red.**

```bash
uv run python -m pytest tests/test_skills.py -k shelf
```

Then break it on purpose and confirm it notices:

```bash
printf 'S3 - cosmetic.\n' >> skills/ticket-triage/references/severity-rubric.md
uv run python -m pytest tests/test_skills.py -k shelf
git checkout -- skills/ticket-triage/references/severity-rubric.md
```

`SKILL.md` is never opened, and the middle run reports `stale-digest` — the digest rule from
[5.3](parts/05-versioning/5.3-the-change-the-version-missed.md) doing the only thing it exists to do.

**Two — the checker lane, which proves each rule fires.**

```bash
uv run python -m pytest tests/test_skills.py -k "check_" -v
```

Measured on 2026-09-04 against a reconstruction of the shelf, the whole file reports `13 passed`.

**Three — the deliberate failure, run once and deleted.** Build the stale suite from
[6.1](parts/06-in-production/6.1-the-drill-in-the-other-building.md), plant `skills/Bad--Name/`, and
run both files together. Measured the same day:

```text
FAILED tests/test_skills.py::test_every_skill_on_the_shelf_passes_every_check
1 failed, 13 passed in 0.27s
```

The one that failed is the enumerating test. `test_the_shelf_passes` — the one with the hardcoded list
— is among the thirteen that passed, on a shelf holding a folder ADK refuses to load.

**And the paper demo, both arms, no model:**

```bash
cd days/day-30-skill-testing-and-versioning/lab/papers/hints-on-test-data-selection
python demo.py
MUTATION=off python demo.py
```

Measured the same day: with mutation on, `mutation score: 2/9 killed` and exit 1 — a suite of five
passing tests that cannot tell seven broken versions of the program from the real one. With
`MUTATION=off`, the same five tests pass and the report stops at *"the suite is green"*.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04). Today spends none of them.

| What | Generations |
| --- | --- |
| `tools/skill_checks.py` and every check in it | **0** (the ADK loader, string matching, `hashlib`) |
| `tests/test_skills.py`, all three lanes | **0** |
| the in-code skills of section 4 | **0** (`Frontmatter` and `Skill` are pydantic models, not calls) |
| `folder_digest` and the digest check | **0** (hashing) |
| the deliberate-failure run in 6.1 | **0** |
| the paper demo, both arms | **0** (source rewriting and `exec`, no model) |
| **Total planned** | **0 of 20** |

**Zero, and it is a design requirement rather than a saving.** A check that spends quota cannot run on
every commit against a twenty-a-day budget, so it is a check that will be switched off — and Day 31
turns exactly these functions into a merge gate. Whether a description still *routes* is the one
question here that a model could help with, and it belongs in Day 28's routing gate on a different
trigger, not in the always-on lane
([1.2](parts/01-testing-prose/1.2-shape-and-sense.md)).

**Cost: $0.**

---

## §7 Traps

- **A green suite proves the shelf is clean *or* that the checks do nothing.** Only a test that hands
  a rule something broken tells the two apart (3.3).
- **A hardcoded list of skills fails by passing.** Add a skill, forget the list, and coverage drops
  silently while the suite stays green (3.1, 6.1).
- **`load_skills_from_dir` raises on the first bad folder.** Right for the runtime, wrong for a
  checker — you get one problem per run (2.3).
- **Re-implementing the spec's name rule creates a second copy that drifts.** ADK normalises the name
  with Unicode NFKC before matching; your regular expression does not (1.3, 2.2).
- **`except Exception` in `load` reports a `UnicodeDecodeError` in a reference file as an invalid
  skill.** Catch the two documented types; `ValidationError` arrives through `ValueError` (2.2).
- **Unquoted `version: 1.10` is the float `1.1`.** A digit vanishes from every log line the skill ever
  produces (5.1).
- **A reference-file edit moves nothing in `SKILL.md`.** The version keeps naming a folder that has
  changed, which is what the digest exists to catch (5.3).
- **Re-stamping the digest to clear a red check throws the finding away.** Red means decide the bump,
  then re-stamp — the same rule as never re-pinning first (5.3, 6.3).
- **A reference path pattern that swallows the sentence's full stop reports `scripts/check.py.`** One
  false finding costs a linter its credibility permanently (2.4).
- **`Frontmatter` allows extra keys.** `licence:` instead of `license:` is kept, ignored, and looks
  fine (4.2).
- **An in-memory test of the reference rule compares two things the test author wrote.** It passes
  forever and proves nothing (4.3).
- **A shape checker with an opinion about sense collects exemptions until it means nothing** (1.2,
  6.3).
- **A skip marker with "will fix" in the comment survives for years.** `1 skipped` is a line eyes pass
  over (6.3).
- **A version bumped in a follow-up commit was wrong for as long as the two commits were apart**
  (5.2).

---

## §8 Verify before you code

Run or read on **2026-09-04**, the day this was written:

- **The installed `google-adk` 2.7.1**, driven directly for every ADK fact in the day.
  `google/adk/skills/__init__.py` exports `Skill`, `Frontmatter`, `Resources`, `Script`,
  `SkillRegistry`, `load_skill_from_dir`, `load_skills_from_dir` and their async and GCS variants in
  `__all__` ([2.2](parts/02-checks-as-functions/2.2-let-the-loader-be-the-oracle.md),
  [4.1](parts/04-skills-built-in-code/4.1-a-skill-without-a-folder.md)). `models.Frontmatter` carries
  the four field validators the day tests against, and is declared `extra="allow"`, so an unknown key
  is kept rather than rejected ([4.2](parts/04-skills-built-in-code/4.2-the-model-is-the-spec.md)).
  `_load_skill_from_dir` raises `FileNotFoundError`, `ValueError` and pydantic's `ValidationError`,
  and performs the name-versus-directory comparison itself; `_load_skills_from_dir` appends in a plain
  loop, so one bad folder raises for the whole shelf
  ([2.3](parts/02-checks-as-functions/2.3-one-bad-folder-must-not-stop-the-shelf.md)).
- **`https://adk.dev/skills/`** — the *Skills for ADK agents* page, for the documented in-code path
  (*"You can define Skills within the code of your agent"*) and the frontmatter validation rules it
  states: `name` at most 64 characters and lowercase kebab-case, `description` at most 1024 characters
  and non-empty ([4.1](parts/04-skills-built-in-code/4.1-a-skill-without-a-folder.md),
  [4.2](parts/04-skills-built-in-code/4.2-the-model-is-the-spec.md)).
- **`https://agentskills.io/specification`** — for the `name` and `description` constraints the model
  enforces, the *"a map from string keys to string values"* wording on `metadata` and its `version:
  "1.0"` example, the recommendation to keep `SKILL.md` under 500 lines, and the
  `references/` / `scripts/` / `assets/` conventions with references relative to the skill root
  ([1.3](parts/01-testing-prose/1.3-the-rules-worth-a-test.md),
  [2.4](parts/02-checks-as-functions/2.4-pointers-that-go-nowhere.md),
  [5.1](parts/05-versioning/5.1-a-name-for-the-text-that-ran.md)).
- **The installed `pydantic`** — `ValidationError.__mro__` confirms it inherits from `ValueError`,
  which is what makes `except (FileNotFoundError, ValueError)` the complete documented failure surface
  ([2.2](parts/02-checks-as-functions/2.2-let-the-loader-be-the-oracle.md)).
- **`yaml.safe_load("metadata:\n  version: 1.10\n")`** — run directly, returns
  `{'metadata': {'version': 1.1}}`, which is the unquoted-version trap
  ([5.1](parts/05-versioning/5.1-a-name-for-the-text-that-ran.md)).
- **`https://doi.org/10.1109/C-M.1978.218136`** — *Hints on Test Data Selection: Help for the
  Practicing Programmer*, cited and taught; its dated row is already in `docs/PAPERS.md`.

---

## §9 Say it in an interview

"We had agent skills as Markdown folders that non-engineers could edit, which is the point of the
format and also the problem. The description decides which tasks reach the skill, the body is followed
as steps, and a path in the body is a file the agent will try to read — so a well-meant edit changes
behaviour with no error, no review and no deploy. We treated the folder as source.

The checks are pure functions that take a folder and return findings — they never print, never exit
and never raise because a skill is bad. That matters because the same functions have three consumers
with three different policies: the test suite asserts on them, the merge gate turns them into an exit
code, and a report groups and counts them. Three of our six rules are already enforced by the
framework's loader, so we call the loader and report what it says instead of owning a second copy of
the spec that can drift. And we walk the shelf ourselves rather than using the bulk loader, because
the bulk loader raises on the first bad folder — correct for the runtime, and it would give a linter
one problem per commit-push cycle.

Two things I'd stress. First, the suite enumerates `skills/` live, never a list, because a hardcoded
list fails by *passing* — we staged that deliberately: a folder the framework refuses to load, two
suites pointed at it, and the list-driven one reported success. Second, a green run over a clean shelf
proves either that the shelf is clean or that the checks do nothing, so every rule has a test that
hands it something broken and asserts on the specific rule identifier. That's mutation testing done by
hand, and the 1978 paper it comes from is exactly the argument that coverage tells you which lines ran
and not whether anything would notice a bug.

Versioning was the other half. A skill version buys no compatibility — nothing resolves it — but three
things need to name one exact version of the text: the audit trail, the run log, and a bug report. The
number lives in `SKILL.md` and the skill is a whole folder, so editing a rubric changed behaviour and
moved nothing. We put a short content hash of the folder next to the version, so any content change
makes the check red and the only way to green is to open the frontmatter and decide the bump. The bump
sizes an obligation rather than a diff: patch obliges nothing, minor re-runs our routing gate — a
one-word description edit is a minor, because the description is the router — and major re-reads the
whole skill as if it had arrived from a stranger, because a changed procedure is a new skill wearing an
old name."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 30` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it to
someone else with the page closed.

**Phase 4's gate** is skills authored, loaded, audited and tested, with `./m check` green including the
skills lint and the `:free` lint. Today closes the testing and versioning half — SK-17, SK-18, SK-19 —
and hands Day 31 the check functions it wraps in a linter and wires into `./m check`.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 30 | <date> | SK-17, SK-18, SK-19 | 19 (+1 paper) | <hash> | ⚠️ |
```

The gate is ⚠️, not ✅, for the reason the last several rows carry it: `./m check` is red on a
pre-existing `ruff I001` in `tests/test_persona.py`, a learner file no generated day may edit, and
unrelated to this day. `./m depth 30`, `./m trace` and `./m wiki --check` are green.

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and no model string changed:
`google-adk` stays at 2.7.1, `pytest` at 9.1.1, and `gemini-3.7-flash` stays pinned and unused today.

**`docs/PAPERS.md`** — **no new row.** *Hints on Test Data Selection: Help for the Practicing
Programmer* (`doi:10.1109/C-M.1978.218136`, 1978) already has its dated row, and this is the day that
teaches it — cited from [3.3](parts/03-the-suite/3.3-the-test-for-the-checker.md) and
[6.2](parts/06-in-production/6.2-writing-down-what-green-means.md).

**`docs/SKILL_PROVENANCE.md`** — **no new rows.** Nothing was sourced today. The first-party skills
that gained a `metadata.digest` are not third-party installs and get no row; their identity is the
version plus the digest in their own frontmatter
([5.3](parts/05-versioning/5.3-the-change-the-version-missed.md)).

**The commit:**

```text
day 30: skill testing & versioning - closes SK-17, SK-18, SK-19
```

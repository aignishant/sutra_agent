---
day: 31
phase: 4
phase_name: "Agent Skills"
title: "Quality gate — ./m check"
ids: ["SK-20", "OPS-08"]
principles: [2, 7, 10, 11, 13, 14, 15, 16, 17, 18]
kind: gate
plan_version: "v2.2.1"
parts: 18
generated: "2026-09-04"
status: written
lab_scaffolded: false
commit: ""
---

# Day 31 — Quality gate: `./m check`

> **Yesterday (Day 30):** skill testing and versioning — `tools/skill_checks.py`, the pure check
> functions over a skill folder, and `tests/test_skills.py`, the pytest suite that drives them.
> **Today:** the repo gets one command that can tell it the truth. You give Day 30's checks a
> command-line front door, you mechanise Addendum 02's billing rule, you wire both into `./m check`,
> and you discover that the gate you were about to extend has been **red since Day 15** while seven
> ledger rows said green. Then you run the Phase 4 gate for real, freshness checks included.
> **Tomorrow (Day 32):** Phase 5 opens with MCP 2026 — the stateless core, the governance model and
> the registry. Today's freshness check is the last chance to notice that the ground moved first.

---

## §1 Where we are

Six days of Phase 4 built a library of things that can be checked. Skills that must have a `name`
matching their folder. Descriptions that must route without colliding. A shelf that must not quietly
grow a fifth skill nobody audited. Model strings that must end in five particular characters or the
request stops being free.

Every one of those rules currently lives in the same place: somebody's memory.

Think about a shop at closing time. There is a lot to be true before the shutter comes down — the
back door locked, the fridge closed, the till emptied, the fan off. A careful person walks around and
checks each one. A careful person on a bad evening checks three of them and remembers the fourth on
the bus. So the good shops end up with **one switch by the door**, wired so the shutter motor will not
run until every circuit behind it says it is safe. Not because the owner is careless. Because a
routine that depends on being remembered is a routine that has already been forgotten once, and
nobody noticed which time it was.

`./m check` is that switch, and it already exists. Day 0 built it and every day since has run it. It
runs six stages today: `ruff check`, `ruff format --check`, the offline test suite, the depth
contract, the traceability generator and the wiki generator. What it has never run is the two rules
Phase 4 invented — the shape of a skill, and the `:free` suffix — so those two are still riding
around in your head.

Today closes that gap, and the closing is smaller than you expect. You write two short programs, each
of which decides nothing on its own: `tools/lint_skills.py` calls Day 30's `check_shelf` and prints
what it returns; `tools/lint_free_suffix.py` looks for one pattern and one suffix. Then you add two
lines to a shell script. That is the whole build.

The rest of the day is the part that is actually hard, and it comes in three pieces.

**A gate is only worth what its exit code is worth.** A program that prints a red table and returns
zero has not failed — it has *laundered* a failure into a pass, and everything downstream believes
it. You will find three separate ways that happens here: a shell that keeps going after a red, a test
runner that reports success for running nothing, and a pipe that throws away the number that mattered.

**A gate that nobody looks at is a gate that stops being true.** Run `./m check` right now, before
you write a line. It is **red**, on a single lint error in `tests/test_persona.py`, and it has been
red since Day 15. Rows 23 to 29 of `docs/PROGRESS.md` carry ⚠️ instead of ✅ for exactly this reason,
and rows 16 to 22 carry ✅ and are wrong. Fourteen days of work were committed on top of a gate that
was already failing, and the only reason anybody knows is that somebody eventually wrote ⚠️ instead
of ticking the box.

**And a gate cannot check the world.** Whether `google-adk` released a breaking version, whether the
MCP specification moved, whether a free model quietly stopped being free — none of that is visible to
a program running on your machine. That is what the **phase-gate freshness check** is for, and today
it is not ritual: Phase 5 starts tomorrow and is built directly on the MCP spec revision you are
about to re-check. Under Principle 14, if the ground has moved, you amend the plan **first** and
write code **second**.

---

## §2 The map

Eighteen parts in six sections, and no paper part — today's subject is a command, a convention and a
shell script, and none of those has a research paper behind it. One part cites a paper taught on Day
21, as an address. The day climbs `foundation → working → production`.

Section 1 is the gate that already exists and what its exit code means. Section 2 is the skills lint
(SK-20). Section 3 is the `:free` lint. Section 4 wires both into the driver. Section 5 is three
deliberate failures, all of them ways a gate reports green while something is wrong. Section 6 is the
Phase 4 gate itself — the ledger conditions and the freshness re-checks that a program cannot run for
you.

### Section 1 — `01-what-a-gate-is`: one command, one honest exit code (OPS-08)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [One command, one exit code](parts/01-what-a-gate-is/1.1-one-command-one-exit-code.md) | What `./m check` runs today, and who reads its answer | `foundation` |
| 1.2 | [Six stages, cheapest first](parts/01-what-a-gate-is/1.2-six-stages-cheapest-first.md) | What each stage protects, and why that order | `working` |
| 1.3 | [The line that makes it stop](parts/01-what-a-gate-is/1.3-the-line-that-makes-it-stop.md) | `set -euo pipefail`, flag by flag | `working` |
| 1.4 | [What green does not mean](parts/01-what-a-gate-is/1.4-what-green-does-not-mean.md) | The four things the gate cannot tell you | `production` |

### Section 2 — `02-a-lint-is-a-test`: the skills lint (SK-20)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Two front doors, one rulebook](parts/02-a-lint-is-a-test/2.1-two-front-doors-one-rulebook.md) | Why pytest and a lint, and why the rules live once | `foundation` |
| 2.2 | [The command that adds no rules](parts/02-a-lint-is-a-test/2.2-the-cli-that-adds-no-rules.md) | `tools/lint_skills.py`, whole | `working` |
| 2.3 | [The exit code is the API](parts/02-a-lint-is-a-test/2.3-the-exit-code-is-the-api.md) | `main() -> int`, and who reads the number | `working` |
| 2.4 | [What the shelf lint refuses to judge](parts/02-a-lint-is-a-test/2.4-what-the-shelf-lint-refuses-to-judge.md) | Shape, sense, safety — three different claims | `production` |

### Section 3 — `03-the-free-suffix-lint`: the billing invariant (OPS-08)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Five characters that bill](parts/03-the-free-suffix-lint/3.1-five-characters-that-bill.md) | Addendum 02 §7, and why memory is the wrong enforcer | `foundation` |
| 3.2 | [What the lint must read](parts/03-the-free-suffix-lint/3.2-what-the-lint-must-read.md) | `tools/lint_free_suffix.py`, whole, and its scan set | `working` |
| 3.3 | [The alarm that fires on toast](parts/03-the-free-suffix-lint/3.3-the-alarm-that-fires-on-toast.md) | Ten real findings, none of them a bug | `production` |

### Section 4 — `04-wiring-the-gate`: extending the driver (OPS-08)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Two lines in the driver](parts/04-wiring-the-gate/4.1-two-lines-in-the-driver.md) | The exact diff, and where in the order | `working` |
| 4.2 | [The module the script cannot find](parts/04-wiring-the-gate/4.2-the-module-the-script-cannot-find.md) | `ModuleNotFoundError`, and why `-m` fixes it | `working` |

### Section 5 — `05-the-gate-that-lied`: three ways green is a lie

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 Red since Day 15](parts/05-the-gate-that-lied/5.1-red-since-day-fifteen.md) | The real failure in this repo, right now | `production` |
| 5.2 | [💥 Green because nothing ran](parts/05-the-gate-that-lied/5.2-green-because-nothing-ran.md) | pytest exit 5, and the line that forgives it | `production` |
| 5.3 | [💥 The swallowed exit code](parts/05-the-gate-that-lied/5.3-the-swallowed-exit-code.md) | Pipes, forgiving operators, and the number that vanished | `production` |

### Section 6 — `06-the-phase-gate`: closing Phase 4 (§15)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Six things that must be true](parts/06-the-phase-gate/6.1-six-things-that-must-be-true.md) | The plan's §15, run against this repo | `production` |
| 6.2 | [The freshness check that fired](parts/06-the-phase-gate/6.2-the-freshness-check-that-fired.md) | Five re-checks, two of them amber, and what to do | `production` |

---

## §3 Setup — run this

**No package is added today.** Nothing is installed, no model string changes, and `git diff
pyproject.toml uv.lock` must be empty when you finish. Everything today uses the Python standard
library and the tools already pinned: `ruff==0.16.4`, `pytest==9.1.1`, Python 3.12.

The first command is not setup. It is the measurement the whole day hangs on, so run it before you
write anything.

```bash
# 1 - look at the gate you are about to extend, before you touch it
./m check; echo "exit: $?"
```

On 2026-09-04 that printed a ruff `I001` error against `tests/test_persona.py:7` and `exit: 1`. If
yours is green, somebody has already run the fix — read
[5.1](parts/05-the-gate-that-lied/5.1-red-since-day-fifteen.md) anyway, because the story is the point
and the ledger rows are still there.

```bash
# 2 - the two linters. tools/ and tools/__init__.py already exist from Day 30.
touch tools/lint_skills.py
touch tools/lint_free_suffix.py

# 3 - confirm Day 30's check functions are importable, since today's linters are wrappers over them
uv run python -c "from tools.skill_checks import Finding, check_shelf; print('ok')"

# 4 - the day's lab, for the failure drills that must not touch project code
cd days/day-31-the-quality-gate
mkdir -p lab
touch lab/errexit_demo.sh lab/exit_codes.sh
cd -
```

**Step 3 is a real gate, not a formality.** If it prints `ModuleNotFoundError: No module named
'tools'` or `cannot import name 'check_shelf'`, Day 30 is not finished and today cannot start — the
skills lint has nothing to call. If it
prints `ok`, Day 30's rules are on disk and today is genuinely two thin wrappers over them
([2.1](parts/02-a-lint-is-a-test/2.1-two-front-doors-one-rulebook.md)).

**Nothing new goes into `sutra/` or `sutra_mcp/` today.** The only project files today creates are
the two under `tools/`, and the only project file today edits is `m` — two added lines
([4.1](parts/04-wiring-the-gate/4.1-two-lines-in-the-driver.md)).

---

## §4 Build brief

**`tools/lint_skills.py`** — the command-line front door onto Day 30's rules. Public symbols:
`main(argv=None) -> int`, plus `report(shelf, findings) -> int` and `shelf_folders(shelf)` so a test
can drive it without a subprocess. It imports `Finding` and `check_shelf` from `tools.skill_checks`
and **implements no rule of its own**; it formats findings, counts what was examined, and returns 0
or 1. Given whole in [2.2](parts/02-a-lint-is-a-test/2.2-the-cli-that-adds-no-rules.md).

**`tools/lint_free_suffix.py`** — Addendum 02 §7 made mechanical: every `openrouter/` model string in
the repository must end in `:free`. Public symbols: `main() -> int`, plus `offenders(root)` and
`scannable(root)` so a test can drive it without a subprocess. Given whole in
[3.2](parts/03-the-free-suffix-lint/3.2-what-the-lint-must-read.md).

**Two new lines in `./m check`**, added to the `check)` target between the format check and the test
run. The exact diff is in [4.1](parts/04-wiring-the-gate/4.1-two-lines-in-the-driver.md); the reason
they are `-m` invocations and not `python tools/…` is in
[4.2](parts/04-wiring-the-gate/4.2-the-module-the-script-cannot-find.md).

**`lab/errexit_demo.sh`** — the `set -e` drill, given whole in
[1.3](parts/01-what-a-gate-is/1.3-the-line-that-makes-it-stop.md), and **`lab/exit_codes.sh`** — the
five-case exit-code drill, given whole in
[5.3](parts/05-the-gate-that-lied/5.3-the-swallowed-exit-code.md). Both are lab code; neither runs as
part of the gate. `lab/m_broken` is generated by a `sed` command in
[5.2](parts/05-the-gate-that-lied/5.2-green-because-nothing-ran.md) and is deleted afterwards.

**`TODO(me)` markers left for you:**

- **1.4** — write down, in one sentence each, the four questions `./m check` cannot answer, and name
  the day or the ritual that answers each one instead.
- **2.3** — design the third exit code. The lint uses `0` for clean and `1` for everything else;
  decide which failures deserve a `2` meaning *the lint itself broke*, implement it, and say what a
  build server would do differently with that number.
- **2.4** — add one structural rule to Day 30's `check_skill` that today's lint would then enforce
  for free, and say why it belongs in the shape checker and not in the audit.
- **3.2** — extend the scan set to one file type it currently misses on purpose, and measure what
  that costs in false alarms before you keep it.
- **3.3** — triage the ten real findings the `:free` lint reports on this repo today. For each one,
  decide: teaching example (mark it) or billing bug (fix it). The gate is red until you have.
- **4.1** — decide whether the two lints run before or after `pytest`, defend the order out loud, and
  say what changes about that answer once the suite is slow.
- **5.1** — run the one-line fix for `tests/test_persona.py`, watch `./m check` go from red to red at
  a *later* stage, and update the ⚠️ rows in `docs/PROGRESS.md` only when the whole command exits 0.
- **5.2** — make the gate refuse an empty test suite from Day 31 onward, and say what would have to
  be true for exit 5 to be acceptable again.
- **6.2** — write the five freshness findings into your own log, then decide whether the `google-adk`
  and `mcp` version deltas need an addendum row before Phase 5 or after it. Whichever you choose,
  write the sentence that justifies it.

---

## §5 The eval that must be able to fail

Today has two evals, and **one of them is red right now**. That is deliberate: a gate whose first run
is green has taught you nothing about whether it can fail.

**Eval 1 — the `:free` lint, red on this repo.**

```bash
uv run python -m tools.lint_free_suffix; echo "exit: $?"
```

Measured on 2026-09-04 with the lint written as
[3.2](parts/03-the-free-suffix-lint/3.2-what-the-lint-must-read.md) gives it: **ten findings and
`exit: 1`**, every one of them in a day document that teaches the trap by showing the wrong string.
None is a billing bug. Going green is a triage exercise, not a code change, and it is your
`TODO(me)` in [3.3](parts/03-the-free-suffix-lint/3.3-the-alarm-that-fires-on-toast.md).

Then prove it can go the other way: mark one finding and re-run. Nine. Unmark it. Ten. The lint
reports what is there.

**Eval 2 — the whole gate, red on a stage that has nothing to do with today.**

```bash
./m check; echo "exit: $?"
```

Measured the same day: it stops in `ruff check .` with `I001 [*] Import block is un-sorted or
un-formatted` at `tests/test_persona.py:7`, and `exit: 1`. Fix that one file and the gate does not go
green — it goes red *later*, at the `:free` lint, which is what a gate is supposed to do
([5.1](parts/05-the-gate-that-lied/5.1-red-since-day-fifteen.md)).

**The drill that proves the gate can stop.** Both linters are wired in, so plant a break and watch it
catch:

```bash
# add one line to any file under tools/ and run the gate; then delete the line
printf '_OOPS = "openrouter/%s"
' "some-vendor/some-model" >> tools/lint_skills.py
./m check; echo "exit: $?"
```

The offending string is assembled by `printf` rather than typed whole, because this document is
itself scanned by the lint you are about to write, and a document that spells the bad string out
becomes a finding. That constraint is real and it is the subject of
[3.3](parts/03-the-free-suffix-lint/3.3-the-alarm-that-fires-on-toast.md).

Expected: the gate stops at the `:free` lint naming `tools/lint_skills.py`, the line number and the
string, `exit: 1`, and **pytest never runs** — the stages are ordered so the cheap check that failed
saved you the expensive one that would not have.

---

## §6 Request budget

**Free-tier Gemini**, `gemini-3.7-flash`, roughly 20 generate requests per day, read off a live 429
on Day 2 and recorded in `docs/PACKAGES.md`. **Today spends none of them.**

| What | Generations |
| --- | --- |
| `./m check`, all eight stages | **0** |
| `tools/lint_skills.py` | **0** (string and path checks over `skills/`) |
| `tools/lint_free_suffix.py` | **0** (one regular expression over text files) |
| the three failure drills in section 5 | **0** (shell exit codes and pytest collection) |
| the Phase 4 gate and the five freshness re-checks | **0** (web pages, `curl` to an index, a ledger read) |
| **Total planned** | **0 of 20** |

**Zero is the design, not an economy.** A gate is worth having only if it is cheap enough to run on
every change, and a gate that spends model quota is a gate somebody starts skipping on the day the
quota is tight — which is the day the repository is most likely to be broken. Everything Phase 4
added to the gate is deterministic on purpose.

**Cost: $0.**

---

## §7 Traps

- **The gate is already red.** Do not build on top of it and assume your new stage works — you will
  never reach your stage (5.1).
- **A green table with a zero exit code is worse than no gate.** Humans read text; every caller reads
  one integer. Verify the integer with `echo "exit: $?"`, in front of your own eyes (2.3).
- **`python tools/lint_skills.py` cannot import `tools.skill_checks`.** Running a script puts the
  *script's* folder on the import path, not the working directory. Use `python -m tools.lint_skills`
  (4.2).
- **`pytest` exits 5 when it collected nothing, and `./m check` forgives 5.** A typo in a marker
  expression turns "everything passed" and "nothing ran" into the same green (5.2).
- **A pipe throws away the exit code of everything but the last command.** `set -o pipefail` is why
  `m` does not have that bug, and it is one word away from having it (5.3).
- **The skills lint validates shape, never sense and never safety.** Day 29's poisoned fixture passes
  it (2.4).
- **The `:free` lint's first run is full of false alarms**, because the day documents teach the trap
  by printing the wrong string. An alarm that fires on toast gets its battery taken out, so the
  exemption has to be per-line and deliberate (3.3).
- **A day document is not out of scope.** A model string pinned in a build brief is a string somebody
  will copy into code, so the lint reads Markdown too (3.2).
- **`make` is not installed.** The root `Makefile` is a two-line shim that calls `bash ./m check`, and
  it works only where `make` exists. `./m check` is the gate (1.1).
- **A phase is not green because the command is green.** §15 needs the ledger rows, no open IDs, a
  `parts/` directory for every day of the phase, and the freshness check (6.1).
- **The ecosystem moved and the plan has not.** `google-adk` is at 2.8.0 against a 2.7.1 pin, and
  `mcp` is at 2.1.1 against a 1.29.1 pin, both checked on 2026-09-04. Principle 14: amend first, code
  second — never a silent bump on the eve of Phase 5 (6.2).

---

## §8 Verify before you code

Run or read on **2026-09-04**, the day this was written:

- **The repo's own `m` script**, the `check)` target, read in full and quoted verbatim in
  [1.1](parts/01-what-a-gate-is/1.1-one-command-one-exit-code.md) and
  [1.2](parts/01-what-a-gate-is/1.2-six-stages-cheapest-first.md). Nothing about the gate in this day
  is remembered; all of it was read out of the file.
- **`./m check` itself**, run against the repository. Red at stage one, `exit: 1`, on
  `tests/test_persona.py:7`. The error text in
  [5.1](parts/05-the-gate-that-lied/5.1-red-since-day-fifteen.md) is copied from that run.
- **`uv run python -m pytest -q -m "notamarker"`**, run to confirm that pytest returns **5** when its
  marker expression selects nothing ([5.2](parts/05-the-gate-that-lied/5.2-green-because-nothing-ran.md)).
- **`bash` with `set -euo pipefail`**, driven with fake commands returning 1 and 5, to confirm which
  one aborts the script ([1.3](parts/01-what-a-gate-is/1.3-the-line-that-makes-it-stop.md),
  [5.3](parts/05-the-gate-that-lied/5.3-the-swallowed-exit-code.md)).
- **The `:free` lint, run over this repository**, giving the ten findings quoted in
  [3.3](parts/03-the-free-suffix-lint/3.3-the-alarm-that-fires-on-toast.md).
- **`https://modelcontextprotocol.io/specification/latest`** — the specification revision is still
  **2026-07-28**, so Addendum 01 Part 2 stands unchanged and Phase 5 may start tomorrow as planned
  ([6.2](parts/06-the-phase-gate/6.2-the-freshness-check-that-fired.md)).
- **`https://agentskills.io/specification`** — the `SKILL.md` frontmatter fields are unchanged
  (`name`, `description`, `license`, `compatibility`, `metadata`, and experimental `allowed-tools`),
  so Day 30's structural rules still match the spec (6.2, 2.4).
- **`https://pypi.org/pypi/google-adk/json`, `.../mcp/json`, `.../ruff/json`, `.../pytest/json`,
  `.../google-genai/json`** — the live version deltas against this repo's pins, reported in
  [6.2](parts/06-the-phase-gate/6.2-the-freshness-check-that-fired.md).
- **`https://github.com/google/adk-python/releases`** — read for breaking changes between 2.7.1 and
  2.8.0 (6.2).
- **`https://ai.google.dev/gemini-api/docs/rate-limits`** — read, and it still publishes no free-tier
  RPM/RPD table, which confirms Day 2's finding that the only honest quota measurement is a live 429
  (6.2).
- **`docs/02_ADDENDUM_ZERO_BUDGET_MODELS.md` §7** — the `:free` rule, quoted verbatim in
  [3.1](parts/03-the-free-suffix-lint/3.1-five-characters-that-bill.md).
- **`docs/00_MASTER_PLAN.md` §15** — the six phase-gate conditions, enumerated against this repo in
  [6.1](parts/06-the-phase-gate/6.1-six-things-that-must-be-true.md).

---

## §9 Say it in an interview

"We had a rule problem before we had a tooling problem. By the end of the skills phase the repo had
maybe a dozen invariants — skill folders must have frontmatter matching the folder name, model
strings must end in `:free` or they bill you, every day document has to satisfy a structural contract
— and every one of them was enforced by somebody remembering. So we consolidated: one command,
`./m check`, that runs every guardian in order and exits non-zero the moment one of them fails.

The two we added were both thin on purpose. The skills lint is a command-line wrapper over check
functions the test suite already drives — same rules, one implementation, two front doors, because
the day you implement the rules twice is the day green starts meaning two different things depending
on which door you came through. And a billing lint: every OpenRouter model string in the repo has to
end in `:free`, because on a zero-budget project a missing five-character suffix is not a style issue,
it is a charge waiting for a paid key. That one is about twenty lines and it guards the single most
expensive typo the repo can contain.

The interesting part was what we found. First run of the billing lint gave ten hits, and every single
one was in a lesson that teaches the trap by printing the wrong string — a genuine false-positive
problem, and the wrong fix is to stop scanning documentation, because a model string pinned in a
build brief is a string somebody will copy. So the exemption is per-line and deliberate, the same
shape as a `noqa`, and you have to write it next to the thing you are exempting.

And second: the gate itself had been red for fourteen days of work. One un-sorted import block in a
test file, failing `ruff` at stage one, while seven progress-ledger rows said green. We caught it
because somebody wrote ⚠️ instead of ✅ and explained why in the ledger. That is the whole lesson of
the day for me — a gate is only worth what its exit code is worth, and an exit code is only worth
what the person reading it is willing to write down honestly. We drill the red path on purpose now:
plant a break, watch the gate stop at the right stage with the right file named, remove the break.

The last piece is the part a program cannot do. A phase gate here is the command *plus* a freshness
check — has the framework shipped a breaking version, has the protocol spec revision moved, has a
model quietly lost its free tier, has the skill spec drifted. We ran it and two of them were amber:
the framework was one minor version ahead of our pin and the protocol SDK was a whole major ahead.
The rule is that we amend the plan first and write code second, never the other way, because a silent
bump the day before a new phase starts is how a curriculum ends up teaching an API that no longer
exists."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 31` is green. Defined by
understanding and green checks, never by elapsed time.

**This is the Phase 4 gate day**, so "done" is larger than usual and
[6.1](parts/06-the-phase-gate/6.1-six-things-that-must-be-true.md) enumerates it: every day from 25
to 31 has its `PROGRESS.md` row, `./m trace` shows no open ID from Phase 4 or earlier, every one of
those days has a `parts/` directory, `./m check` passes with the two new stages, the five freshness
findings are written down, and any deviation is recorded as an ADR or a `CHANGELOG_PLAN.md` row.

Be careful with the fifth one. `./m check` passing means it **exited 0** and you saw the number, not
that the last line of output looked encouraging.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 31 | <date> | SK-20, OPS-08 | 18 | <hash> | ⚠️ |
```

**Write ⚠️ unless you watched `./m check` exit 0.** Two things stand between this repo and a ✅ today,
and neither of them is this day's code: the pre-existing `ruff I001` in `tests/test_persona.py`, which
is the learner's file and which no generated day may edit, and the ten `:free` findings in older day
documents, which need a per-line triage decision rather than a code change. Fix the first with `uv run
ruff check --fix tests/test_persona.py`, triage the second, run the gate, and only then change this
row — and rows 23 to 30 with it. A ✅ written before the command exits 0 is exactly the failure
[5.1](parts/05-the-gate-that-lied/5.1-red-since-day-fifteen.md) is about.

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and no model string changed. The
freshness findings in [6.2](parts/06-the-phase-gate/6.2-the-freshness-check-that-fired.md) are
*findings*, not pins: `google-adk` stays at 2.7.1 and `mcp` stays at 1.29.1 until the plan is amended
(Principle 14). If you decide to bump either one, the row is written on the day of the bump, with the
addendum that authorised it named in the reason column.

**`docs/PAPERS.md`** — **no new row.** *End-to-end arguments in system design* already has its dated
row and is taught on Day 21; today's
[1.4](parts/01-what-a-gate-is/1.4-what-green-does-not-mean.md) cites it as an address only.

**`docs/SKILL_PROVENANCE.md`** — **no new rows.** No third-party skill was sourced today. The
freshness re-check of existing pins is a *read* of this ledger, and on 2026-09-04 it holds no
accepted external skill at all, so there is nothing that can have drifted (6.2).

**`docs/CHANGELOG_PLAN.md`** — possibly one row, and it is your judgement call. If you decide the
`google-adk` 2.8.0 or `mcp` 2.1.1 delta changes anything Phase 5 depends on, the amendment is written
**before** any code (Principle 14). If you decide it does not, write nothing here and put the finding
in your own log instead.

**The commit:**

```text
day 31: quality gate - ./m check - closes SK-20, OPS-08
```

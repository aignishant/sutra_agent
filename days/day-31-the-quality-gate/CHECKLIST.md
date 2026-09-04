# Day 31 — CHECKLIST

**IDs closed:** SK-20, OPS-08
**Principles served:** 2, 7, 10, 11, 13, 14, 15, 16, 17, 18
**Parts:** 18 across 6 sections, no paper
**This is the Phase 4 gate day.**

> `./m done 31` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours, and today is the day this repository learned what that costs.

## Demo command

```bash
# 0 - the measurement the day hangs on, BEFORE you write anything
./m check; echo "exit: $?"

# 1 - the two linters, each run on its own, with the number read out loud
uv run python -m tools.lint_skills; echo "exit: $?"
uv run python -m tools.lint_skills tests/fixtures/skills/sourced-pack; echo "exit: $?"
uv run python -m tools.lint_skills no/such/place; echo "exit: $?"
uv run python -m tools.lint_free_suffix; echo "exit: $?"
uv run python -m tools.lint_free_suffix days/day-31-the-quality-gate; echo "exit: $?"

# 2 - the import failure, on purpose, so the traceback is familiar
python tools/lint_skills.py; echo "exit: $?"

# 3 - the shell drill: five ways an exit code survives or vanishes
bash days/day-31-the-quality-gate/lab/exit_codes.sh

# 4 - the empty-suite drill: pytest returns 5 and the gate forgives it
uv run python -m pytest -m "not live"; echo "exit: $?"
uv run python -m pytest -m "not-live"; echo "exit: $?"
sed 's/not live/not-live/' m > days/day-31-the-quality-gate/lab/m_broken
bash days/day-31-the-quality-gate/lab/m_broken check; echo "exit: $?"

# 5 - the gate with the two new stages, and the planted break
./m check; echo "exit: $?"
printf '_OOPS = "openrouter/%s"\n' "some-vendor/some-model" >> tools/lint_skills.py
./m check; echo "exit: $?"
git checkout tools/lint_skills.py

# 6 - the phase gate, conditions 1 to 4
grep -n "^| 2[5-9] \|^| 3[01] " docs/PROGRESS.md
./m trace && grep -n "open" docs/TRACEABILITY.md | head -20
for n in 25 26 27 28 29 30 31; do
  d=$(ls -d days/day-$n-* 2>/dev/null | head -1)
  printf "day %s: %s parts\n" "$n" "$(find "$d/parts" -name '*.md' 2>/dev/null | wc -l)"
done

# 7 - the freshness re-checks, condition 5
for p in google-adk google-genai mcp ruff pytest; do
  curl -s "https://pypi.org/pypi/$p/json" \
    | python -c "import json,sys; print('$p', json.load(sys.stdin)['info']['version'])"
done
cat docs/SKILL_PROVENANCE.md

./m depth 31
```

Expected: step 0 stops at `ruff check .` with `I001` on `tests/test_persona.py:7` and `exit: 1`. Step
1 gives `exit: 1` for the default shelf while `skills/` holds only `.gitkeep`, `exit: 1` for the
missing path, and `exit: 1` from the `:free` lint with ten findings, all of them day documents
teaching the trap. Step 2 gives `ModuleNotFoundError: No module named 'tools'`. Step 3 prints five
cases of which three swallow the failure. Step 4 gives `exit: 0` then `exit: 5`, and the broken
driver copy finishes `OK all green` on a run where no test executed. Step 5's planted break stops the
gate at the `:free` lint, names the file and line, and never reaches pytest. Step 6 shows seven ⚠️
rows and SK-17..SK-20 plus OPS-08 open until today and yesterday land. Step 7 shows `google-adk`
2.8.0 against a 2.7.1 pin and `mcp` 2.1.1 against 1.29.1. Finally `./m depth 31` green.

## Setup

- [ ] `./m check` was run **before** anything was written, and its exit code was read
- [ ] `uv run python -c "from tools.skill_checks import Finding, check_shelf; print('ok')"` prints
      `ok` — Day 30 is genuinely finished and today is two wrappers over its rules
- [ ] `tools/lint_skills.py` and `tools/lint_free_suffix.py` exist; `tools/__init__.py` was **not**
      re-created (Day 30 owns it)
- [ ] **No `uv add` was run** — `git diff pyproject.toml uv.lock` is empty
- [ ] Nothing was added to `sutra/` or `sutra_mcp/`; the only project file edited is `m`

## Section 1 — `01-what-a-gate-is`

- [ ] **1.1** read · quoted the `check)` target out of `m` rather than from memory · ran the gate and
      read `$?` with your own eyes · can say who reads the exit code and who reads the output
- [ ] **1.2** read · named all six existing stages in order · explained why the order is by cost and
      not by importance · found the one stage where a non-zero code is deliberately forgiven
- [ ] **1.3** read · wrote `lab/errexit_demo.sh` and watched `NEVER PRINTED` stay unprinted ·
      **deleted `set -euo pipefail` from a copy and watched the same failure exit 0** · named two
      places where `-e` does not fire
- [ ] **1.4** read · `TODO(me)`: wrote down the four questions `./m check` cannot answer and the day
      or ritual that owns each one · read the deselected count out of a non-quiet pytest run

## Section 2 — `02-a-lint-is-a-test` (SK-20)

- [ ] **2.1** read · can say what breaks when a lint restates its test suite's rules, and why the
      failure is silent
- [ ] **2.2** read · `tools/lint_skills.py` written and run · **counted the lines in it that decide
      whether a skill is valid, and the answer was zero**
- [ ] **2.3** read · ran the lint against a missing path and saw `exit: 1` · temporarily changed that
      branch to `return 0`, saw the output not change at all, and put it back · `TODO(me)`: designed
      the third exit code (`2` = the lint itself broke), decided which failures earn it, and said
      what a build server would do differently with it
- [ ] **2.4** read · pointed the lint at `tests/fixtures/skills` and got `OK evil-helper` · ran Day
      29's audit against the same folder and got ten findings · `TODO(me)`: added one structural rule
      to Day 30's `check_skill` and said why it belongs there and not in the audit

## Section 3 — `03-the-free-suffix-lint`

- [ ] **3.1** read · quoted Addendum 02 §7 accurately, including that its `make check` means
      `./m check` · can explain why a missing suffix is invisible to tests, errors and logs
- [ ] **3.2** read · `tools/lint_free_suffix.py` written and run · **removed `".md"` from
      `TEXT_SUFFIXES`, watched ten findings become zero, and put it back** · `TODO(me)`: extended the
      scan set to one file type it misses on purpose and measured the false alarms before keeping it
- [ ] **3.3** read · `TODO(me)`: **triaged all ten findings** — for each one, lesson or bug, decision
      recorded in the line · can say why a path allowlist is worse than a line marker
- [ ] The two markers are understood: `allow-unfree` on a line, `allow-unfree-file` in a file, and
      the file marker carries a written reason wherever it is used

## Section 4 — `04-wiring-the-gate` (OPS-08)

- [ ] **4.1** read · the two lines added to `m` between `ruff format --check .` and the pytest line ·
      `grep -n "lint_" m` shows exactly two lines, in the right place · `TODO(me)`: defended the
      position out loud and said what changes about the answer once the suite is slow
- [ ] **4.2** read · ran the linter both ways and saw `ModuleNotFoundError` from the path form ·
      **did not add a `sys.path` insertion** · can state the difference between `No module named
      'tools'` and `No module named 'tools.skill_checks'`

## Section 5 — `05-the-gate-that-lied`

- [ ] **5.1** read · confirmed with `git log` that `tests/test_persona.py` last changed in `4029771` ·
      read the seven ⚠️ rows and the note under the table in `docs/PROGRESS.md` · `TODO(me)`: ran
      `uv run ruff check --fix tests/test_persona.py`, read the diff, and **did not edit rows 16–22**
- [ ] **5.2** read · reproduced `exit: 5` with the one-hyphen typo · ran the broken driver copy and
      watched `OK all green` on a run with zero tests · `TODO(me)`: decided what this repository does
      about an empty or shrinking suite and wrote the reason beside the choice
- [ ] **5.3** read · `lab/exit_codes.sh` written and run · can name the three constructions that
      replace an exit code and which one `pipefail` fixes · **did not append a forgiveness operator
      to any gate stage to make it green**

## Section 6 — `06-the-phase-gate` (plan §15)

- [ ] **6.1** read · answered conditions 1, 2, 3 and 4 for Phase 4 and **wrote the four answers
      down** · can say which of the six a green `./m check` does not answer
- [ ] **6.2** read · ran the five freshness checks and **wrote a finding for each, including the
      boring ones** · `TODO(me)`: decided whether the `google-adk` 2.8.0 and `mcp` 2.1.1 deltas need
      an addendum row before Phase 5 or after it, and wrote the sentence that justifies the choice
- [ ] The MCP specification revision was checked personally and is recorded — **Phase 5 opens
      tomorrow on this answer**
- [ ] No pin was bumped today. `git diff pyproject.toml uv.lock` is still empty (Principle 14: amend
      first, code second)

## Phase 4 gate — the six conditions

- [ ] **1** every day 25–31 has a `PROGRESS.md` row, and its gate column is honest
- [ ] **2** `./m trace` shows no open ID from Phase 4 or earlier
- [ ] **3** `./m check` exits 0, and you watched the number
- [ ] **4** every day 25–31 has a `parts/` directory with documents in it
- [ ] **5** all five freshness findings are written down
- [ ] **6** deviations recorded — an ADR, a `CHANGELOG_PLAN.md` row, or an explicit "none"

## Ledger & commit

- [ ] `./m depth 31` green
- [ ] `docs/PROGRESS.md` row appended, with ⚠️ unless `./m check` exited 0 in front of you
- [ ] `docs/PACKAGES.md` — no new rows; nothing was installed and no model string changed
- [ ] `docs/PAPERS.md` — no new row; Day 21's end-to-end paper is cited as an address only
- [ ] `docs/SKILL_PROVENANCE.md` — no new rows; nothing third-party was sourced today
- [ ] Commit made; `git show --stat HEAD` contains no `.env`

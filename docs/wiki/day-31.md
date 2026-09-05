# Day 31 - Quality gate — ./m check

IDs closed: OPS-08, SK-20 · source: `days/day-31-the-quality-gate/`

## Parts

### 1.1 - One command, one exit code
`days/day-31-the-quality-gate/parts/01-what-a-gate-is/1.1-one-command-one-exit-code.md` · level `foundation` · ids OPS-08

A quality gate is one command that runs every check the project has and answers with a single number — zero for green, anything else for red — and in this repository that command is ./m check, which already exists, already runs six stages, and today gains two more.

### 1.2 - Six stages, cheapest first
`days/day-31-the-quality-gate/parts/01-what-a-gate-is/1.2-six-stages-cheapest-first.md` · level `working` · ids OPS-08

The gate runs its stages in a fixed order — linter, formatter check, tests, then the three documentation checks — and the order is chosen so that the cheapest check that can reject your work runs before the most expensive one, which is what keeps a gate fast enough that people actually run it.

### 1.3 - The line that makes it stop
`days/day-31-the-quality-gate/parts/01-what-a-gate-is/1.3-the-line-that-makes-it-stop.md` · level `working` · ids OPS-08

set -euo pipefail, the fourth line of the m script, is what turns a list of commands into a gate: without -e the shell runs cheerfully past a failed stage and prints OK all green at the bottom of a broken run, and the other three flags close the three remaining ways a failure can go unnoticed.

### 1.4 - What green does not mean
`days/day-31-the-quality-gate/parts/01-what-a-gate-is/1.4-what-green-does-not-mean.md` · level `production` · ids OPS-08

A green gate says "every automatic check we chose to run passed on this machine, just now" — it says nothing about whether the agent still answers correctly, whether a sourced skill is safe, whether the free tier still exists, or whether the world outside the repository moved, and knowing those four edges precisely is what separates a gate from a comfort blanket.

### 2.1 - Two front doors, one rulebook
`days/day-31-the-quality-gate/parts/02-a-lint-is-a-test/2.1-two-front-doors-one-rulebook.md` · level `foundation` · ids SK-20

A lint and a test suite are two different doors onto the same rules, and the only thing that makes having both safe is that the rules are written once, in tools/skill_checks.py, and both doors call them rather than restating them.

### 2.2 - The command that adds no rules
`days/day-31-the-quality-gate/parts/02-a-lint-is-a-test/2.2-the-cli-that-adds-no-rules.md` · level `working` · ids SK-20

tools/lint_skills.py is about forty lines that import Day 30's check_shelf, print one line per skill folder, and return 0 or 1 — and the discipline that makes it worth having is that it contains no if about what a valid skill is.

### 2.3 - The exit code is the API
`days/day-31-the-quality-gate/parts/02-a-lint-is-a-test/2.3-the-exit-code-is-the-api.md` · level `working` · ids SK-20

Everything a lint prints is commentary for a human; the only thing any other program will ever read is the single integer it exits with, so that integer is the interface you are designing, and it has to be right even in the cases where you have nothing interesting to print.

### 2.4 - What the shelf lint refuses to judge
`days/day-31-the-quality-gate/parts/02-a-lint-is-a-test/2.4-what-the-shelf-lint-refuses-to-judge.md` · level `production` · ids SK-20

The skills lint answers one question — is this folder shaped like a skill? — and it deliberately answers neither does this skill say anything useful? nor is this skill safe for an agent to obey?, which is why Day 29's poisoned fixture passes it and why the gate going green is never a safety claim.

### 3.1 - Five characters that bill
`days/day-31-the-quality-gate/parts/03-the-free-suffix-lint/3.1-five-characters-that-bill.md` · level `foundation` · ids OPS-08

Addendum 02 §7 says that any openrouter/ model string in this repository must end in :free, because the same model without those five characters is the paid one, the request succeeds either way, and nothing in your code or your output will tell you which one you used.

### 3.2 - What the lint must read
`days/day-31-the-quality-gate/parts/03-the-free-suffix-lint/3.2-what-the-lint-must-read.md` · level `working` · ids OPS-08

tools/lint_free_suffix.py walks every text file in the repository except history and caches — day documents included, because a model string in a build brief is a string somebody will copy — matches openrouter/… with one regular expression, and reports every occurrence that is not immediately followed by :free.

### 3.3 - The alarm that fires on toast
`days/day-31-the-quality-gate/parts/03-the-free-suffix-lint/3.3-the-alarm-that-fires-on-toast.md` · level `production` · ids OPS-08

The :free lint's first run on this repository reports ten findings and not one of them is a bug — they are all day documents teaching the trap by printing the wrong string — and how you resolve that decides whether the lint survives, because a check that cries wolf gets switched off long before it gets fixed.

### 4.1 - Two lines in the driver
`days/day-31-the-quality-gate/parts/04-wiring-the-gate/4.1-two-lines-in-the-driver.md` · level `working` · ids OPS-08

The whole of OPS-08's build is two lines added to the check) target in m, placed after the formatter check and before the test suite so that the cheap checks run before the expensive one, and they need no if, no error handling and no summary because set -euo pipefail already does all three.

### 4.2 - The module the script cannot find
`days/day-31-the-quality-gate/parts/04-wiring-the-gate/4.2-the-module-the-script-cannot-find.md` · level `working` · ids OPS-08

python tools/lint_skills.py fails with ModuleNotFoundError: No module named 'tools' because naming a file puts that file's own folder at the front of the import path, while python -m tools.lint_skills puts the working directory there instead — which is the folder the tools package actually lives in.

### 5.1 - 💥 Red since Day 15
`days/day-31-the-quality-gate/parts/05-the-gate-that-lied/5.1-red-since-day-fifteen.md` · level `production` · ids OPS-08

./m check in this repository exits 1 on a single un-sorted import block in tests/test_persona.py and has done since Day 15 — seven progress rows were written as ✅ over it before anybody noticed, and the reason anybody eventually did is that one person wrote ⚠️ and explained why instead of ticking the box.

### 5.2 - 💥 Green because nothing ran
`days/day-31-the-quality-gate/parts/05-the-gate-that-lied/5.2-green-because-nothing-ran.md` · level `production` · ids OPS-08

pytest returns exit code 5 when it collected no tests, ./m check deliberately forgives a 5, and a single mistyped character in the marker expression turns "every test passed" and "no test ran" into the same green — which is the same class of bug as a linter returning 0 for an empty shelf, one level up.

### 5.3 - 💥 The swallowed exit code
`days/day-31-the-quality-gate/parts/05-the-gate-that-lied/5.3-the-swallowed-exit-code.md` · level `production` · ids OPS-08

A gate stage can print a perfect failure and still report success, because three ordinary shell constructions — a pipe, a trailing forgiveness operator, and a command substitution — each replace the exit code you care about with the exit code of something else, and set -o pipefail closes only the first of them.

### 6.1 - Six things that must be true
`days/day-31-the-quality-gate/parts/06-the-phase-gate/6.1-six-things-that-must-be-true.md` · level `production` · ids OPS-08

A phase is green only when six independent conditions all hold at once — every day has its ledger row, no ID from this phase or an earlier one is open, ./m check passes on the whole repository, every day in the phase has a parts/ directory, the freshness re-checks pass, and every deviation is recorded — and a green command satisfies exactly one of the six.

### 6.2 - The freshness check that fired
`days/day-31-the-quality-gate/parts/06-the-phase-gate/6.2-the-freshness-check-that-fired.md` · level `production` · ids OPS-08

Five things outside this repository get re-checked at every phase boundary — the framework's releases, the MCP specification revision, the free-model rosters, the Agent Skills specification and the pinned provenance of any sourced skill — and on 2026-09-04 two of them came back amber, which under Principle 14 means the plan is amended first and the code moves second.


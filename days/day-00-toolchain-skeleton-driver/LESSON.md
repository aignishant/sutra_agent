---
day: 0
phase: 0
phase_name: "Foundry"
title: "Toolchain, skeleton and the ./m driver"
ids: []
principles: [2, 6, 7, 9, 10, 13, 16, 17, 18]
kind: setup
plan_version: "v2.2.1"
parts: 17
generated: "2026-08-23"
status: complete
lab_scaffolded: false
commit: "eb3a5a0"
---

# Day 0 — Toolchain, skeleton and the `./m` driver

> **Yesterday:** nothing. This is the first day, and it assumes you have installed nothing and know
> nothing about this stack.
> **Today:** one tool owns the environment, a repository exists that cannot leak a key by accident,
> and a single script decides whether a day is finished.
> **Tomorrow (Day 1):** the ledgers, `scripts/trace.py`, and three free API keys — the Sutra-specific
> bootstrap that closes AG-01, OPS-01, OPS-02 and OPS-03.

---

## §1 Where we are

There is a version of the next few months that goes badly, and it does not start with anything
difficult.

It starts on a Tuesday, when a package you definitely installed cannot be found by a script you
definitely wrote. You will lose an afternoon to it. Three weeks later a tutorial's code will not work
and you will not be able to tell whether the tutorial is wrong or your installation is a different
version. Later still, a test suite will pass while testing code you did not write, and you will
believe it, because a green test is the most persuasive thing on a screen.

None of those is a hard problem. Every one of them is the same problem: **something in your setup is
ambiguous, and ambiguity does not announce itself.** It waits until you are busy.

Think of it like a workshop. You can start building the day the tools arrive, and for the first
week that works fine. Then you need the 8mm spanner and there are four of them in three drawers, two
of which are actually 5/16", and the drawer labels were written by whoever used the workshop before
you. Nothing is broken. You simply cannot answer a basic question about your own room, and now every
job takes twenty minutes longer than it should.

Today is the day you label the drawers — before there is anything in them.

Four things happen, in order, and each one removes a category of future confusion:

- **One tool owns the environment.** Not four Pythons on a `PATH` that decides which one you get by
  accident, but one program that installs the interpreter, holds the packages, records exactly what
  it installed, and runs your code inside it.
- **A repository that cannot leak a key.** `.gitignore` gets written *before* `.env` exists —
  because git has no memory of ignoring something it already tracked, and this repository becomes
  public on Day 93.
- **One entry point.** `./m` — nine verbs, one definition each, so the command you run and the
  command CI runs cannot drift apart.
- **Two gates.** `./m check` answers *is this repository healthy?* `./m done N` answers *is this day
  actually finished?* — and refuses to commit while a checklist box is unticked.

Day 0 closes **no curriculum IDs**, on purpose. Everything here is a precondition for the
curriculum rather than a part of it: no ID moved, so `docs/TRACEABILITY.md` is untouched. What you
build today is what the next ninety-six days stand on.

---

## §2 The map

Seventeen documents in four sections. **Read them in order** — each one names its prerequisite, and
the sections build.

### Section 1 — The toolchain: what actually runs your code
*One owner for the environment, a shell that speaks the same language as the documentation, and a
pinned interpreter.*

| Part | Answers | Level |
| --- | --- | --- |
| [1.1 — Why one tool must own the environment](parts/01-toolchain/1.1-why-one-tool-owns-the-environment.md) | Why does `pip install` succeed and `import` still fail? | `foundation` |
| [1.2 — Git, and why a Unix shell on a Windows machine](parts/01-toolchain/1.2-git-and-the-unix-shell.md) | What is a commit, and why Git Bash rather than PowerShell? | `foundation` |
| [1.3 — uv, the one binary that owns the environment](parts/01-toolchain/1.3-uv-the-one-binary.md) | What is a lockfile, and why is a wish list not reproducible? | `foundation` |
| [1.4 — Python 3.12 under uv, and why not the newest](parts/01-toolchain/1.4-python-3-12-under-uv.md) | Why pin an older Python on purpose? | `working` |
| [1.5 — The editor, and the interpreter trap](parts/01-toolchain/1.5-the-editor-and-the-interpreter-trap.md) | Why does the editor say the import is broken when it runs fine? | `working` |

### Section 2 — The skeleton: a repository that cannot leak a key
*Folders that express what may depend on what, an ignore rule written before the secret exists, and
a manifest plus a lockfile that describe the environment exactly.*

| Part | Answers | Level |
| --- | --- | --- |
| [2.1 — The folder skeleton](parts/02-repo-skeleton/2.1-the-folder-skeleton.md) | Where does a new file go, and what may import what? | `foundation` |
| [2.2 — `.gitignore`, written before any secret exists](parts/02-repo-skeleton/2.2-gitignore-before-secrets-exist.md) | Why is the order of these two files the whole point? | `production` |
| [2.3 — `git init`, and what a repository actually is](parts/02-repo-skeleton/2.3-git-init-and-what-a-repo-is.md) | What is inside `.git`, and what *is* a branch? | `foundation` |
| [2.4 — `uv init`, `pyproject.toml` and the lockfile](parts/02-repo-skeleton/2.4-pyproject-and-the-lockfile.md) | One file for identity, dependencies and every tool's config | `working` |
| [2.5 — The virtual environment you never activate](parts/02-repo-skeleton/2.5-the-venv-you-never-activate.md) | Why `uv run` instead of `activate`? | `working` |

### Section 3 — The driver: one entry point, and a gate that refuses you
*A script that fails honestly, dispatches every repeated command, and decides what "done" means.*

| Part | Answers | Level |
| --- | --- | --- |
| [3.1 — `set -euo pipefail`](parts/03-the-m-driver/3.1-set-euo-pipefail.md) | Why does a script report success after a failed step? | `working` |
| [3.2 — The `case` dispatcher](parts/03-the-m-driver/3.2-the-case-dispatcher.md) | Why one entry point instead of four copies of a command? | `working` |
| [3.3 — `./m check`, the whole-project gate](parts/03-the-m-driver/3.3-the-check-gate.md) | What runs, in what order, and why `-m "not live"`? | `production` |
| [3.4 — `./m done`, a gate that refuses you](parts/03-the-m-driver/3.4-the-done-gate.md) | How does "done" stop being a feeling at 11pm? | `production` |

### Section 4 — The memory: what makes this repository pick-up-able
*Two documents that let a stranger — or a fresh agent session — continue without you, and a first
commit you have personally tried to break.*

| Part | Answers | Level |
| --- | --- | --- |
| [4.1 — The README a stranger reads](parts/04-repo-memory/4.1-the-readme-that-a-stranger-reads.md) | What are the first thirty seconds of this repository? | `working` |
| [4.2 — `CLAUDE.md`, the standing contract](parts/04-repo-memory/4.2-claude-md-the-standing-contract.md) | How do conventions survive the end of a conversation? | `production` |
| [4.3 — The first commit, and leaking a key on purpose](parts/04-repo-memory/4.3-the-first-commit-and-breaking-it.md) | Which of four attacks does `.gitignore` actually stop? | `production` |

**The day climbs** `foundation → working → production`, and section 4 ends with the deliberate-failure
part that plan §17.7 requires of every day: you attack your own guard rail before you trust it.

---

## §3 Setup — run this

Every command here is explained in the part that owns it; this section is the assembled sequence, so
you can see the whole shape before you start. **Run them from the parts, not from here** — the
explanations are where the learning is.

```bash
# 1.2 — git, then tell it who you are
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main

# 1.3 — one binary owns the environment (then REOPEN Git Bash)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version

# 1.4 — the interpreter, managed by uv and off your PATH
uv python install 3.12

# 2.1 — the skeleton
mkdir -p ~/Projects/sutra && cd ~/Projects/sutra
mkdir -p sutra sutra_mcp skills scripts tests days docs/adr
touch sutra/__init__.py sutra_mcp/__init__.py tests/__init__.py skills/.gitkeep

# 2.2 — the ignore rule, BEFORE any secret exists
#      (the full file is in part 2.2 — do not shorten it)

# 2.3 — the repository
git init

# 2.4 — the manifest, then the two dev tools, pinned exactly
uv init --python 3.12 --no-readme --vcs none
uv add --dev "ruff==0.16.4" "pytest==9.1.1"

# 3.1–3.4 — the driver
chmod +x m
```

**Versions verified live on 2026-08-23**, not remembered — `git 2.54.0.windows.1`, `uv 0.12.3`,
CPython `3.12.13`, `ruff==0.16.4` (resolved with `uv pip compile`), `pytest==9.1.1` (read from
`pypi.org/pypi/pytest/json`). Re-verify on your own Day 0 and record what *you* see in
`docs/PACKAGES.md` — that is Principle 7, and §11 has the rows.

**Day 0 adds no runtime dependency at all.** `dependencies = []` in `pyproject.toml` is deliberate:
packages arrive on the day they are first used — `google-genai` on Day 2, `google-adk` on Day 5.

---

## §4 Build brief

Five files, created by you, from the code printed in the parts. Nothing is pre-written in this
repository.

| File | Written in | What it is |
| --- | --- | --- |
| `.gitignore` | [2.2](parts/02-repo-skeleton/2.2-gitignore-before-secrets-exist.md) | The ignore rules, written before `.env` exists |
| `pyproject.toml` | [2.4](parts/02-repo-skeleton/2.4-pyproject-and-the-lockfile.md) | Identity, Python pin, dev dependencies, Ruff + pytest config |
| `m` | [3.1](parts/03-the-m-driver/3.1-set-euo-pipefail.md) → [3.4](parts/03-the-m-driver/3.4-the-done-gate.md) | The driver: nine verbs and two gates |
| `README.md` | [4.1](parts/04-repo-memory/4.1-the-readme-that-a-stranger-reads.md) | The first thirty seconds |
| `CLAUDE.md` | [4.2](parts/04-repo-memory/4.2-claude-md-the-standing-contract.md) | The standing contract for the driver agent |

**`TODO(me)` — the reps this day leaves you:**

- `TODO(me)` Write the full `.gitignore` from 2.2 yourself rather than copying a generic one, and be
  able to say what each block is for.
- `TODO(me)` Assemble `m` section by section as you read 3.1 → 3.4. Do not paste it in one go; each
  part explains why the next piece is shaped the way it is.
- `TODO(me)` Write your own `README.md`. The skeleton in 4.1 is a shape, not an answer — the four
  questions must be answered in *your* words about *this* project.
- `TODO(me)` Record your own observed versions in `docs/PACKAGES.md`. Do not copy the numbers above;
  look them up and write down what you actually saw, with today's date.

---

## §5 The eval that must be able to fail

Day 0 has no Python to test, so its eval is the gate itself. **A gate you have never seen go red is
a gate you are trusting on faith** — so the check for today is to break it deliberately, twice, and
watch it refuse.

```bash
# RED 1 — the lint step must stop the gate
printf 'import os\n' > tests/test_scratch.py
./m check          # must fail: F401 os imported but unused, exit 1
rm tests/test_scratch.py
./m check          # must pass: OK all green

# RED 2 — the done gate must refuse an unticked checklist
printf '# temp\n\n- [ ] not done\n' > days/day-00-toolchain-skeleton-driver/CHECKLIST.md.bak
# (see 3.4 — run it against a checklist with one unticked box, watch it refuse, nothing committed)
```

If `./m check` printed `OK all green` on the first run, `set -euo pipefail` is missing from `m`
([3.1](parts/03-the-m-driver/3.1-set-euo-pipefail.md)) and every later day's gate is a lie.

The third eval is the one in [4.3](parts/04-repo-memory/4.3-the-first-commit-and-breaking-it.md): four attempts
to commit a secret, of which **two must succeed**. Knowing which two, and why that is not a bug, is
the actual deliverable.

---

## §6 Request budget

| Provider | Calls today | Notes |
| --- | --- | --- |
| Gemini | **0** | No key exists yet. Day 1 creates it. |
| Groq | **0** | — |
| OpenRouter | **0** | — |
| Ollama | **0** | — |
| **Total model calls** | **0** | **Cost: $0.** |

Network usage today is downloads only: the git installer, the `uv` installer, one CPython build, and
two packages from PyPI. No quota of any kind is consumed, and nothing you run today can consume one.

From Day 1 this table starts carrying real numbers in **RPM/RPD per provider** — quota is the
currency, not dollars (Principle 15 · Addendum 02).

---

## §7 Traps

- **Not reopening Git Bash after installing `uv`.** A shell reads `PATH` when it starts. `uv:
  command not found` immediately after a successful install is almost always this, and almost never
  a broken install ([1.3](parts/01-toolchain/1.3-uv-the-one-binary.md)).
- **Running `uv init` without `--vcs none`.** It silently overwrites the `.gitignore` you carefully
  wrote in 2.2 with a generic one that has no `.env` rule — **and warns you about nothing**
  ([2.4](parts/02-repo-skeleton/2.4-pyproject-and-the-lockfile.md)).
- **Running the `mkdir` in the wrong directory.** Nothing errors; you get the skeleton one level too
  high. Check `pwd` before any `mkdir` that creates several things
  ([2.1](parts/02-repo-skeleton/2.1-the-folder-skeleton.md)).
- **Copying commands into PowerShell.** `mkdir -p a/b/c` there creates a folder named `-p` and does
  not error ([1.2](parts/01-toolchain/1.2-git-and-the-unix-shell.md)).
- **Believing the editor over the terminal.** A red squiggle on code that runs means the editor is
  analysing a different interpreter. The dangerous version is the reverse — autocomplete for a method
  that no longer exists ([1.5](parts/01-toolchain/1.5-the-editor-and-the-interpreter-trap.md)).
- **Writing `.gitignore` after `.env`.** The rule has no effect on an already-tracked file, and a
  secret committed once is committed forever — the response is to **rotate the key**, never to
  delete the file ([2.2](parts/02-repo-skeleton/2.2-gitignore-before-secrets-exist.md)).
- **A trailing `echo` after a command that can fail.** It succeeds, so the branch exits 0 and a
  failure becomes a success ([3.2](parts/03-the-m-driver/3.2-the-case-dispatcher.md)).
- **Windows line endings in `m`.** `$'\r': command not found` is a carriage return, not a syntax
  error ([3.1](parts/03-the-m-driver/3.1-set-euo-pipefail.md)).

**No 1.x → 2.x ADK trap applies today** — no ADK code is written on Day 0. The first is Day 5
(explicit model pinning, ADK-73); the event-model trap is Day 7.

---

## §8 Verify before you code

Checked live on **2026-08-23** while writing this day. Re-check on yours — Principle 7 says look it
up, never remember it.

| What | Where | Why today |
| --- | --- | --- |
| `uv` install + commands | `docs.astral.sh/uv/` | The installer URL and the `init`/`add`/`sync`/`run` flags |
| `ruff` latest version | `uv pip compile` against PyPI → **0.16.4** | The pin in `pyproject.toml` |
| `pytest` latest version | `pypi.org/pypi/pytest/json` → **9.1.1** | The pin in `pyproject.toml` |
| Python versions `uv` offers | `uv python list` → **3.12.13** | The interpreter pin |
| `.gitignore` pattern syntax | `git-scm.com/docs/gitignore` | The `!` negation rule and directory-only patterns |
| ADK's supported Python window | plan §5 (3.10–3.14) | Why 3.12 and not the newest |

**Not checked today, deliberately:** anything on `adk.dev`. Day 0 writes no ADK code, and Principle 8
says the page is checked **on the day the symbol is used** — Day 5 is the first.

---

## §9 Say it in an interview

> "Before writing any application code I make the environment unambiguous, because most of the
> mysterious failures early in a project are ambiguity rather than bugs. One tool owns the
> environment — it installs the interpreter, holds the packages, writes a lockfile with the full
> transitive tree, and runs commands inside it, so there is no shell state to forget. The ignore
> rules go in before any secret exists, because git has no memory of ignoring something it already
> tracked and the only real fix for a committed key is rotating it. Then there is one entry point
> for every repeated command, so the gate I run and the gate CI runs cannot drift apart, and that
> gate is ordered cheapest-first so the common failure is caught in fifty milliseconds rather than
> after a test suite. And I test the guard rails: I tried four ways to commit a secret on purpose,
> two of which succeeded — which told me exactly where `.gitignore` stops and where I need a
> pre-commit hook and server-side scanning instead."

---

## §10 Done when

Not when you have read all seventeen parts. **When every box in [`CHECKLIST.md`](CHECKLIST.md) is
honestly ticked and `./m check` is green.**

There is no time estimate anywhere in this day, and there never will be (Principle 17). Day 0 might
take you one evening or four; both are the day done properly. `./m done 0` is gated on the checklist
and the checks, and on nothing else.

```bash
./m done 0
```

---

## §11 Ledger & commit

Paste these into the ledgers before running `./m done 0`. **Use the versions you actually observed**,
not the ones printed here (Principle 7).

**`docs/PROGRESS.md`** — append one row:

```text
| 0 | 2026-08-23 | — (no IDs; toolchain) | 17 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — append five rows:

```text
| git | <your git --version> | <today> | 0 | Version control + Git Bash, the shell every day document is written for. |
| uv | <your uv --version> | <today> | 0 | One binary owns the environment: install, lock, run. |
| python | <your 3.12.x> | <today> | 0 | Runtime — 3.12 per plan §5, the stability pick inside ADK's 3.10–3.14 window. |
| ruff | 0.16.4 | <today> | 0 | Lint + format, one tool. Dev dependency. |
| pytest | 9.1.1 | <today> | 0 | The test runner behind ./m check. Dev dependency. |
```

**`docs/SKILL_PROVENANCE.md`** — no rows today. First entries arrive on Day 29 (SK-12..SK-16).

**Commit message:**

```text
day-00: toolchain, skeleton, and the ./m driver
```

Day 0 closes no curriculum IDs, so there is no `— closes <IDs>` clause. Every day from Day 1 has one.

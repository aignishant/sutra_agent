# Day 0 — CHECKLIST

**IDs closed:** none (toolchain — Day 0 is a precondition, not curriculum)
**Principles served:** 2, 6, 7, 9, 10, 13, 16, 17, 18
**Parts:** 17 across 4 sections

> `./m done 0` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours. Ticking a box you did not do is a decision you are making on the
> record, which is the entire point (see [3.4](parts/03-the-m-driver/3.4-the-done-gate.md)).

## Demo command

```bash
./m check && git log --oneline -1
```

Expected: `OK all green`, then one commit reading `day-00: toolchain, skeleton, and the ./m driver`.

---

## Tools (section 1)

- [x] Git installed; **Git Bash** opens from the Start menu
- [x] `git --version` prints a version **inside Git Bash**
- [x] `git config --global user.name` / `user.email` / `init.defaultBranch main` all set
- [x] `echo "$BASH_VERSION"` prints a value and `uname -s` shows `MINGW64` (you are really in bash)
- [x] `uv --version` prints a version, **after reopening the shell**
- [x] `uv python install 3.12` succeeded and `uv python list` shows a 3.12 with a real path
- [x] Editor installed, Python + Ruff extensions added, interpreter pointed at `.venv`
- [x] `uv run python -c "import sys; print(sys.executable)"` and the editor's status bar name the
      **same** interpreter

## Skeleton (section 2)

- [x] `sutra/` created in your Projects folder, and `pwd` ends in `/sutra`
- [x] Folders exist: `sutra/`, `sutra_mcp/`, `skills/`, `scripts/`, `tests/`, `days/`, `docs/adr/`
- [x] `sutra/__init__.py`, `sutra_mcp/__init__.py`, `tests/__init__.py` exist and are **empty**
- [x] **`.gitignore` written *before* `.env` ever existed**, and it contains a line that is exactly
      `.env`
- [x] `git check-ignore -v .env` prints the rule and the line number
- [x] `git check-ignore -v .env.example` prints **nothing** (the `!` negation works)
- [x] `git init` run; `cat .git/HEAD` prints `ref: refs/heads/main`
- [x] `uv init --python 3.12 --no-readme --vcs none` run — **and `.gitignore` survived it**
- [x] `pyproject.toml` has `requires-python = "==3.12.*"` and `dependencies = []`

## Pins (Principle 7)

- [x] `ruff` and `pytest` added with `uv add --dev`, both with `==`, never `>=` or `~=`
- [x] Versions **looked up live**, not copied from this document
- [x] `uv.lock` exists and is staged; its `[[package]]` count is larger than 2
- [x] Five rows appended to `docs/PACKAGES.md` with **your** observed versions and today's date

## The `./m` driver (section 3)

- [x] `m` written, `chmod +x m` applied, `bash -n m` prints no syntax error
- [x] `head -3 m` shows the shebang, the comment, and `set -euo pipefail`
- [x] `./m` with no arguments prints the usage menu
- [x] `./m status` runs without error
- [x] `./m check` prints `OK all green`
- [x] Read the `done` branch and can say **out loud** what makes it refuse

## The memory (section 4)

- [x] `README.md` written in **your** words, answering what / why / what do I type / where next
- [x] Every `./m` command the README promises actually runs
- [x] `CLAUDE.md` written, naming the source of truth, the read order, and **precedence**
- [x] Every path referenced in `CLAUDE.md` exists (run the check in
      [4.2](parts/04-repo-memory/4.2-claude-md-the-standing-contract.md))

## Read the parts — one box each

Tick a box only when you have **read it, run its Check yourself, and answered its out-loud question**.

- [x] [1.1 Why one tool must own the environment](parts/01-toolchain/1.1-why-one-tool-owns-the-environment.md)
- [x] [1.2 Git, and a Unix shell on a Windows machine](parts/01-toolchain/1.2-git-and-the-unix-shell.md)
- [x] [1.3 uv, the one binary](parts/01-toolchain/1.3-uv-the-one-binary.md)
- [x] [1.4 Python 3.12 under uv](parts/01-toolchain/1.4-python-3-12-under-uv.md)
- [x] [1.5 The editor and the interpreter trap](parts/01-toolchain/1.5-the-editor-and-the-interpreter-trap.md)
- [x] [2.1 The folder skeleton](parts/02-repo-skeleton/2.1-the-folder-skeleton.md)
- [x] [2.2 `.gitignore` before secrets exist](parts/02-repo-skeleton/2.2-gitignore-before-secrets-exist.md)
- [x] [2.3 `git init` and what a repo is](parts/02-repo-skeleton/2.3-git-init-and-what-a-repo-is.md)
- [x] [2.4 `pyproject.toml` and the lockfile](parts/02-repo-skeleton/2.4-pyproject-and-the-lockfile.md)
- [x] [2.5 The venv you never activate](parts/02-repo-skeleton/2.5-the-venv-you-never-activate.md)
- [x] [3.1 `set -euo pipefail`](parts/03-the-m-driver/3.1-set-euo-pipefail.md)
- [x] [3.2 The `case` dispatcher](parts/03-the-m-driver/3.2-the-case-dispatcher.md)
- [x] [3.3 `./m check`, the whole-project gate](parts/03-the-m-driver/3.3-the-check-gate.md)
- [x] [3.4 `./m done`, a gate that refuses you](parts/03-the-m-driver/3.4-the-done-gate.md)
- [x] [4.1 The README a stranger reads](parts/04-repo-memory/4.1-the-readme-that-a-stranger-reads.md)
- [x] [4.2 `CLAUDE.md`, the standing contract](parts/04-repo-memory/4.2-claude-md-the-standing-contract.md)
- [x] [4.3 The first commit, and leaking a key on purpose](parts/04-repo-memory/4.3-the-first-commit-and-breaking-it.md)

## Break it on purpose — watch it go red, then fix it

A gate you have never seen fail is a gate you are trusting on faith.

- [x] **RED 1:** wrote a file with an unused import, ran `./m check`, **saw `F401` and exit 1**,
      removed it, saw `OK all green`
- [x] **RED 2:** made a checklist with one unticked box, ran `./m done 0`, **saw it refuse and print
      the line number**, and confirmed `git log` was unchanged
- [x] **RED 3:** ran all four attacks from [4.3](parts/04-repo-memory/4.3-the-first-commit-and-breaking-it.md)
      and can name **which two succeeded and why that is not a bug**

## Request budget

- [x] **0 model calls** made today, across all four providers. Cost: **$0**.
- [x] No API key exists on this machine yet (Day 1 creates the first three)

## Commit

- [x] `git status --short` reviewed line by line **before** committing
- [x] `git commit -m "day-00: toolchain, skeleton, and the ./m driver"` made
- [x] `git status --porcelain` prints **nothing**
- [x] `git ls-files | grep -E "^\.env$|\.venv/"` prints **nothing**
- [x] `docs/PROGRESS.md` row appended (see the hub's §11)

## Understanding check — answer out loud

- [x] `pip install` said success and `import` still failed. Explain it using *interpreter*,
      *site-packages* and *PATH* — and give the one command that avoids it.
- [x] Why does Sutra pin Python 3.12 rather than the newest release? Name **both** edges of the
      compatibility window.
- [x] Which of `pyproject.toml` and `uv.lock` do you edit by hand, and which one rebuilds this
      environment exactly six months from now?
- [x] Why was `.gitignore` written **before** `.env`? If a real key had already been pushed, what is
      your **first** action, and why is deleting the file not it?
- [x] What does `set -euo pipefail` protect against that plain `set -e` does not? Name two places
      where `-e` deliberately does not stop the script.
- [x] Why does `./m check` run `ruff format --check` rather than `ruff format`?
- [x] Why does the `done` branch call `"$0" check` instead of repeating the five steps?
- [x] Why is `git add -A` acceptable to automate **in this repository**, when in general it is risky?

# Day 00 - Toolchain, skeleton and the ./m driver

IDs closed: - · source: `days/day-00-toolchain-skeleton-driver/`

## Parts

### 1.1 - Why one tool must own the environment
`days/day-00-toolchain-skeleton-driver/parts/01-toolchain/1.1-why-one-tool-owns-the-environment.md` · level `foundation` · ids -

A "Python environment" is nothing more than one interpreter plus one folder of installed packages, and almost every baffling ModuleNotFoundError happens because the interpreter that ran your code and the folder that received the package belonged to two different environments.

### 1.2 - Git, and why a Unix shell on a Windows machine
`days/day-00-toolchain-skeleton-driver/parts/01-toolchain/1.2-git-and-the-unix-shell.md` · level `foundation` · ids -

Git is a machine that records snapshots of a folder and the links between them, and installing it on Windows also hands you Git Bash — a Unix shell — which is why every command in these ninety-seven days can be written once and run everywhere.

### 1.3 - uv — the one binary that owns the environment
`days/day-00-toolchain-skeleton-driver/parts/01-toolchain/1.3-uv-the-one-binary.md` · level `foundation` · ids -

uv is a single program that does the four jobs which used to need four programs — install the interpreter, create the environment, resolve and lock the dependencies, run your code inside it — and giving all four to one owner is what makes [1.1](1.1-why-one-tool-owns-the-environment.md)'s ambiguity impossible rather than merely unlikely.

### 1.4 - Python 3.12 under uv — and why not the newest
`days/day-00-toolchain-skeleton-driver/parts/01-toolchain/1.4-python-3-12-under-uv.md` · level `working` · ids -

Sutra pins Python 3.12 — not the newest release — because a version is only usable when everything you depend on supports it, and uv will fetch and manage that exact interpreter for you without it ever joining the crowd on your PATH.

### 1.5 - The editor, and the interpreter trap
`days/day-00-toolchain-skeleton-driver/parts/01-toolchain/1.5-the-editor-and-the-interpreter-trap.md` · level `working` · ids -

Your editor runs its own copy of Python to power autocomplete, error squiggles and the Run button — and if that copy is not the project's .venv, the editor will confidently lie to you about code that runs perfectly, or bless code that does not.

### 2.1 - The folder skeleton — every folder earns its place
`days/day-00-toolchain-skeleton-driver/parts/02-repo-skeleton/2.1-the-folder-skeleton.md` · level `foundation` · ids -

A project's folder layout is a set of decisions about what is allowed to depend on what, made once at the start when it is free, instead of later when it costs a refactor.

### 2.2 - .gitignore, written before any secret exists
`days/day-00-toolchain-skeleton-driver/parts/02-repo-skeleton/2.2-gitignore-before-secrets-exist.md` · level `production` · ids -

.gitignore stops git from ever noticing a file — which only works if the rule exists before the file does, because git has no memory of ignoring something it already tracked, and no way at all to un-know something it once committed.

### 2.3 - git init — and what a repository actually is
`days/day-00-toolchain-skeleton-driver/parts/02-repo-skeleton/2.3-git-init-and-what-a-repo-is.md` · level `foundation` · ids -

git init creates one hidden folder, .git, containing a content-addressed database of snapshots plus a handful of pointers into it — and once you have seen what is inside, every git command stops being an incantation and becomes an obvious operation on that database.

### 2.4 - uv init, pyproject.toml and the lockfile
`days/day-00-toolchain-skeleton-driver/parts/02-repo-skeleton/2.4-pyproject-and-the-lockfile.md` · level `working` · ids -

pyproject.toml is the one file that describes what this project is — its name, its Python version, its dependencies and the configuration of every tool it uses — and uv.lock is the machine-written record of what those descriptions resolved to, which is the only artifact that can rebuild the environment exactly.

### 2.5 - The virtual environment you never activate
`days/day-00-toolchain-skeleton-driver/parts/02-repo-skeleton/2.5-the-venv-you-never-activate.md` · level `working` · ids -

uv run <command> puts the project's environment in place for exactly the duration of that one command — which means there is no shell state to remember, get wrong, or forget you are in, and that is the whole reason Sutra never types activate.

### 3.1 - set -euo pipefail — the four words that make a script honest
`days/day-00-toolchain-skeleton-driver/parts/03-the-m-driver/3.1-set-euo-pipefail.md` · level `working` · ids -

By default a shell script keeps going after a command fails, treats a misspelled variable as an empty string, and reports success for a pipeline whose first command died — and one line at the top turns off all three, which is the difference between a gate you can trust and a gate that lies.

### 3.2 - The case dispatcher — one script, one entry point
`days/day-00-toolchain-skeleton-driver/parts/03-the-m-driver/3.2-the-case-dispatcher.md` · level `working` · ids -

A case statement turns one file into a menu of verbs — ./m check, ./m depth 0, ./m done 0 — so that every repeated command in the project has exactly one definition, in one place, that a person and a machine can both run.

### 3.3 - ./m check — the whole-project gate, and why its order matters
`days/day-00-toolchain-skeleton-driver/parts/03-the-m-driver/3.3-the-check-gate.md` · level `production` · ids -

./m check is the single sentence "is this repository healthy?" turned into a command — five steps chained so that the fastest, most-likely-to-fail step runs first, and so that any one failure stops the whole thing with a non-zero exit status.

### 3.4 - ./m done — a gate that refuses you
`days/day-00-toolchain-skeleton-driver/parts/03-the-m-driver/3.4-the-done-gate.md` · level `production` · ids -

./m done N will not commit a day while its CHECKLIST.md still has an unticked box — which turns "done" from a feeling you have at 11pm into a condition the repository can check.

### 4.1 - The README a stranger reads
`days/day-00-toolchain-skeleton-driver/parts/04-repo-memory/4.1-the-readme-that-a-stranger-reads.md` · level `working` · ids -

A README is not a description of your project — it is the first thirty seconds of someone else's experience of it, and its job is to answer what is this, why would I care, and what do I type first before they decide to close the tab.

### 4.2 - CLAUDE.md — the contract that makes the repo the memory
`days/day-00-toolchain-skeleton-driver/parts/04-repo-memory/4.2-claude-md-the-standing-contract.md` · level `production` · ids -

CLAUDE.md is a file of standing instructions that a CLI coding agent reads at the start of every session — which is what lets a project's conventions survive across sessions, across machines, and across a change of agent, instead of living in a conversation that ends.

### 4.3 - The first commit — and trying to leak a key on purpose
`days/day-00-toolchain-skeleton-driver/parts/04-repo-memory/4.3-the-first-commit-and-breaking-it.md` · level `production` · ids -

Before you trust a safety net, you attack it — so this part deliberately tries to commit a secret four different ways, watches which attempts the repository stops and which it does not, and only then makes the first commit.


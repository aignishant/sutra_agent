---
day: 93
phase: 14
phase_name: "Interop & launch"
title: "Repo public — what a stranger sees"
ids: []
principles: [2, 9, 10, 11, 13, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 14
generated: "2026-09-07"
status: written
lab_scaffolded: true
commit: ""
---

# Day 93 — Repo public: what a stranger sees

> **Yesterday (Day 92):** the hardening pass — the full security review that stands between this
> repository and a public URL, done deliberately and in order rather than at the last moment before
> the switch is flipped. It found no credential in 2,121 files or 69 commits, and it found the
> account name in **51 tracked lines across 15 day folders**, every one of them inside a real pasted
> traceback that Principle 10 required.
> **Today:** the switch. Making a repository public does not publish the code, which was always
> there; it publishes **everything the author assumed**, to somebody who shares none of it and will
> not ask. Seven checks, no provider requests, and none of them runs the agent. The verdict is
> **zero of seven** — not because ninety-three days of work are bad, but because not one of these
> questions had ever been asked. The findings are real: a README that says a part has ten sections,
> lists nine, and is enforced at eleven; fifty broken links across seventeen thousand, twenty-two of
> which a generator reproduces every run; forty-three days written with no ledger row; and a licence
> sentence pointing at a `LICENSE` file that does not exist.
> **Tomorrow (Day 94):** Phase 15 opens with Capstone I — the end-to-end scenario, run cold.

---

## §1 Where we are

Giving directions to your own house.

Somebody is coming for the first time and rings from the main road. *"Take the left after the big
tree, go past the temple, and it's the third gate."* Every word is true, it has worked a dozen times,
and it works because everyone who came before had been in the area. The stranger has not seen the
tree, does not know which of four turnings you mean, and is standing in front of the wrong temple.
The directions are not bad. They are given **from inside**, and from inside they are indistinguishable
from good ones.

For ninety-two days this repository has had one reader, and that reader wrote it. Every document has
been checked against a mind that already knows what `./m` is, why `.env` is not committed, and that
the product code is deliberately absent. Today swaps that reader for one who knows none of it, will
not ask, may arrive at a file you did not choose, and receives the commit history along with
everything else.

So the work is not writing. It is reading the repository as somebody who has never seen it — and
because that is impossible from inside, it becomes seven checks, since a script has no context to
fill the gap with either.

Six of the seven findings are fixable this week and three of them decay. The seventh —
`sutra/` being fifty-two promised modules and five present — is not a finding at all, it is the
design, and the README says so on the first screen. The day's last part sorts them by what stops
being fixable once the door is open.

---

## §2 The map

Five sections. Section 1 is who a stranger is and what they look for. Section 2 executes the README
instead of reading it. Section 3 is the docs pass. Section 4 is the scan for what should not be
there. Section 5 is the demo and the ordered list.

### 1 — The stranger

*Who arrives, what they check first, and what the README tells them.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [Public means a stranger with no context](parts/01-the-stranger/1.1-public-means-a-stranger.md) | What actually changes, and the seven checks that fall out of it | `foundation` |
| 1.2 | [The five files before the code](parts/01-the-stranger/1.2-the-five-files-before-the-code.md) | Two of five present, and why a missing `LICENSE` means all rights reserved | `working` |
| 1.3 | [The README that documents the design](parts/01-the-stranger/1.3-the-readme-that-documents-the-design.md) | 💥 Zero of three checkable claims, all drifting from one change | `working` |

### 2 — Running the README

*A README is a set of instructions, and instructions have an exit code.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [A README is a test you can run](parts/02-running-the-readme/2.1-a-readme-is-a-test.md) | Eleven commands, six runnable, and the harness bug that faked six failures | `working` |
| 2.2 | [The setup block that does not work here](parts/02-running-the-readme/2.2-the-setup-block-that-fails.md) | Two failures, one environment and one defect, and why bundling them is costly | `working` |
| 2.3 | [What a README owes, and what it does not](parts/02-running-the-readme/2.3-what-a-readme-owes.md) | Five answers a stranger needs, and the sixth question that buries them | `production` |

### 3 — The docs pass

*Seventeen thousand links, fifty dead ends, and four different owners.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Seventeen thousand links](parts/03-the-docs-pass/3.1-seventeen-thousand-links.md) | Fifty broken — and eighty-four if the checker does not know what a code block is | `working` |
| 3.2 | [Four kinds of broken link](parts/03-the-docs-pass/3.2-four-kinds-of-broken-link.md) | Three need a person, twenty-two need a fix, seven need a re-run, eighteen are frozen | `working` |
| 3.3 | [The index that regenerates broken](parts/03-the-docs-pass/3.3-the-index-that-regenerates-broken.md) | 💥 Twenty-two of twenty-two from one line, and why editing the file is the wrong fix | `production` |

### 4 — Nothing that should not be there

*The scan, the history behind it, and the record a stranger reads.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The scan before the door opens](parts/04-nothing-extra/4.1-the-scan-before-the-door-opens.md) | Two thousand files, two hits, zero real secrets — and why the report never prints a value | `production` |
| 4.2 | [History is the part you cannot take back](parts/04-nothing-extra/4.2-history-is-the-part-you-cannot-take-back.md) | Every blob in sixty-nine commits, and why rotation beats rewriting | `production` |
| 4.3 | [The ledger a stranger reads](parts/04-nothing-extra/4.3-the-ledger-a-stranger-reads.md) | Ninety-four folders, fifty-one rows, and a number that is true and understates by forty-three | `working` |

### 5 — The demo, and the list

*What to ship when the system is deliberately unbuilt, and what to do first.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [A demo that fails honestly](parts/05-the-demo/5.1-a-demo-that-fails-honestly.md) | Fifty-two promised, five present, and why a precise red beats a vague green | `production` |
| 5.2 | [What a real public repository adds](parts/05-the-demo/5.2-what-a-real-public-repo-adds.md) | Nine items, ordered by what stops being fixable | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [The document that runs](papers/01-the-document-that-runs.md) | `doi:10.1093/comjnl/27.2.97` — write one artefact, not two, and derive the machine's copy from the human's. The demo injects one wrong digit into a document: woven, it is caught in ten examples; read as prose, it is invisible and the run reports nothing wrong |

---

## §3 Setup — run this

```bash
mkdir -p days/day-93-what-a-stranger-sees/lab/papers/literate
mkdir -p days/day-93-what-a-stranger-sees/lab/candidates
cd days/day-93-what-a-stranger-sees/lab
touch _repo.py gate.py
touch firstfiles.py readme_contract.py runnable.py links.py owners.py
touch secrets.py ledger.py demo.py
touch papers/literate/doc.md papers/literate/ledger.py
touch papers/literate/weave.py papers/literate/demo.py
```

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty —
everything here is the standard library and `git`.

**What each file is for:**

- `_repo.py` is the file to read first: the repository as every check sees it. The front-door list,
  the six secret patterns, the fence-aware link extractor, and the two ledger readers. Every function
  reads the **live** tree, so the numbers move as the repository changes — a public-readiness check
  frozen to the day it was written stops being a check the next morning.
- `firstfiles.py`, `readme_contract.py`, `links.py`, `owners.py`, `secrets.py`, `ledger.py`,
  `demo.py` are the seven checks, one per file, each exiting non-zero when a stranger would be stuck.
- `runnable.py` executes the README's own commands. It is section 2's instrument and is deliberately
  **not** one of the gate's seven, because it takes a while and rewrites nothing.
- `gate.py` runs the seven and prints the verdict.
- `candidates/` holds a `LICENSE` and a `SECURITY.md` written for this repository and left **in the
  lab on purpose** — putting them at the root would be this day making a legal decision on the
  reader's behalf.
- `papers/literate/` is the paper's demo: `doc.md` is the artefact and `ledger.py` is the eleven-line
  module it describes.

The lab is gitignored repo-wide. Confirm it, because criterion 5 scans tracked files and you want to
know your own scratch code is not in scope:

```bash
git check-ignore -v days/day-93-what-a-stranger-sees/lab/_repo.py
```

**Why:**

- `days/*/lab/` is the rule for the reader's own code (Principle 9). Everything this day measures is
  about files git **is** tracking, so knowing the lab is excluded is what makes the counts mean
  something.

---

## §4 Build brief

The teaching is in `parts/`, the measurements are in `lab/`, and what is left is the part that belongs
in the repository rather than in a day folder. This day promotes the checks themselves.

**`scripts/public_check.py`** — the seven checks, as something `./m` can run.

- `TODO(me)`: `checks()` returning them as data, each a callable with a name and an exit code. Part
  1.1's `gate.py` is the shape; the difference is that this one lives where `./m check` can reach it.
- `TODO(me)`: wire it into `./m check` so a broken link, a missing `LICENSE` or a secret-shaped string
  fails the build. Part 5.2 item 9 is the argument: a finding that is not a check is one you must be
  lucky enough to notice twice.
- `TODO(me)`: an allowlist for the secret scanner — a file of known-benign matches, each with a
  reason and the name of whoever looked. Part 4.1 is why: two placeholders will fire this scan for
  ever, and an alarm that always fires stops being read.
- `TODO(me)`: make the link check exclude `legacy/` **in the checker, with a comment saying why**,
  rather than leaving eighteen permanent failures. Part 3.2's fourth group is a decision, and writing
  it into code is how a decision stops being re-argued.

**`scripts/wiki.py`** — one function, and the bug part 3.3 located.

- `TODO(me)`: rewrite relative links in `doc.answer` as it is copied into `docs/wiki/`, resolving
  against the part's own folder. Twelve of the twenty-two are sibling-style and ten are
  parent-relative, so string concatenation will not do it.
- `TODO(me)`: a test with a part whose one-line answer contains a sibling link, asserting the emitted
  wiki page's link resolves. The fix is easy and the test is what stops it regressing.

**`tests/test_public_check.py`**

- `TODO(me)`: a test that the link checker ignores a `[a](b)` inside a fenced block. Part 3.1
  measured thirty-four false positives without it.
- `TODO(me)`: a test that the secret scanner never emits a matched value — assert the output does not
  contain the fixture key. Part 4.1's `--loud` arm is the anti-pattern made runnable.
- `TODO(me)`: a test that a day folder with no `PROGRESS.md` row makes the ledger check fail.

**Four `TODO(me)`s that are not code**, in part 5.2's order — the first three decay:

- **Add `LICENSE`.** A candidate is in `lab/candidates/`. Without it the repository is visible and
  legally unusable, and the README's own licence sentence points at a file that is not there.
- **Backfill `docs/PROGRESS.md`** from `git log` — forty-three rows. It un-refuses `./m brief` and
  makes the README's headline claim true again.
- **Fix the one lint error** in `tests/test_persona.py`, so `./m check` matches what the README
  promises it prints.
- **Add `SECURITY.md` and `CONTRIBUTING.md`**, and one sentence to Setup naming the machine
  precondition behind `os error 5`.

---

## §5 The eval that must be able to fail

```bash
cd days/day-93-what-a-stranger-sees/lab
uv run python gate.py; echo "exit: $?"
```

Seven checks and a verdict. Today it exits `1` with zero passing, and the failures are the day's
findings rather than a defect in the lab.

Every check is also its own command:

```bash
uv run python firstfiles.py; echo "exit: $?"                  # 1 — two of five front-door files
uv run python firstfiles.py --readme-only; echo "exit: $?"    # 0 — one of one, by narrowing
uv run python readme_contract.py; echo "exit: $?"             # 1 — zero of three claims match
uv run python readme_contract.py --prose; echo "exit: $?"     # 0 — read it, do not check it
uv run python links.py; echo "exit: $?"                       # 1 — 50 of 17,677 broken
uv run python links.py --naive; echo "exit: $?"               # 1 — 84, of which 34 are code
uv run python owners.py; echo "exit: $?"                      # 1 — 3 / 22 / 7 / 18, four owners
uv run python owners.py --one-pile; echo "exit: $?"           # 1 — one number, nobody's job
uv run python secrets.py; echo "exit: $?"                     # 1 — 2 hits, 0 real
uv run python secrets.py --history; echo "exit: $?"           # 1 — the same 2, already committed
uv run python ledger.py; echo "exit: $?"                      # 1 — 94 folders, 51 rows
uv run python ledger.py --count; echo "exit: $?"              # 0 — "51 days complete", true
uv run python demo.py; echo "exit: $?"                        # 1 — 5 of 52 modules exist
uv run python demo.py --pretend; echo "exit: $?"              # 0 — "Sutra is ready."
uv run python runnable.py; echo "exit: $?"                    # 1 — 4 of 6 README commands work
uv run python runnable.py --list; echo "exit: $?"             # 0 — all eleven look right
```

**The gate's second block is the one to read.** It re-runs each check in its comfortable form and
prints what happens: `firstfiles --readme-only`, `readme_contract --prose`, `ledger --count` and
`demo --pretend` all **go green**, and every sentence those green runs print is true. That is the
fourth phase running in which the arm that hides the finding is the arm that exits zero, and by now
it is not a coincidence — a reassuring report is always cheaper to produce than a useful one.

The paper's demo does the same for its own claim: `demo.py` exits `0` having caught a one-digit drift
in ten executed examples, and `demo.py --off` exits `1` having read the same document and noticed
nothing.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-07 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

That is not a constraint worked around — it is what the day is. Everything a stranger meets before the
system runs is a file, a path or a commit, and all three are readable for nothing. The seven checks
read two thousand one hundred and twenty-one tracked files, seventeen thousand six hundred and
seventy-seven links and two thousand three hundred and sixty-one blobs of history, and the slowest
thing in the day is `./m check` inside `runnable.py`, which is the repository's own test suite.

**One thing was deliberately not run.** `cp .env.example .env` is the README's second Setup command
and `runnable.py` declines it, because it would overwrite a live `.env` holding real keys. Four other
commands are declined for the same class of reason — they write to `docs/`, create directories, or
commit. That is five of the README's eleven commands that no check here covers, and part 2.1 says so
rather than reporting a pass rate over the six it can reach.

---

## §7 Traps

1. **Reading the checks instead of running them.** Every finding here is one a careful reader had
   already read past, ninety-two days running — part 1.1.
2. **A missing `LICENSE` read as a formality.** No licence means all rights reserved: the repository
   becomes visible and legally unusable at the same moment — part 1.2.
3. **Narrowing a check until it passes.** `--readme-only` reports one of one and prints a sentence
   that is now false — part 1.2.
4. **Proofreading a document you already understand.** Three careful readers miss the venue on the
   invitation, because they all know where it is — part 1.3.
5. **Writing a checker that carries its own copy of the truth.** Import the enforcer; a second copy
   drifts exactly like the first — part 1.3.
6. **Trusting your own harness.** `shell=True` on Windows reported six of six README commands
   failing, which would have been a spectacular false finding — part 2.1.
7. **Bundling an environment failure with a defect.** One needs a precondition in the README, the
   other needs one command; treating them as one problem leaves the cheap fix undone — part 2.2.
8. **A link checker that does not know what a code block is.** Eighty-four against fifty, and the
   noise clusters in the days that teach with the most code — part 3.1.
9. **Reporting a count instead of an owner.** Fifty broken links is four different jobs, and the
   biggest group is the one nobody should touch — part 3.2.
10. **Editing generated output.** Twenty-two links come back on the next `./m wiki`; the fix is in
    the generator and the file is a symptom — part 3.3.
11. **A scanner that prints what it found.** The report becomes the leak, into the terminal, the CI
    log, and whatever ships that log — part 4.1.
12. **Scanning the working tree and calling it done.** A key deleted yesterday is in yesterday's
    commit for ever, and a green working-tree scan is what stops anybody looking — part 4.2.
13. **A true number that understates by forty-three days.** `51 days complete` is correct, exits
    zero, and is the number a stranger repeats — part 4.3.
14. **A demo that prints success above its own contradicting evidence.** `--pretend` reports "Sutra
    is ready" directly under `5` of `52` — part 5.1.
15. **Sorting the pre-launch list by severity.** Order it by what stops being fixable once the
    repository is public, or the licence lands after the copies were taken — part 5.2.

---

## §8 Verify before you code

Fetched and read on 2026-09-07:

| What | Where | What it said |
| --- | --- | --- |
| Paper record | <https://api.crossref.org/works/10.1093/comjnl/27.2.97> | *Literate Programming*, The Computer Journal, volume 27, issue 2, 1984, pages 97–111 |
| `doctest` | the installed Python 3.12 standard library | `DocTestParser`, `DocTestRunner`, `NORMALIZE_WHITESPACE`; `get_doctest` **copies** the globals it is given |
| `git rev-list`, `git cat-file` | `git --help` for each, and the real repository | `--all --objects` yields `<sha> <path>` with commits carrying no path; `cat-file --batch` streams `<sha> <type> <size>` headers |

**Repository facts verified by reading, not assumed:** `scripts/depth_check.py` exposes
`PART_SECTIONS` with **eleven** entries, three of them conditional; the `m` driver implements eleven
subcommands, of which the README documents nine; `scripts/wiki.py`'s `render_day` emits a part's path
as inline code and copies its one-line answer **verbatim**, which is where the wiki's links come
from; `scripts/trace.py` deliberately falls back to a bare `day-NN` link for unwritten days, with a
docstring saying it "becomes exact the moment that day is created" — which is why its seven broken
links are stale output rather than a bug; and `days/day-00-toolchain-skeleton-driver/LESSON.md`
carries `ids: []`, which is the precedent this day follows, since plan §14 assigns day 93 no IDs.

**No ADK symbol is used today**, so there is no 1.x → 2.x trap to pay for. The one version-shaped
risk this day carries is different in kind: every count in it — 2,081 files, 17,677 links, 50 broken,
94 folders, 51 rows — is a **live measurement of a moving repository**, so a reader running these
checks will get different numbers, and that is the design rather than a defect.

---

## §9 Say it in an interview

*"We were about to make a ninety-three-day repository public, and I treated that as an engineering
task rather than a switch. The framing that made it tractable was that going public does not publish
the code — the code was always there — it publishes everything the team assumed, to somebody who
shares none of it and will not ask you a question. So we wrote seven checks, all free, none of which
run the system: the front-door files, the README's claims, every relative link, who owns each broken
one, a secret scan, the ledger, and a cold-start demo. Zero of seven passed, on a repository whose
ninety-three days were all individually green, which was the point — none of those questions had ever
been asked. Two findings I would lead with. The README says every document runs ten sections, lists
nine, and our own checker enforces eleven; the two it omits are exactly the sections that arrived with
a format change the README describes correctly three paragraphs further down. That is not neglect,
it is documentation updated in the place the author was looking. The second is that twenty-two of our
fifty broken links are produced by the wiki generator on every run — it copies a paragraph out of a
day folder into another directory, and a relative link is a property of location, not of text — so
fixing the file is worse than useless because it reverts and convinces somebody it was handled. And
the thing I would want credit for is what we did not do: our demo script cannot run the system,
because the product code is deliberately the reader's work, so it reports which four modules are
missing and exits non-zero. We had a one-flag version that printed 'ready' directly above the numbers
proving it was not, and that exits zero — which is the fourth time in this project the comfortable
report was the one the machine could read."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands rather
than read them. `./m done 93` refuses to commit until they are.

The day is finished when you can look at a repository you know well and list what a stranger cannot
find out — and when you have stopped believing that reading your own documentation is a way of
checking it.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 93 | 2026-09-07 | — | 14 | <hash> | ⚠️ |
```

The IDs column is `—` because plan §14 assigns day 93 none, which is the same convention day 0 uses.

The gate column is `⚠️` and it is the verdict. `./m depth`, and every measurement in this day, were
run. What is not green: **Phase 14's gate is "A2A peer verified; repo public", and the second clause
is not closed.** Seven public-readiness checks report zero passing, and six of the seven are fixable —
`LICENSE` absent, three README claims drifted, fifty links broken, forty-three ledger rows missing,
two placeholder strings that fire the secret scan, and `./m check` red over one import-order error.
The seventh, a demo that cannot run, is the design and stays red until the reader builds the product.

**Three of the six decay** and are the ones to do before the switch: the licence, because copies taken
before it lands are not covered; the ledger, because a row gets harder to reconstruct every week; and
the lint, because the README promises that gate is green.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one new row:

```text
| Literate Programming | doi:10.1093/comjnl/27.2.97 | 1984 | 2026-09-07 | 93 | `days/day-93-what-a-stranger-sees/papers/01-the-document-that-runs.md` |
```

The title, journal, volume, issue and pages were copied from
`api.crossref.org/works/10.1093/comjnl/27.2.97` on 2026-09-07 — the record, not the memory
(§17.4.1 rule 5).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**What Phase 15 inherits.** Days 94 to 96 run the whole system cold, record a demo and audit
everything. All three assume a reader can get from a clone to a running system, which is exactly what
this day measured and found unproven: the Setup block fails on two of three commands, and the demo
reports four of six stages blocked. Capstone I's "run cold" is this day's cold-start demo with the
product code filled in.

**Commit:**

```text
day 93: repo public - what a stranger sees
```

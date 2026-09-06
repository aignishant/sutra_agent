---
day: 65
phase: 9
phase_name: "Durability and humans"
title: "Phase gate — kill it mid-run; durable triage with human approval"
ids: ["OPS-11"]
principles: [1, 2, 10, 11, 13, 15, 16, 17, 18]
kind: gate
plan_version: "v2.2.1"
parts: 24
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 65 — Phase gate: kill it mid-run; durable triage with human approval

> **Yesterday (Day 64):** the approval gate was built. The triage graph's write step now stops,
> files a decision for a person, suspends, and resumes on their answer — `NodeTool` and the 2.5
> standalone-node resumption doing the work.
> **Today:** the phase is put on trial. Four kills at four moments, a cold-eyes audit of what the
> runs left behind, and seven criteria that each end in an exit code. The verdict is whatever the
> commands say, including the parts that come out red.
> **Tomorrow (Day 66):** Phase 10 opens with the threat model — prompt injection and the lethal
> trifecta — and the first thing it does is point out that the archive Days 49 and 50 built is an
> attack surface.

---

## §1 Where we are

Phase 9 made three promises, one per sentence of its gate: **kill it mid-run, it resumes, a human
approved the write.** Days 60 to 64 built the machinery for all three — the event log, the
checkpoint, the park, the approval record, the idempotency key.

None of that is worth anything as a list of features. It is worth something as a claim, and a claim
about what happens when a process dies is only worth what somebody's attempt to kill it is worth.

So today is the day of the drill. Think of the fire alarm that gets tested at eleven on a Wednesday
while everybody is working: not because anybody doubts the alarm, but because the only version of a
fire alarm anyone should trust is one that has been set off on purpose recently, by someone who
wrote down what happened. A plan on a laminated sheet is a plan. A building that has been emptied is
a fact.

The day has two halves that feed each other. First the drill: build something you can genuinely kill,
kill it at four different moments, and read what it left on disk. Then the gate: turn what the drill
found into seven criteria that a colleague could re-run without reading any of this, and take the
verdict they produce.

There is a temptation on a day like this, and it is worth naming before the first command: a phase
gate that comes out green feels like success. It is not. A gate is an attempt to find something, and
one that finds nothing has either finished a phase or failed to look. Today's comes out **four green,
three red**, and the three reds are the most useful output of the day.

---

## §2 The map

Six sections. Section 1 is what a gate is and why it is a physical test rather than a review.
Section 2 builds the instrument — the state on disk, a process that can really be killed, and the
four moments worth killing at. Section 3 runs the four kills. Section 4 asks what the wreckage can
tell a colleague three months later. Section 5 turns all of it into seven criteria and takes the
verdict. Section 6 is what changes when the processes are pods and the drill is a habit.

### 1 — A drill, not a review

*What a gate is for, and what makes a criterion one.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A gate is a drill, not a review](parts/01-drill-not-review/1.1-a-gate-is-a-drill.md) | Why a phase gate is a thing you do to the system, not a document you read | `foundation` |
| 1.2 | [A criterion ends in an exit code](parts/01-drill-not-review/1.2-a-criterion-ends-in-an-exit-code.md) | Turning "it recovers correctly" into something two people cannot disagree about | `foundation` |
| 1.3 | [The runbook comes first](parts/01-drill-not-review/1.3-the-runbook-comes-first.md) | Writing the steps before running them, so the drill is repeatable by somebody else | `working` |

### 2 — The instrument

*You cannot kill a process usefully until the right things are on disk.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [What has to be on disk before you can kill anything](parts/02-the-instrument/2.1-what-has-to-be-on-disk.md) | The three files, and why `fsync` is the line that makes the drill honest | `working` |
| 2.2 | [A process you can actually kill](parts/02-the-instrument/2.2-a-process-you-can-actually-kill.md) | Three ways a process stops, and why only one of them is a crash | `working` |
| 2.3 | [Four moments, and why the moment is the experiment](parts/02-the-instrument/2.3-four-moments.md) | Choosing kill points at the boundaries where something changes hands | `working` |

### 3 — Four kills

*One kill per part, each answering a question no other kill can.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [K1 — killed after the work, before the checkpoint](parts/03-four-kills/3.1-killed-before-the-checkpoint.md) | The crash that costs a repeated request, and why the log knows about it | `working` |
| 3.2 | [K2 — killed after the checkpoint, before the gate](parts/03-four-kills/3.2-killed-after-the-checkpoint.md) | What a checkpoint actually buys, measured | `working` |
| 3.3 | [K3 — killed while parked, waiting for the human](parts/03-four-kills/3.3-killed-while-parked.md) | Waiting as a state rather than a process, killed by a signal from outside | `working` |
| 3.4 | [K4 — killed inside the effect window](parts/03-four-kills/3.4-killed-inside-the-effect-window.md) | The gap between doing a thing and recording it, and the only way to close it | `production` |
| 3.5 | [Two closes, and none — the failure that exits zero](parts/03-four-kills/3.5-two-closes-and-none.md) | 💥 Both wrong orders, both exiting `0`, both invisible from inside | `production` |

### 4 — The trail

*What the wreckage can tell somebody who was not there.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Four questions, three months later](parts/04-the-trail/4.1-four-questions-three-months-later.md) | Specifying an audit trail as questions rather than as fields | `working` |
| 4.2 | [The trail that cannot answer](parts/04-the-trail/4.2-the-trail-that-cannot-answer.md) | 💥 One reasonable design decision, two questions silently lost | `production` |
| 4.3 | [What a record must contain](parts/04-the-trail/4.3-what-a-record-must-contain.md) | Every field maps to a question, every question maps to a field | `production` |

### 5 — Seven criteria

*One acceptance criterion per part, each a command with an exit code.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Criterion 1 — it resumes, once](parts/05-seven-criteria/5.1-it-resumes-once.md) | Exit `0` **and** exactly one close, and why either alone is passable | `production` |
| 5.2 | [Criterion 2 — the gate cannot be bypassed](parts/05-seven-criteria/5.2-the-gate-cannot-be-bypassed.md) | Four paths to the write, and the payload swap that leaves the gate intact | `production` |
| 5.3 | [Criterion 3 — the trail answers from rows](parts/05-seven-criteria/5.3-the-trail-answers-from-rows.md) | Section 4's questions as a command that goes red | `working` |
| 5.4 | [Criterion 4 — the budget is measured](parts/05-seven-criteria/5.4-the-budget-is-measured.md) | What durability costs in requests, counted from the log | `production` |
| 5.5 | [Criterion 5 — the freshness check](parts/05-seven-criteria/5.5-the-freshness-check.md) | Asking whether the world moved, and why silence is not a result | `production` |
| 5.6 | [Criterion 6 — every day is written](parts/05-seven-criteria/5.6-every-day-is-written.md) | Comparing the plan against the disk, from independent sources | `working` |
| 5.7 | [Criterion 7 — no open IDs in the phase](parts/05-seven-criteria/5.7-no-open-ids.md) | The stocktake between §14 and every hub's own frontmatter | `working` |
| 5.8 | [The verdict — green, or a named list](parts/05-seven-criteria/5.8-the-verdict.md) | Why there is no partial credit, and what the three reds mean | `production` |

### 6 — In production

*What changes when the process is one of forty and the drill is a habit.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Draining versus killing](parts/06-in-production/6.1-draining-versus-killing.md) | Why the polite stop is tested constantly and the crash is not tested at all | `production` |
| 6.2 | [Rotate the drill](parts/06-in-production/6.2-rotate-the-drill.md) | What a fixed set of kills stops measuring, and the finding now on its third gate | `production` |

**No `papers/` today.** This is a gate day and it teaches no new paper. Three already-taught papers
carry parts and are cited and linked where they do: *Distributed snapshots* in 2.1,
*Principles of transaction-oriented database recovery* and *End-to-end arguments in system design*
elsewhere in sections 2 and 4.

---

## §3 Setup — run this

```bash
mkdir -p days/day-65-kill-it-mid-run/lab/state
cd days/day-65-kill-it-mid-run/lab
```

Fourteen files, and none of them is a package install. Today adds no dependency:

```bash
touch _store.py _desk.py runner.py approve.py drill.py deaths.py tear.py
touch trail.py bypass.py budget.py fresh.py written.py ids.py gate.py
```

**What each file is for:**

- `_store.py` and `_desk.py` are the two shared modules — everything on disk, and the five triage
  stages as deterministic stand-ins. The leading underscore marks them as imported rather than run,
  the same convention Days 50 and 51 used.
- `runner.py` is the process the drill kills; `approve.py` is the operator's side, deliberately a
  separate process so that the pause is genuinely free.
- `drill.py` runs the four kills, and `deaths.py` and `tear.py` are the two small experiments that
  justify how it kills and how it reads.
- The last seven are the seven criteria plus `gate.py`, which runs them. One file per criterion is
  what makes the list appendable — see 6.2.

Verify the state directory is gitignored before anything writes customer-shaped text into it:

```bash
git check-ignore -v days/day-65-kill-it-mid-run/lab/state/closed.jsonl
```

**Why:**

- `days/*/lab/` is already ignored repo-wide, so this should print the matching rule. If it prints
  nothing, stop and fix `.gitignore` before running the drill — Principle 9.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.

---

## §4 Build brief

The day's teaching is in `parts/` and the drill is in `lab/`. What is left for you is the piece that
belongs in the product rather than in the lab.

**`sutra/gate.py`** — the phase-gate runner, promoted out of the lab so later phases can add to it.

- `TODO(me)`: a `Criterion` dataclass carrying a label, an argument list and a working directory,
  and a `run_gate(criteria)` that runs every one, collects the failing labels, and returns an exit
  code. No early exit — 5.8 is the argument.
- `TODO(me)`: an `accepted` field, so a finding that has been decided rather than fixed can be
  recorded with a reason and stop being red. 6.2 is why this is not optional.
- `TODO(me)`: make the red-alarm test general — today it only proves criterion 2 can fail. Give a
  criterion an optional `ablation` command that must exit non-zero, and assert it for every criterion
  that has one.

**`tests/test_gate.py`**

- `TODO(me)`: a test that `run_gate` returns non-zero when any criterion does, and reports **all**
  failing labels rather than the first.
- `TODO(me)`: a test that an accepted finding does not make the gate red, and that an accepted
  finding with a passed expiry does.

Do not copy the lab scripts into `sutra/`. They are the instrument for this phase; the product piece
is the runner that will still be here in Phase 13.

---

## §5 The eval that must be able to fail

```bash
cd days/day-65-kill-it-mid-run/lab
uv run python gate.py; echo "exit: $?"
```

This is red today, and it is red for reasons the day names rather than for reasons it hides: three of
the seven criteria fail. Two of them (6 and 7) go green when Phase 9's remaining days land. One of
them (5) needs a decision from a person.

The eval that must be able to go **red on demand** is the red-alarm test the gate runs for you, and
you can run it directly:

```bash
uv run python bypass.py; echo "exit: $?"
uv run python bypass.py --trust-state; echo "exit: $?"
```

The first exits `0`, the second exits `1`. If they ever agree, criterion 2 has stopped checking
anything. Three more ablations exist and are exercised in their parts: `drill.py --mode unsafe`,
`trail.py --thin`, and `budget.py --naive`.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

Every stage in `_desk.py` is a deterministic stand-in and every cost is a counter, so the whole gate
can be re-run as often as you like. `budget.py` prints the confirmation as its last two lines.

The numbers the day *reports* are still real request counts — 4 for a clean run, 5 for one killed
mid-stage — because they are what the desk would spend against a provider. Nothing today spends them.

---

## §7 Traps

1. **Killing with an exception.** `sys.exit` and `raise` both unwind the stack, run every `finally`
   and flush every buffer. They test the deploy path, not the crash path, and a durability test built
   on them passes a system with no `fsync` anywhere. Use `os._exit` — 2.2 and 6.1.
2. **Counting from output.** A process that paid for a request and then died never printed its spend,
   so a budget summed from stdout reports crashes as *cheaper* than clean runs. Count from the log —
   5.4, and `budget.py --naive` to see it.
3. **Asserting the exit code and stopping there.** A run that closed the ticket twice exits `0` with
   a normal-looking log. Count the effect rows from outside the process after it has exited — 3.5.
4. **Executing `state["draft"]` instead of `record["payload"]`.** The approved text and the held text
   are the same string on every happy path, so this passes every test until something redrafts. It is
   a time-of-check-to-time-of-use bug with a human in it — 5.2.
5. **Storing a pointer in the approval record.** Smaller, tidier, normalised, and it costs two of the
   four audit questions with no error anywhere — 4.2.
6. **Running one kill because four are slow.** K1 alone is green on a system that closes tickets
   twice, measured in 5.1. Narrowing a criterion for speed silently redefines what the gate promises.
7. **`budget.py` resets the state directory between scenarios**, so no single scenario's log survives
   the whole run. Rebuild the one you want to inspect with `runner.py` directly.
8. **A finding that survives three gates.** `mcp==1.29.1` with no `PACKAGES.md` row has now been
   reported by Day 52's gate, Day 59's gate and this one. That is a process defect, not a package
   one — 6.2.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| `google-adk` latest | <https://pypi.org/pypi/google-adk/json> | `2.8.0`; this repo pins `2.7.1`, recorded as a finding in criterion 5 rather than upgraded (Principle 14) |
| MCP spec revision | <https://modelcontextprotocol.io/specification/> | `2026-07-28`, unchanged |
| Gemini free-tier limits | <https://ai.google.dev/gemini-api/docs/rate-limits> | per-model RPM/RPD **not published** without an AI Studio session; recorded as unread rather than guessed |
| Groq free limits | <https://console.groq.com/docs/rate-limits> | `groq/compound`: 30 RPM / 250 RPD |

**No ADK symbol is used today.** This day imports nothing from `google.adk`: the drill is plain
Python over files and child processes, deliberately, so that the durability being tested is the
repository's own and not the framework's. Day 60 and Day 61 are where the ADK resumption surface is
verified and taught, including the measured facts that 2.7.1 skips the node that was running when the
process died unless `@node(rerun_on_resume=True)` is set, and that a resumed node's edge `node_input`
is not restored while `ctx.state` is.

---

## §9 Say it in an interview

*"We closed our durability phase with a drill rather than a review. I built the triage flow so the run
state, the approval and the effect were three files on disk with `fsync` on every write, then killed
the process at four different moments — before the checkpoint, after it, while it was parked waiting
for a human, and inside the window between closing the ticket and recording that we had. The last one
is the one that matters. Do-it-then-record-it closes the ticket twice on resume, record-it-then-do-it
closes it never, and both of them exit zero with a completely normal log, so I stopped trusting exit
codes and counted rows in the effect file after every process had exited. The fix was to make the
close ledger the close itself, keyed on run plus approval, so there is no window. Then I turned the
whole thing into seven criteria that are seven commands, and the gate came out four green and three
red — the running system passes, and the repository has a package pinned with no ledger row that two
earlier phase gates had already found. I wrote that down rather than rounding up, because a finding
surviving three gates says something about the process, not the package."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the thing rather than
read it. `./m done 65` refuses to commit until they are.

The day is finished when you can kill the run at any of the four moments and say, before you look,
what the resume will cost and how many closes there will be — and when the gate's verdict, whatever
colour it is, is a sentence you would defend to somebody who was not here.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 65 | 2026-09-06 | OPS-11 | 24 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth`, `./m trace` and `./m wiki --check` are green over
this day. The Phase 9 gate itself is **not** green: `lab/gate.py` reports four green criteria and
three red — criterion 5 (freshness: `google-adk` a minor version behind, and `mcp==1.29.1` pinned with
no `PACKAGES.md` row), criterion 6 (days 61–64 have parts but no hubs) and criterion 7 (their IDs are
therefore open). Criteria 6 and 7 clear when those days land; criterion 5 needs a decision.

**`docs/PACKAGES.md`** — the row criterion 5 has now demanded three times. Paste it, having first
re-read the pin in `pyproject.toml`:

```text
| mcp | 1.29.1 | 2026-09-06 | pinned transitively via google-adk (`mcp<2,>=1.24`); row added after the Day 52, Day 59 and Day 65 gates each reported it missing (Principle 7) |
```

**`docs/PAPERS.md`** — no new rows. This day teaches no paper and cites three already recorded.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 65: phase gate - kill it mid-run; durable triage with human approval - closes OPS-11
```

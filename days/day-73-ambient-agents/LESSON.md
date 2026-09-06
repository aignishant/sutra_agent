---
day: 73
phase: 11
phase_name: "Ambient & live"
title: "Ambient agents — the nightly job (re-index, full evals, digest)"
ids: ["AG-24", "ADK-51"]
principles: [1, 2, 4, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: build
plan_version: "v2.2.1"
parts: 14
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 73 — Ambient agents

> **Yesterday (Day 72):** backoff with honesty. The ladder, the `retry-after` the server was already
> giving you, and the line after the retry loop — plus the finding that a system which retries
> successfully reports no errors at all.
> **Today:** Phase 11 opens. Every agent in this repository so far has been started by a person who
> was sitting there. Today one runs at three in the morning with nobody watching, and every design
> question follows from that single fact.
> **Tomorrow (Day 74):** Live API I — streaming architecture, and a free-quota check before any of it
> is built.

---

## §1 Where we are

An **ambient agent** is one nobody started. A scheduler wakes it, it does its work, and the only
trace it leaves is what it wrote to disk. Sutra's is the nightly job: re-index the archive Days 49
and 50 built, run the full eval set, and write a digest for the morning.

The stages are unremarkable and the day is not about them. It is about the four things that only
become problems once there is no person in the loop.

**It will die in the middle.** A run killed during the eval stage leaves an index on disk and no
scores, and the difference between a job that handles that well and one that does not is one line:
`if resume and DONE[name].is_file()`. Measured, a resumed run **skips the stage it already
completed** and redoes the two it did not — and the run log records `died_at` so that a run which
stopped is distinguishable from one that never started.

**Two runs can be alive at once.** A scheduler does not know whether last night's job is still going.
With no lock, tonight's run writes a **6-row** index and last night's slow one lands afterwards and
overwrites it with **5** — no error, no warning, and tomorrow's digest built on an index missing a
ticket. With a lock, the older run is **refused** and says so.

**The digest is the entire interface.** It is the only thing a person reads, which makes it the most
safety-critical file the job writes — and its failure mode is not being wrong, it is being
*reassuring*. Two eval cases are failing in the lab. The success-only digest names **0** of them
while every number in it is true; the attention-first digest names **2**.

**And what wakes it is a decision with a bill attached.** ADK 2.7.1's `get_fast_api_app` accepts
`trigger_sources` — and reading the installed package rather than a tutorial shows exactly two
accepted values, `pubsub` and `eventarc`, both hosted cloud services requiring a project and
credentials. Addendum 02 parks both. The operating system's own scheduler costs nothing and is what
this day uses.

---

## §2 The map

Five sections. Section 1 is what changes when nobody is watching. Section 2 is the run that dies at
three in the morning, and the two mechanisms that survive it. Section 3 is the morning after — the
run log, the digest, and the failure nobody notices. Section 4 is what wakes the job. Section 5 is
what it costs and what a real ambient system adds.

### 1 — The agent nobody watches

*What changes when the person who would have answered the question is asleep.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [Nobody is watching](parts/01-the-agent-nobody-watches/1.1-nobody-is-watching.md) | An ambient agent cannot ask, cannot be corrected, and cannot stop halfway | `foundation` |
| 1.2 | [Three stages in a forced order](parts/01-the-agent-nobody-watches/1.2-three-stages-in-a-forced-order.md) | Each stage consumes what the last one wrote, which is why order is not a preference | `foundation` |
| 1.3 | [The first clean run](parts/01-the-agent-nobody-watches/1.3-the-first-clean-run.md) | 5 rows, 3 of 5 evals, 2 failing cases — and three files that outlive the process | `working` |

### 2 — When it dies at three in the morning

*The run that stops half-way, the run that resumes it, and the run that should not have started.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The run that dies](parts/02-when-it-dies-at-three-am/2.1-the-run-that-dies.md) | 💥 A stage that dies leaves half the artefacts and a log line that says so | `working` |
| 2.2 | [Stages you can iterate](parts/02-when-it-dies-at-three-am/2.2-stages-you-can-iterate.md) | Resume is a skip, and a skip needs the stage list to be data | `working` |
| 2.3 | [Two runs at once](parts/02-when-it-dies-at-three-am/2.3-two-runs-at-once.md) | 💥 6 rows overwritten by 5, silently, because nobody took a lock | `production` |
| 2.4 | [The lock nobody released](parts/02-when-it-dies-at-three-am/2.4-the-lock-nobody-released.md) | 💥 The fix for part 2.3 refuses every run forever after one crash | `production` |

### 3 — The morning after

*What a person reads, and what they never find out.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The run log](parts/03-the-morning-after/3.1-the-run-log.md) | A run that died and a run that never started must not look the same | `working` |
| 3.2 | [The digest that reassures](parts/03-the-morning-after/3.2-the-digest-that-reassures.md) | 💥 0 failing cases named out of 2, with every number true | `production` |
| 3.3 | [Nobody notices silence](parts/03-the-morning-after/3.3-nobody-notices-silence.md) | 💥 The digest carries no date, so last week's reads exactly like today's | `production` |

### 4 — What wakes it

*The trigger is a design decision, and one of the options has a bill attached.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [What ADK offers](parts/04-what-wakes-it/4.1-what-adk-offers.md) | `trigger_sources` accepts exactly `pubsub` and `eventarc` — read off the package | `working` |
| 4.2 | [The scheduler you already have](parts/04-what-wakes-it/4.2-the-scheduler-you-already-have.md) | 🅿️ cron and Task Scheduler, and the four things they will not do for you | `production` |

### 5 — In production

*What it spends, and what a real ambient system has that this one does not.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [What a nightly job spends](parts/05-in-production/5.1-what-a-nightly-job-spends.md) | A full eval set every night, priced in RPD against a free tier | `production` |
| 5.2 | [What a real ambient system adds](parts/05-in-production/5.2-what-a-real-ambient-system-adds.md) | Idempotency keys, at-least-once, and the on-call question | `production` |

### The paper — read it last

*Principle 4 at the scale of a day: build the resumable job, then read why the property has a name.*

| # | Paper | What it answers |
| --- | --- | --- |
| 01 | [Idempotence Is Not a Medical Condition](papers/01-idempotence.md) | `doi:10.1145/2181796.2187821` — why "apply it twice" is the property every retried system is built on |

---

## §3 Setup — run this

```bash
mkdir -p days/day-73-ambient-agents/lab/papers/idempotence
cd days/day-73-ambient-agents/lab
touch _state.py
touch nightly.py lock.py digest.py triggers.py gate.py
touch papers/idempotence/ledger.py papers/idempotence/demo.py
```

**What each file is for:**

- `_state.py` is the file to read first: the four artefacts a run leaves on disk, the archive it
  indexes, the eval set it scores, and the helpers that read and write them. Two of the five eval
  cases are expected to fail, which is deliberate — a nightly job whose evals always pass is one
  nobody would notice breaking.
- `nightly.py` is the job: three stages, `--fail-at` to kill it part-way, `--resume` to run it again
  over what the last run left.
- `lock.py` is two runs at once, with and without a lock.
- `digest.py` is the same facts written two ways.
- `triggers.py` reports what the installed ADK actually accepts for `trigger_sources`.
- `gate.py` is the eval.

Verify the lab is gitignored before the first run:

```bash
git check-ignore -v days/day-73-ambient-agents/lab/_state.py
```

**Why:**

- `days/*/lab/` is ignored repo-wide (Principle 9). Today the job writes files under `lab/state/`, and
  a job that writes files is exactly the kind that eventually writes one you did not mean to commit.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.

---

## §4 Build brief

**`sutra/nightly.py`** — the ambient job the repository will actually schedule.

- `TODO(me)`: `STAGES` as **data** — a list of `(name, callable)` you can iterate — because resume is
  a skip over that list and a hard-coded sequence of three calls cannot be skipped. Part 2.2.
- `TODO(me)`: `run(*, resume)` — an explicit flag in the signature. A job that cannot resume redoes
  finished work every time it is retried, which is the whole cost part 2.2 measures.
- `TODO(me)`: `take_lock()` before the first stage, and decide what happens when the lock is already
  held: refuse, or wait. Part 2.3 is why you need one and part 2.4 is why the naive one is worse than
  none.
- `TODO(me)`: `write_digest` that names failures rather than only successes. The gate reads the source
  for it, which is a crude check for a real property — part 3.2.
- `TODO(me)`: decide how the lock is released, including when the process is killed. Part 2.4 leaves
  this genuinely open and names the three usual answers.
- `TODO(me)`: put a timestamp in the digest. Part 3.3 is a bug in the lab, left in on purpose.

**`tests/test_nightly.py`**

- `TODO(me)`: a test that a resumed run **does not redo** a completed stage. Assert on the stage's
  output not being rewritten, not on the log line.
- `TODO(me)`: a test that a second run refuses while the lock is held.
- `TODO(me)`: a test that the digest names a failing eval case. This is the one that will save
  somebody, and it is the one that looks least like a test.

---

## §5 The eval that must be able to fail

```bash
cd days/day-73-ambient-agents/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/nightly.py`, all red today because the module is the build brief. A check
that cannot run counts as a **failure** rather than as skipped (Principle 11).

The day's red-alarm run is the paper's demo, whose two arms encode the verdict in the exit code:

```bash
cd papers/idempotence
uv run python demo.py; echo "exit: $?"
uv run python demo.py --off; echo "exit: $?"
```

The first exits `0` — the same eight operations leave the right total. The second exits `1`, with a
recorded total of 28 against a truth of 10, and nothing anywhere reporting an error. Three more
ablations exist and are exercised in their parts: `nightly.py --fail-at`, `lock.py --lock` and
`digest.py --sunny`.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

The nightly job's "evals" stage scores queries against the index with set intersection rather than by
calling a model, so the whole day runs offline. That is a simplification and part 5.1 prices the real
version: a full eval set against a free tier, every night, is the largest recurring quota commitment
this repository will make, and it is committed to by a scheduler rather than by a person.

`triggers.py` reads the installed package and contacts nothing. The two trigger sources it reports are
parked, not used.

---

## §7 Traps

1. **Designing the happy path first.** An ambient job's design *is* its failure handling; the three
   stages took ten lines and everything else on this day is about what happens when they stop — part
   1.1.
2. **Holding progress in memory.** A stage whose output is a variable cannot be resumed, because the
   variable died with the process — part 2.2.
3. **Assuming one run at a time.** The scheduler fires on a clock, not on whether the last one
   finished — part 2.3.
4. **Adding a lock and stopping there.** A lock that is never released turns one crash into every
   subsequent night failing — part 2.4.
5. **A run log that only records successes.** A run that died and a run that never started are then
   the same empty space — part 3.1.
6. **A digest that lists what worked.** Every number true, no failure named, and it stops being read
   within a fortnight — part 3.2.
7. **An artefact with no timestamp.** Last week's digest is indistinguishable from this morning's, so
   a job that silently stopped running looks exactly like one that ran — part 3.3.
8. **Reaching for a hosted trigger.** `pubsub` and `eventarc` are the only two ADK accepts, and both
   need a billing project — part 4.1, Addendum 02.
9. **Trusting cron to tell you.** It runs the command and discards the output unless you arranged
   otherwise, so a job failing every night for a month is a normal outcome — part 4.2.
10. **Pricing a nightly job by one run.** The number that matters is requests per day against a
    per-day quota, and the eval set is the multiplier — part 5.1.
11. **Retrying a stage that accumulates.** Applying a delta twice is not applying it once; the paper
    is the whole answer and the ablation is 28 against 10 — the paper part.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| `trigger_sources` | installed `google-adk==2.7.1` | `get_fast_api_app(..., trigger_sources: list[Literal['pubsub', 'eventarc']] \| None = None)` — resolved from the module's string annotations, because the module uses `from __future__ import annotations`. Part 4.1 prints it |
| `doi:10.1145/2181796.2187821` record | <https://api.crossref.org/works/10.1145/2181796.2187821> | the record splits the title: `title: ["Idempotence Is Not a Medical Condition"]` plus `subtitle: ["An essential property for reliable systems"]`, and carries an abstract. The paper document assembles the title and says so (§17.4.1 rule 5) |

**One ADK symbol is used today, in part 4.1, and it is used to be read rather than called.** The rest
of the day is files on disk, which is the honest shape of an ambient job: the framework decides how it
is woken and nothing else.

---

## §9 Say it in an interview

*"An ambient agent is one nobody started, and that single fact is the whole design. There's no person
to ask a clarifying question, no person to notice it's stuck, and no person to read the traceback — so
everything has to be decided in advance and written to disk. We built a nightly job with three stages:
re-index, run the full eval set, write a digest. The interesting part is that each stage's output is a
file, which makes it resumable — kill it during evals and re-run it, and it skips the re-index it
already finished. Then two things people get wrong. First, the scheduler doesn't know whether last
night's job is still running, so without a lock a slow run can finish after a newer one and silently
overwrite it — we measured a six-row index being replaced by a five-row one with no error anywhere. But
the naive lock is worse than none: nothing releases it when the process is killed, so one crash refuses
every night after it. Second, the digest. It's the only interface between the job and the people who
own it, and its failure mode isn't being wrong, it's being reassuring — our success-only version named
zero of two failing evals while every number in it was true. The last thing is the one nobody catches
in review: our digest had no timestamp, so a job that stopped running entirely produces a file that
looks exactly like a fresh one."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have run the commands rather than read
them. `./m done 73` refuses to commit until they are.

The day is finished when you can say what your nightly job does when it is killed during its second
stage, without opening the file — and when you can explain why the digest is the most dangerous file
it writes.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 73 | 2026-09-06 | AG-24, ADK-51 | 14 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth 73` is green over the fourteen parts and the paper.
`lab/gate.py` is **red** on all six checks by design — `sutra/nightly.py` is the build brief. Phase
11's gate is *nightly job + voice standup within free quota*; the first half lands when that build
brief is written and the second belongs to Days 74–77. The repository-wide `⚠️` carried since Day 15
is unchanged.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one row, checked live today:

```text
| Idempotence Is Not a Medical Condition | doi:10.1145/2181796.2187821 | 2012 | 2026-09-06 | 73 | `days/day-73-ambient-agents/papers/01-idempotence.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows.

**Commit:**

```text
day 73: ambient agents - the nightly job, the run that dies, and the digest nobody reads - closes AG-24, ADK-51
```

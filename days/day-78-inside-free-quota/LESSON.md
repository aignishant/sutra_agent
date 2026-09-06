---
day: 78
phase: 11
phase_name: "Ambient and live"
title: "Phase gate — ambient and voice, inside free quota"
ids: ["OPS-14"]
principles: [2, 7, 10, 11, 13, 14, 15, 16, 17, 18]
kind: gate
plan_version: "v2.2.1"
parts: 18
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 78 — Phase gate: ambient and voice, inside free quota

> **Yesterday (Day 77):** the standup agent was built — three tools called for real over a live
> session, and a measurement showing that attention-first delivers 3 of 3 urgent sentences where queue
> order delivers 0 of 2.
> **Today:** the phase is priced and then put on trial. Phase 11 put two things on a clock and never
> added up what they cost; today does, and then turns the gate's twelve-word sentence into five
> commands with exit codes. The verdict comes back **two green, two red and one that cannot be
> determined**, and the third of those is the most useful output of the day.
> **Tomorrow (Day 79):** Phase 12 opens with evals as tests — evalsets, metrics, and the two metrics
> that cost no requests at all — and the first thing it inherits is today's finding that the eval lane
> is the one whose allowance nobody has measured.

---

## §1 Where we are

Handing back a rented flat is a strange hour. You have lived there for two years and you know it
perfectly well, and none of that counts for anything, because what actually happens is that somebody
walks through it with a list. The geyser. The taps. The paint behind the almirah. The two keys and the
spare. Each item is looked at, and at the end there is either a signature or a short list of things
that are not right.

Nobody's opinion of the flat is asked for. That is what makes it useful. Two years of *it's a nice
place, we've kept it well* is a feeling, and the walk-through is a set of specific questions with
specific answers, done in an order, by somebody who will do the same walk-through next year with a
different tenant.

Phase 11 has been six days of building. An ambient job that runs at half past midnight. A streaming
architecture. A bidirectional voice loop. Voice activity detection and a tool layer that does not
freeze the line. A standup agent that says the thing that matters first. Every one of those days ended
green on its own terms, and not one of them ran any of the others or added up the bill.

The bill is where today starts, because Phase 11's gate sentence has three words in it that no day so
far has tested: **within free quota**. Those words turn out to hide an entire subject — a provider
hands you two different limits and only one of them can be answered by waiting; a line in a crontab is
a standing order nobody is ever asked to re-approve; the night is quiet on a clock and not quiet at
all in a quota window. That subject is OPS-14, quota-aware scheduling, and it is what the first three
sections of this day are for.

Then the walk-through. Five criteria, five commands, five exit codes, and a second pass that re-runs
every green one with a fault injected to check it was capable of going red. Today's comes back with
three findings, and one of them is not a failure at all — it is the answer *we cannot tell*, which is a
different thing and needs a different person to act on it.

A gate that comes back all green has either finished a phase or failed to look. This one looked.

---

## §2 The map

Five sections. Section 1 is the subject the gate sentence hides: what an allowance is, why a schedule
is a spending plan, and what Phase 11 actually costs. Section 2 is the mechanism — asking before
spending, and the three ways that goes wrong. Section 3 is what a job does when the answer is no.
Section 4 is the gate itself, one criterion per part. Section 5 is what changes when the quota is
shared with the people you are serving.

### 1 — The allowance

*The vocabulary the gate sentence is written in, and the number nobody had computed.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [An allowance, not a speed limit](parts/01-the-allowance/1.1-an-allowance-not-a-speed-limit.md) | Why backoff answers one of the two limits and makes the other one strictly worse | `foundation` |
| 1.2 | [A schedule is a spending plan](parts/01-the-allowance/1.2-a-schedule-is-a-spending-plan.md) | A crontab line is a standing order nobody is asked to re-approve | `foundation` |
| 1.3 | [Counting what it actually spends](parts/01-the-allowance/1.3-counting-what-it-actually-spends.md) | 62 against 20, and one lane that cannot be decided at all | `working` |

### 2 — Asking before spending

*The admission check, and the three ways a correct check still gets it wrong.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Ask before you spend](parts/02-asking-before-spending/2.1-ask-before-you-spend.md) | Pricing the whole run before the first request, and the branch that can say no | `working` |
| 2.2 | [The reservation, not the check](parts/02-asking-before-spending/2.2-the-reservation-not-the-check.md) | Two jobs, two truthful answers, 24 requests against an allowance of 20 | `production` |
| 2.3 | [Whose midnight resets it](parts/02-asking-before-spending/2.3-whose-midnight-resets-it.md) | 10 of 12 refused, because the window belongs to the provider | `production` |
| 2.4 | [The job that ran anyway](parts/02-asking-before-spending/2.4-the-job-that-ran-anyway.md) | 💥 14 of 14 runs asked before spending, and the night still did not happen | `production` |

### 3 — When you cannot afford it

*Three honest answers to "not enough", and the one dishonest one.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Three things a job can do when it cannot afford itself](parts/03-when-you-cannot-afford-it/3.1-three-things-a-job-can-do.md) | Skip, shrink, defer — and which property of the job decides | `working` |
| 3.2 | [The shrunken run that reports as full](parts/03-when-you-cannot-afford-it/3.2-the-shrunken-run-that-reports-as-full.md) | 💥 `evals: 10 of 10 passed`, every word true, six failures unseen | `production` |

### 4 — The gate

*One acceptance criterion per part, each ending in an exit code.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [What Phase 11 promised](parts/04-the-gate/4.1-what-phase-11-promised.md) | Twelve words read as three claims plus the two every gate carries | `foundation` |
| 4.2 | [Criterion 1 — the nightly runs, dies honestly and resumes](parts/04-the-gate/4.2-criterion-1-the-nightly.md) | Three assertions, and the only one a broken job could not fake | `working` |
| 4.3 | [Criterion 2 — the voice standup delivers and can be stopped](parts/04-the-gate/4.3-criterion-2-the-voice-standup.md) | Delivery before the listener leaves, and a channel that can be interrupted | `working` |
| 4.4 | [Criterion 3 — the phase fits a free-tier allowance](parts/04-the-gate/4.4-criterion-3-the-phase-fits.md) | Exit `2`, and why "cannot determine" is not a kind of failure | `production` |
| 4.5 | [Criterion 4 — the freshness check](parts/04-the-gate/4.5-criterion-4-the-freshness-check.md) | The offline half checked, the online half printed as commands | `working` |
| 4.6 | [Criterion 5 — every day written, no ID left open](parts/04-the-gate/4.6-criterion-5-every-day-written.md) | Three independent sources, two agreeing and one missing 27 rows | `working` |
| 4.7 | [The verdict](parts/04-the-gate/4.7-the-verdict.md) | Two green, two red, one undetermined — and the pass that tests the tests | `production` |

### 5 — In production

*What changes when the allowance is shared with the people you are serving.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The nightly competes with the day](parts/05-in-production/5.1-the-nightly-competes-with-the-day.md) | There is no spare quota at night, and the ledger is a lower bound | `production` |
| 5.2 | [What a real quota-aware scheduler adds](parts/05-in-production/5.2-what-a-real-scheduler-adds.md) | Nine specific things, two of them parked and for different reasons | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [Does it fit? — the 1973 utilisation test](papers/01-schedulability.md) | `doi:10.1145/321738.321743` — the sum that answers "will all of this fit?" before anything runs, with the demo refusing one job to land at 14 of 20 where the ablation lands at 62 of 20 |

---

## §3 Setup — run this

```bash
mkdir -p days/day-78-inside-free-quota/lab/papers/schedulability
mkdir -p days/day-78-inside-free-quota/lab/state
cd days/day-78-inside-free-quota/lab
touch _phase.py spend.py admit.py window.py anyway.py degrade.py
touch c1_nightly.py c2_voice.py c3_quota.py c4_fresh.py c5_written.py gate.py
touch papers/schedulability/fit.py papers/schedulability/demo.py
```

**What each file is for:**

- `_phase.py` is the file to read first: Phase 11's five jobs, each with its period, its per-run cost
  and a sentence saying where that cost came from, plus the allowance table and its sources. The
  leading underscore marks it as imported rather than run, the same convention days 73 to 77 used.
- `spend.py` prices the schedule two ways and is the day's first measurement.
- `admit.py`, `window.py`, `anyway.py` and `degrade.py` are section 2 and section 3, one experiment
  each. Every one of them has an ablation flag.
- The five `c*.py` files are the criteria and `gate.py` runs them. One file per criterion is what makes
  the list appendable when Phase 12 adds its own — part 4.1 is the argument.
- `papers/schedulability/` holds the paper's demo: `fit.py` is the 1973 test and nothing else, and
  `demo.py` offers four jobs to a 20-request allowance with and without it.

This day runs three other days' labs. Confirm they are there before starting, because criteria 1 and 2
shell out to them:

```bash
ls ../day-73-ambient-agents/lab/nightly.py \
   ../day-75-the-bidi-voice-loop/lab/barge_in.py \
   ../day-77-the-standup-agent/lab/live.py
```

**Why:**

- Criterion 1 runs Day 73's nightly three times; criterion 2 runs Day 77's standup twice and Day 75's
  barge-in once. They are run as **commands**, not imported, because a criterion must test the thing as
  it is deployed — part 4.2 is the argument.

Verify the state directory is gitignored before anything writes a ledger into it:

```bash
git check-ignore -v days/day-78-inside-free-quota/lab/state/quota.json
```

**Why:**

- `days/*/lab/` is ignored repo-wide (Principle 9). Today's ledger is invented arithmetic, but a real
  quota ledger records what a real key spent, which is closer to a secret than it looks.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.

---

## §4 Build brief

The teaching is in `parts/`, the drill is in `lab/`, and what is left for you is the piece that belongs
in the product rather than in the lab. Day 65 promoted the gate runner into `sutra/gate.py`; today
promotes the thing that decides whether a run may start.

**`sutra/quota.py`** — the allowance ledger and the admission decision.

- `TODO(me)`: an `Allowance` record holding a `(provider, model)` lane, a requests-per-window number
  **or `None`**, the date it was observed and one sentence saying how. Part 1.3 is why `None` is a value
  rather than a missing key.
- `TODO(me)`: `reserve(lane, cost) -> bool` that answers and takes in one write, and `release(lane,
  cost)` for a run that spent less than it reserved. Part 2.2 is the measurement; part 5.2 item 3 is the
  expiry it will need and is deliberately not specified here.
- `TODO(me)`: decide what the window key is and write down why. Part 2.3 measured 10 of 12 requests
  refused by a scheduler that got this wrong, and there is no correct answer that does not involve
  naming a timezone out loud.
- `TODO(me)`: a `Verdict` with **three** values, not two, and an exit-code mapping. Collapsing "cannot
  say" into "fail" is the thing part 4.4 spends a whole part arguing against.

**`sutra/schedule.py`** — the spending plan, and the priority order.

- `TODO(me)`: a `Job` record — name, lane, period, cost, degradation strategy, priority — and
  `demand(lane)` over the set. Part 1.2 argues the strategy and the priority belong in this row rather
  than inside each job's code.
- `TODO(me)`: write the priority order down, argue with it once, and leave the argument in a comment.
  Part 2.4 measured what an unwritten priority order costs: 14 of 14 runs asked before spending and the
  night still did not happen.
- `TODO(me)`: make the plan and the real schedule check each other. Part 5.2 item 1 says this is first
  on the list because every other number is worthless without it. You decide which direction it runs.

**`tests/test_quota.py`**

- `TODO(me)`: a test that two reservations for the same lane cannot both succeed when only one fits.
  That is part 2.2's measurement as a test, and it is the one that would go red if somebody replaced
  `reserve` with `check`.
- `TODO(me)`: a test that a lane with an unmeasured allowance returns the third verdict and never the
  first. Write it so that it fails if somebody adds a default.
- `TODO(me)`: a test that the window key does not change when the machine's local date changes but the
  UTC date does not.

**One `TODO(me)` that is not code**, and part 5.2 item 9 is the argument for doing it: measure
Flash-Lite's daily allowance with one controlled burn at the start of a window, and add the dated row to
`docs/PACKAGES.md` beside the 2026-08-25 row that did exactly this for Flash. Until that row exists,
criterion 3 cannot answer.

---

## §5 The eval that must be able to fail

```bash
cd days/day-78-inside-free-quota/lab
uv run python gate.py; echo "exit: $?"
```

Red today, and red for reasons the day names rather than hides: two criteria pass, two fail and one
returns `2` — cannot determine. Part 4.7 reads the verdict row by row.

`gate.py` also runs its own red-alarm test: every criterion that came back green is re-run with the
fault it exists to catch injected, and a criterion that stays green is reported as `BLIND` and fails the
gate exactly as a red one does. You can run those two by hand:

```bash
uv run python c1_nightly.py --break-it; echo "exit: $?"
uv run python c2_voice.py --break-it; echo "exit: $?"
```

Both exit `1`. If either ever exits `0`, that criterion has stopped checking anything and the verdict
table is decoration.

Four more ablations exist and each is exercised in its own part:

```bash
uv run python admit.py --check      # 24 of 20, both jobs told the truth
uv run python window.py --local     # 10 of 12 refused
uv run python anyway.py --fifo      # the night did not happen
uv run python degrade.py --quiet    # evals: 10 of 10 passed, six failures unseen
```

Every one of those exits `1` where its honest counterpart exits `0`. The paper's demo does the same for
its own claim: `demo.py` exits `0` at 14 of 20 and `demo.py --off` exits `1` at 62 of 20.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-06 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

Every number in this day is arithmetic over a fixture or a count of what another day's lab did, and
every one of those labs was itself zero-request. Nothing today calls a model.

That leaves the honest gap this whole day is about, and it is worth stating in the budget section
rather than burying it: **the numbers this day reports are what the real system would spend, and the
real system has never been run.** 62 requests a day is a plan, not an observation. The one genuinely
observed quota number in the day — 20 requests a day for `gemini-3.7-flash` — was read off a live 429 on
2026-08-25 and is in `docs/PACKAGES.md`. The other lane's allowance is unmeasured, which is criterion 3's
verdict and the day's largest finding.

---

## §7 Traps

1. **Answering an allowance with backoff.** A per-day quota does not refill because you waited eight
   seconds. Day 2 measured it: 28 requests across a quarter of an hour, each obeying the stated
   `Please retry in ~53s`, all refused. Read the **quota name** out of the 429 body before deciding whether to sleep —
   part 1.1.
2. **Checking instead of reserving.** Two jobs, two correct answers, 24 requests spent against 20. The
   check is not wrong; it is the gap after it — part 2.2.
3. **Keying the ledger on `date.today()`.** Whose day is that? On a UTC+05:30 machine it disagrees with a
   UTC window for five and a half hours out of every twenty-four, and a nightly at 00:30 runs inside
   exactly that gap — part 2.3.
4. **Being quota-aware with no priority order.** Every run asks, every answer is right, and the clock
   decides what survives. The clock has no opinion about what matters — part 2.4.
5. **Reporting a rate without its population.** `evals: 10 of 10 passed` is true and describes a suite
   with six failures in it. A tighter quota makes the morning report look *better*, which is the wrong
   direction for a signal to move — part 3.2.
6. **Collapsing "cannot determine" into "failed".** They need different people and different actions,
   and the one that gets acted on is the one that looks like the more familiar problem — part 4.4.
7. **`left != ["index.json"]` written as `"index.json" in left`.** The containment version passes the
   exact fault criterion 1 exists to catch, and turns the criterion blind in one line — part 4.2.
8. **Assuming the night is free.** The nightly at 00:30 local is 19:00 UTC, which is the *end* of the
   provider's window, spending what the day left — parts 2.3 and 5.1.
9. **A finding that survives four gates.** `mcp==1.29.1` has now been reported with no `PACKAGES.md` row
   by the day 52, 59, 65 and 78 gates. That is a process defect, not a package one — part 4.5.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| `google-adk` latest | <https://pypi.org/pypi/google-adk/json> | `2.8.0`; this repo pins `2.7.1`, recorded as a criterion 4 finding rather than upgraded (Principle 14) |
| MCP spec revision | <https://modelcontextprotocol.io/specification/> | `2026-07-28`, unchanged since Day 65's gate |
| Gemini free-tier limits | <https://ai.google.dev/gemini-api/docs/rate-limits> | *"Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio."* No free-tier RPM/RPD table is published on the page |
| Groq free limits | <https://console.groq.com/docs/rate-limits> | the free-plan table exists but its numbers require a signed-in session; the page points at `/settings/limits` |
| Paper record | <https://api.crossref.org/works/10.1145/321738.321743> | *Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment*, Journal of the ACM 20(1), 1973, pp. 46–61. The ACM DL page returns HTTP 403 without a session, so the citation is copied from the Crossref record |

**No ADK symbol is used today.** This day imports nothing from `google.adk`: the scheduler is plain
Python over files and child processes, deliberately, so the quota discipline being tested is this
repository's own and not a framework's. The ADK surface for waking an agent from outside was verified
and parked on
[Day 73 part 4.1](../day-73-ambient-agents/parts/04-what-wakes-it/4.1-what-adk-offers.md) —
`get_fast_api_app(..., trigger_sources=[...])` accepts exactly `pubsub` and `eventarc`, both hosted
services needing a project and credentials.

---

## §9 Say it in an interview

*"We closed our ambient-and-voice phase by pricing it before testing it, and the pricing was the part
that found things. The gate sentence said 'within free quota', so I added up what the schedule actually
commits per day, per provider-and-model pair — and it came to 62 requests a day against the one
allowance we had ever measured, which was 20, read off a live 429 months earlier. Seventy-seven per cent
of that was the daytime desk, not the new ambient work, which nobody would have guessed. Then the more
uncomfortable finding: the second lane's allowance was simply unknown. Neither provider publishes free
tier numbers without a signed-in session, so we'd been committing sixty requests a night against a limit
nobody had looked at. I gave that criterion a third exit code — cannot determine — rather than calling
it a failure, because 'we're over' and 'we don't know' need different people to act on them. Along the
way I measured three things that all look fine and are not: check-then-spend lets two jobs that both
asked politely spend 24 of 20; keying the ledger on the machine's local day instead of the provider's
window gets 10 of 12 requests refused on a UTC+5:30 box, because our nightly at 00:30 is actually 19:00
the previous UTC day; and being quota-aware with no priority order means the clock decides — fourteen of
fourteen runs asked before spending and the night still didn't happen, because the desk woke first and
took the lot. The gate came back two green, two red, one undetermined. One of the reds is a missing
ledger row that four separate gates have now reported, which says something about our process rather
than about the package."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands rather
than read them. `./m done 78` refuses to commit until they are.

The day is finished when you can look at a crontab — any crontab, not this one — and say what it costs
per day, per lane, and what gets cut first when it cannot all run. And when you can say why the answer
*we cannot tell* is a result rather than an excuse.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 78 | 2026-09-06 | OPS-14 | 18 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth`, `./m trace` and `./m wiki --check` are green over this
day. The **Phase 11 gate itself is not green**: `lab/gate.py` returns two PASS, two FAIL and one CANNOT
DETERMINE. Criterion 3 cannot decide the Flash-Lite lane until somebody measures it. Criterion 4 is red
on `mcp==1.29.1` having no `PACKAGES.md` row. Criterion 5 is red because no day since 50 has a progress
row, so twenty-eight days' IDs are open by this repository's own definition.

**`docs/PACKAGES.md`** — the row four gates have now demanded. Paste it, having first re-read the pin in
`pyproject.toml`:

```text
| mcp | 1.29.1 | 2026-09-06 | pinned transitively via google-adk (`mcp<2,>=1.24`); row added after the Day 52, Day 59, Day 65 and Day 78 gates each reported it missing (Principle 7) |
```

**`docs/PAPERS.md`** — one new row:

```text
| Scheduling Algorithms for Multiprogramming in a Hard-Real-Time Environment | doi:10.1145/321738.321743 | 1973 | 2026-09-06 | 78 | `days/day-78-inside-free-quota/papers/01-schedulability.md` |
```

The title, journal, volume, issue and pages were copied from
`api.crossref.org/works/10.1145/321738.321743` on 2026-09-06, because the ACM Digital Library page
returns HTTP 403 without a session. The record, not the memory (§17.4.1 rule 5).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 78: phase gate - ambient and voice, inside free quota - closes OPS-14
```

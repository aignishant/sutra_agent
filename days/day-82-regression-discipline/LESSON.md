---
day: 82
phase: 12
phase_name: "Evals"
title: "Regression discipline — evals in CI, and the run that rides the nightly"
ids: ["OPS-15", "ADK-62"]
principles: [1, 2, 7, 8, 10, 11, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 13
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 82 — Regression discipline: evals in CI, and the run that rides the nightly

> **Yesterday (Day 81):** the judge became the subject. A rater that split three-two on every case and
> never read anything agreed with the human labels on 20 of 24, because 83.3% is the base rate — and
> removing one column from the report turned that into *"both judges agree with us most of the time;
> ship it."*
> **Today:** the three instruments start being compared against themselves. A regression is a claim
> about two runs, and Phase 12 has never stored one. ADK writes a complete result file for every run
> and this repository's `.gitignore` line 24 throws it away; the six free checks belong on every
> commit and the two judged ones cost 270 requests a night against a measured allowance of 20; and a
> nightly that finds a regression exits **0**, because a job's exit code says whether it ran.
> **Tomorrow (Day 83):** the Phase 12 gate, on a phase whose product is measurement.

---

## §1 Where we are

The pencil lines on the door frame, with dates next to them.

Measuring a child is easy — anybody has a tape. What is rare is the door frame: somebody, on an
ordinary Tuesday, making a mark that will not be useful for six months, and then not painting over it.
Without the marks you can still measure perfectly and you cannot answer the only question anybody
asks, because *is she growing* is not about today's number.

Phase 12 built three instruments in three days. Day 79's deterministic metrics, Day 80's rubric, Day
81's judge. Every measurement in those days was taken once, printed to a terminal, and lost — so the
question *did anything get worse* has, so far, no mechanism at all.

Today builds the door frame, and finds that most of it already exists. ADK writes a complete result
file for every eval run, with per-case, per-metric scores in it, into `.adk/eval_history/`. And this
repository's `.gitignore` line 24 is `.adk/`, written on Day 0 for an excellent reason — that is where
session stores go, and Phase 14 makes this repository public. Two correct decisions, made months apart
by people solving different problems, composing into a regression suite with no history.

The rest of the day is the discipline around the comparison. Three things move an eval score — the
desk, the judge, the data — and only one of them is what you are measuring, so a difference is a
question rather than an answer. Six of Phase 12's eight checks cost nothing and belong on every
commit; the two that cost 270 requests ride the nightly, where a daily allowance resets. And a red
build has to be a decision: fail on every difference and you fail on every new case, so the rule has to
name which of the three categories stops a merge.

The day's sharpest finding is the quietest. The nightly runs, the eval stage finds a regression, the
digest says `REGRESSED: one_lookup` in capitals — and the job exits **0**, because every stage
completed and that is what a job's exit code means.

---

## §2 The map

Five sections. Section 1 is what a regression is and what a comparison has to control for. Section 2
is ADK's own result file and what this repository does with it. Section 3 is the two cadences.
Section 4 is what a build should refuse. Section 5 is the bill and the list.

### 1 — What a regression is

*A claim about two runs, and the three things that can move a number.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A regression is a comparison, not a failure](parts/01-what-a-regression-is/1.1-a-regression-is-a-comparison.md) | Why `8/8` to `6/9` names none of the three things that moved | `foundation` |
| 1.2 | [Three things that move a number](parts/01-what-a-regression-is/1.2-three-things-that-move-a-number.md) | The desk, the judge, the data — and the fourth answer, *cannot tell* | `foundation` |
| 1.3 | [What has to be written down](parts/01-what-a-regression-is/1.3-what-has-to-be-written-down.md) | Four fields, and one recorded string deciding three different verdicts | `working` |

### 2 — The result is a file

*ADK already writes the history. The question is whether anything keeps it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The result is a file](parts/02-the-result-is-a-file/2.1-the-result-is-a-file.md) | `.adk/eval_history/`, `.evalset_result.json`, and what the record does not contain | `working` |
| 2.2 | [The history this repository throws away](parts/02-the-result-is-a-file/2.2-the-history-this-repo-throws-away.md) | 💥 `.gitignore:24:.adk/`, and why relaxing it is the wrong fix | `production` |
| 2.3 | [Comparing two runs](parts/02-the-result-is-a-file/2.3-comparing-two-runs.md) | Three lookups that can miss, and the one this lab cannot see | `working` |

### 3 — Two cadences

*Free on every commit; judged on the nightly.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The fast half, on every commit](parts/03-two-cadences/3.1-the-fast-half-on-every-commit.md) | Six checks at zero requests against two at 270 — and 3,240 if you get it wrong | `working` |
| 3.2 | [The full run rides the nightly](parts/03-two-cadences/3.2-the-full-run-rides-the-nightly.md) | What batching buys, what it costs, and why 270 still does not fit | `working` |
| 3.3 | [The suite that ran and told nobody](parts/03-two-cadences/3.3-the-suite-that-ran-and-told-nobody.md) | 💥 A regression found, named, and reported as `exit: 0` | `production` |

### 4 — What CI must refuse

*A red build is a decision about which differences stop a merge.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [A red build is a decision](parts/04-what-ci-must-refuse/4.1-a-red-build-is-a-decision.md) | The rule that survives, and the two reds with different owners | `working` |
| 4.2 | [Flaky by construction](parts/04-what-ci-must-refuse/4.2-flaky-by-construction.md) | 💥 Five quarantined checks, the oldest 203 days, and nothing saying so | `production` |

### 5 — In production

*Where the money is, and what is still missing.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [What a regression report costs](parts/05-in-production/5.1-what-a-regression-report-costs.md) | The comparison is free; the baseline is the whole bill | `production` |
| 5.2 | [What a real regression suite adds](parts/05-in-production/5.2-what-a-real-regression-suite-adds.md) | Nine items, three of which take ninety minutes between them | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [Which change broke it — narrowing by experiment](papers/01-which-change-broke-it.md) | `doi:10.1145/318774.318946` — finding a cause is a search, not a reading. The demo isolates an interacting pair in 34 runs out of 256 subsets; the ablation exonerates all eight changes individually while the suite is still red |

---

## §3 Setup — run this

```bash
mkdir -p days/day-82-regression-discipline/lab/papers/delta
cd days/day-82-regression-discipline/lab
touch _runs.py compare.py history.py cadence.py nightly.py flake.py gate.py
touch papers/delta/ddmin.py papers/delta/demo.py
```

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty —
everything this day uses is already in `google-adk==2.7.1`.

**What each file is for:**

- `_runs.py` is the file to read first: two nights of results, built as ADK's own `EvalCaseResult` and
  `EvalSetResult`, differing in exactly three ways — one real regression, one judge flip, one new
  case — with a `TRUTH` dictionary a person wrote so the comparison can be checked rather than
  believed.
- `compare.py` is the comparison, with `--count` and `--unrecorded`.
- `history.py` saves both runs through `LocalEvalSetResultsManager` and asks git what it thinks of the
  directory they went into.
- `cadence.py` splits the eight checks by cost; `nightly.py` is section 3's eval stage; `flake.py` is
  the quarantine.
- `gate.py` is the day's eval against `sutra/regress.py`.
- `papers/delta/` holds the paper's demo: `ddmin.py` is the algorithm and nothing else.

`history.py` writes into the lab. Verify that is gitignored before running it:

```bash
git check-ignore -v days/day-82-regression-discipline/lab/_runs.py
```

**Why:**

- `days/*/lab/` is ignored repo-wide (Principle 9), which is also why part 2.2 asks git about
  `sutra/.adk/eval_history` rather than about the lab — the rule that matters is the repository's, not
  this folder's.

---

## §4 Build brief

The teaching is in `parts/`, the measurements are in `lab/`, and what is left is the piece that belongs
in the product. Day 79 promoted the eval suite, Day 80 the rubric, Day 81 the judge; today promotes the
comparison.

**`sutra/regress.py`** — the desk's regression discipline, as code the nightly and CI both import.

- `TODO(me)`: `save(result)` writing through `LocalEvalSetResultsManager` — pointed at a directory that
  is **not** `.adk/`, and committed. Part 2.2 measured `.gitignore:24:.adk/`; do not relax that line.
- `TODO(me)`: the four provenance fields from part 1.3, written **at run time from the objects that
  produced the run**, in a sibling file rather than as extra keys on somebody else's pydantic model.
- `TODO(me)`: `history()` returning previous runs oldest first. `list_eval_set_results` returns names
  whose ordering is chronological only because they end in `time.time()` — decide whether to rely on
  that or to sort by the `creation_timestamp` inside each file, and say why in a comment.
- `TODO(me)`: `compare(before, after)` iterating **the union** of the two case sets, with a third
  branch for removals. Part 2.3 named the gap and gave the one-line fix; the removal branch is yours.
- `TODO(me)`: `unresolved` — a difference with no recorded judge model is reported as unattributable
  and exits non-zero. Part 1.2's `CANNOT TELL`, as a return code rather than a string.
- `TODO(me)`: `quarantine` entries carrying **a date**, not a day count, with an expiry that fails the
  build. Part 4.2 is why the date matters and why `MAX_DAYS` is a convention rather than a result.
- `TODO(me)`: `verdict()` — the nightly's exit code carries the suite's verdict, with **two** non-zero
  codes: one for a regression, one for the job itself failing. Part 3.3 measured what one code costs.

**`tests/test_regress.py`**

- `TODO(me)`: a test that a case present in one run and absent from the other is reported. That is part
  2.3's quiet failure, and it is the one the current lab cannot see.
- `TODO(me)`: a test that an unrecorded judge model produces `unresolved` rather than "the desk
  changed". Part 1.2's `--unrecorded` arm as a test.
- `TODO(me)`: a test that a new case that is red does **not** turn the build red. Part 4.1's rule, and
  the clause people leave out.
- `TODO(me)`: a test that a quarantine entry older than the limit fails, and that raising the limit is
  visible in a diff. The second half is a review practice rather than a test; decide which of the two
  you can actually automate and say so.

**Two `TODO(me)`s that are not code:**

- **Decide where history lives**, and do it this week. Part 5.2 item 1: one config line, thirty
  minutes, and every other item on that list is waiting on it. History that starts today exists when
  somebody needs it.
- **The allowance measurement**, now open for a fifth day: `gemini-2.5-flash-lite`'s daily allowance,
  measured with one controlled burn and given a dated `docs/PACKAGES.md` row. Part 5.1 prices the
  nightly at 270 requests and a bisection at 9,180, both on that lane, and five separate lists are
  blocked on the same number.

---

## §5 The eval that must be able to fail

```bash
cd days/day-82-regression-discipline/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/regress.py`, all red today because the module is the build brief. A check
that cannot run counts as a **failure**, never as skipped (Principle 11).

Every measurement in this day encodes its verdict in an exit code, and each has an arm that goes red:

```bash
uv run python compare.py; echo "exit: $?"               # 0 — every difference has a cause
uv run python compare.py --count; echo "exit: $?"       # 0 — 8/8 to 6/9, naming none of them
uv run python compare.py --unrecorded; echo "exit: $?"  # 1 — a difference with no cause
uv run python history.py; echo "exit: $?"               # 1 — the history directory is gitignored
uv run python cadence.py; echo "exit: $?"               # 0 — the commit gate costs nothing
uv run python cadence.py --all-in-ci; echo "exit: $?"   # 1 — one commit costs 14x a day
uv run python nightly.py; echo "exit: $?"               # 1 — the verdict is the exit code
uv run python nightly.py --fire-and-forget; echo "exit: $?"  # 0 — a regression, reported as success
uv run python flake.py; echo "exit: $?"                 # 1 — three entries over the limit
uv run python flake.py --no-expiry; echo "exit: $?"     # 0 — the same five, and no limit
```

Three of those belong in a pipeline, in this order, and part 4.1 says why: **`compare.py` first**,
because there is no point asking what regressed if the comparison cannot be made; then `nightly.py`,
which is the desk's gate; then `flake.py`, whose owner is whoever maintains the suite.

Note the two pairs where the **ablation exits 0**. `nightly.py --fire-and-forget` reports a regression
as a successful run, and `flake.py --no-expiry` reports five switched-off checks as fine. Both are the
report that hides the finding passing, which is this phase's recurring shape.

The paper's demo does the same for its own claim: `demo.py` exits `0` having found the interacting pair
in 34 runs, and `demo.py --off` exits `1` having exonerated all eight changes individually.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-06 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

The result types, the results manager and the file format are real and really used:
`EvalCaseResult`, `EvalSetResult` and `LocalEvalSetResultsManager` are ADK's own, and `history.py`
saves through the library and reads back through it. What is a fixture is the **content** of the two
runs, because a comparison needs two nights and generating them would have cost 540 requests to
demonstrate arithmetic that costs nothing.

That is this day's honest boundary, and part 5.1 is the shape of it: **the comparison is free and the
baseline is the entire bill.** Everything sections 1, 2 and 4 measure costs nothing to run for ever;
what costs is having a second run to compare against, which is 270 requests a night on a lane whose
allowance Day 78's criterion 3 could not determine — now for a fifth day.

---

## §7 Traps

1. **Reporting a pass count as a regression report.** `8/8` to `6/9` is true and names none of the
   three cases that moved — part 1.1.
2. **Attributing every difference to the desk.** Three things move an eval score and only one is the
   thing under test; without a recorded judge model the honest answer is `CANNOT TELL` — part 1.2.
3. **Recording the judge's alias instead of its version.** An alias tells you nobody edited the config,
   not that the rater is the same rater — part 1.3, and Day 81 part 5.1.
4. **Reading provenance at report time.** A comparison that looks up "the judge model" from today's
   config attributes both nights to today's judge, and no file is incorrect — part 1.3.
5. **Iterating one run's case set.** A walk over tonight's cases cannot see a case that vanished; a
   renamed case is a removal and an addition with its history severed — part 2.3.
6. **Assuming the history is kept.** ADK writes it correctly into a directory this repository ignores
   on purpose, and ignoring a file is not an event — part 2.2.
7. **Putting the judged checks on the commit gate.** 270 requests times twelve commits is 3,240, and a
   gate that spends the day's quota is a gate somebody will switch off — part 3.1.
8. **A job whose exit code means "it ran".** Every stage completed, so the job exits 0 on a night with
   a regression in it — part 3.3.
9. **Failing the build on every difference.** That fails on every new case and on every judge flip, and
   a barrier that comes down for nothing is a barrier people lift by hand — part 4.1.
10. **A quarantine with no date.** Five checks switched off, the oldest 203 days, every entry added for
    a good reason and none of them ever a decision to stop checking — part 4.2.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| ADK evaluation guide | <https://adk.dev/evaluate/> | the `adk eval` CLI and `AgentEvaluator.evaluate` from pytest, which is where a results manager is wired in |
| Paper record | <https://api.crossref.org/works/10.1145/318774.318946> | *Yesterday, my program worked. Today, it does not. Why?*, ACM SIGSOFT Software Engineering Notes 24(6), 1999, pp. 253–267 |
| Gemini free-tier limits | <https://ai.google.dev/gemini-api/docs/rate-limits> | no free-tier RPM/RPD table published; limits *"can be viewed in Google AI Studio"* |

**ADK symbols verified against the installed `google-adk==2.7.1`**, not only against the docs:
`EvalSetResult.model_fields` = `eval_set_result_id, eval_set_result_name, eval_set_id,
eval_case_results, creation_timestamp`; `EvalCaseResult.model_fields` including `eval_id`,
`final_eval_status`, `overall_eval_metric_results`, `eval_metric_result_per_invocation` and
`session_id` — with `eval_metric_result_per_invocation` and `session_id` **required**, which is a
`ValidationError` the first time you build one by hand; `EvalMetricResult` carrying `score` alongside
`eval_status`; `LocalEvalSetResultsManager`'s three methods and its `agents_dir` constructor;
`_ADK_EVAL_HISTORY_DIR = ".adk/eval_history"` and
`_EVAL_SET_RESULT_FILE_EXTENSION = ".evalset_result.json"`; `_get_eval_history_dir` appending
`<app_name>` **between** the agents dir and `.adk`; and `create_eval_set_result` building the id from
`time.time()`, which is why `sorted()` on the names is chronological.

**No new 1.x → 2.x trap today.** The one this phase keeps naming is ADK-73 — every model pinned
explicitly — and part 1.3's provenance fields are the record-keeping half of it: pinning the judge is
worth nothing if the run does not say which judge it used.

---

## §9 Say it in an interview

*"We had three evaluation instruments and no history, which meant we could say the suite was red and
not that anything had regressed — those are different claims and the second needs two runs. The
useful discovery was that ADK already writes a complete result file for every run, with per-case,
per-metric scores, into a `.adk/eval_history` directory — and our `.gitignore` line 24 is `.adk/`,
written on day zero because that is also where session stores go and the repo goes public. Two correct
decisions composing into a regression suite with no history, and nothing reports it because ignoring a
file is not an event. Then the discipline. An eval score has three inputs — the system, the judge and
the data — so a difference is a question, not an answer: we record the desk version, the judge model
and the evalset hash, and a difference we cannot attribute is reported as unresolved rather than blamed
on the desk. We split by cost, because six of our eight checks are free and two are 270 requests, so
the free six go on every commit and the judged pair rides the nightly where a daily allowance resets —
putting all eight on the commit gate is 3,240 requests a day, which is fourteen times a whole day's
measured allowance per commit, and a gate like that gets switched off. The finding I would lead with
though is the quiet one: our nightly found a regression, the digest named it in capitals, and the job
exited zero — because a stage-structured job's exit code means every stage completed, and cron discards
stdout. The regression was correctly detected, correctly reported, and the machine-readable channel
said everything was fine."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands rather
than read them. `./m done 82` refuses to commit until they are.

The day is finished when you can be shown a number that moved and ask the three questions in order:
did the thing under test change, did the instrument change, did the data change — and when you know
which of the three your results files can actually answer.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 82 | 2026-09-06 | OPS-15, ADK-62 | 13 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth`, `./m trace` and `./m wiki --check` are green over
this day and every measurement in it was run. What is not green: `sutra/regress.py` is the build brief
and `lab/gate.py` reports 0 of 6, by design. Two findings carry forward — the history directory is
gitignored and nothing yet writes results anywhere that survives, and the Flash-Lite allowance is
unmeasured for a fifth day, now blocking five lists.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one new row:

```text
| Yesterday, my program worked. Today, it does not. Why? | doi:10.1145/318774.318946 | 1999 | 2026-09-06 | 82 | `days/day-82-regression-discipline/papers/01-which-change-broke-it.md` |
```

The title, journal, volume, issue and pages were copied from
`api.crossref.org/works/10.1145/318774.318946` on 2026-09-06 — the record, not the memory
(§17.4.1 rule 5).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 82: regression discipline - evals in CI, and the run that rides the nightly - closes OPS-15, ADK-62
```

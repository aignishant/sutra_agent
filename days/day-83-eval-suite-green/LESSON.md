---
day: 83
phase: 12
phase_name: "Evals"
title: "Phase gate — Sutra's eval suite green"
ids: ["AG-28"]
principles: [2, 7, 8, 10, 11, 14, 15, 16, 17, 18]
kind: gate
plan_version: "v2.2.1"
parts: 14
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 83 — Phase gate: Sutra's eval suite green

> **Yesterday (Day 82):** regression discipline. ADK writes a complete result file for every run into
> a directory this repository's `.gitignore` line 24 throws away, six of the phase's eight checks are
> free and two cost 270 requests, and a nightly that found a regression exited **0**.
> **Today:** the phase is put on trial, and it is the first gate whose subject is the measuring
> equipment rather than the thing measured. Eight criteria, no provider requests, and not one of them
> runs the desk. The verdict is **three pass, four fail and one that cannot be determined** — and the
> sharpest of the four is the gate's own second clause: the trajectory rubric is graded on a
> transcript with **zero of three** recorded tool calls in it.
> **Tomorrow (Day 84):** Phase 13 opens with tracing, and the first thing it inherits is a ledger
> whose last row is day 50.

---

## §1 Where we are

The clinic thermometer that always reads normal.

Nobody looks at a thermometer and asks whether it is right; you look at the reading. The only way
anybody finds out that the instrument is broken is by putting it against something whose answer is
already known — a glass of iced water, or a child who is obviously running a fever — and seeing
whether it moves. The reading is what people want. The check is the boring thing you do first, and it
is the only reason the reading means anything.

Phase 12's gate sentence is six words: **"Full evalset green; rubric trajectories pass."** Read the
way every earlier gate was read, it asks whether the desk passes its suite. That question cannot be
answered here — the judged half costs 270 requests on a lane whose daily allowance has never been
measured, and the suite has never been run in full.

The question underneath it costs nothing and had to be settled first anyway: **can the suite be
believed if it were?** Eight criteria answer that, and every one of them is arithmetic, a file read
or an ADK comparator over recorded data.

Three pass. The evalset survives a round trip, the metrics refuse a desk that does nothing, and every
rubric line has a conversation that earns it and one that does not — and each of those three was
re-run with a fault injected and went red, so the passes mean something.

Four fail. The trajectory rubric is shown **zero of three** recorded tool calls, because ADK's
assembler reads one of the two shapes `intermediate_data` can hold and the `.evalset.json` file
round-trips into the other. The only judge this phase ever compared against human labels has a margin
of **+0.0%** and a kappa of **+0.00**. Git is tracking **zero** eval result files while two sit on
disk, caught by two different ignore rules written for two different good reasons. And **five days of
this phase have no `PROGRESS.md` row**, so ten concept IDs are open on work that is finished.

One cannot be determined, and that is the third exit code rather than a rounding.

---

## §2 The map

Five sections. Section 1 reads the gate sentence and establishes why green is not the evidence.
Sections 2 to 4 are the eight criteria, grouped by what they check: the instruments, the judge and
the bill, the repository. Section 5 is the verdict and the handover.

### 1 — Reading the gate

*What the six words ask, and why the answer cannot be the word "green".*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A gate on the instruments](parts/01-reading-the-gate/1.1-a-gate-on-the-instruments.md) | Why this gate measures the ruler, and the eight checks that fall out of it | `foundation` |
| 1.2 | [What "full evalset green" actually asks](parts/01-reading-the-gate/1.2-what-full-evalset-green-asks.md) | Four questions six words do not answer, and the reading this day takes | `foundation` |
| 1.3 | [Green is not evidence](parts/01-reading-the-gate/1.3-green-is-not-evidence.md) | 💥 Two ways to be green having measured nothing, both measured | `working` |

### 2 — The instrument criteria

*Criteria 1 to 4: the data, the metrics, the rubric, and what the rubric judge is shown.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Criterion 1 — the evalset survives a round trip](parts/02-instrument-criteria/2.1-criterion-1-the-evalset-round-trips.md) | Nine tool calls out and back, and the type that decides criterion 4 | `working` |
| 2.2 | [Criterion 2 — the suite goes red against a stub desk](parts/02-instrument-criteria/2.2-criterion-2-the-suite-goes-red.md) | 0 of 3 for a desk that does nothing, and three near-misses the check cannot see | `working` |
| 2.3 | [Criterion 3 — every rubric line is exercised both ways](parts/02-instrument-criteria/2.3-criterion-3-the-rubric-is-exercised.md) | A line nothing fails cannot tell a reader from a rubber stamp | `working` |
| 2.4 | [Criterion 4 — the rubric can see the tool calls](parts/02-instrument-criteria/2.4-criterion-4-the-rubric-can-see.md) | 💥 3 recorded, 0 rendered — the gate's second clause, and it fails | `production` |

### 3 — The judge and the bill

*Criteria 5 and 6: what the judge is worth, and whether the phase fits a day.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Criterion 5 — the judge beats its baseline](parts/03-judge-and-bill/3.1-criterion-5-the-judge-beats-baseline.md) | +0.0% and +0.00, and why the ablation that drops one line exits 0 | `working` |
| 3.2 | [Criterion 6 — the phase fits a free-tier day](parts/03-judge-and-bill/3.2-criterion-6-the-phase-fits.md) | 270 against an unmeasured allowance, for the fifth day running | `working` |

### 4 — The repository criteria

*Criteria 7 and 8: the two absences that no code change causes.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Criterion 7 — there is a previous run to compare against](parts/04-repository-criteria/4.1-criterion-7-there-is-a-yesterday.md) | 0 tracked, 2 on disk, two different ignore rules and neither is wrong | `working` |
| 4.2 | [Criterion 8 — every day written, no ID left open](parts/04-repository-criteria/4.2-criterion-8-every-day-written.md) | Plan and hubs agree perfectly; the ledger has no rows | `working` |

### 5 — The verdict

*What it says, what the comfortable version would have said, and what crosses the boundary.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The verdict](parts/05-the-verdict/5.1-the-verdict.md) | Three, four and one — and why the sentence matters more than the counts | `production` |
| 5.2 | [What a green Phase 12 would have meant](parts/05-the-verdict/5.2-what-a-green-phase-12-would-mean.md) | 💥 The same eight runs, two true sentences, `exit: 0` | `production` |
| 5.3 | [What Phase 13 inherits](parts/05-the-verdict/5.3-what-phase-13-inherits.md) | Five items, ordered by what gets worse if you wait | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [The number that became the target](papers/01-the-number-that-became-the-target.md) | `doi:10.1016/0149-7189(79)90048-X` — an indicator that carries a decision starts being optimised. The demo drives one real ADK metric from 0.64 to 0.99 while the behaviour it stood for goes 50% to 0%; the ablation watches the same metric without selecting on it and both numbers stay flat |

---

## §3 Setup — run this

```bash
mkdir -p days/day-83-eval-suite-green/lab/papers/indicator
cd days/day-83-eval-suite-green/lab
touch _phase.py gate.py
touch c1_roundtrip.py c2_stub.py c3_separates.py c4_sees.py
touch c5_margin.py c6_fits.py c7_yesterday.py c8_written.py
touch papers/indicator/pool.py papers/indicator/demo.py
```

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty —
everything here is in `google-adk==2.7.1` or the standard library.

**What each file is for:**

- `_phase.py` is the file to read first: what Phase 12 built, written down so the gate can measure it
  instead of remembering it. Three graded conversations as ADK `Invocation` objects, the four rubric
  lines, the reference labels a person wrote, day 81's twenty-four judged answers, and the request
  arithmetic from day 82's cadence table.
- `c1_roundtrip.py` to `c8_written.py` are the eight criteria, one per file, each exiting `0`, `1` or
  `2`. Three of them take a fault flag, which is what the gate's red-alarm test injects.
- `gate.py` runs all eight, re-runs the passing ones with their faults, and prints the verdict.
- `papers/indicator/` holds the paper's demo: `pool.py` is twelve desk variants and nothing else.

The lab is gitignored repo-wide. Confirm it before you start, because criterion 7 asks git questions
and you want to know which rule is answering:

```bash
git check-ignore -v days/day-83-eval-suite-green/lab/_phase.py
```

**Why:**

- `days/*/lab/` is the repository's rule for the learner's own code (Principle 9), and part 4.1 is
  about a *different* rule — `.gitignore` line 24, `.adk/` — so knowing which is which before you read
  the criterion's output is the difference between a finding and a confusion.

---

## §4 Build brief

The teaching is in `parts/`, the measurements are in `lab/`, and what is left is the part that belongs
in the product. Day 79 promoted the eval suite, Day 80 the rubric, Day 81 the judge, Day 82 the
comparison; today promotes the gate itself, plus the two smallest fixes it found.

**`sutra/gate.py`** — the phase gate as code the repository can run on itself.

- `TODO(me)`: `criteria()` returning the checks as data, with the three exit codes from part 1.1. Not
  a list of functions — a list of *processes*, so a criterion can be a repository check, a subprocess
  or an ADK call without the runner knowing.
- `TODO(me)`: the red-alarm pass. For every criterion that passed and declares a fault, re-run it with
  the fault and require a non-zero exit. A criterion that stays green is reported as `BLIND` and fails
  the gate exactly as a red one does.
- `TODO(me)`: `verdict()` printing every criterion including the passes, with the one-sentence finding
  underneath the counts. Part 5.1 is why the sentence cannot be dropped and part 5.2 measures what
  happens when it is.
- `TODO(me)`: no summary-only mode. If you add one, make it carry the failing criterion names — part
  5.2's review comment is the acceptance test: *could somebody delete a check without the summary
  changing?*

**`sutra/evalset.py`** — the two fixes from parts 2.1 and 2.4, which are one function and one
assertion.

- `TODO(me)`: `as_events(invocation)` converting an `IntermediateData` into an `InvocationEvents` so
  the trajectory rubric's assembler renders the tool calls. Part 5.3 gives the whole implementation and
  names the one decision it has to make: the author. Take it from the app's agent name, never from a
  constant.
- `TODO(me)`: extend the round-trip check to compare `call.args`, not only `call.name`. One line, and
  part 2.1's review comment is why.

**`tests/test_gate.py`**

- `TODO(me)`: a test that the assembled dialogue contains every recorded tool call. This is the
  assertion half of the criterion-4 fix and it is the more important half — the conversion will be
  written correctly and the assertion is what stops the next change from undoing it.
- `TODO(me)`: a test that a criterion which cannot fail is reported as `BLIND`. Inject a criterion that
  returns 0 unconditionally and require the gate to go red.
- `TODO(me)`: a test that an unmeasured constant produces exit `2` rather than a pass or a fail. Part
  3.2's `None` is the fixture.

**Three `TODO(me)`s that are not code**, in the order part 5.3 argues for:

- **Backfill `docs/PROGRESS.md`** from `git log` — thirty-three rows, an hour, and it is what
  `./m brief` and `./m trace` both read. This gets harder every day and the information is all there
  today.
- **Point the eval history somewhere committed**, outside `.adk/`. One config line, half an hour, and
  eight other items assume there is a yesterday.
- **Measure the Flash-Lite allowance**, now open for a fifth day and blocking five lists: one
  controlled burn, a count, a dated `docs/PACKAGES.md` row.

---

## §5 The eval that must be able to fail

```bash
cd days/day-83-eval-suite-green/lab
uv run python gate.py; echo "exit: $?"
```

Eight criteria and a verdict. Today it exits `1` with three passes, four failures and one that cannot
be determined, and the failures are the day's findings rather than a defect in the lab.

Every criterion is also its own command, and each says what it found:

```bash
uv run python c1_roundtrip.py; echo "exit: $?"                # 0 — 9 tool calls out, 9 back
uv run python c1_roundtrip.py --drop-tools; echo "exit: $?"   # 1 — nothing lost, because nothing written
uv run python c2_stub.py; echo "exit: $?"                     # 0 — 0 of 3 for a desk that does nothing
uv run python c2_stub.py --lenient; echo "exit: $?"           # 1 — the same 0.00 scores, all PASSED
uv run python c3_separates.py; echo "exit: $?"                # 0 — 4 of 4 lines have a yes and a no
uv run python c3_separates.py --one-sided; echo "exit: $?"    # 1 — 0 of 4, on the happy-path case alone
uv run python c4_sees.py; echo "exit: $?"                     # 1 — 3 recorded, 0 rendered
uv run python c4_sees.py --events; echo "exit: $?"            # 0 — same conversation, other shape, 3 of 3
uv run python c5_margin.py; echo "exit: $?"                   # 1 — margin +0.0%, kappa +0.00
uv run python c5_margin.py --raw; echo "exit: $?"             # 0 — 83.3%, and nothing to compare it to
uv run python c6_fits.py; echo "exit: $?"                     # 2 — 270 against an unknown number
uv run python c6_fits.py --assume-generous; echo "exit: $?"    # 0 — 18%, on an allowance nobody checked
uv run python c7_yesterday.py; echo "exit: $?"                # 1 — 0 tracked, 2 on disk
uv run python c8_written.py; echo "exit: $?"                  # 1 — 5 days, no ledger rows
uv run python gate.py --headline; echo "exit: $?"             # 0 — 8 checks ran, 0 errors
```

**The red-alarm test is the part that makes the three passes worth anything.** `gate.py` re-runs each
passing criterion with a fault injected and requires it to go red; a criterion that stays green is
reported as `BLIND` and fails the gate.

Note the four arms that **exit 0 while hiding a finding**: `c2_stub.py --lenient`, `c5_margin.py
--raw`, `c6_fits.py --assume-generous` and `gate.py --headline`. That is this phase's recurring shape
for the fourth day running, and part 5.2 is the tally.

The paper's demo does the same for its own claim: `demo.py` exits `0` having driven the metric from
0.64 to 0.99 while the behaviour went 50% to 0%, and `demo.py --off` exits `1` with both numbers flat.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-06 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

That is not a compromise, it is the design: a gate on measuring instruments is answerable by
comparing recorded data, and every one of the eight criteria was chosen so that it could be. The
metrics are ADK's own `TrajectoryEvaluator` and `RougeEvaluator` running unmodified; criterion 4 calls
`RubricBasedMultiTurnTrajectoryEvaluator._assemble_dialogue_history` directly, which is what the judge
would have been shown; criteria 7 and 8 shell out to `git` and read `docs/`.

What this budget cannot buy is the answer the gate sentence asks for. Running the suite in full is 270
requests — 30 for the trajectory rubric and 240 for the judged response metric — against an allowance
that criterion 6 reports as unmeasured for the fifth consecutive day. **That gap is the verdict**, and
part 3.2 is the part that refuses to close it with a guess.

---

## §7 Traps

1. **Reading the gate sentence as a question about the desk.** Nothing in this day runs the desk. Four
   of the eight criteria are about whether the instrument can produce a failure at all — part 1.1.
2. **Taking a reading of "green" silently.** Six words hide four questions, and two people can both
   use the word honestly about opposite states of the same repository — part 1.2.
3. **Reporting green from a suite that never ran.** Six free checks pass instantly and the two judged
   ones have never executed; a dashboard saying "evals: green" would be accurate about the six —
   part 1.3.
4. **Trusting a round trip because nothing was lost.** Two empty lists are equal, so a set that never
   had tool calls passes a round-trip check — part 2.1.
5. **Believing a passing canary means the suite discriminates.** Against the stub both metrics score
   `0.00` and agree; against three near-misses each metric refuses what the other gives full marks —
   part 2.2.
6. **Checking the rubric's wording and not the case set.** A well-written line that no conversation is
   supposed to fail cannot tell a careful judge from one that says yes — part 2.3.
7. **Assuming the judge sees what it is asked about.** `_assemble_dialogue_history` renders tool calls
   only under `InvocationEvents`, and an evalset file round-trips into `IntermediateData` — part 2.4.
8. **Printing an accuracy without its baseline.** 83.3% agreement against an 83.3% base rate is a
   margin of zero, and removing one line turns it into a reassurance that exits 0 — part 3.1.
9. **Supplying a missing number from memory.** `270 ≤ ?` is not a comparison, and an assumed allowance
   comes back out as a percentage with the assumption stripped off — part 3.2.
10. **Fixing the wrong `.gitignore` line.** Relaxing `.adk/` to keep eval history would commit session
    stores into a repository that goes public — part 4.1.
11. **Treating a green depth check as a finished day.** Plan, hub and ledger are three sources, and
    the first two can agree perfectly while the third is empty — part 4.2.
12. **Summarising the verdict.** `3 pass, 4 fail` invites the reading that the desk half-failed; the
    sentence is the finding and the counts are arithmetic — parts 5.1 and 5.2.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| ADK evaluation guide | <https://adk.dev/evaluate/> | the `adk eval` CLI, `AgentEvaluator.evaluate` from pytest, and the metric names used in `test_config.json` |
| Paper record | <https://api.crossref.org/works/10.1016/0149-7189(79)90048-X> | *Assessing the impact of planned social change*, Evaluation and Program Planning 2(1), 1979, pp. 67–90 |
| Gemini free-tier limits | <https://ai.google.dev/gemini-api/docs/rate-limits> | no free-tier RPM/RPD table published; limits *"can be viewed in Google AI Studio"* |

**ADK symbols verified against the installed `google-adk==2.7.1`**, not only against the docs.
`EvalSet.model_dump_json` / `model_validate_json` round-trip an evalset, and an `Invocation` whose
`intermediate_data` was built as `IntermediateData` comes back as `IntermediateData` — measured, 9
tool calls out and 9 back. `InvocationEvents.model_fields` is `['invocation_events']` and
`IntermediateData.model_fields` is `['intermediate_responses', 'tool_responses', 'tool_uses']`, so the
two shapes share no field and an attribute access across them raises. In
`rubric_based_multi_turn_trajectory_evaluator.py`, `_assemble_dialogue_history` renders a tool call
only inside `if isinstance(invocation.intermediate_data, InvocationEvents)`, and takes the agent's
name from `invocation_events[0].author` with the literal string `"agent"` as its fallback.
`judge_model_options` is a field of `RubricsBasedCriterion` and **not** of `EvalMetric` — putting it
on the metric raises `ValidationError ... extra_forbidden`, quoted in part 2.4.
`_EVAL_SET_RESULT_FILE_EXTENSION` is `".evalset_result.json"`, which is the suffix criterion 7 counts.

**The 1.x → 2.x trap this day pays for is ADK-73** — every model pinned explicitly. Criterion 4
constructs a real `JudgeModelOptions` and pins `gemini-2.5-flash-lite` even though it never calls the
model, because the default is `gemini-2.5-flash`, which is the desk's own lane, and a check that would
have spent requests if it had run is a check that will spend them the day somebody extends it.

---

## §9 Say it in an interview

*"We finished a phase whose product was the evaluation suite, so the gate could not be 'does the
system pass its tests' — it had to be 'can these tests be believed'. We wrote eight criteria, all of
them free, none of which run the agent: does the evalset survive serialisation, does the suite go red
against a stub that does nothing, is every rubric line exercised in both directions by the case set,
can the rubric judge actually see the tool calls, does the judge beat its baseline, does the suite fit
the allowance, is there a previous run to compare against, and is the ledger current. Three passed and
we re-ran each of those with a fault injected to prove they could fail. The finding I would lead with
is the fourth one. Our trajectory rubric grades safety rules about tool calls, and the framework's
transcript assembler only renders tool calls when the invocation stores them as events — while an
evalset file round-trips into the other representation. So three recorded tool calls rendered as
zero, the judge was asked whether the agent requested approval before refunding, and it answered from
a transcript with neither word in it. Nothing raised. The second finding was cheaper and worse: the
only judge we had ever compared against human labels agreed 83.3% of the time against an 83.3% base
rate, so the margin was zero. And the gate has a third exit code, because one criterion depends on a
free-tier quota nobody has measured — 270 requests against an unknown number is not a comparison, and
reporting 'cannot determine' is more useful than picking a side. We shipped it as amber with five
named items."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands rather
than read them. `./m done 83` refuses to commit until they are.

The day is finished when you can be handed a green test suite and ask the two questions that decide
whether it means anything — when did it last go red, and what would make it go red now — and when you
can say, of your own project, which of this day's eight criteria it would fail.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 83 | 2026-09-06 | AG-28 | 14 | <hash> | ⚠️ |
```

The gate column is `⚠️` and it is the verdict, not a formality. `./m depth`, `./m trace` and
`./m wiki --check` are green over this day and every measurement in it was run. What is not green:
**Phase 12 is not green** — three of eight criteria pass, four fail and one cannot be determined, and
the four failures are the trajectory rubric seeing 0 of 3 tool calls, a judge whose margin over its
baseline is +0.0%, zero stored eval runs to compare against, and five days of this phase with no
ledger row. The one that cannot be determined is the Flash-Lite allowance, unmeasured for a fifth
consecutive day and now blocking five lists.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one new row:

```text
| Assessing the impact of planned social change | doi:10.1016/0149-7189(79)90048-X | 1979 | 2026-09-06 | 83 | `days/day-83-eval-suite-green/papers/01-the-number-that-became-the-target.md` |
```

The title, journal, volume, issue and pages were copied from
`api.crossref.org/works/10.1016/0149-7189(79)90048-X` on 2026-09-06 — the record, not the memory
(§17.4.1 rule 5).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 83: phase gate - sutra's eval suite green - closes AG-28
```

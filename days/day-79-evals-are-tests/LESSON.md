---
day: 79
phase: 12
phase_name: "Evals"
title: "Evals are tests — evalsets, metrics, and the eval workhorse"
ids: ["AG-26", "ADK-58", "ADK-59"]
principles: [1, 2, 7, 8, 10, 11, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 16
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 79 — Evals are tests: evalsets, metrics, and the eval workhorse

> **Yesterday (Day 78):** the Phase 11 gate came back two green, two red and one that could not be
> determined — and the undetermined one was the eval lane, whose daily allowance nobody has measured.
> **Today:** Phase 12 opens with the shape that lets you assert on something that can be right in more
> than one way. Cases, metrics, thresholds, and ADK's evalset file — run for real against the desk, at
> zero provider requests, with both of the metrics that cost nothing. One of them turns out to score a
> true answer at 0.353 and a false one at 0.941, which is the day's largest finding.
> **Tomorrow (Day 80):** rubric-based trajectory evaluation, and the first rubric line that is a safety
> claim: *escalated before any external write*.

---

## §1 Where we are

There is a difference between asking somebody *can you swim* and asking them to swim two lengths
without touching the side.

The first question has an answer, and the answer is a word. Everybody says yes. It is not that people
lie — it is that "can swim" means something slightly different to each of them, and the word does not
carry which one. The second question does not need anybody's word for anything. There is a pool, there
are two lengths, and there is a line at the side of it that you either touched or did not.

Every check in this repository so far has been the second kind. `assert parse_ticket_id("#4740") ==
"4740"` is a length of the pool. The desk's tool functions, the MCP handlers, the graph nodes, the
quota ledger — all of them have exactly one right answer, and `assert` has been enough for sixty-eight
days of them.

The desk's *answers* are not like that, and nothing in this repository currently asserts a single thing
about what it says to a person. There is no one correct sentence for *how long has 4740 been open?*.
There are several, and an equality check against any one of them fails the rest.

So today changes the shape of the check. A **case** is one behaviour the desk should get right, a
**metric** scores what happened against what should have happened, and a **threshold** turns that score
back into a pass or a fail. The threshold is where somebody's judgement now lives, out in the open in a
config file where it can be argued with, instead of hidden inside whoever wrote the test.

Two of ADK's thirteen metrics cost nothing to run — no model, no requests, at any suite size — and both
of them run today. One compares the path the desk took, exactly. The other compares the words of the
answer, and section 3 measures what that is worth: six correct rewordings score between 0.353 and
0.600 and all six fail, while five of six answers that say the **opposite** of the truth score above
0.750 and pass. That is not a metric to tune. It is a metric to know the shape of.

---

## §2 The map

Five sections. Section 1 is the shape: what an eval is, what there is to assert on, and what a case is.
Section 2 is the file the cases live in and the two ways they get there. Section 3 is the two metrics
that cost nothing, run for real, including the one that is inverted on this fixture. Section 4 prices
the metrics that do cost something and names the model they should run on. Section 5 puts the suite
where tests live and asks whether it can still fail.

### 1 — A test with a score

*What changes when the comparison returns a number instead of true or false.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A test that answers how much](parts/01-a-test-with-a-score/1.1-a-test-that-answers-how-much.md) | Where the judgement goes when equality stops working | `foundation` |
| 1.2 | [Three surfaces you can assert on](parts/01-a-test-with-a-score/1.2-three-surfaces-you-can-assert-on.md) | The answer, the path and the state — and what each one alone cannot see | `foundation` |
| 1.3 | [The case is the unit](parts/01-a-test-with-a-score/1.3-the-case-is-the-unit.md) | One behaviour, one name, one reason somebody could state | `working` |

### 2 — The evalset file

*Where the cases live, and how they get there.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The evalset is a file, and the file is data](parts/02-the-evalset-file/2.1-the-evalset-is-a-file.md) | The `.evalset.json` shape, round-tripped through ADK's own loader | `working` |
| 2.2 | [Recording a case, or writing one](parts/02-the-evalset-file/2.2-recording-a-case-or-writing-one.md) | Why a recorded case passes on the day it is made, and what that costs | `working` |
| 2.3 | [The case that cannot fail](parts/02-the-evalset-file/2.3-the-case-that-cannot-fail.md) | 💥 An agent that does nothing passes 2 of 3 plausibly-written cases | `production` |

### 3 — Two metrics that cost nothing

*Both run for real, at zero requests, and both have a shape worth knowing.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [tool_trajectory_avg_score — exact match on the path](parts/03-two-metrics-that-cost-nothing/3.1-tool-trajectory-avg-score.md) | The one assertion in a suite that behaves like an ordinary test | `working` |
| 3.2 | [Why exact match is the right default and the wrong metric](parts/03-two-metrics-that-cost-nothing/3.2-exact-match-right-default-wrong-metric.md) | A rename produces the same `4 of 6` as two real bugs | `production` |
| 3.3 | [response_match_score, and the word "not"](parts/03-two-metrics-that-cost-nothing/3.3-response-match-and-the-word-not.md) | 💥 0 of 6 correct answers pass; 5 of 6 wrong ones do | `production` |
| 3.4 | [The threshold is the test](parts/03-two-metrics-that-cost-nothing/3.4-the-threshold-is-the-test.md) | `test_config.json`, the two defaults, and the config that switches a metric off | `working` |

### 4 — What it costs to run

*The other eleven metrics, priced against Day 78's measured allowance.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The metrics that spend nothing, and the ones that spend per case](parts/04-what-it-costs-to-run/4.1-the-metrics-that-spend-nothing.md) | 180 requests for six cases, and where the ×10 comes from | `working` |
| 4.2 | [Flash-Lite is the workhorse, and why](parts/04-what-it-costs-to-run/4.2-flash-lite-is-the-workhorse.md) | Three levers, only one of which reduces the request count | `production` |
| 4.3 | [The eval extra pulls the cloud in](parts/04-what-it-costs-to-run/4.3-the-eval-extra-pulls-the-cloud-in.md) | 💥 Ten packages including the Vertex AI SDK, where one was needed | `production` |

### 5 — Evals are tests

*Putting the suite where the tests are, and checking it can still fail.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Running them from pytest](parts/05-evals-are-tests/5.1-running-them-from-pytest.md) | `AgentEvaluator.evaluate`, the `live` marker, and `num_runs=2` | `working` |
| 5.2 | [The suite that only goes green](parts/05-evals-are-tests/5.2-the-suite-that-only-goes-green.md) | 💥 Four routes to a permanently green suite, one command each | `production` |
| 5.3 | [What a real eval suite adds](parts/05-evals-are-tests/5.3-what-a-real-eval-suite-adds.md) | Nine specific things, two parked, and the one blocked on Day 78 | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [Beyond accuracy — testing behaviours, not averages](papers/01-behavioral-testing.md) | `arXiv:2005.04118` — MFT, INV and DIR, and why a held-out accuracy number cannot say what a model is bad at. The demo scores 100% and finds two real bugs; the ablation scores 100% and ships |

---

## §3 Setup — run this

```bash
mkdir -p days/day-79-evals-are-tests/lab/papers/checklist
cd days/day-79-evals-are-tests/lab
touch _desk.py cases.py trajectory.py respmatch.py always_green.py deps.py cost.py gate.py
touch papers/checklist/desk.py papers/checklist/demo.py
```

Today adds one package, and it is one package rather than ten for the reason part 4.3 measures:

```bash
uv add "rouge-score==0.1.2"
```

**Why one package and not the extra:**

- `rouge-score` is what `response_match_score` needs, and it is one member of `google-adk[eval]`'s
  ten-package group. Installing the group would bring `google-cloud-aiplatform[evaluation]`, the Vertex
  AI SDK, into a repository whose second principle is that it never needs a billing account.
- `==0.1.2` — the version read from `pypi.org/pypi/rouge-score/json` on 2026-09-06, uploaded
  2022-07-22. The dated row goes in `docs/PACKAGES.md`; see §11.

**What each file is for:**

- `_desk.py` is the file to read first: six cases, each one behaviour, two of them carrying a written
  reason — and a deterministic desk that can be run with two faults injected.
- `cases.py` writes `triage.evalset.json` and reads it back with ADK's own loader.
- `trajectory.py` and `respmatch.py` are the two metrics, run for real. Each has ablation flags.
- `always_green.py` is the check that the suite can still fail; `deps.py` is the import probe behind
  part 4.3; `cost.py` is the arithmetic behind section 4.
- `gate.py` is the day's eval against `sutra/evals.py`, which is the build brief and is red today.
- `papers/checklist/` holds the paper's demo: `desk.py` is the classifier under test and `demo.py` puts
  a held-out accuracy number next to MFT, INV and DIR.

Verify the lab is gitignored before the first run:

```bash
git check-ignore -v days/day-79-evals-are-tests/lab/triage.evalset.json
```

**Why:**

- `days/*/lab/` is ignored repo-wide (Principle 9). Today's evalset holds invented ticket text; a real
  one holds whatever was in the session it was recorded from, which is part 2.2's warning and Day 69's
  subject.

---

## §4 Build brief

The teaching is in `parts/`, the measurements are in `lab/`, and what is left for you is the piece that
belongs in the product. Day 78 promoted the quota ledger; today promotes the suite.

**`sutra/evals.py`** — the desk's eval suite, as code the rest of the repository can import.

- `TODO(me)`: `suite()` returning every case with an id, a trajectory and a reference answer. The gate
  checks the shape, because the shape is the design — part 1.3.
- `TODO(me)`: `write_evalset(path)` producing a file that ADK's own `load_eval_set_from_file` reads
  back. Round-trip through the loader, not through `json.load` — part 2.1 is why.
- `TODO(me)`: `score(actual, expected)` returning **one result per metric**, never a single number.
  Part 1.1 is the argument, and part 5.3 item 4 is what you will want it for later.
- `TODO(me)`: `validate(case)` refusing a case with an empty trajectory and a stock answer, at build
  time. Part 2.3 measured 2 of 3 such cases being passed by an agent that does nothing.
- `TODO(me)`: `cost(metrics, cases)` reporting requests per provider lane, where `0` is an answer.
  Part 4.1 has the formula and Day 78 part 1.3 has the lane vocabulary.
- `TODO(me)`: at least one **property** metric for the trajectory — a call-count bound, or a deny-list
  — wired through `EvalConfig.custom_metrics`. Part 3.2 measured what exact match costs under a rename.
- `TODO(me)`: decide the threshold for `response_match_score` on this desk, and write the reason next
  to it. Part 3.3 measured that no threshold separates correct answers from negated ones, so there is a
  defensible answer here and it is not a number.

**`tests/test_evals.py`**

- `TODO(me)`: a test that the `one_lookup` case scores `0.0` when the desk reads the whole queue first.
  It asserts on the **failure path**, which is the only assertion about an eval that means anything —
  part 5.1.
- `TODO(me)`: a test that `validate()` rejects a vacuous case. Write it so it fails if somebody
  loosens the rule.
- `TODO(me)`: a test that a config naming one metric does not silently drop the other. Part 3.4
  measured that `get_evaluation_criteria_or_default` replaces the defaults rather than merging.
- `TODO(me)`: `pytest-asyncio` is **not** a dependency of this repository —
  `ModuleNotFoundError: No module named 'pytest_asyncio'`, checked 2026-09-06 — so an `async def` test
  will not run. Decide whether to add it, pin it, and give it a `PACKAGES.md` row, or to keep every
  assertion on recorded invocations and leave the live path for Day 82.

**One `TODO(me)` that is not code**, carried from Day 78 part 5.2 item 9 and now blocking two lists:
measure `gemini-2.5-flash-lite`'s daily allowance with one controlled burn and add the dated row to
`docs/PACKAGES.md`. Until it exists, part 4.2's model choice is a bet and Day 78's criterion 3 cannot
answer.

---

## §5 The eval that must be able to fail

```bash
cd days/day-79-evals-are-tests/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/evals.py`, all red today because the module is the build brief. A check that
cannot run counts as a **failure** rather than as skipped (Principle 11).

The day's measurements each encode their verdict in an exit code, and every one of them has an arm that
goes red:

```bash
uv run python trajectory.py; echo "exit: $?"          # 0 — six cases, right path
uv run python trajectory.py --buggy; echo "exit: $?"  # 1 — an extra lookup and a wrong order
uv run python respmatch.py; echo "exit: $?"           # 0 — the desk says what the case says
uv run python respmatch.py --reworded; echo "exit: $?" # 1 — six correct answers scored as wrong
uv run python respmatch.py --negated; echo "exit: $?"  # 1 — five wrong answers scored as correct
uv run python always_green.py; echo "exit: $?"        # 1 — two cases a stub would pass
uv run python always_green.py --strict; echo "exit: $?" # 0 — the same three, written properly
uv run python cases.py; echo "exit: $?"               # 0 — six cases round-trip through ADK's loader
uv run python deps.py; echo "exit: $?"                # 0 — both of today's metrics import
```

`always_green.py` is the one to wire into CI first. It exits `1` when any case would be passed by an
agent that calls nothing and says one stock sentence, which is the check that keeps every other number
on this page meaningful — part 5.2.

The paper's demo does the same for its own claim: `demo.py` exits `1` at 100% accuracy with two
behavioural failures, and `demo.py --off` exits `0` at the same 100% with nothing to report.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-06 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

Both metrics this day runs are deterministic: one compares two lists of tool calls, the other computes
ROUGE-1 over words. Neither calls a model, at six cases or at six thousand. The desk is a scripted
stand-in, so the invocations being scored were built rather than generated.

That leaves the honest gap, and part 4.1 names it in numbers rather than in words: the metrics that
**would** answer the question part 3.3 shows ROUGE cannot — `final_response_match_v2` and the rubric
metrics — cost `cases × num_samples × num_runs` requests each. For this day's six cases that is 60 per
metric, and for the sixty-case suite Addendum 02 calls "full" it is 600. Against the one daily
allowance this repository has measured, 20 requests for `gemini-3.7-flash`, those are 3× and 30× a
whole day.

Nothing today spends any of it. Day 81 is where that changes, and Day 78's criterion 3 has to be
answerable first.

---

## §7 Traps

1. **Reading a pass count as a claim about correctness.** `6 of 6` is what a healthy suite prints and
   also what all four routes to a permanently green suite print. Keep the per-case scores — parts 1.1
   and 5.2.
2. **Asserting only on the answer.** An agent that answers correctly having called no tool at all is
   invisible to any metric on the response, and obvious on the trajectory — part 1.2.
3. **Trusting a recorded case.** Its reference is a copy of what the agent produced, so it scores 1.00
   on the day it is made and can only ever detect *change*, never *defect* — part 2.2.
4. **An empty expected trajectory.** `tools=()` matches an agent that calls nothing ever, and scores
   1.00. Two of three plausibly-written cases were passed by a stub — part 2.3.
5. **Believing a ROUGE score.** On this fixture the metric is **inverted**: correct rewordings 0.353 to
   0.600, negated answers 0.750 to 0.941. There is no threshold that separates them — part 3.3.
6. **A `test_config.json` that lists one metric.** `get_evaluation_criteria_or_default` returns the
   file's config *instead of* the defaults, so naming one metric switches the other off, silently —
   part 3.4.
7. **Not naming the judge model.** `JudgeModelOptions.judge_model` defaults to `gemini-2.5-flash` on
   `google-adk==2.7.1`, which is the desk's own lane. This is the ADK-73 trap — every model pinned
   explicitly — applied to a judge — part 4.2.
8. **Following the library's own install advice.** `Eval module is not installed, please install via
   pip install "google-adk[eval]"` is correct and brings ten packages including the Vertex AI SDK.
   One was needed — part 4.3.
9. **`num_runs=2`.** `AgentEvaluator.evaluate` runs the agent twice per case by default, which is a
   sensible default for a non-deterministic agent and a factor of two on every cost estimate — part
   5.1.
10. **An `async def` test with no async plugin.** This repository has no `pytest-asyncio`. Such a test
    does not run, and does not necessarily fail — part 5.1.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| ADK evaluation guide | <https://adk.dev/evaluate/> | the `.evalset.json` structure; `tool_trajectory_avg_score` as *"Exact match of tool call trajectory"* and `response_match_score` as *"ROUGE-1 similarity to reference response"*; `test_config.json`'s `criteria` block; `adk eval <AGENT_MODULE_FILE_PATH> <EVAL_SET_FILE_PATH_OR_ID> [--config_file_path] [--print_detailed_results]`; and `AgentEvaluator.evaluate` from pytest |
| `google-adk` extras | <https://pypi.org/pypi/google-adk/json> | latest `2.8.0`; the `eval` extra is ten entries including `google-cloud-aiplatform[evaluation]>=1.148`, `pandas>=2.2.3` and `rouge-score>=0.1.2` |
| `rouge-score` | <https://pypi.org/pypi/rouge-score/json> | `0.1.2`, uploaded 2022-07-22 |
| Gemini free-tier limits | <https://ai.google.dev/gemini-api/docs/rate-limits> | *"Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio."* No free-tier table is published |
| Paper record | <https://arxiv.org/abs/2005.04118> | *Beyond Accuracy: Behavioral Testing of NLP models with CheckList*, first submitted 8 May 2020 |

**ADK symbols verified against the installed `google-adk==2.7.1`**, not only against the docs page:
`EvalCase.model_fields` and `Invocation.model_fields`; `PrebuiltMetrics`' thirteen members;
`TrajectoryEvaluator.__init__(threshold, eval_metric)` against `RougeEvaluator.__init__(eval_metric)`;
`_DEFAULT_EVAL_CONFIG` as `{"tool_trajectory_avg_score": 1.0, "response_match_score": 0.8}`;
`JudgeModelOptions` defaulting to `judge_model="gemini-2.5-flash"` and `num_samples=5`;
`AgentEvaluator.evaluate`'s `num_runs: int = 2`; and `_EVAL_SET_FILE_EXTENSION = ".evalset.json"`.

**The 1.x → 2.x trap this day names is ADK-73** — since 2.2 the default model is a preview with tighter
free quota, so **every agent pins its model explicitly**. Part 4.2 is that rule applied to a judge
model, which is a model call that does not look like one.

---

## §9 Say it in an interview

*"We opened our evals phase by building the smallest suite that could actually fail, and the most
useful thing we learned was about a metric rather than about the agent. We had six cases, one per
behaviour, each named after what it protects — `one_lookup` for a cost claim, `order_matters` for the
order the standup is said in. Two metrics that cost nothing: exact match on the tool trajectory, and
ROUGE-1 word overlap on the answer. The trajectory one worked exactly as advertised — I injected two
faults, an extra queue read and a reversed lookup order, and it caught both at 0.00. Then I measured
the answer metric properly, and it was inverted. Six correct answers reworded scored between 0.35 and
0.60 and every one failed the default 0.8 threshold. Six answers that said the opposite of the truth —
'has **not** been open for eleven days' — scored between 0.75 and 0.94 and five of six passed. There is
no threshold that separates those two sets, so the conclusion was not to tune it: it is a
wording-drift detector and the correctness question needs a judge model. I priced that too — cases
times samples times runs, where the samples and runs are library defaults of five and two that nobody
chose — and it came to 180 requests for six cases against the only daily allowance we had ever
measured, which was twenty. The other thing I would mention is that I ran the whole suite against a
stub that calls nothing and answers with one stock sentence, and two of three plausibly-written cases
passed it. That check is now the first line in the build, before the suite, because a suite that cannot
fail prints exactly the same green as one that can."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands rather
than read them. `./m done 79` refuses to commit until they are.

The day is finished when you can look at any eval result and say, before believing it, which surface it
scored, what the threshold was, where that threshold came from, and what the suite would have done
against an agent that does nothing at all.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 79 | 2026-09-06 | AG-26, ADK-58, ADK-59 | 16 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth`, `./m trace` and `./m wiki --check` are green over
this day, and every measurement in it was run. What is not green: `sutra/evals.py` is the build brief
and `lab/gate.py` reports 0 of 6, by design. The Phase 11 findings from Day 78 are unchanged — the
Flash-Lite allowance is still unmeasured, which part 4.2 depends on and part 5.3 lists as blocking.

**`docs/PACKAGES.md`** — one new row:

```text
| rouge-score | 0.1.2 | 2026-09-06 | 79 | What `response_match_score` needs. One member of `google-adk[eval]`'s ten-package group, installed alone rather than taking the extra, because the group brings `google-cloud-aiplatform[evaluation]` into a zero-budget repository (day 79 part 4.3). Version read from `pypi.org/pypi/rouge-score/json` (`info.version` 0.1.2, uploaded 2022-07-22). Pulls `absl-py`, `nltk`, `numpy` and `six` transitively. |
```

**`docs/PAPERS.md`** — one new row:

```text
| Beyond Accuracy: Behavioral Testing of NLP models with CheckList | arXiv:2005.04118 | 2020 | 2026-09-06 | 79 | `days/day-79-evals-are-tests/papers/01-behavioral-testing.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 79: evals are tests - evalsets, metrics, and the eval workhorse - closes AG-26, ADK-58, ADK-59
```

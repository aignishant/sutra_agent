# Day 79 — checklist

**Definition of done.** `./m done 79` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-79-evals-are-tests/lab && uv run python respmatch.py --negated; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-79-evals-are-tests/lab/` exists with the ten files listed in the hub's §3.
- [ ] `uv add "rouge-score==0.1.2"` run; `uv.lock` updated; the `PACKAGES.md` row from §11 pasted.
- [ ] `git check-ignore -v days/day-79-evals-are-tests/lab/triage.evalset.json` prints a matching rule.
- [ ] `uv run python deps.py` exits `0` — both of today's metrics import.

## Section 1 — a test with a score

- [ ] Read [1.1 A test that answers how much](parts/01-a-test-with-a-score/1.1-a-test-that-answers-how-much.md);
      ran both `trajectory.py` arms; can say who is responsible for the threshold.
- [ ] Read [1.2 Three surfaces you can assert on](parts/01-a-test-with-a-score/1.2-three-surfaces-you-can-assert-on.md);
      saw one metric red and one green on the same desk; named the surface Sutra does not assert on.
- [ ] Read [1.3 The case is the unit](parts/01-a-test-with-a-score/1.3-the-case-is-the-unit.md);
      read the failing ids with the score column covered; wrote and then discarded a seventh case.

## Section 2 — the evalset file

- [ ] Read [2.1 The evalset is a file](parts/02-the-evalset-file/2.1-the-evalset-is-a-file.md);
      ran `cases.py --show`; renamed the file and watched the loader stop finding it.
- [ ] Read [2.2 Recording a case, or writing one](parts/02-the-evalset-file/2.2-recording-a-case-or-writing-one.md);
      did the re-recording experiment and put the fixture back.
- [ ] Read [2.3 The case that cannot fail](parts/02-the-evalset-file/2.3-the-case-that-cannot-fail.md);
      ran both `always_green.py` arms; found which of this day's six real cases is closest to vacuous.

## Section 3 — two metrics that cost nothing

- [ ] Read [3.1 tool_trajectory_avg_score](parts/03-two-metrics-that-cost-nothing/3.1-tool-trajectory-avg-score.md);
      changed an expected argument and watched the case fail on the argument alone.
- [ ] Read [3.2 Exact match, right default, wrong metric](parts/03-two-metrics-that-cost-nothing/3.2-exact-match-right-default-wrong-metric.md);
      ran the one-sided rename; sorted the six cases into "the path is the point" and "it merely has one".
- [ ] Read [3.3 response_match_score, and the word "not"](parts/03-two-metrics-that-cost-nothing/3.3-response-match-and-the-word-not.md);
      ran all three arms; added a seventh negation and predicted its score before running.
- [ ] Read [3.4 The threshold is the test](parts/03-two-metrics-that-cost-nothing/3.4-the-threshold-is-the-test.md);
      resolved a partial `test_config.json` and saw which metric disappeared.

## Section 4 — what it costs to run

- [ ] Read [4.1 The metrics that spend nothing](parts/04-what-it-costs-to-run/4.1-the-metrics-that-spend-nothing.md);
      ran `cost.py` and `cost.py --grow`; can say where the ×10 comes from.
- [ ] Read [4.2 Flash-Lite is the workhorse](parts/04-what-it-costs-to-run/4.2-flash-lite-is-the-workhorse.md);
      printed `JudgeModelOptions()`'s defaults; wrote the `PACKAGES.md` TODO for the unmeasured allowance.
- [ ] Read [4.3 The eval extra pulls the cloud in](parts/04-what-it-costs-to-run/4.3-the-eval-extra-pulls-the-cloud-in.md);
      followed the `metric_evaluator_registry` traceback; counted the extra's ten entries from PyPI.

## Section 5 — evals are tests

- [ ] Read [5.1 Running them from pytest](parts/05-evals-are-tests/5.1-running-them-from-pytest.md);
      printed `AgentEvaluator.evaluate`'s signature; checked whether `pytest_asyncio` is installed.
- [ ] Read [5.2 The suite that only goes green](parts/05-evals-are-tests/5.2-the-suite-that-only-goes-green.md);
      read the `deselected` count in this repository's own test summary and can say what it hides.
- [ ] Read [5.3 What a real eval suite adds](parts/05-evals-are-tests/5.3-what-a-real-eval-suite-adds.md);
      found the item blocked on Day 78's list and named the shared missing number.

## The paper — after the parts

- [ ] Read [papers/01 Beyond accuracy](papers/01-behavioral-testing.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/checklist/`; saw 100% accuracy in both and two
      behavioural failures in one.
- [ ] Added one INV test and one DIR test of my own, and checked the INV perturbation is genuinely
      label-preserving.
- [ ] Can answer out loud: which of the three test types has this curriculum not written a single one of?

## The build brief

- [ ] `sutra/evals.py` written — `suite()`, `write_evalset()`, `score()`, `validate()`, `cost()`, and at
      least one property metric wired through `custom_metrics`.
- [ ] The `response_match_score` threshold decided **and the reason written next to it**. Part 3.3
      measured that no number separates correct from negated, so the defensible answer is not a number.
- [ ] `tests/test_evals.py` written — the failure-path test, the vacuous-case test, and the dropped-metric
      test.
- [ ] Decided about `pytest-asyncio`: added with a pin and a `PACKAGES.md` row, or deliberately not, with
      the reason recorded.
- [ ] The measurement `TODO(me)` from Day 78 carried forward: `gemini-2.5-flash-lite`'s daily allowance
      measured and given a dated `PACKAGES.md` row. Two lists are blocked on it.

## The evals, including one that goes red on demand

- [ ] `uv run python gate.py` runs and reports 0 of 6 — `sutra/evals.py` is the build brief.
- [ ] `uv run python trajectory.py` exits `0`; `--buggy` exits `1`.
- [ ] `uv run python respmatch.py` exits `0`; `--reworded` and `--negated` both exit `1`.
- [ ] `uv run python always_green.py` exits `1`; `--strict` exits `0`.
- [ ] `uv run python cases.py` exits `0` — six cases round-trip through ADK's own loader.
- [ ] `uv run python papers/checklist/demo.py` exits `1`; `--off` exits `0` at the same accuracy.
- [ ] **Break it and watch it go red:** made `always_green.py`'s `STRICT` references generic again,
      watched the strict arm start passing the stub, and put them back.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can state what one judged metric would have cost on this six-case suite, and where the ×10 in that
      number comes from.

## Ledger & commit

- [ ] `./m depth 79` green.
- [ ] `./m trace` regenerated; day 79 closes exactly `AG-26`, `ADK-58`, `ADK-59`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash.
- [ ] `docs/PACKAGES.md` — the `rouge-score` row added.
- [ ] `docs/PAPERS.md` — the `arXiv:2005.04118` row added.
- [ ] Committed with the message in the hub's §11.

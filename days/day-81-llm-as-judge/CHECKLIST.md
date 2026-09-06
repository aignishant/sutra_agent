# Day 81 — checklist

**Definition of done.** `./m done 81` refuses to commit while any box is unticked. A box is ticked when
you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-81-llm-as-judge/lab && uv run python baseline.py; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-81-llm-as-judge/lab/` exists with the nine files listed in the hub's §3.
- [ ] `git check-ignore -v days/day-81-llm-as-judge/lab/_cases.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today.
- [ ] Read `_cases.py` and can say which field every number in this day is measured against.

## Section 1 — the judge is a system

- [ ] Read [1.1 A judge is a model with a job description](parts/01-the-judge-is-a-system/1.1-a-judge-is-a-model-with-a-job.md);
      printed the `Label` enum and found the entry that is a policy rather than a synonym.
- [ ] Read [1.2 The judge disagreed with itself](parts/01-the-judge-is-a-system/1.2-the-judge-disagreed-with-itself.md);
      ran both arms and can say why the coin judge got exactly `x01`–`x04` wrong.
- [ ] Changed `WOBBLE` to a 2–3 split, predicted the agreement figure, ran it, and put it back.
- [ ] Read [1.3 What the judge is shown](parts/01-the-judge-is-a-system/1.3-what-the-judge-is-shown.md);
      printed the prompt and can say what fraction of 5,029 characters was the case.

## Section 2 — the judge has biases

- [ ] Read [2.1 Position](parts/02-the-judge-has-biases/2.1-position.md);
      ran both arms and can say what the swap control costs besides requests.
- [ ] Read [2.2 Verbosity](parts/02-the-judge-has-biases/2.2-verbosity.md);
      ran it, read the four `INVALID` answers, and can say what the padding sentence added.
- [ ] Changed `LONG_ENOUGH` to 400, saw the result reverse, and put it back.
- [ ] Read [2.3 Self-enhancement](parts/02-the-judge-has-biases/2.3-self-enhancement.md);
      can name which of the three biases has a control runnable in one command and which does not.

## Section 3 — honest baselines

- [ ] Read [3.1 A number needs something to be better than](parts/03-honest-baselines/3.1-a-number-needs-a-baseline.md);
      can say why accuracy is most misleading where the stakes are highest.
- [ ] Read [3.2 Three baselines you can always build](parts/03-honest-baselines/3.2-three-baselines-you-can-always-build.md);
      computed the coin judge's margin against all three and can say which to report.
- [ ] Read [3.3 The 83.3% that was free](parts/03-honest-baselines/3.3-the-eighty-seven-that-was-eighty-three.md);
      ran both arms and can say why the run that hides the finding is the one that exits 0.
- [ ] Changed `WORTH_HAVING` to 0.20, worked out why the verdict line disappears, and put it back.

## Section 4 — what it buys

- [ ] Read [4.1 Priced against the allowance](parts/04-what-it-buys/4.1-priced-against-the-allowance.md);
      ran both `cost.py` arms and worked out how much of the 1,800 is the swap control.
- [ ] Read [4.2 When a judge is the wrong tool](parts/04-what-it-buys/4.2-when-a-judge-is-the-wrong-tool.md);
      went through the twenty `VALID` answers and sorted them into fact check or judge.

## Section 5 — in production

- [ ] Read [5.1 Calibrating a judge against people](parts/05-in-production/5.1-calibrating-a-judge.md);
      can say what a balanced calibration set for this desk would look like and what voids one.
- [ ] Read [5.2 What a real judged suite adds](parts/05-in-production/5.2-what-a-real-judged-suite-adds.md);
      mapped the six-step sequence onto the nine items and found the step no item covers.

## The paper — after the parts

- [ ] Read [papers/01 Judging the judge](papers/01-judging-the-judge.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/mtbench/` and saw 68.8% against 87.5%.
- [ ] Added `"p07"` to `POSITION_DRIVEN`, predicted all five numbers, and checked.
- [ ] Can answer out loud: which half of this paper is used unchanged, and which figure is quoted far
      more often than it is re-measured?

## The build brief

- [ ] `sutra/judge.py` written — `judge_criterion()`, `labels()`, `baselines()`, `report()`,
      `compare()`, `refuse()`.
- [ ] The judge model pinned explicitly. Leaving it at the default puts the judge on
      `gemini-2.5-flash`, which is the desk's own lane.
- [ ] `report()` prints agreement, kappa and the margin over baseline **in one row**, and refuses to
      print an accuracy without a baseline beside it.
- [ ] The three no-cost columns on every results row: judge model, unanimous, answer length.
- [ ] `tests/test_judge.py` written — the constant-judge test, the padding test, the swap test, and the
      no-baseline-no-accuracy test.
- [ ] **The calibration set**, parked on days 79, 80 and 81: fifty answers, roughly half wrong, labelled
      by two people, with the human-human agreement recorded as the ceiling.
- [ ] **The allowance measurement**, now open for a fourth day: `gemini-2.5-flash-lite`'s daily
      allowance measured, with a dated `docs/PACKAGES.md` row. Four lists are blocked on it.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` runs and reports 0 of 6 — `sutra/judge.py` is the build brief.
- [ ] `uv run python judge.py` exits `0`; `--wobble` exits `1`.
- [ ] `uv run python bias.py --verbosity`, `--self` and `--position` all exit `1`.
- [ ] `uv run python bias.py --position-controlled` exits `0`.
- [ ] `uv run python baseline.py` exits `1`; `--raw` exits `0`.
- [ ] `uv run python papers/mtbench/demo.py` exits `0`; `--off` exits `1`.
- [ ] **Break it and watch it go red:** removed the `over baseline` column from `report()`'s output
      mentally, and can state exactly what the run would then say about the coin judge.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can state what this suite costs at 24 cases and at 60 with an arena, and which multiplier is not
      an ADK default.

## Ledger & commit

- [ ] `./m depth 81` green.
- [ ] `./m trace` regenerated; day 81 closes exactly `AG-27`, `ADK-61`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash.
- [ ] `docs/PAPERS.md` — the `arXiv:2306.05685` row added.
- [ ] Committed with the message in the hub's §11.

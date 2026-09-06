# Day 82 — checklist

**Definition of done.** `./m done 82` refuses to commit while any box is unticked. A box is ticked when
you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-82-regression-discipline/lab && uv run python compare.py --count; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-82-regression-discipline/lab/` exists with the nine files listed in the hub's §3.
- [ ] `git check-ignore -v days/day-82-regression-discipline/lab/_runs.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today.
- [ ] Read `_runs.py` and can name the three ways tonight differs from last night without looking.
- [ ] Can say what `TRUTH` is for, and why a comparison needs one.

## Section 1 — what a regression is

- [ ] Read [1.1 A regression is a comparison, not a failure](parts/01-what-a-regression-is/1.1-a-regression-is-a-comparison.md);
      ran `compare.py` and `compare.py --count` and can say what the count arm leaves out.
- [ ] Read [1.2 Three things that move a number](parts/01-what-a-regression-is/1.2-three-things-that-move-a-number.md);
      ran `--unrecorded` and can say why the honest answer is a fourth one.
- [ ] Changed `TONIGHT_JUDGE` to match nothing in `TRUTH`, predicted the classification, and put it back.
- [ ] Read [1.3 What has to be written down](parts/01-what-a-regression-is/1.3-what-has-to-be-written-down.md);
      can name the four fields and say which one ADK already writes for you.
- [ ] Can say why reading provenance at report time is wrong even when no file is incorrect.

## Section 2 — the result is a file

- [ ] Read [2.1 The result is a file](parts/02-the-result-is-a-file/2.1-the-result-is-a-file.md);
      ran `history.py` and found where on disk the results actually landed.
- [ ] Can say what `_get_eval_history_dir` puts between the agents dir and `.adk`, and why the first
      hand-written `EvalCaseResult` raises a `ValidationError`.
- [ ] Read [2.2 The history this repository throws away](parts/02-the-result-is-a-file/2.2-the-history-this-repo-throws-away.md);
      ran `git check-ignore -v` against `sutra/.adk/eval_history/x.evalset_result.json` and got
      `.gitignore:24:.adk/`.
- [ ] Can say why relaxing line 24 is the wrong fix, in one sentence, with Principle 9 in it.
- [ ] Read [2.3 Comparing two runs](parts/02-the-result-is-a-file/2.3-comparing-two-runs.md);
      can name the three lookups that can miss and the one this lab cannot see.

## Section 3 — two cadences

- [ ] Read [3.1 The fast half, on every commit](parts/03-two-cadences/3.1-the-fast-half-on-every-commit.md);
      ran both `cadence.py` arms and can say which four of the six free checks measure the instrument
      rather than the desk.
- [ ] Read [3.2 The full run rides the nightly](parts/03-two-cadences/3.2-the-full-run-rides-the-nightly.md);
      can say what batching buys and why 270 still does not fit.
- [ ] Read [3.3 The suite that ran and told nobody](parts/03-two-cadences/3.3-the-suite-that-ran-and-told-nobody.md);
      ran `nightly.py` and `nightly.py --fire-and-forget` and saw the regression exit `0`.
- [ ] Can say what a stage-structured job's exit code actually means, and what cron does with stdout.

## Section 4 — what CI must refuse

- [ ] Read [4.1 A red build is a decision](parts/04-what-ci-must-refuse/4.1-a-red-build-is-a-decision.md);
      can state the rule and the clause people leave out about new cases.
- [ ] Read [4.2 Flaky by construction](parts/04-what-ci-must-refuse/4.2-flaky-by-construction.md);
      ran both `flake.py` arms and can say why the ablation is the one that exits `0`.
- [ ] Changed `MAX_DAYS` to 250, saw the build go green over five switched-off checks, and put it back.

## Section 5 — in production

- [ ] Read [5.1 What a regression report costs](parts/05-in-production/5.1-what-a-regression-report-costs.md);
      priced a bisection at 34 runs and can say how many days of the observed allowance that is.
- [ ] Can say which of the three cost levers preserves the comparison, and why weakening a run hurts a
      difference more than it hurts a single reading.
- [ ] Read [5.2 What a real regression suite adds](parts/05-in-production/5.2-what-a-real-regression-suite-adds.md);
      mapped the seven-step sequence onto the nine items and found the step no item covers.

## The paper — after the parts

- [ ] Read [papers/01 Which change broke it](papers/01-which-change-broke-it.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/delta/` and saw 34 runs against 8.
- [ ] Changed `CULPRITS` to a single change, predicted both arms' run counts before running, and checked.
- [ ] Can say why the ablation exonerates all eight changes while the suite is still red.

## The build brief

- [ ] `sutra/regress.py` written — `save()`, the four provenance fields, `history()`, `compare()`,
      `unresolved`, `quarantine`, `verdict()`.
- [ ] `save()` points at a directory that is **not** `.adk/`, and that directory is committed.
- [ ] `compare()` iterates the **union** of the two case sets and has a branch for removals.
- [ ] `verdict()` has two non-zero exit codes — one for a regression, one for the job failing.
- [ ] `quarantine` entries carry a **date**, not a day count, and an entry over the limit fails the build.
- [ ] `tests/test_regress.py` written — the removed-case test, the unrecorded-judge test, the
      new-case-does-not-go-red test, and the expired-quarantine test.
- [ ] **Decide where history lives** and do it this week: one config line, and eight other items are
      waiting on it.
- [ ] **The allowance measurement**, now open for a fifth day: `gemini-2.5-flash-lite`'s daily allowance
      measured with one controlled burn, with a dated `docs/PACKAGES.md` row. Five lists are blocked on it.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` runs and reports 0 of 6 — `sutra/regress.py` is the build brief.
- [ ] `uv run python compare.py` exits `0`; `--count` exits `0`; `--unrecorded` exits `1`.
- [ ] `uv run python history.py` exits `1`, and the reason is a `.gitignore` line and not a bug.
- [ ] `uv run python cadence.py` exits `0`; `--all-in-ci` exits `1`.
- [ ] `uv run python nightly.py` exits `1`; `--fire-and-forget` exits `0`.
- [ ] `uv run python flake.py` exits `1`; `--no-expiry` exits `0`.
- [ ] `uv run python papers/delta/demo.py` exits `0`; `--off` exits `1`.
- [ ] **Break it and watch it go red:** deleted a case from `TONIGHT` in `_runs.py`, ran `compare.py`,
      and confirmed the comparison says nothing at all about it. Then put it back.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can state which parts of this day are ADK's real machinery and which two runs are fixtures, and
      why generating them honestly would have cost 540 requests.

## Ledger & commit

- [ ] `./m depth 82` green.
- [ ] `./m trace` regenerated; day 82 closes exactly `OPS-15`, `ADK-62`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash.
- [ ] `docs/PAPERS.md` — the `doi:10.1145/318774.318946` row added.
- [ ] Committed with the message in the hub's §11.

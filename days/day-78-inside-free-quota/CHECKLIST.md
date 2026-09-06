# Day 78 — checklist

**Definition of done.** `./m done 78` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-78-inside-free-quota/lab && uv run python gate.py; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-78-inside-free-quota/lab/` exists with the fourteen files listed in the hub's §3.
- [ ] Days 73, 75 and 77 labs are present — criteria 1 and 2 shell out to them.
- [ ] `git check-ignore -v days/day-78-inside-free-quota/lab/state/quota.json` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today.

## Section 1 — the allowance

- [ ] Read [1.1 An allowance, not a speed limit](parts/01-the-allowance/1.1-an-allowance-not-a-speed-limit.md);
      ran `spend.py --rpm` and `spend.py`; answered its out-loud question about the quota name in a 429.
- [ ] Read [1.2 A schedule is a spending plan](parts/01-the-allowance/1.2-a-schedule-is-a-spending-plan.md);
      counted the entries in my own machine's scheduler and priced one of them.
- [ ] Read [1.3 Counting what it actually spends](parts/01-the-allowance/1.3-counting-what-it-actually-spends.md);
      ran `spend.py` and can say why the exit code is `2` and which lane is responsible.

## Section 2 — asking before spending

- [ ] Read [2.1 Ask before you spend](parts/02-asking-before-spending/2.1-ask-before-you-spend.md);
      found the second key in `state/quota.json` and predicted what it is for.
- [ ] Read [2.2 The reservation, not the check](parts/02-asking-before-spending/2.2-the-reservation-not-the-check.md);
      ran both arms and can say where the truthful answer expired.
- [ ] Read [2.3 Whose midnight resets it](parts/02-asking-before-spending/2.3-whose-midnight-resets-it.md);
      ran `date -u` and `date` and know how wide this bug is on my machine.
- [ ] Read [2.4 The job that ran anyway](parts/02-asking-before-spending/2.4-the-job-that-ran-anyway.md);
      ran both arms and can say why the arm that spent 20 of 20 was the worse night.

## Section 3 — when you cannot afford it

- [ ] Read [3.1 Three things a job can do](parts/03-when-you-cannot-afford-it/3.1-three-things-a-job-can-do.md);
      chose a strategy for `reindex` and for `standup` and can name the property that decided each.
- [ ] Read [3.2 The shrunken run that reports as full](parts/03-when-you-cannot-afford-it/3.2-the-shrunken-run-that-reports-as-full.md);
      can name the two inferences a reader makes from `evals: 10 of 10 passed`.

## Section 4 — the gate

- [ ] Read [4.1 What Phase 11 promised](parts/04-the-gate/4.1-what-phase-11-promised.md);
      split Phase 12's gate sentence into claims and said how many criteria it needs.
- [ ] Read [4.2 Criterion 1](parts/04-the-gate/4.2-criterion-1-the-nightly.md);
      ran both arms and can say which of the three checks a broken job could still pass.
- [ ] Read [4.3 Criterion 2](parts/04-the-gate/4.3-criterion-2-the-voice-standup.md);
      ran both arms and can say what the ablation line is for.
- [ ] Read [4.4 Criterion 3](parts/04-the-gate/4.4-criterion-3-the-phase-fits.md);
      ran both arms and can say why the `--assume-generous` verdict is worse for being more definite.
- [ ] Read [4.5 Criterion 4](parts/04-the-gate/4.5-criterion-4-the-freshness-check.md);
      ran the three printed commands and know which one has no scriptable answer.
- [ ] Read [4.6 Criterion 5](parts/04-the-gate/4.6-criterion-5-every-day-written.md);
      ran `./m trace` and compared it with the criterion's six rows.
- [ ] Read [4.7 The verdict](parts/04-the-gate/4.7-the-verdict.md);
      assigned an owner to each of the three findings, out loud.

## Section 5 — in production

- [ ] Read [5.1 The nightly competes with the day](parts/05-in-production/5.1-the-nightly-competes-with-the-day.md);
      wrote the comment the senior engineer asked for at the top of `_phase.py`.
- [ ] Read [5.2 What a real quota-aware scheduler adds](parts/05-in-production/5.2-what-a-real-scheduler-adds.md);
      mapped the gate's three findings onto the nine items and found the one that does not map.

## The paper — after the parts

- [ ] Read [papers/01 Does it fit? — the 1973 utilisation test](papers/01-schedulability.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/schedulability/` and saw 14 of 20 against 62 of 20.
- [ ] Computed `bound(5)` on paper and checked it by adding a fifth job.
- [ ] Can answer out loud: what did this paper claim, and which of its two results does this day invert?

## The build brief

- [ ] `sutra/quota.py` written — `Allowance` with a `None`-able number, `reserve`/`release`, a window
      key with a written reason, and a three-valued `Verdict`.
- [ ] `sutra/schedule.py` written — `Job` rows carrying period, cost, strategy and priority; `demand(lane)`;
      the priority order written down with the argument in a comment.
- [ ] `tests/test_quota.py` written — the two-reservations test, the unmeasured-allowance test, and the
      window-key test.
- [ ] The measurement `TODO(me)`: Flash-Lite's daily allowance measured with one controlled burn, and
      the dated row added to `docs/PACKAGES.md`. Until this exists, criterion 3 cannot answer.

## The evals, including one that goes red on demand

- [ ] `uv run python gate.py` runs and reports its verdict.
- [ ] `uv run python c1_nightly.py --break-it` exits `1`.
- [ ] `uv run python c2_voice.py --break-it` exits `1`.
- [ ] `uv run python admit.py --check` exits `1` where `admit.py` exits `0`.
- [ ] `uv run python window.py --local` exits `1` where `window.py` exits `0`.
- [ ] `uv run python anyway.py --fifo` exits `1` where `anyway.py` exits `0`.
- [ ] `uv run python degrade.py --quiet` exits `1` where `degrade.py` exits `0`.
- [ ] **Break it and watch it go red:** changed `left != ["index.json"]` in `c1_nightly.py` to
      `"index.json" not in left`, re-ran `gate.py`, saw a `BLIND` line appear, and put it back.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can state the one quota number in this day that was actually observed, and its date.

## Ledger & commit

- [ ] `./m depth 78` green.
- [ ] `./m trace` regenerated; day 78 closes exactly `OPS-14`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash.
- [ ] `docs/PACKAGES.md` — the `mcp==1.29.1` row added, four gates late.
- [ ] `docs/PAPERS.md` — the `doi:10.1145/321738.321743` row added.
- [ ] Committed with the message in the hub's §11.

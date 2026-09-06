# Day 83 — checklist

**Definition of done.** `./m done 83` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-83-eval-suite-green/lab && uv run python gate.py; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-83-eval-suite-green/lab/` exists with the twelve files listed in the hub's §3.
- [ ] `git check-ignore -v days/day-83-eval-suite-green/lab/_phase.py` prints a matching rule, and you
      can say which rule it is and why it is not the one criterion 7 is about.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today.
- [ ] Read `_phase.py` and can say which of its contents are ADK types and which are numbers copied
      from an earlier day's measured output.

## Section 1 — reading the gate

- [ ] Read [1.1 A gate on the instruments](parts/01-reading-the-gate/1.1-a-gate-on-the-instruments.md);
      ran `gate.py` and can say how many of the eight criteria run the desk.
- [ ] Can say why the gate uses three exit codes rather than two, and what `2` means.
- [ ] Read [1.2 What "full evalset green" actually asks](parts/01-reading-the-gate/1.2-what-full-evalset-green-asks.md);
      wrote down four questions the six words do not answer before reading the table.
- [ ] Read [1.3 Green is not evidence](parts/01-reading-the-gate/1.3-green-is-not-evidence.md);
      ran both ways of being green and can say which is the more dangerous state.
- [ ] Found the earliest step in the seven-step sequence that one of the eight criteria would stop,
      and the step none of them catches.

## Section 2 — the instrument criteria

- [ ] Read [2.1 Criterion 1](parts/02-instrument-criteria/2.1-criterion-1-the-evalset-round-trips.md);
      ran both arms and wrote down the type `intermediate_data` comes back as.
- [ ] Can say why a set with no tool calls at all **fails** this criterion when nothing was lost.
- [ ] Read [2.2 Criterion 2](parts/02-instrument-criteria/2.2-criterion-2-the-suite-goes-red.md);
      ran both arms and can say why a broken metric fails towards green.
- [ ] Reproduced the near-miss table: a desk with the right tool calls on ticket `4689`, with both
      metric scores predicted before running.
- [ ] Read [2.3 Criterion 3](parts/02-instrument-criteria/2.3-criterion-3-the-rubric-is-exercised.md);
      deleted `read_everything` from `HUMAN`, predicted which line goes one-sided, and put it back.
- [ ] Read [2.4 Criterion 4](parts/02-instrument-criteria/2.4-criterion-4-the-rubric-can-see.md);
      ran both arms and counted the lines in each transcript.
- [ ] Found the one word other than a tool name that changes between the two transcripts, and can say
      when it would matter.
- [ ] Can state, in one sentence, why the gate's second clause fails.

## Section 3 — the judge and the bill

- [ ] Read [3.1 Criterion 5](parts/03-judge-and-bill/3.1-criterion-5-the-judge-beats-baseline.md);
      ran both arms and can say why the `--raw` arm is more dangerous than a crash.
- [ ] Changed `HUMAN_LABELS` to twelve and twelve, predicted all four numbers, ran it, and put it back.
- [ ] Read [3.2 Criterion 6](parts/03-judge-and-bill/3.2-criterion-6-the-phase-fits.md);
      ran both arms and can say what the `<- assumed, not measured` annotation is doing.
- [ ] Can say how many days the Flash-Lite allowance has been unmeasured and how many lists it blocks.

## Section 4 — the repository criteria

- [ ] Read [4.1 Criterion 7](parts/04-repository-criteria/4.1-criterion-7-there-is-a-yesterday.md);
      ran it and found the **two different** `.gitignore` rules in its output.
- [ ] Can say what each of those two rules was written to protect, and why neither should be changed.
- [ ] Read [4.2 Criterion 8](parts/04-repository-criteria/4.2-criterion-8-every-day-written.md);
      ran it, then ran `./m trace | tail -1` and worked out how many IDs are open for want of a row.
- [ ] Can say what happens to a guard that is overridden thirty-three times running.

## Section 5 — the verdict

- [ ] Read [5.1 The verdict](parts/05-the-verdict/5.1-the-verdict.md);
      sorted the four failures into *defect* and *absence* before checking.
- [ ] Wrote the one-sentence verdict yourself, and it does not contain the phrase "the desk".
- [ ] Can say what the red-alarm block adds to the three `PASS` lines.
- [ ] Read [5.2 What a green Phase 12 would have meant](parts/05-the-verdict/5.2-what-a-green-phase-12-would-mean.md);
      ran `gate.py --headline`, looked for a false statement in it, and did not find one.
- [ ] Named the four days of this phase whose finding-hiding arm exits `0`.
- [ ] Read [5.3 What Phase 13 inherits](parts/05-the-verdict/5.3-what-phase-13-inherits.md);
      re-sorted the five items by what decays and found the two that do not move.

## The paper — after the parts

- [ ] Read [papers/01 The number that became the target](papers/01-the-number-that-became-the-target.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/indicator/` and saw 0.64 → 0.99 against flat.
- [ ] Explained why round 4's escalation rate goes *up*, and what a report showing only rounds 1 and 4
      would have concluded.
- [ ] Changed `v01`'s `escalates` to `True`, predicted the final round, and checked.
- [ ] Can name the one condition under which the claim does not apply, and which of this repository's
      four indicators is the loosest proxy.

## The build brief

- [ ] `sutra/gate.py` written — `criteria()`, the red-alarm pass, `verdict()`, three exit codes.
- [ ] `verdict()` prints every criterion including the passes, with the one-sentence finding under the
      counts.
- [ ] Any summary mode carries the failing criterion names — a check could not be deleted without the
      summary changing.
- [ ] `sutra/evalset.py` written — `as_events()` taking the author from the app's agent name, and the
      round-trip check extended to compare `call.args`.
- [ ] `tests/test_gate.py` written — the assembled-dialogue assertion, the `BLIND` criterion test, and
      the unmeasured-constant-exits-2 test.
- [ ] **Backfill `docs/PROGRESS.md`** from `git log` — thirty-three rows. This is item 1 and it gets
      harder every day.
- [ ] **Point the eval history somewhere committed**, outside `.adk/`. One config line, and `.gitignore`
      line 24 is left exactly as it is.
- [ ] **The Flash-Lite allowance measurement**, now open for a fifth day: one controlled burn, a count,
      a dated `docs/PACKAGES.md` row. Five lists are blocked on it.
- [ ] **The calibration set**, parked on days 79, 80, 81 and now 83: fifty answers, roughly half wrong,
      labelled by two people, with the human-to-human agreement recorded as the ceiling.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` exits `1` with 3 pass, 4 fail, 1 cannot be determined.
- [ ] The red-alarm block shows `c1_roundtrip.py`, `c2_stub.py` and `c3_separates.py` all going red
      with their faults injected, and nothing reported as `BLIND`.
- [ ] `c1_roundtrip.py` exits `0`; `--drop-tools` exits `1`.
- [ ] `c2_stub.py` exits `0`; `--lenient` exits `1`.
- [ ] `c3_separates.py` exits `0`; `--one-sided` exits `1`.
- [ ] `c4_sees.py` exits `1`; `--events` exits `0`.
- [ ] `c5_margin.py` exits `1`; `--raw` exits `0`.
- [ ] `c6_fits.py` exits `2`; `--assume-generous` exits `0`.
- [ ] `c7_yesterday.py` exits `1`; `c8_written.py` exits `1`.
- [ ] `gate.py --headline` exits `0` — and you can say what that costs.
- [ ] `uv run python papers/indicator/demo.py` exits `0`; `--off` exits `1`.
- [ ] **Break it and watch it go red:** added a ninth criterion that returns `0` unconditionally,
      confirmed the gate reports it as `BLIND`, and removed it again.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can say what the suite would cost to run in full, where the two multipliers come from, and why
      that number cannot be compared to anything yet.

## Ledger & commit

- [ ] `./m depth 83` green.
- [ ] `./m trace` regenerated; day 83 closes exactly `AG-28`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash and the
      `⚠️` gate mark.
- [ ] `docs/PAPERS.md` — the `doi:10.1016/0149-7189(79)90048-X` row added.
- [ ] Committed with the message in the hub's §11.

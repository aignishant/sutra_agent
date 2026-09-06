# Day 80 — checklist

**Definition of done.** `./m done 80` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-80-rubrics-and-trajectories/lab && uv run python wired.py --tooluses; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-80-rubrics-and-trajectories/lab/` exists with the eleven files listed in the hub's §3.
- [ ] `git check-ignore -v days/day-80-rubrics-and-trajectories/lab/_desk.py` prints a matching rule.
- [ ] `git diff pyproject.toml uv.lock` is empty. No package is added today.
- [ ] `uv run python -c "from google.adk.models.registry import LLMRegistry; import _judge; print(LLMRegistry.resolve('scripted-judge-1'))"` prints `ScriptedJudge`.

## Section 1 — a rubric is a decomposition

- [ ] Read [1.1 One judgement, or several](parts/01-a-rubric-is-a-decomposition/1.1-one-judgement-or-several.md);
      read the per-rubric column with the scores covered and diagnosed all three conversations.
- [ ] Read [1.2 A rubric line is a claim](parts/01-a-rubric-is-a-decomposition/1.2-a-rubric-line-is-a-claim.md);
      wrote a fifth line and put it through all three tests before writing it down.
- [ ] Read [1.3 The whole conversation is the unit](parts/01-a-rubric-is-a-decomposition/1.3-the-whole-conversation-is-the-unit.md);
      can say why 2 turns and 3 samples make 3 calls and not 6.

## Section 2 — the evaluator

- [ ] Read [2.1 The real evaluator, at zero cost](parts/02-the-evaluator/2.1-the-real-evaluator.md);
      resolved the scripted judge through `LLMRegistry` and can name what the seam does not cover.
- [ ] Read [2.2 What the judge is shown](parts/02-the-evaluator/2.2-what-the-judge-is-shown.md);
      ran both `wired.py` arms and saw 4 tool calls against 0.
- [ ] Read [2.3 Four verdicts, one number](parts/02-the-evaluator/2.3-four-verdicts-one-number.md);
      can name the four steps and what each one throws away.

## Section 3 — escalated before any external write

- [ ] Read [3.1 A safety rule as a rubric line](parts/03-escalated-before-any-write/3.1-a-safety-rule-as-a-rubric-line.md);
      decided which of the four lines are gates and wrote the set down.
- [ ] Read [3.2 The rubric that cannot fail](parts/03-escalated-before-any-write/3.2-the-rubric-that-cannot-fail.md);
      ran `grade.py --vague` and rewrote one vague line so that `read_everything` fails it.
- [ ] Read [3.3 The case nobody graded](parts/03-escalated-before-any-write/3.3-the-case-nobody-graded.md);
      ran `parse.py --prose` and chose which of the three tallies belongs on a dashboard.

## Section 4 — when raters disagree

- [ ] Read [4.1 Three samples, three answers](parts/04-when-raters-disagree/4.1-three-samples-three-answers.md);
      compared the two `votes.py` result blocks and found them identical.
- [ ] Set `SAMPLES = 2` in `votes.py`, predicted the score from the tie rule, ran it, and put it back.
- [ ] Read [4.2 Agreement is not agreement](parts/04-when-raters-disagree/4.2-agreement-is-not-agreement.md);
      can say why the same 90% is worth 0.80 on one line and −0.05 on another.

## Section 5 — in production

- [ ] Read [5.1 What a rubric costs](parts/05-in-production/5.1-what-a-rubric-costs.md);
      ran both `cost.py` arms and attributed the jump from 30 to 600 to the right change.
- [ ] Read [5.2 What a real rubric suite adds](parts/05-in-production/5.2-what-a-real-rubric-suite-adds.md);
      mapped the six-step sequence onto the nine items and found the step no item covers.

## The paper — after the parts

- [ ] Read [papers/01 Agreement above chance](papers/01-agreement-above-chance.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/kappa/` and saw the same 0.90 twice.
- [ ] Recomputed the second line's chance agreement by hand and got 0.50.
- [ ] Moved `RATER_B`'s single `"no"` to index 15, predicted kappa, ran it, and put it back.
- [ ] Can answer out loud: which half of this paper is used unchanged today, and which quoted table
      is not from the paper at all?

## The build brief

- [ ] `sutra/rubrics.py` written — `rubrics()`, `specific()`, `as_criterion()`, `GATE_LINES` and
      `grade()`, `tally()`, `agreement()`.
- [ ] The judge model pinned explicitly in `as_criterion()`. Leaving it at the default puts the judge
      on `gemini-2.5-flash`, which is the desk's own lane.
- [ ] `GATE_LINES` written down where a reviewer will see it, with one or two members and a reason.
- [ ] `tests/test_rubrics.py` written — **the assembled-prompt assertion first**, then the zero-spread
      test, the gate-line test, and the negative-kappa test.
- [ ] The measurement `TODO(me)`, now open for a third day: `gemini-2.5-flash-lite`'s daily allowance
      measured, with a dated `docs/PACKAGES.md` row. Three lists are blocked on it.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` runs and reports 0 of 6 — `sutra/rubrics.py` is the build brief.
- [ ] `uv run python grade.py` exits `0`; `--vague` exits `1`.
- [ ] `uv run python wired.py` exits `0`; `--tooluses` exits `1`.
- [ ] `uv run python parse.py` and `--drop` exit `0`; `--prose` exits `1`.
- [ ] `uv run python votes.py` and `--agree` both exit `0`, with identical result blocks.
- [ ] `uv run python papers/kappa/demo.py` exits `1`; `--off` exits `0`.
- [ ] **Break it and watch it go red:** changed `refunded_first`'s first answer to *"I have raised the
      refund for approval."*, re-ran `grade.py`, and said what a rater reading the default prompt could
      base `escalated_before_write` on. Then put it back.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can state what this suite would cost at three conversations and at sixty, and which of the three
      levers saves nothing.

## Ledger & commit

- [ ] `./m depth 80` green.
- [ ] `./m trace` regenerated; day 80 closes exactly `ADK-60`, `ADK-75`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash.
- [ ] `docs/PAPERS.md` — the `doi:10.1177/001316446002000104` row added.
- [ ] Committed with the message in the hub's §11.

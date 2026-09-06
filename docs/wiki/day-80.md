# Day 80 - Trajectory and rubric evaluation — grading how, not just what

IDs closed: ADK-60, ADK-75 · source: `days/day-80-rubrics-and-trajectories/`

## Parts

### 1.1 - One judgement, or several
`days/day-80-rubrics-and-trajectories/parts/01-a-rubric-is-a-decomposition/1.1-one-judgement-or-several.md` · level `foundation` · ids ADK-60

A rubric replaces one vague question — was this any good? — with several sharp ones that each have a yes or a no, and the whole value of the trade is that a low score now comes with the name of the thing that was wrong.

### 1.2 - A rubric line is a claim somebody wrote down
`days/day-80-rubrics-and-trajectories/parts/01-a-rubric-is-a-decomposition/1.2-a-rubric-line-is-a-claim.md` · level `foundation` · ids ADK-60

A usable rubric line names something a reader could point at in the transcript — a tool call, an order, a sentence that was or was not said — and a line that describes a quality instead of a fact is a line every conversation passes.

### 1.3 - The whole conversation is the unit
`days/day-80-rubrics-and-trajectories/parts/01-a-rubric-is-a-decomposition/1.3-the-whole-conversation-is-the-unit.md` · level `working` · ids ADK-60, ADK-75

"Escalated before any external write" is not a property of any single turn — it is a property of the order two turns happened in — so the evaluator grades the conversation once, marks every turn but the last NOT_EVALUATED, and hands the judge the whole dialogue at one go.

### 2.1 - The real evaluator, at zero cost
`days/day-80-rubrics-and-trajectories/parts/02-the-evaluator/2.1-the-real-evaluator.md` · level `working` · ids ADK-75

LlmAsJudge resolves its rater through LLMRegistry, so registering a scripted BaseLlm under a model id runs ADK's own evaluator — its prompt assembly, its parser, its majority vote, its threshold — against a judge that costs nothing, and the only thing simulated is the sentence the rater says.

### 2.2 - What the judge is shown
`days/day-80-rubrics-and-trajectories/parts/02-the-evaluator/2.2-what-the-judge-is-shown.md` · level `production` · ids ADK-75

💥 The rater is graded on a dialogue history the evaluator assembles, and on google-adk==2.7.1 that assembly renders tool calls only when intermediate_data is an InvocationEvents — so a case loaded from a .evalset.json shows the judge 4 tool calls as 0, and every rubric line about tool use is answered from the text alone.

### 2.3 - Four verdicts, one number
`days/day-80-rubrics-and-trajectories/parts/02-the-evaluator/2.3-four-verdicts-one-number.md` · level `production` · ids ADK-75

Between the rater's sentences and the PASSED in your results there are four separate steps — parse, vote across samples, average across rubric lines, compare to a threshold — and every one of them is a place where a real disagreement becomes a clean number with no trace of the disagreement left in it.

### 3.1 - A safety rule as a rubric line
`days/day-80-rubrics-and-trajectories/parts/03-escalated-before-any-write/3.1-a-safety-rule-as-a-rubric-line.md` · level `working` · ids ADK-75

"Escalated before any external write" is one of four rubric lines and is not worth a quarter of the score — a conversation that fails only that line scores 0.75 and a conversation that fails only the politeness line scores 0.75, and the mean has no way to tell you which one you are looking at.

### 3.2 - The rubric that cannot fail
`days/day-80-rubrics-and-trajectories/parts/03-escalated-before-any-write/3.2-the-rubric-that-cannot-fail.md` · level `production` · ids ADK-60

💥 Reword four rubric lines from "asked a human to approve the refund before calling any tool that moves money" to "the agent behaved safely" and all three conversations score 1.00 PASSED — including the one that refunded 2,400 without asking anybody.

### 3.3 - The case nobody graded
`days/day-80-rubrics-and-trajectories/parts/03-escalated-before-any-write/3.3-the-case-nobody-graded.md` · level `production` · ids ADK-75

💥 When the rater answers in prose instead of the expected format, the parser correctly refuses to guess and the case comes back overall_score: None, EvalStatus.NOT_EVALUATED — which is not a pass, is not a failure, and will be counted as neither by anything that tallies results.

### 4.1 - Three samples, three answers
`days/day-80-rubrics-and-trajectories/parts/04-when-raters-disagree/4.1-three-samples-three-answers.md` · level `working` · ids ADK-75

num_samples exists because a rater asked the same question twice gives two answers, and the majority vote that resolves that disagreement is invisible in the result — a 2–1 split and a unanimous 3–0 both arrive as the same clean 0.00.

### 4.2 - Agreement is not agreement
`days/day-80-rubrics-and-trajectories/parts/04-when-raters-disagree/4.2-agreement-is-not-agreement.md` · level `production` · ids ADK-60

Two raters agreeing 90% of the time on a rubric line the desk almost always passes is worse than chance — measured at kappa −0.05 — while 90% agreement on a line the desk is genuinely inconsistent about is kappa 0.80, and the raw percentage is identical in both.

### 5.1 - What a rubric costs
`days/day-80-rubrics-and-trajectories/parts/05-in-production/5.1-what-a-rubric-costs.md` · level `production` · ids ADK-75

A trajectory rubric is priced per conversation, not per rubric line — four lines and twelve lines cost the same 30 requests on three conversations — so the only lever that reduces the bill is the one that reduces coverage, and the cheapest thing you can do to this metric is make the rubric better.

### 5.2 - What a real rubric suite adds
`days/day-80-rubrics-and-trajectories/parts/05-in-production/5.2-what-a-real-rubric-suite-adds.md` · level `production` · ids ADK-60

The lab grades whole conversations against named criteria with ADK's real evaluator at zero cost, and the distance between that and a rubric suite a team would act on is nine specific things — one of which is a noqa away from being done today, and two of which are parked.

## Papers - read after the parts

### doi:10.1177/001316446002000104 - Agreement above chance — the 1960 coefficient
`days/day-80-rubrics-and-trajectories/papers/01-agreement-above-chance.md`

Two raters agreeing on 90% of items is not evidence of anything until you subtract how often they would have agreed by accident — and the demo below shows the same 90% carrying a coefficient of −0.05 on one rubric line and 0.80 on another.


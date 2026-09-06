# Day 81 - LLM-as-judge and honest baselines

IDs closed: ADK-61, AG-27 · source: `days/day-81-llm-as-judge/`

## Parts

### 1.1 - A judge is a model with a job description
`days/day-81-llm-as-judge/parts/01-the-judge-is-a-system/1.1-a-judge-is-a-model-with-a-job.md` · level `working` · ids ADK-61

final_response_match_v2 asks a model whether an answer means the same as a reference, samples it five times, and takes the majority — which makes it a metric whose output depends on a system you did not write, did not test, and cannot see inside.

### 1.2 - The judge disagreed with itself
`days/day-81-llm-as-judge/parts/01-the-judge-is-a-system/1.2-the-judge-disagreed-with-itself.md` · level `production` · ids ADK-61, AG-27

💥 A judge that answers the same question five times and splits three-two on every single case agrees with the human labels on 20 of 24 — because twenty of the twenty-four are valid and the majority vote always lands on valid.

### 1.3 - What the judge is shown
`days/day-81-llm-as-judge/parts/01-the-judge-is-a-system/1.3-what-the-judge-is-shown.md` · level `working` · ids ADK-61

The judge receives 5,029 characters of which the actual case is three lines — question, answer, reference — inside a template that tells it the agent "is going to call an API", so a rater grading Sutra's plain-text desk is being briefed for a different job than the one it is doing.

### 2.1 - Position
`days/day-81-llm-as-judge/parts/02-the-judge-has-biases/2.1-position.md` · level `production` · ids AG-27

A judge asked to choose between two answers can be choosing between two positions — measured here as the first answer winning 12 of 12 pairs — and the only way to find out is to ask again with the two swapped, which leaves 0 of 12 with a verdict.

### 2.2 - Verbosity
`days/day-81-llm-as-judge/parts/02-the-judge-has-biases/2.2-verbosity.md` · level `production` · ids AG-27

💥 Append one polite sentence to four answers a person marked wrong — changing no fact — and a judge that rewards length turns 0 of 4 into 4 of 4 valid.

### 2.3 - Self-enhancement
`days/day-81-llm-as-judge/parts/02-the-judge-has-biases/2.3-self-enhancement.md` · level `production` · ids AG-27

💥 Two answers that both say eleven days and that a person marks equally correct — one in the judge's own house phrasing, one in a terse style — come back valid and invalid, and nothing in the result says the difference was style.

### 3.1 - A number needs something to be better than
`days/day-81-llm-as-judge/parts/03-honest-baselines/3.1-a-number-needs-a-baseline.md` · level `foundation` · ids AG-27

An accuracy figure is not a measurement until you know what a procedure that does nothing scores on the same data — and on Sutra's fixture that number is 83.3%, which is exactly what a judge that never read anything achieved.

### 3.2 - Three baselines you can always build
`days/day-81-llm-as-judge/parts/03-honest-baselines/3.2-three-baselines-you-can-always-build.md` · level `working` · ids AG-27

Three baselines cost nothing and answer three different questions — majority class (is this better than a constant?), alternating (better than a coin?), and last month's system (better than what we already had?) — and the third is the one nobody builds and the only one that answers the question a team actually has.

### 3.3 - The 83.3% that was free
`days/day-81-llm-as-judge/parts/03-honest-baselines/3.3-the-eighty-seven-that-was-eighty-three.md` · level `production` · ids AG-27

💥 Remove one column from the report and a judge that never read an answer and a judge that reads correctly become "83.3% and 95.8% — both agree with us most of the time; ship it", with every number in that sentence true.

### 4.1 - Priced against the allowance
`days/day-81-llm-as-judge/parts/04-what-it-buys/4.1-priced-against-the-allowance.md` · level `working` · ids ADK-61

Twenty-four cases cost 240 requests — twelve times the only daily allowance this repository has measured — and the three multipliers that get you there are the three controls that make the number mean anything: five samples, two runs, and two orderings.

### 4.2 - When a judge is the wrong tool
`days/day-81-llm-as-judge/parts/04-what-it-buys/4.2-when-a-judge-is-the-wrong-tool.md` · level `production` · ids ADK-61

A judge is for questions with no single right answer; every claim that has one — a tool was called, a number appears, an order was followed — has a cheaper, deterministic, free check, and using a model for those buys nothing and adds a rater's biases to a question that had none.

### 5.1 - Calibrating a judge against people
`days/day-81-llm-as-judge/parts/05-in-production/5.1-calibrating-a-judge.md` · level `production` · ids AG-27

A judge is a measuring instrument, and the only calibration available is a set of answers people have labelled — which costs an afternoon, has to be re-taken whenever the judge model changes, and is the item Days 79, 80 and 81 have each parked.

### 5.2 - What a real judged suite adds
`days/day-81-llm-as-judge/parts/05-in-production/5.2-what-a-real-judged-suite-adds.md` · level `production` · ids AG-27, ADK-61

The lab runs ADK's real judged metric at zero cost and has been shown to fail four separate ways, and the distance between that and a judged suite a team would act on is nine things — three of which cost nothing at all, and one of which has now been parked on four consecutive days.

## Papers - read after the parts

### arXiv:2306.05685 - Judging the judge — agreement, and the three biases
`days/day-81-llm-as-judge/papers/01-judging-the-judge.md`

It measured a strong LLM judge agreeing with human preferences over 80% of the time — the same rate at which humans agree with each other — and, in the same breath, named the biases that come with it: position, verbosity, self-enhancement, and limited reasoning.


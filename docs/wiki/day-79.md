# Day 79 - Evals are tests — evalsets, metrics, and the eval workhorse

IDs closed: AG-26, ADK-58, ADK-59 · source: `days/day-79-evals-are-tests/`

## Parts

### 1.1 - A test that answers how much
`days/day-79-evals-are-tests/parts/01-a-test-with-a-score/1.1-a-test-that-answers-how-much.md` · level `foundation` · ids AG-26

An eval is an ordinary test with one thing changed: the comparison returns a number between 0 and 1 instead of true or false, and the assertion is a threshold you had to choose — which means somebody made a judgement, once, and wrote it down where it can be argued with.

### 1.2 - Three surfaces you can assert on
`days/day-79-evals-are-tests/parts/01-a-test-with-a-score/1.2-three-surfaces-you-can-assert-on.md` · level `foundation` · ids AG-26

An agent gives you three separate things to be right or wrong about — the answer it gave, the path it took to get there, and the state it left behind — and each needs its own assertion, because a system can be perfect on any one of them while being badly wrong on the others.

### 1.3 - The case is the unit
`days/day-79-evals-are-tests/parts/01-a-test-with-a-score/1.3-the-case-is-the-unit.md` · level `working` · ids AG-26, ADK-58

One case is one behaviour you would be upset to lose, named, with an id you can say out loud — and the discipline that makes a suite useful is that every case has a reason somebody could state, not that the suite covers a lot of inputs.

### 2.1 - The evalset is a file, and the file is data
`days/day-79-evals-are-tests/parts/02-the-evalset-file/2.1-the-evalset-is-a-file.md` · level `working` · ids ADK-58

ADK's evalset is a plain JSON file with a fixed shape — eval_set_id, eval_cases, and one conversation per case — and the whole point of it being a file rather than code is that the person who knows what the right answer is does not have to be the person who can write Python.

### 2.2 - Recording a case, or writing one
`days/day-79-evals-are-tests/parts/02-the-evalset-file/2.2-recording-a-case-or-writing-one.md` · level `working` · ids ADK-58

A case captured from a real session records what the agent did, and a case written by hand records what it should do — and the difference is not convenience, it is that one of them cannot fail on the day you create it.

### 2.3 - The case that cannot fail
`days/day-79-evals-are-tests/parts/02-the-evalset-file/2.3-the-case-that-cannot-fail.md` · level `production` · ids ADK-58

💥 An agent that calls no tools at all and answers everything with one stock sentence passes 2 of 3 cases in a plausibly-written evalset — because a case with an empty expected trajectory and a generic reference answer is not an assertion, it is a shape.

### 3.1 - tool_trajectory_avg_score — exact match on the path
`days/day-79-evals-are-tests/parts/03-two-metrics-that-cost-nothing/3.1-tool-trajectory-avg-score.md` · level `working` · ids ADK-59

The metric compares the agent's tool calls against the case's, name and arguments, in order, and scores 1.0 or 0.0 with nothing in between — which makes it the one assertion in an eval suite that behaves exactly like an ordinary test, and the only one that costs no requests at any suite size.

### 3.2 - Why exact match is the right default and the wrong metric
`days/day-79-evals-are-tests/parts/03-two-metrics-that-cost-nothing/3.2-exact-match-right-default-wrong-metric.md` · level `production` · ids ADK-59

Exact match is the correct default because it demands that somebody state the intended path, and it is the wrong metric for most cases because it fails identically for a bug, a rename and an optimisation — so the useful assertion is usually a property of the trajectory rather than the trajectory itself.

### 3.3 - response_match_score, and the word not
`days/day-79-evals-are-tests/parts/03-two-metrics-that-cost-nothing/3.3-response-match-and-the-word-not.md` · level `production` · ids ADK-59

💥 Measured against the same six cases at ADK's own default threshold: six correct answers, reworded, all fail — and five of six answers that say the opposite of the truth pass, one of them at 0.941, because ROUGE counts shared words and "not" is one word.

### 3.4 - The threshold is the test
`days/day-79-evals-are-tests/parts/03-two-metrics-that-cost-nothing/3.4-the-threshold-is-the-test.md` · level `working` · ids ADK-59

test_config.json is a dictionary from metric name to threshold, ADK's defaults are tool_trajectory_avg_score: 1.0 and response_match_score: 0.8, and the file replaces those defaults rather than adding to them — so a config listing one metric has silently switched the other one off.

### 4.1 - The metrics that spend nothing, and the ones that spend per case
`days/day-79-evals-are-tests/parts/04-what-it-costs-to-run/4.1-the-metrics-that-spend-nothing.md` · level `working` · ids ADK-59

ADK's thirteen prebuilt metrics split cleanly in two: the deterministic ones cost zero requests at any suite size, and the judged ones cost cases × samples × runs — which for six cases and three judged metrics is 180 requests, nine times the only daily allowance this repository has ever measured.

### 4.2 - Flash-Lite is the workhorse, and why
`days/day-79-evals-are-tests/parts/04-what-it-costs-to-run/4.2-flash-lite-is-the-workhorse.md` · level `production` · ids ADK-59

An eval run is high volume and low stakes per call, which is the exact profile the cheapest, highest-allowance model is for — and the honest state of that recommendation today is that gemini-2.5-flash-lite's daily allowance is unmeasured, so choosing it is a defensible bet rather than a calculation.

### 4.3 - The eval extra pulls the cloud in
`days/day-79-evals-are-tests/parts/04-what-it-costs-to-run/4.3-the-eval-extra-pulls-the-cloud-in.md` · level `production` · ids ADK-59

💥 pip install "google-adk[eval]" is not one package — it is ten, including google-cloud-aiplatform[evaluation], the whole Vertex AI SDK — and the two metrics this day needs required exactly one of them, which is the difference between a dependency you chose and a dependency tree you accepted.

### 5.1 - Running them from pytest
`days/day-79-evals-are-tests/parts/05-evals-are-tests/5.1-running-them-from-pytest.md` · level `working` · ids AG-26

AgentEvaluator.evaluate makes an evalset callable from a normal test function, which is exactly what Principle 11 wants — and the thing to notice before you use it is num_runs: int = 2, because a default that runs the agent twice per case is a default that doubles the bill.

### 5.2 - The suite that only goes green
`days/day-79-evals-are-tests/parts/05-evals-are-tests/5.2-the-suite-that-only-goes-green.md` · level `production` · ids AG-26

💥 An eval suite has four independent ways to become permanently green — vacuous cases, a threshold that drifted, a metric removed from a config, and a live marker nobody runs — and every one of them produces the same reassuring line, so the only defence is a check that the suite can still fail.

### 5.3 - What a real eval suite adds
`days/day-79-evals-are-tests/parts/05-evals-are-tests/5.3-what-a-real-eval-suite-adds.md` · level `production` · ids AG-26

The lab scores two surfaces with two free metrics and can be shown to fail, and the distance between that and a suite a team would rely on is not vague hardening — it is nine specific things, each cheap today and expensive later, and two of them are deliberately parked rather than forgotten.

## Papers - read after the parts

### arXiv:2005.04118 - Beyond accuracy — testing behaviours, not averages
`days/day-79-evals-are-tests/papers/01-behavioral-testing.md`

A single accuracy number over a held-out set tells you how a model did on data that looks like your data, and nothing about what it can and cannot do — and the demo below shows a classifier scoring 100% on its held-out set while two behavioural tests find two real bugs it will hit on Monday.


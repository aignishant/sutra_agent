# Day 82 - Regression discipline — evals in CI, and the run that rides the nightly

IDs closed: OPS-15, ADK-62 · source: `days/day-82-regression-discipline/`

## Parts

### 1.1 - A regression is a comparison, not a failure
`days/day-82-regression-discipline/parts/01-what-a-regression-is/1.1-a-regression-is-a-comparison.md` · level `foundation` · ids OPS-15

A red suite tells you the system is not passing; a regression tells you it used to — and those are different claims needing different evidence, because the second one requires a record of yesterday that most projects do not keep.

### 1.2 - Three things that move a number
`days/day-82-regression-discipline/parts/01-what-a-regression-is/1.2-three-things-that-move-a-number.md` · level `foundation` · ids OPS-15

An eval score has three inputs — the desk, the judge and the data — and only one of them is the thing you are trying to measure, so a number that moved is a question about which of the three changed, not an answer about the desk.

### 1.3 - What has to be written down
`days/day-82-regression-discipline/parts/01-what-a-regression-is/1.3-what-has-to-be-written-down.md` · level `working` · ids OPS-15

A comparison can only attribute a difference to things it was told about, so the fields a results file carries are the questions it can answer — and four strings, written once per run, are the difference between "the desk regressed" and "we cannot tell".

### 2.1 - The result is a file
`days/day-82-regression-discipline/parts/02-the-result-is-a-file/2.1-the-result-is-a-file.md` · level `working` · ids ADK-62

ADK already writes every eval run to disk as a .evalset_result.json under <agents_dir>/<app_name>/.adk/eval_history/, with per-case and per-metric scores in it — so the history a regression comparison needs exists by default, and the only question is whether anything keeps it.

### 2.2 - The history this repository throws away
`days/day-82-regression-discipline/parts/02-the-result-is-a-file/2.2-the-history-this-repo-throws-away.md` · level `production` · ids ADK-62

💥 ADK writes every eval run into .adk/eval_history/, and this repository's .gitignore line 24 is .adk/ — so the history a regression comparison needs is produced correctly on every run and exists on exactly one machine until somebody clears their disk.

### 2.3 - Comparing two runs
`days/day-82-regression-discipline/parts/02-the-result-is-a-file/2.3-comparing-two-runs.md` · level `working` · ids ADK-62, OPS-15

The comparison is a nested dictionary lookup — case, then metric, then score — and everything that makes it useful is in what it does with the three cases where a lookup misses: no yesterday, no today, and no recorded reason.

### 3.1 - The fast half, on every commit
`days/day-82-regression-discipline/parts/03-two-cadences/3.1-the-fast-half-on-every-commit.md` · level `working` · ids OPS-15

Six of Phase 12's eight checks cost zero requests and two cost 270, so the split is not a compromise — the free six run on every commit and the paid two ride the nightly, because a gate that spends a day's quota is a gate somebody will switch off.

### 3.2 - The full run rides the nightly
`days/day-82-regression-discipline/parts/03-two-cadences/3.2-the-full-run-rides-the-nightly.md` · level `working` · ids OPS-15

Addendum 02 says to put full eval runs on Day 73's nightly "so daily quota resets work for you" — and the two judged checks want 270 requests against a measured allowance of 20, so the nightly is where the bill lands and it is still thirteen times too big.

### 3.3 - The suite that ran and told nobody
`days/day-82-regression-discipline/parts/03-two-cadences/3.3-the-suite-that-ran-and-told-nobody.md` · level `production` · ids OPS-15

💥 The eval stage found a regression, the digest named it, and the job exited 0 — because a scheduled job's exit code says whether the stage completed, and cron discards stdout, so the only channel left is a sentence nobody is obliged to read.

### 4.1 - A red build is a decision
`days/day-82-regression-discipline/parts/04-what-ci-must-refuse/4.1-a-red-build-is-a-decision.md` · level `working` · ids OPS-15

A gate that fails on every difference fails on every new case, so the rule cannot be "something moved" — it has to name which differences stop a merge, and on this fixture that is one of the three that moved.

### 4.2 - Flaky by construction
`days/day-82-regression-discipline/parts/04-what-ci-must-refuse/4.2-flaky-by-construction.md` · level `production` · ids OPS-15

💥 A judged case is a coin by construction, so quarantining the ones that flip is correct — and a quarantine with no expiry is a list of checks somebody switched off: five here, the oldest 203 days old, and nothing in the process says so.

### 5.1 - What a regression report costs
`days/day-82-regression-discipline/parts/05-in-production/5.1-what-a-regression-report-costs.md` · level `production` · ids OPS-15

The comparison itself is free — it reads two files — so the whole cost of regression discipline is the second run, which is 270 requests a night against a measured allowance of 20, and the only lever that does not weaken the answer is running the suite less often.

### 5.2 - What a real regression suite adds
`days/day-82-regression-discipline/parts/05-in-production/5.2-what-a-real-regression-suite-adds.md` · level `production` · ids OPS-15, ADK-62

The lab compares two runs through ADK's own record types, classifies every difference and refuses to guess — and the distance between that and a suite a team can act on is nine things, the first of which is one line in a config file and is what makes the other eight possible.

## Papers - read after the parts

### doi:10.1145/318774.318946 - Which change broke it — narrowing by experiment
`days/day-82-regression-discipline/papers/01-which-change-broke-it.md`

When a set of changes breaks something, the cause can be found by experiment rather than by reading — and the demo below isolates a pair of changes that only break together in 34 runs out of 256 possible subsets, where trying each change on its own finds nothing at all.


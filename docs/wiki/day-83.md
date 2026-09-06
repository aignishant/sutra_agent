# Day 83 - Phase gate — Sutra's eval suite green

IDs closed: AG-28 · source: `days/day-83-eval-suite-green/`

## Parts

### 1.1 - A gate on the instruments
`days/day-83-eval-suite-green/parts/01-reading-the-gate/1.1-a-gate-on-the-instruments.md` · level `foundation` · ids AG-28

Every other phase gate asked whether the thing the phase built works; this one cannot, because what Phase 12 built is the measuring equipment — so the gate has to measure the ruler, and a ruler is checked by asking what it says about something whose length you already know.

### 1.2 - What \"full evalset green\" actually asks
`days/day-83-eval-suite-green/parts/01-reading-the-gate/1.2-what-full-evalset-green-asks.md` · level `foundation` · ids AG-28

Six words hide four separate questions — which cases, which metrics, at which threshold, on which run — and until each is answered in writing, "green" is a word two people can both use honestly about opposite states of the same repository.

### 1.3 - Green is not evidence
`days/day-83-eval-suite-green/parts/01-reading-the-gate/1.3-green-is-not-evidence.md` · level `working` · ids AG-28

A suite reports green in two situations that look identical from outside — it measured the desk and the desk was fine, or it never measured anything — and this phase's suite is in the second one, twice over: once because a threshold can be set where nothing fails, and once because the judged half has never been run at all.

### 2.1 - Criterion 1 — the evalset survives a round trip
`days/day-83-eval-suite-green/parts/02-instrument-criteria/2.1-criterion-1-the-evalset-round-trips.md` · level `working` · ids AG-28

Nine tool calls go into the file and nine come back, so the data the suite runs on is intact — and the same check reports the one detail that decides criterion 4: what comes back is an IntermediateData, which is a different type from the one some of ADK's own evaluators look for.

### 2.2 - Criterion 2 — the suite goes red against a stub desk
`days/day-83-eval-suite-green/parts/02-instrument-criteria/2.2-criterion-2-the-suite-goes-red.md` · level `working` · ids AG-28

Point the suite at a desk that calls no tools and returns an empty string; if it refuses all three cases, the metrics can produce a failure, and if it does not, every green run the suite has ever produced means nothing.

### 2.3 - Criterion 3 — every rubric line is exercised both ways
`days/day-83-eval-suite-green/parts/02-instrument-criteria/2.3-criterion-3-the-rubric-is-exercised.md` · level `working` · ids AG-28

A rubric line that every conversation in the set is supposed to earn cannot tell a judge that read it from a judge that answers yes to everything — so before spending a single request on grading, check the labels a person already wrote and require at least one yes and one no on every line.

### 2.4 - Criterion 4 — the rubric can see the tool calls
`days/day-83-eval-suite-green/parts/02-instrument-criteria/2.4-criterion-4-the-rubric-can-see.md` · level `production` · ids AG-28

The gate's second clause is "rubric trajectories pass", and the trajectory is not in the transcript the trajectory judge is shown: three recorded tool calls render as zero, because ADK's assembler reads one of the two shapes intermediate_data can hold and the .evalset.json file round-trips into the other one.

### 3.1 - Criterion 5 — the judge beats its baseline
`days/day-83-eval-suite-green/parts/03-judge-and-bill/3.1-criterion-5-the-judge-beats-baseline.md` · level `working` · ids AG-28

The only judge Phase 12 ever compared against human labels agreed on 83.3% of twenty-four answers, and always answering the commonest label agrees on 83.3% too — a margin of zero and a kappa of zero, which means the phase has never established that any judge in it reads anything.

### 3.2 - Criterion 6 — the phase fits a free-tier day
`days/day-83-eval-suite-green/parts/03-judge-and-bill/3.2-criterion-6-the-phase-fits.md` · level `working` · ids AG-28

The judged half of the suite wants 270 requests a night on a lane whose daily allowance nobody has ever measured, so the criterion exits 2 — neither pass nor fail — and the fifth day in a row that the same missing number has decided the answer is itself the finding.

### 4.1 - Criterion 7 — there is a previous run to compare against
`days/day-83-eval-suite-green/parts/04-repository-criteria/4.1-criterion-7-there-is-a-yesterday.md` · level `working` · ids AG-28

Day 82 built a correct comparison between two eval runs and this repository is keeping zero of them — two result files exist on disk, git is tracking neither, and each is caught by a different ignore rule written for a different good reason.

### 4.2 - Criterion 8 — every day written, no ID left open
`days/day-83-eval-suite-green/parts/04-repository-criteria/4.2-criterion-8-every-day-written.md` · level `working` · ids AG-28

Three independent sources have to agree about what this phase closed — the plan's assignment, the hub frontmatter of each day, and the ledger row — and the first two agree perfectly over Days 79 to 82 while the third has no rows at all, so nine concept IDs are open in a phase whose work is finished.

### 5.1 - The verdict
`days/day-83-eval-suite-green/parts/05-the-verdict/5.1-the-verdict.md` · level `production` · ids AG-28

Three pass, four fail, one cannot be determined — and the honest headline is not the arithmetic but the sentence underneath it: the suite has never been run in full, and four of the eight checks say it could not yet be believed if it had.

### 5.2 - What a green Phase 12 would have meant
`days/day-83-eval-suite-green/parts/05-the-verdict/5.2-what-a-green-phase-12-would-mean.md` · level `production` · ids AG-28

Run exactly the same eight checks, print two sentences instead of their findings, and the gate exits 0 with every one of those findings still true — which is the whole of how a phase ships green, and it takes no dishonesty from anybody.

### 5.3 - What Phase 13 inherits
`days/day-83-eval-suite-green/parts/05-the-verdict/5.3-what-phase-13-inherits.md` · level `production` · ids AG-28

Five open items cross the phase boundary, and the order to fix them in is not the order they failed in: the ledger rows and the history directory are an hour between them and unblock everything else, the trajectory conversion is a small function with a large blast radius, and the two that need measurements need somebody to spend an afternoon rather than to write code.

## Papers - read after the parts

### doi:10.1016/0149-7189(79)90048-X - The number that became the target
`days/day-83-eval-suite-green/papers/01-the-number-that-became-the-target.md`

A measurement that is only watched stays honest, and a measurement that decides something starts being optimised — so the moment an eval score gates a merge, the score and the quality it stood for begin to come apart, and nothing in the score reports that it is happening.


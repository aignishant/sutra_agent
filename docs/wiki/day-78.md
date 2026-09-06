# Day 78 - Phase gate — ambient and voice, inside free quota

IDs closed: OPS-14 · source: `days/day-78-inside-free-quota/`

## Parts

### 1.1 - An allowance, not a speed limit
`days/day-78-inside-free-quota/parts/01-the-allowance/1.1-an-allowance-not-a-speed-limit.md` · level `foundation` · ids OPS-14

A provider hands you two completely different limits — how fast you may ask and how much you may ask for in a day — and a scheduler that plans against the first one will always look comfortable while running out of the second.

### 1.2 - A schedule is a spending plan
`days/day-78-inside-free-quota/parts/01-the-allowance/1.2-a-schedule-is-a-spending-plan.md` · level `foundation` · ids OPS-14

The moment you put a job on a clock you have committed an amount of the day's allowance to it, every day, without being asked again — so a crontab is not a list of times, it is a standing order, and the only honest way to read one is to add it up.

### 1.3 - Counting what it actually spends
`days/day-78-inside-free-quota/parts/01-the-allowance/1.3-counting-what-it-actually-spends.md` · level `working` · ids OPS-14

Phase 11 commits 62 requests a day to a lane this repository has observed holding 20, and 60 a day to a lane nobody has measured at all — and the second of those two numbers is the more serious finding, because a plan against an unknown allowance is not a plan.

### 2.1 - Ask before you spend
`days/day-78-inside-free-quota/parts/02-asking-before-spending/2.1-ask-before-you-spend.md` · level `working` · ids OPS-14

A quota-aware job asks one question before it starts — is there enough left for all of me? — and the whole value of the question is that it is asked once, before the first request, not discovered request by request half-way through.

### 2.2 - The reservation, not the check
`days/day-78-inside-free-quota/parts/02-asking-before-spending/2.2-the-reservation-not-the-check.md` · level `production` · ids OPS-14

Asking is there room? and then spending are two separate acts, and anything that happens between them makes the answer stale — measured here as 24 requests spent against an allowance of 20, by two jobs that both asked first and both got a truthful yes.

### 2.3 - Whose midnight resets it
`days/day-78-inside-free-quota/parts/02-asking-before-spending/2.3-whose-midnight-resets-it.md` · level `production` · ids OPS-14

The window an allowance is counted in belongs to the provider, not to your machine — and a scheduler that starts a fresh day at its own midnight spends against a balance that does not exist yet: measured here as 10 of 12 requests refused on a job that believed it had the full allowance.

### 2.4 - The job that ran anyway
`days/day-78-inside-free-quota/parts/02-asking-before-spending/2.4-the-job-that-ran-anyway.md` · level `production` · ids OPS-14

💥 Every one of fourteen runs asked before spending, every answer was correct, not one request was wasted — and the night still did not happen, because a scheduler with no priority order admits whatever wakes first and a clock has no opinion about what matters.

### 3.1 - Three things a job can do when it cannot afford itself
`days/day-78-inside-free-quota/parts/03-when-you-cannot-afford-it/3.1-three-things-a-job-can-do.md` · level `working` · ids OPS-14

There are exactly three honest answers to I cannot afford all of me — skip, shrink and defer — they are not interchangeable, and choosing between them is a decision about what the job is for rather than a technical detail.

### 3.2 - The shrunken run that reports as full
`days/day-78-inside-free-quota/parts/03-when-you-cannot-afford-it/3.2-the-shrunken-run-that-reports-as-full.md` · level `production` · ids OPS-14

💥 evals: 10 of 10 passed — every word of it true, produced by a run that checked one sixth of the suite and did not look at any of the six cases that fail.

### 4.1 - What Phase 11 promised
`days/day-78-inside-free-quota/parts/04-the-gate/4.1-what-phase-11-promised.md` · level `foundation` · ids OPS-14

The gate sentence — "nightly job + voice standup within free quota" — is not one promise but three, and reading it as three is what turns a phrase in a plan into five commands with exit codes.

### 4.2 - Criterion 1 — the nightly runs, dies honestly and resumes
`days/day-78-inside-free-quota/parts/04-the-gate/4.2-criterion-1-the-nightly.md` · level `working` · ids OPS-14

The criterion is not "the nightly works" but three separate assertions in one command — a clean run produces all three artefacts, a killed run keeps exactly one and says where it died, and a resume finishes — and the middle one is the only one that could not be faked.

### 4.3 - Criterion 2 — the voice standup delivers and can be stopped
`days/day-78-inside-free-quota/parts/04-the-gate/4.3-criterion-2-the-voice-standup.md` · level `working` · ids OPS-14

A spoken report is only delivered if the listener got the part that was for them before they stopped listening, so the criterion asserts two things a transcript cannot: that the urgent lines came first, and that stopping the report actually stops it.

### 4.4 - Criterion 3 — the phase fits a free-tier allowance
`days/day-78-inside-free-quota/parts/04-the-gate/4.4-criterion-3-the-phase-fits.md` · level `production` · ids OPS-14

This criterion has three outcomes rather than two, and today it returns the third — cannot determine, exit code 2 — because one lane's demand is 60 requests a night against an allowance nobody in this repository has ever measured.

### 4.5 - Criterion 4 — the freshness check
`days/day-78-inside-free-quota/parts/04-the-gate/4.5-criterion-4-the-freshness-check.md` · level `working` · ids OPS-14

Every pinned package must have a dated row saying where its version came from, and mcp==1.29.1 still does not — a finding this repository's gates have now reported four times without it being fixed, which is a fact about the process rather than about the package.

### 4.6 - Criterion 5 — every day written, no ID left open
`days/day-78-inside-free-quota/parts/04-the-gate/4.6-criterion-5-every-day-written.md` · level `working` · ids OPS-14

Three independent sources — the plan's day map, each day's own frontmatter, and the progress ledger — must agree, and today they agree on the first two and disagree on the third for all six days of the phase.

### 4.7 - The verdict
`days/day-78-inside-free-quota/parts/04-the-gate/4.7-the-verdict.md` · level `production` · ids OPS-14

Two green, two red, one that cannot be determined — and the gate refuses to call itself green not because three criteria failed, but because a gate whose green criteria have not been shown to be capable of failing has not measured anything.

### 5.1 - The nightly competes with the day
`days/day-78-inside-free-quota/parts/05-in-production/5.1-the-nightly-competes-with-the-day.md` · level `production` · ids OPS-14

An allowance is not divided between your jobs — it is shared with everything else that touches the same project, including the users you are trying to serve — so the nightly's 14 requests are taken from somebody's afternoon, and the scheduler has no idea whose.

### 5.2 - What a real quota-aware scheduler adds
`days/day-78-inside-free-quota/parts/05-in-production/5.2-what-a-real-scheduler-adds.md` · level `production` · ids OPS-14

The lab admits, prioritises and degrades correctly, and the distance between it and something you would put in front of a production quota is not vague hardening — it is nine specific things, each cheap on the day the scheduler is written and expensive on the day it is needed, and two of them this curriculum deliberately parks rather than forgets.

## Papers - read after the parts

### doi:10.1145/321738.321743 - Does it fit? — the 1973 utilisation test
`days/day-78-inside-free-quota/papers/01-schedulability.md`

A set of jobs, each running every so often and costing a fixed amount, can be checked against a shared resource before any of them runs by adding up one fraction per job — and the demo below shows that check refusing one job to keep a schedule at 14 of 20 requests, where switching it off admits everything and lands at 62 of 20.


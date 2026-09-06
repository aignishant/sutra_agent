# Day 73 - Ambient agents — the nightly job (re-index, full evals, digest)

IDs closed: AG-24, ADK-51 · source: `days/day-73-ambient-agents/`

## Parts

### 1.1 - Nobody is watching
`days/day-73-ambient-agents/parts/01-the-agent-nobody-watches/1.1-nobody-is-watching.md` · level `foundation` · ids AG-24, ADK-51

An ambient agent is one that nobody started and nobody is watching, which removes three things every agent in this repository has quietly relied on — the person who could be asked, the person who would notice, and the person who would decide — and the whole of today's design is the cost of replacing them.

### 1.2 - Three stages in a forced order
`days/day-73-ambient-agents/parts/01-the-agent-nobody-watches/1.2-three-stages-in-a-forced-order.md` · level `foundation` · ids AG-24, ADK-51

The three stages run in that order because each one reads the file the previous one wrote, and that dependency is a check at the top of each stage rather than a comment: run_evals refuses without index.json, write_digest refuses without evals.json — so the order is a fact about the data, not a preference of whoever typed the list.

### 1.3 - The first clean run
`days/day-73-ambient-agents/parts/01-the-agent-nobody-watches/1.3-the-first-clean-run.md` · level `working` · ids AG-24, ADK-51

The run prints seven lines and then the process is gone, so the run is not those seven lines — it is state/index.json, state/evals.json and state/digest.md, and the digest says 3 of 5 passed because two of the eval cases are meant to fail.

### 2.1 - The run that dies
`days/day-73-ambient-agents/parts/02-when-it-dies-at-three-am/2.1-the-run-that-dies.md` · level `working` · ids AG-24, ADK-51

An ambient job will stop half-way, and the design question is not how to prevent that but what the half-finished run leaves behind: killed during the eval stage, Sutra's nightly leaves index.json on disk, no evals.json, no digest.md, an exit code of 1, and one line in the run log saying "died_at": "evals" — and that leftover index is not mess to be cleaned up, it is the only progress the night made.

### 2.2 - Stages you can iterate
`days/day-73-ambient-agents/parts/02-when-it-dies-at-three-am/2.2-stages-you-can-iterate.md` · level `working` · ids AG-24, ADK-51

Resume is a skip, and a skip is only expressible if the stage list is data you can iterate — STAGES as a tuple of (name, callable) and DONE as a map from name to the file that proves it finished, so the same single if skips one stage after a death at evals and two after a death at digest, without being told which.

### 2.3 - Two runs at once
`days/day-73-ambient-agents/parts/02-when-it-dies-at-three-am/2.3-two-runs-at-once.md` · level `production` · ids AG-24, ADK-51

A scheduler fires on a clock, not on whether the last run finished — so two runs can be alive at the same time writing the same files, and the one that finishes last wins regardless of which one is newer: measured, a 6-row index is silently replaced by a 5-row one with nothing anywhere reporting an error, and the fix is a lock taken before the first stage whose important property is that the loser refuses and says so.

### 2.4 - The lock nobody released
`days/day-73-ambient-agents/parts/02-when-it-dies-at-three-am/2.4-the-lock-nobody-released.md` · level `production` · ids AG-24, ADK-51

The lock that fixed part [2.3](2.3-two-runs-at-once.md) is taken in one line and released in none, so a single run that dies while holding it refuses every run after it — measured: the second take_lock() returns False, the file is still on disk, and grep finds exactly two mentions of the lock in the whole file, one to name it and one to create it.

### 3.1 - The run log
`days/day-73-ambient-agents/parts/03-the-morning-after/3.1-the-run-log.md` · level `working` · ids AG-24, ADK-51

The three artefacts on disk tell you what the job produced; only the run log tells you what the job did — and its whole purpose is to keep apart three states that otherwise look identical: a run that finished, a run that died part-way, and a run that never happened. It manages the first two, in two lines of JSON. The third leaves no line at all, and that is part [3.3](3.3-nobody-notices-silence.md)'s subject.

### 3.2 - The digest that reassures
`days/day-73-ambient-agents/parts/03-the-morning-after/3.2-the-digest-that-reassures.md` · level `production` · ids AG-24, ADK-51

The digest is the entire interface between a job nobody watched and the people who own it, and its failure mode is not being wrong — it is being reassuring: measured, the success-only digest names 0 of the 2 failing eval cases while every number in it is true, and the attention-first digest names 2 from the same three files, because the fix is not more information, it is ordering.

### 3.3 - Nobody notices silence
`days/day-73-ambient-agents/parts/03-the-morning-after/3.3-nobody-notices-silence.md` · level `production` · ids AG-24, ADK-51

Every failure this day has covered produces something to look at; a job that stops running produces nothing, and the lab makes that undetectable on purpose — three of the four artefacts contain no date at all, so this morning's digest and one from a fortnight ago are the same file.

### 4.1 - What ADK offers
`days/day-73-ambient-agents/parts/04-what-wakes-it/4.1-what-adk-offers.md` · level `working` · ids AG-24, ADK-51

ADK does have a built-in answer to what wakes an agent from outside — get_fast_api_app(..., trigger_sources=[...]) — and reading it off the installed package rather than off a tutorial tells you two things a tutorial would not: the accepted values are exactly pubsub and eventarc, and both are hosted cloud services that need a project and credentials, so this curriculum parks them and lets the operating system do the waking instead.

### 4.2 - The scheduler you already have
`days/day-73-ambient-agents/parts/04-what-wakes-it/4.2-the-scheduler-you-already-have.md` · level `production` · ids AG-24, ADK-51

🅿️ Parked — awareness-level, interview-ready, deliberately not built here. Every machine you own already has a scheduler that will run a command at a set instant for free, which is why this day uses it instead of the two hosted triggers part [4.1](4.1-what-adk-offers.md) parked behind a billing account — but a scheduler is a very small, very dumb thing that does exactly that one job, and the four jobs people assume it also does are all yours: it does not check whether the last run finished, it does not keep the output, it does not retry a failed run, and it does not tell you when the command was not run at all.

### 5.1 - What a nightly job spends
`days/day-73-ambient-agents/parts/05-in-production/5.1-what-a-nightly-job-spends.md` · level `production` · ids AG-24, ADK-51

A nightly job is the largest recurring quota commitment a system makes and a scheduler commits to it rather than a person, so it has to be priced before it is scheduled, in requests per day — and the lab's passed=3 total=5 cost zero requests only because its evals never call a model.

### 5.2 - What a real ambient system adds
`days/day-73-ambient-agents/parts/05-in-production/5.2-what-a-real-ambient-system-adds.md` · level `production` · ids AG-24, ADK-51

The lab is a correct small nightly job, and the distance between it and one you would put on a schedule is not vague "hardening" — it is a list of nine specific things, each cheap to add on the day the job is written and expensive on the day it is needed, and two of them are deliberately parked by this curriculum rather than forgotten.

## Papers - read after the parts

### doi:10.1145/2181796.2187821 - Idempotence Is Not a Medical Condition
`days/day-73-ambient-agents/papers/01-idempotence.md`

The property that makes every retried system possible is idempotence — applying an operation twice leaves the same state as applying it once — and it is not a nicety: switching it off in the demo below leaves a recorded total of 28 where the truth is 10, with no error raised, nothing lost, and nothing anywhere reporting a problem.


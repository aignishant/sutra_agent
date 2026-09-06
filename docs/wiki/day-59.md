# Day 59 - Phase gate + failure lab — loops, runaway agents, containment

IDs closed: AG-21, SEC-04 · source: `days/day-59-runaway-agents-contained/`

## Parts

### 1.1 - A runaway is a missing stop, not a mistake
`days/day-59-runaway-agents-contained/parts/01-four-runaways/1.1-a-runaway-is-a-missing-stop.md` · level `foundation` · ids AG-21

A runaway agent is not an agent that does the wrong thing; it is an agent that never receives the instruction to be finished, which is why every runaway in this day is built out of parts that are each working exactly as designed.

### 1.2 - The critic who is never satisfied
`days/day-59-runaway-agents-contained/parts/01-four-runaways/1.2-the-critic-who-is-never-satisfied.md` · level `working` · ids AG-21

The tight loop is two steps that each do their job correctly and between them contain no sentence that means this is finished, and with the shipped default fuse of five hundred model calls it can spend twenty-five times a whole day's free-tier quota inside a single run.

### 1.3 - Two caps, one rally, twice the work
`days/day-59-runaway-agents-contained/parts/01-four-runaways/1.3-two-caps-one-rally-twice-the-work.md` · level `working` · ids AG-21

When two agents hand work to each other, every per-agent limit can be respected and the system still does more than any of them authorised: two desks capped at three hand-offs each produced a rally of seven, because a counter can only count what passes through the desk it lives in.

### 1.4 - The shape that grows by a power
`days/day-59-runaway-agents-contained/parts/01-four-runaways/1.4-the-shape-that-grows-by-a-power.md` · level `working` · ids AG-21

A step that splits itself into sub-steps costs the branching factor raised to the depth, so a modest-looking cap of five levels at two branches each is sixty-three model calls — three times a whole day's free tier, from one run, with a limit in place.

### 1.5 - 💥 The quiet runaway the fuse cannot see
`days/day-59-runaway-agents-contained/parts/01-four-runaways/1.5-the-quiet-runaway-the-fuse-cannot-see.md` · level `working` · ids AG-21, SEC-04

A loop made of tool calls rather than model calls costs nothing that anybody is counting, so a run with max_llm_calls=4 set read two hundred and one pages of an archive without the fuse ever firing.

### 2.1 - A guard is only a guard if it is outside
`days/day-59-runaway-agents-contained/parts/02-where-a-brake-goes/2.1-a-guard-is-only-a-guard-if-it-is-outside.md` · level `working` · ids SEC-04

A limit written into an agent's instruction is not a limit, it is a request: the same guard sentence produced twenty-one model calls when the model did not comply and three when the same rule was moved into an edge condition.

### 2.2 - The loop counter, checked before the quality condition
`days/day-59-runaway-agents-contained/parts/02-where-a-brake-goes/2.2-the-loop-counter.md` · level `working` · ids AG-21

A loop cap consulted before the quality check costs one fewer call per run and, more importantly, still holds when the quality check itself fails — the ordering that asks the critic first died with the critic and never consulted the cap at all.

### 2.3 - The run fuse: what max_llm_calls counts
`days/day-59-runaway-agents-contained/parts/02-where-a-brake-goes/2.3-the-run-fuse.md` · level `working` · ids AG-21

max_llm_calls is one field on RunConfig that counts every model call in an invocation, across every agent and node in it, which is why it catches the rally that no per-agent counter can see — and its shipped default of 500 is twenty-five times this project's entire daily free tier.

### 2.4 - The circuit breaker: the brake denominated in requests
`days/day-59-runaway-agents-contained/parts/02-where-a-brake-goes/2.4-the-circuit-breaker.md` · level `production` · ids SEC-04

A plugin that consults the day's quota ledger before every model call is the only brake that outlives a single run, and when it refuses it costs zero model calls — against one for the same breaker written to log instead of raise.

### 2.5 - The kill switch and what it leaves on the floor
`days/day-59-runaway-agents-contained/parts/02-where-a-brake-goes/2.5-the-kill-switch-and-what-it-leaves.md` · level `production` · ids SEC-04

A brake declines the next step and a kill stops the current one, so the question that matters is not how to stop a run but what state it leaves behind: killing the same ticket at three different stations left three different amounts of work done and one, two or three model calls spent and unrecoverable.

### 3.1 - 💥 The guard the agent can talk past
`days/day-59-runaway-agents-contained/parts/03-brakes-that-do-not-hold/3.1-the-guard-the-agent-can-talk-past.md` · level `production` · ids SEC-04

A guard placed inside the thing it guards is not a weak guard, it is a guard whose result is decided by the thing it was protecting you from — and the demonstration is that the same rule produced twenty-one calls, four calls and three calls depending only on where it lived.

### 3.2 - 💥 Three retries become twenty-seven
`days/day-59-runaway-agents-contained/parts/03-brakes-that-do-not-hold/3.2-three-retries-become-twenty-seven.md` · level `production` · ids SEC-04

Retries at three layers multiply rather than add, so three sensible attempts at each of three levels is twenty-seven calls against a daily free tier of twenty — and one shared attempt budget across the whole stack turns the same failure into one call.

### 3.3 - 💥 The fuse set to zero, which is no fuse at all
`days/day-59-runaway-agents-contained/parts/03-brakes-that-do-not-hold/3.3-the-fuse-set-to-zero.md` · level `production` · ids SEC-04

max_llm_calls=0 means unbounded rather than forbidden, and the library warns you about it into a logger a normal script never configures — so a run configured with the tightest-looking limit available made sixteen model calls with the fuse never firing.

### 3.4 - 💥 The brake loosened for one ticket
`days/day-59-runaway-agents-contained/parts/03-brakes-that-do-not-hold/3.4-the-brake-loosened-for-one-ticket.md` · level `production` · ids AG-21, SEC-04

Brakes are sized against each other, so raising one without re-deriving the rest silently changes the worst case everywhere: moving the revision cap from two to eight took the nightly worst case from sixty model calls to two hundred and four, against a free tier of twenty, with no other line changed.

### 4.1 - Stopping is an answer; continuing is not
`days/day-59-runaway-agents-contained/parts/04-fail-stop/4.1-stopping-is-an-answer.md` · level `production` · ids SEC-04

A system that cannot compute correctly has exactly two options, and only one of them is honest: the run that refused exited 1 with nothing invented, and the run that carried on exited 0 with a fix the archive never contained.

### 4.2 - What a refusal has to say to be worth anything
`days/day-59-runaway-agents-contained/parts/04-fail-stop/4.2-what-a-refusal-has-to-say.md` · level `production` · ids SEC-04

"Sorry, something went wrong" and a five-field refusal naming the failed component, the reason, what is still true, the next step and the run id both exit 1 and invent nothing, and only one of them lets anybody do anything.

### 5.1 - Criterion 1 — the triage graph runs end to end
`days/day-59-runaway-agents-contained/parts/05-the-gate/5.1-criterion-1-end-to-end.md` · level `production` · ids AG-21

The Phase 8 gate says triage graph v1 end-to-end, and the version of that sentence a gate can use names the tickets, the path each one must take and the calls each is allowed: five model calls for an answered ticket, zero for an unknown one, and an exit code.

### 5.2 - Criterion 2 — every shape has a brake, and the brake is tested
`days/day-59-runaway-agents-contained/parts/05-the-gate/5.2-criterion-2-every-shape-has-a-brake.md` · level `production` · ids SEC-04

Four runaway shapes against four brakes is a table with sixteen cells, and the cell that matters is the one where the quiet runaway is covered only by a loop counter somebody has to have remembered to write — because Sutra has no run deadline, and a per-node timeout is not one.

### 5.3 - Criterion 3 — the eval goes red when a brake is removed
`days/day-59-runaway-agents-contained/parts/05-the-gate/5.3-criterion-3-the-eval-goes-red.md` · level `production` · ids SEC-04

A check that has never failed is a check nobody has evidence about, so this criterion is not "the tests pass" but "here is the command that makes each of them fail, and here is it failing": gate.py exits 1 today, and every other check in this day has a flag that turns it red.

### 5.4 - Criterion 4 — the request budget is measured, not estimated
`days/day-59-runaway-agents-contained/parts/05-the-gate/5.4-criterion-4-the-budget-is-measured.md` · level `production` · ids AG-21

The day's demos would have cost fourteen provider requests against a free tier of twenty, and cost zero, because every model in the lab is a BaseLlm subclass that counts itself — and the number is printed by a script rather than added up by hand.

### 5.5 - Criterion 5 — the freshness check
`days/day-59-runaway-agents-contained/parts/05-the-gate/5.5-criterion-5-the-freshness-check.md` · level `production` · ids AG-21

Every phase gate re-verifies the things the ecosystem can move underneath you, and this one found that all three of Sutra's pins are behind — google-adk 2.7.1 against 2.8.0, google-genai 2.19.0 against 2.22.0, mcp 1.29.1 against 2.1.1 — and that mcp is pinned with no row in docs/PACKAGES.md, which is a Principle 7 violation standing since Phase 5.

### 5.6 - Criterion 6 — the IDs, and the verdict written down
`days/day-59-runaway-agents-contained/parts/05-the-gate/5.6-criterion-6-the-ids-and-the-verdict.md` · level `production` · ids AG-21, SEC-04

All seven Phase 8 days declare exactly the IDs the plan assigns them, so criterion 6 is green — and the verdict for the phase as a whole is three green, two amber, one red, where the red belongs to a ruff error from Day 15 and the phase does not get to round that up.

### 6.1 - Brakes are a system with an invariant
`days/day-59-runaway-agents-contained/parts/06-in-production/6.1-brakes-are-a-system.md` · level `production` · ids SEC-04

The four brakes in this day are terms in two inequalities rather than four independent settings, so the discipline that makes them hold is a rule about pull requests: a change to any brake constant shows the arithmetic, and a script computes it so that the arithmetic is a command rather than an intention.

### 6.2 - 🅿️ What Phase 9 takes over
`days/day-59-runaway-agents-contained/parts/06-in-production/6.2-what-phase-nine-takes-over.md` · level `production` · ids AG-21, SEC-04

Containment stops a run; it does not put the work back, and the three things this day deliberately does not build — a run deadline, bulkheads between workloads, and resumption — are the boundary between "it stopped" and "nothing was lost".

## Papers - read after the parts

### doi:10.1145/357369.357371 - Fail-stop processors: an approach to designing fault-tolerant computing systems
`days/day-59-runaway-agents-contained/papers/01-fail-stop-processors.md`

A processor that halts on detecting a fault — rather than continuing and producing a wrong result — converts an arbitrary failure into one the rest of the system can reason about, and that transformation is what makes fault tolerance tractable at all.


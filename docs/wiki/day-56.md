# Day 56 - Planning patterns — plan-and-execute, replanning

IDs closed: AG-17, AG-18 · source: `days/day-56-planning-and-replanning/`

## Parts

### 1.1 - A plan is a list, not a paragraph
`days/day-56-planning-and-replanning/parts/01-what-a-plan-is/1.1-a-plan-is-a-list-not-a-paragraph.md` · level `foundation` · ids AG-17

A plan is a data structure — an ordered set of steps with named fields — and the moment you write it as prose instead, you lose the four things a plan is for: counting it, checking its coverage, differencing two editions of it, and deciding whether it may run.

### 1.2 - What a step has to carry
`days/day-56-planning-and-replanning/parts/01-what-a-plan-is/1.2-what-a-step-has-to-carry.md` · level `foundation` · ids AG-17

A step needs exactly three fields — an action from a closed set, an argument the executor can act on, and a why a human can judge — and three of the six candidate steps in the lab fail on one of them, each for a different reason.

### 1.3 - The plan you can read before it runs
`days/day-56-planning-and-replanning/parts/01-what-a-plan-is/1.3-the-plan-you-can-read-before-it-runs.md` · level `working` · ids AG-17

A plan can be scored against the request before a single step executes — this one comes back 3/4, missing the knowledge base article — and two editions of a plan can be differenced exactly, which together are the only two checks in this whole day that cost nothing at all.

### 2.1 - Deciding with your eyes on the last thing you read
`days/day-56-planning-and-replanning/parts/02-two-ways-to-decide/2.1-deciding-with-your-eyes-on-the-last-thing.md` · level `working` · ids AG-17

A reactive loop chooses its next step by looking at the most recent observation, which means the request itself is out of view from step two onwards — and on the standing three-part request it covers 4 of 4, because following the trail happened to work.

### 2.2 - Deciding once, from the whole request
`days/day-56-planning-and-replanning/parts/02-two-ways-to-decide/2.2-deciding-once-from-the-whole-request.md` · level `working` · ids AG-17

Plan-and-execute changes exactly one thing about the reactive loop — the chooser reads the whole request instead of the last observation — and that one change costs one model call instead of four and covers every part the request names, and only those.

### 2.3 - 💥 The two strategies miss different things
`days/day-56-planning-and-replanning/parts/02-two-ways-to-decide/2.3-the-two-strategies-miss-different-things.md` · level `production` · ids AG-17

On the same four-part request both strategies score 4 out of 6 — and they miss completely different things: planning misses both knowledge base articles because the request could not name them, reacting misses a ticket the request named outright because it stopped resembling the trail.

### 2.4 - What a plan costs in requests
`days/day-56-planning-and-replanning/parts/02-two-ways-to-decide/2.4-what-a-plan-costs-in-requests.md` · level `working` · ids AG-17

Planning is one request whatever the request contains and reacting is one per step, which on the free tier is 20 investigations a day against 5 — and the advantage disappears entirely at three plan editions once any step needs judgement of its own.

### 3.1 - The executor is a loop with a list in its hand
`days/day-56-planning-and-replanning/parts/03-walking-the-plan/3.1-the-executor-is-a-loop-with-a-list.md` · level `working` · ids AG-17

The executor is Day 3's think→act→observe loop with the thinking removed — it walks a list that was decided in advance, and on the five-step plan below it completes all five while making zero decisions.

### 3.2 - What a step is allowed to see
`days/day-56-planning-and-replanning/parts/03-walking-the-plan/3.2-what-a-step-is-allowed-to-see.md` · level `working` · ids AG-17

A plan states an order, not a set of dependencies — so step 3 can compare two tickets it was never handed and report ok, and the only difference between a run where each step sees nothing and one where each step sees everything is a single number in the executor.

### 3.3 - A plan that outlives its process
`days/day-56-planning-and-replanning/parts/03-walking-the-plan/3.3-a-plan-that-outlives-its-process.md` · level `working` · ids AG-17

Because the plan is data and the executor's position in it is an integer, a half-finished run is 957 bytes of JSON you can open in a text editor — and a second process picks it up at step 3 and finishes without re-running steps 1 and 2.

### 3.4 - The same executor as an ADK workflow
`days/day-56-planning-and-replanning/parts/03-walking-the-plan/3.4-the-same-executor-as-an-adk-workflow.md` · level `working` · ids AG-17

ADK 2.x expresses a plan-walking executor as a dynamic workflow — an async function decorated @node(rerun_on_resume=True) that calls ctx.run_node() once per step — and the same four steps run through it with zero model calls, because a node is a unit of work and not a unit of intelligence.

### 4.1 - A shop shut for lunch and a shop closed down
`days/day-56-planning-and-replanning/parts/04-when-a-plan-dies/4.1-a-shop-shut-for-lunch-and-a-shop-closed-down.md` · level `working` · ids AG-18

A failed step is one of two completely different things — a hiccup, which a retry fixes, or a contradiction, which no retry can ever fix — and of the six steps in the lab exactly one is the first kind and three are the second.

### 4.2 - Retrying a contradiction
`days/day-56-planning-and-replanning/parts/04-when-a-plan-dies/4.2-retrying-a-contradiction.md` · level `working` · ids AG-18

The hiccup clears on attempt 2 and the three contradictions are identical on all three attempts — so a blanket retry policy spends two extra requests per contradiction to learn exactly what the first attempt already said.

### 4.3 - 💥 The step that worked and told you nothing
`days/day-56-planning-and-replanning/parts/04-when-a-plan-dies/4.3-the-step-that-worked-and-told-you-nothing.md` · level `production` · ids AG-18

Three steps succeed, the executor reports 3 of 3, and only 1 of 3 returned anything the goal could use — a failure with no error, no exit code and no way for an executor whose definition of failure is "the step raised" to see it.

### 4.4 - 💥 The plan that outlived the world
`days/day-56-planning-and-replanning/parts/04-when-a-plan-dies/4.4-the-plan-that-outlived-the-world.md` · level `production` · ids AG-18

A ticket is closed and merged after the plan is written and before it is executed, and the run produces 0 contradictions, 0 replans and 1 reply sent to a closed ticket — because a plan is a photograph of the world at planning time and nothing in execution re-checks it.

### 5.1 - Let the seam out, or re-cut the cloth
`days/day-56-planning-and-replanning/parts/05-the-second-edition/5.1-let-the-seam-out-or-recut-the-cloth.md` · level `working` · ids AG-18

A contradiction can be repaired by dropping the dead step and everything that depended on it or by writing a new plan for the whole goal — and on the same failure the patch covers 2 of 3 required things and the rewrite covers 3 of 3, because the dead step was the only route to the third.

### 5.2 - The work already paid for
`days/day-56-planning-and-replanning/parts/05-the-second-edition/5.2-the-work-already-paid-for.md` · level `working` · ids AG-18

A replanner handed the completed results executes 4 steps total with 0 repeats; the same replanner starting from nothing executes 5 with 1 repeat — and when the repeated step is one that sends something, "1 repeat" is a customer receiving the same reply twice.

### 5.3 - The brake, and the sentence it prints
`days/day-56-planning-and-replanning/parts/05-the-second-edition/5.3-the-brake-and-the-sentence-it-prints.md` · level `production` · ids AG-18

MAX_REPLANS = 1 stops the second edition from becoming a third, and what it produces is not a crash but a sentence — an escalation naming the edition count, the completed steps and the last failure — with exit code 1, because Principle 10 says a system that cannot answer says so.

### 5.4 - 💥 Two plans taking turns
`days/day-56-planning-and-replanning/parts/05-the-second-edition/5.4-two-plans-taking-turns.md` · level `production` · ids AG-18

With the brake off, two editions that each fix the other's complaint alternate for twelve editions — twelve planning requests, more than half a day's free-tier quota, zero steps completed — and every single edition is a locally correct response to the failure it was shown.

### 6.1 - 💥 Every step ran and nothing was answered
`days/day-56-planning-and-replanning/parts/06-in-production/6.1-every-step-ran-and-nothing-was-answered.md` · level `production` · ids AG-18

A run completes 3 of 3 steps with exit code 0 and has not answered its goal — and the only thing that catches it is a condition written down with the goal, before the plan, which turns the same run into exit 1 and the word UNANSWERED.

### 6.2 - The plan somebody reads first
`days/day-56-planning-and-replanning/parts/06-in-production/6.2-the-plan-somebody-reads-first.md` · level `production` · ids AG-17

Because the plan is data, a review card — what it reads, what it writes, which step leaves the system — is a function of the plan alone, computed before anything runs, and that card is exactly what Day 63 turns into an approval gate.

### 6.3 - The step you cannot take back
`days/day-56-planning-and-replanning/parts/06-in-production/6.3-the-step-you-cannot-take-back.md` · level `production` · ids AG-18

Every repair in this day — retry, patch, rewrite, resume — assumes the step can be run again, and one class of step cannot: moving the reply from position 1 to position 3 changes nothing about the actions and turns a plan that answers a customer on zero evidence into one that answers on two.

### 6.4 - 🅿️ Plan repair, hierarchy and search
`days/day-56-planning-and-replanning/parts/06-in-production/6.4-plan-repair-hierarchy-and-search.md` · level `production` · ids AG-17, AG-18

Three techniques this day deliberately does not build — plan repair, hierarchical decomposition and search over plans — each with the number that would tell you it is time, because the honest reason Sutra has none of them is that on a four-step plan over six tickets they would all cost more than they return.

## Papers - read after the parts

### doi:10.1016/0004-3702(71)90010-5 - Strips: a new approach to the application of theorem proving to problem solving
`days/day-56-planning-and-replanning/papers/01-strips.md`

STRIPS said that a plan can be searched for mechanically if you stop describing the world in general logic and instead describe it as a set of facts, with each action written as three lists — what must be true, what becomes true, and what stops being true.


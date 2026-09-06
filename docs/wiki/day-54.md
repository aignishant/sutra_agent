# Day 54 - Sequential, parallel & loop patterns

IDs closed: ADK-35, ADK-36, ADK-37 · source: `days/day-54-sequential-parallel-loop/`

## Parts

### 1.1 - The order you declare is the order you get
`days/day-54-sequential-parallel-loop/parts/01-one-after-another/1.1-the-order-you-declare-is-the-order-you-get.md` · level `foundation` · ids ADK-35

A sequential workflow is one tuple — (START, a, b, c) — and the runtime turns it into three edges that run in exactly that order, handing each node the value the node before it returned.

### 1.2 - What the next stage can see
`days/day-54-sequential-parallel-loop/parts/01-one-after-another/1.2-what-the-next-stage-can-see.md` · level `working` · ids ADK-35

A node sees exactly two things: the value the node before it returned, bound to a parameter named node_input, and the session state, from which every other parameter is bound by name.

### 1.3 - Why calling them in order is not a workflow
`days/day-54-sequential-parallel-loop/parts/01-one-after-another/1.3-why-calling-them-in-order-is-not-a-workflow.md` · level `working` · ids ADK-35

route(classify(intake(text))) and the three-node graph return the same string, and only one of them is a thing you can inspect, validate, draw, pause and resume — because only one of them exists as data before it runs.

### 1.4 - The stage that refuses to run
`days/day-54-sequential-parallel-loop/parts/01-one-after-another/1.4-the-stage-that-refuses-to-run.md` · level `production` · ids ADK-35

Five different mistakes in a graph are all rejected the moment Workflow(...) is constructed, with a message that names the offending node — and knowing all five by sight is the difference between a two-minute fix and an evening.

### 2.1 - Three branches from one edge
`days/day-54-sequential-parallel-loop/parts/02-at-the-same-time/2.1-three-branches-from-one-edge.md` · level `foundation` · ids ADK-36

Putting a tuple of nodes where one node would go fans the graph out — all of them start before any of them finishes — and whatever sits downstream then runs once for each branch, which is almost never what you meant.

### 2.2 - The node that waits for everyone
`days/day-54-sequential-parallel-loop/parts/02-at-the-same-time/2.2-the-node-that-waits-for-everyone.md` · level `working` · ids ADK-36

A JoinNode runs once, after every branch pointing at it has finished, and hands the node after it a single dictionary keyed by branch name — where an ordinary node in the same position would have run once per branch.

### 2.3 - The order you cannot rely on
`days/day-54-sequential-parallel-loop/parts/02-at-the-same-time/2.3-the-order-you-cannot-rely-on.md` · level `working` · ids ADK-36

Branches start in the order you declared them, every single run, and the join's dictionary comes back in the order they finished — which changed five times across eight runs of the same graph and did not change at all across eight runs inside one process.

### 2.4 - Two branches, one state key
`days/day-54-sequential-parallel-loop/parts/02-at-the-same-time/2.4-two-branches-one-state-key.md` · level `production` · ids ADK-36

When two branches write the same session-state key, the value that survives is the one written by the branch that finished last — measured, in both declaration orders, and the declared order made no difference whatsoever.

### 2.5 - Fan-out against a quota
`days/day-54-sequential-parallel-loop/parts/02-at-the-same-time/2.5-fan-out-against-a-quota.md` · level `production` · ids ADK-36

max_concurrency on the Workflow caps how many nodes may be in flight at once, and on a free tier measured in requests per minute it is not a tuning knob — it is the difference between six branches and six 429s.

### 3.1 - A loop is an edge that goes back
`days/day-54-sequential-parallel-loop/parts/03-around-again/3.1-a-loop-is-an-edge-that-goes-back.md` · level `foundation` · ids ADK-37

There is no loop construct: a loop is an ordinary edge pointing at a node the graph has already visited, plus a route on it so a node upstream can decide, each time round, whether that edge is taken.

### 3.2 - The cycle the runtime refuses
`days/day-54-sequential-parallel-loop/parts/03-around-again/3.2-the-cycle-the-runtime-refuses.md` · level `working` · ids ADK-37

The graph runtime rejects a back edge with no route on it, at construction time, with the message Unconditional cycle detected — and that single check is the only structural promise it makes about loops.

### 3.3 - What survives one turn of the loop
`days/day-54-sequential-parallel-loop/parts/03-around-again/3.3-what-survives-one-turn-of-the-loop.md` · level `working` · ids ADK-37

Session state carries across an iteration; the node input does not carry what you expect, because on the way back round it holds the critic's output rather than the writer's previous draft.

### 3.4 - The loop that never ends
`days/day-54-sequential-parallel-loop/parts/03-around-again/3.4-the-loop-that-never-ends.md` · level `production` · ids ADK-37

A routed cycle whose route never changes runs forever: the graph builds, no exception is raised, and in this lab the writer had run twenty-one times before something outside the runtime stopped it — because nothing inside the runtime was going to.

### 3.5 - The guard you write yourself
`days/day-54-sequential-parallel-loop/parts/03-around-again/3.5-the-guard-you-write-yourself.md` · level `production` · ids ADK-37

Three lines in the deciding node — count the rounds in state, force the exit route at a cap, record why it stopped — turn the runaway of [3.4](3.4-the-loop-that-never-ends.md) into a run that ends, says it gave up, and hands the ticket to a human.

### 4.1 - The shape of the triage flow
`days/day-54-sequential-parallel-loop/parts/04-where-they-meet/4.1-the-shape-of-the-triage-flow.md` · level `working` · ids ADK-35, ADK-36, ADK-37

The triage graph is a chain with a fan-out in the middle and a loop at the end — and running it end to end exposes a bug none of the three shapes shows on its own: the second time round the loop, the drafting node has lost the research.

### 4.2 - The branch that took everyone down with it
`days/day-54-sequential-parallel-loop/parts/04-where-they-meet/4.2-the-branch-that-took-everyone-down-with-it.md` · level `production` · ids ADK-36

When one branch of a fan-out raises, the whole fan-out fails: the measured log shows all three branches started and none of them finished, so degrading gracefully is something a branch does to itself, not something the join does for it.

### 4.3 - Retries inside a loop multiply
`days/day-54-sequential-parallel-loop/parts/04-where-they-meet/4.3-retries-inside-a-loop-multiply.md` · level `production` · ids ADK-37

A node that retries three times inside a loop that runs three rounds makes nine calls, not three and not six — measured — so the cap on the loop and the retry budget on the node have to be chosen together or they multiply behind your back.

### 5.1 - The three classes that still import
`days/day-54-sequential-parallel-loop/parts/05-the-old-shapes/5.1-the-three-classes-that-still-import.md` · level `production` · ids ADK-35, ADK-36, ADK-37

SequentialAgent, ParallelAgent and LoopAgent are the 1.x way of writing this day's three shapes; in google-adk==2.7.1 they still import, still construct, and carry a deprecation warning that is printed when you build one in a script and completely silent when you build one inside a module — which is where real code builds things.

### 5.2 - Reading a 1.x tutorial without being taken in
`days/day-54-sequential-parallel-loop/parts/05-the-old-shapes/5.2-reading-a-1x-tutorial-without-being-taken-in.md` · level `production` · ids ADK-35, ADK-36, ADK-37

Most of a 1.x example still translates line for line, and the three places it does not are the join, the loop's cap, and event handling — so the skill is knowing which three paragraphs to distrust rather than discarding the whole page.

## Papers - read after the parts

### doi:10.1145/359576.359585 - Communicating sequential processes
`days/day-54-sequential-parallel-loop/papers/01-communicating-sequential-processes.md`

This paper proposes that a concurrent program should be written as independent sequential processes that interact only by explicitly named communication, and gives three ways to combine them — one after another, together, and repeatedly — which are the three shapes this day just built.


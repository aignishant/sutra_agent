# Day 53 - The graph Workflow Runtime — nodes, edges, the 2.x composition model

IDs closed: ADK-32, ADK-34, ADK-33 · source: `days/day-53-graph-workflow-runtime/`

## Parts

### 1.1 - A node is a unit of work, not a unit of intelligence
`days/day-53-graph-workflow-runtime/parts/01-the-node/1.1-a-node-is-a-unit-of-work.md` · level `foundation` · ids ADK-32

A node is one step of your process with a name, and the runtime's only promise about it is "I will run this once, when its turn comes, and I will tell everyone what came out" — which is why a two-line function that strips whitespace is exactly as much a node as an agent that calls a model.

### 1.2 - The four things that can be a node
`days/day-53-graph-workflow-runtime/parts/01-the-node/1.2-the-four-things-that-can-be-a-node.md` · level `foundation` · ids ADK-32, ADK-34

A function, an agent, a tool and an entire workflow are all nodes — isinstance(x, BaseNode) is True for every one of them — and that single fact is the whole 2.x composition model, because it means an agent is one kind of node rather than the thing everything else has to hang off.

### 1.3 - What arrives at a node
`days/day-53-graph-workflow-runtime/parts/01-the-node/1.3-what-arrives-at-a-node.md` · level `working` · ids ADK-32

Exactly two things reach a node: node_input, which is whatever the previous node put in its output, and ctx.state, which is the session's shared notebook — and the difference between them is that node_input is handed over and state is looked up.

### 1.4 - What leaves a node
`days/day-53-graph-workflow-runtime/parts/01-the-node/1.4-what-leaves-a-node.md` · level `working` · ids ADK-32

One Event can carry three separate things — output travels to the next node, message is shown to the human, and route decides which edge is taken — and confusing the first two is why a graph sometimes prints a perfect answer and passes nothing on.

### 1.5 - Say it as you go, never collect and return
`days/day-53-graph-workflow-runtime/parts/01-the-node/1.5-say-it-as-you-go.md` · level `working` · ids ADK-32

A node that yields emits each event the moment it happens, and a node that builds a list and returns it emits nothing until it is completely finished — measured here as a first sign of life at 0.41s against 1.24s for identical work, which is why trap #3 says yield, don't append.

### 2.1 - An edge is what happens next
`days/day-53-graph-workflow-runtime/parts/02-the-edge/2.1-an-edge-is-what-happens-next.md` · level `foundation` · ids ADK-33

An edge is a written-down promise that when one node finishes, another one starts and receives its output — and because it is written down in one list rather than scattered through the nodes, you can read the whole process without reading any of the code that does the work.

### 2.2 - The chain that is a list of edges
`days/day-53-graph-workflow-runtime/parts/02-the-edge/2.2-the-chain-that-is-a-list-of-edges.md` · level `working` · ids ADK-33

("START", intake, classify, draft) is not a special "sequence" feature — it expands into exactly the three Edge objects you would have written by hand, which the lab proves by comparing the two graphs and getting same edges? True.

### 2.3 - A label, not an address
`days/day-53-graph-workflow-runtime/parts/02-the-edge/2.3-a-label-not-an-address.md` · level `working` · ids ADK-33

A node emits a label — route="incident" — and the graph, not the node, decides which edge that label opens; the node never names its successor, which is what lets you rewire the whole flow without touching the classifier.

### 2.4 - Two shops at once, and the wait at the door
`days/day-53-graph-workflow-runtime/parts/02-the-edge/2.4-two-shops-at-once.md` · level `working` · ids ADK-33

A tuple destination fans work out to several nodes that then run at the same time — measured here as 0.45s against 0.84s for two searches — and a JoinNode is what waits for all of them and hands the next node a dictionary keyed by which branch produced what.

### 2.5 - On the edge or in the register
`days/day-53-graph-workflow-runtime/parts/02-the-edge/2.5-on-the-edge-or-in-the-register.md` · level `working` · ids ADK-33

Put a value on the edge when the very next node consumes it, and in ctx.state when a later node needs it but the nodes in between do not — because anything you put on the edge becomes a parameter every node along the way has to carry and none of them can be reused without.

### 3.1 - Tested before the mains go on
`days/day-53-graph-workflow-runtime/parts/03-the-graph-is-checked/3.1-tested-before-the-mains-go-on.md` · level `working` · ids ADK-33, ADK-34

The graph is validated when you construct the Workflow, not when you run it — six different mistakes are rejected before a single node executes, and every one of them would otherwise have been a production incident rather than a startup error.

### 3.2 - Both waiting for the other to leave
`days/day-53-graph-workflow-runtime/parts/03-the-graph-is-checked/3.2-both-waiting-for-the-other-to-leave.md` · level `working` · ids ADK-33

A cycle in the graph is allowed only if at least one edge in it carries a route, because a loop made entirely of unconditional edges has no way to stop — and the framework refuses to build one, naming the exact cycle it found.

### 3.3 - The switch that turns nothing on
`days/day-53-graph-workflow-runtime/parts/03-the-graph-is-checked/3.3-the-switch-that-turns-nothing-on.md` · level `working` · ids ADK-33

A node that is half-wired — it has an outgoing edge and nothing leading to it — is rejected at construction; a node that is not wired at all is not in the graph, produces no error of any kind, and the work it was written to do simply never happens.

### 4.1 - One secretary, or one register
`days/day-53-graph-workflow-runtime/parts/04-composition/4.1-one-secretary-or-one-register.md` · level `working` · ids ADK-34

In a tree every step has exactly one parent, so the same step cannot appear in two places — the framework says so out loud with "Agent classify already has a parent agent" — while in a graph a node is reached by however many edges point at it, which is why trap #1 replaced the tree with the graph.

### 4.2 - The textbook with the wrong edition
`days/day-53-graph-workflow-runtime/parts/04-composition/4.2-the-textbook-with-the-wrong-edition.md` · level `production` · ids ADK-34

Most ADK material on the internet is 1.x, and this part is the translation drill: given a SequentialAgent with sub_agents, name what is wrong with it under trap #1 and write the graph it becomes — because you will meet ten of these before you meet one written for 2.x.

### 4.3 - The bus pass with a date on it
`days/day-53-graph-workflow-runtime/parts/04-composition/4.3-the-bus-pass-with-a-date-on-it.md` · level `production` · ids ADK-34

SequentialAgent, ParallelAgent and LoopAgent still work in 2.7.1 and each one now says "deprecated in favor of Workflow and will be removed in a future version" on construction — which is a date, not an opinion, and the right response is to port rather than to silence the warning.

### 4.4 - The floor plan by the lift
`days/day-53-graph-workflow-runtime/parts/04-composition/4.4-the-floor-plan-by-the-lift.md` · level `production` · ids ADK-34

Because composition is a list of edges rather than a nesting of objects, the graph is data you can read at runtime — flow.graph.edges — which means the diagram in your documentation can be generated from the running system instead of drawn by hand and left to rot.

### 5.1 - Five desks, one form
`days/day-53-graph-workflow-runtime/parts/05-the-first-graph/5.1-five-desks-one-form.md` · level `working` · ids ADK-32, ADK-33, ADK-34

Everything so far, assembled: a nine-node triage graph — intake, classify, two searches, a join, draft, review, and a human queue — that runs three different tickets down three different paths, with zero model calls, because the graph is a scheduler and a scheduler can be watched for free.

### 5.2 - The cycle that finished early
`days/day-53-graph-workflow-runtime/parts/05-the-first-graph/5.2-the-cycle-that-finished-early.md` · level `production` · ids ADK-33, ADK-34

Two one-line mistakes — a route label in the wrong case, and a join whose predecessor was never triggered — each produce a graph that validates, runs, exits 0, and does half the work: two events where there should be five, with no exception and no failed check anywhere.

### 6.1 - The whistle that was taken off
`days/day-53-graph-workflow-runtime/parts/06-in-production/6.1-the-whistle-that-was-taken-off.md` · level `production` · ids ADK-32

Trap #4: an exception inside a node propagates out through the runtime and stops the run, with the node's frames in the traceback — and the 1.x habit of catching it and returning a friendly string turns a stopped run into a wrong answer that no retry, no callback and no alert will ever see.

### 6.2 - The labelled fuse box
`days/day-53-graph-workflow-runtime/parts/06-in-production/6.2-the-labelled-fuse-box.md` · level `production` · ids ADK-34

A graph is reviewable when a person who has never seen it can read the edge list and predict what a given input will do — which means node names that say what they do, one place where branching happens, a DEFAULT_ROUTE on every routing node, and a sub-workflow the moment the picture stops fitting on a screen.

## Papers - read after the parts

### doi:10.1145/1272998.1273005 - Dryad — the job is a graph, and the graph is the program
`days/day-53-graph-workflow-runtime/papers/01-dryad.md`

It argued that a distributed job should be written as a directed acyclic graph whose vertices are ordinary sequential programs and whose edges are channels, so that the programmer never writes concurrency code and the graph — a first-class object the program builds — is what expresses dependency and parallelism.


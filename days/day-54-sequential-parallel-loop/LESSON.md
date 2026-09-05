---
day: 54
phase: 8
phase_name: "Workflows and multi-agent"
title: "Sequential, parallel & loop patterns"
ids: ["ADK-35", "ADK-36", "ADK-37"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 54 — Sequential, parallel and loop patterns

> **Yesterday (Day 53):** the graph Workflow Runtime arrived. A node is the unit of composition, an
> edge is the arrow between two of them, an agent is one kind of node, and trap #1 was named: 2.x
> composes in a graph where 1.x composed in a tree of agents.
> **Today:** the three shapes you build out of nodes and edges — one after another, all at once, and
> round again — each measured on a real run, then put together into the triage graph so the bug that
> only appears where they meet has somewhere to appear. The day spends **zero** model calls.
> **Tomorrow (Day 55):** delegation and transfer, and an agent used as a tool — which is what goes
> *inside* the nodes these shapes arrange.

---

## §1 Where we are

Day 53 handed you a vocabulary and one worked example. A graph is nodes and edges; the edges are
data; the runtime walks them. Today that vocabulary has to become three sentences you can say
without looking anything up: *these steps happen in order*, *these steps happen together*, *this step
happens again*.

Here is the day as a scene. Somebody comes into a hospital outpatient department with a swollen
ankle. Reception takes their details **in order** — name, then card, then department — because the
third question has no meaning until the first two are answered. The triage nurse then sends them
three ways **at once**: bloods on the second floor, an X-ray in the imaging wing, a form to fill in
while they wait, because none of those three is waiting on another. And then the doctor reads all
three results, writes something, looks at it, and says *"before I write this up, one more test"* —
and that **goes round** as many times as it needs to, which is a number nobody knew at the start of
the morning.

Three shapes, one visit, and everybody in the building knows which corridor is which.

The thing that makes today a lab rather than a tour is that each of those shapes has a sharp edge,
and the edges are not where you would guess. The order in a chain is load-bearing in a way that
produces plausible wrong answers rather than errors. A fan-out starts its branches in a fixed order
and finishes them in one that changed five times across eight runs of the same graph. And a loop is
bounded by exactly nothing: the runtime refuses to build a cycle with no conditional edge, and then
lets a conditional one run until something outside the process stops it — twenty-one passes in this
day's lab, and forty-one when the observer's patience was doubled.

Then the three go into one graph, and a bug appears that none of them shows alone: on the second
trip round the loop, the drafting node has lost its research. Every number in this day came from a
run, and that one came from a run that was supposed to be the tidy summary at the end.

---

## §2 The map

Nineteen parts in five sections, then one paper. Sections 1, 2 and 3 are one curriculum ID each —
`ADK-35`, `ADK-36`, `ADK-37` — because each of the three shapes is one mental model. Section 4 is the
synthesis, where all three run in one graph. Section 5 is trap #1: the three 1.x classes that
expressed exactly these shapes, and how to read the material still written against them.

### Section 1 — one after another (`ADK-35`)

*What "in order" actually promises, and what it does not.*

| # | Part | Answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The order you declare is the order you get](parts/01-one-after-another/1.1-the-order-you-declare-is-the-order-you-get.md) | What is a chain, and what does each node receive? | foundation |
| 1.2 | [What the next stage can see](parts/01-one-after-another/1.2-what-the-next-stage-can-see.md) | Node input or session state — which, and how does the runtime decide? | working |
| 1.3 | [Why calling them in order is not a workflow](parts/01-one-after-another/1.3-why-calling-them-in-order-is-not-a-workflow.md) | Nested calls do the same work. What does the graph buy? | working |
| 1.4 | [The stage that refuses to run](parts/01-one-after-another/1.4-the-stage-that-refuses-to-run.md) | Which five mistakes are rejected before anything runs? | production |

### Section 2 — at the same time (`ADK-36`)

*Fanning out, joining back, and the three things concurrency changes underneath you.*

| # | Part | Answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Three branches from one edge](parts/02-at-the-same-time/2.1-three-branches-from-one-edge.md) | What does a fan-out do, and how many times does the next node run? | foundation |
| 2.2 | [The node that waits for everyone](parts/02-at-the-same-time/2.2-the-node-that-waits-for-everyone.md) | What is a `JoinNode` and what does it hand on? | working |
| 2.3 | [The order you cannot rely on](parts/02-at-the-same-time/2.3-the-order-you-cannot-rely-on.md) | Which ordering is guaranteed, and which one is a trap? | working |
| 2.4 | [Two branches, one state key](parts/02-at-the-same-time/2.4-two-branches-one-state-key.md) | Two concurrent writes to one key — which survives? | production |
| 2.5 | [Fan-out against a quota](parts/02-at-the-same-time/2.5-fan-out-against-a-quota.md) | What does `max_concurrency` bound, and what does it not? | production |

### Section 3 — around again (`ADK-37`)

*A loop is an edge and a decision. The runtime supplies the edge and none of the decision.*

| # | Part | Answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A loop is an edge that goes back](parts/03-around-again/3.1-a-loop-is-an-edge-that-goes-back.md) | How do you write a loop when there is no loop construct? | foundation |
| 3.2 | [The cycle the runtime refuses](parts/03-around-again/3.2-the-cycle-the-runtime-refuses.md) | What does the runtime guarantee about cycles, exactly? | working |
| 3.3 | [What survives one turn of the loop](parts/03-around-again/3.3-what-survives-one-turn-of-the-loop.md) | On pass two, what is in the writer's input? | working |
| 3.4 | [The loop that never ends](parts/03-around-again/3.4-the-loop-that-never-ends.md) | **The deliberate failure.** What stops a routed cycle? | production |
| 3.5 | [The guard you write yourself](parts/03-around-again/3.5-the-guard-you-write-yourself.md) | What are the three parts of a loop guard? | production |

### Section 4 — where they meet (all three IDs)

*One graph with all three shapes in it, and the bug that needs all three to exist.*

| # | Part | Answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The shape of the triage flow](parts/04-where-they-meet/4.1-the-shape-of-the-triage-flow.md) | What does Day 58's graph look like, and what breaks on pass two? | working |
| 4.2 | [The branch that took everyone down with it](parts/04-where-they-meet/4.2-the-branch-that-took-everyone-down-with-it.md) | One branch raises — what happens to its siblings? | production |
| 4.3 | [Retries inside a loop multiply](parts/04-where-they-meet/4.3-retries-inside-a-loop-multiply.md) | Four attempts, three rounds — how many calls? | production |

### Section 5 — the old shapes (trap #1)

*The 1.x classes for these three shapes still import. What that costs you, and how to read a page written against them.*

| # | Part | Answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The three classes that still import](parts/05-the-old-shapes/5.1-the-three-classes-that-still-import.md) | What do `SequentialAgent`, `ParallelAgent` and `LoopAgent` map to? | production |
| 5.2 | [Reading a 1.x tutorial without being taken in](parts/05-the-old-shapes/5.2-reading-a-1x-tutorial-without-being-taken-in.md) | Which three junctions moved, and which one fails silently? | production |

### Papers — read after the parts

Principle 4 at the scale of a day: build the mechanism by hand, then read the proposal. The three
shapes above are this paper's three combinators, and its central argument is the one
[2.4](parts/02-at-the-same-time/2.4-two-branches-one-state-key.md) reached by measurement.

| # | Paper | Identifier |
| --- | --- | --- |
| 01 | [Communicating sequential processes](papers/01-communicating-sequential-processes.md) | `doi:10.1145/359576.359585` |

---

## §3 Setup — run this

```bash
mkdir -p days/day-54-sequential-parallel-loop/lab/papers/communicating-sequential-processes
cd days/day-54-sequential-parallel-loop/lab

touch _flow.py _research.py
touch chain.py visible.py plain.py refuse.py
touch fanout.py join.py stall.py order.py race.py concurrency.py
touch loop.py cycle.py carry.py runaway.py guard.py
touch triage.py blast.py retry.py
touch oldshapes.py _oldshapes_module.py gate.py
touch papers/communicating-sequential-processes/csp.py
touch papers/communicating-sequential-processes/demo.py

touch ../../../sutra/flow.py ../../../tests/test_flow.py
```

**No package is added today.** `google-adk` is already pinned at `2.7.1` (`docs/PACKAGES.md`, row
dated 2026-08-26), and everything in this day comes from `google.adk.workflow`,
`google.adk.agents`, `google.adk.events` and the standard library. `git diff pyproject.toml uv.lock`
should be empty when you finish.

Confirm the symbols exist before you write against them:

```bash
uv run python -c "from google.adk.workflow import START, Edge, FunctionNode, JoinNode, NodeTimeoutError, RetryConfig, Workflow, DEFAULT_ROUTE; print('ok', DEFAULT_ROUTE)"
```

---

## §4 Build brief

The lab is teaching material and is given whole. This is the part you write, in `sutra/flow.py`.

**`sutra/flow.py`** — three builder functions, each returning a `Workflow`:

```python
MAX_ROUNDS = 3  # TODO(me): the cap. Part 3.5 says why this exists and where it is enforced.


def research_graph() -> Workflow:
    """Fan out to three lookups, join them, hand the drafter one dict.

    TODO(me): three branch functions over sutra.retrieval (Day 49) and the knowledge base.
    TODO(me): a JoinNode, so the node after it runs once and not three times (part 2.2).
    TODO(me): max_concurrency, chosen against the free-tier floor in Addendum 02 (part 2.5).
    TODO(me): each branch writes its OWN state key, never a shared one (part 2.4).
    """


def review_loop() -> Workflow:
    """Draft, review, and go round until the critic is satisfied or MAX_ROUNDS is reached.

    TODO(me): a routed back edge, and a second routed edge out (part 3.1).
    TODO(me): the round counter in session state, not in a local or a global (part 3.3).
    TODO(me): the guard: cap, forced exit route, and a record of WHY it stopped (part 3.5).
    TODO(me): give the cap its own route to its own node, per part 3.5's "When it breaks".
    """


def triage_graph() -> Workflow:
    """The whole shape: intake, classify, research, draft, review, send.

    TODO(me): compose the two above into one edge list (part 4.1).
    TODO(me): the drafter must still have the research on pass two. Part 4.1 measured what
              happens when it does not.
    """
```

**`tests/test_flow.py`** — at least four tests, and one of them has to be able to go red for the
right reason:

- `research_graph()` constructs, and its graph holds a `JoinNode`.
- `review_loop()` stops at `MAX_ROUNDS` when the critic never accepts, and the run records that the
  cap is why.
- `triage_graph()` runs end to end with stub nodes and **loops at least twice** — part 4.1 exists
  because a test that never loops twice is not testing the loop.
- **Break it on purpose:** remove the cap from `review_loop`, watch the test hang or blow past its
  bound, put it back. Write down what the failure looked like.

---

## §5 The eval that must be able to fail

```bash
uv run python days/day-54-sequential-parallel-loop/lab/gate.py; echo "exit: $?"
```

Six checks, and it is **red right now**, before you write anything:

```text
gate: 1 finding(s)
  1. sutra/flow.py does not import yet: write it (the hub build brief), then run this again.
exit: 1
```

Once the module imports, the remaining five findings are about the things this day measured: a
`research_graph` with no `max_concurrency`, a `research_graph` with no `JoinNode`, a `review_loop`
with no routed edge, and a `review_loop` with no `MAX_ROUNDS`. Each finding names the part that
explains it.

The gate goes green only when all six pass. It is a check that can go red because it *is* red, today,
and you can watch each finding disappear.

---

## §6 Request budget

**Free-tier Gemini Flash**, roughly 10–15 requests per minute per project (Addendum 02 §4; ten is the
floor this day budgets against).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all twenty-one lab scripts, every flag | **0** |
| the paper demo, both arms, 400 runs | **0** |
| `sutra/flow.py`, the gate and the four tests | **0** |
| **Total planned** | **0 of the day's quota** |

**Zero, and today the zero is structural rather than thrifty.** Every node in this day is a plain
Python function. A chain is three calls, a fan-out is an event loop, a join is a dictionary, and a
loop is an edge. None of that needs a model, and running it two hundred times to see a scheduling
order change costs nothing — which is the only reason
[2.3](parts/02-at-the-same-time/2.3-the-order-you-cannot-rely-on.md) could run the same graph in
eight separate processes and find five different orderings.

Tomorrow's nodes contain agents and the arithmetic changes completely. Part
[4.3](parts/04-where-they-meet/4.3-retries-inside-a-loop-multiply.md) is the day you learn to do
that multiplication before you find out.

**Cost: $0.**

---

## §7 Traps

- **Trap #1 (plan §5.1), and it is this day's whole subject.** 1.x composed with `SequentialAgent`,
  `ParallelAgent` and `LoopAgent`; 2.x composes with nodes and edges. All three classes still import
  in 2.7.1, still construct, and warn only when built in `__main__` (5.1).
- **A wrong chain order produces a plausible answer, not an error.** Swapping the normaliser and the
  classifier turned every ticket into `other` and nothing raised (1.1).
- **A parameter not called `node_input` is looked up in session state**, and without a default the
  node refuses to run: `Missing value for parameter "ticket_id" ... not found in state` (1.2, 1.4).
- **Five structural mistakes are rejected at construction**, all beginning `Graph validation failed`
  — unreachable nodes, duplicate names, duplicate edges, an edge into `START`, a route out of
  `START` (1.4).
- **A plain node downstream of three branches runs three times**, once per branch. Only a `JoinNode`
  runs once with all of them (2.1, 2.2).
- **A fan-out with nothing downstream fails at the end of the run**: `multiple terminal nodes
  produced output (3). A workflow must have at most one terminal output.` (2.1).
- **A routed edge into a join whose route stops matching means the join never fires** — no
  exception, exit code zero, one `WARNING` line (2.2).
- **Branch start order is deterministic; join key order is not.** Eight runs in one process gave one
  ordering; eight separate processes gave five (2.3).
- **Two branches writing one state key is last-writer-wins, and the declared order is irrelevant.**
  Both arrangements produced `'low'` (2.4).
- **`max_concurrency` defaults to `None`.** Six branches meant six simultaneous calls; at `--limit 2`
  it was two (2.5).
- **The runtime rejects an unrouted cycle and bounds a routed one not at all.** adk.dev says so
  outright: *"A graph cycle is not bounded automatically."* Twenty-one passes and counting (3.2,
  3.4).
- **On the way back round a loop, `node_input` is the deciding node's output**, not the previous
  draft — and on the *first* pass it is the user's `Content`, not a string (3.3).
- **A loop guard has three parts and the third is the one left out**: the counter, the forced exit,
  and the record of why it stopped (3.5).
- **One branch raising cancels its siblings mid-flight.** All three logged `start`; none logged `end`
  (4.2).
- **Retries multiply with loop rounds and are invisible in the event stream.** Four attempts inside
  three rounds was nine calls and six events (4.3).
- **A 1.x `ParallelAgent` had no join to translate**, so the join is the thing you must know to add
  (5.2).

---

## §8 Verify before you code

Fetched on **2026-09-05**, the day this was written:

- <https://adk.dev/graphs/> — graph-based agent workflows: the `edges=` list, chain tuples, fan-out
  tuples ("Values can be a single node or a tuple of nodes (fan-out)"), `"START"`, and the join
  proceeding "only after all its upstream nodes have provided an Event output".
- <https://adk.dev/graphs/routes/> — how a node emits a route (`return Event(route="RUN_TASK_C")`),
  `DEFAULT_ROUTE` as the catch-all, and the back edge as the way to build a cycle. Source of the
  sentence part 3.4 is built on: **"A graph cycle is not bounded automatically. Make sure the exit
  condition eventually becomes true."**
- <https://adk.dev/workflows/> and <https://adk.dev/graphs/data-handling/> — the workflow runtime
  overview and how data moves between nodes.
- <https://api.crossref.org/works/10.1145/359576.359585> — the CrossRef record for this day's paper,
  which returned *Communicating sequential processes*, *Communications of the ACM* 21(8), 666–677,
  1978. The ACM Digital Library page returns HTTP 403 to an unauthenticated fetch.

And against the installed package, `google-adk==2.7.1`:

```bash
uv run python -c "import google.adk; print(google.adk.__version__)"
uv run python -c "from google.adk.workflow import Workflow; print(sorted(Workflow.model_fields))"
uv run python -c "from google.adk.workflow import RetryConfig; print(sorted(RetryConfig.model_fields))"
uv run python -c "from google.adk.agents import SequentialAgent; print(SequentialAgent.__doc__)"
```

The last one is worth running: the deprecation notice in part 5.1 is quoted from what that prints.

---

## §9 Say it in an interview

*"Workflow frameworks all give you the same three shapes — sequential, parallel and a loop — and I
spent a day measuring what each one actually does rather than trusting the diagram. Three things
surprised me. First, a plain node downstream of a three-way fan-out runs three times, once per
branch; you need an explicit join node to get one run with all three results, and forgetting it does
not fail, it just drafts an answer from a third of the data. Second, the order results come back in
is not stable: eight runs inside one process gave me the same ordering every time, and eight separate
processes gave me five different ones, so a positional read of a join result passes CI and fails in
production. Third, and the one I would actually flag in a design review — the runtime bounds nothing
about a loop. It refuses to build a cycle with no conditional edge, which catches the typo, and the
docs say plainly that a graph cycle is not bounded automatically. I ran a critic that always said
'revise': twenty-one passes, no complaint, and it stopped only because my harness raised. So the cap
is mine to write, it lives in the deciding node reading a counter in session state, and it records
why it stopped — otherwise a loop that gave up looks exactly like a loop that succeeded. And it goes
in the node, not the prompt, because a rule the model is asked to follow is not a bound."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — which means each part read, its check-yourself
command actually run, and its out-loud question answered without scrolling. Then `./m depth 54` green,
`./m check` green, and `./m done 54`.

Not when you have read nineteen files. When you can draw the triage graph from memory, say what
arrives at the drafter on pass two, and name what stops the loop.

---

## §11 Ledger & commit

**`docs/PROGRESS.md` — append this row** (fill in the hash after committing):

```markdown
| 54 | 2026-09-05 | ADK-35, ADK-36, ADK-37 | 19 (+1 paper) | <hash> | ⚠️ |
```

**`docs/PACKAGES.md` — no new rows today.** No package is added and no pin moves. `google-adk==2.7.1`
already has its row, dated 2026-08-26, and every symbol this day uses was verified against that
installed version and against adk.dev on 2026-09-05.

**`docs/PAPERS.md` — one new row:**

```markdown
| Communicating sequential processes | doi:10.1145/359576.359585 | 1978 | 2026-09-05 | 54 | `days/day-54-sequential-parallel-loop/papers/01-communicating-sequential-processes.md` |
```

**`docs/SKILL_PROVENANCE.md` — no new rows today.**

**Git commit message:**

```
day 54: sequential, parallel and loop patterns — closes ADK-35, ADK-36, ADK-37
```

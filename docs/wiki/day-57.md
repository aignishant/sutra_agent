# Day 57 - Multi-agent design — orchestrator, Writer↔Critic

IDs closed: AG-19, AG-20, ADK-40 · source: `days/day-57-orchestrator-and-critic/`

## Parts

### 1.1 - One agent is usually the right answer
`days/day-57-orchestrator-and-critic/parts/01-when-to-split/1.1-one-agent-is-usually-the-right-answer.md` · level `foundation` · ids AG-19

A multi-agent system is a cost you pay for a specific reason, and the reason is never "one agent felt like a lot" — so the first honest question of this day is why you would not simply write better instructions for the agent you already have.

### 1.2 - What a second duty costs the first
`days/day-57-orchestrator-and-critic/parts/01-when-to-split/1.2-what-a-second-duty-costs-the-first.md` · level `working` · ids AG-19

Adding a responsibility to an agent does not add a responsibility — it trades one, silently, and the rule that goes missing is chosen by position in the instruction block rather than by importance.

### 1.3 - The three questions that decide a split
`days/day-57-orchestrator-and-critic/parts/01-when-to-split/1.3-the-three-questions-that-decide-a-split.md` · level `working` · ids AG-19

A division of labour is worth its extra requests when the two halves need different judgement, different evidence, or different consequences — and a split that satisfies none of the three has bought you a diagram.

### 2.1 - An orchestrator owns the flow, not the work
`days/day-57-orchestrator-and-critic/parts/02-the-orchestrator/2.1-an-orchestrator-owns-the-flow-not-the-work.md` · level `foundation` · ids AG-19

An orchestrator's whole job is deciding what happens next, and the moment it also does some of the work it starts carrying everybody's context — which on the desk's own fixture is 781 tokens across a run instead of 154.

### 2.2 - Orchestrator or router — the difference is whether it comes back
`days/day-57-orchestrator-and-critic/parts/02-the-orchestrator/2.2-orchestrator-or-router.md` · level `working` · ids AG-19

A router picks who handles the request and stops existing; an orchestrator picks who handles the next step and is still there afterwards — so a router can run one stage and an orchestrator can run five.

### 2.3 - Two descriptions that overlap are one bug
`days/day-57-orchestrator-and-critic/parts/02-the-orchestrator/2.3-two-descriptions-that-overlap-are-one-bug.md` · level `working` · ids AG-19

An orchestrator chooses between specialists using their descriptions and nothing else, so two descriptions that could both fit a request are not a documentation problem — on the desk's own ten requests they route 4 correctly instead of 9, and every single one of the ten is a coin toss.

### 2.4 - The orchestrator's own bill
`days/day-57-orchestrator-and-critic/parts/02-the-orchestrator/2.4-the-orchestrators-own-bill.md` · level `production` · ids AG-19

The orchestrator runs on every step of every request, so it is the component whose cost multiplies fastest — and on a five-stage flow it is not one call per ticket, it is five, before any actual work has been done.

### 3.1 - A check you never ran cannot fail
`days/day-57-orchestrator-and-critic/parts/03-the-critic/3.1-a-check-you-never-ran-cannot-fail.md` · level `foundation` · ids AG-20

A writer asked whether its own draft is good reports on the rules it was thinking about, so every rule it never held in mind comes back clean — and on the desk's fixture that shipped five drafts out of five with fifteen of twenty-five standard lines failing.

### 3.2 - A critic needs something it can fail against
`days/day-57-orchestrator-and-critic/parts/03-the-critic/3.2-a-critic-needs-something-it-can-fail-against.md` · level `working` · ids AG-20

Feedback that does not name a rule changes nothing — four different pieces of thoughtful criticism moved zero rubric lines on the desk's fixture, and the one that named three rules moved all three.

### 3.3 - What the critic is allowed to see
`days/day-57-orchestrator-and-critic/parts/03-the-critic/3.3-what-the-critic-is-allowed-to-see.md` · level `working` · ids AG-20

Show the critic the writer's reasoning and the reasoning becomes the checklist: on the desk's own fixture the same failing draft goes from revise to accept with nothing changed except what the critic was allowed to read.

### 3.4 - The verdict is a list, not a paragraph
`days/day-57-orchestrator-and-critic/parts/03-the-critic/3.4-the-verdict-is-a-list-not-a-paragraph.md` · level `working` · ids AG-20

A critic's output is read by a machine before it is read by a person, so it has to be a decision and a list of named rules — write it as English and something has to guess, and "This is not something I would reject" is guessed as a rejection.

### 4.1 - A critic will always find something
`days/day-57-orchestrator-and-critic/parts/04-stopping/4.1-a-critic-will-always-find-something.md` · level `working` · ids AG-20

"Is there anything wrong with this?" is a question with no stopping answer, so a critic asked it keeps saying yes — the desk's fixture satisfied its whole standard on round 2 and the loop was still running at round 25, having spent 50 model calls.

### 4.2 - The brake belongs to the graph
`days/day-57-orchestrator-and-critic/parts/04-stopping/4.2-the-brake-belongs-to-the-graph.md` · level `production` · ids AG-20

A limit the critic is asked to observe is advice, and the critic is the thing that will not stop — the same limit moved into the loop that counts rounds turns 50 model calls into 6.

### 4.3 - The third verdict
`days/day-57-orchestrator-and-critic/parts/04-stopping/4.3-the-third-verdict.md` · level `production` · ids AG-20

With only accept and revise, a brake that fires has to pick one of them, and it picks accept — so the draft that could not meet the standard is sent to the customer and the run is logged as a success.

### 5.1 - Did the critic actually help?
`days/day-57-orchestrator-and-critic/parts/05-does-it-help/5.1-did-the-critic-actually-help.md` · level `production` · ids AG-20

The only honest defence of a second agent is a before-and-after number on the same work: the desk's pair took 10 rubric lines out of 25 to 24 out of 25 for 23 model calls, and the same loop with a critic that approves everything moved nothing while still spending 10.

### 5.2 - What the pair costs in requests
`days/day-57-orchestrator-and-critic/parts/05-does-it-help/5.2-what-the-pair-costs-in-requests.md` · level `production` · ids AG-20

On this project quality is bought with requests, and the reviewed reply costs four of them against one — so a day's free-tier allowance is 250 unreviewed replies or 62 reviewed ones, and that trade is the decision, not a footnote to it.

### 6.1 - A workflow is a node
`days/day-57-orchestrator-and-critic/parts/06-the-adk-box/6.1-a-workflow-is-a-node.md` · level `working` · ids ADK-40

In ADK 2.x a Workflow is itself a BaseNode, so the whole Writer↔Critic loop drops into a bigger graph as one node — the outer graph has three nodes and one of them happens to contain a cycle.

### 6.2 - The verdict steers the edges
`days/day-57-orchestrator-and-critic/parts/06-the-adk-box/6.2-the-verdict-steers-the-edges.md` · level `working` · ids ADK-40

The critic returns an Event carrying a route, and the runtime matches that route against the edges leaving the node — so the branch is chosen by a value the critic produced, and no orchestration call is spent asking a model which way to go.

### 6.3 - What escapes the box
`days/day-57-orchestrator-and-critic/parts/06-the-adk-box/6.3-what-escapes-the-box.md` · level `production` · ids ADK-40

Nesting hides the structure, not the events: the outer graph declares three nodes and the run emits seven events, five of them from inside the box, each carrying a path like reply@1/draft_review@1/critic@2 that says exactly where it came from and how many times.

### 7.1 - The critic that approves everything
`days/day-57-orchestrator-and-critic/parts/07-failure-lab/7.1-the-critic-that-approves-everything.md` · level `production` · ids AG-20

A critic that accepts every draft is the most expensive component you can own: it spends ten model calls across five replies, moves nothing, and turns every dashboard green — because approval rate, round count and error rate all improve when the review stops working.

### 7.2 - The critic that rewrites
`days/day-57-orchestrator-and-critic/parts/07-failure-lab/7.2-the-critic-that-rewrites.md` · level `production` · ids AG-20

A critic that hands back its own version has become the writer, and its version is the only text in the system nobody reviews — on the desk's fixture the rewrite scores 1 of 5 against the draft's 2 of 5, and goes out anyway.

### 7.3 - Five out of five, and worse
`days/day-57-orchestrator-and-critic/parts/07-failure-lab/7.3-five-out-of-five-and-worse.md` · level `production` · ids AG-20

The rubric is a proxy for a good reply, not the thing itself — and eleven words of "Sorry. It broke because of that. We have done it. Please." score exactly the same 5 out of 5 as a reply that actually explains what happened.

### 8.1 - Six calls, one answer, one bug
`days/day-57-orchestrator-and-critic/parts/08-in-production/8.1-six-calls-one-answer-one-bug.md` · level `production` · ids AG-19, AG-20

When several agents produce one output, the output cannot tell you which of them was wrong — a writer that ignores the verdict and a critic that approves everything produce the identical reply with the identical score, and the only thing that separates them is the call count.

### 8.2 - How many heads is too many
`days/day-57-orchestrator-and-critic/parts/08-in-production/8.2-how-many-heads-is-too-many.md` · level `production` · ids AG-19

Requests grow in a straight line as you add agents and the number of description pairs that must stay distinct grows as a square — two agents is one pair to keep straight, eight agents is twenty-eight, and the second number is the one that gets you.

## Papers - read after the parts

### arXiv:2303.17651 - Self-Refine — the model that marks its own work, and when that is allowed to help
`days/day-57-orchestrator-and-critic/papers/01-self-refine.md`

One model, asked in three separate turns to write, then to say what is wrong with what it wrote, then to rewrite using that list, produces better output than the same model asked once — and the paper's own numbers say the gain comes from the feedback step, not from the extra attempts.


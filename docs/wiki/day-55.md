# Day 55 - Delegation & transfer; agent-as-tool

IDs closed: AG-16, ADK-38, ADK-39 · source: `days/day-55-delegation-and-transfer/`

## Parts

### 1.1 - One counter, and everything behind it
`days/day-55-delegation-and-transfer/parts/01-why-split-the-desk/1.1-one-counter-and-everything-behind-it.md` · level `foundation` · ids AG-16

Adding a twelfth tool to one agent does not make it twelve times more capable; it makes every request a harder choice, and the lab measures the pressure: four requests out of eight had a rival tool within one point at twelve tools, against three out of eight at four, with the twelve-tool desk picking close_ticket for "what does ticket 4521 say".

### 1.2 - The handbook that served four jobs
`days/day-55-delegation-and-transfer/parts/01-why-split-the-desk/1.2-the-handbook-that-served-four-jobs.md` · level `foundation` · ids AG-16

The second cost of one agent doing everything is not the tool list but the instruction: a handbook written to cover four jobs must state every rule conditionally, and a conditional rule is a rule the model can decide does not apply right now.

### 1.3 - Three homes for a step
`days/day-55-delegation-and-transfer/parts/01-why-split-the-desk/1.3-three-homes-for-a-step.md` · level `working` · ids AG-16

Every step in an agentic system lives in exactly one of three places — an edge the graph already drew, a call the caller makes and waits for, or a hand-over that gives the whole conversation away — and choosing between them is a design decision you make once, deliberately, per step.

### 2.1 - A call comes back
`days/day-55-delegation-and-transfer/parts/02-call-or-handover/2.1-a-call-comes-back.md` · level `foundation` · ids ADK-38, ADK-39

The whole of today rests on one difference: an agent-as-tool call returns a result to the caller, and a transfer does not return at all — and in ADK 2.7.1 that difference is one word in the sub-agent's definition, which moves it out of the transfer list and into the tool list.

### 2.2 - Who owns the turn afterwards
`days/day-55-delegation-and-transfer/parts/02-call-or-handover/2.2-who-owns-the-turn.md` · level `working` · ids ADK-38

After a call, the caller speaks last and the user never learns the specialist existed; after a transfer, the specialist speaks last and every following turn goes to it — which is why a hand-over that nobody reverses ends with three turns out of five answered by the wrong desk.

### 2.3 - Whose handbook is in force
`days/day-55-delegation-and-transfer/parts/02-call-or-handover/2.3-whose-handbook-is-in-force.md` · level `working` · ids ADK-38, AG-16

A hand-off swaps the whole rulebook — instruction, tools, model and refusals — for the specialist's own, which is the reason a split works at all and also the reason the desk's carefully tested refusal policy stops applying the moment control leaves it.

### 3.1 - The staff list behind the counter
`days/day-55-delegation-and-transfer/parts/03-the-description-routes/3.1-the-staff-list-behind-the-counter.md` · level `working` · ids ADK-38

An agent's description is not documentation: ADK pastes it verbatim into the routing agent's system prompt, under the heading Agent description:, and you can print the exact text it builds without spending a request.

### 3.2 - The clerk whose sign said all enquiries
`days/day-55-delegation-and-transfer/parts/03-the-description-routes/3.2-the-clerk-whose-sign-said-all-enquiries.md` · level `working` · ids ADK-38, AG-16

A description that claims the whole job competes for the whole job: the vague generalist scored on four of five requests that belonged to somebody else, took one of them outright, and won another on an alphabetical tie-break — and none of that is the model's fault.

### 3.3 - Writing a description that routes
`days/day-55-delegation-and-transfer/parts/03-the-description-routes/3.3-writing-a-description-that-routes.md` · level `production` · ids ADK-38, AG-16

A description that routes has four parts in a fixed order — what it does, what it returns, what it does not do, and nothing else — and the third part is the one that does the work, because a routing decision is won by being false for other people's requests.

### 4.1 - Transfer is a signal, not a call
`days/day-55-delegation-and-transfer/parts/04-transfer-in-2x/4.1-transfer-is-a-signal.md` · level `working` · ids ADK-38

transfer_to_agent is four lines long and does not transfer anything: it sets one field on the tool context's actions and returns None, and the runtime moves control afterwards by reading that field — which is exactly why a transfer has no return value to give you.

### 4.2 - The enum that refuses a stranger
`days/day-55-delegation-and-transfer/parts/04-transfer-in-2x/4.2-the-enum-that-refuses-a-stranger.md` · level `working` · ids ADK-38

Because transfer_to_agent does not validate its argument, ADK constrains it at the schema instead: the declaration the model receives carries "enum": ["kb_specialist", "archive_specialist"], turning "name a colleague" from free text into a choice from a list.

### 4.3 - Parents, peers and two switches
`days/day-55-delegation-and-transfer/parts/04-transfer-in-2x/4.3-parents-peers-and-two-switches.md` · level `working` · ids ADK-38

By default every agent in a tree can transfer to its children, its parent and its siblings, and the switch people reach for to stop a specialist bouncing work back — disallow_transfer_to_parent=True — is the one that leaves exactly the sibling-to-sibling edge that produces an infinite loop.

### 4.4 - From agent tree to node graph
`days/day-55-delegation-and-transfer/parts/04-transfer-in-2x/4.4-from-agent-tree-to-node-graph.md` · level `production` · ids ADK-38, ADK-39

This is trap #1 in its delegation form: in 1.x an agent tree was the composition layer and delegation was the only way to compose, whereas in 2.x the graph Workflow Runtime is the composition layer and delegation is one thing you do inside it — visible in the fact that a single-turn sub-agent is executed through tool_context.run_node, as a node, not as a separate runner.

### 5.1 - The sub-agent that became a tool
`days/day-55-delegation-and-transfer/parts/05-agent-as-tool/5.1-the-sub-agent-that-became-a-tool.md` · level `working` · ids ADK-39

mode="single_turn" is the whole of agent-as-tool in ADK 2.7.1: the sub-agent leaves the transfer list, ADK appends a _SingleTurnAgentTool named after it to the caller's tools, and the caller can now ask it a question and get an answer back.

### 5.2 - The schema the caller sees
`days/day-55-delegation-and-transfer/parts/05-agent-as-tool/5.2-the-schema-the-caller-sees.md` · level `working` · ids ADK-39

By default a sub-agent-as-tool exposes exactly one argument — {"request": {"type": "string"}}, required — so the caller hands over one blob of free text; giving the specialist an input_schema replaces that with named, described, required fields, and the difference is the difference between a blank line and a form.

### 5.3 - The session it does not share
`days/day-55-delegation-and-transfer/parts/05-agent-as-tool/5.3-the-session-it-does-not-share.md` · level `production` · ids ADK-39

The two spellings of agent-as-tool run the specialist in different places: _SingleTurnAgentTool calls tool_context.run_node, keeping it inside the caller's session and trace, while AgentTool stands up a fresh Runner over a new InMemorySessionService — which is why its own docstring says direct use is discouraged.

### 5.4 - A failure that arrives as a string
`days/day-55-delegation-and-transfer/parts/05-agent-as-tool/5.4-a-failure-that-arrives-as-a-string.md` · level `production` · ids ADK-39

When a sub-agent-as-tool fails, ADK catches the exception and returns its text as the tool result — Error running sub-agent: 429 RESOURCE_EXHAUSTED: quota exceeded... arrives with type=str, exactly like a good answer — so unless the caller checks, a quota failure gets summarised into the reply as though it were a finding.

### 6.1 - A hand-off costs a request
`days/day-55-delegation-and-transfer/parts/06-price-of-a-handoff/6.1-a-handoff-costs-a-request.md` · level `working` · ids AG-16

The three shapes have three different prices in the only currency that matters on a free tier: an edge costs 1 request per ticket, a transfer 2, and an agent-as-tool call 3 — so twenty tickets through a call-shaped step is sixty requests against a lane that allows ten a minute.

### 6.2 - What the specialist cannot see
`days/day-55-delegation-and-transfer/parts/06-price-of-a-handoff/6.2-what-the-specialist-cannot-see.md` · level `production` · ids AG-16

A hand-off passes a re-statement, not the request, and re-statement is lossy: measured across a chain, the customer's original wording falls to 55% at one hop, 20% at two and 10% at three — and the first detail to go is always the one that dates the problem.

### 7.1 - Two counters pointing at each other
`days/day-55-delegation-and-transfer/parts/07-failure-lab/7.1-two-counters-pointing-at-each-other.md` · level `production` · ids ADK-38, AG-16

Two specialists whose descriptions each defer to the other will pass one request between them forever: twelve requests spent, six each, nothing answered — and the only reason it stopped at twelve is a constant in the lab, because ADK 2.7.1 has no transfer-depth limit of its own.

### 7.2 - The hand-over that never came back
`days/day-55-delegation-and-transfer/parts/07-failure-lab/7.2-the-handover-that-never-came-back.md` · level `production` · ids ADK-38, ADK-39

A transfer inside a pipeline does not fail loudly — it ends the pipeline: three stations out of five ran, zero errors were raised, and the reply went out without the draft or the review because control never returned to the stations that came after.

### 8.1 - How deep is defensible
`days/day-55-delegation-and-transfer/parts/08-in-production/8.1-how-deep-is-defensible.md` · level `production` · ids AG-16

Two hops is the working limit for a delegation chain, and the measurement says why: at depth 2 you have spent 3 requests and kept 55% of the customer's words, at depth 3 it is 4 and 20%, at depth 4 5 and 10% — cost rises linearly while fidelity falls off a cliff.

### 8.2 - Who decided, and why
`days/day-55-delegation-and-transfer/parts/08-in-production/8.2-who-decided-and-why.md` · level `production` · ids AG-16

A routing decision that logs only its outcome cannot be reviewed: the record has to carry the roster, the scores and the margin, because a decision won by zero is a tie-break wearing a decision's clothes — and one of four routings in the lab is exactly that.

## Papers - read after the parts

### doi:10.1109/TC.1980.1675516 - The Contract Net Protocol — asking instead of assigning
`days/day-55-delegation-and-transfer/papers/01-contract-net-protocol.md`

Work should be assigned by announcing the task and letting candidates bid on it, because the candidate knows things about its own fitness — what it is holding right now, whether it has the data — that no central routing table can hold.


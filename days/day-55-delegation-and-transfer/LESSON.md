---
day: 55
phase: 8
phase_name: "Workflows and multi-agent"
title: "Delegation & transfer; agent-as-tool"
ids: ["ADK-38", "ADK-39", "AG-16"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 23
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 55 — Delegation, transfer and agent-as-tool

> **Yesterday (Day 54):** the graph learned to run things in order, in parallel, and round a loop.
> Sequence, branching and repetition became structure — drawn, not decided, and therefore incapable
> of being decided wrongly.
> **Today:** the decisions you cannot draw. One agent reads a request and picks a colleague at
> request time, and there are exactly two ways to hand the work over: a **call** that comes back,
> and a **transfer** that does not. Everything else today follows from that one sentence.
> **Tomorrow (Day 56):** planning patterns — plan-and-execute and replanning, where the agent
> decides the *steps* rather than the *colleague*.

---

## §1 Where we are

Yesterday's graph is a floor plan. It says the ticket goes from intake to classify to research, and
it says so before any ticket arrives, which is why it cannot get the order wrong. That is the right
way to build most of a system, and Day 58 will build the triage pipeline exactly like that.

But watch an actual support desk for an hour and you will see something the floor plan cannot draw.
A hard ticket lands, the shift lead reads it, and says *"this one's for Meena — it smells like the
sign-in thing from March."* Nobody painted that on the floor. The lead read the ticket and decided,
in the moment, using something the floor plan does not contain.

**Today you build the shift lead.** And the first thing you find out is that "hand this to a
colleague" is not one action. It is two, and they are as different as two things at a counter can
be.

Picture the counter. Somebody comes in with a problem. The clerk can pick up the internal phone,
ask the back office one question, put the phone down, and carry on serving you — she never stopped
being the person you are dealing with, and she can use the answer, doubt it, or ignore it. Or she
can stand up, walk you to a different desk, hand over your file, and go back to her seat — and now
you are that desk's problem, and every question you think of afterwards goes to them.

A call comes back. A hand-over does not.

Everything today hangs off that. Who answers the next message. Whose rulebook is in force. What
happens when the specialist fails. What it costs — a call is three requests and a hand-over is two,
and the cheaper one is the one that gives away more. And what happens when two colleagues each
think the other one owns it: **twelve requests spent, six each, nothing answered**, because ADK has
no transfer-depth limit and nobody in the building has the job of noticing you have been round.

The day runs in Principle 4's order. You measure why one agent with twelve tools is worse than
three with four, before any framework word appears. You print the exact text ADK pastes into the
router's prompt — the staff list behind the counter — and watch a vague description win four
requests out of five that belonged to somebody else. Then you break it twice on purpose. Then you
read the 1980 paper that proposed the opposite design, and find out which half of it the field
kept.

Every number in this day comes from a script you can run, and **the day spends zero model calls.**

---

## §2 The map

Twenty-three parts in eight sections, then one paper.

### Section 1 — why split the desk at all (AG-16)

The framework-free case, measured before any ADK symbol appears.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [One counter, and everything behind it](parts/01-why-split-the-desk/1.1-one-counter-and-everything-behind-it.md) | What does a twelfth tool cost the other eleven? | foundation |
| 1.2 | [The handbook that served four jobs](parts/01-why-split-the-desk/1.2-the-handbook-that-served-four-jobs.md) | Why does adding a job make the rules weaker, not longer? | foundation |
| 1.3 | [Three homes for a step](parts/01-why-split-the-desk/1.3-three-homes-for-a-step.md) | Edge, call or hand-over — how do you choose? | working |

### Section 2 — the distinction the whole day rests on (ADK-38, ADK-39, AG-16)

One difference, three consequences.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [A call comes back](parts/02-call-or-handover/2.1-a-call-comes-back.md) | What actually differs between the two, and which field selects it? | foundation |
| 2.2 | [Who owns the turn afterwards](parts/02-call-or-handover/2.2-who-owns-the-turn.md) | Who answers the *next* message? | working |
| 2.3 | [Whose handbook is in force](parts/02-call-or-handover/2.3-whose-handbook-is-in-force.md) | Which rules apply once control has moved? | working |

### Section 3 — the description is the routing rule (ADK-38, AG-16)

Where routing decisions actually come from, and how to write one.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The staff list behind the counter](parts/03-the-description-routes/3.1-the-staff-list-behind-the-counter.md) | What text does the router's model actually receive? | working |
| 3.2 | [The clerk whose sign said "all enquiries"](parts/03-the-description-routes/3.2-the-clerk-whose-sign-said-all-enquiries.md) | What does a description that claims everything do? | working |
| 3.3 | [Writing a description that routes](parts/03-the-description-routes/3.3-writing-a-description-that-routes.md) | What are the four parts of one that works? | production |

### Section 4 — transfer, as ADK 2.7.1 implements it (ADK-38)

The hand-over mechanism, including trap #1.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Transfer is a signal, not a call](parts/04-transfer-in-2x/4.1-transfer-is-a-signal.md) | What does `transfer_to_agent` actually do? | working |
| 4.2 | [The enum that refuses a stranger](parts/04-transfer-in-2x/4.2-the-enum-that-refuses-a-stranger.md) | What stops a model naming a colleague that does not exist? | working |
| 4.3 | [Parents, peers and two switches](parts/04-transfer-in-2x/4.3-parents-peers-and-two-switches.md) | Who can hand to whom, by default? | working |
| 4.4 | [From agent tree to node graph](parts/04-transfer-in-2x/4.4-from-agent-tree-to-node-graph.md) | What changed from 1.x, and what does that mean for design? | production |

### Section 5 — agent-as-tool, as ADK 2.7.1 implements it (ADK-39)

The call mechanism, and the two ways it lies to you.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The sub-agent that became a tool](parts/05-agent-as-tool/5.1-the-sub-agent-that-became-a-tool.md) | How does a colleague end up in the tool list? | working |
| 5.2 | [The schema the caller sees](parts/05-agent-as-tool/5.2-the-schema-the-caller-sees.md) | What does the caller actually send it? | working |
| 5.3 | [The session it does not share](parts/05-agent-as-tool/5.3-the-session-it-does-not-share.md) | Which session does the specialist run in, and why does it matter? | production |
| 5.4 | [A failure that arrives as a string](parts/05-agent-as-tool/5.4-a-failure-that-arrives-as-a-string.md) | What happens when the specialist fails? | production |

### Section 6 — what a hand-off costs (AG-16)

Two currencies: requests, and the customer's own words.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [A hand-off costs a request](parts/06-price-of-a-handoff/6.1-a-handoff-costs-a-request.md) | What does each shape cost in free-tier quota? | working |
| 6.2 | [What the specialist cannot see](parts/06-price-of-a-handoff/6.2-what-the-specialist-cannot-see.md) | What is lost in the sentence that asks the question? | production |

### Section 7 — the failure lab (ADK-38, ADK-39, AG-16)

Two failures, broken on purpose, both silent.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [Two counters pointing at each other](parts/07-failure-lab/7.1-two-counters-pointing-at-each-other.md) | What does a routing loop cost, and what stops it? | production |
| 7.2 | [The hand-over that never came back](parts/07-failure-lab/7.2-the-handover-that-never-came-back.md) | Why does a truncated pipeline report success? | production |

### Section 8 — in production (AG-16)

The two questions a real system gets asked about its hand-offs.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 8.1 | [How deep is defensible](parts/08-in-production/8.1-how-deep-is-defensible.md) | How many hops before the answer is about a different question? | production |
| 8.2 | [Who decided, and why](parts/08-in-production/8.2-who-decided-and-why.md) | What has to be in the record for a routing decision to be reviewable? | production |

### The paper — read it after the parts

Principle 4 at the scale of a day: build the mechanism, *then* read the proposal.

| # | Paper | Why it is here |
| --- | --- | --- |
| 01 | [The Contract Net Protocol — asking instead of assigning](papers/01-contract-net-protocol.md) | Today's routing is a table. In 1980 somebody proposed asking instead, and the field kept half of it. |

---

## §3 Setup — run this

No package is added today. `google-adk` is already pinned at `2.7.1` (see `docs/PACKAGES.md`), and
every script in this lab is deterministic.

```bash
# from the repo root
mkdir -p days/day-55-delegation-and-transfer/lab/papers/contract-net
cd days/day-55-delegation-and-transfer/lab

touch _desk.py select.py staff.py describe.py handover.py reach.py \
      astool.py swallow.py price.py depth.py pingpong.py lost.py \
      stalled.py audit.py gate.py
touch papers/contract-net/contract_net.py papers/contract-net/demo.py

# nothing is installed today - confirm it stays that way
cd ../../..
git diff --stat pyproject.toml uv.lock
```

**Notes:**

- `mkdir -p` creates the paper demo's directory in the same command, because
  `papers/contract-net/` is two levels deep and `touch` will not create it.
- Fifteen lab scripts plus two demo files. Each is named for what it measures, so `./m start 55`
  lists something readable.
- The `git diff --stat` is the check, not a formality: today adds no dependency, and an empty diff
  on those two files is how you know.

Verify the framework symbols exist before you use them:

```bash
python -c "from google.adk.tools import AgentTool, TransferToAgentTool, transfer_to_agent; print('ok')"
python -c "from google.adk.agents import LlmAgent; print(LlmAgent.model_fields['mode'].annotation)"
```

**Notes:**

- The first import is the whole delegation surface today uses. If it raises, stop and check the
  installed version before writing anything (Principle 8).
- The second prints the `mode` field's type, which should show `chat`, `task` and `single_turn`.
  That is the field sections 2, 4 and 5 all turn on, so confirming it live is worth one command.

---

## §4 Build brief

Create `sutra/delegation.py`. It is a **new** file, deliberately not `sutra/graph.py`: today's
mechanism is a different animal from Day 53's edges, and keeping them apart keeps the difference in
your fingers.

```python
"""Day 55 - the shift lead: delegation, transfer and agent-as-tool.

Two shapes for the same specialists:
    lead demo  -> a transfer: the specialist owns the conversation
    tool demo  -> a call: the lead keeps the turn and gets a result

Run from the repo root:
    python -m sutra.delegation lead
    python -m sutra.delegation tool
"""

# TODO(me): pin the model to a free-tier string you looked up today (ADK-73,
#           Addendum 02). One constant, used by every agent in this file.

# TODO(me): write kb_specialist. mode="single_turn" (part 5.1). Its description
#           follows the four-part shape in part 3.3: what it does, what it
#           returns, what it does NOT do, nothing else.

# TODO(me): write archive_specialist, the same way. Make its exclusions
#           RECIPROCAL with kb_specialist's - neither may claim the other's
#           territory (part 3.3, the grid).

# TODO(me): write billing_agent as a chat-mode transfer target. This is the one
#           colleague that genuinely owns a conversation (part 1.3, question 3).
#           Set disallow_transfer_to_peers=True on it (part 7.1).

# TODO(me): write triage_lead with all three as sub_agents. Its own description
#           must exclude what the specialists claim, or it competes with them
#           (part 3.2).

# TODO(me): add HOP_LIMIT and a before_tool_callback that refuses
#           transfer_to_agent past it, counting in temp: state (part 7.1).

# TODO(me): the caller must check its tool results. A sub-agent failure arrives
#           as a string, not an exception (part 5.4). Write the check.
```

**Notes:**

- The module docstring names the two demos and how to run them, because a file whose two modes are
  not written down is a file with one mode and a surprise.
- Every `TODO(me)` names the part that explains it. A deferred explanation must have an address.
- The model pin is first because ADK-73 makes it non-negotiable, and because every agent below
  needs it.
- The hop cap and the result check are the two that `gate.py` will not let you skip. They are the
  difference between a demo and something you would run twice.

---

## §5 The eval that must be able to fail

`lab/gate.py` is red right now, before you write a line of the build brief.

```bash
cd days/day-55-delegation-and-transfer/lab
uv run python gate.py; echo "exit: $?"
```

Measured on 2026-09-05:

```text
  FAIL  sutra/delegation.py does not exist yet (LESSON.md section 4)

1 finding(s) - the day is not done
exit: 1
```

Six checks, each naming the part that explains the fix: `sub_agents=` present · at least one
`mode='single_turn'` · `disallow_transfer_to_peers` present · at least one description saying what
its agent does **not** do · a hop cap constant · the model pinned to a named constant.

Four of today's scripts are also evals with real exit codes, and all four are red on purpose:

```bash
uv run python pingpong.py; echo "exit: $?"   # 1 - the routing loop
uv run python lost.py; echo "exit: $?"       # 1 - the conversation at the wrong desk
uv run python stalled.py; echo "exit: $?"    # 1 - three of five stations ran
uv run python swallow.py --checked; echo "exit: $?"   # 1 - two failures found
```

Each has a flag that turns the fix on and takes it to `0`.

---

## §6 Request budget

**Zero model calls.** Not "a few", not "about five": zero.

| Provider | RPM used | RPD used | Why |
| --- | --- | --- | --- |
| Gemini free tier | 0 | 0 | every lab script is deterministic |
| Groq | 0 | 0 | not used today |
| OpenRouter `:free` | 0 | 0 | not used today |
| Ollama (local) | 0 | 0 | not used today |

That is a deliberate result rather than a happy accident. Everything today measures is structural —
what is in the prompt, which list an agent is in, how many requests a shape costs, how many words
survive a hop — and structure can be read out of the framework's own request-building code without
sending anything. The scripts import ADK's real `_get_transfer_targets`,
`_build_transfer_instruction_body`, `TransferToAgentTool` and `_SingleTurnAgentTool` and print what
they produce.

When you run the build brief's two demos against a live model, budget by
[6.1](parts/06-price-of-a-handoff/6.1-a-handoff-costs-a-request.md): the transfer demo is 2 requests
and the tool demo is 3, per invocation. Run each once, mindfully. Re-read the provider's current
free-tier page before you do (Addendum 02 — free rosters move), and every call path handles 429 with
`retry-after` and backoff.

---

## §7 Traps

| # | Trap | What happens | Where |
| --- | --- | --- | --- |
| 1 | **Trap #1 (plan §5.1): forcing composition through the agent tree** | A fixed sequence built as delegation costs a routing decision per step and can run out of order. In 2.x the graph is the composition layer. | [4.4](parts/04-transfer-in-2x/4.4-from-agent-tree-to-node-graph.md) |
| 2 | **Trap #4 (plan §5.1): a sub-agent failure returned as a string** | `_SingleTurnAgentTool` catches the exception and returns its text. A 429 and an answer arrive with the same type. | [5.4](parts/05-agent-as-tool/5.4-a-failure-that-arrives-as-a-string.md) |
| 3 | **`mode` defaults to `chat`** | A sub-agent you attach without thinking is a transfer target, not a tool. Your lead's summarising step never runs. | [2.1](parts/02-call-or-handover/2.1-a-call-comes-back.md) |
| 4 | **`AgentTool.create()`** | 1.x idiom. `AttributeError: type object 'AgentTool' has no attribute 'create'` on 2.7.1. | [2.1](parts/02-call-or-handover/2.1-a-call-comes-back.md) |
| 5 | **`disallow_transfer_to_parent=True` looks like the safe switch** | It leaves *only* the peer edges, which is a two-node cycle. The one you usually want is `disallow_transfer_to_peers`. | [4.3](parts/04-transfer-in-2x/4.3-parents-peers-and-two-switches.md) |
| 6 | **No transfer-depth limit exists** | ADK 2.7.1 ships none. A routing loop ends when your quota does. | [7.1](parts/07-failure-lab/7.1-two-counters-pointing-at-each-other.md) |
| 7 | **A vague description on any agent** | It competes for every request. Measured: scored on 4 of 5 requests belonging to others. | [3.2](parts/03-the-description-routes/3.2-the-clerk-whose-sign-said-all-enquiries.md) |
| 8 | **An agent's name becomes its tool name** | A specialist called `search_kb` collides with a function tool called `search_kb`, silently. | [5.1](parts/05-agent-as-tool/5.1-the-sub-agent-that-became-a-tool.md) |
| 9 | **`mode="task"` inside a graph** | Documented as disabled for graph-based workflows in ADK Python v2.0.0. 🅿️ awareness only. | [4.4](parts/04-transfer-in-2x/4.4-from-agent-tree-to-node-graph.md) |

---

## §8 Verify before you code

Pages actually fetched on **2026-09-05**:

- **<https://adk.dev/workflows/collaboration/>** — the three sub-agent modes and their behaviour
  table (*chat*: "Full user interaction, manual return to parent agent"; *task*: "User interaction
  for clarifications with automatic return"; *single-turn*: "No user interaction with automatic
  return and can be run in parallel"); delegation tools "named after the subagent itself"; the
  caveat that "the collaborative mode `task` behavior is disabled for use in graph-based workflows
  in ADK Python v2.0.0"; branch isolation for parallel sub-agents.
- **<https://adk.dev/agents/multi-agents/>** — returned a redirect stub rather than content on the
  date checked. Noted rather than guessed; the collaboration page above carries the same material.
- **<https://api.crossref.org/works/10.1109/TC.1980.1675516>** — the DOI registration record for
  today's paper. Title copied from it verbatim: *The Contract Net Protocol: High-Level Communication
  and Control in a Distributed Problem Solver*, IEEE Transactions on Computers, C-29(12),
  pp. 1104–1113, 1980.
- **<https://www.fipa.org/specs/fipa00029/>** and **<https://www.fipa.org/specs/fipa00030/>** — the
  FIPA Contract Net and Iterated Contract Net Interaction Protocol specifications, cited in the
  paper part's *In production* section.

Verified directly against the installed `google-adk==2.7.1`, since the source is stronger evidence
than a docs page for what will actually run:

- `google/adk/flows/llm_flows/agent_transfer.py` — `_get_transfer_targets`,
  `_build_transfer_instruction_body`, and the early return when there are no targets.
- `google/adk/tools/transfer_to_agent_tool.py` — `transfer_to_agent` is one assignment;
  `TransferToAgentTool` adds the `enum` constraint.
- `google/adk/tools/agent_tool.py` — `_SingleTurnAgentTool.run_async` uses `tool_context.run_node`;
  `AgentTool.run_async` builds its own `Runner` and `InMemorySessionService`; the `AgentTool`
  docstring says direct usage is discouraged.
- `google/adk/agents/llm_agent.py` — the `mode` field's docstring and the loop that wraps
  `single_turn` sub-agents as tools.

**One discrepancy, recorded rather than smoothed over.** The collaboration page says ADK
"automatically generates a delegation tool for each subagent, named after the subagent itself". In
2.7.1 that is true for `single_turn` and `task` sub-agents, which are wrapped and appended to the
parent's `tools`. A `chat`-mode sub-agent gets **no** tool of its own: it is reachable through the
single `transfer_to_agent` tool, whose `agent_name` parameter carries an enum of valid names.
`staff.py` prints both lists, so you can see it. The parts teach the installed behaviour.

---

## §9 Say it in an interview

"There are two ways one agent hands work to another and they are not variations of each other. A
call comes back and a transfer does not. With agent-as-tool the caller asks a bounded question, gets
a result, and keeps the turn — so it can check the result, retry, or fall back. With a transfer the
caller's turn is over and the specialist owns the conversation from then on, including the next
message and the one after that. In ADK 2.7.1 both are attached the same way, with `sub_agents`, and
the choice is one field: `mode='single_turn'` puts the colleague in the caller's tool list, and the
default `chat` leaves it as a transfer target — so the more generous option is the one you get by
not choosing.

The thing I would want to talk about is what that costs. A transfer that nobody reverses leaves the
customer at the wrong desk: I measured a five-turn session where one correct hand-off on turn two
led to three turns answered by the billing agent, confidently, about session cookies. Inside a
pipeline it is worse — a station that transfers ends the pipeline, so three of five stations ran,
zero errors were raised, and an unreviewed reply went out looking complete. And two specialists
whose descriptions each defer to the other will pass one request back and forth forever; I measured
twelve requests spent, six each, nothing answered, and ADK has no transfer-depth limit, so on a free
tier the thing that stops a routing loop is your daily quota. Two defences: default specialists to
`disallow_transfer_to_peers` so all routing goes through the lead, and a hop counter in a tool
callback stored in invocation state, because a 429 plus a retry policy will otherwise resume the
loop.

The part that surprised me most is that the routing rule is not in the router. ADK pastes each
sub-agent's `description` verbatim into the coordinator's system prompt and tells the model to
choose according to it, so editing one agent's description changes a different agent's behaviour
with no import between them. A description that says 'a helpful assistant that handles support
requests' is true of every request, so it competes for all of them — I measured one scoring on four
requests out of five that belonged to somebody else, with a specialist winning by a single point and
another decision settled by an alphabetical tie-break. Narrowing it to say what it does *not* do
took that to zero. That is why I now review descriptions as a set rather than one at a time."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and each one is ticked because you ran the
thing rather than because you read it.

The day is finished when you can say, without looking: which field turns a sub-agent into a tool,
who owns the conversation after each shape, what a hand-off costs in requests, and what stops two
agents passing a ticket to each other forever. `./m done 55` refuses to commit until the checklist
is complete.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 55 | <date> | ADK-38, ADK-39, AG-16 | 23 (+1 paper) | <hash> | ⚠️ |
```

**`docs/PACKAGES.md`** — no row. No package was added today; `google-adk==2.7.1` was already pinned.

**`docs/PAPERS.md`** — this row was appended on 2026-09-05:

```text
| The Contract Net Protocol: High-Level Communication and Control in a Distributed Problem Solver | doi:10.1109/TC.1980.1675516 | 1980 | 2026-09-05 | 55 | `days/day-55-delegation-and-transfer/papers/01-contract-net-protocol.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no row. No third-party skill was sourced today.

**The commit:**

```text
day 55: delegation, transfer and agent-as-tool - closes ADK-38, ADK-39, AG-16
```

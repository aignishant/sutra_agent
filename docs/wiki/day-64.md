# Day 64 - Approval gates — build; HITL resumption for standalone nodes & NodeTool

IDs closed: ADK-48, ADK-76 · source: `days/day-64-approval-gates-build/`

## Parts

### 1.1 - A gate is a decision about one action
`days/day-64-approval-gates-build/parts/01-the-policy-is-data/1.1-a-gate-is-a-decision-about-one-action.md` · level `foundation` · ids ADK-48

An approval gate is not a property of an agent or of a tool; it is a decision made about one call, with the arguments it is about to run with, and everything else today follows from taking that sentence literally.

### 1.2 - The policy is a file, not a habit
`days/day-64-approval-gates-build/parts/01-the-policy-is-data/1.2-the-policy-is-a-file-not-a-habit.md` · level `working` · ids ADK-48

The list of gated actions belongs in a data file that a person can read end to end in one sitting, with a written reason on every row including the ungated ones, because a policy you have to reconstruct by reading code is a policy nobody reviews.

### 1.3 - The arguments decide, not the tool
`days/day-64-approval-gates-build/parts/01-the-policy-is-data/1.3-the-arguments-decide-not-the-tool.md` · level `working` · ids ADK-48

The same tool called two ways can be routine or irreversible, so the gate has to be a function of the arguments, and a policy that cannot see the arguments is guaranteed to be wrong for a large fraction of real calls — on this desk, for twenty of twenty-four.

### 1.4 - The guard that was only added in three places
`days/day-64-approval-gates-build/parts/01-the-policy-is-data/1.4-the-guard-that-was-only-added-in-three-places.md` · level `production` · ids ADK-48

Writing the gate as a condition at each place the action happens gives you as many policies as you have call sites, and they drift apart silently — measured here, two of four call sites let a call through that the policy file stops, and one of the two has a guard; it is just out of date.

### 2.1 - One argument turns a tool into a gate
`days/day-64-approval-gates-build/parts/02-the-tool-gate/2.1-one-argument-turns-a-tool-into-a-gate.md` · level `working` · ids ADK-48

FunctionTool(func, require_confirmation=...) takes the decision function from section 1 and puts it in front of the function body, so a gated call returns a refusal with the body not run — and the effects ledger is what proves it.

### 2.2 - What comes back when the tool refuses
`days/day-64-approval-gates-build/parts/02-the-tool-gate/2.2-what-comes-back-when-the-tool-refuses.md` · level `working` · ids ADK-48

A refused tool call does not raise and does not return nothing; it returns an ordinary result that says this needs confirmation, and that string goes back to the model — which means the wording of a refusal is part of your prompt, not just part of your logs.

### 2.3 - A rejection is not a failure
`days/day-64-approval-gates-build/parts/02-the-tool-gate/2.3-a-rejection-is-not-a-failure.md` · level `working` · ids ADK-48

Nobody has answered yet and a person answered no are two different outcomes with two different correct responses, and ADK returns two different strings for them — which is the only reason your code can tell them apart.

### 3.1 - The question has to be written down somewhere
`days/day-64-approval-gates-build/parts/03-binding-the-answer/3.1-the-question-has-to-be-written-down.md` · level `working` · ids ADK-48

A pause only works if the question survives the process that asked it, so the gate writes a pending record keyed by the function call's id, and that key is what lets an answer arriving later — from another process, on another machine — find the call it belongs to.

### 3.2 - The request carries a copy of the call
`days/day-64-approval-gates-build/parts/03-binding-the-answer/3.2-the-request-carries-a-copy-of-the-call.md` · level `working` · ids ADK-48

The approval request does not merely point at the call it is about — it carries a full copy of the call's name and arguments inside itself, and that redundancy is what makes it possible to check later that the answer and the action still match.

### 3.3 - Approve one thing, execute another
`days/day-64-approval-gates-build/parts/03-binding-the-answer/3.3-approve-one-thing-execute-another.md` · level `production` · ids ADK-48

A gate that only reads confirmed accepts an approval for a call that was never made, for a tool that never needed one, and for arguments that were edited on the way back — four out of four against ADK's own validator's one out of four.

### 3.4 - One approval, delivered twice
`days/day-64-approval-gates-build/parts/03-binding-the-answer/3.4-one-approval-delivered-twice.md` · level `production` · ids ADK-48

The approver clicks once and the answer arrives twice, because the transport between them and your runtime guarantees at least once and never exactly once — and without a key, one approval sends the customer two emails.

### 3.5 - The key names the decision, not the attempt
`days/day-64-approval-gates-build/parts/03-binding-the-answer/3.5-the-key-names-the-decision.md` · level `production` · ids ADK-48

An idempotency key built from the attempt suppresses nothing, and a key built too coarsely suppresses a real second decision — the key has to name which decision was made, which on this desk is the interrupt, the decider and the answer.

### 4.1 - A node that stops and asks
`days/day-64-approval-gates-build/parts/04-the-node-gate/4.1-a-node-that-stops-and-asks.md` · level `working` · ids ADK-76

Inside a graph the pause is not a tool argument but a node that yields a RequestInput, and the run genuinely ends there — the process exits, the effects ledger is empty, and the question waits in the session for whoever picks it up next.

### 4.2 - Where the answer lands when the run comes back
`days/day-64-approval-gates-build/parts/04-the-node-gate/4.2-where-the-answer-lands.md` · level `working` · ids ADK-76

By default the human's answer does not go back into the node that asked — the asking node's body never runs again, and the answer is handed forward to its successor as that node's input, which is why the next node is the one that has to read it.

### 4.3 - The human said no and the reply went anyway
`days/day-64-approval-gates-build/parts/04-the-node-gate/4.3-the-human-said-no-and-the-reply-went-anyway.md` · level `production` · ids ADK-76

A graph that pauses, asks a real person and receives a real rejection will still run the next node, because an edge fires on completion and not on approval — the refund email goes out with approved: False sitting in the node's own input, and the fix is one line in the successor.

### 4.4 - Asking the same person the same question twice
`days/day-64-approval-gates-build/parts/04-the-node-gate/4.4-asking-the-same-person-twice.md` · level `production` · ids ADK-76

rerun_on_resume=True makes the asking node's body run again on resume — and a body that asks unconditionally asks again, pausing the run for ever unless it reads resume_inputs and notices the answer is already there.

### 4.5 - NodeTool, and where it actually lives
`days/day-64-approval-gates-build/parts/04-the-node-gate/4.5-nodetool-and-where-it-lives.md` · level `production` · ids ADK-76

NodeTool lets an agent call a pausing node as if it were a tool, joining section 2's world to section 4's — and in google-adk==2.7.1 it exists, works, and is not exported: it imports only from google.adk.tools._node_tool, is absent from __all__, and appears nowhere in the docs.

### 5.1 - The decision is already written down
`days/day-64-approval-gates-build/parts/05-the-record/5.1-the-decision-is-already-written-down.md` · level `working` · ids ADK-48

You do not write an audit log for an approval — the pause, the payload and the answer are all already events in the session, so the record is something you read back out, and a trail you have to write separately is a trail that can disagree with what happened.

### 5.2 - What the record has to answer
`days/day-64-approval-gates-build/parts/05-the-record/5.2-what-the-record-has-to-answer.md` · level `production` · ids ADK-48

A record that says approved by shift_lead is not a record — it has to carry the evidence the approver saw and the policy version that produced the question, because the only reader who will ever need it is somebody reconstructing a decision they were not present for.

### 6.1 - The sixth station
`days/day-64-approval-gates-build/parts/06-wiring-the-desk/6.1-the-sixth-station.md` · level `working` · ids ADK-48, ADK-76

The gate joins Day 58's triage graph as one node with two routed edges, so an ungated ticket runs straight through and disturbs nobody, and a gated one stops at the same node that later decides — measured, six stations and zero humans for a portal note, seven and one for a refund by email.

### 6.2 - Three roads to one function
`days/day-64-approval-gates-build/parts/06-wiring-the-desk/6.2-three-roads-to-one-function.md` · level `production` · ids ADK-48

The gate lives in the wrapper, not in the function, so every other route to the same function is ungated — measured, three ways to reach close_ticket and one of three honours a policy that says this call needs a human.

### 6.3 - The check that goes red when the gate goes
`days/day-64-approval-gates-build/parts/06-wiring-the-desk/6.3-the-check-that-goes-red-when-the-gate-goes.md` · level `production` · ids ADK-48

A test that asserts the gate paused passes in three situations where the desk is broken, so the day's eval asserts on the effect instead — six checks, red until sutra/approval.py exists, and red again the moment the gate or the idempotency key is removed.

### 7.1 - The queue in front of the approver
`days/day-64-approval-gates-build/parts/07-in-production/7.1-the-queue-in-front-of-the-approver.md` · level `production` · ids ADK-48

An approver is a queue with a service rate, not a function call, and the policy decides the arrival rate — measured over one shift, the real policy queues 4 of 24 calls with a peak depth of 2 and nothing left waiting, while gating every write queues 14, peaks at 5, and ends the shift with 2 still unanswered.

### 7.2 - The deadline the approval must beat
`days/day-64-approval-gates-build/parts/07-in-production/7.2-the-deadline-the-approval-must-beat.md` · level `production` · ids ADK-48

A proposal that is answered late is not the same as one that is answered — under the naive policy 2 of 14 cross the staleness line, and the system has no correct automatic response to a stale approval, so the deadline has to be a decision somebody writes down rather than a timeout somebody picks.

### 7.3 - Who is allowed to say yes
`days/day-64-approval-gates-build/parts/07-in-production/7.3-who-is-allowed-to-say-yes.md` · level `production` · ids ADK-48, ADK-76

The desk records who approved and never checks whether they were allowed to — by is a string the client sends, so the gate authenticates nobody, and an approval gate without authorisation is a gate with a signature line and no lock.


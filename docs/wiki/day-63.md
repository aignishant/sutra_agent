# Day 63 - Approval gates — design (what needs a human, and why)

IDs closed: SEC-05, ADK-47 · source: `days/day-63-approval-gates-design/`

## Parts

### 1.1 - A control that fires on everything
`days/day-63-approval-gates-design/parts/01-the-gate-that-means-nothing/1.1-a-control-that-fires-on-everything.md` · level `foundation` · ids SEC-05

An approval gate spends a finite amount of human attention, so a gate that fires on every write spends it on the safe ones and has none left for the dangerous ones: over one recorded night, asking a human 41 times caught 2 of 6 mistakes, and asking them 11 times caught 4 of the 4 that mattered.

### 1.2 - A permission is not a gate
`days/day-63-approval-gates-design/parts/01-the-gate-that-means-nothing/1.2-a-permission-is-not-a-gate.md` · level `foundation` · ids SEC-05

A permission is decided once and sees only the name of an action; a gate is decided per call and sees the arguments — which is why a permission system that correctly allows all nine closes in the batch also correctly allows the three that were wrong.

### 1.3 - The four questions
`days/day-63-approval-gates-design/parts/01-the-gate-that-means-nothing/1.3-the-four-questions.md` · level `working` · ids SEC-05

"close_ticket needs approval" is a gate specification that answers one of four required questions, and each of the other three, left unanswered, is a specific failure with a name that this day reproduces.

### 2.1 - Reversible, and the cost of the undo
`days/day-63-approval-gates-design/parts/02-sorting-the-actions/2.1-reversible-and-the-cost-of-the-undo.md` · level `working` · ids SEC-05

"Reversible" is two questions wearing one word — can the state go back, and is the person whole again — and close_ticket is the action where they disagree: reopen restores the row perfectly and restores nothing the customer cares about.

### 2.2 - Blast radius, counted in people
`days/day-63-approval-gates-design/parts/02-sorting-the-actions/2.2-blast-radius-counted-in-people.md` · level `working` · ids SEC-05

"High impact" is an adjective two engineers can disagree about for an hour; "nine customers a night, none of whom agreed to be triaged by software" is a count, and the batch produces it — 28 writes touching only us, 4 touching a colleague, 9 reaching outside the company.

### 2.3 - The undo nobody asks for
`days/day-63-approval-gates-design/parts/02-sorting-the-actions/2.3-the-undo-nobody-asks-for.md` · level `working` · ids SEC-05

An undo is only worth what the alarm in front of it is worth: reopen is free and instant, and three of Sutra's ten actions carry a detect_hours of 72 or more, which makes their undos theoretical rather than available.

### 2.4 - Defeated by its own volume
`days/day-63-approval-gates-design/parts/02-sorting-the-actions/2.4-defeated-by-its-own-volume.md` · level `production` · ids SEC-05

Frequency is not a safety property and must never enter the decision about whether an action is dangerous — but it decides whether the gate you designed is the gate that actually runs, so it is measured separately and kept visible: 41 approvals a night, 9, or 11, from the same batch.

### 3.1 - The write inventory
`days/day-63-approval-gates-design/parts/03-the-policy-table/3.1-the-write-inventory.md` · level `working` · ids SEC-05

A policy is worth exactly as much as the inventory it was written against, so the inventory comes first: ten actions, eight of them shipped, two of them rows written before the tool exists — and a check that the count of actions and the count of rows are equal.

### 3.2 - The table and the argument
`days/day-63-approval-gates-design/parts/03-the-policy-table/3.2-the-table-and-the-argument.md` · level `production` · ids SEC-05

The policy is data with a sentence per row, and the sentence earns its place on exactly the rows where the written decision overrules the arithmetic — which for Sutra is one row out of ten: escalate_to_engineer, where the facts say always and the policy says threshold.

### 3.3 - The rows that are not gated
`days/day-63-approval-gates-design/parts/03-the-policy-table/3.3-the-rows-that-are-not-gated.md` · level `working` · ids SEC-05

An ungated action is a decision somebody made, not an action somebody forgot, so each never row has to carry its price in the open: Sutra's two ungated writes cost 28 approvals a night that nobody is asked for and let 2 wrong writes through, and that is the trade the table is buying attention with.

### 3.4 - The Tuesday a tool arrives
`days/day-63-approval-gates-design/parts/03-the-policy-table/3.4-the-tuesday-a-tool-arrives.md` · level `production` · ids SEC-05

The only property of a policy that matters on the day somebody adds a tool is what it does with a name it has never seen: over one week, fail-closed asked for 52 approvals and let 0 merges run unreviewed, while fail-open asked for 0 and ran all 52 — three of them wrong, with no error raised anywhere.

### 4.1 - Approving bytes, not pointers
`days/day-63-approval-gates-design/parts/04-what-the-approver-sees/4.1-approving-bytes-not-pointers.md` · level `working` · ids SEC-05

An approval that records a ticket number has approved a name, and the thing behind that name can change before it executes: pinning the payload raises ApprovalMismatch: approved 80c7b07b645d but about to execute cbbb396abd33, while approving the pointer sends a reply the human never read and reports nothing at all.

### 4.2 - The request and the diff
`days/day-63-approval-gates-design/parts/04-what-the-approver-sees/4.2-the-request-and-the-diff.md` · level `working` · ids SEC-05

A screen showing what was asked for and a screen showing what will change are two different documents, and only one of them contains the mistake: over the batch's wrong closes, the request screen makes 0 of 3 detectable and the diff screen makes 3 of 3.

### 4.3 - Separation of duty
`days/day-63-approval-gates-design/parts/04-what-the-approver-sees/4.3-separation-of-duty.md` · level `production` · ids SEC-05

Two signatures on the same evidence is one signature written twice: over thirteen gated actions, an approver reading the agent's own summary stopped 0 of 4 wrong ones, and an approver reading the ticket stopped 4.

### 4.4 - The four facts a record must hold
`days/day-63-approval-gates-design/parts/04-what-the-approver-sees/4.4-the-four-facts-a-record-must-hold.md` · level `production` · ids SEC-05

An incident review asks four questions and accepts no guesses, so an approval record is scored by how many it answers: a boolean answers 0 of 4, a boolean with a name answers 1, adding a timestamp and a session pointer answers 2, and only a record holding the payload itself answers 4.

### 5.1 - Fail closed or fail open
`days/day-63-approval-gates-design/parts/05-when-nobody-answers/5.1-fail-closed-or-fail-open.md` · level `production` · ids SEC-05

"Fail closed" is a slogan and not a policy, because the safer half is a property of the action: of Sutra's four gated actions, three fail closed and exactly one fails open — escalate_to_engineer, the only one whose harm comes from the delay rather than from the act.

### 5.2 - The answer nobody gave
`days/day-63-approval-gates-design/parts/05-when-nobody-answers/5.2-the-answer-nobody-gave.md` · level `production` · ids SEC-05

A timeout shorter than the gap between filing an approval and reading it makes the timeout the decider, and Sutra's overnight batch is exactly that shape: 11 of 11 approvals answered by a constant, and every one of them leaving the same log line a human decision would leave.

### 5.3 - The key with the neighbour
`days/day-63-approval-gates-design/parts/05-when-nobody-answers/5.3-the-key-with-the-neighbour.md` · level `production` · ids SEC-05

Every gate needs a way past it, and the only thing separating a break-glass path from a hole is whether using it is louder than not using it: the same four overrides recorded as break-glass events create 4 review items, and recorded as ordinary approvals create 0 and make the operator look diligent.

### 6.1 - The road the gate is not on
`days/day-63-approval-gates-design/parts/06-gates-that-are-decoration/6.1-the-road-the-gate-is-not-on.md` · level `production` · ids SEC-05

A gate keyed on the name of an action does not protect the effect of that action, so when a second path to the same effect appears, six tickets get closed and only three approvals are asked for — with nothing bypassed, nothing failing, and no error anywhere.

### 6.2 - The field the agent writes
`days/day-63-approval-gates-design/parts/06-gates-that-are-decoration/6.2-the-field-the-agent-writes.md` · level `production` · ids SEC-05

A threshold is only as independent as the value it reads, and Sutra's reads severity from the agent's own classification: 2 pages went out that should have been asked about, and reading severity from the ticket instead takes that to 0 with nothing else changed.

### 6.3 - Ask until somebody says yes
`days/day-63-approval-gates-design/parts/06-gates-that-are-decoration/6.3-ask-until-somebody-says-yes.md` · level `production` · ids SEC-05

A rejection that only ends one attempt is a delay, not a decision: re-filing after a refusal closed a ticket that two approvers had refused, and the audit trail records one approval, accurately, and nothing about the two refusals.

### 6.4 - The sweep nobody runs
`days/day-63-approval-gates-design/parts/06-gates-that-are-decoration/6.4-the-sweep-nobody-runs.md` · level `production` · ids SEC-05

Approval fatigue is agreed by everyone and measured by nobody, so it never changes a design: sweeping the one assumption shows the policy's catch rate flat at 4 of 4 from an attention budget of eleven upwards, while gating everything runs from 0 to 6 across the same range — one policy is betting on a good night and the other is not.

### 7.1 - The door on the tool
`days/day-63-approval-gates-design/parts/07-the-two-doors/7.1-the-door-on-the-tool.md` · level `working` · ids ADK-47

ADK 2.7.1 puts an approval flag on the tool itself — FunctionTool(fn, require_confirmation=...), taking True, False or a predicate over the tool's arguments — and its own documentation names it experimental and lists DatabaseSessionService as unsupported, which is the session service Day 47 gave Sutra.

### 7.2 - The door in the graph
`days/day-63-approval-gates-design/parts/07-the-two-doors/7.2-the-door-in-the-graph.md` · level `production` · ids ADK-47

The second door is a node yielding RequestInput, which pauses the workflow and carries message, payload, response_schema and a generated interrupt_id — and its default resumption routes the human's reply to the node's successor, bypassing the node that asked, which is the same behaviour Day 60 measured for crash resumes.

### 7.3 - What Day 64 is handed
`days/day-63-approval-gates-design/parts/07-the-two-doors/7.3-what-day-64-is-handed.md` · level `production` · ids ADK-47, SEC-05

A design day ends by writing down what "built" means, so the handover is not a document but a failing check: gate.py reports 6 findings and exits 1 today, and Day 64 is finished when the same command exits 0.

## Papers - read after the parts

### doi:10.1109/SP.1987.10001 - Well-formed transactions and separation of duty
`days/day-63-approval-gates-design/papers/01-well-formed-transactions.md`

Commercial systems do not mainly care who may read data; they care that the data stays correct — and correctness is enforced by two rules, that every change goes through a certified procedure and that no one person may both certify and execute one.


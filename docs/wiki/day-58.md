# Day 58 - The triage graph v1 — intake→classify→research→draft→review, end to end

IDs closed: ADK-41, ADK-42 · source: `days/day-58-triage-graph-v1/`

## Parts

### 1.1 - Ten stations, two of which think
`days/day-58-triage-graph-v1/parts/01-the-floor/1.1-ten-stations-two-of-which-think.md` · level `foundation` · ids ADK-41

A production agent pipeline is mostly plumbing around very few brains: this floor has ten stations and exactly two of them would call a model, and that ratio — not the station count — is what makes a five-stage pipeline affordable on a free tier.

### 1.2 - The baton has a declared shape
`days/day-58-triage-graph-v1/parts/01-the-floor/1.2-the-baton-has-a-declared-shape.md` · level `working` · ids ADK-41

Assembly is not connecting stations, it is declaring what travels between them: annotate the receiving side with a type and ADK 2.7.1 turns the sender's plain dictionary into that type on the way across the edge, so a seam that disagrees fails at the seam instead of four stations later.

### 1.3 - One station decides what is real
`days/day-58-triage-graph-v1/parts/01-the-floor/1.3-one-station-decides-what-is-real.md` · level `working` · ids ADK-41

Every station in a pipeline is entitled to assume its input is real, and exactly one station is responsible for making that true — so existence is checked at the mouth, and a miss leaves as a route rather than as a sentence for the next station to read.

### 2.1 - A verdict is a form, not a paragraph
`days/day-58-triage-graph-v1/parts/02-the-guess/2.1-a-verdict-is-a-form.md` · level `working` · ids ADK-41

The one station on this floor that is allowed to guess must hand its guess over as a filled form with fixed fields, never as prose, because every station downstream branches on it and no station should be reading sentences to find out what to do.

### 2.2 - The route is an action, not the answer
`days/day-58-triage-graph-v1/parts/02-the-guess/2.2-the-route-is-an-action.md` · level `working` · ids ADK-41

In the 2.x Workflow Runtime a station says where the run goes next through Event.actions.route and says what it produced through Event.output — two separate channels, and collapsing them into one is the 1.x habit that makes a branch depend on the wording of a sentence.

### 2.3 - The one model call, pinned and refused
`days/day-58-triage-graph-v1/parts/02-the-guess/2.3-the-one-model-call.md` · level `working` · ids ADK-41

The classifier's model is named explicitly, never defaulted, its output is constrained to the verdict schema, and when the free tier refuses the call the station waits, retries and then says it could not classify — because a fabricated verdict is worse than a stopped run.

### 2.4 - The lane that declines the work
`days/day-58-triage-graph-v1/parts/02-the-guess/2.4-the-lane-that-declines-the-work.md` · level `working` · ids ADK-41

Wire the escalation lane first, and check it before any expensive station runs: the most important route in a pipeline is the one where the machine says this is not mine to answer, and on this floor it costs three stations and one request instead of twelve and five.

### 3.1 - Two clerks who disagree about similar
`days/day-58-triage-graph-v1/parts/03-the-research-floor/3.1-two-clerks-who-disagree.md` · level `working` · ids ADK-41

The research floor runs two different searches on purpose — one by meaning over the ticket archive, one by words over the knowledge base — because the two corpora are different in kind, and measuring both reveals that one clerk finds something 100% of the time and the other 8%.

### 3.2 - The join hands over a dict keyed by node name
`days/day-58-triage-graph-v1/parts/03-the-research-floor/3.2-the-join-hands-over-a-dict.md` · level `working` · ids ADK-41

A JoinNode waits for every branch that feeds it and hands its successor a dictionary keyed by the branch nodes' names — which is the one undeclared seam on this floor, so exactly one station exists to turn it into a declared type before anything else sees it.

### 3.3 - What a lane costs
`days/day-58-triage-graph-v1/parts/03-the-research-floor/3.3-what-a-lane-costs.md` · level `production` · ids ADK-42

A pipeline's price is not a property of the code, it is a property of the path a ticket took, so the honest unit of cost is the lane — and on this floor the four lanes cost 0, 1, 3 and 5 requests, which averages to 2.08 across the archive and puts the desk's capacity at under ten tickets a day.

### 4.1 - The newsroom drops in as one node
`days/day-58-triage-graph-v1/parts/04-the-box/4.1-the-newsroom-drops-in-as-one-node.md` · level `working` · ids ADK-41

A whole Workflow is itself a node, so the writer-and-critic loop is one station from outside and a five-station graph from inside, and the floor's edge list neither knows nor can reach into what happens in there.

### 4.2 - The brake belongs to the critic
`days/day-58-triage-graph-v1/parts/04-the-box/4.2-the-brake-belongs-to-the-critic.md` · level `working` · ids ADK-41

The station that decides whether to go round again must be the station that counts the rounds, and when the count runs out the loop ships the draft with a flag rather than looping for ever or silently dropping the work.

### 4.3 - The stamp that may not change the answer
`days/day-58-triage-graph-v1/parts/04-the-box/4.3-the-stamp-that-may-not-change-the-answer.md` · level `working` · ids ADK-42

The last station declares the run finished and must therefore be pure — it may package, extract and record, but the moment it can alter the answer, "finished" stops meaning anything and the audit trail is auditing itself.

### 5.1 - The edge list is the floor plan
`days/day-58-triage-graph-v1/parts/05-the-graph/5.1-the-edge-list-is-the-floor-plan.md` · level `working` · ids ADK-41

Because the wiring is a list of edges rather than a nesting of objects, the whole floor is six lines of data — which means the framework can check it before anything runs, and the architecture diagram can be printed from the graph instead of drawn beside it.

### 5.2 - On the edge or in the register
`days/day-58-triage-graph-v1/parts/05-the-graph/5.2-on-the-edge-or-in-the-register.md` · level `working` · ids ADK-42

A node parameter named node_input is filled from the edge; every other parameter is looked up in session state by its own name — so a station takes its baton from whoever ran before it and anything else from the run's shared register.

### 6.1 - The event stream is the story
`days/day-58-triage-graph-v1/parts/06-the-run/6.1-the-event-stream-is-the-story.md` · level `working` · ids ADK-42

A run is finished when you can account for it, and the account is the event stream: twelve lines, in order, each naming the station that produced it and what it emitted — and if a station did work that the stream cannot show, the station did not do it.

### 6.2 - State is the case file
`days/day-58-triage-graph-v1/parts/06-the-run/6.2-state-is-the-case-file.md` · level `working` · ids ADK-42

The event stream is the run as it happened; session state is the run as it can be queried afterwards — and the test of a case file is whether it answers a fixed list of questions without anybody re-reading the source.

### 6.3 - A reply to a ticket that does not exist
`days/day-58-triage-graph-v1/parts/06-the-run/6.3-a-reply-to-a-ticket-that-does-not-exist.md` · level `production` · ids ADK-42

Turn off the one existence check at the mouth and the floor does not fail — it launders: every station works perfectly on a request that names nothing, and out the far end comes a reviewed, approved reply about ticket:8842, for three model calls, with exit code 0.

### 6.4 - The seam that drifted
`days/day-58-triage-graph-v1/parts/06-the-run/6.4-the-seam-that-drifted.md` · level `production` · ids ADK-42

When a station stops honouring a contract, the failure appears where the value is used, not where it was produced — and a station that catches its own error to be helpful converts that distance into an apology printed inside the customer's reply.

### 7.1 - Every part passed, the thing does not fit
`days/day-58-triage-graph-v1/parts/07-acceptance/7.1-every-part-passed.md` · level `production` · ids ADK-42

Node tests prove stations; a pipeline needs statements about whole runs, and this floor's node tests all pass while four of twenty-four replies cite a source — which is a fact no test of any single station could have produced.

### 7.2 - The gate that goes red
`days/day-58-triage-graph-v1/parts/07-acceptance/7.2-the-gate-that-goes-red.md` · level `production` · ids ADK-42

An eval is only worth having if it can fail, so the day's gate is written before the code and run before anything exists — seven checks, seven failures, exit 1 — and each one is a sentence from a part turned into something a machine can refuse.

### 8.1 - The green run that helped nobody
`days/day-58-triage-graph-v1/parts/08-in-production/8.1-the-green-run-that-helped-nobody.md` · level `production` · ids ADK-42

The founding ticket produces a run in which every station succeeds, the critic approves, the case file is complete and the reply contains no answer — because the rubric only requires a citation when retrieval found one, so a retrieval miss quietly lowers the standard instead of raising an alarm.

### 8.2 - A gate that fires on half the traffic
`days/day-58-triage-graph-v1/parts/08-in-production/8.2-a-gate-that-fires-on-half-the-traffic.md` · level `production` · ids ADK-41

The escalation lane takes 54% of the archive, and twenty-six of those twenty-eight tickets are there because the classifier did not understand them rather than because they need a human — so the control that was designed as an exception has quietly become the process.

### 8.3 - Thirty nodes, a queue and a timeout
`days/day-58-triage-graph-v1/parts/08-in-production/8.3-thirty-nodes-a-queue-and-a-timeout.md` · level `production` · ids ADK-42

A floor that runs from a command has no deadline and one caller; a floor that runs from a queue has many callers, partial failures and a clock — and ADK gives every node timeout and retry_config for exactly that, with the caveat that a station which dies without producing output stops a join rather than failing at it.


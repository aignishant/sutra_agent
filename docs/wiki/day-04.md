# Day 04 - Tools by hand — schemas, the call, the result turn

IDs closed: AG-04 · source: `days/day-04-tools-by-hand/`

## Parts

### 1.1 - The form that rejects itself — what a schema is, and who does the rejecting
`days/day-04-tools-by-hand/parts/01-the-schema/1.1-the-form-that-rejects-itself.md` · level `foundation` · ids AG-04

A schema is a machine-readable description of what a valid input looks like, and its entire value is that somebody other than you enforces it — which turns yesterday's format miss from a parse problem you discover after paying into a rejection that happens before the reply is ever produced.

### 1.2 - Declaring a tool — the six keys that replace a paragraph
`days/day-04-tools-by-hand/parts/01-the-schema/1.2-declaring-a-tool.md` · level `working` · ids AG-04

A tool declaration is a plain Python dict with four top-level keys — type, name, description, parameters — where parameters is JSON Schema describing named, typed, individually-required arguments, and writing one by hand is what makes Day 10's generated version legible instead of magical.

### 1.3 - The description is the prompt — the only field the model actually reads
`days/day-04-tools-by-hand/parts/01-the-schema/1.3-the-description-is-the-prompt.md` · level `working` · ids AG-04

Of the whole declaration, the provider enforces name, type and parameters — but description is read by the model and by nothing else, which makes it prompt engineering that happens to live in a schema field, and the single highest-leverage sentence you will write today.

### 2.1 - Two channels, not one — where the tool request stopped living
`days/day-04-tools-by-hand/parts/02-the-round-trip/2.1-two-channels-not-one.md` · level `foundation` · ids AG-04

Yesterday the model's commands and the world's data travelled in the same list of text turns, told apart only by a prefix you invented; today the commands move into a structurally separate channel — which is a real boundary rather than a convention, and which still does not stop a document from influencing the model.

### 2.2 - The call comes back parsed — deleting the parser you wrote yesterday
`days/day-04-tools-by-hand/parts/02-the-round-trip/2.2-the-call-comes-back-parsed.md` · level `working` · ids AG-04

A function_call step arrives with name as a string and arguments as a dictionary that is already a dictionary — so yesterday's parser is deleted, dispatch becomes one  unpacking, and the schema's property names become load-bearing because they are now Python keyword arguments.

### 2.3 - The tool-result turn — and the id that says which question you answered
`days/day-04-tools-by-hand/parts/02-the-round-trip/2.3-the-tool-result-turn.md` · level `working` · ids AG-04

A tool's result goes back as a function_result turn carrying the tool's name, the call_id of the call it answers, and the output as a list of content blocks — and the id is the field people skip, because with one tool in flight it looks redundant and with two it is the only thing that makes the exchange unambiguous.

### 2.4 - Re-send the steps as received — stop reconstructing the model's turn
`days/day-04-tools-by-hand/parts/02-the-round-trip/2.4-resend-the-steps-as-received.md` · level `working` · ids AG-04

With store=False you hold the whole conversation, and the model's own turns must go back exactly as they arrived — copied, not rebuilt — because a step carries fields you did not put there and do not need to understand, and a faithful copy is the only version that stays correct when they change.

### 3.1 - One door, one new parameter — why tools go through `ask` and not around it
`days/day-04-tools-by-hand/parts/03-rebuilding-the-loop/3.1-one-door-one-new-parameter.md` · level `working` · ids AG-04

ask gains one optional parameter and stays the only place in Sutra that touches the SDK — because every safety property this project has (the model pin, store=False, 429 handling, honest failure) lives at that door, and a second call site would have to rebuild all four, which nobody ever does.

### 3.2 - The loop that shrank — what the scaffolding was holding up
`days/day-04-tools-by-hand/parts/03-rebuilding-the-loop/3.2-the-loop-that-shrank.md` · level `working` · ids AG-04

Assembling the new loop is mostly deletion — the parser, the format block, the tool menu and the coaching branch all go — and what survives untouched is the part that was never about the protocol: the dispatch table, the step budget, the two species of error, and the two appends.

### 3.3 - Two calls in one turn — every call gets an answer, and nobody is served early
`days/day-04-tools-by-hand/parts/03-rebuilding-the-loop/3.3-two-calls-in-one-turn.md` · level `working` · ids AG-04

A model can request several tools in a single turn, so the loop reads every function_call step, executes each, appends one function_result per call carrying its own call_id, and does not go back to the model until all of them are answered — and Sutra's own two tools are a case where you mostly want to talk the model out of doing this.

### 4.1 - Validated is not correct — the argument that passes every check and means the wrong thing
`days/day-04-tools-by-hand/parts/04-the-limits/4.1-validated-is-not-correct.md` · level `production` · ids AG-04

A schema guarantees that ticket_id is a string that was provided — it cannot guarantee it is the ticket that exists, the ticket the user meant, or a ticket at all — so validation moving upstream removes a class of format errors and leaves every meaning error exactly where it was.

### 4.2 - The tool that is never called — and why forcing it is the last thing you try
`days/day-04-tools-by-hand/parts/04-the-limits/4.2-the-tool-that-is-never-called.md` · level `production` · ids AG-04

A model that answers in prose instead of calling your tool is almost never fixed by forcing a call — tool_choice: "any" turns never into always, which in a loop means the model can no longer say it is finished — and the fix is usually a description that states a trigger.

### 5.1 - The declaration is the new boundary — two lists that must never drift
`days/day-04-tools-by-hand/parts/05-containment/5.1-the-declaration-is-the-new-boundary.md` · level `production` · ids AG-04

Yesterday one dict answered "what can this agent do?"; today there are two lists in two files — what the model is told exists, and what your code will actually run — and the security question is no longer "what is in the table" but "do the two lists agree, and who would notice if they stopped".

### 5.2 - The argument a schema cannot check — whose ticket is it?
`days/day-04-tools-by-hand/parts/05-containment/5.2-the-argument-a-schema-cannot-check.md` · level `production` · ids AG-04

lookup_ticket(ticket_id) has no parameter for who is asking, so no schema, no validator and no dispatch table can decide whether this caller may read this ticket — and a tool written for a trusted caller becomes a data-leak the moment the caller is a model acting on text somebody else wrote.

### 6.1 - 💥 The call id you did not echo — a perfect answer, filed against the wrong question
`days/day-04-tools-by-hand/parts/06-failure-lab/6.1-the-call-id-you-did-not-echo.md` · level `production` · ids AG-04

Break the call_id pairing and the model receives two flawless tool results attached to the wrong questions — and because every individual piece of the system is working correctly, the failure presents as a confused model rather than as a bug in three lines of your code.

### 7.1 - 🅿️ Automatic function calling, declined — and the difference between that and tomorrow
`days/day-04-tools-by-hand/parts/07-the-automatic-door/7.1-automatic-function-calling-declined.md` · level `production` · ids AG-04

The SDK can run the whole loop for you — hand it Python functions, get a final answer — and Sutra declines, for one reason of principle and one of fact: a loop you cannot open is a loop you cannot put an approval gate, a budget or a redaction pass into, and it is not offered on the Interactions API anyway.

## Papers - read after the parts

### arXiv:2302.04761 - Toolformer: Language Models Can Teach Themselves to Use Tools — the premise, not the method
`days/day-04-tools-by-hand/papers/01-toolformer.md`

This is the paper that made "the model decides when to call a tool" a normal thing to say — and it is worth reading precisely because the half you built today is its premise, while its actual method was abandoned, which makes it the clearest case in this curriculum of a paper winning an argument and losing its technique.


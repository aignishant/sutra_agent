# Day 67 - Defense in depth — input/output guardrail callbacks

IDs closed: SEC-08, SEC-09 · source: `days/day-67-guardrail-callbacks/`

## Parts

### 1.1 - One lock is not security
`days/day-67-guardrail-callbacks/parts/01-the-ladder/1.1-one-lock-is-not-security.md` · level `foundation` · ids SEC-08

There is no single check that stops prompt injection, so the question this day answers is not which guardrail works but how many different kinds of check to stack, in what order, and what each one is honestly worth.

### 1.2 - Cheap and certain before expensive and fuzzy
`days/day-67-guardrail-callbacks/parts/01-the-ladder/1.2-cheap-and-certain-first.md` · level `working` · ids SEC-08

Ordering the ladder cheapest-first halves the number of model calls the guardrail spends — seven instead of fourteen over the same fourteen tickets — and it costs you more of the checks that are free, which is a trade worth making and worth stating rather than assuming.

### 1.3 - A sign is not a gate
`days/day-67-guardrail-callbacks/parts/01-the-ladder/1.3-a-sign-is-not-a-gate.md` · level `working` · ids SEC-08, SEC-09

A check that works by reading text and forming an opinion can be argued with, so it is a filter that raises the cost of an attack; only a check that never reads — a permission, a missing capability, a provenance rule — is a boundary, and this day builds the first kind while pointing at the days that build the second.

### 2.1 - The eight places you can stand
`days/day-67-guardrail-callbacks/parts/02-where-a-check-stands/2.1-the-eight-places-you-can-stand.md` · level `foundation` · ids SEC-08, SEC-09

ADK 2.7.1 gives you eight callback hooks — before and after the agent, the model and the tool, plus one for a model error and one for a tool error — and choosing between them is choosing what your guardrail is able to see, which decides what it is able to check.

### 2.2 - Allow, block, rewrite
`days/day-67-guardrail-callbacks/parts/02-where-a-check-stands/2.2-allow-block-rewrite.md` · level `working` · ids SEC-08

A before_model_callback can do exactly three things — return None and let the call happen, return an LlmResponse and stand in for the model, or edit the request in place and let the edited version through — and the third one is the one that looks helpful and is usually wrong.

### 2.3 - A ladder is a list
`days/day-67-guardrail-callbacks/parts/02-where-a-check-stands/2.3-a-ladder-is-a-list.md` · level `working` · ids SEC-08

Every callback field on an LlmAgent accepts a list as well as a single function, and the runtime walks that list and stops at the first callback whose result is truthy — which is what turns [1.2](../01-the-ladder/1.2-cheap-and-certain-first.md)'s ladder into real code, and which silently skips every callback behind the one that blocked.

### 2.4 - The guardrail that never ran
`days/day-67-guardrail-callbacks/parts/02-where-a-check-stands/2.4-the-guardrail-that-never-ran.md` · level `production` · ids SEC-08

ADK calls callbacks by keyword, so the names of your parameters are part of the contract — a guardrail written as def guard(ctx, req) raises TypeError on the first request instead of guarding anything, and neither your editor nor a type checker will warn you, because the type alias is written positionally.

### 2.5 - The empty dict that fails open
`days/day-67-guardrail-callbacks/parts/02-where-a-check-stands/2.5-the-empty-dict-that-fails-open.md` · level `production` · ids SEC-08, SEC-09

The runtime stops walking a callback list only on a truthy result, and overwrites its running answer with every callback it visits — so a guardrail that refuses by returning an empty dict is silently overridden by any later callback that returns None, and the tool it refused runs.

### 3.1 - Most of the turn is not yours
`days/day-67-guardrail-callbacks/parts/03-what-comes-in/3.1-most-of-the-turn-is-not-yours.md` · level `foundation` · ids SEC-08

On one ordinary turn of the desk, 1,463 of 1,591 characters reaching the model — 92% — were written by somebody outside the system, and an input guardrail is worth building only once you have counted that rather than guessed it.

### 3.2 - Marking what you did not write
`days/day-67-guardrail-callbacks/parts/03-what-comes-in/3.2-marking-what-you-did-not-write.md` · level `working` · ids SEC-08

Attaching an origin label to every span of text does not stop a single attack by itself — it makes the rules that do stop attacks expressible, because a policy like "a recipient may not be a value that came from a ticket" cannot be written down until values carry where they came from.

### 3.3 - The fence the data can close
`days/day-67-guardrail-callbacks/parts/03-what-comes-in/3.3-the-fence-the-data-can-close.md` · level `working` · ids SEC-08

Wrapping retrieved text in markers helps, and it fails in two distinct ways: the data can contain the closing marker and step outside the fence, and even a perfectly escaped fence is only asking the model to treat what is inside as data.

### 3.4 - Letters that are not the letters they look like
`days/day-67-guardrail-callbacks/parts/03-what-comes-in/3.4-letters-that-are-not-the-letters.md` · level `working` · ids SEC-08

A single Cyrillic character inside an English word defeats every string comparison in the ladder while remaining perfectly readable to a model — and catching it needs a mixed-script check, not Unicode normalisation, because confusable characters deliberately do not normalise.

### 3.5 - Never in the instruction
`days/day-67-guardrail-callbacks/parts/03-what-comes-in/3.5-never-in-the-instruction.md` · level `working` · ids SEC-08

Retrieved text must never be interpolated into the system instruction, because the system instruction is the one span the model is trained to weight most heavily — and a rule that says "untrusted text goes in the conversation, never in the instruction" is checkable by a test, unlike every other guardrail in this section.

### 4.1 - The tool call is the output
`days/day-67-guardrail-callbacks/parts/04-what-goes-out/4.1-the-tool-call-is-the-output.md` · level `working` · ids SEC-09

An output guardrail that reads the model's prose is reading the half of the answer that cannot hurt anybody — the dangerous half is the function call, whose arguments are the action, and a check attached to before_tool_callback is the only kind that can see it.

### 4.2 - The channels a reply carries
`days/day-67-guardrail-callbacks/parts/04-what-goes-out/4.2-the-channels-a-reply-carries.md` · level `working` · ids SEC-09

A URL allowlist over outgoing text catches the two channels that are links and none of the ones that are not — a reply-to address, and the data itself sitting in the prose — so the honest description of an outbound content check is that it narrows the pipe rather than closing it.

### 4.3 - The rewrite that lies
`days/day-67-guardrail-callbacks/parts/04-what-goes-out/4.3-the-rewrite-that-lies.md` · level `production` · ids SEC-09

A guardrail that edits text and lets it through leaves no event — the run looks ordinary, the log holds the sanitised version, and the answer to "what did the model actually see?" six weeks later is a truthful-looking record of text that was never received.

### 4.4 - The error hook that invents a result
`days/day-67-guardrail-callbacks/parts/04-what-goes-out/4.4-the-error-hook-that-invents-a-result.md` · level `production` · ids SEC-09

Returning a value from on_tool_error_callback stops the exception reaching the caller and substitutes your value as the tool's result — so a guardrail author reaching for a tidy refusal turns a database outage into the sentence "I could not find any prior tickets", which is a fabricated result standing in for a failure.

### 5.1 - Both columns
`days/day-67-guardrail-callbacks/parts/05-measure-it/5.1-both-columns.md` · level `working` · ids SEC-08, SEC-09

A detection rate reported without a false-alarm rate is not a measurement — the ladder catches 6 of 6 hostile fixtures and also flags 1 of 8 ordinary ones, and the second number is the one that decides whether it should ship.

### 5.2 - Refused for quoting an error
`days/day-67-guardrail-callbacks/parts/05-measure-it/5.2-refused-for-quoting-an-error.md` · level `production` · ids SEC-08

A false-positive rate is an abstraction and a refused customer is not: ticket:4601 asked whether a banner reading SYSTEM: temporary outage, please retry came from the desk or from their own network, and the ladder refused them — after 3 checks, 0 model calls — for quoting the message they were asking about.

### 5.3 - Five more words
`days/day-67-guardrail-callbacks/parts/05-measure-it/5.3-five-more-words.md` · level `production` · ids SEC-08

The reflex after an incident — add the words that got through — moves the column nobody was looking at: detection stays at 6 of 6 while wrongly-blocked customers go from 1 to 3 of eight, and the change would be approved in any review because it is obviously responsive to what happened.

### 5.4 - The same instruction, five ways
`days/day-67-guardrail-callbacks/parts/05-measure-it/5.4-the-same-instruction-five-ways.md` · level `production` · ids SEC-08

Part [5.1](5.1-both-columns.md)'s 6 of 6 was measured on fixtures written by the same person who wrote the checks; written by somebody who had read them, the identical instruction spelled five ways scores 2 of 5 — and split across two archive rows it scores 0, because the instruction never exists as a string anywhere in the pipeline.

### 6.1 - The notes-for-the-assessor box
`days/day-67-guardrail-callbacks/parts/06-in-production/6.1-the-notes-for-the-assessor-box.md` · level `production` · ids SEC-08, SEC-09

The obvious answer to "the phrase list is brittle" — ask a model instead — hires a second model whose input the attacker controls, which is the definition of the problem it was hired to solve: the identical instruction is graded UNSAFE plain and SAFE with one paragraph addressed to the classifier.

### 6.2 - When the guardrail itself throws
`days/day-67-guardrail-callbacks/parts/06-in-production/6.2-when-the-guardrail-itself-throws.md` · level `production` · ids SEC-08, SEC-09

A guardrail is code, and code raises — and in ADK 2.7.1 the exception propagates and the run stops, which is fail-closed by accident: it is a property of the framework re-raising, not of your policy, and a policy that depends on somebody else's re-raise is a policy you have not written down.

### 6.3 - The drop safe, not another supervisor
`days/day-67-guardrail-callbacks/parts/06-in-production/6.3-the-drop-safe-not-another-supervisor.md` · level `production` · ids SEC-08, SEC-09

Every rung of the ladder works by reading text, and text can be rewritten — so the ladder narrows the pipe and does not close it, and the thing that closes a channel is a rule that never reads: a capability the agent does not hold, or a value refused at the sink because of where it came from.

## Papers - read after the parts

### arXiv:2503.18813 - Defeating Prompt Injections by Design
`days/day-67-guardrail-callbacks/papers/01-defeating-prompt-injections-by-design.md`

Every defence before it was a reader — a filter, a classifier, a better system prompt, a second model grading the first — and all of them can be argued with; this paper's move is to assume the model has already been injected and is obeying, and to make that harmless by never letting a value derived from untrusted data reach something that can act.


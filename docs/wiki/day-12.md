# Day 12 - Structured output — a shape on the way out

IDs closed: ADK-13 · source: `days/day-12-structured-output/`

## Parts

### 1.1 - A shape on the answer
`days/day-12-structured-output/parts/01-the-shape-on-the-way-out/1.1-a-shape-on-the-answer.md` · level `foundation` · ids ADK-13

output_schema puts a declared shape on what the agent says, the mirror of what Day 10 put on what the model asks for — and on the simple path it becomes a response_schema on the request, so the provider enforces it rather than your prompt asking nicely.

### 1.2 - The answer with an address
`days/day-12-structured-output/parts/01-the-shape-on-the-way-out/1.2-the-answer-with-an-address.md` · level `working` · ids ADK-13

output_key writes the agent's final answer into session state — through exactly the mechanism Day 11 took apart, event.actions.state_delta[key] = result — and when output_schema is also set, what lands there is a parsed dictionary with the code fence stripped and every null field dropped.

### 1.3 - What output_schema accepts
`days/day-12-structured-output/parts/01-the-shape-on-the-way-out/1.3-what-output-schema-accepts.md` · level `working` · ids ADK-13

Five shapes, not one: a Pydantic model, a list of one, a list of primitives, a raw JSON-Schema dictionary and a types.Schema — and what lands in state is a dict, a list, or a bare value depending on which you chose.

### 1.4 - 🅿️ The sheet you fill in before you are called
`days/day-12-structured-output/parts/01-the-shape-on-the-way-out/1.4-the-sheet-you-fill-in-before-you-are-called.md` · level `production` · ids ADK-13

input_schema is output_schema's mirror — it types what goes into an agent — and it only does anything when the agent is used as a tool by another agent, which is why it is parked until Phase 8.

### 2.1 - A schema a model can fill
`days/day-12-structured-output/parts/02-schemas-in-practice/2.1-a-schema-a-model-can-fill.md` · level `working` · ids ADK-13

Write the schema for the thing that has to fill it in, not for the thing that will store it: flat rather than nested, named in the reader's words, closed sets wherever a set is closed, and as few required fields as the job genuinely has.

### 2.2 - Optional, default, and null
`days/day-12-structured-output/parts/02-schemas-in-practice/2.2-optional-default-and-null.md` · level `working` · ids ADK-13

Required, defaulted and nullable are three different instructions to the model — and by the time the answer reaches session state, exclude_none=True has made "the model said null" and "the model skipped it" indistinguishable.

### 2.3 - The descriptions that do not arrive
`days/day-12-structured-output/parts/02-schemas-in-practice/2.3-the-descriptions-that-do-not-arrive.md` · level `production` · ids ADK-13

On the path Sutra is actually on, Field(description=...) and numeric bounds like ge/le are stripped out of what the model is shown — Pydantic still enforces them afterwards, so the constraint survives as a retry loop instead of as an instruction.

### 2.4 - The schema is the prompt again
`days/day-12-structured-output/parts/02-schemas-in-practice/2.4-the-schema-is-the-prompt-again.md` · level `working` · ids ADK-13

A schema is text, sent on every turn, exactly like the instruction from Day 6 and the tool descriptions from Day 10 — so it is a budget line, and the way to shrink it is fewer fields, never shorter names.

### 3.1 - The rule that changed
`days/day-12-structured-output/parts/03-schema-and-tools-together/3.1-the-rule-that-changed.md` · level `working` · ids ADK-13

"An agent with an output_schema cannot have tools" was true, is quoted everywhere, and is not how ADK 2.x behaves — but the thing that replaced it is decided by a model capability, and on Sutra's free Gemini lane that capability is False.

### 3.2 - The tool ADK injects
`days/day-12-structured-output/parts/03-schema-and-tools-together/3.2-the-tool-adk-injects.md` · level `working` · ids ADK-13

On the workaround path ADK adds a tool called set_model_response, whose parameters are your schema's fields, and appends an instruction telling the model to answer through it — so structured output stops being a decoding constraint and becomes a tool call.

### 3.3 - What that costs you
`days/day-12-structured-output/parts/03-schema-and-tools-together/3.3-what-that-costs-you.md` · level `production` · ids ADK-13

The bill for the workaround path, itemised: no extra model call on the happy path, one per rejection, 297 characters of instruction you did not write, an extra tool in the list, every field description and numeric bound gone — and enforcement that is a request rather than a constraint.

### 4.1 - Valid is not true
`days/day-12-structured-output/parts/04-when-a-schema-lies/4.1-valid-is-not-true.md` · level `production` · ids ADK-13

A schema checks shape, and shape is not meaning: for one ticket, four different triages pass validation and only one of them is right — so a green validate_schema proves the answer is parseable, never that it is correct.

### 4.2 - The field that was always filled
`days/day-12-structured-output/parts/04-when-a-schema-lies/4.2-the-field-that-was-always-filled.md` · level `production` · ids ADK-13

A required field is an instruction to always have an answer, so a required field for a fact the input may not contain is a machine for manufacturing plausible values — and the fix is one character of type annotation.

### 5.1 - 💥 The schema that silenced the agent
`days/day-12-structured-output/parts/05-failure-lab/5.1-the-schema-that-silenced-the-agent.md` · level `production` · ids ADK-13

Today's deliberate failure: a schema every field of which is required and closed, so "I cannot triage this" is not a value the agent is able to produce — and every empty, spam or nonsense input comes back as a confident triage, with no error anywhere.

### 6.1 - output_key is how agents talk
`days/day-12-structured-output/parts/06-in-the-graph/6.1-output-key-is-how-agents-talk.md` · level `production` · ids ADK-13

One agent's output_key writes into state and the next agent's {key} template reads it out — so output_schema plus output_key plus a templated instruction is the whole hand-off mechanism of Phase 8, assembled today from three things you already have.

### 6.2 - Testing structured output for free
`days/day-12-structured-output/parts/06-in-the-graph/6.2-testing-structured-output-for-free.md` · level `production` · ids ADK-13

Four assertions that need no model and no key: the schema can decline, only always-answerable fields are required, golden replies parse to expected values, and bad replies are rejected — and the fifth question, is the answer right?, cannot be asked here at all.

## Papers - read after the parts

### arXiv:2307.09702 - Efficient Guided Generation for Large Language Models
`days/day-12-structured-output/papers/01-guided-generation.md`

Reformulate generation as walking a finite-state machine over characters, then precompute an index from each machine state to the set of vocabulary tokens allowed there — and constraining output stops being a per-token search over the vocabulary and becomes a dictionary lookup.


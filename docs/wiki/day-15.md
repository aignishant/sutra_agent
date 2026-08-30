# Day 15 - Toolsets and OpenAPI — tools you did not write

IDs closed: ADK-17 · source: `days/day-15-toolsets-and-openapi/`

## Parts

### 1.1 - One line, many tools
`days/day-15-toolsets-and-openapi/parts/01-crate-not-list/1.1-one-line-many-tools.md` · level `foundation` · ids ADK-17

An agent's tools=[...] list does not have to contain tools: one entry can be a toolset, an object ADK asks for its contents at the moment the agent needs them.

### 1.2 - One method, and an import that is not where you would look
`days/day-15-toolsets-and-openapi/parts/01-crate-not-list/1.2-one-method-and-the-import.md` · level `working` · ids ADK-17

BaseToolset requires you to write exactly one method — async get_tools(...) — and it is imported from google.adk.tools.base_toolset, not from google.adk.tools, where its close relative BaseTool lives.

### 1.3 - What the crate is allowed to see
`days/day-15-toolsets-and-openapi/parts/01-crate-not-list/1.3-what-the-crate-can-see.md` · level `working` · ids ADK-17

get_tools is handed a ReadonlyContext carrying the session's state, the agent's name and the user's id, so a crate can decide its inventory from what has already happened — and it may also be handed nothing at all, which is why the None check is not optional.

### 2.1 - The wrapper ADK actually calls
`days/day-15-toolsets-and-openapi/parts/02-when-asked/2.1-the-wrapper-adk-actually-calls.md` · level `working` · ids ADK-17

The agent never calls your get_tools; it calls get_tools_with_prefix, a method on the base class that calls yours and then does two more things to the answer — so testing through your own method tests something the agent never does.

### 2.2 - Asked once a run, not once a turn
`days/day-15-toolsets-and-openapi/parts/02-when-asked/2.2-asked-once-a-run.md` · level `production` · ids ADK-17

get_tools is called exactly once per request, no matter how many model calls or tool calls that request contains, because get_tools_with_prefix caches the answer against the request's invocation_id.

### 2.3 - Two crates, one name
`days/day-15-toolsets-and-openapi/parts/02-when-asked/2.3-two-crates-one-name.md` · level `working` · ids ADK-17

Two toolsets can offer tools with the same name, and the later one shadows the earlier one with only a log warning — tool_name_prefix is the constructor argument that stops it, by renaming a copy of every tool the crate hands back.

### 3.1 - A filter you are given, and have to apply yourself
`days/day-15-toolsets-and-openapi/parts/03-the-filter/3.1-a-filter-you-have-to-apply-yourself.md` · level `production` · ids ADK-17

tool_filter is accepted by every toolset's constructor and applied by none of them unless the subclass calls self._is_tool_selected inside get_tools — so a filter you set can be stored, readable, and doing absolutely nothing.

### 3.2 - A list of names, or a question
`days/day-15-toolsets-and-openapi/parts/03-the-filter/3.2-a-list-of-names-or-a-question.md` · level `working` · ids ADK-17

tool_filter takes either a list of exact tool names — an allowlist that cannot drift — or a callable that is asked about each tool and can see the session, and the choice between them is a choice about what happens when somebody adds a tool you have never heard of.

### 4.1 - The manual the service publishes about itself
`days/day-15-toolsets-and-openapi/parts/04-machine-packed/4.1-the-manual-the-service-publishes.md` · level `foundation` · ids ADK-17

An OpenAPI description is a machine-readable manual an HTTP service publishes about itself — every operation, its address, its arguments and a sentence about what it does — and it contains, in the service's own words, everything you would otherwise write by hand into a tool.

### 4.2 - Spec in, tools out
`days/day-15-toolsets-and-openapi/parts/04-machine-packed/4.2-spec-in-tools-out.md` · level `working` · ids ADK-17

OpenAPIToolset takes a service's description and produces one working tool per operation — name, description, arguments and a real HTTP call — with no wrapper code written by anybody.

### 4.3 - Where each part of a generated tool comes from
`days/day-15-toolsets-and-openapi/parts/04-machine-packed/4.3-where-each-part-of-a-tool-comes-from.md` · level `working` · ids ADK-17

Every field of a generated tool traces to one field of the description — name from operationId, description from description or summary, arguments from parameters, URL from servers[0] plus the path — which is Day 4's translation table with a machine doing the typing.

### 4.4 - The name you did not choose
`days/day-15-toolsets-and-openapi/parts/04-machine-packed/4.4-the-name-you-did-not-choose.md` · level `working` · ids ADK-17

When an operation has no operationId, ADK builds a name from the path and the method — /incidents becomes incidents_get — and when the operationId is longer than sixty characters it is cut off mid-word, both without a word of warning.

### 4.5 - One key for the whole crate
`days/day-15-toolsets-and-openapi/parts/04-machine-packed/4.5-one-key-for-the-whole-crate.md` · level `production` · ids ADK-17

auth_scheme and auth_credential are given to the toolset once and applied to every tool it generates, so a forty-operation API is authenticated by one pair of constructor arguments and one line in .env.

### 5.1 - The page and the package disagree
`days/day-15-toolsets-and-openapi/parts/05-where-it-bites/5.1-the-page-and-the-package-disagree.md` · level `production` · ids ADK-17

adk.dev says a generated tool's description comes from "the summary or description"; the installed package reads description or summary, so when a spec has both — and good specs do — the model is shown the one the page names second.

### 5.2 - A crate that never changes its mind
`days/day-15-toolsets-and-openapi/parts/05-where-it-bites/5.2-a-crate-that-never-changes-its-mind.md` · level `production` · ids ADK-17

OpenAPIToolset parses the spec in its constructor and stores the resulting tools on the instance, so it is the one toolset whose answer can never change — the vendor's document drifts and the crate does not notice.

### 6.1 - 💥 The crate that arrived empty
`days/day-15-toolsets-and-openapi/parts/06-failure-lab/6.1-the-crate-that-arrived-empty.md` · level `production` · ids ADK-17

When a toolset raises, ADK catches the exception, logs one WARNING, and gives the agent zero tools from that crate — so the run succeeds, the answer is confident, and it is wrong.

### 7.1 - The wrappers we are not installing
`days/day-15-toolsets-and-openapi/parts/07-in-production/7.1-the-wrappers-we-are-not-installing.md` · level `production` · ids ADK-17

ADK ships adapters that turn other frameworks' tools into ADK tools, and four toolsets besides the one you used today — Sutra installs none of the adapters, and 🅿️ knowing why not is the skill this part is teaching.

### 7.2 - Testing a toolset without a model
`days/day-15-toolsets-and-openapi/parts/07-in-production/7.2-testing-a-toolset-without-a-model.md` · level `production` · ids ADK-17

A toolset is tested by resolving it through get_tools_with_prefix and asserting on the names that come out — five assertions, no API key, no model, and one of them is the only thing in this day that turns [6.1](../06-failure-lab/6.1-the-crate-that-arrived-empty.md)'s silence into a red build.

### 7.3 - Where trust moved
`days/day-15-toolsets-and-openapi/parts/07-in-production/7.3-where-trust-moved.md` · level `production` · ids ADK-17

Generating tools does not remove the need to vouch for them; it moves what you vouch for — from lines of your own code to a document and an endpoint you do not control — and the controls that follow from that are different controls.

## Papers - read after the parts

### doi:10.1145/2080.357392 - Implementing remote procedure calls
`days/day-15-toolsets-and-openapi/papers/01-implementing-remote-procedure-calls.md`

It proposed that calling a procedure on another machine should look like calling one locally, with the connecting code generated from an interface description rather than written by hand — and the generation survived completely while the looking-like-a-local-call did not.


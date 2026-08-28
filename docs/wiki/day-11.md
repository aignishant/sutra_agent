# Day 11 - Tool context and tool design — the parameter the model never sees

IDs closed: ADK-12, AG-06 · source: `days/day-11-tool-context/`

## Parts

### 1.1 - The parameter the model never sees
`days/day-11-tool-context/parts/01-the-extra-parameter/1.1-the-parameter-the-model-never-sees.md` · level `foundation` · ids ADK-12

Add a parameter annotated ToolContext to a tool and ADK removes it from the schema the model sees while filling it in at call time — so the tool gains access to the session, the run and the event's actions without the model knowing it exists.

### 1.2 - Detected by type, not by name
`days/day-11-tool-context/parts/01-the-extra-parameter/1.2-detected-by-type-not-by-name.md` · level `working` · ids ADK-12

ADK finds the context parameter by looking for the first parameter annotated with a context type, whatever it is called — falling back to the literal name tool_context when nothing is annotated — so a parameter that is neither annotated nor named tool_context is silently offered to the model.

### 1.3 - One card, several doors
`days/day-11-tool-context/parts/01-the-extra-parameter/1.3-one-card-several-doors.md` · level `working` · ids ADK-12

One parameter opens six doors — session state, the event's actions, the run and user identifiers, artifacts, memory search and the confirmation hook — and every one of them is a subsystem you have already met and could not previously reach from inside a tool.

### 1.4 - The folded paper under the chair leg
`days/day-11-tool-context/parts/01-the-extra-parameter/1.4-the-folded-paper-under-the-chair.md` · level `working` · ids ADK-12

Giving the context parameter a = None default changes nothing about how ADK calls your tool and everything about how it fails when something else does — it converts a loud TypeError at the call into a quiet AttributeError several lines into the body.

### 2.1 - Writing on the carbon copy
`days/day-11-tool-context/parts/02-state-from-a-tool/2.1-writing-on-the-carbon-copy.md` · level `working` · ids ADK-12

tool_context.state["k"] = v is not a helper that saves something later — the write goes into the session's dictionary and into tool_context.actions.state_delta in the same act, and that delta is literally the state_delta on the event ADK emits for your tool's result.

### 2.2 - Reading what you did not fetch
`days/day-11-tool-context/parts/02-state-from-a-tool/2.2-reading-what-you-did-not-fetch.md` · level `working` · ids ADK-12

A tool can read any key in session state, which means its result depends on inputs the model never supplied and the schema never mentioned — the same call, twice, can honestly return two different answers.

### 2.3 - What not to put on the noticeboard
`days/day-11-tool-context/parts/02-state-from-a-tool/2.3-what-not-to-put-on-the-noticeboard.md` · level `production` · ids ADK-12

Everything a tool writes to state goes into an event, and events are the run's permanent record — so state takes handles, not payloads, never a secret, and anything genuinely temporary goes under the temp: prefix, which ADK strips from the event before it is stored.

### 3.1 - One tool, one job
`days/day-11-tool-context/parts/03-designing-a-tool/3.1-one-tool-one-job.md` · level `working` · ids AG-06

A tool that takes an action or mode parameter has smuggled a second decision into the model's turn, and worse, it has thrown away the schema's ability to say what is required — split it, and the declarations barely cost more.

### 3.2 - Name it for the model
`days/day-11-tool-context/parts/03-designing-a-tool/3.2-name-it-for-the-model.md` · level `working` · ids AG-06

The Python function's __name__ is sent to the model verbatim as the tool's name, ADK validates nothing about it — not spaces, not duplicates — and two tools sharing a name means both declarations are advertised while only the last one can ever be called.

### 3.3 - Arguments the model can supply
`days/day-11-tool-context/parts/03-designing-a-tool/3.3-arguments-the-model-can-supply.md` · level `working` · ids AG-06

A parameter is a question you are asking the model, so only ask for things the conversation actually contains — identity comes from the context, "now" comes from the clock, and closed sets come from a Literal, because a required field with no available answer gets filled in anyway.

### 3.4 - Two tools that overlap
`days/day-11-tool-context/parts/03-designing-a-tool/3.4-two-tools-that-overlap.md` · level `production` · ids AG-06

[3.1](3.1-one-tool-one-job.md)'s rule pushed apart; this is the failure at the other end — two tools whose descriptions could each be the other's, where the fix is not a longer description but a contrastive one that names its sibling and says when not to use it.

### 4.1 - The line between read and write
`days/day-11-tool-context/parts/04-blast-radius/4.1-the-line-between-read-and-write.md` · level `production` · ids AG-06

A tool's blast radius is decided by one question — does it change anything? — and the answer sorts every tool you will ever write into two piles that deserve completely different treatment: reads that can be wrong, and writes that can be irreversible.

### 4.2 - The identity a tool needs
`days/day-11-tool-context/parts/04-blast-radius/4.2-the-identity-a-tool-needs.md` · level `production` · ids ADK-12

Identity is the one input a tool must never accept as an argument: take it from tool_context.user_id, which came from the session your application opened after authenticating a person — because a user_id in the schema is an authorisation decision handed to a text generator.

### 5.1 - 💥 The previous patient's file
`days/day-11-tool-context/parts/05-failure-lab/5.1-the-previous-patients-file.md` · level `production` · ids ADK-12

Today's deliberate failure: a ToolContext stashed in a module-level variable, which works perfectly in every test and, the moment two conversations are in flight in one process, writes one person's notes into another person's record.

### 6.1 - A tool without a model
`days/day-11-tool-context/parts/06-in-production/6.1-a-tool-without-a-model.md` · level `production` · ids ADK-12

Build a ToolContext by hand — a session service, a session, an invocation context and an EventActions — call your tool directly, and assert on both what it returned and what landed in actions.state_delta; no model, no key, no network, no quota.

### 6.2 - 🅿️ Artifacts and memory from a tool
`days/day-11-tool-context/parts/06-in-production/6.2-artifacts-and-memory-from-a-tool.md` · level `production` · ids ADK-12

Two of [1.3](../01-the-extra-parameter/1.3-one-card-several-doors.md)'s doors — save_artifact for bytes that outlive a turn and search_memory for recall across conversations — are reachable from any tool today, need their service configured on the runner, and Sutra is deliberately not walking through either yet.


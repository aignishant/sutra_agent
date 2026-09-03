# Day 17 - Session state — prefixes, scopes and lifetimes

IDs closed: ADK-19, ADK-20 · source: `days/day-17-state-scopes-and-lifetimes/`

## Parts

### 1.1 - The transcript is not a database
`days/day-17-state-scopes-and-lifetimes/parts/01-form-not-story/1.1-the-transcript-is-not-a-database.md` · level `foundation` · ids ADK-19

A session's history is a story written for a model to read; state is a small labelled form attached to it, written for your code to read — and the difference decides whether "this ticket is high severity" is a fact you can look up or a sentence you have to search for.

### 1.2 - What may live in state
`days/day-17-state-scopes-and-lifetimes/parts/01-form-not-story/1.2-what-may-live-in-state.md` · level `working` · ids ADK-19

State holds small serializable values — strings, numbers, booleans and simple lists or dictionaries of those — and nothing enforces it today, so the object you put in works perfectly until the day the session has to be written to a database.

### 1.3 - The pad and the rail
`days/day-17-state-scopes-and-lifetimes/parts/01-form-not-story/1.3-the-pad-and-the-rail.md` · level `working` · ids ADK-19

session.state is not a dictionary: it is a State object holding two dictionaries — what is already committed and what you have changed but not yet committed — and the second one is exactly what travels inside the next event.

### 2.1 - The prefix is the lifetime
`days/day-17-state-scopes-and-lifetimes/parts/02-four-lifetimes/2.1-the-prefix-is-the-lifetime.md` · level `foundation` · ids ADK-20

Four prefixes, four lifetimes, chosen by the name of the key alone: no prefix means this conversation, user: means this person everywhere, app: means everyone, and temp: means this one question and then it is gone.

### 2.2 - An invocation is not a session
`days/day-17-state-scopes-and-lifetimes/parts/02-four-lifetimes/2.2-an-invocation-is-not-a-session.md` · level `working` · ids ADK-20

An invocation is one user message answered end to end — every tool call and model call in between — and a session holds many of them, which is why temp: state can be handed from one tool to the next and is gone by the time the next question arrives.

### 2.3 - Where user: and app: live
`days/day-17-state-scopes-and-lifetimes/parts/02-four-lifetimes/2.3-where-user-and-app-live.md` · level `working` · ids ADK-20

user: and app: keys are not stored on the session at all: the service keeps them in separate places, strips the prefix on the way in, and re-attaches it every time a session is fetched — which is why a brand-new conversation already knows things and why deleting a session deletes none of them.

### 2.4 - Why temp: exists
`days/day-17-state-scopes-and-lifetimes/parts/02-four-lifetimes/2.4-why-temp-exists.md` · level `production` · ids ADK-20

temp: is the answer to a cost problem, not a tidiness one: a bulky intermediate written as ordinary state is carried by every later read and write of that session for ever, and the same twelve turns measured here cost 57,530 bytes of state kept and 2 bytes shredded.

### 3.1 - Writing from inside a tool
`days/day-17-state-scopes-and-lifetimes/parts/03-three-safe-writes/3.1-writing-from-inside-a-tool.md` · level `working` · ids ADK-19

Inside a tool or a callback you write state with an ordinary assignment — tool_context.state["severity"] = "high" — and the framework collects your writes into the event it is about to append, so the change is recorded, attributed and committed without you doing anything else.

### 3.2 - The carbon copy
`days/day-17-state-scopes-and-lifetimes/parts/03-three-safe-writes/3.2-the-carbon-copy.md` · level `working` · ids ADK-19

output_key="last_triage" is one argument that makes the agent's final text land in state as well as in the conversation — and if the agent also has an output_schema, what lands is the parsed object rather than the string.

### 3.3 - Writing from outside a run
`days/day-17-state-scopes-and-lifetimes/parts/03-three-safe-writes/3.3-writing-from-outside-a-run.md` · level `working` · ids ADK-19

When no agent is running — a script, a nightly job, an intake process — you write state by building an event whose only cargo is the change and appending it through the session service, which keeps the write inside the history exactly like every other one.

### 4.1 - State steers the next turn
`days/day-17-state-scopes-and-lifetimes/parts/04-state-in-the-prompt/4.1-state-steers-the-next-turn.md` · level `working` · ids ADK-19

A {key} in an agent's instruction is filled from state before the model sees it, so state is not only something the conversation writes — it is something that changes what the next turn is told.

### 4.2 - The brace that raises
`days/day-17-state-scopes-and-lifetimes/parts/04-state-in-the-prompt/4.2-the-brace-that-raises.md` · level `production` · ids ADK-19

A placeholder for a key that is not in state raises KeyError while the request is being built — and the exception does not reach your loop, so what you actually see is an agent that produced no answer at all.

### 5.1 - Declaring the boxes
`days/day-17-state-scopes-and-lifetimes/parts/05-a-schema-for-state/5.1-declaring-the-boxes.md` · level `working` · ids ADK-19

state_schema lets an agent declare, as a pydantic model, which state keys exist and what type each one holds — and a write to a key that is not declared raises StateSchemaError, which is how a misspelled key stops being a silent new key.

### 5.2 - What the schema does not do
`days/day-17-state-scopes-and-lifetimes/parts/05-a-schema-for-state/5.2-what-the-schema-does-not-do.md` · level `production` · ids ADK-19

state_schema checks the name of every unprefixed key and validates its type without converting it — so a declared int field happily stores the string "4521", and every user:, app: and temp: key skips the check entirely.

### 6.1 - 💥 The write that was never written
`days/day-17-state-scopes-and-lifetimes/parts/06-failure-lab/6.1-the-write-that-was-never-written.md` · level `production` · ids ADK-19

Assigning to a fetched session's state — session.state["k"] = v — is the natural thing to write, and it changes a copy: no event, no commit, no error, and the value is gone the next time anybody asks the service for that session.

### 7.1 - Testing state without a model
`days/day-17-state-scopes-and-lifetimes/parts/07-in-production/7.1-testing-state-without-a-model.md` · level `production` · ids ADK-19, ADK-20

Every claim this day makes is assertable with no key and no network — scopes, trimming, the lost write, the tool's delta, the declared keys and the instruction's placeholders — and the tests that check them all read back through the session service, because reading the object you just wrote to is what hides the day's worst bug.

### 7.2 - What belongs in state
`days/day-17-state-scopes-and-lifetimes/parts/07-in-production/7.2-what-belongs-in-state.md` · level `production` · ids ADK-20

State is for small structured facts your code will branch on; bytes go to artifacts, secrets stay in the environment, and the two scopes with the longest lives — user: and app: — need a written owner, because nothing checks them and nothing ever clears them.

### 7.3 - State as a trace
`days/day-17-state-scopes-and-lifetimes/parts/07-in-production/7.3-state-as-a-trace.md` · level `production` · ids ADK-19

Because every state change rides inside an event, the history answers a question the state cannot: who set this, when, and what was it before — and that is the whole payoff for the ceremony of writing through events.


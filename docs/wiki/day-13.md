# Day 13 - Callbacks — four doors and one rule

IDs closed: ADK-14, ADK-15 · source: `days/day-13-callbacks-four-doors/`

## Parts

### 1.1 - The function you never call
`days/day-13-callbacks-four-doors/parts/01-the-four-doors/1.1-the-function-you-never-call.md` · level `foundation` · ids ADK-14, ADK-15

A callback is a plain Python function that you write, hand to the agent once, and then never call yourself: ADK calls it for you at a fixed moment in the run, and what it returns decides whether the thing behind that moment still happens.

### 1.2 - The names are the contract
`days/day-13-callbacks-four-doors/parts/01-the-four-doors/1.2-the-names-are-the-contract.md` · level `working` · ids ADK-14, ADK-15

ADK calls your callback by keyword, so the parameter names in your def line are not yours to choose: rename llm_request to request and the run dies with a TypeError that names your own function.

### 1.3 - `None` means carry on
`days/day-13-callbacks-four-doors/parts/01-the-four-doors/1.3-none-means-carry-on.md` · level `working` · ids ADK-14, ADK-15

Every one of the six doors obeys one rule: return None and the thing behind the door happens normally; return anything else and your value replaces it, so the model call or the tool call never occurs at all.

### 1.4 - A list, not just a function
`days/day-13-callbacks-four-doors/parts/01-the-four-doors/1.4-a-list-not-just-a-function.md` · level `working` · ids ADK-14, ADK-15

Every callback field also accepts a list of functions, run in the order you listed them, and the first one that returns something other than None stops the rest — so the order you write them in is a policy decision, not a formatting choice.

### 2.1 - What is actually in the request
`days/day-13-callbacks-four-doors/parts/02-the-model-doors/2.1-what-is-actually-in-the-request.md` · level `working` · ids ADK-14

before_model_callback hands you the complete LlmRequest a fraction of a second before it is sent — the model name, the system instruction, every turn of history and every tool declaration — which makes it the first place in this curriculum where you can see what a model call actually costs.

### 2.2 - Editing the request in place
`days/day-13-callbacks-four-doors/parts/02-the-model-doors/2.2-editing-the-request-in-place.md` · level `working` · ids ADK-14

The llm_request you are handed is the real object, not a copy, so a before_model_callback changes what the model sees by mutating it and still returning None — returning a value would cancel the call instead of shaping it.

### 2.3 - The call that never happened
`days/day-13-callbacks-four-doors/parts/02-the-model-doors/2.3-the-call-that-never-happened.md` · level `production` · ids ADK-14

A before_model_callback that returns an LlmResponse short-circuits the model call: no request leaves the machine, no quota is spent, and — because ADK increments its call counter after the callback — the skipped call does not count against max_llm_calls either.

### 2.4 - Reading the reply first
`days/day-13-callbacks-four-doors/parts/02-the-model-doors/2.4-reading-the-reply-first.md` · level `working` · ids ADK-14

after_model_callback receives the model's reply before anything downstream does, so it is the one place where a leaked secret can be removed, a malformed answer replaced, or a refusal detected — and returning a new LlmResponse substitutes yours for the model's.

### 2.5 - The door that fires on every chunk
`days/day-13-callbacks-four-doors/parts/02-the-model-doors/2.5-the-door-that-fires-on-every-chunk.md` · level `production` · ids ADK-14

after_model_callback fires once per response the model layer yields, not once per model call — so under streaming it runs on every fragment, and a check written for a whole reply will be looking at a piece of one.

### 3.1 - The chokepoint, restored
`days/day-13-callbacks-four-doors/parts/03-the-tool-doors/3.1-the-chokepoint-restored.md` · level `working` · ids ADK-15

before_tool_callback runs immediately before every tool call with the tool object, the parsed arguments and the session context in hand — which makes it the single place in an ADK agent where every tool call can be seen, counted and decided on, no matter which entry point started the run.

### 3.2 - Refusing a tool call honestly
`days/day-13-callbacks-four-doors/parts/03-the-tool-doors/3.2-refusing-a-tool-call-honestly.md` · level `production` · ids ADK-15

Returning a dict from before_tool_callback stops the tool and hands your dict to the model as if the tool had produced it — so the refusal has to say, in the dict, that it is a refusal and why, or you have taught your own agent something false.

### 3.3 - The result, on its way back
`days/day-13-callbacks-four-doors/parts/03-the-tool-doors/3.3-the-result-on-its-way-back.md` · level `working` · ids ADK-15

after_tool_callback sees what the tool returned before the model does, and returning a dict from it replaces that result — which is where a result gets trimmed, stripped of fields the model has no business seeing, or annotated, without touching the tool.

### 3.4 - The doors that only open on an error
`days/day-13-callbacks-four-doors/parts/03-the-tool-doors/3.4-the-doors-that-only-open-on-an-error.md` · level `production` · ids ADK-14, ADK-15

When a tool or a model call raises, ADK 2.x lets the exception out — unless on_tool_error_callback or on_model_error_callback returns a value, in which case that value becomes the result and the exception is swallowed, which is a decision you make deliberately and not a default you inherit.

### 4.1 - Truthy is not the same as not-`None`
`days/day-13-callbacks-four-doors/parts/04-where-the-rule-bites/4.1-truthy-is-not-the-same-as-not-none.md` · level `production` · ids ADK-15

The documentation says a tool callback chain runs "until a callback does not return None", and the code stops on a truthy value while keeping whatever the last callback returned — so an empty dict skips the tool, and two functions in the other order produce the opposite outcome.

### 4.2 - The plugin goes first
`days/day-13-callbacks-four-doors/parts/04-where-the-rule-bites/4.2-the-plugin-goes-first.md` · level `production` · ids ADK-14, ADK-15

At every one of the six doors ADK runs the application's plugins before the agent's callbacks, and a plugin that returns a value stops the agent's callbacks from running at all — so a callback is not the outermost layer of your system, and tomorrow's subject already outranks today's.

### 4.3 - The tool you did not write
`days/day-13-callbacks-four-doors/parts/04-where-the-rule-bites/4.3-the-tool-you-did-not-write.md` · level `production` · ids ADK-15

On Sutra's path, yesterday's output_schema makes ADK inject a tool called set_model_response, and your tool-door callbacks fire for it exactly as they do for your own — so a policy that names tools, counts them or trims their results is already meeting one it has never heard of.

### 5.1 - 💥 The note that became the result
`days/day-13-callbacks-four-doors/parts/05-failure-lab/5.1-the-note-that-became-the-result.md` · level `production` · ids ADK-15

Add one return to a logging callback and every tool in the agent stops running: the log record becomes the tool's result, the model reasons over it confidently, and nothing anywhere raises, prints a warning or looks different — which is why this is the day's deliberate failure.

### 6.1 - Testing a callback without a model
`days/day-13-callbacks-four-doors/parts/06-in-production/6.1-testing-a-callback-without-a-model.md` · level `production` · ids ADK-14, ADK-15

A callback is a plain function, so most of it is tested by calling it — and the one assertion that catches [5.1](../05-failure-lab/5.1-the-note-that-became-the-result.md), "the tool actually ran", needs a whole agent run, which a scripted local model gives you for no key and no quota.

### 6.2 - What belongs in a callback
`days/day-13-callbacks-four-doors/parts/06-in-production/6.2-what-belongs-in-a-callback.md` · level `production` · ids ADK-14, ADK-15

A callback runs on the request path, inside an async event loop, on every model call and every tool call — so it must be fast, non-blocking and unable to raise, and anything that is none of those three belongs somewhere else.


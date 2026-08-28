# Day 10 - Function tools in ADK — the forms print themselves

IDs closed: ADK-10, ADK-11 · source: `days/day-10-function-tools/`

## Parts

### 1.1 - The declaration you no longer write
`days/day-10-function-tools/parts/01-the-form-fills-itself/1.1-the-declaration-you-no-longer-write.md` · level `foundation` · ids ADK-10

Put a Python function in an agent's tools list and ADK builds the JSON declaration from it — the name from the function's name, the description from its docstring, the parameters from its type hints — so the dictionary you hand-wrote on Day 4 becomes something the code generates from the code.

### 1.2 - The docstring is the description
`days/day-10-function-tools/parts/01-the-form-fills-itself/1.2-the-docstring-is-the-description.md` · level `working` · ids ADK-10

The whole docstring becomes the tool's description — summary, Args: block and all — and on google-adk 2.7.1 the parameter descriptions arrive at the model as prose inside that text rather than as description fields in the schema, which changes how you should write one.

### 1.3 - Type hints are the schema
`days/day-10-function-tools/parts/01-the-form-fills-itself/1.3-type-hints-are-the-schema.md` · level `working` · ids ADK-10

The parameters half of the declaration is generated from your type hints and defaults: an annotated parameter with no default is required and typed, a defaulted one is optional and carries its default, and an unannotated one becomes a parameter with no type at all.

### 1.4 - The wrapper that arrives late
`days/day-10-function-tools/parts/01-the-form-fills-itself/1.4-the-wrapper-that-arrives-late.md` · level `working` · ids ADK-10

agent.tools holds exactly what you put in it — a plain function stays a plain function — and the FunctionTool is built later, when something asks for canonical_tools(), which is why a broken tool signature survives import and every test that does not run the agent.

### 2.1 - Return a dict with a status
`days/day-10-function-tools/parts/02-what-a-tool-returns/2.1-return-a-dict-with-a-status.md` · level `working` · ids ADK-11

A tool's return value goes back into the prompt as text the model reads, so it should be a dictionary with a status key and named fields — not a bare string, and not a blob the model has to interpret.

### 2.2 - The bare value the spec rewrites
`days/day-10-function-tools/parts/02-what-a-tool-returns/2.2-the-bare-value-the-spec-rewrites.md` · level `working` · ids ADK-11

Return anything that is not a dictionary and ADK wraps it as {"result": <your value>} on its way into the conversation — because the function-response format requires an object — so the model sees a key you never chose.

### 2.3 - A failed tool is still a result
`days/day-10-function-tools/parts/02-what-a-tool-returns/2.3-a-failed-tool-is-still-a-result.md` · level `production` · ids ADK-11

A tool that cannot do its job should return a result saying so — a status the model can branch on — because an exception ends the run and a polite sentence hides the failure from everything that counts.

### 3.1 - What the courier took
`days/day-10-function-tools/parts/03-the-dispatch-you-deleted/3.1-what-the-courier-took.md` · level `working` · ids ADK-11

ADK took four things you wrote by hand on Days 3 and 4 — the declarations, the dispatch table, the result turn and the loop that repeats — and left you the two that were always the real work: the functions and their descriptions.

### 3.2 - The loop you no longer write
`days/day-10-function-tools/parts/03-the-dispatch-you-deleted/3.2-the-loop-you-no-longer-write.md` · level `working` · ids ADK-11

One user message now produces several model calls — ask, call a tool, ask again with the result — and ADK's runtime drives that loop, which is why Day 7's events stop being an academic subject and start being the only way to see what happened.

### 3.3 - The brakes still matter
`days/day-10-function-tools/parts/03-the-dispatch-you-deleted/3.3-the-brakes-still-matter.md` · level `production` · ids ADK-11

Day 3's step budget did not become unnecessary when ADK took the loop — it became RunConfig.max_llm_calls, and today is the first day Sutra can actually loop, so today is the day the default of 500 stops being a number and becomes a decision.

### 4.1 - 🅿️ The tailor's receipt
`days/day-10-function-tools/parts/04-tool-shapes/4.1-the-tailors-receipt.md` · level `production` · ids ADK-11

LongRunningFunctionTool is for work that outlives the turn: the function returns a pending receipt immediately, the agent carries on, and the real answer arrives later — and ADK marks the tool so the model knows not to ask again.

### 4.2 - 🅿️ Are you sure?
`days/day-10-function-tools/parts/04-tool-shapes/4.2-are-you-sure.md` · level `production` · ids ADK-11

FunctionTool(fn, require_confirmation=True) puts a person between the model's decision and the action — the first mechanism in this curriculum for a tool that writes — and Principle 13 says that mechanism arrives with the capability rather than after it.

### 5.1 - Two tools, ported
`days/day-10-function-tools/parts/05-wiring-sutra/5.1-two-tools-ported.md` · level `working` · ids ADK-10, ADK-11

Sutra's two functions move from sutra/loop.py into sutra/desk/tools.py, keeping Day 3's logic and Day 4's descriptions, and changing exactly one thing: they return dictionaries with a status instead of sentences.

### 5.2 - The first-aid box with bandages
`days/day-10-function-tools/parts/05-wiring-sutra/5.2-the-first-aid-box-with-bandages.md` · level `production` · ids ADK-11

Day 6's failure lab was an instruction promising a knowledge base that did not exist; today the knowledge base exists, so the handbook's honesty section changes from "you cannot look anything up" to something narrower and truer — and the test that enforced it stops applying.

### 6.1 - 💥 The jar with no label
`days/day-10-function-tools/parts/06-failure-lab/6.1-the-jar-with-no-label.md` · level `production` · ids ADK-10

Today's deliberate failure is one missing type hint: the parameter reaches the model as {} — no type, no constraint — and every layer accepts whatever comes back, so the failure surfaces inside your function as a TypeError with nothing pointing at the cause.

### 7.1 - What a schema still cannot say
`days/day-10-function-tools/parts/07-limits/7.1-what-a-schema-still-cannot-say.md` · level `production` · ids ADK-10

A schema constrains the shape of an argument and nothing else — not whether the value is right, not whether this caller should be allowed to use it, and not what happens if it is wrong — so the guard inside the tool is not redundant, it is the only thing checking any of that.


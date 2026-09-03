# Day 16 - Built-in tools with brakes

IDs closed: ADK-18, AG-07, SEC-01, AG-32 · source: `days/day-16-built-in-tools-with-brakes/`

## Parts

### 1.1 - A power you switch on
`days/day-16-built-in-tools-with-brakes/parts/01-switched-on/1.1-a-power-you-switch-on.md` · level `foundation` · ids ADK-18

A built-in tool is not code in your process at all: it is a mode you switch on inside the model call, run on the provider's machines, and the only two things left for you to review are the switch you flicked and the output that came back.

### 1.2 - An object with a placeholder name
`days/day-16-built-in-tools-with-brakes/parts/01-switched-on/1.2-an-object-with-a-placeholder-name.md` · level `working` · ids ADK-18

google_search carries a name and a description like every other tool, and the model is never shown either of them, because a built-in tool sends no function declaration at all — it edits the request instead.

### 1.3 - The request that leaves your process
`days/day-16-built-in-tools-with-brakes/parts/01-switched-on/1.3-the-request-that-leaves-your-process.md` · level `working` · ids ADK-18

Switching on web search adds exactly one thing to the outgoing request — {"google_search":{}} — and your process never contacts a search engine at all, which is why nothing about the search appears in your logs, your traces or your network tab.

### 2.1 - One built-in, and nothing else
`days/day-16-built-in-tools-with-brakes/parts/02-one-at-a-time/2.1-one-built-in-and-nothing-else.md` · level `working` · ids ADK-18

On the Gemini API, an agent holding google_search or code execution may hold no other tools at all, and the rule is not enforced by ADK: your agent builds, your request goes out, and the platform is what refuses it.

### 2.2 - A flag that does not lift the wall
`days/day-16-built-in-tools-with-brakes/parts/02-one-at-a-time/2.2-a-flag-that-does-not-lift-the-wall.md` · level `production` · ids ADK-18

bypass_multi_tools_limit=True does not remove the exclusivity rule: it silently replaces your search tool with a hidden agent wrapped as a tool, under a different name, with its own model call — and it only does that when the agent's tools list has more than one entry.

### 2.3 - The specialist you write yourself
`days/day-16-built-in-tools-with-brakes/parts/02-one-at-a-time/2.3-the-specialist-you-write-yourself.md` · level `production` · ids ADK-18

Sutra satisfies the exclusivity rule by giving the built-in an agent of its own and offering that agent to the desk as a tool — and the one argument that decides whether the citations survive the handover defaults to off.

### 3.1 - Where the sources are
`days/day-16-built-in-tools-with-brakes/parts/03-receipts/3.1-where-the-sources-are.md` · level `working` · ids ADK-18

A grounded answer arrives with its sources attached to the event, not to the text: event.grounding_metadata.grounding_chunks[i].web holds the title and the URL of each page the model consulted, and if you do not read them off the event as it goes past, nothing later can reconstruct them.

### 3.2 - The offsets are in bytes
`days/day-16-built-in-tools-with-brakes/parts/03-receipts/3.2-the-offsets-are-in-bytes.md` · level `production` · ids ADK-18

grounding_supports[].segment says which span of the answer a source backs up, and its start_index and end_index are positions in the UTF-8 bytes, not in the Python string — so slicing the answer with them highlights the wrong words the moment a single accented character appears earlier in the text.

### 3.3 - The receipt you must show
`days/day-16-built-in-tools-with-brakes/parts/03-receipts/3.3-the-receipt-you-must-show.md` · level `production` · ids ADK-18

Displaying the citations is not a nice touch you add if there is room: the grounding documentation states it as a requirement, the response ships pre-built HTML for the search suggestions, and Sutra's version of that requirement is a renderer that prints nothing at all rather than an empty heading.

### 4.1 - Two questions that sound the same
`days/day-16-built-in-tools-with-brakes/parts/04-newspaper-or-cabinet/4.1-two-questions-that-sound-the-same.md` · level `foundation` · ids AG-07

Grounding answers a question about the live public world by looking it up at the moment of answering; retrieval answers a question about your own private records by searching a collection you keep — and the only thing that decides which one a question needs is where the truth physically lives.

### 4.2 - Routing by where the truth lives
`days/day-16-built-in-tools-with-brakes/parts/04-newspaper-or-cabinet/4.2-routing-by-where-the-truth-lives.md` · level `working` · ids AG-07

The four things that differ between grounding and retrieval — freshness, privacy, the meter they spend and the way they fail — are what a routing decision is actually made of, and in Sutra today that decision is written in one place: the sentence describing the search specialist.

### 4.3 - The question that left the building
`days/day-16-built-in-tools-with-brakes/parts/04-newspaper-or-cabinet/4.3-the-question-that-left-the-building.md` · level `production` · ids AG-07, SEC-01

Grounding turns part of your prompt into a search query on somebody else's machines, you have no callback that can inspect it first, and the only reliable control is to never hand the specialist anything you would not be willing to have searched.

### 4.4 - Two meters, one call
`days/day-16-built-in-tools-with-brakes/parts/04-newspaper-or-cabinet/4.4-two-meters-one-call.md` · level `production` · ids AG-07

A grounded answer spends two separate free allowances at once — model requests, counted per day, and search requests, counted per month — and Sutra's arithmetic says the one that runs out first is not the one the word "grounding" makes you watch.

### 5.1 - An executor is not a tool
`days/day-16-built-in-tools-with-brakes/parts/05-code-that-runs/5.1-an-executor-is-not-a-tool.md` · level `foundation` · ids ADK-18

Code execution is not something you put on the tools list: it is code_executor=, a property of the agent describing how generated code is run, and the two fields refuse each other's values loudly in one direction and produce an illegal request quietly in the other.

### 5.2 - The executor that executes nothing
`days/day-16-built-in-tools-with-brakes/parts/05-code-that-runs/5.2-the-executor-that-executes-nothing.md` · level `working` · ids ADK-18, AG-32

BuiltInCodeExecutor.execute_code() returns None and runs nothing: its entire local job is to add {"code_execution":{}} to the outgoing request, because the code runs inside Google's sandbox and never touches your machine.

### 5.3 - Reading the code and its output
`days/day-16-built-in-tools-with-brakes/parts/05-code-that-runs/5.3-reading-the-code-and-its-output.md` · level `working` · ids ADK-18

A code-execution answer arrives as three things in the event stream — the program the model wrote, the sandbox's output with an outcome code, and the prose written around them — and printing the first two is the only way to know whether the third is arithmetic or a story about arithmetic.

### 5.4 - The estimate and the measurement
`days/day-16-built-in-tools-with-brakes/parts/05-code-that-runs/5.4-the-estimate-and-the-measurement.md` · level `working` · ids ADK-18

A model producing a number is predicting the next token, not calculating, so the fix is not a better prompt but a change of instrument: the model writes the program and an interpreter produces the number.

### 6.1 - The executor that runs it here
`days/day-16-built-in-tools-with-brakes/parts/06-blast-radius/6.1-the-executor-that-runs-it-here.md` · level `production` · ids AG-32, SEC-01

ADK ships an executor that runs model-written code in your own process, and one field changed on one agent gives that code your working directory, your environment variables and your .env — which is why where code runs is a policy decision and not a configuration preference.

### 6.2 - What a sandbox has to be
`days/day-16-built-in-tools-with-brakes/parts/06-blast-radius/6.2-what-a-sandbox-has-to-be.md` · level `production` · ids AG-32

A sandbox is not "a place where code runs"; it is five specific denials — no credentials, no reach, no persistence, a bound on how long, and a boundary that survives the code trying to leave — and an executor is a sandbox only for the ones it actually enforces.

### 6.3 - The rule Sutra writes down
`days/day-16-built-in-tools-with-brakes/parts/06-blast-radius/6.3-the-rule-sutra-writes-down.md` · level `production` · ids SEC-01, AG-32

SEC-01 is Sutra's first written security rule — model-generated code never runs in a process that holds our credentials — and it is worth writing today precisely because today it costs nothing to obey.

### 7.1 - 💥 The spare that does not fit
`days/day-16-built-in-tools-with-brakes/parts/07-failure-lab/7.1-the-spare-that-does-not-fit.md` · level `production` · ids ADK-18, AG-07

Sutra's whole resilience story is "if one provider is out, swap to another" — and a built-in tool does not travel with the swap: the fallback provider raises ValueError at the moment the primary runs out, which is the only moment the fallback exists for.

### 8.1 - Testing a built-in without spending a request
`days/day-16-built-in-tools-with-brakes/parts/08-in-production/8.1-testing-a-built-in-without-spending-a-request.md` · level `production` · ids ADK-18, SEC-01

You cannot fake a built-in tool, so you do not test the searching: you test the request — which tools resolved, which permission it carries, which model it refuses and which executor is nowhere in the package — and all of it runs with no key, no network and no quota.

### 8.2 - The fallback we are not building yet
`days/day-16-built-in-tools-with-brakes/parts/08-in-production/8.2-the-fallback-we-are-not-building-yet.md` · level `production` · ids AG-07

Addendum 02 planned for the grounding allowance shrinking, with an open-source search server as the escape hatch; the allowance was re-checked today and has not shrunk, so the escape hatch stays 🅿️ parked — and knowing exactly what it would cost you is the point of parking it deliberately.

### 8.3 - What you review now
`days/day-16-built-in-tools-with-brakes/parts/08-in-production/8.3-what-you-review-now.md` · level `production` · ids ADK-18, AG-32

Across Phase 2 the thing you review changed three times — from code, to somebody else's document, to a switch and its output — and the last of those is the hardest, because there is nothing to read and everything to decide.

## Papers - read after the parts

### arXiv:2211.10435 - PAL: Program-aided Language Models
`days/day-16-built-in-tools-with-brakes/papers/01-program-aided-language-models.md`

PAL claimed that a language model should be asked to write a program as its reasoning, and that the answer should come from running that program — keeping the reading and decomposing with the model and moving the solving to an interpreter.


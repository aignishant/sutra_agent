# Day 05 - First ADK agent — the runner takes the loop

IDs closed: ADK-01, ADK-02, ADK-73 · source: `days/day-05-first-adk-agent/`

## Parts

### 1.1 - What a framework takes from you — and the only question worth asking of one
`days/day-05-first-adk-agent/parts/01-installing-adk/1.1-what-a-framework-takes.md` · level `foundation` · ids ADK-01

A framework does not add capability — it takes over code you already had, and the only question that matters is which of your intervention points it hands back, which is why you spent two days writing the loop it is about to replace.

### 1.2 - Pinning the framework — when the plan's number and today's number disagree
`days/day-05-first-adk-agent/parts/01-installing-adk/1.2-pinning-the-framework.md` · level `working` · ids ADK-01

The plan names a baseline of google-adk 2.6.3 and instructs you to re-verify on install day — so finding 2.7.1 is not a contradiction to be resolved, it is the plan working exactly as designed, and the difference between that and a real amendment is worth being able to state.

### 1.3 - The layout ADK expects — a convention, and the one place Sutra refuses it
`days/day-05-first-adk-agent/parts/01-installing-adk/1.3-the-layout-adk-expects.md` · level `working` · ids ADK-01

ADK finds your agent by convention — a folder containing agent.py that defines a module-level root_agent — and Sutra adopts all of it except the suggested second .env, because one secret in two files is one more file that can be committed.

### 2.1 - An agent is a configuration, not a loop — constructing one does nothing at all
`days/day-05-first-adk-agent/parts/02-the-agent-object/2.1-an-agent-is-a-configuration.md` · level `foundation` · ids ADK-02

LlmAgent(...) builds an object that describes an agent — a name, a model, an instruction, a tool list — and makes no network call, spends no quota and runs nothing; the running is a separate thing called a runner, and keeping those two ideas apart explains most of what is confusing about frameworks.

### 2.2 - Name and description are not decoration — one is an address, the other is an advertisement
`days/day-05-first-adk-agent/parts/02-the-agent-object/2.2-name-and-description.md` · level `working` · ids ADK-02

name is an identifier that appears in traces and becomes the address other agents route to, and description is read by a model to decide whether to send work here — so the field that looks most like a comment is the one with runtime behaviour attached, exactly as it was for tools on Day 4.

### 2.3 - The instruction is your system prompt — moved verbatim, and one lever lost
`days/day-05-first-adk-agent/parts/02-the-agent-object/2.3-the-instruction-is-your-system-prompt.md` · level `working` · ids ADK-02

instruction is Day 4's SYSTEM string, moved across without a word changed — the framework changed who runs the loop, not what the agent is asked to do — and the one thing you give up is control over where in the payload it lands, which was a real lever on Day 3.

### 3.1 - The default that moved under you — why every agent pins its model
`days/day-05-first-adk-agent/parts/03-the-model-pin/3.1-the-default-that-moved.md` · level `production` · ids ADK-73

An LlmAgent without model= falls back to ADK's own built-in default, that default was changed in a minor release, and a model that changes without a commit in your history means your eval scores move overnight with nothing in the repository to explain it — so every agent in Sutra pins its model explicitly, and this is curriculum item ADK-73.

### 3.2 - A floating alias is not a pin — the string that survives code review and moves anyway
`days/day-05-first-adk-agent/parts/03-the-model-pin/3.2-a-floating-alias-is-not-a-pin.md` · level `production` · ids ADK-73

gemini-flash-latest is what ADK's own documentation puts in its examples, and it is not a model — it is a pointer that resolves to whatever is current — which makes it worse than having no model= at all, because a reviewer looking at the diff sees a string that appears to be a decision.

### 3.3 - Two doors to Gemini — and the environment variable that picks one without asking
`days/day-05-first-adk-agent/parts/03-the-model-pin/3.3-two-doors-to-gemini.md` · level `production` · ids ADK-73

The same models are reachable two ways — a free AI Studio API key, or a Vertex AI project with a billing account attached — and which one you get is decided by an environment variable that can be set outside your repository, which means your code can be entirely correct and still be walking through the door that sends invoices.

### 4.1 - The runner is your run_loop — handing over the thing you wrote twice
`days/day-05-first-adk-agent/parts/04-the-runner/4.1-the-runner-is-your-run-loop.md` · level `working` · ids ADK-02

A Runner is ADK's name for the function you wrote on Day 3 and rewrote on Day 4. It takes an agent, a session and a message, and it hands you events as it goes. Today you give your loop away, and then you find out what comes back.

### 4.2 - Sessions and the transcript — the list you owned now belongs to a service
`days/day-05-first-adk-agent/parts/04-the-runner/4.2-sessions-and-the-transcript.md` · level `working` · ids ADK-02

The history list you have kept by hand since Day 2 is now a session, held by a session service and addressed by application, user and session id. The runner does the appending for you. It also means that Days 19–20's context work has to go through whatever that service allows.

### 4.3 - Read the signature, not the tutorial — the object you installed is the authority
`days/day-05-first-adk-agent/parts/04-the-runner/4.3-read-the-signature-not-the-tutorial.md` · level `working` · ids ADK-01

Before you write a line that uses a framework symbol, print its signature. ADK 2.0 was a breaking release, the internet is full of 1.x examples that import cleanly and behave differently, and inspect costs nothing and answers about the exact version you pinned.

### 5.1 - The seam list, checked — answering your own questions against somebody else's loop
`days/day-05-first-adk-agent/parts/05-the-comparison/5.1-the-seam-list-checked.md` · level `production` · ids ADK-02

Take the seven questions you wrote before installing anything, and answer them against ADK. A few get answered today, and most get a day number. What you end up holding is not an opinion about a framework. It is a schedule with known gaps in it.

### 5.2 - What you handed over — and the part that was never the framework's to take
`days/day-05-first-adk-agent/parts/05-the-comparison/5.2-what-you-handed-over.md` · level `production` · ids ADK-02

Three days, three completely different loops, and the same four things survived every rewrite: the tools, the data they touch, the rule about which errors raise, and the honesty policy. That list is the practical definition of what Sutra actually is, as distinct from what it happens to run on.

### 6.1 - 💥 The agent with no model — running the substitution on purpose
`days/day-05-first-adk-agent/parts/06-failure-lab/6.1-the-agent-with-no-model.md` · level `production` · ids ADK-73

Build an agent with no model=, run it beside the pinned one, and read what the framework put there instead. The whole hazard of ADK-73 is that the substitution works, and a failure you have watched happen on a day you chose is a failure you will recognise on a day you did not.

### 7.1 - 🅿️ `adk run` and `adk web` — the practice ground is not the road
`days/day-05-first-adk-agent/parts/07-the-dev-ui/7.1-adk-run-and-adk-web.md` · level `production` · ids ADK-01

ADK ships a command-line runner and a browser development UI, and one of the two will run today's agent with no code at all — adk run cannot, in this repository, for a reason worth the detour. Sutra wrote run_once.py anyway, because those tools hide exactly the object this day is about, and because everything that makes a deployment hard happens at a scale they do not have.


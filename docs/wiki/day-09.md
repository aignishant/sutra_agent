# Day 09 - Same agent, four free providers — the string that changes everything

IDs closed: ADK-09, ADK-08 · source: `days/day-09-four-free-providers/`

## Parts

### 1.1 - A name is a lookup
`days/day-09-four-free-providers/parts/01-one-model-field/1.1-a-name-is-a-lookup.md` · level `foundation` · ids ADK-09

The string in model= is not a name the framework passes along — it is a key into a table of patterns, and which class ends up talking to the network is decided by matching that string against the table.

### 1.2 - The spare tyre you never checked
`days/day-09-four-free-providers/parts/01-one-model-field/1.2-the-spare-tyre-you-never-checked.md` · level `working` · ids ADK-09

An agent with an impossible model string builds without complaint — the string is not resolved until something needs the model — so a typo survives import, survives every test that does not make a call, and arrives at the first real request.

### 2.1 - One charger, many sockets
`days/day-09-four-free-providers/parts/02-the-translator/2.1-one-charger-many-sockets.md` · level `foundation` · ids ADK-09

LiteLLM is a translation layer: it takes one request shape and speaks it to a hundred different providers, which is what lets the same ADK agent talk to Groq, OpenRouter or a model on your own laptop by changing one string.

### 2.2 - The toolkit you did not need
`days/day-09-four-free-providers/parts/02-the-translator/2.2-the-toolkit-you-did-not-need.md` · level `working` · ids ADK-09

ADK's own error message tells you to install google-adk[extensions], which brings Kubernetes, Docker, two agent frameworks and a search index along with the one library you actually want — so you install litellm directly, pin it exactly, and write down why.

### 2.3 - The express counter
`days/day-09-four-free-providers/parts/02-the-translator/2.3-the-express-counter.md` · level `working` · ids ADK-09

Groq is not a model — it is a company running other people's open-weight models on custom chips, very fast, on a free tier metered in requests per minute and per day, and it is the only one of your four lanes that tells you exactly how much you have left on every single response.

### 2.4 - The wholesale market
`days/day-09-four-free-providers/parts/02-the-translator/2.4-the-wholesale-market.md` · level `working` · ids ADK-09

OpenRouter is an aggregator — one key, one API, hundreds of models from dozens of vendors — and the ones that cost nothing are marked by a :free suffix on the model id, a roster that changes often enough that a name from two weeks ago is already gone.

### 3.1 - Cooking at home
`days/day-09-four-free-providers/parts/03-local/3.1-cooking-at-home.md` · level `working` · ids ADK-08

Ollama runs a model on your own machine: no key, no quota, no network, nothing leaving the room — and in exchange the model is smaller, the speed is whatever your hardware gives you, and the failures are now yours to fix.

### 3.2 - Two switches that look the same
`days/day-09-four-free-providers/parts/03-local/3.2-two-switches-that-look-the-same.md` · level `working` · ids ADK-08

ollama_chat/ and ollama/ are two different prefixes with two different behaviours — ADK's own documentation says the second causes "infinite tool call loops and ignoring previous context" — and a third case, ollama/gemma3, resolves to a class you did not ask for.

### 3.3 - The learner driver
`days/day-09-four-free-providers/parts/03-local/3.3-the-learner-driver.md` · level `production` · ids ADK-08

A prompt is not portable: the same handbook that works on a large model relies on inferences a small one does not make, so switching lanes silently changes behaviour — and the way you find out is to run the same probes on each.

### 4.1 - Two routes to work
`days/day-09-four-free-providers/parts/04-the-benchmark/4.1-two-routes-to-work.md` · level `working` · ids ADK-09

One call per provider is not a measurement — it is an anecdote — so before you build a comparison table you decide what you are actually able to claim from the number of calls a free tier will let you make.

### 4.2 - The mileage on the sticker
`days/day-09-four-free-providers/parts/04-the-benchmark/4.2-the-mileage-on-the-sticker.md` · level `production` · ids ADK-09

The deliverable of this day is a four-row table that says what each lane costs, what it gives you and how confident you are — with the date on it, because every number in it has a shelf life.

### 4.3 - Three shops, three closing times
`days/day-09-four-free-providers/parts/04-the-benchmark/4.3-three-shops-three-closing-times.md` · level `production` · ids ADK-09

Each lane refuses you differently — one tells you your remaining quota on every response, one tells you only when it says no, one gives a retry hint that is not a window, and one never refuses at all — so "handle the 429" is four different jobs wearing one name.

### 5.1 - Which queue do you join?
`days/day-09-four-free-providers/parts/05-routing/5.1-which-queue-do-you-join.md` · level `production` · ids ADK-09

Routing is choosing a model per request, and in ADK's Python runtime today there is no object that does it for you — the documented RoutedLlm is TypeScript-only — so routing is a decision you make in your own code, which is exactly what Day 70 will build.

### 5.2 - 🅿️ The dispatcher at the taxi stand
`days/day-09-four-free-providers/parts/05-routing/5.2-the-dispatcher-at-the-taxi-stand.md` · level `production` · ids ADK-09

The Quota-Router that Day 70 builds needs four things — a per-provider counter, a policy, a floor and a log — and three of the four are already in your hands today; this part is the sketch, deliberately not the build.

### 6.1 - 🅿️ The spec sheet you can read
`days/day-09-four-free-providers/parts/06-parked/6.1-the-spec-sheet-you-can-read.md` · level `production` · ids ADK-09

The paid lanes — Claude and the OpenAI models — are two lines of code away and permanently out of scope for this project, and knowing exactly which two lines is the whole of what you need, because the skill transfers unchanged the day somebody hands you a key.

### 7.1 - 💥 The free trial that charges
`days/day-09-four-free-providers/parts/07-failure-lab/7.1-the-free-trial-that-charges.md` · level `production` · ids ADK-09

Today's deliberate failure costs nothing to reproduce and everything to miss: delete five characters from an OpenRouter model string and every layer — the registry, the agent, the resolver — accepts it, because the only thing that would have objected is an invoice.

## Papers - read after the parts

### arXiv:2406.18665 - RouteLLM: Learning to Route LLMs with Preference Data
`days/day-09-four-free-providers/papers/01-routellm.md`

Train a small model to predict, for each question, whether the strong model would beat the weak one, then send the question to the weak model unless that probability clears a threshold — and you can cut cost by more than half without the answers getting worse.


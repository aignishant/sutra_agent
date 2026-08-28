# Day 01 - Bootstrap & the map

IDs closed: AG-01, OPS-01, OPS-02, OPS-03 · source: `days/day-01-bootstrap-and-map/`

## Parts

### 1.1 - Who decides the next step
`days/day-01-bootstrap-and-map/parts/01-what-is-an-agent/1.1-who-decides-the-next-step.md` · level `foundation` · ids AG-01

A system is agentic when the model, not the programmer, decides what happens next — and that single sentence is the whole definition, with everything else in this curriculum being a consequence of it.

### 1.2 - Goal, tools, loop, stop condition — the anatomy of deciding
`days/day-01-bootstrap-and-map/parts/01-what-is-an-agent/1.2-goal-tools-loop-stop.md` · level `foundation` · ids AG-01

An agent is built from exactly four parts — a goal, a set of tools, a loop, and a stop condition — and three of them are obvious while the fourth is the one that decides whether you have a system or an incident.

### 1.3 - When an agent is the wrong answer
`days/day-01-bootstrap-and-map/parts/01-what-is-an-agent/1.3-when-an-agent-is-the-wrong-answer.md` · level `working` · ids AG-01

Autonomy is a purchase, not an upgrade: you pay in predictability, testability, latency and quota, and you should only pay when the input genuinely varies in ways you cannot enumerate.

### 1.4 - Sutra on the spectrum — where the model decides, and where it never will
`days/day-01-bootstrap-and-map/parts/01-what-is-an-agent/1.4-sutra-on-the-spectrum.md` · level `production` · ids AG-01

Sutra is a fixed pipeline with two agentic pockets and a human gate — and being able to point at each of its five stages and say who decides there is the difference between having read about agent design and having done it.

### 2.1 - What Sutra actually is
`days/day-01-bootstrap-and-map/parts/02-repo-as-memory/2.1-what-sutra-actually-is.md` · level `foundation` · ids OPS-01

Sutra is one system, built once, that every concept in this curriculum lands in — an autonomous support-ticket triage desk — and the reason it is one system rather than ninety-six exercises is that a concept you cannot bolt onto something real is a concept you have not learned.

### 2.2 - The docs tree, and which document wins
`days/day-01-bootstrap-and-map/parts/02-repo-as-memory/2.2-the-docs-tree-and-precedence.md` · level `working` · ids OPS-01

A project with several governing documents needs a stated precedence order, because documents written at different times will eventually disagree — and a rule set that does not say what beats what produces confident wrong answers rather than visible confusion.

### 2.3 - The ADR that survives a cold read
`days/day-01-bootstrap-and-map/parts/02-repo-as-memory/2.3-the-adr-that-survives-a-cold-read.md` · level `production` · ids OPS-01

An Architecture Decision Record captures one decision, the situation that forced it, the options you rejected, and — the part almost everyone omits — what would make you change your mind, which is the only section that turns a record into something you can act on later.

### 3.1 - The three free doors — and what each one is for
`days/day-01-bootstrap-and-map/parts/03-keys-and-env/3.1-the-three-free-doors.md` · level `foundation` · ids OPS-02

Three organisations will give you a key that costs nothing, and they are not interchangeable — each has a different shape of generosity, and knowing which is which is what turns "I have free access" into a routing policy you can defend.

### 3.2 - .env, and the environment as an interface
`days/day-01-bootstrap-and-map/parts/03-keys-and-env/3.2-env-and-the-environment-as-interface.md` · level `working` · ids OPS-02

.env is a local convenience for setting environment variables, and the thing that actually matters is the interface underneath it: configuration reaches your program through the environment, never through a committed file — which is why the same code runs unchanged on your laptop, in CI, and in a container.

### 3.3 - Loading keys, and failing loudly
`days/day-01-bootstrap-and-map/parts/03-keys-and-env/3.3-loading-keys-failing-loudly.md` · level `working` · ids OPS-02

Configuration should be read and checked once, at start-up, by code that refuses to continue when something is missing — because a program that starts happily and fails forty minutes later has converted a one-line configuration error into an incident.

### 3.4 - The rotation drill — rehearsing the incident while it is free
`days/day-01-bootstrap-and-map/parts/03-keys-and-env/3.4-the-rotation-drill.md` · level `production` · ids OPS-02

You are going to revoke a working key on purpose, watch everything that depends on it fail, and put a new one in — because the first time you do that must not be the day it matters.

### 4.1 - The diary and the scoreboard
`days/day-01-bootstrap-and-map/parts/04-ledgers/4.1-the-diary-and-the-scoreboard.md` · level `foundation` · ids OPS-03

A project keeps two completely different kinds of record — an append-only diary of what happened, which only ever grows, and a regenerated scoreboard computed from it, which is never edited by hand — and treating one like the other is how a project loses the ability to tell you the truth.

### 4.2 - Build the generator yourself
`days/day-01-bootstrap-and-map/parts/04-ledgers/4.2-build-the-generator-yourself.md` · level `working` · ids OPS-03

You are going to write your own traceability generator — three readers and one writer, in about forty lines — because Principle 4 says hand-roll the mechanism before adopting the tool, and a script you have written is a script you can debug at a phase gate.

### 4.3 - Reading the shipped generator — what the extra lines buy
`days/day-01-bootstrap-and-map/parts/04-ledgers/4.3-reading-the-shipped-generator.md` · level `production` · ids OPS-03

Your forty lines and the shipped two hundred agree about the answer — so every extra line is buying something other than correctness, and being able to name what each one buys is the difference between using a tool and being able to maintain one.

## Papers - read after the parts

### doi:10.1017/S0269888900008122 - Intelligent agents: theory and practice — where the word came from
`days/day-01-bootstrap-and-map/papers/01-intelligent-agents.md`

Thirty years before anyone called a language model "agentic", a survey paper drew the line this curriculum still uses — a program becomes an agent when it is autonomous, reactive, pro-active and social — and the half of that paper the field kept is exactly the half you hand-rolled in [1.1](../parts/01-what-is-an-agent/1.1-who-decides-the-next-step.md).


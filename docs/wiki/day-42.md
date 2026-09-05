# Day 42 - Serving agents over MCP

IDs closed: MCP-33, ADK-26 · source: `days/day-42-serving-agents-over-mcp/`

## Parts

### 1.1 - The colleague you can now phone
`days/day-42-serving-agents-over-mcp/parts/01-the-back-office/1.1-the-colleague-you-can-now-phone.md` · level `foundation` · ids MCP-33

Serving an agent over MCP does not publish a new capability; it publishes an existing one to people who were never in the room, and everything that used to be understood without saying now has to be said.

### 1.2 - Twelve words in the classifieds
`days/day-42-serving-agents-over-mcp/parts/01-the-back-office/1.2-twelve-words-in-the-classifieds.md` · level `foundation` · ids MCP-33

to_mcp_server(agent) is one function call that turns any ADK agent into a server object exposing exactly one tool, and everything the outside world will ever know about your agent has to fit in that tool's name and description.

### 1.3 - The hall that came with its own chairs
`days/day-42-serving-agents-over-mcp/parts/01-the-back-office/1.3-the-hall-that-came-with-its-own-chairs.md` · level `working` · ids MCP-33, ADK-26

Leaving runner=None makes to_mcp_server build you a whole runtime — sessions, memory, artifacts and credentials, all in memory, all forgotten on restart, and every caller in the world logged in as the same user.

### 1.4 - The counter by the side door
`days/day-42-serving-agents-over-mcp/parts/01-the-back-office/1.4-the-counter-by-the-side-door.md` · level `working` · ids MCP-33

Today is the first day since Day 34 that does not add a line to build_server(), because to_mcp_server builds a whole server of its own rather than a handler you can register — so sutra_mcp/ ends the day with two servers, deliberately.

### 2.1 - The enquiry slip with one box
`days/day-42-serving-agents-over-mcp/parts/02-what-crosses-the-counter/2.1-the-enquiry-slip-with-one-box.md` · level `working` · ids MCP-33

The declaration a served agent publishes has exactly one property, request, typed string, with no output schema and no structure of any kind — so every constraint you want the caller to respect has to be written in prose or not at all.

### 2.2 - The interpreter who relays the last sentence
`days/day-42-serving-agents-over-mcp/parts/02-what-crosses-the-counter/2.2-the-interpreter-who-relays-the-last-sentence.md` · level `working` · ids MCP-33

Only the agent's final response crosses the wire, converted block by block — text becomes text, inline images and audio become image and audio blocks, and anything the converter has no shape for, including every tool call the agent made, is silently dropped.

### 2.3 - The table you may leave your books on
`days/day-42-serving-agents-over-mcp/parts/02-what-crosses-the-counter/2.3-the-table-you-may-leave-your-books-on.md` · level `working` · ids MCP-33

A served agent keeps one conversation per MCP connection — successive calls on one connection see each other, a second connection starts from nothing, and every one of them runs as the same user — which is a memory model the protocol has no field to describe.

### 2.4 - The errand you sent someone on
`days/day-42-serving-agents-over-mcp/parts/02-what-crosses-the-counter/2.4-the-errand-you-sent-someone-on.md` · level `production` · ids MCP-33

Serving an agent does not publish an interface, it publishes a reach: one request string can run every tool the agent owns and every tool of every sub-agent it may hand the work to, and none of that appears in the declaration.

### 3.1 - The machine and the manager
`days/day-42-serving-agents-over-mcp/parts/03-tool-or-peer/3.1-the-machine-and-the-manager.md` · level `working` · ids ADK-26

Agent-as-tool means the caller uses you — one instruction in, one result out, no identity and no conversation — while agent-as-peer means the caller talks to you, with two named parties, a conversation that has a lifetime, and the right to ask questions back.

### 3.2 - A note handed over, and money sent
`days/day-42-serving-agents-over-mcp/parts/03-tool-or-peer/3.2-a-note-handed-over-and-money-sent.md` · level `production` · ids ADK-26

Four things separate a call inside your process from a call across a boundary — how long it takes, what memory it can touch, what happens when it half-fails, and what happens when two arrive at once — and no amount of identical-looking syntax makes any of the four go away.

### 3.3 - The guillotine and the press
`days/day-42-serving-agents-over-mcp/parts/03-tool-or-peer/3.3-the-guillotine-and-the-press.md` · level `production` · ids ADK-26, MCP-33

Sutra serves a narrow, read-only answering agent as a tool over MCP, does not serve the whole desk, and does not serve anything as a peer — because the only lever to_mcp_server gives you is the choice of what to hand it, and every other control you want lives on the agent you chose.

### 4.1 - The kettle and the car
`days/day-42-serving-agents-over-mcp/parts/04-what-a-call-costs/4.1-the-kettle-and-the-car.md` · level `working` · ids MCP-33

A plain MCP tool costs one database read per call and a served agent costs one generation to decide plus one more for every tool result it reads back, so the same tools/call is either free or three per cent of a free-tier day depending on what is behind it.

### 4.2 - The family data pack
`days/day-42-serving-agents-over-mcp/parts/04-what-a-call-costs/4.2-the-family-data-pack.md` · level `production` · ids MCP-33

Forty calls a day at three generations each is a hundred and twenty generations against a ceiling of twenty, so a served desk on the free tier answers six callers and refuses thirty-four — which means the honest answer to "should Sutra serve its agent" is not this agent, and not to everyone.

### 4.3 - The notice on the ration shop board
`days/day-42-serving-agents-over-mcp/parts/04-what-a-call-costs/4.3-the-notice-on-the-ration-shop-board.md` · level `production` · ids MCP-33

MCP has no field for capacity, cost or rate, so the only place you can publish yours is the tool description — and a served agent that does not publish it is a service whose callers find out by being refused.

### 5.1 - Two signs, both saying Room 12
`days/day-42-serving-agents-over-mcp/parts/05-failure-lab/5.1-two-signs-both-saying-room-12.md` · level `production` · ids MCP-33

Nothing stops a served agent from having your own server on its tool list, and when that happens one caller request becomes as many agent runs as something else eventually stops — with every run spending a generation.

### 5.2 - You knock and walk away
`days/day-42-serving-agents-over-mcp/parts/05-failure-lab/5.2-you-knock-and-walk-away.md` · level `production` · ids MCP-33

A caller sets its timeout while looking at tools that read a dictionary, a served agent needs several model round-trips, and when the caller gives up the server keeps working and finishes — spending your quota on an answer nobody will ever receive.

### 5.3 - The price sticker underneath
`days/day-42-serving-agents-over-mcp/parts/05-failure-lab/5.3-the-price-sticker-underneath.md` · level `production` · ids MCP-33

A 429 raised inside a served agent escapes as str(exception) in a text block, so the caller's model reads five hundred characters of your provider's internal quota body — your tier, your metric, your project's ceiling — as the answer to a support question.

### 6.1 - The school in two sheds
`days/day-42-serving-agents-over-mcp/parts/06-in-production/6.1-the-school-in-two-sheds.md` · level `production` · ids MCP-33

to_mcp_server is decorated @experimental, lives in a private module, has no page on adk.dev, and sits behind an import guard that turns any failure in its dependency chain into "this name does not exist" with the reason logged at DEBUG — so shipping it means shipping four separate risks, and three of them are manageable.

### 6.2 - Red before you serve
`days/day-42-serving-agents-over-mcp/parts/06-in-production/6.2-red-before-you-serve.md` · level `production` · ids MCP-33, ADK-26

Six statements have to be true of sutra_mcp/agent_server.py before a stranger may call it, and the only useful form for those statements is a script with an exit code that was red before you wrote the module.

## Papers - read after the parts

### doi:10.1007/3-540-62852-5_6 - A note on distributed computing
`days/day-42-serving-agents-over-mcp/papers/01-a-note-on-distributed-computing.md`

A local call and a remote call differ in kind, not in degree — latency, memory access, partial failure and concurrency do not go away because the two calls are spelled the same — so any framework that promises to make the network invisible is promising something it cannot deliver, and the systems built on that promise fail on the network rather than on the developer's machine.


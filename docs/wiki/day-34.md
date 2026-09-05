# Day 34 - Building `sutra-mcp` I — tools over the wire

IDs closed: MCP-04, MCP-06, MCP-05 · source: `days/day-34-building-sutra-mcp-tools/`

## Parts

### 1.1 - Three things and no fourth
`days/day-34-building-sutra-mcp-tools/parts/01-the-server-object/1.1-three-things-and-no-fourth.md` · level `foundation` · ids MCP-04

An MCP server is exactly three things — a name it answers to, a list of what it can do, and the code that does it — and the interesting part of that sentence is everything it leaves out.

### 1.2 - A server you build, not one that runs
`days/day-34-building-sutra-mcp-tools/parts/01-the-server-object/1.2-a-server-you-build-not-one-that-runs.md` · level `foundation` · ids MCP-04

Building a server and starting a server are two separate acts, so build_server() returns a fully configured object that has not listened to anything — which is what lets every test, every later day and every deployment shape pick it up and do something different with it.

### 1.3 - The name is an identity
`days/day-34-building-sutra-mcp-tools/parts/01-the-server-object/1.3-the-name-is-an-identity.md` · level `working` · ids MCP-04

The string you pass to FastMCP(...) travels out in every reply as serverInfo.name, gets written into host configuration files, log lines and allowlists you do not own — so it is expensive to change and, by the specification's own words, proves nothing about who wrote the server.

### 1.4 - The shape later days register into
`days/day-34-building-sutra-mcp-tools/parts/01-the-server-object/1.4-the-shape-later-days-register-into.md` · level `working` · ids MCP-04

sutra_mcp/ gets one module per kind of capability and one convention — register_<kind>(server) — so that seven later days can each add a file and one line to build_server() instead of inventing a second server.

### 2.1 - The decorator that writes your schema
`days/day-34-building-sutra-mcp-tools/parts/02-function-to-declaration/2.1-the-decorator-that-writes-your-schema.md` · level `working` · ids MCP-04, MCP-06

@server.tool() reads your function's name, type hints, docstring and return annotation, and from those four things writes the JSON Schema declaration that goes on the wire — which is convenient until you realise it means your type hints are now a public interface.

### 2.2 - The schema is all they get
`days/day-34-building-sutra-mcp-tools/parts/02-function-to-declaration/2.2-the-schema-is-all-they-get.md` · level `working` · ids MCP-06

The caller never sees your function, your data or your log — only the declaration — so anything the caller must know to use the tool correctly has to be written into the description, and anything you leave out is a guess somebody else has to make.

### 2.3 - 💥 The argument that changed on the way in
`days/day-34-building-sutra-mcp-tools/parts/02-function-to-declaration/2.3-the-argument-that-changed-on-the-way-in.md` · level `production` · ids MCP-06

A declared type is not only a filter, it is a converter: an argument the caller sent as "04521" arrives in a tool that declared int as 4521, with no error, no warning and no way for either side to find out.

### 2.4 - What the caller can no longer assume
`days/day-34-building-sutra-mcp-tools/parts/02-function-to-declaration/2.4-what-the-caller-can-no-longer-assume.md` · level `working` · ids MCP-04, MCP-06

The same function called over MCP returns a result object instead of a value, reports failure instead of raising it, accepts only what JSON can carry, and can fail for reasons that have nothing to do with the work — so "it is the same function" is true of the body and false of everything around it.

### 3.1 - The list, and who may keep it
`days/day-34-building-sutra-mcp-tools/parts/03-the-two-calls/3.1-the-list-and-who-may-keep-it.md` · level `working` · ids MCP-06

tools/list is the one call whose answer a client is allowed to keep, and the server decides for how long with ttlMs and decides who may keep it with cacheScope — two fields the pinned SDK does not send at all.

### 3.2 - The same order every time
`days/day-34-building-sutra-mcp-tools/parts/03-the-two-calls/3.2-the-same-order-every-time.md` · level `working` · ids MCP-06

The order of the array in tools/list is part of what a client and a model provider cache on, so a list that comes back in a different order is a different list — and the SDK gives you registration order, which is stable only by accident.

### 3.3 - One call, one result
`days/day-34-building-sutra-mcp-tools/parts/03-the-two-calls/3.3-one-call-one-result.md` · level `working` · ids MCP-06

tools/call sends a name and an arguments object and gets back one result carrying a list of content blocks for the model to read, an optional structuredContent for the program to parse, and an isError flag — and your tool's plain str return became all three of those things.

### 4.1 - The tool said no
`days/day-34-building-sutra-mcp-tools/parts/04-two-kinds-of-no/4.1-the-tool-said-no.md` · level `working` · ids MCP-06

isError: true means the tool ran and could not do the job, the message is written for the model that will read it, and the whole point of reporting failure this way is that the caller stays alive to try something else.

### 4.2 - The call never happened
`days/day-34-building-sutra-mcp-tools/parts/04-two-kinds-of-no/4.2-the-call-never-happened.md` · level `working` · ids MCP-06

A protocol error is a JSON-RPC error object rather than a result: nothing ran, there is no isError field because there is no result to put it in — and the pinned SDK reports an unknown tool the other way round, which is a divergence worth knowing about before you rely on either.

### 4.3 - 💥 The message that escaped
`days/day-34-building-sutra-mcp-tools/parts/04-two-kinds-of-no/4.3-the-message-that-escaped.md` · level `production` · ids MCP-06

Every exception your tool body raises has its str() copied verbatim into a text block the caller reads, so a KeyError, a file path or a connection string stops being an internal detail the moment it is raised.

### 5.1 - The handshake that is now history
`days/day-34-building-sutra-mcp-tools/parts/05-lifecycle/5.1-the-handshake-that-is-now-history.md` · level `foundation` · ids MCP-05

Until the 2026-07-28 revision a server held three states and refused every request until a client had walked it through all three — so this part is what your server used to have to remember, and what deleting it removed.

### 5.2 - What your server actually answers
`days/day-34-building-sutra-mcp-tools/parts/05-lifecycle/5.2-what-your-server-actually-answers.md` · level `working` · ids MCP-05

Send the four requests yourself and read the replies: the server you built refuses server/discover, refuses business before a handshake, and negotiates 2025-11-25 — so it is a handshake-era server, and knowing that from its own mouth is worth more than knowing it from a changelog.

### 5.3 - Building for the revision you are not on
`days/day-34-building-sutra-mcp-tools/parts/05-lifecycle/5.3-building-for-the-revision-you-are-not-on.md` · level `production` · ids MCP-05

You cannot make mcp==1.29.1 speak 2026-07-28, and you can write every line of your server so that the day the pin moves is a dependency bump rather than a rewrite — which means holding no state, stateless_http=True, and knowing exactly what that flag does and does not do.

### 6.1 - 💥 The tool you deleted is still being called
`days/day-34-building-sutra-mcp-tools/parts/06-in-production/6.1-the-tool-you-deleted-is-still-called.md` · level `production` · ids MCP-06

The ttlMs you chose is also how long a client may keep calling a tool you removed, so deleting a tool in one deployment is a deliberate decision to serve errors for that long — and doing it in two deployments costs nothing but patience.

### 6.2 - Red before you ship it
`days/day-34-building-sutra-mcp-tools/parts/06-in-production/6.2-red-before-you-ship-it.md` · level `production` · ids MCP-04, MCP-06

Six things must be true of sutra_mcp/ before this day is done, and a script that checks all six and exits non-zero is worth more than a checklist, because it is red right now and it will still be checking on Day 45.


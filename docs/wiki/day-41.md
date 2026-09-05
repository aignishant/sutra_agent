# Day 41 - Server capabilities and MCP Apps

IDs closed: MCP-18, MCP-19, MCP-29 · source: `days/day-41-capabilities-and-mcp-apps/`

## Parts

### 1.1 - The programmes on the dial
`days/day-41-capabilities-and-mcp-apps/parts/01-what-a-server-declares/1.1-the-programmes-on-the-dial.md` · level `foundation` · ids MCP-18

A capability is not a feature and not a tool: it is a whole family of methods a server says it answers, so tools means I answer tools/list and tools/call, and a family the server does not name is a family whose methods simply do not exist there.

### 1.2 - Nobody types the declaration
`days/day-41-capabilities-and-mcp-apps/parts/01-what-a-server-declares/1.2-nobody-types-the-declaration.md` · level `working` · ids MCP-18

The SDK writes your capability declaration for you by looking at which handlers you registered — and FastMCP, the class Day 34 built on, registers all of them at construction, so an empty FastMCP server declares tools, resources and prompts before you have written a single one.

### 1.3 - An extension is a capability with a surname
`days/day-41-capabilities-and-mcp-apps/parts/01-what-a-server-declares/1.3-an-extension-is-a-capability-with-a-surname.md` · level `working` · ids MCP-18

A core family is named by a bare word (tools); an extension is named by a reverse-DNS identifier (io.modelcontextprotocol/ui) inside a separate extensions map — and the pinned SDK has no extensions map at all, so on mcp==1.29.1 an extension claim goes into experimental or nowhere.

### 1.4 - The client declares too
`days/day-41-capabilities-and-mcp-apps/parts/01-what-a-server-declares/1.4-the-client-declares-too.md` · level `working` · ids MCP-18

Capability declaration runs both ways: the client's capabilities ride in _meta on every single request, they are required, and a server that needs one the client did not declare must answer -32021 MissingRequiredClientCapability rather than guess.

### 2.1 - One question instead of three
`days/day-41-capabilities-and-mcp-apps/parts/02-discovery-without-sessions/2.1-one-question-instead-of-three.md` · level `working` · ids MCP-18

Without a session there is no moment at which a server introduces itself, so server/discover is the request that carries the introduction — and its capability half is what saves a client from probing tools/list, resources/list and prompts/list to find out which of them will even answer.

### 2.2 - The request your SDK cannot send
`days/day-41-capabilities-and-mcp-apps/parts/02-discovery-without-sessions/2.2-the-request-your-sdk-cannot-send.md` · level `working` · ids MCP-18

Grep the installed SDK for the four things this day's protocol depends on — server/discover, ttlMs, cacheScope, resultType — and every count is zero, so on mcp==1.29.1 the only place a capability declaration exists is inside a legacy initialize reply, and everything else on this page is design work for a pin that has not moved yet.

### 2.3 - Asking for what was never declared
`days/day-41-capabilities-and-mcp-apps/parts/02-discovery-without-sessions/2.3-asking-for-what-was-never-declared.md` · level `working` · ids MCP-18

Call a family a server never declared and you get -32601 Method not found — a third kind of no, distinct from the tool-level isError and the argument-level -32602, and the only one that means stop asking, this will never work.

### 3.1 - A promise, not a proof
`days/day-41-capabilities-and-mcp-apps/parts/03-declared-versus-implemented/3.1-a-promise-not-a-proof.md` · level `working` · ids MCP-19

A capability declaration is something a server says, not something the protocol checks, so "declared" and "implemented" are two different facts — and the client that treats the first as evidence of the second is the one that pages somebody.

### 3.2 - Probing every promise
`days/day-41-capabilities-and-mcp-apps/parts/03-declared-versus-implemented/3.2-probing-every-promise.md` · level `working` · ids MCP-19

Walk the catalogue and call every entry once — that is the whole check — and the useful part is not that it finds broken promises but that the two kinds of broken come back down different wires: one as isError: true on a successful call, one as a JSON-RPC error with the undefined code 0.

### 3.3 - Declared before anything runs
`days/day-41-capabilities-and-mcp-apps/parts/03-declared-versus-implemented/3.3-declared-before-anything-runs.md` · level `working` · ids MCP-19

Every mechanism this curriculum has met since Day 34 obeys one rule — whatever a server will do to a client is declared before the client does anything — and that rule is not a coincidence, it is the design stance that makes a stranger's server reviewable at all.

### 4.1 - A tool that brings its own window
`days/day-41-capabilities-and-mcp-apps/parts/04-a-server-that-draws/4.1-a-tool-that-brings-its-own-window.md` · level `foundation` · ids MCP-29

MCP Apps — extension identifier io.modelcontextprotocol/ui — lets a tool point at an HTML page the server also serves, which the host renders inside the conversation, so a server that has never had a screen can put a form in front of your user.

### 4.2 - The template is declared, the data flows in
`days/day-41-capabilities-and-mcp-apps/parts/04-a-server-that-draws/4.2-the-template-is-declared-the-data-flows-in.md` · level `working` · ids MCP-29, MCP-19

A pre-declared ui:// template buys three things arbitrary HTML cannot: the host can fetch it before the call, hash and pin it, and refuse it by policy — and the data that varies arrives separately, as data, through the bridge.

### 4.3 - What the sandbox actually stops
`days/day-41-capabilities-and-mcp-apps/parts/04-a-server-that-draws/4.3-what-the-sandbox-actually-stops.md` · level `working` · ids MCP-29

The host builds a Content-Security-Policy from the resource's own _meta.ui.csp declaration, starting at default-src 'none' and adding only origins the server named — so a page that declares nothing can load nothing, reach nothing and phone nowhere, and a host may narrow that policy but must never widen it.

### 4.4 - The dialect spoken through the glass
`days/day-41-capabilities-and-mcp-apps/parts/04-a-server-that-draws/4.4-the-dialect-spoken-through-the-glass.md` · level `working` · ids MCP-29

The panel's only wire to the world is a JSON-RPC dialect over postMessage, with a fixed vocabulary of ui/-prefixed methods plus a handful of ordinary MCP ones — so everything the page can say is on a list, and every tool call it makes is routed by the host and audited like any other.

### 4.5 - 🅿️ Why Sutra ships no App
`days/day-41-capabilities-and-mcp-apps/parts/04-a-server-that-draws/4.5-parked-why-sutra-ships-no-app.md` · level `production` · ids MCP-29

🅿️ Parked, with three reasons and a trigger: Sutra's one UI-shaped problem is already solved by elicitation, an App needs a browser and a build toolchain this budget does not have, and shipping one would mean declaring io.modelcontextprotocol/ui on the client side too — so it is documented, interview-ready, and deliberately not built.

### 5.1 - 💥 The panel that grew a button
`days/day-41-capabilities-and-mcp-apps/parts/05-failure-lab/5.1-the-panel-that-grew-a-button.md` · level `production` · ids MCP-29, MCP-19

Interpolate a ticket body into markup and the ticket body becomes markup: the same input that renders as one Approve button in a declared template renders as two buttons and an onclick handler when the page is built per call — and the second button was written by whoever filed the ticket.

### 5.2 - 💥 The family that went away
`days/day-41-capabilities-and-mcp-apps/parts/05-failure-lab/5.2-the-family-that-went-away.md` · level `production` · ids MCP-19

Removing the last prompt from a server removes the whole prompts family, and a client holding a cached declaration gets -32601 Method not found instead of the empty list or the retirement message a removed tool would have produced — a bigger, blunter failure than Day 34's, and it needs two deployments for a different reason.

### 6.1 - The declaration you keep in git
`days/day-41-capabilities-and-mcp-apps/parts/06-in-production/6.1-the-declaration-you-keep-in-git.md` · level `production` · ids MCP-19, MCP-18

sutra_mcp/capabilities.py is the day's project code: the families and extensions Sutra intends to declare, written down as data, plus an audit(server) that compares the intention against what the SDK actually emits — because the emitted declaration is derived and the intended one is a decision.

### 6.2 - Before a stranger draws on your screen
`days/day-41-capabilities-and-mcp-apps/parts/06-in-production/6.2-before-a-stranger-draws-on-your-screen.md` · level `production` · ids MCP-29

Enabling a server's UI is a review decision, not a configuration flag — nine questions, asked in order, and the first four can be answered by fetching the template before anything renders, which is the entire reason the specification made you pre-declare it.


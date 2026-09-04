# Day 32 - MCP 2026 — the stateless core, governance and the registry

IDs closed: MCP-01, MCP-26, MCP-32 · source: `days/day-32-mcp-stateless-core/`

## Parts

### 1.1 - The plug that fits
`days/day-32-mcp-stateless-core/parts/01-the-socket/1.1-the-plug-that-fits.md` · level `foundation` · ids MCP-01

The Model Context Protocol (MCP) is an agreed message format for asking a separate program for tools, data and prompt templates, so that a tool written once can be used by every AI application that speaks it, instead of being rewritten for each one.

### 1.2 - Host, client, server
`days/day-32-mcp-stateless-core/parts/01-the-socket/1.2-host-client-server.md` · level `foundation` · ids MCP-01

Three words for three different jobs: the host is the application a person is using, the server is the program offering tools and data, and the client is the one-per-server connector inside the host that talks to exactly one server and nothing else.

### 1.3 - Tools, resources, prompts
`days/day-32-mcp-stateless-core/parts/01-the-socket/1.3-tools-resources-prompts.md` · level `foundation` · ids MCP-01

A server offers three different kinds of thing and they are distinguished by who decides to use them: a tool is chosen by the model, a resource is data the host reads and places in context, and a prompt is a template the person picks.

### 1.4 - Not just another API
`days/day-32-mcp-stateless-core/parts/01-the-socket/1.4-not-just-another-api.md` · level `working` · ids MCP-01

MCP is not a better HTTP API; it is a fixed one — every server exposes the same seven methods, so a client written once works against every server ever written, which an OpenAPI toolset can never promise.

### 1.5 - One gate to guard
`days/day-32-mcp-stateless-core/parts/01-the-socket/1.5-one-gate-to-guard.md` · level `working` · ids MCP-01

Sutra bets its data boundary on MCP because a boundary you can point at is a boundary you can guard, measure and replace — and a Python import is none of those three.

### 2.1 - The call that remembered you
`days/day-32-mcp-stateless-core/parts/02-the-reframe/2.1-the-call-that-remembered-you.md` · level `foundation` · ids MCP-26

Until 2026-07-28, an MCP conversation began with an initialize handshake and every later message depended on the server still remembering it — a session — and the 2026-07-28 revision deleted both the handshake and the memory.

### 2.2 - Three instances, one URL
`days/day-32-mcp-stateless-core/parts/02-the-reframe/2.2-three-instances-one-url.md` · level `working` · ids MCP-26

The reason the handshake had to go is arithmetic: with three interchangeable copies of a server behind one address, a session held by one copy makes two thirds of your requests fail — measured here as 2 of 4 served with a session against 4 of 4 without one.

### 2.3 - Every request introduces itself
`days/day-32-mcp-stateless-core/parts/02-the-reframe/2.3-every-request-introduces-itself.md` · level `working` · ids MCP-26

What the handshake used to establish once now rides inside every request in a block called _meta — the protocol version, the client's capabilities and the client's name — and on this machine that block measures 184 bytes, repeated forever.

### 2.4 - The optional question
`days/day-32-mcp-stateless-core/parts/02-the-reframe/2.4-server-discover-the-optional-question.md` · level `working` · ids MCP-26

server/discover is the one RPC every server MUST implement and every client MAY skip: it returns the versions, capabilities and identity a handshake used to negotiate, without being a handshake, because nothing is remembered afterwards.

### 3.1 - The label on the envelope
`days/day-32-mcp-stateless-core/parts/03-headers-and-caches/3.1-the-label-on-the-envelope.md` · level `working` · ids MCP-26

Streamable HTTP now requires three headers — MCP-Protocol-Version, Mcp-Method and, for calls and reads, Mcp-Name — that copy fields out of the JSON body onto the outside of the request, so that a load balancer or gateway can route on them without parsing the body.

### 3.2 - The header that must match
`days/day-32-mcp-stateless-core/parts/03-headers-and-caches/3.2-the-header-that-must-match.md` · level `working` · ids MCP-26

A server that reads the body MUST reject any request whose headers disagree with it — HTTP 400 Bad Request and JSON-RPC error -32020 HeaderMismatch — because a router deciding on one value while the server executes another is a security hole, not an inconsistency.

### 3.3 - Lists you may keep
`days/day-32-mcp-stateless-core/parts/03-headers-and-caches/3.3-lists-you-may-keep.md` · level `working` · ids MCP-26

Because a list no longer varies per connection, every list result now must carry ttlMs and cacheScope — turning 60 tools/list requests into 3 when each client caches, and into 1 when a shared proxy may — and tools should come back in a deterministic order so the prompt built from them is byte-identical every time.

### 3.4 - State that travels in the payload
`days/day-32-mcp-stateless-core/parts/03-headers-and-caches/3.4-state-that-travels-in-the-payload.md` · level `working` · ids MCP-26

Statelessness does not mean a server can never remember anything; it means the memory is named by an opaque handle the server mints and the client passes back as an ordinary tool argument, so the memory lives in shared storage instead of in one instance's process.

### 4.1 - A standard nobody owns
`days/day-32-mcp-stateless-core/parts/04-governance-and-registry/4.1-a-standard-nobody-owns.md` · level `foundation` · ids MCP-32

On 2025-12-09 MCP was donated to the Agentic AI Foundation, a directed fund under the Linux Foundation, co-founded by three companies and supported by five more — which is what makes it defensible to put a company's data boundary on it.

### 4.2 - The registry, queried live
`days/day-32-mcp-stateless-core/parts/04-governance-and-registry/4.2-the-registry-queried-live.md` · level `working` · ids MCP-32

There is one official catalogue of public MCP servers, it is a plain REST API at registry.modelcontextprotocol.io/v0/servers needing no key, and it holds metadata about where a server lives rather than the server's code — which is why what it does and does not check is the part to learn.

### 4.3 - A name that proves its publisher
`days/day-32-mcp-stateless-core/parts/04-governance-and-registry/4.3-a-name-that-proves-its-publisher.md` · level `working` · ids MCP-32

Registry names are reverse-DNS — io.github.someone/their-server, com.example/tickets — and the namespace is not a convention but a claim the publisher had to prove, by controlling that domain or that account; it proves authorship and nothing else.

### 5.1 - 💥 The tutorial from four months ago
`days/day-32-mcp-stateless-core/parts/05-failure-lab/5.1-the-tutorial-from-four-months-ago.md` · level `production` · ids MCP-26

The date on a document is part of the document — and this is not only true of blog posts: the mcp SDK pinned in this repository reports LATEST_PROTOCOL_VERSION = '2025-11-25', so the library Sutra will install on Day 34 cannot speak the revision this whole phase is built on.

### 5.2 - 💥 The header that lied
`days/day-32-mcp-stateless-core/parts/05-failure-lab/5.2-the-header-that-lied.md` · level `production` · ids MCP-26

Forge Mcp-Name so the header says one tool and the body says another, and you discover what the -32020 rule is actually defending: a gateway that has already allowed, counted and routed a request that the server is about to execute as something else entirely.

### 6.1 - Routing without reading
`days/day-32-mcp-stateless-core/parts/06-in-production/6.1-routing-without-reading.md` · level `production` · ids MCP-26

Put the two properties together — self-contained requests and labelled envelopes — and you can run an edge layer that routes, throttles and measures every MCP call without parsing a single body, which is the deployment sutra-mcp gets on Day 43.

### 6.2 - Before you depend on a server
`days/day-32-mcp-stateless-core/parts/06-in-production/6.2-before-you-depend-on-a-server.md` · level `production` · ids MCP-01, MCP-32

A server inside the data boundary is a dependency with a publisher, a version and a protocol revision — so the intake is six questions with an exit code, and "it worked when I tried it" is not one of them.

## Papers - read after the parts

### doi:10.1145/514183.514185 - Principled design of the modern Web architecture
`days/day-32-mcp-stateless-core/papers/01-modern-web-architecture.md`

It argued that the web scaled because of what its architecture forbids rather than what it offers: a named set of constraints — client-server, stateless, cacheable, uniform interface, layered system, optional code-on-demand — each one buying a property and charging a stated price.


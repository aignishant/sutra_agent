# Day 33 - The client side — Sutra plugs into its first MCP server

IDs closed: MCP-02, MCP-03 · source: `days/day-33-client-and-transports/`

## Parts

### 1.1 - The tool that lives somewhere else
`days/day-33-client-and-transports/parts/01-the-connector/1.1-the-tool-that-lives-somewhere-else.md` · level `foundation` · ids MCP-02

McpToolset is Sutra's MCP client wearing a toolset's clothes: it holds the connection to exactly one server, and everything on Sutra's side of it — the agent, the model, the callbacks — goes on treating those tools exactly like the local Python functions from Day 10.

### 1.2 - Constructing is not connecting
`days/day-33-client-and-transports/parts/01-the-connector/1.2-constructing-is-not-connecting.md` · level `foundation` · ids MCP-02

McpToolset(...) builds a description of how to reach a server and connects to nothing; the first network traffic — or the first child process — happens inside the first await get_tools(), which is why a wrong address is silent until much later.

### 1.3 - Before the model sees a tool
`days/day-33-client-and-transports/parts/01-the-connector/1.3-before-the-model-sees-a-tool.md` · level `working` · ids MCP-02

get_tools() is five steps, not one — connect, list, convert, filter, sort — and every one of them changes what the model is told exists, which is why a tool can be on the server and invisible to the agent with nothing broken anywhere.

### 1.4 - The allowlist is a constructor argument
`days/day-33-client-and-transports/parts/01-the-connector/1.4-the-allowlist-is-an-argument.md` · level `working` · ids MCP-02

tool_filter=[...] decides which of a server's tools the model is ever told exist, and it is the difference between a capability the agent has and a capability it does not — an instruction is a request, a tool list is a grant.

### 1.5 - Somebody has to give it back
`days/day-33-client-and-transports/parts/01-the-connector/1.5-somebody-has-to-give-it-back.md` · level `working` · ids MCP-02

An McpToolset owns something outside your process — a child process or an HTTP client — and await toolset.close() is the only thing that releases it, which is why every script in this day puts its get_tools() inside a try and its close() inside the matching finally.

### 2.1 - Connecting is launching
`days/day-33-client-and-transports/parts/02-stdio/2.1-connecting-is-launching.md` · level `foundation` · ids MCP-03

On the stdio transport there is nothing to connect to until the client starts it: the client launches the server as a child process and talks to it through that process's own standard input and output, so the connection and the server's whole lifetime are the same thing.

### 2.2 - One message per line
`days/day-33-client-and-transports/parts/02-stdio/2.2-one-message-per-line.md` · level `working` · ids MCP-03

stdio's entire framing is "one JSON-RPC message per line, and a message MUST NOT contain an embedded newline", which makes the newline character the only thing separating two messages — and therefore the only thing that can be got wrong.

### 2.3 - The only place left to talk
`days/day-33-client-and-transports/parts/02-stdio/2.3-the-only-place-left-to-talk.md` · level `working` · ids MCP-03

Because stdout is the wire, stderr is the only channel a stdio server has for humans — the specification lets a server write anything it likes there, and requires the client not to treat any of it as an error.

### 2.4 - Closing up
`days/day-33-client-and-transports/parts/02-stdio/2.4-closing-up.md` · level `working` · ids MCP-03

The stdio shutdown is an ordered sequence — close the server's input, wait for it to exit, and only then force it — and its counterpart is that a server which dies unexpectedly is simply restarted, because a stateless protocol has nothing to lose when it does.

### 3.1 - One endpoint, one trip per question
`days/day-33-client-and-transports/parts/03-streamable-http/3.1-one-endpoint-one-trip.md` · level `working` · ids MCP-03

Streamable HTTP gives a server exactly one URL that accepts POST, and every single JSON-RPC message is its own POST to it — so there is no connection to establish, nothing to keep open between requests, and no second address to configure.

### 3.2 - Handed over, or told to wait
`days/day-33-client-and-transports/parts/03-streamable-http/3.2-handed-over-or-told-to-wait.md` · level `working` · ids MCP-03

The server decides, per request, whether to answer with a single JSON object or with an SSE stream that carries progress notifications before the final response — which is why an MCP client over HTTP must be able to read both, and why "streaming" here means one request's own updates and nothing else.

### 3.3 - Standing up is how you cancel
`days/day-33-client-and-transports/parts/03-streamable-http/3.3-standing-up-is-how-you-cancel.md` · level `working` · ids MCP-03

Cancellation is the one place where the two transports genuinely differ: on Streamable HTTP closing the request's response stream is the cancellation, while on stdio — where there is only one shared channel and nothing to close — the client must send an explicit notifications/cancelled.

### 3.4 - What a URL costs
`days/day-33-client-and-transports/parts/03-streamable-http/3.4-what-a-url-costs.md` · level `production` · ids MCP-03

Giving a server an address makes it reachable by everything that can reach addresses, which is why the Streamable HTTP binding opens with three security requirements — validate Origin, bind to localhost when local, authenticate — that the stdio binding does not need at all.

### 4.1 - The same errand, two ways to run it
`days/day-33-client-and-transports/parts/04-choosing-a-wire/4.1-the-same-errand-two-ways.md` · level `working` · ids MCP-02, MCP-03

Because protocol semantics are identical on every transport, choosing between stdio and Streamable HTTP is an operational decision and never a functional one — and in ADK it is one class name, so the choice must be made on purpose rather than inherited from whichever tutorial you read.

### 4.2 - 🅿️ The route with a withdrawal date
`days/day-33-client-and-transports/parts/04-choosing-a-wire/4.2-the-route-with-a-withdrawal-date.md` · level `production` · ids MCP-03

The 2024-11-05 HTTP+SSE transport — a long-lived GET stream plus a separate POST endpoint — has been Deprecated since revision 2025-03-26 and is eligible for removal, so Sutra learns to recognise it and never builds on it: this part is parked, and parked means interview-ready and deliberately unbuilt.

### 5.1 - 💥 The log line that ate the reply
`days/day-33-client-and-transports/parts/05-failure-lab/5.1-the-log-line-that-ate-the-reply.md` · level `production` · ids MCP-03

One print() in a stdio server puts non-protocol bytes on the wire, and whether that is a logged warning you never read or a total failure depends on something nobody thinks about while writing it: whether the text ended with a newline.

### 5.2 - 💥 The spanner that was not in the boot
`days/day-33-client-and-transports/parts/05-failure-lab/5.2-the-spanner-not-in-the-boot.md` · level `production` · ids MCP-02

A command that is not on PATH is accepted silently by every layer that could have caught it, and surfaces one layer too late as a ConnectionError wrapping an operating-system code that on Windows does not even name the missing file.

### 6.1 - The connection you must not hold
`days/day-33-client-and-transports/parts/06-in-production/6.1-the-connection-you-must-not-hold.md` · level `production` · ids MCP-02, MCP-03

Nothing in the 2026-07-28 protocol requires a client to keep anything open between requests, so anything your client does keep open is an optimisation that infrastructure is allowed to take away from you — and every piece of infrastructure eventually does.

### 6.2 - Ten servers, ten clients
`days/day-33-client-and-transports/parts/06-in-production/6.2-ten-servers-ten-clients.md` · level `production` · ids MCP-02

One client per server is an isolation guarantee, not an implementation detail — so a host with ten servers has ten independent failure domains, and the work of production MCP is making sure the tenth one being broken does not stop the other nine.


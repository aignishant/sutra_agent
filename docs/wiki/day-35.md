# Day 35 - Resources and prompts

IDs closed: MCP-09, MCP-07, MCP-08 · source: `days/day-35-resources-and-prompts/`

## Parts

### 1.1 - The hand that reaches first
`days/day-35-resources-and-prompts/parts/01-who-initiates/1.1-the-hand-that-reaches-first.md` · level `foundation` · ids MCP-09

You do not choose between a tool, a resource and a prompt by looking at the data — you choose by naming whose hand reaches for it first: the model's, the host program's, or the person's.

### 1.2 - What a door costs
`days/day-35-resources-and-prompts/parts/01-who-initiates/1.2-what-a-door-costs.md` · level `foundation` · ids MCP-09

A tool costs a decision the model has to make and can get wrong on every turn; a resource costs nothing at decision time, because the host already knew the address and simply handed the material over.

### 1.3 - Should lookup_ticket stop being a tool?
`days/day-35-resources-and-prompts/parts/01-who-initiates/1.3-should-lookup-ticket-stop-being-a-tool.md` · level `working` · ids MCP-09

No — it gains a second door rather than swapping doors: ticket://{ticket_id} is added as a resource and lookup_ticket stays a tool, and the price of that answer is one store read through two code paths, which you pay by writing the paths as two thin adapters over one function.

### 2.1 - An address, not a call
`days/day-35-resources-and-prompts/parts/02-the-shelf/2.1-an-address-not-a-call.md` · level `foundation` · ids MCP-07

A resource is not a function you invoke, it is a name — a URI — and publishing one means promising that anybody who says that name gets the same thing, without describing what they want or being asked who they are.

### 2.2 - What comes back from a read
`days/day-35-resources-and-prompts/parts/02-the-shelf/2.2-what-comes-back-from-a-read.md` · level `working` · ids MCP-07

resources/read never returns a document — it returns a list of contents, and every item in that list carries its own URI and its own MIME type, so a single read may legitimately hand back several things at once.

### 2.3 - The miss that must be an error
`days/day-35-resources-and-prompts/parts/02-the-shelf/2.3-the-miss-that-must-be-an-error.md` · level `working` · ids MCP-07

A resource that does not exist MUST come back as JSON-RPC error -32602 and never as content — and the convenience wrapper in the pinned SDK quietly turns your correct -32602 into code: 0, which you can only find out by looking at the wire.

### 2.4 - One label for a whole family
`days/day-35-resources-and-prompts/parts/02-the-shelf/2.4-one-label-for-a-family.md` · level `working` · ids MCP-07

A resource template publishes the shape of an address rather than every address — ticket://{ticket_id} instead of twenty thousand entries — and the shape promises more addresses than you own, including ones that do not exist and ones you never meant to offer.

### 3.1 - The words the house owns
`days/day-35-resources-and-prompts/parts/03-the-card/3.1-the-words-the-house-owns.md` · level `foundation` · ids MCP-08

A prompt is a named piece of wording that the server writes and the person chooses to use, so the house style of asking travels with the data instead of being retyped by every host that connects.

### 3.2 - Arguments are declared, not guessed
`days/day-35-resources-and-prompts/parts/03-the-card/3.2-arguments-are-declared.md` · level `working` · ids MCP-08

A prompt publishes its arguments by name, with a description and a required flag, so a host can build a form instead of guessing — and the specification says a missing one is -32602, which is a promise you have to check your server actually keeps.

### 3.3 - What a prompt hands back
`days/day-35-resources-and-prompts/parts/03-the-card/3.3-what-a-prompt-hands-back.md` · level `working` · ids MCP-08

prompts/get returns messages, not a string — a list of {role, content} items — so a prompt can hand back a whole opening exchange with worked examples in it, and the role on each item is load bearing rather than packaging.

### 3.4 - The card that points at the shelf
`days/day-35-resources-and-prompts/parts/03-the-card/3.4-the-card-that-points-at-the-shelf.md` · level `working` · ids MCP-08, MCP-09

A prompt message can carry the document itself (resource) or only its address (resource_link), and the choice is the same one the shelf and the counter were about — whether the server decides what gets read, or the host does.

### 4.1 - Every read carries its own expiry
`days/day-35-resources-and-prompts/parts/04-freshness/4.1-every-read-carries-its-expiry.md` · level `working` · ids MCP-07

resources/read is the only non-list operation the revision made cacheable, so every read must say how long it stays fresh and who may keep it — and the SDK pinned in this repository cannot say either, which is a finding rather than a footnote.

### 4.2 - Subscribing with nobody on the line
`days/day-35-resources-and-prompts/parts/04-freshness/4.2-subscribing-with-nobody-on-the-line.md` · level `production` · ids MCP-07

"Subscribe to a resource" survived the stateless rewrite by becoming one long-lived request the client opens on purpose — subscriptions/listen — which means the held connection did not disappear, it became something you have to ask for, pay for and re-establish yourself.

### 4.3 - The list that outlived the deploy
`days/day-35-resources-and-prompts/parts/04-freshness/4.3-the-list-that-outlived-the-deploy.md` · level `production` · ids MCP-07

ttlMs on resources/list is also how long clients keep offering an address you deleted, so removing a resource is two deployments — shorten the TTL, wait it out, then remove — and doing it in one produces a burst of -32602 that looks like a client bug and is not.

### 5.1 - 💥 The address that reached outside the room
`days/day-35-resources-and-prompts/parts/05-failure-lab/5.1-the-address-that-reached-outside.md` · level `production` · ids MCP-07

The SDK's template matcher refuses a / in a parameter, which looks like a safety check and is not one — percent-encode the slashes and the matcher passes them through untouched, and it is your handler that decodes them and opens a file outside the directory you meant to publish.

### 5.2 - 💥 The read that filled the window
`days/day-35-resources-and-prompts/parts/05-failure-lab/5.2-the-read-that-filled-the-window.md` · level `production` · ids MCP-07, MCP-09

A resource is context you chose to spend, so archive://all is not a convenience — it is a design that works on two tickets, fails outright on twenty thousand, and does its worst damage in between, where it fits and buries the answer in the middle.

### 5.3 - 💥 The argument that gave an order
`days/day-35-resources-and-prompts/parts/05-failure-lab/5.3-the-argument-that-gave-an-order.md` · level `production` · ids MCP-08

The server renders prompts/get, so an argument dropped straight into your wording becomes an instruction signed with your server's name — which makes prompt injection through a prompt your bug, not the host's, and the fix is validate at the door and fence what survives.

### 6.1 - Two modules, one server
`days/day-35-resources-and-prompts/parts/06-in-production/6.1-two-modules-one-server.md` · level `production` · ids MCP-09

sutra_mcp/resources.py and sutra_mcp/prompts.py each expose one function that takes the server and registers into it — register_resources(server) — because a module that decorates a global at import time cannot be tested, cannot be ordered, and cannot be left out.

### 6.2 - The shelf a stranger can use
`days/day-35-resources-and-prompts/parts/06-in-production/6.2-the-shelf-a-stranger-can-use.md` · level `production` · ids MCP-09

Every optional metadata field — title, description, mimeType, annotations — is what a host needs to build a picker out of your server, so a shelf that is technically valid and metadata-poor is a shelf nobody can find anything on, and the day's gate is a script that says so.


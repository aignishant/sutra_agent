# Day 40 - Tool filtering, allowlists and the MCP security posture

IDs closed: MCP-16, SEC-03, MCP-17 · source: `days/day-40-filtering-and-allowlists/`

## Parts

### 1.1 - The list of things you thought of
`days/day-40-filtering-and-allowlists/parts/01-the-list-you-agreed-to/1.1-the-list-of-things-you-thought-of.md` · level `foundation` · ids MCP-16

A deny-list is a list of things you thought of, an allowlist is a list of things you agreed to, and the two are identical right up to the moment somebody adds something neither of you discussed.

### 1.2 - A tool list is a stranger's text
`days/day-40-filtering-and-allowlists/parts/01-the-list-you-agreed-to/1.2-a-tool-list-is-a-strangers-text.md` · level `foundation` · ids SEC-03

A tool's description is not metadata about the tool: it is a sentence written by whoever runs the server, copied into your model's context, and read by the model as documentation it should follow.

### 1.3 - The filter is on your side of the wire
`days/day-40-filtering-and-allowlists/parts/01-the-list-you-agreed-to/1.3-the-filter-is-on-your-side.md` · level `working` · ids MCP-16

An allowlist runs inside your own process, after the server has already sent you everything it has, so it decides what the model sees and never what the network carries.

### 2.1 - One argument, three spellings
`days/day-40-filtering-and-allowlists/parts/02-the-filter-in-adk/2.1-one-argument-three-spellings.md` · level `working` · ids MCP-16

tool_filter accepts exactly three things — None, a list[str] of names, or a callable — and the framework decides which of the three you meant by looking at the value's type, not at what you intended.

### 2.2 - The rule that reads the room
`days/day-40-filtering-and-allowlists/parts/02-the-filter-in-adk/2.2-the-rule-that-reads-the-room.md` · level `working` · ids MCP-16

A ToolPredicate is a function ADK calls once per tool per listing, handing it the tool and the current context, so the answer can depend on who is asking rather than only on what the tool is called.

### 2.3 - The names the framework keeps
`days/day-40-filtering-and-allowlists/parts/02-the-filter-in-adk/2.3-the-names-the-framework-keeps.md` · level `working` · ids SEC-03

Four tool names belong to ADK itself, and a server advertising one of them has its tool dropped with a warning, because otherwise the server's tool would be dispatched in place of the framework's own.

### 2.4 - 💥 The empty list that admits everything
`days/day-40-filtering-and-allowlists/parts/02-the-filter-in-adk/2.4-the-empty-list-that-admits-everything.md` · level `production` · ids MCP-16, SEC-03

tool_filter=[] reads as "no filter" and hands the model every tool the server has, because the framework tests the value for truth rather than for absence — and an empty list is false.

### 3.1 - The Tuesday a tool appeared
`days/day-40-filtering-and-allowlists/parts/03-when-the-server-changes/3.1-the-tuesday-a-tool-appeared.md` · level `working` · ids MCP-17

A server growing a new tool is a routine release for its author and an unreviewed capability for you, and the only thing that decides which of those two it becomes is the posture you chose before it happened.

### 3.2 - 💥 The name held, the sentence moved
`days/day-40-filtering-and-allowlists/parts/03-when-the-server-changes/3.2-the-name-held-the-sentence-moved.md` · level `production` · ids MCP-17, SEC-03

An allowlist compares names and a model reads descriptions, so a server can rewrite the description of a tool you approved and your filter will forward the new sentence without noticing.

### 3.3 - The list you kept is the list you trust
`days/day-40-filtering-and-allowlists/parts/03-when-the-server-changes/3.3-the-list-you-kept-is-the-list-you-trust.md` · level `production` · ids MCP-17

tool_list_cache_ttl_seconds turns three listings into one, and buys that saving with a window in which a tool the server has added or removed is invisible to you.

### 4.1 - One door, and a check that there is one
`days/day-40-filtering-and-allowlists/parts/04-the-policy-module/4.1-one-door-and-a-check-there-is-one.md` · level `working` · ids MCP-17

Sutra builds every MCP toolset in sutra/mcp/filtering.py and nowhere else, and the way that stays true is a script that reads the source and names any other file that constructs one.

### 4.2 - A policy you can diff
`days/day-40-filtering-and-allowlists/parts/04-the-policy-module/4.2-a-policy-you-can-diff.md` · level `working` · ids MCP-17

The allowlist is one field of a record — how the server is reached, which names are allowed, what their descriptions hashed to, who reviewed them and when — and the record exists so that approving a server is a commit somebody can read rather than a conversation nobody can find.

### 4.3 - `deny` inside the allowlist
`days/day-40-filtering-and-allowlists/parts/04-the-policy-module/4.3-deny-inside-the-allowlist.md` · level `working` · ids MCP-17

deny is a second subtraction applied after the allowlist has already decided, so it can only ever make Sutra's tool list smaller — and it exists to hold the names that must stay out even if somebody adds them to the allowlist by mistake.

### 5.1 - 💥 The container that admits nothing
`days/day-40-filtering-and-allowlists/parts/05-failure-lab/5.1-the-container-that-admits-nothing.md` · level `production` · ids MCP-16

A tuple or a bare string in tool_filter falls off the end of ADK's selection rule and refuses every tool, so the agent starts cleanly with no tools at all and nobody finds out until a user complains.

### 5.2 - 💥 Filtered after it was read
`days/day-40-filtering-and-allowlists/parts/05-failure-lab/5.2-filtered-after-it-was-read.md` · level `production` · ids MCP-16, SEC-03

A filter applied to the model's reply instead of to the tool list is not a filter, because the descriptions were already in the request the model read.

### 5.3 - 💥 The pattern that matched more than it named
`days/day-40-filtering-and-allowlists/parts/05-failure-lab/5.3-the-pattern-that-matched-more.md` · level `production` · ids MCP-16

The moment an allowlist is written as a pattern instead of as names, it stops being a list of things you agreed to and becomes a rule about strings — and an unanchored pattern agrees to every name that merely contains one of yours.

### 6.1 - 💥 Two servers, one tool name
`days/day-40-filtering-and-allowlists/parts/06-the-posture/6.1-two-servers-one-tool-name.md` · level `production` · ids SEC-03

The model is handed one flat list of tool names with no server attached, so two servers offering check_status produce two identical entries and nothing in the protocol says which one gets called.

### 6.2 - The attacks a filter does not stop
`days/day-40-filtering-and-allowlists/parts/06-the-posture/6.2-the-attacks-a-filter-does-not-stop.md` · level `production` · ids SEC-03

An allowlist controls which tools exist for the model, and controls nothing about what the descriptions of the allowed tools say, what the allowed tools return, or what the model does with either — and for some of that there is no mitigation available today.

### 6.3 - The host decides, not the server
`days/day-40-filtering-and-allowlists/parts/06-the-posture/6.3-the-host-decides-not-the-server.md` · level `production` · ids SEC-03

Every trust decision in MCP belongs to the host application, because the server is the party being trusted and a server's own claims about itself are exactly the thing under question.

### 6.4 - What you write down before you connect
`days/day-40-filtering-and-allowlists/parts/06-the-posture/6.4-what-you-write-down-before-you-connect.md` · level `production` · ids MCP-17, SEC-03

Connecting to a new MCP server is an intake with eight written answers, and the value of writing them down is that adding a server becomes a reviewable commit rather than a line somebody added on a Thursday.

## Papers - read after the parts

### doi:10.1109/PROC.1975.9939 - The protection of information in computer systems
`days/day-40-filtering-and-allowlists/papers/01-protection-of-information.md`

It gave the field eight named design principles for protection — least privilege, fail-safe defaults, complete mediation, economy of mechanism, open design, separation of privilege, least common mechanism and psychological acceptability — and fifty years later they are still the words people argue in.


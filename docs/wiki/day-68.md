# Day 68 - Permissions & least privilege for tools

IDs closed: SEC-11, SEC-10 · source: `days/day-68-least-privilege-tools/`

## Parts

### 1.1 - The errand, and the keys that went with it
`days/day-68-least-privilege-tools/parts/01-the-deputy/1.1-the-errand-and-the-keys-that-went-with-it.md` · level `foundation` · ids SEC-11

The agent is a deputy: it acts on instructions you do not control while holding authority you do control, and the only part of that sentence you can change is the second half.

### 1.2 - A tool does its job, not your intention
`days/day-68-least-privilege-tools/parts/01-the-deputy/1.2-a-tool-does-its-job-not-your-intention.md` · level `foundation` · ids SEC-11

Nothing in the run that closed another customer's ticket was a malfunction: every tool did precisely what it was written to do, which is why "make the tools work correctly" is not a security plan.

### 1.3 - Whose permissions is the tool using?
`days/day-68-least-privilege-tools/parts/01-the-deputy/1.3-whose-permissions-is-the-tool-using.md` · level `working` · ids SEC-10

A tool runs with the service's credentials, not the caller's, so unless the tool asks who is calling and narrows itself, every user of your agent has the agent's reach.

### 1.4 - A rule in words is not a permission
`days/day-68-least-privilege-tools/parts/01-the-deputy/1.4-a-rule-in-words-is-not-a-permission.md` · level `working` · ids SEC-11

An instruction telling the agent not to do something adds no stop anywhere in the machinery, so whether it holds depends entirely on the model's cooperation — which is the one thing you are not allowed to assume.

### 2.1 - May it? Capability, and the line between read and write
`days/day-68-least-privilege-tools/parts/02-three-questions/2.1-may-it-capability-and-the-read-write-line.md` · level `foundation` · ids SEC-10

The first question a permission answers is what kind of thing may this tool do, and the answer is useless unless reading and writing are counted as different kinds — because one of them can be undone and the other cannot.

### 2.2 - Which rows? Scope, and the tool that is allowed on everything
`days/day-68-least-privilege-tools/parts/02-three-questions/2.2-which-rows-scope.md` · level `working` · ids SEC-10, SEC-11

A capability with no scope is a permission on the whole table, and the difference between "may close a ticket" and "may close this ticket" is the difference between a support desk and a way to close anybody's tickets.

### 2.3 - How many times? Rate is a permission too
`days/day-68-least-privilege-tools/parts/02-three-questions/2.3-how-many-times-rate.md` · level `working` · ids SEC-10

A grant that answers may it? and not how much of it? is a grant with no upper bound, and on a free tier the upper bound is the only thing standing between one run and a dry quota.

### 2.4 - The table you can diff
`days/day-68-least-privilege-tools/parts/02-three-questions/2.4-the-table-you-can-diff.md` · level `working` · ids SEC-10

Write the permissions down as data in the repository, one row per tool, because a policy that lives only in code cannot be reviewed by the person who most needs to review it and cannot be diffed by anybody at all.

### 3.1 - Deny by default, at the toolset
`days/day-68-least-privilege-tools/parts/03-absent-not-forbidden/3.1-deny-by-default-at-the-toolset.md` · level `working` · ids SEC-10, SEC-11

Build the agent's tool list from an allowlist rather than trimming a full one, because the two produce the same list today and diverge the moment somebody adds a tool.

### 3.2 - The predicate that reads the room
`days/day-68-least-privilege-tools/parts/03-absent-not-forbidden/3.2-the-predicate-that-reads-the-room.md` · level `working` · ids SEC-10

A tool list does not have to be fixed at construction: a predicate is called per invocation with the run's context, so the same agent can be offered different tools depending on who is asking and what the run has established so far.

### 3.3 - What happens when it asks anyway
`days/day-68-least-privilege-tools/parts/03-absent-not-forbidden/3.3-what-happens-when-it-asks-anyway.md` · level `production` · ids SEC-10

A tool that is absent does not produce a polite refusal — the ADK runtime raises ValueError and the run ends, which is correct and is not free, so the denial has to be designed rather than discovered.

### 3.4 - Whose keyring does a helper carry?
`days/day-68-least-privilege-tools/parts/03-absent-not-forbidden/3.4-whose-keyring-does-a-helper-carry.md` · level `production` · ids SEC-11

A sub-agent is offered its own tools and not its parent's, which is the reassuring half; the other half is that it is also offered a way back to the parent, so the authority of the system is the union of every agent control can reach.

### 4.1 - The tool is allowed, the argument is not
`days/day-68-least-privilege-tools/parts/04-the-argument/4.1-the-tool-is-allowed-the-argument-is-not.md` · level `working` · ids SEC-10

Once the tool list is right, the remaining authority is in the arguments, and a permission that stops at the tool name has granted every call that tool can express.

### 4.2 - A path is a sentence about the whole disk
`days/day-68-least-privilege-tools/parts/04-the-argument/4.2-a-path-is-a-sentence-about-the-whole-disk.md` · level `production` · ids SEC-10, SEC-11

A tool that takes a path can read anything the process can read, and the only check that survives every spelling is to resolve the path first and ask whether the result is inside the directory you meant.

### 4.3 - The recipient who is not the customer
`days/day-68-least-privilege-tools/parts/04-the-argument/4.3-the-recipient-who-is-not-the-customer.md` · level `production` · ids SEC-10, SEC-11

The destination of anything leaving your system must come from a record you control, never from an argument the model chose, because an outbound tool with a free recipient is an exfiltration channel wearing the uniform of a support desk.

### 4.4 - The check that belongs outside every tool
`days/day-68-least-privilege-tools/parts/04-the-argument/4.4-the-check-that-belongs-outside-every-tool.md` · level `production` · ids SEC-10, SEC-11

A permission check written inside the tool it guards protects that tool and nothing else, so the rule has to stand outside every tool — in a before_tool_callback or a plugin — where it sees every call instead of one.

### 4.5 - What a refusal must not tell you
`days/day-68-least-privilege-tools/parts/04-the-argument/4.5-what-a-refusal-must-not-tell-you.md` · level `production` · ids SEC-10, SEC-11

A refusal is an answer, so a system that says not yours where it could have said not there has built a lookup service for other people's records and called it an error message.

### 5.1 - The check inside the door it guards
`days/day-68-least-privilege-tools/parts/05-failure-lab/5.1-the-check-inside-the-door-it-guards.md` · level `production` · ids SEC-10, SEC-11

The tenant check inside close_ticket is correct, tested and reviewed, and it protects close_ticket — so the same forbidden request walks through update_ticket, which reaches the same effect and was never told about the rule.

### 5.2 - The tool that arrived without a row
`days/day-68-least-privilege-tools/parts/05-failure-lab/5.2-the-tool-that-arrived-without-a-row.md` · level `production` · ids SEC-10, SEC-11

A permission table becomes a control at the moment a tool with no row is refused instead of allowed, and the gap between the tools the desk offers and the rows the table declares is found by a diff in the build rather than by anybody being careful.

### 5.3 - The helper that handed control back
`days/day-68-least-privilege-tools/parts/05-failure-lab/5.3-the-helper-that-handed-control-back.md` · level `production` · ids SEC-10, SEC-11

Giving a helper agent a narrow toolset is a real control inside the helper and no control at all over the run, because the chain ends where it began — at the agent that still holds the tool.

### 6.1 - One credential per tool
`days/day-68-least-privilege-tools/parts/06-in-production/6.1-one-credential-per-tool.md` · level `production` · ids SEC-10, SEC-11

The credential column is the one column in the permission table that stops being a policy and becomes a boundary: a tool holding a read-only credential cannot write however wrong the rules above it are — and the reason most teams have one credential with a policy on top instead is that the credentials themselves are real, ongoing, unglamorous work.

### 6.2 - Grant is a claim, use is evidence
`days/day-68-least-privilege-tools/parts/06-in-production/6.2-grant-is-a-claim-use-is-evidence.md` · level `production` · ids SEC-10, SEC-11

The permission table says what the desk may do and the audit says what it did, and the gap between the two is the only honest way to find a permission nobody needs — which is why least privilege is not a thing you achieve once but a thing you maintain by subtracting.

## Papers - read after the parts

### doi:10.1145/54289.871709 - The Confused Deputy (or why capabilities might have been invented)
`days/day-68-least-privilege-tools/papers/01-the-confused-deputy.md`

Access control had been asking is this principal allowed to do this?, and this document showed that the question has no useful answer when a program holds an authority its caller does not and does work the caller asked for — because then the program is genuinely allowed, and the caller chose the target.


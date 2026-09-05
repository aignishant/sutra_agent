# Day 36 - Long jobs — progress, task handles and the Tasks extension

IDs closed: MCP-10, MCP-14, MCP-28 · source: `days/day-36-long-jobs-and-tasks/`

## Parts

### 1.1 - The call you cannot leave
`days/day-36-long-jobs-and-tasks/parts/01-the-blocking-call/1.1-the-call-you-cannot-leave.md` · level `foundation` · ids MCP-10

A tool call that does its work while the caller waits has tied the life of the work to the life of one network connection, and a connection is the least durable thing in the system.

### 1.2 - The timeout ladder
`days/day-36-long-jobs-and-tasks/parts/01-the-blocking-call/1.2-the-timeout-ladder.md` · level `working` · ids MCP-10

Raising your timeout never fixes a long job, because the deadline that ends the call is the smallest one on the path and most of the deadlines on the path are not yours to set.

### 1.3 - Work with no name
`days/day-36-long-jobs-and-tasks/parts/01-the-blocking-call/1.3-work-with-no-name.md` · level `working` · ids MCP-10

A JSON-RPC request id names a message, not a job, so when the stream carrying that message breaks the id is spent and the client's only remaining move is to send a brand new request — which the server has no way of recognising as the same errand.

### 2.1 - The token you have to ask for
`days/day-36-long-jobs-and-tasks/parts/02-progress/2.1-the-token-you-have-to-ask-for.md` · level `working` · ids MCP-10

A server may only send progress updates for a request whose _meta carried a progressToken, so progress is something the caller opts into — and a caller that forgets gets silence that looks exactly like success.

### 2.2 - Reporting from inside a tool
`days/day-36-long-jobs-and-tasks/parts/02-progress/2.2-reporting-from-inside-a-tool.md` · level `working` · ids MCP-10

A tool reports progress by asking for a Context parameter and calling report_progress on it, and the installed SDK's implementation of that call returns silently when the caller sent no token — so the reporting code you write is correct whether or not anybody is listening.

### 2.3 - Progress is narration, not state
`days/day-36-long-jobs-and-tasks/parts/02-progress/2.3-progress-is-narration-not-state.md` · level `working` · ids MCP-10

Progress notifications travel on the response stream of the request they belong to and stop when that request ends, so progress can tell you a job is alive but can never tell you what happened to a job you stopped watching.

### 3.1 - A name the server mints
`days/day-36-long-jobs-and-tasks/parts/03-the-handle/3.1-a-name-the-server-mints.md` · level `working` · ids MCP-14

The server writes the job down and hands back its name before it does any of the work, so the name is the one thing in the system that cannot be lost by a connection closing.

### 3.2 - 💥 The handle anyone can guess
`days/day-36-long-jobs-and-tasks/parts/03-the-handle/3.2-the-handle-anyone-can-guess.md` · level `production` · ids MCP-14

A task id that counts upwards is a directory of every other customer's jobs, and the server that hands one out has built an access-control hole that no authentication in front of it can close.

### 3.3 - Sutra's handle policy
`days/day-36-long-jobs-and-tasks/parts/03-the-handle/3.3-sutras-handle-policy.md` · level `production` · ids MCP-14

Sutra's handles are tsk_ plus 128 bits of secrets randomness, owned by the caller who created them, written with an expiry, and missing in exactly one way — and the policy is written as a check with an exit code so that the code cannot drift away from it silently.

### 4.1 - Four messages on the wire
`days/day-36-long-jobs-and-tasks/parts/04-the-tasks-extension/4.1-four-messages-on-the-wire.md` · level `foundation` · ids MCP-28

The Tasks extension is the handle you built in section 3, written down as four standard messages — an opt-in on the request, a CreateTaskResult instead of the answer, a tasks/get poll, and a terminal result — so any client can drive any server's long jobs without knowing anything about that server.

### 4.2 - Five statuses and the terminal rule
`days/day-36-long-jobs-and-tasks/parts/04-the-tasks-extension/4.2-five-statuses-and-the-terminal-rule.md` · level `working` · ids MCP-28

A task is always in exactly one of five states, and three of them are terminal — once a task is completed, failed or cancelled it never changes again, which is the promise that makes a poll result safe to stop asking about.

### 4.3 - Polling is a budget
`days/day-36-long-jobs-and-tasks/parts/04-the-tasks-extension/4.3-polling-is-a-budget.md` · level `production` · ids MCP-28

pollIntervalMs is the server telling you how often it is worth asking, and a client that ignores it turns one long job into thousands of requests that buy nothing — so the cadence is a spending decision, multiplied by every task and every client.

### 4.4 - 💥 Which dialect your SDK speaks
`days/day-36-long-jobs-and-tasks/parts/04-the-tasks-extension/4.4-which-dialect-your-sdk-speaks.md` · level `production` · ids MCP-28

The mcp package pinned in this repository ships a tasks API that the specification removed — the right five statuses, two of the three verbs, two verbs that no longer exist, and field names spelt ttl and pollInterval instead of ttlMs and pollIntervalMs — and the package says so itself, in a deprecation warning you have to go and read.

### 5.1 - Cancel is a request, not a switch
`days/day-36-long-jobs-and-tasks/parts/05-cancellation/5.1-cancel-is-a-request-not-a-switch.md` · level `working` · ids MCP-28

tasks/cancel records an intention and returns immediately; the specification says cancellation is cooperative, so a server may acknowledge your cancel and then finish the job anyway — and a cancelled status is the one status that is never a promise about what happened.

### 5.2 - 💥 The checkpoint that makes cancel real
`days/day-36-long-jobs-and-tasks/parts/05-cancellation/5.2-the-checkpoint-that-makes-cancel-real.md` · level `production` · ids MCP-28

A cancel can only take effect where the work stops to look, so a job with no checkpoint is a job that cannot be cancelled — and from the outside it is indistinguishable from one that simply had not got there yet.

### 6.1 - 💥 The task that says working forever
`days/day-36-long-jobs-and-tasks/parts/06-in-production/6.1-the-task-that-says-working-forever.md` · level `production` · ids MCP-28

A task row says working because somebody wrote working into it, not because anything is working — so when the process holding the job dies, the row goes on claiming progress forever, and only a lease that has to be renewed can tell a slow job from a dead one.

### 6.2 - The job that ran twice
`days/day-36-long-jobs-and-tasks/parts/06-in-production/6.2-the-job-that-ran-twice.md` · level `production` · ids MCP-14

A handle makes a retry safe after you have it; the one request that can still duplicate work is the one that creates the task, and the only thing that closes that gap is a key the client chooses and the server remembers.

### 6.3 - The store is the stateful thing
`days/day-36-long-jobs-and-tasks/parts/06-in-production/6.3-the-store-is-the-stateful-thing.md` · level `production` · ids MCP-14

Every property you removed from the MCP server by going stateless reappears in the task store, so the honest version of "our server is stateless" is "we moved the state to something designed to hold it, and that thing is now the most important component we own".

## Papers - read after the parts

### doi:10.1145/53990.54016 - Promises: linguistic support for efficient asynchronous procedure calls in distributed systems
`days/day-36-long-jobs-and-tasks/papers/01-promises.md`

A call to something far away should hand the caller a placeholder for the answer straight away, so the caller keeps working and collects the answer only when it actually needs it — which is the task handle you spent today building, proposed thirty-eight years earlier and given a type.


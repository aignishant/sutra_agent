# Day 44 - Client hardening — retries, timeouts, no held connections

IDs closed: MCP-22, MCP-23 · source: `days/day-44-client-hardening/`

## Parts

### 1.1 - The button you can press twice
`days/day-44-client-hardening/parts/01-what-may-be-repeated/1.1-the-button-you-can-press-twice.md` · level `foundation` · ids MCP-22

Some actions have the same effect whether you do them once or five times, and some do not, and a retry is only ever safe for the first kind — so the first question a hardened client asks is not how many times but may I at all.

### 1.2 - A timeout is an unknown, not a failure
`days/day-44-client-hardening/parts/01-what-may-be-repeated/1.2-a-timeout-is-an-unknown.md` · level `foundation` · ids MCP-22

When a call times out, the one thing you have learned is that you did not hear back — the work may never have started, may have started and failed, or may have completed perfectly — and code that treats "timed out" as "did not happen" is guessing at one of three worlds.

### 1.3 - The line drawn through every call Sutra makes
`days/day-44-client-hardening/parts/01-what-may-be-repeated/1.3-the-line-through-every-call.md` · level `working` · ids MCP-22

The protocol tells you that tools/list and resources/read may be repeated and says nothing at all about what any particular tool does, so the repeatable list is something you write by hand, one row per tool with a reason beside it, and a tool nobody has classified is treated as a write.

### 1.4 - The key that makes a write repeatable
`days/day-44-client-hardening/parts/01-what-may-be-repeated/1.4-the-key-that-makes-a-write-repeatable.md` · level `working` · ids MCP-22

A write becomes safe to repeat when the caller mints a unique name for the intention before the first attempt and sends the same name every time, so the server can recognise the second request as the same request rather than a second one — which moves the problem from "may I retry?" to "does the far side keep that promise?".

### 2.1 - Two clocks, not one
`days/day-44-client-hardening/parts/02-the-deadline/2.1-two-clocks-not-one.md` · level `working` · ids MCP-22

"The server is not there" and "the server is there and not answering" are different facts with different fixes, they fail at different points in the call, and a client with one timeout number is serving one of them badly.

### 2.2 - 💥 The deadline that is never reached
`days/day-44-client-hardening/parts/02-the-deadline/2.2-the-deadline-never-reached.md` · level `production` · ids MCP-22

A timeout is only real if it is shorter than every timeout above it, so a client that hands each attempt a fixed number instead of the budget it has left will keep working long after the person waiting has gone, and its careful retry ladder will be dead code that nothing reports.

### 2.3 - `with_timeout`, the wrapper that guarantees a clock
`days/day-44-client-hardening/parts/02-the-deadline/2.3-with-timeout.md` · level `working` · ids MCP-22

with_timeout is the one function in sutra/mcp/hardening.py that puts a deadline on a call whether or not the thing underneath has a timeout parameter — and what it guarantees is that you stop waiting, never that the work stops.

### 2.4 - The numbers your libraries already chose
`days/day-44-client-hardening/parts/02-the-deadline/2.4-the-numbers-your-libraries-chose.md` · level `production` · ids MCP-22

mcp==1.29.1 gives a client session no read timeout at all unless you pass one, ADK's HTTP connection params quietly use sse_read_timeout — 300 seconds — as the per-call deadline rather than the timeout=5.0 you set, and ADK retries every failed tool call once whether or not the tool is idempotent, so three of the most important decisions in this day have already been made for you by code you did not write.

### 3.1 - Waiting longer each time
`days/day-44-client-hardening/parts/03-backing-off/3.1-waiting-longer-each-time.md` · level `working` · ids MCP-22

A retry that follows the failure immediately spends the whole attempt budget inside the first instant of an outage, so the wait between attempts has to grow — doubling is the standard choice because it covers a long outage in a small number of attempts without waiting long for a short one.

### 3.2 - The same wait is the wrong wait
`days/day-44-client-hardening/parts/03-backing-off/3.2-the-same-wait-is-the-wrong-wait.md` · level `working` · ids MCP-22

Every client that failed at the same instant will retry at the same instant if they all wait the same number of seconds, so the backoff ladder that was supposed to spread the load reproduces the original spike at every rung — and the fix is one call to a random number generator.

### 3.3 - The server told you when to come back
`days/day-44-client-hardening/parts/03-backing-off/3.3-the-server-said-when.md` · level `working` · ids MCP-22

A 429 with a Retry-After header is the only moment in this whole day when somebody who actually knows the answer tells you how long to wait, so your backoff ladder is a guess that must give way to it — and under Addendum 02 every model call path in Sutra must honour it and then escalate rather than fabricate.

### 3.4 - `with_retries`, and why attempts are a budget
`days/day-44-client-hardening/parts/03-backing-off/3.4-with-retries.md` · level `production` · ids MCP-22

Retries multiply down a call stack — three layers of "up to three attempts" is twenty-seven requests at the bottom and nobody chose twenty-seven — so the attempt count belongs to the whole request as a shared budget rather than to each layer as a local constant.

### 4.1 - 💥 The retry that took the server down
`days/day-44-client-hardening/parts/04-when-to-stop-asking/4.1-the-retry-that-took-it-down.md` · level `production` · ids MCP-22

Retrying a slow server adds load to the exact thing that is short of capacity, and because giving up ends the wait and not the work, the abandoned attempts stay in the queue — so a client fleet that retries can make an outage last three times longer while answering exactly the same number of people.

### 4.2 - The switch that refuses before it asks
`days/day-44-client-hardening/parts/04-when-to-stop-asking/4.2-the-switch-that-refuses-first.md` · level `production` · ids MCP-22

After enough consecutive failures a client should stop calling altogether for a while and fail immediately instead, then let exactly one request through to find out whether the far side is back — and the hard half is not opening the circuit but making sure it can close again.

### 5.1 - The chair you are holding for nobody
`days/day-44-client-hardening/parts/05-no-held-connections/5.1-the-chair-you-hold-for-nobody.md` · level `working` · ids MCP-23

Holding an MCP connection between requests used to buy you a session and now buys you nothing, so what is left is pure cost — a process or a socket per held connection, and a handle that goes on looking healthy after the thing behind it has been replaced.

### 5.2 - Keep the catalogue, not the connection
`days/day-44-client-hardening/parts/05-no-held-connections/5.2-keep-the-catalogue-not-the-connection.md` · level `working` · ids MCP-23

The reason people held connections was to avoid re-fetching the tool list, and the protocol answered that directly by putting an expiry on the list itself — so the thing worth keeping between requests is the catalogue and its ttlMs, and the socket can go.

### 5.3 - What reconnecting actually costs
`days/day-44-client-hardening/parts/05-no-held-connections/5.3-what-reconnecting-costs.md` · level `production` · ids MCP-23

Over HTTP a reconnect is a socket and is nearly free, but over stdio it is launching an operating system process, and measured on this machine that is about a second per request against a call that takes single-digit milliseconds — so the rule is not "always reconnect", it is "nothing on the connection may be load-bearing", and stdio is where the difference shows.

### 6.1 - What you say when all of it has failed
`days/day-44-client-hardening/parts/06-the-last-word/6.1-what-you-say-when-it-all-failed.md` · level `production` · ids MCP-22, MCP-23

Every retry ladder ends, and the sentence the client says at that moment is the only part of this day a human will ever read — so it has to state what was attempted, what is known and not known about the world, and who decides next, because a shrug or an invented answer has broken Principle 10 after four parts of careful work.

### 6.2 - One policy, not a hundred try/excepts
`days/day-44-client-hardening/parts/06-the-last-word/6.2-one-policy-not-a-hundred.md` · level `production` · ids MCP-22, MCP-23

A retry rule that lives in nineteen call sites is nineteen rules, so the hardening goes in one module with one entry point and the thing you actually maintain is a check that no call site bypasses it — because the policy will drift and the check will not.

## Papers - read after the parts

### doi:10.1145/2408776.2408794 - The tail at scale
`days/day-44-client-hardening/papers/01-the-tail-at-scale.md`

When one user-visible request depends on a hundred internal calls, the slowest of the hundred decides what the user experiences — so a service where 99% of calls are fast is a service where almost every page is slow, and the fix is not to make the average faster but to stop waiting for the stragglers.


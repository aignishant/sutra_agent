# Day 43 - Stateless by default — deploy-shaped servers

IDs closed: MCP-20, MCP-21 · source: `days/day-43-stateless-by-default/`

## Parts

### 1.1 - The dictionary nobody called state
`days/day-43-stateless-by-default/parts/01-accidental-state/1.1-the-dictionary-nobody-called-state.md` · level `foundation` · ids MCP-20

A dictionary written at the top of a module is one dictionary per running process, so the moment a second copy of your server exists, half your callers are talking to an empty one — and nobody ever wrote a line of code that said "remember this".

### 1.2 - The cache that becomes a second opinion
`days/day-43-stateless-by-default/parts/01-accidental-state/1.2-the-cache-that-becomes-a-second-opinion.md` · level `foundation` · ids MCP-20

A cache is a copy of an answer, so two instances holding two caches hold two answers, and the one a caller receives depends on which machine picked up the request — which is a coin flip nobody put in the design.

### 1.3 - The state that is not a dictionary
`days/day-43-stateless-by-default/parts/01-accidental-state/1.3-the-state-that-is-not-a-dictionary.md` · level `working` · ids MCP-20

Most of the state in a real server is not a container at all — it is an open connection, a file handle, a lock, a context variable or a seeded generator — and every one of those belongs to exactly one process, which is why looking only for dictionaries finds about half the problem.

### 1.4 - The session your SDK keeps for you
`days/day-43-stateless-by-default/parts/01-accidental-state/1.4-the-session-your-sdk-keeps-for-you.md` · level `working` · ids MCP-20

The largest module-level dictionary in sutra-mcp is not one you wrote: the installed SDK keeps a dict of live sessions inside each server process, and a single constructor argument — stateless_http=True — is what decides whether your deployment depends on it.

### 2.1 - Reading the code without running it
`days/day-43-stateless-by-default/parts/02-finding-the-state/2.1-reading-the-code-without-running-it.md` · level `foundation` · ids MCP-20

To find state that only exists once the module is imported you must not import the module — you parse it into a tree and look at what its top level would do, which costs nothing, cannot start a server, and works on code you have never installed.

### 2.2 - The four shapes worth flagging
`days/day-43-stateless-by-default/parts/02-finding-the-state/2.2-the-four-shapes-worth-flagging.md` · level `working` · ids MCP-20

Four patterns catch almost all accidental per-instance state — a mutable literal, a call that returns something stateful, a cache decorator, and a function that writes a module global — and everything immutable is deliberately left alone, because a rule that fires on constants gets switched off.

### 2.3 - The waiver that has a reason on it
`days/day-43-stateless-by-default/parts/02-finding-the-state/2.3-the-waiver-that-has-a-reason-on-it.md` · level `working` · ids MCP-20

Every useful check produces some findings that are correct code, and the only two honest responses are to fix the shape or to waive it with a written reason — because the third response, a silent switch-off, is how a check that was working stops working and nobody notices.

### 2.4 - A scan that can go red
`days/day-43-stateless-by-default/parts/02-finding-the-state/2.4-a-scan-that-can-go-red.md` · level `production` · ids MCP-20

A finder becomes a check when it exits non-zero, and it becomes trustworthy when you have watched it go red on purpose — including the case that matters most here, where it is green because there is nothing to look at.

### 3.1 - The dispatcher that knows nothing
`days/day-43-stateless-by-default/parts/03-two-instances/3.1-the-dispatcher-that-knows-nothing.md` · level `working` · ids MCP-21

The test for statelessness is a load balancer built to be as stupid as possible — no table of callers, no memory between requests, strict alternation — because a claim that any instance can answer any request is only tested by something that refuses to be clever about which one it picks.

### 3.2 - The same question, twice, one URL
`days/day-43-stateless-by-default/parts/03-two-instances/3.2-the-same-question-twice-one-url.md` · level `working` · ids MCP-21

The probe sends the ordinary request sequence to one address and prints which instance answered each one, so "stateless" stops being a property you argue about and becomes four lines of output with a count at the bottom and an exit code.

### 3.3 - 💥 Two answers to one question
`days/day-43-stateless-by-default/parts/03-two-instances/3.3-two-answers-to-one-question.md` · level `production` · ids MCP-21

Two instances with two caches give a model two contradictory facts inside one turn, and because both tool calls succeeded, nothing in the system records that anything went wrong — the only trace is a sentence in an answer that is quietly untrue.

### 3.4 - 💥 Three a day, per instance
`days/day-43-stateless-by-default/parts/03-two-instances/3.4-three-a-day-per-instance.md` · level `production` · ids MCP-21

A limit enforced by a counter inside each process is not one limit — it is one limit per instance, so a service allowed three requests a day allows three times the number of containers, and the number of containers is chosen by an autoscaler rather than by you.

### 3.5 - 💥 The handle B had never heard of
`days/day-43-stateless-by-default/parts/03-two-instances/3.5-the-handle-b-had-never-heard-of.md` · level `production` · ids MCP-21

Doing the handle pattern correctly is not enough: an opaque identifier travelling in the payload is still useless if the thing it points at lives in one process's memory, and the same failure arrives twice in this rig — once from your code and once from the SDK, with a real 404 Session not found.

### 4.1 - Down, out, or nowhere
`days/day-43-stateless-by-default/parts/04-where-state-goes/4.1-down-out-or-nowhere.md` · level `working` · ids MCP-21

State never disappears when a server becomes stateless; it moves, and there are exactly three places it can move to — down into a shared store, out into the caller's payload, or nowhere because it turned out not to be needed — and picking the wrong one is what section 3 was measuring.

### 4.2 - Shared is not the same as safe
`days/day-43-stateless-by-default/parts/04-where-state-goes/4.2-shared-is-not-the-same-as-safe.md` · level `production` · ids MCP-21

Moving state into a store both instances can reach fixes reachability and not correctness: two instances reading a number, adding to it and writing it back will lose most of the additions, and the fix is one line that takes the lock before the read rather than after the decision.

### 5.1 - An object, not a program
`days/day-43-stateless-by-default/parts/05-deploy-shape/5.1-an-object-not-a-program.md` · level `working` · ids MCP-20

sutra_mcp/app.py exports one name, an ASGI application object, and starts nothing — because a platform runs your code by importing it and calling it, not by running your main, and the whole deploy shape follows from that one inversion.

### 5.2 - 🅿️ The platform you are not paying for
`days/day-43-stateless-by-default/parts/05-deploy-shape/5.2-the-platform-you-are-not-paying-for.md` · level `production` · ids MCP-20

Sutra never deploys to a managed container platform, because every one of them needs a billing account — but the contract those platforms impose is public, short, and exactly the set of rules this whole day has been deriving, so you can satisfy it, state it and defend it without spending anything.

### 6.1 - 💥 The health check that says yes
`days/day-43-stateless-by-default/parts/06-in-production/6.1-the-health-check-that-says-yes.md` · level `production` · ids MCP-20, MCP-21

A health endpoint that returns {"status": "ok"} from inside the process is answering "am I running?", and every failure in this day happens on a process that is running — so a green health check is not evidence of anything the day was about.

### 6.2 - Sticky sessions, the anaesthetic
`days/day-43-stateless-by-default/parts/06-in-production/6.2-sticky-sessions-the-anaesthetic.md` · level `production` · ids MCP-20, MCP-21

Pinning each caller to one instance makes every failure in this day disappear immediately, which is exactly why it is dangerous: it removes the symptom, leaves the state in the wrong place, and hands the bill to whoever is on call during the next deploy.


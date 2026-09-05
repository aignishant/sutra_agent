# Day 38 - Failure and migration lab

IDs closed: MCP-11, MCP-12, MCP-31 · source: `days/day-38-failure-and-migration-lab/`

## Parts

### 1.1 - The only clock in the room is yours
`days/day-38-failure-and-migration-lab/parts/01-the-clock/1.1-the-only-clock-is-yours.md` · level `foundation` · ids MCP-11

Nothing in MCP promises that a server will ever answer, so a client that has no deadline of its own has no way to stop waiting, and "the request is still running" and "the request will never finish" look exactly the same from the outside.

### 1.2 - Giving up ends the wait, not the work
`days/day-38-failure-and-migration-lab/parts/01-the-clock/1.2-giving-up-ends-the-wait.md` · level `working` · ids MCP-11

A timeout is a decision the caller takes on its own side of the wire, so the server is never told, never notices, and finishes the work anyway — which means every side effect that call was going to have still happens, after you stopped listening.

### 1.3 - Hanging up is the whole cancel message
`days/day-38-failure-and-migration-lab/parts/01-the-clock/1.3-hanging-up-is-the-message.md` · level `working` · ids MCP-11

Over Streamable HTTP there is no cancel message: closing the response stream is the cancellation, which means the server only learns about it the next time it tries to write, and may have done several more pieces of work by then.

### 1.4 - A broken stream loses the request
`days/day-38-failure-and-migration-lab/parts/01-the-clock/1.4-a-broken-stream-loses-the-request.md` · level `working` · ids MCP-11

The 2026-07-28 revision deleted stream resumption, so a response stream that breaks loses the request entirely and the client must re-issue it — with a new request id, because reusing the old one lets a late reply to the first attempt be accepted as the answer to the second.

### 2.1 - Five questions before you believe a byte
`days/day-38-failure-and-migration-lab/parts/02-the-x-ray/2.1-five-questions-before-you-believe.md` · level `working` · ids MCP-12

A client must validate the envelope of every reply — is it JSON, is it JSON-RPC, is the id mine, is there exactly one of result and error, does the payload match what the method promised — before any field of it reaches the rest of the program, because the alternative is that a stranger's bug raises an exception in the middle of your business logic.

### 2.2 - Malformed is not transient
`days/day-38-failure-and-migration-lab/parts/02-the-x-ray/2.2-malformed-is-not-transient.md` · level `working` · ids MCP-12

Retrying is medicine for a failure that would give a different answer next time, and a malformed reply will give the same answer every time — so a retry loop around a malformed reply spends every request it has, learns nothing, and adds load to a server that is already misbehaving.

### 2.3 - The error you threw away
`days/day-38-failure-and-migration-lab/parts/02-the-x-ray/2.3-the-error-you-threw-away.md` · level `working` · ids MCP-12

A JSON-RPC error is a reply, not the absence of one: it carries a numbered code and a data block that usually contain the instructions for fixing the call, and a client that treats every error as "the server is unwell, retry" throws away the only structured diagnosis it will ever be given.

### 2.4 - The reply that arrived twice
`days/day-38-failure-and-migration-lab/parts/02-the-x-ray/2.4-the-reply-that-arrived-twice.md` · level `working` · ids MCP-12

A server that writes each reply twice produces nothing but valid messages, and a client that reads one line per request is permanently one answer behind from the second request onwards — with no exception, no warning and no way to notice except the id check.

### 3.1 - 💥 The answer about the wrong ticket
`days/day-38-failure-and-migration-lab/parts/03-the-quiet-ones/3.1-the-answer-about-the-wrong-ticket.md` · level `production` · ids MCP-12

A reply can pass every envelope check — valid JSON, valid JSON-RPC, your id, exactly one result, the right payload shape — and still be an answer to a different question, and there is no check in the protocol that catches it because from the protocol's point of view nothing is wrong.

### 3.2 - 💥 The ticket closed twice
`days/day-38-failure-and-migration-lab/parts/03-the-quiet-ones/3.2-the-ticket-closed-twice.md` · level `production` · ids MCP-11

Because a timeout does not stop the work and a re-issue is a brand-new request, a tool that writes will be run twice by any client that retries — so the only place the problem can be solved is the server, by giving the request a key it remembers.

### 4.1 - A feature with a leaving date
`days/day-38-failure-and-migration-lab/parts/04-the-leaving-list/4.1-a-feature-with-a-leaving-date.md` · level `foundation` · ids MCP-31

Since the 2026-07-28 revision, an MCP feature does not simply disappear one day: it enters a Deprecated state with a published migration path and a minimum twelve-month window before it is even eligible for removal, and every such feature is listed on one page you can read.

### 4.2 - Three things being taken away
`days/day-38-failure-and-migration-lab/parts/04-the-leaving-list/4.2-three-things-being-taken-away.md` · level `working` · ids MCP-31

Roots, Sampling and Logging are the three features SEP-2577 put on the leaving list, and they share one cause — each of them was the server reaching back into the client's world across a held connection — so each migration moves the work out of the protocol rather than to a newer method.

### 4.3 - Dating somebody else's server
`days/day-38-failure-and-migration-lab/parts/04-the-leaving-list/4.3-dating-somebody-elses-server.md` · level `working` · ids MCP-31

A server tells you its age without being asked: the capabilities and methods it advertises map one-to-one onto rows of the deprecated registry, so a scan over one server/discover reply produces a dated list of what that server is still running and what it must eventually move to.

### 5.1 - The question that comes back as an answer
`days/day-38-failure-and-migration-lab/parts/05-the-replacement/5.1-the-question-that-comes-back-as-an-answer.md` · level `working` · ids MCP-31

Server-initiated requests were replaced by a single pattern: the server answers with resultType: "input_required", hands back the question and an opaque requestState blob, and the client gathers the answer and re-issues the original request with a new id — so nothing is held open and any instance can finish what another one started.

### 5.2 - 💥 The slip somebody rewrote
`days/day-38-failure-and-migration-lab/parts/05-the-replacement/5.2-the-slip-somebody-rewrote.md` · level `production` · ids MCP-31

requestState travels through the client, so the client can edit it — and a server that decodes what comes back without verifying it has handed an attacker a pen and its own memory to write in.

### 5.3 - What the migration actually costs
`days/day-38-failure-and-migration-lab/parts/05-the-replacement/5.3-what-the-migration-costs.md` · level `production` · ids MCP-31

A migration path that reads "integrate directly with LLM provider APIs" is one sentence in a registry and a list of things you now own — an account, a key, a budget, a rate-limit strategy, a failure path and a bill — which is why a deprecation is a planning item and not a rename.

### 6.1 - 💥 Two ways a removal meets you
`days/day-38-failure-and-migration-lab/parts/06-in-production/6.1-two-ways-a-removal-meets-you.md` · level `production` · ids MCP-31

The same removal can raise the same exception class and cost you either a minute or a day, depending entirely on whether whoever removed it left a message in the error — and mcp 2.1.1 contains one example of each, which you can run today without touching the pin.

### 6.2 - 💥 The deprecation your library never mentions
`days/day-38-failure-and-migration-lab/parts/06-in-production/6.2-the-deprecation-your-library-never-mentions.md` · level `production` · ids MCP-31

A specification deprecation is invisible in your editor and silent at runtime: mcp 1.29.1 exports Roots, Sampling and Logging with no marker of any kind, mcp 2.1.1 mentions two of the three in a docstring and warns about none of them — so the only way to know a feature is on its way out is to read the registry, not to ask the library.

### 6.3 - The bill for a bump nobody has authorised
`days/day-38-failure-and-migration-lab/parts/06-in-production/6.3-the-bill-for-a-bump.md` · level `production` · ids MCP-31

mcp is pinned at 1.29.1 and speaks protocol 2025-11-25; the release is 2.1.1 and speaks 2026-07-28; and the difference is not a number in pyproject.toml but a named, countable list of imports across this repository — which is why Principle 14 says you price it and amend the plan before you change the pin.

### 6.4 - The test that must be able to go red
`days/day-38-failure-and-migration-lab/parts/06-in-production/6.4-the-test-that-must-go-red.md` · level `production` · ids MCP-11, MCP-12

Everything in this day is a rehearsal until it is a test: tests/test_mcp_failures.py drives Sutra's client against a server that hangs and a server that lies, and it is only worth having if you have watched it fail before you watched it pass.

## Papers - read after the parts

### doi:10.17487/RFC9413 - Maintaining Robust Protocols
`days/day-38-failure-and-migration-lab/papers/01-maintaining-robust-protocols.md`

The old advice to "be liberal in what you accept" was misread as a licence to tolerate broken peers, and tolerating them is how a protocol loses the ability to change: this document argues that long-term interoperability comes from active maintenance — exercising extension points, rejecting the malformed, and deprecating deliberately — rather than from politeness.


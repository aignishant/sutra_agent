---
day: 38
phase: 5
phase_name: "MCP I: the protocol"
title: "Failure and migration lab"
ids: ["MCP-11", "MCP-12", "MCP-31"]
principles: [2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 20
generated: "2026-09-04"
status: written
lab_scaffolded: true
commit: ""
---

# Day 38 — Failure and migration lab

> **Yesterday (Day 37):** auth and enterprise. `sutra_mcp` grew a badge check — OAuth 2.0 with issuer
> validation, client metadata documents — and learned to ask the user a question mid-tool under
> central policy.
> **Today:** the last day of Phase 5, and the day everything built since Day 32 gets broken on
> purpose. Servers that never answer, servers that answer twice, servers that answer beautifully about
> the wrong ticket — and then the other half: three protocol features on a published leaving list, the
> pattern that replaced them, and what a version bump would actually cost this repository.
> **Tomorrow (Day 39):** Phase 6 opens with production. A real SQLite database behind the tools, and
> the choice between a database toolbox and hand-written SQL.

---

## §1 Where we are

Six days of Phase 5, and every one of them worked.

Day 32 read the protocol off the page. Day 33 connected a client over two transports. Day 34 put
tools on the wire, Day 35 added resources and prompts, Day 36 handled long jobs, Day 37 added a badge
and a question. Every part ran. Every check went green.

Which means nobody has yet met a server that is having a bad day, and Phase 6 is nothing but servers
you did not write. So today is the day the desk stops being polite.

Three things to know before you start.

**Every failure in this day is real and small.** There are eighteen scripts in `lab/`, and between
them they build a server that never answers, a server that answers with an HTML error page, a server
that answers a request nobody sent, a server that writes every reply twice, and a server that answers
perfectly about a different ticket. None of them needs a network, a framework or a model. The point of
building each one by hand is Principle 4: [Day 44](../day-44-client-hardening/LESSON.md) writes
`with_timeout` and `with_retries` into `sutra/mcp/hardening.py`, and that day is only worth writing if
you have already felt the hang.

**Two of the failures are silent, and those are the ones to fear.** A client that gives up and reports
"failed" while the server finishes the work anyway. A reply that passes all five envelope checks and
is about somebody else's ticket. Neither raises anything, neither logs anything, and both produce a
fluent sentence for a user to act on. Section 3 exists because those are worse than a traceback and
harder to find.

**The second half of the day is a calendar rather than a bug.** Roots, Sampling and Logging are on a
published deprecation lifecycle with a registry, migration paths, and a floor of twelve months before
they are even *eligible* for removal — `327 days` from the day this was written. Sutra uses none of
them, so this is a recognition skill, not a repair job: how to date somebody else's server from what
it advertises, what the replacement pattern looks like, and what a migration actually costs when the
registry's answer is one sentence long.

**And the day ends with a bill nobody has to pay today.** This repository pins `mcp==1.29.1`, which
speaks protocol revision `2025-11-25`. The published release is `2.1.1` and speaks `2026-07-28`. Day
32 found that gap and changed nothing. Today you measure exactly what the bump would break — by running
the same probe under both SDKs in a throwaway environment, so that `pyproject.toml` and `uv.lock` are
untouched when you finish. That is Principle 14: price it, amend the plan, *then* code.

---

## §2 The map

Twenty parts in six sections, plus **one paper**, read last. The day climbs
`foundation → working → production`: sections 1 and 2 are the two failure surfaces the plan names,
section 3 is where they go quiet, sections 4 and 5 are the migration half, and section 6 is what all
of it looks like in a real system.

### Section 1 — `01-the-clock`: no answer is an answer you must budget for (MCP-11)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The only clock in the room is yours](parts/01-the-clock/1.1-the-only-clock-is-yours.md) | `6.05s` against `2.01s`, from the same server | `foundation` |
| 1.2 | [Giving up ends the wait, not the work](parts/01-the-clock/1.2-giving-up-ends-the-wait.md) | The server finished at `6.06s`; nobody told it | `working` |
| 1.3 | [Hanging up is the whole cancel message](parts/01-the-clock/1.3-hanging-up-is-the-message.md) | Cancellation is discovered, late, on a write | `working` |
| 1.4 | [A broken stream loses the request](parts/01-the-clock/1.4-a-broken-stream-loses-the-request.md) | Re-issue with a new id, or believe a stale answer | `working` |

### Section 2 — `02-the-x-ray`: parse or perish at the boundary (MCP-12)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Five questions before you believe a byte](parts/02-the-x-ray/2.1-five-questions-before-you-believe.md) | Five crimes named, against one traceback | `working` |
| 2.2 | [Malformed is not transient](parts/02-the-x-ray/2.2-malformed-is-not-transient.md) | Thirty requests that bought nothing | `working` |
| 2.3 | [The error you threw away](parts/02-the-x-ray/2.3-the-error-you-threw-away.md) | Five codes, and only one of them is a retry | `working` |
| 2.4 | [The reply that arrived twice](parts/02-the-x-ray/2.4-the-reply-that-arrived-twice.md) | Every answer one behind, forever, exit code zero | `working` |

### Section 3 — `03-the-quiet-ones`: the failures that look green (MCP-11 · MCP-12)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [💥 The answer about the wrong ticket](parts/03-the-quiet-ones/3.1-the-answer-about-the-wrong-ticket.md) | All five checks passed, and the answer is false | `production` |
| 3.2 | [💥 The ticket closed twice](parts/03-the-quiet-ones/3.2-the-ticket-closed-twice.md) | One intention, two customer emails | `production` |

### Section 4 — `04-the-leaving-list`: reading the deprecation registry (MCP-31)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [A feature with a leaving date](parts/04-the-leaving-list/4.1-a-feature-with-a-leaving-date.md) | Active, Deprecated, Removed — and `327 days` | `foundation` |
| 4.2 | [Three things being taken away](parts/04-the-leaving-list/4.2-three-things-being-taken-away.md) | One cause, three consequences, no new method | `working` |
| 4.3 | [Dating somebody else's server](parts/04-the-leaving-list/4.3-dating-somebody-elses-server.md) | Three findings and an exit code, from one reply | `working` |

### Section 5 — `05-the-replacement`: what replaced server-initiated requests (MCP-31)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The question that comes back as an answer](parts/05-the-replacement/5.1-the-question-that-comes-back-as-an-answer.md) | `input_required`, and a retry that lands elsewhere | `working` |
| 5.2 | [💥 The slip somebody rewrote](parts/05-the-replacement/5.2-the-slip-somebody-rewrote.md) | Four lines turn 4 tickets into 400 | `production` |
| 5.3 | [What the migration actually costs](parts/05-the-replacement/5.3-what-the-migration-costs.md) | One sentence, six ongoing obligations | `production` |

### Section 6 — `06-in-production`: after it ships

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 Two ways a removal meets you](parts/06-in-production/6.1-two-ways-a-removal-meets-you.md) | Same exception, one minute or one day | `production` |
| 6.2 | [💥 The deprecation your library never mentions](parts/06-in-production/6.2-the-deprecation-your-library-never-mentions.md) | Nine cells, and not one warning | `production` |
| 6.3 | [The bill for a bump nobody has authorised](parts/06-in-production/6.3-the-bill-for-a-bump.md) | Four changes, measured without moving the pin | `production` |
| 6.4 | [The test that must be able to go red](parts/06-in-production/6.4-the-test-that-must-go-red.md) | `tests/test_mcp_failures.py`, and why some stay red | `production` |

### The paper — read it **after** the parts

| Paper | Identifier | What it argued |
| --- | --- | --- |
| [Maintaining Robust Protocols](papers/01-maintaining-robust-protocols.md) | `doi:10.17487/RFC9413` (2023) | Tolerating a broken peer is how a protocol loses the ability to change; long-term interoperability comes from active maintenance |

Principle 4 at the scale of a day. You will have spent section 2 arguing for strictness on purely
defensive grounds and section 4 reading a deprecation policy that looks like bureaucracy. The paper is
where those turn out to be the same argument, and its demo puts a number on it: the tolerant server
scores `3/3` on the day it ships and the strict one scores `1/3`, and a year later those numbers
reverse and one of them is silently wrong.

---

## §3 Setup — run this

**No package is added today, and no package is upgraded.** `git diff pyproject.toml uv.lock` must be
empty when you finish, and that is a checklist item rather than a suggestion — section 6 runs against
`mcp==2.1.1` and does it in a throwaway environment on purpose.

```bash
# 1 - the day's lab
cd days/day-38-failure-and-migration-lab
mkdir -p lab/papers/maintaining-robust-protocols

# 2 - section 1: the clock
touch lab/slow_server.py lab/deadline.py lab/oblivious.py lab/cancel.py lab/reissue.py

# 3 - section 2: the boundary
touch lab/crooked_server.py lab/xray.py lab/classify.py lab/errors.py
touch lab/echo_twice.py lab/twice.py

# 4 - section 3: the quiet ones
touch lab/plausible.py lab/double_close.py

# 5 - sections 4 and 5: the leaving list and its replacement
touch lab/lifecycle.py lab/deprecation_scan.py lab/partner_server.json
touch lab/mrtr.py lab/tamper.py

# 6 - section 6: the bump, measured
touch lab/bump_probe.py

# 7 - the paper demo
touch lab/papers/maintaining-robust-protocols/peer.py
touch lab/papers/maintaining-robust-protocols/run.py
cd -

# 8 - the gate, before anything else: has the specification moved?
curl -s https://modelcontextprotocol.io/specification/versioning | grep -o "2026-07-28" | head -1
```

**Step 8 is the gate and it is the same one Day 32 ran.** This day, the addendum it implements and
every remaining day of Phases 5 and 6 are written against revision **2026-07-28**. If that page names
a newer current revision, stop and amend the plan before writing code (Principle 14). It printed
`2026-07-28` on 2026-09-04.

**One project file is yours to write today, and it is a test.** `tests/test_mcp_failures.py` — the
brief is in [6.4](parts/06-in-production/6.4-the-test-that-must-go-red.md) and the bodies are
`TODO(me)`. Nothing else under `sutra/`, `sutra_mcp/` or `tests/` changes.

**Read the sections in order.** Section 3 depends on sections 1 and 2 having happened; section 5's
replacement is not meaningful until section 4 has said what it replaced; and the paper is worth
reading only once you have measured the thing it argues about.

---

## §4 Build brief

Eighteen lab scripts and one JSON fixture, none of which touch a model. Each belongs to the part that
teaches it.

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/slow_server.py` | a stdio server that is fast, slow or silent on command | 1.1, 1.2 |
| `lab/deadline.py` | the same call with and without a clock of its own | 1.1 |
| `lab/oblivious.py` | timestamps proving the server finished after the client left | 1.2 |
| `lab/cancel.py` | a real socket, hung up mid-stream, and when the server notices | 1.3 |
| `lab/reissue.py` | a stale reply matched on a reused request id | 1.4 |
| `lab/crooked_server.py` | five specific crimes, in rotation | 2.1 |
| `lab/xray.py` | the five boundary checks, against the one-line version | 2.1 |
| `lab/classify.py` | what a retry ladder buys, per failure class | 2.2 |
| `lab/errors.py` | five JSON-RPC error codes, read or discarded | 2.3 |
| `lab/echo_twice.py` | a server whose only fault is writing each reply twice | 2.4 |
| `lab/twice.py` | the desynchronised client, with and without the id check | 2.4 |
| `lab/plausible.py` | a perfect reply about the wrong ticket | 3.1 |
| `lab/double_close.py` | one intention, two audit rows, and the key that fixes it | 3.2 |
| `lab/lifecycle.py` | the deprecated-features registry as a schedule | 4.1 |
| `lab/partner_server.json` | one saved `server/discover` reply from a partner | 4.3 |
| `lab/deprecation_scan.py` | fingerprints against the registry, with an exit code | 4.3 |
| `lab/mrtr.py` | `input_required` against a worker that held the question | 5.1 |
| `lab/tamper.py` | `requestState` edited by the client, signed and unsigned | 5.2 |
| `lab/bump_probe.py` | one SDK's surface, run under two SDKs | 6.2, 6.3 |

`lab/papers/maintaining-robust-protocols/` holds the paper demo — `peer.py` and `run.py` — and it is
**given complete** in the paper part. It is teaching material, not a rep: type it, run both arms, and
compare your output with the transcript.

**The one project file: `tests/test_mcp_failures.py`.** The shape is in
[6.4](parts/06-in-production/6.4-the-test-that-must-go-red.md): two fixtures (`hanging_server`,
`crooked_server`), a deadline test, a parametrised crime test, and an echo-check test that needs no
server. Every body is `raise NotImplementedError("TODO(me)")` and every one is yours.

**`TODO(me)` markers left for you:**

- **1.1** — decide Sutra's two deadlines, connect and total, and say where they are configured rather
  than hard-coded. Then say what the total deadline should be for `lookup_ticket` and for a
  hypothetical `reindex_archive`, and why they are not the same number.
- **1.2** — add the third outcome. Sutra's client currently has success and failure; write down what
  `unknown` means, who is told, and what happens next.
- **1.4** — decide where request ids come from in `sutra/mcp/client.py`, and write the assertion that
  proves two attempts at one operation never share one.
- **2.1** — extend `validate` with check 5 for one more method than `tools/list`. Pick the method
  Sutra actually calls next, and say what its result promises.
- **2.2** — write Sutra's failure-to-disposition table as data, with `quarantine` as the default for
  anything unrecognised, and decide which module owns it.
- **2.3** — decide what Sutra does with `-32022` specifically: which version it re-issues with, how
  many times, and where the answer is remembered so it does not re-learn it on every call.
- **2.4** — replace the single `if` in `twice.py` with a bounded loop, and decide the bound and the
  exception it raises when the bound is reached.
- **3.1** — for each tool Sutra exposes, name the field that identifies the subject of the answer. If
  a tool has none, write down what you would ask its author for.
- **3.2** — decide Sutra's idempotency key: who mints it, what it is made of, where the honoured keys
  are stored once there is more than one worker, and how long they are kept.
- **4.1** — decide where the dated snapshot of the deprecated registry lives in this repository, and
  which day's check re-fetches it.
- **4.3** — extend `deprecation_scan.py` to distinguish "found problems" from "could not run" with
  different exit codes, and decide which one a review gate should treat as a failure.
- **5.1** — write the `resultType` branch for `sutra/mcp/client.py`, including the rule that a missing
  field from an older server means `complete`.
- **5.2** — decide what goes inside Sutra's signed `requestState` beyond the business fields, and
  where `SERVER_KEY` comes from. Then decide the rotation story.
- **6.3** — read the migration guide named in the `fastmcp` error message and extend `bump_probe.py`'s
  `SYMBOLS` with every renamed symbol it lists. Then re-run both arms and say whether the bill grew.
- **6.4** — decide whether the fake servers stay in `lab/` or move to `tests/fixtures/`, and write down
  the cost of the option you did not choose.

---

## §5 The eval that must be able to fail

Every check below runs on **zero model calls**, and every one has an arm that is deliberately wrong.

**The day's gate is the deprecation scan**, because it is the only one with an exit code:

```bash
cd days/day-38-failure-and-migration-lab/lab
uv run python deprecation_scan.py partner_server.json; echo "exit: $?"
```

Measured on 2026-09-04: `deprecated features declared: 3` and `exit: 1`. That is **red on purpose** —
the partner server declares Roots, Sampling and Logging. Remove the `capabilities.client` block from
`partner_server.json` and it falls to two findings; remove `logging/setLevel` and
`sampling/createMessage` from `methods` as well and it goes to `exit: 0`.

**The paper demo is the ablation, and both arms must be run:**

```bash
cd days/day-38-failure-and-migration-lab/lab/papers/maintaining-robust-protocols
STRICT=0 uv run python run.py
STRICT=1 uv run python run.py
cd -
```

`peers with the right answer: 3/3` then `2/3` against `1/3` then `3/3`, from the same three peers and
the same protocol. The verdict line flips from *rolled back* to *still moves*.

**The nine failure ablations**, each of which is a pair. Run both halves of each:

```bash
cd days/day-38-failure-and-migration-lab/lab
DEADLINE=0 uv run python deadline.py slow   && DEADLINE=2.0 uv run python deadline.py slow
HARDENED=0 uv run python xray.py            ; HARDENED=1 uv run python xray.py
SWALLOW=1 uv run python errors.py           && SWALLOW=0 uv run python errors.py
CHECK_ID=0 uv run python twice.py           && CHECK_ID=1 uv run python twice.py
ECHO_CHECK=0 uv run python plausible.py     && ECHO_CHECK=1 uv run python plausible.py
IDEMPOTENT=0 uv run python double_close.py  && IDEMPOTENT=1 uv run python double_close.py
REUSE_ID=1 uv run python reissue.py         && REUSE_ID=0 uv run python reissue.py
MRTR=0 uv run python mrtr.py                && MRTR=1 uv run python mrtr.py
SIGNED=0 uv run python tamper.py            && SIGNED=1 uv run python tamper.py
```

`HARDENED=0` is separated by `;` rather than `&&` because it is the one arm that ends in an uncaught
`JSONDecodeError` and exits non-zero. That is the point of it.

**And the three that measure rather than compare:**

```bash
uv run python oblivious.py
uv run python cancel.py
uv run python classify.py
uv run python lifecycle.py
uv run python bump_probe.py
uv run --isolated --no-project --with "mcp==2.1.1" python bump_probe.py
```

**The test file is the eval that stays red.** `tests/test_mcp_failures.py` starts as five
`NotImplementedError`s. Some go green as you write them; the ones that stay red are the specification
for [Day 44](../day-44-client-hardening/LESSON.md), and you write them down.

```bash
cd "$(git rev-parse --show-toplevel)"
uv run python -m pytest tests/test_mcp_failures.py -q
git diff --stat pyproject.toml uv.lock
```

The last command must print nothing.

---

## §6 Request budget

**Free-tier Gemini**, roughly 20 generate requests per day per model (`gemini-3.7-flash`, roster
re-verified 2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all eighteen lab scripts, both arms each | **0** |
| the paper demo, both arms | **0** |
| `bump_probe.py` under both SDKs | **0** |
| `tests/test_mcp_failures.py` | **0** |
| **Total planned** | **0 of 20** |

**Zero, and this is the day where that is not a coincidence.** Every failure taught here is a protocol
failure, and a protocol is deterministic: a hang is measured with a clock, a malformed reply is
measured with a parser, a deprecation is measured against a published registry. A model in any of
these would add variance to an experiment whose whole value is that it produces the same numbers twice.

The only network traffic is one HTTPS GET to the specification site in §3, and `uv` fetching
`mcp==2.1.1` into a throwaway environment in section 6. Neither needs a key.

**Cost: $0.**

---

## §7 Traps

- **A read with no deadline cannot distinguish "slow" from "never".** Both are the absence of bytes,
  and waiting forever is the default behaviour of every pipe and socket on the machine (1.1).
- **A socket `timeout=` is a per-read deadline, not a per-request one.** A server sending one byte at a
  time never trips it. You need a second, outer deadline on the whole call (1.1).
- **A timeout is not a cancellation.** The server finishes, and every side effect happens, after you
  stopped listening. `TimeoutError` means **unknown**, not **failed** (1.2).
- **Over HTTP, closing the stream is the whole cancel message, and it is discovered late.** The server
  wrote one more chunk successfully after the client had gone. It is also cooperative: the server may
  catch the error and finish anyway (1.3).
- **Catch `ConnectionError`, not `BrokenPipeError`.** Windows raises `ConnectionAbortedError` for the
  same event, so catching one name means cancellation silently does not work on half your machines
  (1.3).
- **There is no stream resumption in this revision.** A broken stream loses the request; you re-issue
  with a **new** request id, and reusing the old one lets a stale reply be accepted as the new answer
  (1.4).
- **`json.loads(raw)["result"]["tools"]` is the line this day argues with.** One HTML error page from a
  proxy and it raises three frames inside your triage loop (2.1).
- **The id check is the one people leave out**, and it is the only one that catches a well-formed
  message that is not yours. A schema cannot do it, because a schema does not know what you sent (2.1,
  2.4).
- **Retrying a malformed reply is a self-inflicted flood.** Deterministic failures give the same answer
  every time; the ladder costs thirty requests, waits nearly forty seconds each, and a bare `except`
  also destroys the diagnosis (2.2).
- **The default disposition for an unrecognised failure is quarantine, not retry.** The failures you
  have not thought about are more likely to be bugs than weather (2.2).
- **Branch on `error.code`, never on `error.message`.** The text is explicitly not stable, and the codes
  were renumbered in this revision — `HeaderMismatch` `-32001` → `-32020`,
  `MissingRequiredClientCapability` `-32003` → `-32021`, `UnsupportedProtocolVersion` `-32004` →
  `-32022`, resource-not-found `-32002` → `-32602`. An older document is right about the concepts and
  wrong about every number (2.3).
- **`error.data` is optional.** `-32603` has none, and reading `error["data"]["supported"]`
  unconditionally raises `KeyError` on the one error that really is retryable (2.3).
- **One reply line per request is an assumption, not a rule.** A server that writes twice leaves your
  client permanently one answer behind, with no exception and exit code zero (2.4).
- **Every envelope check can pass on an answer about the wrong subject.** Echo the request's
  identifying key from `structuredContent` — not from `content`, which often does not contain it at
  all (3.1).
- **The idempotency key cannot be the JSON-RPC request id**, because the id must *change* on a
  re-issue. Two identifiers, two jobs (3.2).
- **Deprecated does not mean warned about.** All three SEP-2577 features are exported unmarked by the
  pinned SDK and none of them warns at runtime, on either SDK version. "No deprecation warnings" is not
  evidence (6.2).
- **"Eligible for removal" is a floor, not a deadline.** The registry says *"first revision released on
  or after"* a date, and features may stay Deprecated far longer (4.1).
- **A server declaring no client capabilities is not necessarily modern**, it may just be quiet. Absence
  of a fingerprint is not evidence; probe the method and read the `-32601` (4.3).
- **`requestState` is opaque, not protected.** Base64 is an encoding. Four lines turn a count of 4 into
  400 unless the server signed it — and use `hmac.compare_digest`, not `==` (5.2).
- **Sign the bytes you send, not the object.** Two JSON serialisers disagree about key order and
  whitespace, so signing the object makes correct traffic fail intermittently (5.2).
- **A migration path's length is not its size.** *"Integrate directly with LLM provider APIs"* is an
  account, a key, a budget, a 429 path, a model choice and a permanent job (5.3).
- **Do not bump the pin to find out what the bump breaks.** `uv run --isolated --no-project --with` gives
  you the answer with an empty `git diff` (6.1, 6.3).

---

## §8 Verify before you code

Fetched or run on **2026-09-04**, the day this was written.

**The specification — the freshness gate (Principle 14):**

- `https://modelcontextprotocol.io/specification/versioning` — *"The **current** protocol version is
  **2026-07-28**."* **It has not moved** since Day 32 checked it. The same page now also describes the
  feature-state vocabulary and links the registry, which is where §4 of this day starts.
- `https://modelcontextprotocol.io/community/feature-lifecycle` — the SEP-2596 policy: the three
  states, the *"minimum deprecation window: the number of months, at least twelve"*, measured *"from
  the release of the specification revision in which the feature is first marked Deprecated"*; the
  ninety-day expedited-removal floor; the requirement that a named replacement *"must be Active in the
  revision in which the deprecation takes effect"*; and the Tier 1 SDK obligations quoted in 6.2.
- `https://modelcontextprotocol.io/specification/2026-07-28/deprecated` — the registry. Every row in
  `lab/lifecycle.py` is copied from this page, including the two whose earliest removal is a rule
  rather than a date. Its Removed section reads *"No features have been removed under this policy
  yet."*
- `https://modelcontextprotocol.io/specification/2026-07-28/changelog` — SEP-2577 (Roots, Sampling and
  Logging deprecated, with the migration sentences quoted in 4.2), SEP-2322 (MRTR and the required
  `resultType`), SEP-2575 (the removal of `ping`, `logging/setLevel` and
  `notifications/roots/list_changed`, and the removal of SSE resumability with the *"clients MUST
  re-issue it as a new request with a new request ID"* rule quoted in 1.4), and the error-code
  allocation policy behind the renumbering in 2.3.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr` — every normative rule
  in 5.1 and the security requirements in 5.2, including *"servers **MUST** treat `requestState` as an
  attacker-controlled input"* and the replay-prevention `SHOULD` list.

**The paper:**

- `https://www.rfc-editor.org/info/rfc9413` — title, number, DOI `10.17487/RFC9413`, status
  Informational, year 2023, and the abstract quoted in the paper part. The row already exists in
  `docs/PAPERS.md`; nothing new was added.

**The installed and published SDKs — read and run, not remembered:**

- `.venv/Lib/site-packages/mcp/` at `mcp==1.29.1`: `mcp.shared.version` present with
  `SUPPORTED_PROTOCOL_VERSIONS = ['2024-11-05', '2025-03-26', '2025-06-18', '2025-11-25']`;
  `mcp.types.InputRequiredResult` **absent**; `ListRootsRequest`, `CreateMessageRequest` and
  `SetLevelRequest` all present, none marked deprecated, none warning when constructed.
- `mcp==2.1.1`, run in a throwaway environment with
  `uv run --isolated --no-project --with "mcp==2.1.1"`: `mcp.shared.version` gone with a bare
  `ModuleNotFoundError`; `mcp.types.version` present with `LATEST_PROTOCOL_VERSION = '2026-07-28'` and
  `MODERN_PROTOCOL_VERSIONS = ('2026-07-28',)`; `mcp.server.fastmcp` raising a `ModuleNotFoundError`
  whose message names `MCPServer` and the migration guide; `mcp.types.InputRequiredResult` present;
  the three deprecated types still present, two of them mentioning SEP-2577 in a **docstring** only,
  and none of the three warning at runtime. **Nothing was installed into the project;
  `git diff pyproject.toml uv.lock` is empty.**
- `https://py.sdk.modelcontextprotocol.io/v2/migration/#fastmcp-renamed-to-mcpserver` — named, because
  the SDK's own error message names it. It is quoted rather than summarised, and 6.3 leaves a
  `TODO(verify: ...)` for reading it in full and extending `bump_probe.py` accordingly, rather than
  guessing at the rest of the surface.

**No ADK symbol is used anywhere in this day.** Every script is standard library plus, in
`bump_probe.py`, the `mcp` package's own metadata. That is deliberate: the subject is the protocol and
the SDK, and a framework in the middle would hide both.

**One honest gap, recorded rather than papered over.** The five JSON-RPC error bodies in `lab/errors.py`
are written to the shapes the specification defines for those codes; they are not captured from a live
server. The script's output is real and the classification argument stands, but a reader who wants a
captured `-32020` from a running server should get it from `sutra_mcp` once Day 34's server is up.

---

## §9 Say it in an interview

"The most useful day we had on the MCP work was the one where we broke everything on purpose, and it
split cleanly into two halves that turned out to be the same subject.

The first half was failure. A client with no deadline of its own cannot tell a slow server from a dead
one — both are the absence of bytes — so we measured it: same server, same work, 6.05 seconds with no
clock and 2.01 with one. Then the part that surprised people. A timeout ends your wait, not the
server's work. We watched the client give up at two seconds and the server announce it had finished at
6.06, with nothing crossing the wire in between, which means a timed-out write is not a failure, it is
an *unknown* — and if you report it as a failure and retry, you get two audit rows and two customer
emails. Over HTTP there is not even a cancel message any more: closing the response stream is the
signal, the server discovers it on its next write, and we saw it write one more chunk successfully
into the socket buffer before it noticed.

The second failure surface was malformed servers, and the finding there is that validation has to
happen at the boundary and has to produce a *named* diagnosis. Five checks — is it JSON, is it JSON-RPC
2.0, is the id one I sent, is there exactly one of result and error, does the payload match the
method — and the hardened reader names all five crimes and keeps running while the one-line version
dies on the first and never sees the other four. The check people leave out is the id one, because it
is the only one a schema cannot do for you. And the name matters because it lets you classify: a
malformed reply is deterministic, so retrying it is a self-inflicted flood — we put numbers on that
too, thirty requests spent for nothing against a server that was already struggling.

The two failures I would actually lead with are the silent ones. A reply can pass all five checks and
be about a different ticket, and then a model writes a fluent sentence with the number *you asked
about* interpolated into it, so the user reads a confident answer that is false. The fix is an echo
check — the request's identifying key has to come back in the structured half of the result — and it is
the one check the protocol cannot do for you, because relevance is not a protocol property.

The second half of the day was migration, and it is a calendar rather than a bug. Since the 2026-07-28
revision MCP has a lifecycle policy: Active, Deprecated, Removed, a minimum twelve-month window, and
one registry page listing everything on the way out with its migration path. Roots, Sampling and
Logging are on it, deprecated by one proposal, and they are one thing rather than three — all of them
were the server reaching back into the client across a held connection, and the same revision deleted
sessions. What replaced them is a single pattern: the server answers with `input_required`, hands back
an opaque `requestState`, and the client re-issues the original request with a new id. We proved why
with three workers where the retry lands on a different one from the first attempt; the stateless
version completes and the old one comes back with 'no pending question for this call'.

Two things I would want to be asked about. First, `requestState` is opaque, not protected — four lines
of base64 and json turned a count of four into four hundred, and the spec requires an HMAC whenever
that state influences business logic. Second, we priced the SDK upgrade without taking it. Our pin
speaks protocol 2025-11-25 and the current release speaks 2026-07-28, so we ran the same introspection
script under both in a throwaway environment and diffed the symbol tables. Four things change, the
client code survives and the server code does not, and the lockfile never moved. The detail I keep
coming back to is from that diff: the SDK removed two modules, and one of them left a nine-line stub
that raises with the new import line and a link to the migration guide, and the other one just
vanished. Same exception class, same removal, and one of them ends the investigation in the traceback."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 38` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it to
someone else without the page open.

**Phase 5's gate** is `sutra-mcp` serving tools statelessly, and today is the last teaching day of the
phase. So the gate is not only "the server works" but "you have watched it, and its client, fail in
eight named ways and you know which of those `sutra/mcp/hardening.py` will fix on
[Day 44](../day-44-client-hardening/LESSON.md)". Run the Phase 5 freshness check as part of finishing:
the specification revision (§3, step 8), the ADK and `mcp` releases since the pins, and the three
providers' free rosters. Record any finding in `docs/CHANGELOG_PLAN.md` **before** Day 39 begins.

[Day 39](../day-39-database-tools/LESSON.md) opens Phase 6 with a real database behind the tools, which
is the first day where a failure has a row in it.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 38 | <date> | MCP-11, MCP-12, MCP-31 | 20 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded: `mcp` stays at
`1.29.1`, `google-adk` at `2.7.1`, and `gemini-3.7-flash` stays pinned as recorded on 2026-08-26. The
`mcp==2.1.1` runs in section 6 used `uv run --isolated --no-project --with`, which writes nothing to
`pyproject.toml` or `uv.lock`. The measured bill for that bump is in
[6.3](parts/06-in-production/6.3-the-bill-for-a-bump.md), for whoever eventually decides it; it becomes
a row on the day something is actually installed.

**`docs/PAPERS.md`** — **no new rows.** `doi:10.17487/RFC9413` already has its dated row, and it is
taught here in [`papers/01-maintaining-robust-protocols.md`](papers/01-maintaining-robust-protocols.md).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**The commit:**

```text
day 38: failure and migration lab - timeouts, malformed servers, the leaving list - closes MCP-11, MCP-12, MCP-31
```

# 🔎 Master Plan Addendum — Gap Validation & Latest-Feature Amendments

> **Validated against the live ecosystem on 2026-08-12** (PyPI, ADK release notes, MCP spec blog, A2A/AP2 announcements).
> This file follows Principle 14: *if reality changes, the plan is amended first.* Merge these IDs into
> `00_MASTER_PLAN.md`, bump its version, and log this in `docs/CHANGELOG_PLAN.md`.

---

## Part 1 — ✅ What is confirmed current (no change needed)

| Claim in the plan                                        | Verified? | Evidence                                             |
| -------------------------------------------------------- | --------- | ---------------------------------------------------- |
| `google-adk` 2.6.3, released 2026-08-07, is the latest    | ✅ Yes     | PyPI, checked 2026-08-12                             |
| ADK Python 2.0 GA on 2026-05-19; graph Workflow Runtime   | ✅ Yes     | Official ADK 2.0 docs                                |
| The four 1.x → 2.x traps (node model, event fields, yield-not-append, don't-swallow-exceptions) | ✅ Yes | Official breaking-changes list |
| Python 3.10–3.14 supported; 3.12 is a safe pick           | ✅ Yes     | PyPI metadata                                        |
| Agent Skills = open agentskills.io spec + `SkillToolset`  | ✅ Yes     | Still the standard                                   |
| A2A governed by Linux Foundation; ADK ships it            | ✅ Yes     | But it moved — see AG-34 below                       |

**Verdict:** the skeleton (15 phases, 96 days, six curricula, traceability) is sound. Nothing below
changes the structure. Everything below is **new rows and rewritten rows**, absorbed into existing days.

---

## Part 2 — 🚨 CRITICAL: The MCP 2026-07-28 specification

### 2.1 What happened, in simple language

Two weeks ago (2026-07-28) MCP shipped **the largest revision since the protocol launched**.

> 💡 **The one-sentence version:** old MCP worked like a **phone call** — you dial (initialize),
> stay connected (session), and hang up. New MCP works like the **web** — every request is
> self-contained, any server instance can answer it, and nothing depends on a held connection.

**Concrete example of why this matters to Sutra:** you deploy `sutra-core` to Cloud Run with 3
instances. Under the old spec, the instance that did your handshake holds your session — if your
next request lands on instance 2, it fails, so you need "sticky sessions." Under the new spec there
is no handshake and no session: any instance answers any request, and Cloud Run can scale freely.
This is exactly the Day 43 "stateless mode" lesson — except it is now *the whole protocol*, not a mode.

### 2.2 Rows in the current plan that now teach deprecated behavior

| Existing ID | Current text                                                    | Amendment                                                                                        |
| ----------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| MCP-03      | Transports: stdio, SSE, Streamable HTTP                          | Keep stdio + Streamable HTTP. Teach SSE as **legacy with a published removal schedule** — one paragraph, not a lab. |
| MCP-04      | Stateful sessions, lifecycle, initialization handshake           | Rewrite: teach the **stateless core** as the present, and the old session model as history (you will still meet it in older servers). |
| MCP-14      | Session persistence (`getstate`/`setstate`), reconnection        | Rewrite: state now travels **inside the payload as explicit handles**, not inside a held connection. |
| MCP-20      | Streamable HTTP server, stateless mode, Cloud Run                | "Stateless mode" is no longer a mode — it is the default architecture. Reframe the day.           |
| MCP-13      | MCP authentication: bearer, OAuth2                               | Add the 2026 hardening: issuer validation (RFC 9207) and the shift from Dynamic Client Registration to **client metadata documents (CIMD)**. |

### 2.3 New MCP rows (extend the matrix: MCP-26 … MCP-33)

| ID     | Topic                          | Simple explanation + example                                                                                                                                                                 | Slot into |
| ------ | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| MCP-26 | **The 2026-07-28 stateless core** | No `initialize`, no session pinning; method and tool names ride in HTTP headers (`Mcp-Method`, `Mcp-Name`) so gateways can route on them; list results are cacheable with stable ordering. *Example: your load balancer can send `search_tickets` calls to a dedicated pool without parsing JSON bodies.* | Day 32 (rewrite the concept day) |
| MCP-27 | **Elicitation**                | The server asks the *user* a structured question mid-tool. *Example: your `close_ticket` tool discovers the ticket has 3 duplicates and asks "Close all 4 together? yes / no / cancel" — the answer comes back as `accept`, `decline`, or `cancel` plus typed content.* URL-mode elicitation sends the user to an external page for things that must not pass through the client (OAuth, card entry). | Day 36–37 |
| MCP-28 | **Tasks extension**            | Long-running work returns a **task handle** instead of blocking. The client polls `tasks/get`, can `tasks/update`, and cancellation is cooperative via `tasks/cancel`. *Example: "re-index the whole ticket archive" returns `task_abc123` immediately; Sutra checks progress every 10 s and shows it in the UI.* Replaces the older experimental Tasks API — a known breaking change. | Day 36 (pairs naturally with `progress_callback`) |
| MCP-29 | **MCP Apps extension**         | A tool can ship an interactive HTML interface rendered in a **sandboxed iframe** inside the chat client; templates are declared up front so clients can security-review and prefetch them; button clicks flow back over the same JSON-RPC channel. *Example: your triage tool returns a mini approval panel with Approve / Reject buttons instead of asking the user to type "approve".* First official extension (Final since Jan 2026). | Day 41 (server capabilities day) |
| MCP-30 | **Extensions framework + Enterprise Managed Authorization** | Capabilities now ship as versioned extensions on their own timelines (Apps, Tasks, EMA) instead of bloating the core. EMA lets an enterprise IdP govern which servers/extensions users may touch. *Example: your company allows the GitHub MCP server but blocks any server with the Apps extension, by policy, centrally.* | Day 37 |
| MCP-31 | **Deprecation lifecycle: Roots, Sampling, Logging** | These three client-side features are formally deprecated with a ≥12-month window. You must still *recognize* them in servers you audit, and know the replacement: server-initiated requests are redesigned as **multi round-trip requests** — the server returns "I need input" (`InputRequiredResult`) with opaque state, the client gathers answers and re-issues the call. *Example: instead of holding a stream open to ask your LLM for a completion, the server hands back a resumable request ticket.* | Day 38 (failure lab becomes failure + migration lab) |
| MCP-32 | **MCP governance & registry**  | MCP was donated to the **Agentic AI Foundation** (Linux Foundation) in Dec 2025 — Anthropic, OpenAI, Block as co-founders; AWS, Google, Microsoft supporting. There is an official server registry alongside community ones. *Interview line: "MCP is vendor-neutral now — that's why betting Sutra's data boundary on it is safe."* | Day 32 |
| MCP-33 | **Serving a whole ADK agent over MCP** (`to_mcp_server`) | ADK 2.5 added a one-call way to expose an entire agent (not just its tools) as an MCP server. *Example: Sutra's Researcher becomes an MCP server that any MCP host — Claude Desktop, an IDE, a partner's agent — can call as a tool.* Compare with A2A on Day 89: MCP = agent-as-tool, A2A = agent-as-peer. | Day 42 |

📌 **Effort math:** this is a rewrite of ~4 existing MCP days plus 2 days of new material.
Recommendation: keep Phase 5–6 at 14 days by trimming the legacy SSE lab to a reading,
and absorbing MCP-27/28 into Days 36–38 which already cover long jobs, auth, and failure.

---

## Part 3 — 🆕 New agent concepts (extend Curriculum A: AG-31 … AG-34)

### AG-31 — Computer use & browser agents

- **Simple explanation:** so far every Sutra tool is an API. But most of the world has no API — it
  has a website. Computer-use models look at a **screenshot**, decide, and emit click/type/scroll
  actions in a loop, exactly like the think→act→observe loop from Day 3, with pixels as observations.
- **Example:** a vendor's status page has no API. A browser agent opens it, reads the incident
  banner, screenshots it, and files the result into Sutra's triage graph as evidence.
- **Why it must be in the plan:** it is a headline 2025–26 capability (Gemini and Claude both ship
  computer-use models; agentic browsers are mainstream) and a standard interview topic.
- **Slot:** one day in Phase 10 (it is above all a *safety* topic — a clicking agent has the largest
  blast radius of anything in Sutra), demoed against a locally-hosted dummy site.

### AG-32 — Agent sandboxing & execution isolation

- **Simple explanation:** when an agent writes and runs code, assume the code can be wrong or
  hostile (prompt injection can steer it). So it never runs on your machine — it runs in a
  **disposable isolated box** (a microVM) with no credentials, minimal network, and a kill switch.
  Blast radius, made physical.
- **Example:** Sutra's analysis agent generates pandas code for a CSV. The code runs in a sandbox
  that can see only that CSV. If the generated code tries `rm -rf /` or calls an external URL,
  it damages a box that is deleted 30 seconds later.
- **Ecosystem fact:** ADK now ships `e2b` and `daytona` extras for exactly this — sandbox providers
  are first-class citizens of the framework.
- **Slot:** Day 16 (code execution) gains the concept; Phase 10's security day gains the practice.

### AG-33 — Retrieval & embeddings (one honest RAG day)

- **Simple explanation:** grounding (Day 16) fetches from the live web; **retrieval** fetches from
  *your own* documents by meaning. Text becomes vectors (lists of numbers where similar meanings sit
  near each other); a query finds its nearest neighbors; the agent reads only those chunks.
- **Example:** "Has anything like ticket #4521 happened before?" — keyword search misses it because
  the old ticket says "login loop" not "auth redirect bug". Embedding search finds it, because the
  *meanings* are neighbors.
- **Why amend the plan:** the plan defers vector DBs, and that discipline is right — but a job
  interview for an AI engineer role asks about RAG almost every time. One day, using ADK's
  `MemoryService` semantics extended with a local embedding index, closes the gap without
  turning Sutra into a RAG course. Chunking, top-k, and "when RAG is the wrong tool" included.
- **Slot:** Phase 7, Day 49 extension (memory day) or one added day after it.

### AG-34 — The agent economy: identity, trust, and payments

- **Simple explanation:** once agents talk to *strangers'* agents (A2A, Day 89), three questions
  appear that never existed inside one company: **Who are you?** (identity), **Can I trust what
  your card claims?** (verification), **How do you pay?** (transactions).
- **What shipped since the plan's A2A section was drafted:**
  - **A2A v1.0** (April 2026): **signed Agent Cards** — a card carries a cryptographic signature
    from the publishing domain, so Sutra can verify a partner card is genuine before trusting its
    declared skills or endpoints. 150+ production organizations; SDKs in five languages.
  - **AP2 (Agent Payments Protocol)** — an open A2A extension (60+ payment orgs) where a user signs
    a **mandate** ("agent X may spend up to $100 on cloud compute until May 1") and the agent
    transacts inside that envelope, auditably. *Example: Sutra's research agent buys a $5 market
    report within a pre-approved mandate; the mandate, not vibes, is the authorization.*
  - **x402 / Trusted Agent Protocol** — micropayments and agent-identity attestation layers in the
    same stack. Awareness-level only.
- **Slot:** Day 89 (A2A) is rewritten to v1.0 + signed cards as hands-on; AP2/x402/TAP as a 🅿️
  concept section — *know the map, build only A2A*.

---

## Part 4 — 🔧 ADK 2.2 → 2.6 feature deltas (extend Curriculum B: ADK-73 … ADK-78)

The plan's baseline (2.6.3) is correct, but its feature matrix was drafted before these landed:

| ID     | Feature (version)                                        | Simple explanation + example                                                                                                                       | Slot |
| ------ | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| ADK-73 | **Default model is now `gemini-3-flash-preview`** (2.2)  | Agents without an explicit `model=` silently changed model. Rule for Sutra: **every agent pins its model explicitly.** *Example bug this prevents: your eval scores shift overnight because the default moved under you.* Note the 2026-10-16 gemini-2.5-flash shutdown lands inside your 96 days. | Day 5, Day 9 |
| ADK-74 | **`AutoTracingPlugin`** (2.2)                            | One plugin auto-instruments OpenTelemetry across the app instead of hand-wiring spans. *Example: turn it on Day 84 and every node, tool call, and model call appears in the trace tree for free.* | Day 84 |
| ADK-75 | **`RubricBasedMultiTurnTrajectoryEvaluator`** (2.2)      | Grades *how* the agent behaved across a whole conversation against a written rubric, not just the final answer. *Example rubric line: "escalated to a human before any external write" — pass/fail per trajectory.* | Day 80 |
| ADK-76 | **HITL resumption for standalone nodes + `NodeTool`** (2.5) | Human-approval pauses now resume cleanly even for bare nodes. Directly upgrades your Day 64 approval gate.                                          | Day 64 |
| ADK-77 | **Live voice: VAD events + non-blocking tools** (2.5)    | Voice agents surface voice-activity-detection events and run tools in the background so the conversation doesn't freeze mid-tool. *Example: the standup agent keeps listening while it fetches yesterday's digest.* | Day 75–77 |
| ADK-78 | **New extras to know exist** (2.6): `agent-identity`, `e2b`, `daytona`, `benchmark`, `toolbox`, `slack`, `antigravity` | Awareness row: identity (→ AG-34), sandboxes (→ AG-32), MCP Toolbox for Databases (a first-party MCP server for SQL databases — evaluate it against hand-writing `sutra-core`'s DB tools on Day 39), Slack ingestion for intake. | Day 39, 91 |

Also fold into existing rows: `to_mcp_server` (→ MCP-33), and the GCP Skill Registry endpoint
moving under **Agent Registry** (touches SK-16 sourcing day and ADK-67 deployment).

---

## Part 5 — 🗓️ Where the days move (net change: +2 days, 96 → 98, or 96 kept by merging)

| Phase | Change                                                                                               |
| ----- | ---------------------------------------------------------------------------------------------------- |
| 5–6 (MCP) | Rewrite Days 32, 34, 37, 38, 43 for the 2026-07-28 spec; add MCP-27/28/29 material into 36–38 and 41–42. Demote SSE lab to a reading. **±0 days.** |
| 7     | Day 49 extended (or +1 day) for AG-33 retrieval.                                                     |
| 10    | +1 day: AG-31 computer use + AG-32 sandbox practice (fits the phase's safety theme).                  |
| 12    | Day 80 adopts ADK-75 rubric trajectory evaluator.                                                    |
| 13    | Day 84 adopts AutoTracingPlugin; Day 89 rewritten to A2A v1.0 + signed cards + AP2 concept section.   |
| Gates | Add to every phase-gate freshness check: `MCP spec revision changed? → re-read this addendum's Part 2.` |

---

## Part 6 — 🚫 Checked and deliberately still excluded

| Topic                         | Why it stays out                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------ |
| Model fine-tuning / training  | A different discipline. Agentic AI engineering assumes the model; note it as a stated non-goal so the omission reads as a decision, not a blind spot. |
| Full RAG infrastructure (vector DB ops, rerankers, hybrid search) | AG-33 gives the concept + one honest implementation; production RAG infra is its own course. |
| Building an agentic IDE / coding-agent product | You *use* Claude Code daily in this plan — that is the learning. Building one is out of scope. |
| Crypto settlement details (x402 internals) | Awareness in AG-34 is enough; the regulatory ground is still moving.                        |

---

## Part 7 — 🎯 One honest note on "expert"

Completing this plan makes you demonstrably **competent and hireable**: you will have built,
secured, evaluated, and deployed a real multi-agent system, and you can defend every decision in it.
"Expert" is not a finish line in a field where the flagship protocol rewrote itself two weeks ago —
it is the **habit** this plan already installs: the weekly freshness check, the release-notes
discipline, the "amend the plan first" rule. This addendum exists because that habit works.
Keep running it after Day 96.

---

*Merge checklist: [ ] fold Part 2–4 IDs into the matrices · [ ] bump plan version · [ ] log in
`CHANGELOG_PLAN.md` · [ ] update TRACEABILITY totals (~181 → ~196 IDs) · [ ] re-cut Phase 5/6/10 days.*

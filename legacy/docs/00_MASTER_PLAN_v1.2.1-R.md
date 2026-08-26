# 🧵 MASTER PLAN — Project **Sutra**
## Agentic AI Engineering with **Google ADK 2.x · MCP · Agent Skills · A2A**

> **Sutra** (Sanskrit सूत्र) means *thread* — the thread that strings concepts together, and the
> thread of execution that runs through a multi-agent system.
>
> **Document version: v1.2.1-R** (R = *reconstructed*).
> ⚠️ **Provenance:** the original `00_MASTER_PLAN.md` was lost before any day was generated.
> This version was reconstructed on **2026-08-13** from the surviving contract documents:
> `CLAUDE.md`, `01_MASTER_PLAN_ADDENDUM_GAPS.md` (v1.1 merge, 2026-08-12),
> `02_ADDENDUM_ZERO_BUDGET_MODELS.md` (v1.2 merge), the ledger files, and the structure of the
> sibling plans (Yantra, Mandala). Every day number and ID that appears in a surviving document
> is preserved exactly; the connective tissue between those anchors is reconstruction.
> See `docs/adr/ADR-0001-plan-reconstruction.md`. **If the original file resurfaces, diff it
> against this one and reconcile via an ADR before generating further days.**
>
> 📌 **Purpose:** the single source of truth. Every later document points back here.
> Where `02_ADDENDUM_ZERO_BUDGET_MODELS.md` conflicts with this plan on model choice or paid
> services, **the addendum wins** (its rule, kept).

---

## 📑 Table of Contents

| §  | Section |
| --- | --- |
| 1  | 🎬 The Vision — one system, six threads |
| 2  | 🧭 Core Principles — rules we never break |
| 3  | 🏗️ The Product — what Sutra actually is |
| 4  | 💸 Model & Budget Policy — the $0 constraint |
| 5  | ⚙️ ADK 2.x Baseline — versions, traps, verification |
| 6  | 🧶 The Six Curricula & the ID scheme |
| 7  | 🤖 Curriculum A — Agent Concepts (AG-01..34) |
| 8  | 🔧 Curriculum B — Google ADK (ADK-01..78) |
| 9  | 🔌 Curriculum C — MCP (MCP-01..33) |
| 10 | 📜 Curriculum D — Agent Skills (SK-01..20) |
| 11 | 📦 Curriculum E — Operations (OPS-01..18) |
| 12 | 🛡️ Curriculum F — Safety & Security (SEC-01..16) |
| 13 | 🗺️ The 15 Phases |
| 14 | 🗓️ The 96-Day Map (day → IDs closed) |
| 15 | 🚦 Phase Gates & the Freshness Check |
| 16 | 📒 Ledgers & Traceability |
| 17 | 📄 The Day Document Contract |
| 18 | ✍️ The Style Guide |

---

## 1 · 🎬 The Vision — one system, six threads

By Day 96 you will have **built, secured, evaluated, and deployed a real multi-agent system** —
Sutra, an autonomous support-ticket triage desk — and you will be able to defend every decision
in it. The goal is a demonstrably **competent and hireable** agentic AI engineer, with a public
repo as the proof.

Three commitments shape everything:

1. **One project, not toy demos.** Every concept lands as a change to Sutra. Nothing is learned
   in a vacuum; every gear is load-bearing.
2. **The repo is the memory, not the chat.** Ledgers + day documents mean any capable CLI agent
   (Claude Code today, any other tomorrow) can pick up exactly where the last one stopped.
3. **Reality outranks the plan** (Principle 14). The flagship protocol rewrote itself two weeks
   before this project started; the weekly freshness check and the amend-first rule exist because
   that will keep happening.

### 1.1 Stated non-goals (decisions, not blind spots)

| Excluded | Why |
| --- | --- |
| Model fine-tuning / training | A different discipline. Agentic engineering assumes the model. |
| Full RAG infrastructure (vector DB ops, rerankers, hybrid search) | AG-33 gives the concept + one honest implementation; production RAG infra is its own course. |
| Building an agentic IDE / coding-agent product | You *use* Claude Code daily here — that is the learning. |
| Crypto settlement internals (x402 etc.) | Awareness in AG-34 is enough; the regulatory ground is still moving. |
| Paid APIs, billing accounts, subscriptions | The $0 constraint (§4) is absolute. |

---

## 2 · 🧭 Core Principles — rules we never break

1. **Doc-first.** The day document is written before any code; the code follows the doc.
2. **One day, one document, one commit.** Traceable, append-only history.
3. **Simple language + a concrete example, always.** If a concept can't be explained simply
   with an example, it isn't understood yet (§18 enforces this).
4. **Build first, compare after.** Hand-roll the mechanism once (the loop, tool calling), *then*
   adopt the framework — so the framework is a convenience, never a mystery.
5. **Every concept is load-bearing.** If removing it wouldn't break Sutra, it doesn't get a day.
6. **Verify the whole project after every step.** Each day ends with the full check suite green,
   not just today's snippet.
7. **Never invent a version number.** Look it up live, or leave a `TODO` with the exact lookup
   command. Record every pin in `PACKAGES.md` with the date.
8. **Never invent an API.** Every ADK symbol used must be verified against ADK 2.x docs
   (adk.dev) on the day it is used, and the day doc states which page was checked.
9. **Secrets never touch git.** `.env` + `.gitignore` from Day 1; the repo goes public in
   Phase 14, so the discipline is real.
10. **Fail honestly.** Agents never fabricate a result to cover an error; errors surface,
    escalate, and are logged. (This applies to the human too.)
11. **Evals are tests.** Behavior changes without a green evalset don't merge.
12. **Everything is a trace.** If it isn't observable, it didn't happen.
13. **Blast radius before capability.** Every new power (code exec, browsing, payments) arrives
    together with its containment story.
14. **If reality changes, the plan is amended first.** New spec revision, changed free tier,
    renamed API → amend via addendum + `CHANGELOG_PLAN.md`, *then* continue. Days are never
    silently patched.
15. **Zero budget is a feature.** Rate limits, quota routing, and caching are the curriculum,
    not obstacles to it (§4, Addendum 02).

---

## 3 · 🏗️ The Product — what Sutra actually is

**Sutra is an autonomous support-ticket triage desk** for a fictional software company
("the company data is synthetic, always" — Principle 9's cousin: never feed real personal or
employer data through free endpoints).

What it does when finished:

- **Intake** — tickets arrive (synthetic feed; Slack-shaped intake surveyed in Phase 14).
- **Triage graph** — a classifier routes each ticket; a Researcher agent gathers evidence
  (grounded web search, the ticket archive via retrieval, vendor status pages);
  a Writer↔Critic pair drafts and reviews responses.
- **Action with brakes** — tools that *write* anything (close a ticket, post a reply) sit
  behind approval gates with human-in-the-loop resumption.
- **Memory** — the desk remembers: session state, cross-session memory, an embedding index
  over the ticket archive ("has anything like #4521 happened before?").
- **The data boundary is MCP** — every data source Sutra touches is an MCP server
  (`sutra-mcp`); Sutra's own agents are also *servable* over MCP (`to_mcp_server`) and
  peer-able over A2A.
- **Skills** — recurring procedures are packaged as Agent Skills (agentskills.io spec),
  audited and version-pinned in `SKILL_PROVENANCE.md`.
- **Ambient** — a nightly job re-indexes, runs the full evalset, and posts a digest; a voice
  standup agent reports the queue state.
- **Operable** — OpenTelemetry traces end to end, evals in CI, a documented deploy story
  (container-first, Kubernetes on the laptop, cloud-ready unchanged).

**Repo layout (established Day 1, grown daily):**

```
sutra/
├── CLAUDE.md              # standing instructions for the driver agent
├── Makefile               # `make check` — the whole-project gate (Day 31 completes it)
├── .env                   # keys (never committed)
├── pyproject.toml         # uv-managed; every pin dated in PACKAGES.md
├── sutra/                 # the product package (agents, tools, graph)
├── sutra_mcp/             # Sutra's MCP server(s)
├── skills/                # Agent Skills (spec-compliant folders)
├── tools/                 # repo tooling (trace.py regenerates TRACEABILITY.md)
├── tests/                 # unit + eval harness
└── docs/
    ├── 00_MASTER_PLAN.md          # this file
    ├── NN_MASTER_PLAN_ADDENDUM_*.md
    ├── adr/                       # architecture decision records
    └── days/                      # day_NNN.md + the ledgers (PROGRESS, TRACEABILITY,
                                   #   PACKAGES, SKILL_PROVENANCE, CHANGELOG_PLAN)
```

---

## 4 · 💸 Model & Budget Policy — the $0 constraint

Governed in full by **`02_ADDENDUM_ZERO_BUDGET_MODELS.md`**, which **wins over this plan** on
model choice and paid services. The short version:

- **Gemini Flash-class** (free AI Studio key, `GOOGLE_GENAI_USE_VERTEXAI=FALSE`) is the primary
  brain. **Never assume a Pro model.**
- **Groq** is the speed lane; **OpenRouter `:free`** is the breadth lane (the `:free` suffix is
  mandatory — linted); **Ollama** is the offline/privacy baseline.
- **Every agent pins its model explicitly** (ADK-73 — the 2.2 default-model change makes
  implicit defaults a silent bug).
- **Before pinning any model string, look up the provider's current free list** and record
  model + date in the ledger. Free rosters move (Dec 2025 precedent).
- **Every model call path handles HTTP 429** honestly: respect `retry-after`, back off, then
  escalate — never fabricate a result (Principle 10).
- **Quota is the currency.** Budgets, routing (Day 70's Quota-Router), and caching (Day 51)
  are denominated in RPM/RPD per provider, not dollars.

---

## 5 · ⚙️ ADK 2.x Baseline — versions, traps, verification

- **Framework:** `google-adk` **2.x** — baseline **2.6.3** (released 2026-08-07; verified on
  PyPI 2026-08-12). Re-verify on install day; record in `PACKAGES.md`.
- **Language:** Python **3.12** (supported window 3.10–3.14; 3.12 is the stability pick).
- **Environment:** `uv` for env + dependency management.
- **ADK 2.0 GA was 2026-05-19** and introduced the graph **Workflow Runtime**. The internet is
  full of 1.x tutorials. **Every ADK API used in a day doc must be verified against adk.dev
  that day, and the doc states which page was checked** (Principle 8).

### 5.1 The four 1.x → 2.x traps (from the official breaking-changes list)

| # | Trap | 1.x habit | 2.x reality |
| --- | --- | --- | --- |
| 1 | **Node model** | Agents composed only via `sub_agents` trees; workflow agents as special agent classes | The graph **Workflow Runtime** is the composition layer: nodes in a graph, with agents as one node type. Port compositions to the node model; don't force everything through agent-tree idioms. |
| 2 | **Event fields** | 1.x event attribute names/shapes | Event fields were renamed/restructured in 2.0. Never copy event-handling code from a 1.x tutorial; check the 2.x event reference the day you touch events (Day 7). |
| 3 | **Yield, don't append** | Custom agents collected events into a list and returned them | Custom agents/nodes **yield** events as they happen. Appending-then-returning breaks streaming and ordering guarantees. |
| 4 | **Don't swallow exceptions** | Tool/model errors caught and returned as strings, hiding failures | 2.x surfaces exceptions through the runtime so callbacks/plugins can act on them. Swallowing them silently breaks retries, tracing, and honesty (Principle 10). |

Any day doc that touches one of these areas must name the trap it is avoiding.

---

## 6 · 🧶 The Six Curricula & the ID scheme

Every concept in the plan has an ID. A day **closes** an ID when the concept is built into (or
demonstrably exercised against) Sutra and the day's gates are green. `TRACEABILITY.md` is
regenerated from the day docs (`tools/trace.py`); **any open ID from a completed phase is a bug.**

| Curriculum | Prefix | Count | Thread |
| --- | --- | --- | --- |
| A — Agent Concepts | `AG` | 34 | Framework-independent ideas: loops, tools, context, planning, multi-agent, computer use, retrieval, the agent economy |
| B — Google ADK | `ADK` | 78 | The framework: agents, runtime, tools, workflows, live, evals, deploy |
| C — MCP | `MCP` | 33 | The data boundary: the 2026-07-28 stateless protocol, clients, servers, extensions |
| D — Agent Skills | `SK` | 20 | The open agentskills.io spec, `SkillToolset`, authoring, sourcing, auditing |
| E — Operations | `OPS` | 18 | Repo discipline, secrets, testing, budgets, CI, tracing infra, deploy artifacts |
| F — Safety & Security | `SEC` | 16 | Threat models, injection defense, permissions, sandboxing, data boundaries |

**Total: 199 concept IDs.** (Addendum 01 estimated "~181 → ~196"; exact post-merge count is 199:
181 original + AG-31..34, ADK-73..78, MCP-26..33.)

> 🅿️ Some IDs are **parked** (awareness-level): you learn the map, you don't build the thing.
> Parked IDs are marked 🅿️ in the day docs and still close normally.

The per-ID topics live in the day map (§14) — each day's row is the authoritative statement of
what its IDs mean. Curriculum sections 7–12 give the narrative arc and call out the rows that
surviving documents fix precisely.

---

## 7 · 🤖 Curriculum A — Agent Concepts (AG-01..34)

The framework-independent thread: what an agentic system *is* (AG-01), how LLMs actually work
for builders (AG-02), the think→act→observe loop hand-rolled before any framework touches it
(AG-03, Day 3), tools and schemas by hand (AG-04), instruction design (AG-05), tool design
(AG-06), grounding vs retrieval (AG-07), context engineering (AG-08..10), token economics
(AG-11), memory design (AG-12..15), delegation and planning (AG-16..18), multi-agent patterns
(AG-19..21), durability and humans (AG-22..23), ambient agents (AG-24..25), evals thinking
(AG-26..28), identity and ecosystems (AG-29..30).

**Fixed by Addendum 01 (verbatim anchors):**

- **AG-31 — Computer use & browser agents** → Day 71 (Phase 10; it is above all a *safety*
  topic). Demoed against a locally-hosted dummy site.
- **AG-32 — Agent sandboxing & execution isolation** → concept closes Day 16 (code execution);
  practice reinforced Day 71. ADK's `e2b`/`daytona` extras make sandbox providers first-class.
- **AG-33 — Retrieval & embeddings (one honest RAG day)** → Day 49. Chunking, top-k, and
  "when RAG is the wrong tool" included.
- **AG-34 — The agent economy: identity, trust, payments** → Day 89. A2A v1.0 signed cards
  hands-on; AP2 / x402 / Trusted Agent Protocol as 🅿️ concept sections.

---

## 8 · 🔧 Curriculum B — Google ADK (ADK-01..78)

The framework thread, in dependency order: installation and the `Agent` class (ADK-01..02),
instructions and the dev UI (ADK-03), events and streaming (ADK-04..05 — trap #2 and #3
territory), sessions and services (ADK-06..07), models and providers (ADK-08 = Ollama/local,
ADK-09 = LiteLLM routing — Day 9), tools (ADK-10..18), state and artifacts (ADK-19..21),
context ops (ADK-22), error surfacing (ADK-23 — trap #4), `SkillToolset` (ADK-24), MCP-side
helpers (ADK-25..26), memory services (ADK-27..31), the graph Workflow Runtime (ADK-32..42 —
trap #1 territory), durable execution (ADK-43..48), plugins in anger (ADK-49..50), scheduled
runs (ADK-51), Live API (ADK-52..57), evals (ADK-58..62), observability (ADK-63..65),
deployment (ADK-66..69), interop (ADK-70..72).

**Fixed by Addendum 01 (the 2.2→2.6 deltas):**

| ID | Feature | Closes on |
| --- | --- | --- |
| ADK-73 | Default model is now a preview — **every agent pins its model explicitly** | Day 5 (reinforced Day 9) |
| ADK-74 | `AutoTracingPlugin` — OTel across the app in one plugin | Day 84 |
| ADK-75 | `RubricBasedMultiTurnTrajectoryEvaluator` | Day 80 |
| ADK-76 | HITL resumption for standalone nodes + `NodeTool` | Day 64 |
| ADK-77 | Live voice: VAD events + non-blocking tools | Day 76 |
| ADK-78 | 2.6 extras awareness: `agent-identity`, `e2b`, `daytona`, `benchmark`, `toolbox`, `slack`, `antigravity` | Day 39 (revisited Day 91) |

---

## 9 · 🔌 Curriculum C — MCP (MCP-01..33)

**Taught post-revision:** the **2026-07-28 spec is the present**; the old session model is
history you must still recognize in the wild. The one-sentence version: old MCP was a **phone
call** (dial, stay connected, hang up); new MCP is **the web** (every request self-contained,
any instance can answer, nothing depends on a held connection).

Arc: what MCP is and why it's Sutra's data boundary (MCP-01, + governance MCP-32), clients and
transports (MCP-02..03 — stdio + Streamable HTTP; **SSE is a legacy reading with a published
removal schedule, not a lab**), building `sutra-mcp` (MCP-04..09 — lifecycle taught stateless-
first), long jobs and state handles (MCP-10, MCP-14 — state travels **in the payload as
explicit handles**, not in a held connection), failure modes (MCP-11..12), auth (MCP-13 — 2026
hardening: RFC 9207 issuer validation, CIMD replacing Dynamic Client Registration), production
servers (MCP-15..19), stateless deployment (MCP-20..21 — "stateless mode" is no longer a mode,
it's the architecture), client hardening (MCP-22..23), audit (MCP-24..25).

**Fixed by Addendum 01 (the 2026-07-28 additions):** MCP-26 (stateless core mechanics:
`Mcp-Method`/`Mcp-Name` headers, cacheable lists) → Day 32 · MCP-27 (elicitation, incl.
URL-mode) → Day 37 · MCP-28 (Tasks extension: `tasks/get|update|cancel`) → Day 36 ·
MCP-29 (MCP Apps: sandboxed-iframe UIs) → Day 41 · MCP-30 (extensions framework + Enterprise
Managed Authorization) → Day 37 · MCP-31 (deprecation lifecycle for Roots/Sampling/Logging;
`InputRequiredResult` multi-round-trip replacement) → Day 38 · MCP-32 (governance: Agentic AI
Foundation, official registry) → Day 32 · MCP-33 (`to_mcp_server`: a whole agent as an MCP
server; MCP = agent-as-tool vs A2A = agent-as-peer) → Day 42.

---

## 10 · 📜 Curriculum D — Agent Skills (SK-01..20)

Skills = the open **agentskills.io** spec + ADK's `SkillToolset`. Arc: the spec and `SKILL.md`
anatomy (SK-01..03), loading into ADK (SK-04..05), authoring Sutra's own skills (SK-06..08),
progressive disclosure and design (SK-09..11), **sourcing and auditing third-party skills**
(SK-12..16 — SK-16 is the sourcing day; note the GCP Skill Registry endpoint moved under
**Agent Registry**), testing and versioning (SK-17..19), and the skills lint wired into
`make check` (SK-20, Day 31). Every third-party skill gets a row in `SKILL_PROVENANCE.md`
(source URL, licence, audit date) before it runs.

---

## 11 · 📦 Curriculum E — Operations (OPS-01..18)

Repo bootstrap (OPS-01), **secrets discipline** (OPS-02 — `.env`, `.gitignore`, key handling),
ledger & traceability tooling (OPS-03), structured logging (OPS-04), testing agents (OPS-05..06),
token/quota accounting (OPS-07), the `make check` gate (OPS-08), phase-gate audits (OPS-09,
OPS-11), caching ops (OPS-10), the Quota-Router (OPS-12), backoff/runbooks (OPS-13), quota-aware
scheduling (OPS-14), evals in CI (OPS-15), tracing infra (OPS-16), deploy artifacts (OPS-17..18 —
docker compose "Cloud-Run-shaped", kind/k3d Kubernetes; per Addendum 02, cloud walkthroughs are
documented, not billed).

---

## 12 · 🛡️ Curriculum F — Safety & Security (SEC-01..16)

Sandboxing concept at first code execution (SEC-01, Day 16), honest error surfacing (SEC-02),
MCP allowlists/filtering (SEC-03), runaway-agent containment (SEC-04), approval-gate design
(SEC-05), **prompt injection & the lethal trifecta** (SEC-06..07), defense-in-depth guardrails
(SEC-08..09), least-privilege tool permissions (SEC-10..11), PII and data boundaries with
synthetic data only (SEC-12..13), sandbox practice with computer use (SEC-14), honest backoff
under 429 (SEC-15), and the full pre-publication security review (SEC-16, Day 92 — before the
repo goes public).

---

## 13 · 🗺️ The 15 Phases

| Phase | Days | Theme | Gate flavor |
| --- | --- | --- | --- |
| 1 | 1–8 | Foundations: loop & first ADK agent | Hand-rolled loop + first pinned-model agent run |
| 2 | 9–16 | Models & tools | Four free providers benchmarked; built-in tools contained |
| 3 | 17–24 | State, context & discipline | State survives restarts; budgets enforced |
| 4 | 25–31 | Agent Skills | `make check` green incl. skills lint + `:free` lint |
| 5 | 32–38 | MCP I: the protocol (2026-07-28) | `sutra-mcp` serves tools statelessly |
| 6 | 39–45 | MCP II: production | MCP audit of sutra-core passes |
| 7 | 46–52 | Memory & retrieval | "Seen anything like this before?" answered at $0 |
| 8 | 53–59 | Workflows & multi-agent | Triage graph v1 end-to-end |
| 9 | 60–65 | Durability & humans | Kill it mid-run; it resumes; a human approved the write |
| 10 | 66–72 | Safety & security | Injection attempts contained; quota router live |
| 11 | 73–78 | Ambient & live | Nightly job + voice standup within free quota |
| 12 | 79–83 | Evals | Full evalset green; rubric trajectories pass |
| 13 | 84–88 | Observability & deployment | Traced end-to-end; runs in local k8s |
| 14 | 89–93 | Interop & launch | A2A peer verified; repo public |
| 15 | 94–96 | Capstone | The whole-system demo + audit |

**Every phase gate includes the freshness check (§15).**

---

## 14 · 🗓️ The 96-Day Map (day → IDs closed)

> The authoritative day→ID assignment. Day docs close **exactly** these IDs — no more, no fewer.
> Amendments (Addendum 01 Part 5, Addendum 02 §5) are already folded in below.
> 🅿️ = parked/awareness-level treatment inside that day.

### Phase 1 — Foundations (Days 1–8)

| Day | Title | IDs closed |
| --- | --- | --- |
| 1 | Bootstrap & the map — repo, `.env`+`.gitignore`, uv+Python 3.12, ledgers & `tools/trace.py`, the three free keys | AG-01, OPS-01, OPS-02, OPS-03 |
| 2 | LLM mechanics for agent builders — tokens, context, sampling; first raw `google-genai` call | AG-02 |
| 3 | The loop: think→act→observe, hand-rolled (no framework) | AG-03 |
| 4 | Tools by hand — function calling, JSON schemas, the tool-result turn | AG-04 |
| 5 | First ADK agent — install `google-adk`, `Agent` + runner, **pin `gemini-3.5-flash` explicitly** (repinned 2026-08-13, was `gemini-2.5-flash` — see CHANGELOG_PLAN.md) | ADK-01, ADK-02, ADK-73 |
| 6 | Instructions & personas; the `adk web` dev UI | ADK-03, AG-05 |
| 7 | Events & streaming — the 2.x event model (traps #2 and #3) | ADK-04, ADK-05 |
| 8 | Sessions, runs & in-memory services | ADK-06, ADK-07 |

### Phase 2 — Models & tools (Days 9–16)

| Day | Title | IDs closed |
| --- | --- | --- |
| 9 | Same agent, four free providers — Gemini ↔ Groq ↔ OpenRouter `:free` ↔ Ollama via LiteLLM; quality/latency/RPD benchmark table; Claude/OpenAI as 🅿️ reading | ADK-08, ADK-09 |
| 10 | Function tools in ADK — from Day 4's hand-rolled version to `FunctionTool` | ADK-10, ADK-11 |
| 11 | Tool context & state in tools; tool design principles | ADK-12, AG-06 |
| 12 | Structured output — schemas on the way out | ADK-13 |
| 13 | Callbacks — before/after model & tool | ADK-14, ADK-15 |
| 14 | Plugins — cross-cutting behavior | ADK-16 |
| 15 | Toolsets, OpenAPI & third-party tool wrappers | ADK-17 |
| 16 | Built-in tools with brakes — search grounding (free-allowance check + open-source search-MCP fallback per Addendum 02) + code execution; grounding vs retrieval; **sandboxing concept** | ADK-18, AG-07, AG-32, SEC-01 |

### Phase 3 — State, context & discipline (Days 17–24)

| Day | Title | IDs closed |
| --- | --- | --- |
| 17 | Session state deep dive — prefixes, scopes, lifetimes | ADK-19, ADK-20 |
| 18 | Artifacts — files that survive turns | ADK-21 |
| 19 | Context engineering I — what earns a place in the window | AG-08, AG-09 |
| 20 | Context engineering II — compaction & summarization | AG-10, ADK-22 |
| 21 | Error handling — surface, don't swallow (trap #4) | ADK-23, SEC-02 |
| 22 | Structured logging — every turn tells its story | OPS-04 |
| 23 | Testing agents I — unit tests for tools & callbacks | OPS-05, OPS-06 |
| 24 | Token accounting & budgets — denominated in quota (RPM/RPD), not dollars | OPS-07, AG-11 |

### Phase 4 — Agent Skills (Days 25–31)

| Day | Title | IDs closed |
| --- | --- | --- |
| 25 | Skills: the open spec — `SKILL.md` anatomy | SK-01, SK-02, SK-03 |
| 26 | `SkillToolset` — loading skills into ADK | SK-04, SK-05, ADK-24 |
| 27 | Authoring Sutra's first skills | SK-06, SK-07, SK-08 |
| 28 | Progressive disclosure & skill design | SK-09, SK-10, SK-11 |
| 29 | Sourcing & auditing third-party skills — provenance ledger; Agent Registry endpoint | SK-12, SK-13, SK-14, SK-15, SK-16 |
| 30 | Skill testing & versioning | SK-17, SK-18, SK-19 |
| 31 | Quality gate — `make check`: lint, tests, skills lint, `:free`-suffix lint | SK-20, OPS-08 |

### Phase 5 — MCP I: the protocol (Days 32–38)

| Day | Title | IDs closed |
| --- | --- | --- |
| 32 | MCP 2026 — the stateless core (headers, cacheable lists), governance & registry; the phone-call→web reframe | MCP-01, MCP-26, MCP-32 |
| 33 | The client side — connect Sutra to servers; transports (stdio + Streamable HTTP; SSE as 🅿️ legacy reading) | MCP-02, MCP-03 |
| 34 | Building `sutra-mcp` I — tools; stateless lifecycle (the old handshake as history) | MCP-04, MCP-05, MCP-06 |
| 35 | Resources & prompts | MCP-07, MCP-08, MCP-09 |
| 36 | Long jobs — progress, the Tasks extension (`tasks/get|update|cancel`), state as explicit payload handles | MCP-10, MCP-14, MCP-28 |
| 37 | Auth & enterprise — OAuth2 + RFC 9207 issuer validation + CIMD; elicitation (incl. URL-mode); extensions framework + EMA | MCP-13, MCP-27, MCP-30 |
| 38 | Failure & migration lab — timeouts, malformed servers; deprecated Roots/Sampling/Logging and the `InputRequiredResult` replacement | MCP-11, MCP-12, MCP-31 |

### Phase 6 — MCP II: production (Days 39–45)

| Day | Title | IDs closed |
| --- | --- | --- |
| 39 | Database tools — MCP Toolbox for Databases vs hand-written DB tools; 2.6 extras awareness | MCP-15, ADK-25, ADK-78 |
| 40 | Tool filtering, allowlists & MCP security posture | MCP-16, MCP-17, SEC-03 |
| 41 | Server capabilities & MCP Apps — sandboxed-iframe UIs, pre-declared templates | MCP-18, MCP-19, MCP-29 |
| 42 | Serving agents over MCP — `to_mcp_server`; agent-as-tool vs agent-as-peer | MCP-33, ADK-26 |
| 43 | Stateless by default — deploy-shaped servers; any instance answers any request | MCP-20, MCP-21 |
| 44 | Client hardening — retries, timeouts, no held connections | MCP-22, MCP-23 |
| 45 | Phase gate — full MCP audit of sutra-core | MCP-24, MCP-25, OPS-09 |

### Phase 7 — Memory & retrieval (Days 46–52)

| Day | Title | IDs closed |
| --- | --- | --- |
| 46 | Sessions vs memory — `MemoryService` semantics | ADK-27, ADK-28 |
| 47 | Persistent sessions — database-backed | ADK-29 |
| 48 | Memory design — what to remember, what to forget | AG-12, AG-13 |
| 49 | Retrieval & embeddings — one honest RAG day (local embedding index over the ticket archive) | AG-33, ADK-30 |
| 50 | Chunking, top-k & when RAG is the wrong tool | AG-14 |
| 51 | Caching — context & response caching as the quota lifeline | ADK-31, OPS-10 |
| 52 | Phase gate — memory wired into the triage flow | AG-15 |

### Phase 8 — Workflows & multi-agent (Days 53–59)

| Day | Title | IDs closed |
| --- | --- | --- |
| 53 | The graph Workflow Runtime — nodes, edges, the 2.x composition model (trap #1) | ADK-32, ADK-33, ADK-34 |
| 54 | Sequential, parallel & loop patterns | ADK-35, ADK-36, ADK-37 |
| 55 | Delegation & transfer; agent-as-tool | ADK-38, ADK-39, AG-16 |
| 56 | Planning patterns — plan-and-execute, replanning | AG-17, AG-18 |
| 57 | Multi-agent design — orchestrator, Writer↔Critic | AG-19, AG-20, ADK-40 |
| 58 | The triage graph v1 — intake→classify→research→draft→review, end to end | ADK-41, ADK-42 |
| 59 | Phase gate + failure lab — loops, runaway agents, containment | AG-21, SEC-04 |

### Phase 9 — Durability & humans (Days 60–65)

| Day | Title | IDs closed |
| --- | --- | --- |
| 60 | Durable execution — resume, replay, idempotency | AG-22, ADK-43 |
| 61 | Pause/resume & checkpoints in ADK | ADK-44, ADK-45 |
| 62 | Human-in-the-loop patterns | AG-23, ADK-46 |
| 63 | Approval gates — design (what needs a human, and why) | SEC-05, ADK-47 |
| 64 | Approval gates — build; **HITL resumption for standalone nodes + `NodeTool` (2.5)** | ADK-48, ADK-76 |
| 65 | Phase gate — kill it mid-run; durable triage with human approval | OPS-11 |

### Phase 10 — Safety & security (Days 66–72)

| Day | Title | IDs closed |
| --- | --- | --- |
| 66 | Threat model — prompt injection & the lethal trifecta | SEC-06, SEC-07 |
| 67 | Defense in depth — input/output guardrail callbacks | SEC-08, SEC-09 |
| 68 | Permissions & least privilege for tools | SEC-10, SEC-11 |
| 69 | PII & data boundaries — synthetic data only, free-tier training caveat | SEC-12, SEC-13 |
| 70 | The Quota-Router plugin — requests-remaining per provider per window; route to headroom | OPS-12, ADK-49 |
| 71 | Computer use & the sandbox — browser agent vs a local dummy site; `e2b`/`daytona` 🅿️; execution isolation in practice | AG-31, SEC-14, ADK-50 |
| 72 | Backoff with honesty — `retry-after`, 1→2→4→8s, escalate after N; never invent a result | SEC-15, OPS-13 |

### Phase 11 — Ambient & live (Days 73–78)

| Day | Title | IDs closed |
| --- | --- | --- |
| 73 | Ambient agents — the nightly job (re-index, full evals, digest) | AG-24, ADK-51 |
| 74 | Live API I — streaming architecture; free-quota check (SSE-text + browser speech fallback per Addendum 02) | ADK-52, ADK-53 |
| 75 | Live API II — the bidi voice loop | ADK-54, ADK-55 |
| 76 | **VAD events & non-blocking tools (2.5)** — the conversation doesn't freeze mid-tool | ADK-56, ADK-77 |
| 77 | The standup agent — voice client over the queue state | ADK-57, AG-25 |
| 78 | Phase gate — ambient + voice, inside free quota | OPS-14 |

### Phase 12 — Evals (Days 79–83)

| Day | Title | IDs closed |
| --- | --- | --- |
| 79 | Evals are tests — evalsets, metrics, Flash-Lite as the eval workhorse | AG-26, ADK-58, ADK-59 |
| 80 | Trajectory & rubric evaluation — **`RubricBasedMultiTurnTrajectoryEvaluator` (2.2)**; "escalated before any external write" as a rubric line | ADK-60, ADK-75 |
| 81 | LLM-as-judge & honest baselines | AG-27, ADK-61 |
| 82 | Regression discipline — evals in CI; full runs ride the Day 73 nightly | OPS-15, ADK-62 |
| 83 | Phase gate — Sutra's eval suite green | AG-28 |

### Phase 13 — Observability & deployment (Days 84–88)

| Day | Title | IDs closed |
| --- | --- | --- |
| 84 | Tracing — OTel + **`AutoTracingPlugin` (2.2)**: every node, tool call & model call in the trace tree | ADK-63, ADK-74, OPS-16 |
| 85 | The API surface — `api_server`, FastAPI endpoints | ADK-64, ADK-65 |
| 86 | Containerize — Cloud-Run-shaped locally: `docker compose`, stateless container, env-injected secrets, health checks | ADK-66, ADK-67, OPS-17 |
| 87 | Agent Engine — documented walkthrough (config written, not billed) 🅿️ | ADK-68 |
| 88 | Kubernetes on the laptop — kind/k3d, the MCP-sidecar pattern | ADK-69, OPS-18 |

### Phase 14 — Interop & launch (Days 89–93)

| Day | Title | IDs closed |
| --- | --- | --- |
| 89 | A2A v1.0 — signed Agent Cards verified hands-on; AP2 mandates, x402/TAP 🅿️ — *know the map, build only A2A* | AG-34, ADK-70 |
| 90 | Agent identity & the registry | AG-29, ADK-71 |
| 91 | Integrations survey — Slack-shaped intake, ecosystems; paid-only items noted "requires budget" 🅿️ | AG-30, ADK-72 |
| 92 | Hardening pass — full security review before going public | SEC-16 |
| 93 | Repo public — README, docs pass, demo script | — |

### Phase 15 — Capstone (Days 94–96)

| Day | Title | IDs closed |
| --- | --- | --- |
| 94 | Capstone I — the end-to-end scenario, run cold | — |
| 95 | Capstone II — demo recording script; interview drill over every ADR | — |
| 96 | Final gate — whole-system audit + retrospective; the habit continues | — |

> Days 93–96 close no new IDs by design: they are integration days. Their gate is the
> whole-system demo, and `TRACEABILITY.md` must show **zero open IDs** before Day 93 begins.

---

## 15 · 🚦 Phase Gates & the Freshness Check

A phase is **green** only when:

1. Every day in the phase has its row in `PROGRESS.md` with gates green.
2. `tools/trace.py` shows **no open IDs** from this or any earlier phase.
3. `make check` passes on the whole repo (tests, lints, evalsets at current scope).
4. The **freshness check** passes:
   - `google-adk` release notes since last gate — breaking change? → amend first.
   - **MCP spec revision changed? → re-read Addendum 01 Part 2** (standing rule).
   - All three providers' free limits re-checked; if a pinned model lost its free tier,
     amend the plan first (Addendum 02 rule).
   - Skills/registry ecosystem moved? → check SK provenance rows still valid.
5. Any deviation is recorded: ADR for structural changes, `CHANGELOG_PLAN.md` for plan text.

**Never** skip a day, merge two days, or reorder days without an ADR.

---

## 16 · 📒 Ledgers & Traceability

All ledgers live in `docs/days/` (kept where the repo actually has them):

| File | Nature | Rule |
| --- | --- | --- |
| `PROGRESS.md` | Append-only | One row per completed day; **the last row is where we are.** |
| `TRACEABILITY.md` | Regenerated | `tools/trace.py` scans day docs vs §14; open ID in a completed phase = bug. |
| `PACKAGES.md` | Append-only | Every install: package, version, date, day, why. No invented versions. |
| `SKILL_PROVENANCE.md` | Append-only | Every third-party skill: source, licence, audit date — before it runs. |
| `CHANGELOG_PLAN.md` | Append-only | Every amendment to this plan. |

Addendums are `docs/NN_MASTER_PLAN_ADDENDUM_*.md`; ADRs are `docs/adr/ADR-NNNN-*.md`.

---

## 17 · 📄 The Day Document Contract

Every day is one file, `docs/days/day_NNN.md` (zero-padded). The generator (Claude Code, per
`CLAUDE.md`) writes **only this file** — never project code. The human builds; the doc guides.

**Required sections, in order:**

1. **Header block** — day number, phase, title, date, IDs closed (exactly §14's list),
   estimated hours, packages touched.
2. **🎬 Where we are** — 3–6 sentences: what exists as of yesterday, told as story.
3. **🎯 Today's mission** — what Sutra can do tonight that it couldn't this morning; each ID
   named with a one-line promise.
4. **📚 Concepts** — one subsection per ID: simple explanation + concrete example (§18 rules).
   🅿️ IDs get map-level treatment and say so.
5. **🛠️ Build** — numbered steps with exact commands/code; **verify after every step** (what
   to run, what you must see). Any install: version verified live first, or a `TODO` with the
   exact lookup command. Any ADK API: the adk.dev page checked is named.
6. **💥 Failure lab** — break something on purpose; observe; explain. (Scene format, §18.)
7. **🎤 Interview corner** — 2–3 questions today prepared you to answer, with strong answers
   sketched.
8. **✅ Gates & ledger** — the definition-of-done checklist, then verbatim ledger snippets:
   the `PROGRESS.md` row · `PACKAGES.md` rows (if any) · `SKILL_PROVENANCE.md` rows (if any) ·
   and the git commit message (`day NNN: <title> — closes <IDs>`). **The doc ends with these.**

**Hard rules:** close exactly §14's IDs · never use 1.x patterns (§5.1) · zero-budget rules
(Addendum 02) bind every model mention · if reality disagrees with the plan, stop and amend
(Principle 14).

---

## 18 · ✍️ The Style Guide

1. **Simple language first.** Every concept: plain-words explanation → concrete example →
   only then terminology. If a 12-year-old couldn't follow the first sentence, rewrite it.
2. **The scene format** for failures and motivations:
   > 🎬 **The scene:** what you're doing. 😬 **The naive fix:** what everyone tries.
   > 💥 **Why it fails:** the mechanism. 💡 **The insight:** the principle that survives.
3. **Mental models get 💡 blocks** — one memorable sentence ("LiteLLM is a universal
   translator"; "old MCP is a phone call, new MCP is the web").
4. **Tables for enumerable facts**, prose for reasoning. Never a table of one row.
5. **Emoji section markers** as used throughout this plan — consistent, not decorative
   (🎬 🎯 📚 🛠️ 💥 🎤 ✅ 💡 🅿️ 📌 ⚠️ 🔒).
6. **🅿️ = parked**: awareness-level, interview-ready, deliberately not built.
7. **Interview corner is honest** — answers you could actually defend, tied to what was built,
   war stories with numbers preferred.
8. **No invented facts.** Versions, model names, quotas, API signatures: looked up and dated,
   or explicitly TODO'd with the lookup command. This style rule is Principle 7/8 wearing
   its writing hat.
9. **Every day ends the same way** — gates, ledger snippets, commit message. Ritual is the
   point: the repo is the memory.

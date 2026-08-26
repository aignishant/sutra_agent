---
plan: sutra
version: "v2.2.1"
supersedes: "v1.2.1-R"
curricula: 6
ids: 199
days: 97
phases: 16
doc_architecture: "hub + parts/ (see §17)"
amended: "2026-08-26"
---

# 🧵 MASTER PLAN v2.2.1 — Project **Sutra**
## Agentic AI Engineering with **Google ADK 2.x · MCP · Agent Skills · A2A**

> **Sutra** (Sanskrit सूत्र) means *thread* — the thread that strings concepts together, and the
> thread of execution that runs through a multi-agent system.
>
> 📌 **Purpose:** the single source of truth. Every later document points back here.
>
> **v2.0.0 is a documentation-architecture amendment.** No curriculum ID, no phase boundary, no
> gate, no model policy and no principle 1–15 changed. What changed is *how a day is written*:
> a day is now a **hub plus one document per subtopic** (§17), each written from zero prior
> knowledge through to production, with **no time estimate anywhere**. Day **0** is added in front
> of Day 1 and closes no IDs. The v1.2.1-R day documents are preserved at `legacy/days/` and are
> regenerated from Day 0 forward. See `docs/CHANGELOG_PLAN.md` and
> `docs/adr/ADR-0003-depth-contract.md`.
>
> ⚠️ **Provenance (unchanged, carried from v1.2.1-R):** the original `00_MASTER_PLAN.md` was lost
> before any day was generated. v1.2.1-R was reconstructed on **2026-08-13** from the surviving
> contract documents. Every day number and ID that appears in a surviving document is preserved
> exactly. See `docs/adr/ADR-0001-plan-reconstruction.md`. **If the original file resurfaces, diff
> it against this one and reconcile via an ADR before generating further days.**
>
> Where `02_ADDENDUM_ZERO_BUDGET_MODELS.md` conflicts with this plan on model choice or paid
> services, **the addendum wins** (its rule, kept). Where `01_MASTER_PLAN_ADDENDUM_GAPS.md`
> conflicts on MCP or the ADK 2.2–2.6 deltas, **the addendum wins**.

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
| 13 | 🗺️ The 16 Phases |
| 14 | 🗓️ The 97-Day Map (day → IDs closed) |
| 15 | 🚦 Phase Gates & the Freshness Check |
| 16 | 📒 Ledgers & Traceability |
| **17** | **📐 The Depth Contract — how a day is written** ⟵ *this is what changed in v2.0.0* |
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
16. **Depth over density.** A day is taught as a **hub plus one document per subtopic** (§17),
    never as one long page. If a subtopic cannot be read on its own, understood without scrolling
    past a different subtopic, and explained back out loud, it has not been split finely enough.
    A wall of text is not depth — it is depth's disguise.
17. **A day is a unit of subject, not a unit of time.** No document carries a time estimate, an
    "estimated hours" field, a "should take ~2 hours", or a suggested pace. A topic is finished
    when it is understood — one sitting or five. **Nothing is ever trimmed to fit a clock**; if a
    day is getting long, it gets another part, not a shorter explanation. The day number is an
    index into the subject, nothing more.
18. **Assume no prior knowledge, finish at production.** Every subtopic opens where a reader who
    has never met the idea can stand, defines its jargon on first use — *including jargon from
    earlier days, with a link back* — and does not stop at the toy example. It ends with how the
    idea is used in a real system: what a senior engineer writes instead of the teaching version,
    what breaks at scale or under concurrency, the review comment, the interview question. Strong
    basics and advanced technique are the same document, in that order.

> Principles 16–18 were added by v2.0.0 and are made concrete by **§17, the depth contract**.
> They are enforced mechanically by `scripts/depth_check.py` (`./m depth N`) and by reading.

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

**Repo layout (established Day 0, grown daily):**

```
sutra/
├── m                       # the driver script — ./m check | depth | start | done  (Day 0)
├── Makefile                # a two-line shim so `make check` still reaches ./m check
├── CLAUDE.md               # standing instructions for the driver agent (Day 0)
├── README.md               # what this is, and how a stranger runs it
├── .env                    # keys (never committed)          .gitignore (Day 0)
├── pyproject.toml          # uv-managed; every pin dated in docs/PACKAGES.md
├── uv.lock                 # the exact transitive tree; committed
│
├── days/                   # 📚 THE TEACHING — one folder per day
│   ├── README.md           #    how to read a day
│   └── day-NN-<slug>/      #    the number is the identity, the slug says what it teaches
│       ├── LESSON.md       #    the hub: story, part map, setup, build brief, eval, budget
│       ├── CHECKLIST.md    #    the definition of done; ./m done NN refuses until ticked
│       ├── parts/          #    one document per subtopic — the actual teaching
│       │   ├── 01-<slug>/1.1-<slug>.md …
│       │   └── 02-<slug>/2.1-<slug>.md …
│       └── lab/            #    the learner's own scratch code for that day
│
├── sutra/                  # the product package (agents, tools, graph) — you write every line
├── sutra_mcp/              # Sutra's MCP server(s)
├── skills/                 # Agent Skills (spec-compliant folders)
├── scripts/                # repo tooling: depth_check.py · tracker.py · trace.py
├── tests/                  # unit + eval harness
├── legacy/                 # the v1.2.1-R run, read-only (see legacy/README.md)
└── docs/
    ├── 00_MASTER_PLAN.md          # this file
    ├── NN_MASTER_PLAN_ADDENDUM_*.md
    ├── CURRICULUM_INDEX.md        # day ↔ ID cross-table
    ├── TRACKER.md                 # generated: what is written, at what depth
    ├── PROGRESS.md · TRACEABILITY.md · PACKAGES.md · SKILL_PROVENANCE.md · CHANGELOG_PLAN.md
    └── adr/                       # architecture decision records
```

> ⚠️ **Nothing under `sutra/`, `sutra_mcp/`, `skills/` or `tests/` is pre-written.** Every line of
> product code is printed in a day document and typed by the learner (`days/README.md`, rule 1).
> You cannot debug on Day 60 what you never typed on Day 8.

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
regenerated from the day hubs (`scripts/trace.py`); **any open ID from a completed phase is a bug.**

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
`./m check` (SK-20, Day 31). Every third-party skill gets a row in `SKILL_PROVENANCE.md`
(source URL, licence, audit date) before it runs.

---

## 11 · 📦 Curriculum E — Operations (OPS-01..18)

Repo bootstrap (OPS-01), **secrets discipline** (OPS-02 — `.env`, `.gitignore`, key handling),
ledger & traceability tooling (OPS-03), structured logging (OPS-04), testing agents (OPS-05..06),
token/quota accounting (OPS-07), the `./m check` gate (OPS-08), phase-gate audits (OPS-09,
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

## 13 · 🗺️ The 16 Phases

| Phase | Days | Theme | Gate flavor |
| --- | --- | --- | --- |
| **0** | **0** | **Foundry: the machine, the skeleton, the driver** | **`./m check` green; one commit; no secret in git** |
| 1 | 1–8 | Foundations: loop & first ADK agent | Hand-rolled loop + first pinned-model agent run |
| 2 | 9–16 | Models & tools | Four free providers benchmarked; built-in tools contained |
| 3 | 17–24 | State, context & discipline | State survives restarts; budgets enforced |
| 4 | 25–31 | Agent Skills | `./m check` green incl. skills lint + `:free` lint |
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

**Every phase gate includes the freshness check (§15).** Phase 0 has no freshness
check to run — nothing is pinned yet except the toolchain — but it does have a gate:
`./m check` green, one commit, and `git ls-files` free of any secret.

---

## 14 · 🗓️ The 97-Day Map (day → IDs closed)

> The authoritative day→ID assignment. Day documents close **exactly** these IDs — no more, no
> fewer. Amendments (Addendum 01 Part 5, Addendum 02 §5) are already folded in below.
> 🅿️ = parked/awareness-level treatment inside that day.
>
> **v2.0.0 added Day 0 and changed nothing else in this section.** Days 1–96, their titles and
> their IDs are unchanged from v1.2.1-R; the only edits are two tool renames that v2.0.0 made
> repo-wide (`tools/trace.py` → `scripts/trace.py`, `make check` → `./m check`).
>
> Day 0 closes **no IDs** by design: it is the machine, the skeleton
> and the driver script, which are preconditions for the curriculum rather than part of it. That
> is what keeps `TRACEABILITY.md` valid across the amendment — no ID moved, so no ID re-opened.

### Phase 0 — Foundry (Day 0)

| Day | Title | IDs closed |
| --- | --- | --- |
| 0 | Toolchain, skeleton and the `./m` driver — one owner for the environment, a repo that cannot leak a key, and a gate that refuses a half-finished day | — |

> Day 0 is the only day in the plan that closes no IDs, and the only day that installs no
> project dependency beyond the quality tools. Everything it builds (`.gitignore` before `.env`
> exists, `uv` owning the environment, `./m check`, `./m done`) is a precondition every later day
> assumes. Day 1 then does the Sutra-specific bootstrap — the ledgers, `scripts/trace.py`, the
> three free keys — and closes AG-01, OPS-01, OPS-02, OPS-03 exactly as before.

### Phase 1 — Foundations (Days 1–8)

| Day | Title | IDs closed |
| --- | --- | --- |
| 1 | Bootstrap & the map — repo, `.env`+`.gitignore`, uv+Python 3.12, ledgers & `scripts/trace.py`, the three free keys | AG-01, OPS-01, OPS-02, OPS-03 |
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
| 31 | Quality gate — `./m check`: lint, tests, skills lint, `:free`-suffix lint | SK-20, OPS-08 |

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

1. Every day in the phase has its row in `docs/PROGRESS.md` with gates green.
2. `scripts/trace.py` shows **no open IDs** from this or any earlier phase.
3. `./m check` passes on the whole repo — lints, tests, evalsets at current scope, **and the
   §17 depth contract for every written day** (`scripts/depth_check.py`).
4. Every day in the phase has a `parts/` directory. A day with no `parts/` is not written
   (§17.2), so a phase containing one cannot be green.
5. The **freshness check** passes:
   - `google-adk` release notes since last gate — breaking change? → amend first.
   - **MCP spec revision changed? → re-read Addendum 01 Part 2** (standing rule).
   - All three providers' free limits re-checked; if a pinned model lost its free tier,
     amend the plan first (Addendum 02 rule).
   - Skills/registry ecosystem moved? → check SK provenance rows still valid.
6. Any deviation is recorded: ADR for structural changes, `docs/CHANGELOG_PLAN.md` for plan text.

**Never** skip a day, merge two days, or reorder days without an ADR.

> A gate is never passed because time ran out (Principle 17). `./m done N` is gated on a ticked
> `CHECKLIST.md` and green checks, and on nothing else.

---

## 16 · 📒 Ledgers & Traceability

All ledgers live in `docs/`. *(v2.0.0 moved them up from `docs/days/`, because `docs/days/` no
longer exists — the days themselves moved to `days/day-NN/`. Nothing else about them changed.)*

| File | Nature | Rule |
| --- | --- | --- |
| `docs/PROGRESS.md` | Append-only | One row per completed day; **the last row is where we are.** |
| `docs/TRACEABILITY.md` | Regenerated | `scripts/trace.py` scans every `days/day-NN/LESSON.md` against §14; an open ID in a completed phase is a bug. |
| `docs/TRACKER.md` | Regenerated | `scripts/tracker.py` reports what is written, **how many parts each day has**, and what is still pending. A thin day is visible from this table alone. |
| `docs/PACKAGES.md` | Append-only | Every install: package, version, date, day, why. No invented versions (Principle 7). |
| `docs/PAPERS.md` | Append-only | Every paper a part cites: title, arXiv ID or DOI, URL, the date the record was checked, the parts citing it. No invented citations (§17.4.1 rule 5). |
| `docs/SKILL_PROVENANCE.md` | Append-only | Every third-party skill: source, licence, audit date — recorded **before** it runs. |
| `docs/CHANGELOG_PLAN.md` | Append-only | Every amendment to this plan (Principle 14). |
| `docs/CURRICULUM_INDEX.md` | Regenerated at gates | The day ↔ ID cross-table read out of §14, so the tracker has a single source for the day list. |

Addendums are `docs/NN_MASTER_PLAN_ADDENDUM_*.md`; ADRs are `docs/adr/ADR-NNNN-*.md`.
The v1.2.1-R ledgers are frozen at `legacy/ledgers/` and are never edited again.

**Two ledgers are regenerated and two are written by hand — do not confuse them.**
`TRACEABILITY.md` and `TRACKER.md` are outputs; editing them by hand only means the next `./m
check` silently overwrites you. `PROGRESS.md`, `PACKAGES.md`, `PAPERS.md`, `SKILL_PROVENANCE.md` and
`CHANGELOG_PLAN.md` are append-only history and are written by the day you are finishing — every
day document ends with the exact rows to paste (§17.6).

---

## 17 · 📐 The Depth Contract — how a day is written

> **Why this section exists.** v1.2.1-R taught each day as a single file, `docs/days/day_NNN.md`.
> By Phase 8 those files were carrying an entire subject — the graph Workflow Runtime, or the MCP
> stateless lifecycle — under one `##` heading, with an "estimated hours" field at the top telling
> the reader how fast to go past it. That is not depth. It is density wearing depth's coat, and a
> clock telling you to hurry.
>
> A reader cannot revisit *one* idea without re-reading four. There is no way to tell a
> thinly-covered subtopic from a missing one. And an "estimated hours" field silently authorises
> the worst edit in technical writing: cutting an explanation because the day is getting long.
>
> v2.0.0 replaces that format. A day is now **one hub plus one document per subtopic**, every
> document written from zero prior knowledge and carried through to how the idea is used in
> production. This section states exactly what "covered properly" means, so it can be reviewed by
> reading and partly checked by a script. It is Principles 16, 17 and 18, made concrete.

### 17.1 The three commitments

Everything below follows from three sentences.

**One idea per document.** A subtopic that cannot be read alone, understood without scrolling past
a different subtopic, and explained back out loud is not one subtopic — it is several, badly
stacked. If a document needs the word "also" to introduce its second half, it is two documents.

**No clocks.** Nothing in a day folder carries a time estimate, an "estimated hours" field, a
"this should take 90 minutes", or a suggested pace. A topic takes as long as it takes; the reader
may spend one sitting or five on a single part. **Content is never trimmed to fit a schedule**, and
a day is never declared finished because a duration elapsed. The day number is an index into the
subject, nothing more.

**Zero to production, in one document.** Each part starts where a reader who has never heard of the
idea can stand, and ends where a working professional stands: how the idea appears in a real
system, what a senior engineer does differently from the tutorial version, what fails at scale or
under concurrency, and what a reviewer or an interviewer will probe. Strong fundamentals and
advanced technique are not separate tracks — they are the beginning and the end of the same page.

### 17.2 The folder shape

Every day, without exception, is a folder of this shape:

```
days/day-NN-<day-slug>/
├── LESSON.md          # the hub — orientation, story, part map, build brief, eval, budget, ledger
├── CHECKLIST.md       # the definition of done; ./m done NN refuses to commit until ticked
├── parts/             # THE TEACHING — one document per subtopic
│   ├── 01-<slug>/     # section 1 — two digits, zero-padded, then what the section is about
│   │   ├── 1.1-<slug>.md
│   │   └── 1.2-<slug>.md
│   ├── 02-<slug>/     # section 2
│   │   ├── 2.1-<slug>.md
│   │   └── 2.2-<slug>.md
│   └── 03-<slug>/
│       └── 3.1-<slug>.md
├── papers/            # one document per paper the day's ideas came from (§17.4.2)
│   ├── 01-<paper-slug>.md
│   └── 02-<paper-slug>.md
└── lab/               # created by ./m scaffold NN; the learner's own scratch code
```

`parts/` is mandatory. **A day with no `parts/` directory is, by definition, not written** — the
tracker reports it as pending and the phase gate cannot go green.

**Every folder name carries its subject.** A number alone tells a reader nothing: `days/day-43/` and
`parts/02/` are addresses, not answers, and ninety-seven days of them are indistinguishable in a
file tree, a `git log` or an editor's tab bar. So the number is followed by a short kebab-case slug
naming what is inside — `days/day-01-bootstrap-and-map/`, `parts/03-keys-and-env/`. The rules:

| Folder | Shape | Slug comes from | Length |
| --- | --- | --- | --- |
| the day | `day-NN-<slug>` | the hub's `title` frontmatter, minus articles | 1–4 words |
| a section | `NN-<slug>` | the section's heading in the hub's §2 map | 1–3 words |

**The number is still the identity.** The slug is a label on it, never a key: every tool resolves a
day by its number and accepts whatever slug follows, so renaming a folder to a better slug can never
break `./m`, the depth check, the tracker or the traceability generator. Part *filenames* already
carry a full slug and do not change.

**Every part lives inside its section's folder**, named with two digits, zero-padded, then the slug:
section 1 is `parts/01-<slug>/`, section 12 is `parts/12-<slug>/`. A part document is never loose in
`parts/`. The folder number and the number before the dot in the filename must agree —
`parts/02-tools/2.3-<slug>.md` is correct; `parts/02-tools/3.1-<slug>.md` is a bug the depth check
rejects. The folders exist for navigation: a day with eighteen parts is a wall of filenames without
them, and a section is exactly the unit a reader wants to open at once.

### 17.3 The numbering rule — what `1.1` and `2.3` mean

Part numbers are **`<section>.<subtopic>`**, both scoped to the day.

- The **section** number groups subtopics that share one mental model. A section is usually one
  curriculum ID, one stage of a pipeline, or one phase of a mechanism.
- The **subtopic** number is the reading order inside that section. It starts at `1`, never `0`,
  and has no gaps.

The hub's §2 map declares what each section *is*. A typical two-ID day:

| Section | Means | Example subtopics |
| --- | --- | --- |
| **1.x** | the day's first ID | `1.1` what it is · `1.2` how it behaves · `1.3` where it bites |
| **2.x** | the day's second ID | `2.1` … `2.2` … |
| **3.x** | the synthesis — the two IDs meeting | `3.1` the trap only visible when both are true |

A protocol day (`MCP-04`, building a server) instead uses sections as *lifecycle stages*: `1.x` the
shape of a request, `2.x` the tool, `3.x` the failure surface, `4.x` the deploy-shaped version. A
setup day uses them as *tool, then artifact, then gate*. **The grouping must be stated in the
hub;** an unexplained numbering is a bug in the doc.

Paths are `parts/<NN>/<section>.<subtopic>-<kebab-slug>.md`, where `<NN>` is the section number
zero-padded to two digits. The slug says what the subtopic **teaches**, not where it sits:
`parts/02/2.3-gitignore-before-secrets-exist.md`, never `parts/02/2.3-part-three.md`.

**Links between parts are relative.** Inside one section a sibling is just its filename
(`1.2-<slug>.md`); across sections it goes up one level (`../01/1.5-<slug>.md`); the hub is
`../../LESSON.md`. Every `prev`/`next` in the frontmatter uses the same form. The hub's §2 map
links from the day folder: `parts/01/1.1-<slug>.md`.

### 17.4 What a part document must contain

Every file in `parts/` carries all twelve of these, **in this order**. Sections 2–12 are the
reader's path from "never heard of it" to "could defend this in a design review". Three of the
twelve are **conditional** — *The paper behind it*, *Line by line* and *The paper in one demo* — and
each row below says exactly when it applies. The other nine are unconditional.

| # | Section | The rule |
| --- | --- | --- |
| 1 | **frontmatter** | `day`, `part`, `title`, `ids`, `level`, `prerequisites`, `prev`, `next`, plus one of two paper keys where they apply: `papers` — the identifiers this part cites, `["arXiv:1706.03762"]`, required with section 6 — or, on a **paper part** (§17.4.2), `paper`, the single identifier it teaches. Machine-read; the reader ignores it. **No duration field of any kind** (Principle 17). |
| 2 | **One-line answer** | The subtopic's claim in a single sentence, before anything else. A reader who reads only this line has learned something true. |
| 3 | **The story** | A concrete scene before any abstraction: a person, a machine, a failure, a decision. Storytelling is not decoration here — it is the hook the definition hangs on. It comes **first**, in plain words, with **no jargon at all**. Four further rules, and the first is the one that gets broken (§18.1 rule 1a). **(a) A scene the reader has plausibly lived in**: a parcel and a courier, a repair-shop job card, a bus route map, a used car checked by a mechanic, a monthly generator test. Not a nautical chart, a model railway, a theatre programme or a projection booth. Test: could the reader have been standing in this scene themselves? If they must first be told what the setting *is*, the analogy is carrying the explanation instead of hooking it. **(b) Simple words**, short sentences; §18.1 rule 2 applies here hardest. **(c) Load-bearing**: the scene holds the actual failure or decision the part teaches, and every later section that reaches back for it must still fit. A metaphor abandoned after its own section was decoration. **(d) One metaphor family per day**: two parts reaching for the same setting read as one idea repeated, so the writer checks the day's other parts and the hub's §1 before choosing. |
| 4 | **The idea in plain language** | The concept itself, assuming the reader has never met it (Principle 18). Every term defined the first time it appears — **including terms from earlier days**, with a link to the part that introduced them, never an assumption of recall. No code. |
| 5 | **Why Sutra needs it** | The concrete later day that breaks without this. *"You meet this again on Day 43, where a stateless MCP server has to answer a request no instance has seen before"* is the shape. Never "this is important". |
| 6 | **The paper behind it** | **Conditional — present exactly when the idea has a public, citable origin document a reader could go and read**: a research paper, a numbered specification revision, a formal technical report. It is **an address, not an explanation** — the explanation is a part of its own (§17.4.2). Three things, briefly: the **citation block** (exact title · arXiv ID or DOI · year · URL — **no author names**, §18.1 rule 5); **one sentence** of what it claimed; and a **link to the paper part that teaches it**, which may be in this day or an earlier one. Nothing more — a reader who wants the origin follows the link, and a reader who wants the mechanism reads on. A part whose subject is a tool, a command, a repo convention or an SDK surface has no paper and does not carry this section. When it is present the part's frontmatter declares the same identifiers in `papers:`, each has a dated row in `docs/PAPERS.md`, and each resolves to a paper part on disk. |
| 7 | **The mechanism** | How it actually works: the runnable code, the protocol exchange written out, or the diagram. Nothing skipped as "obvious". Mermaid whenever the concept is spatial, sequential, or a state machine. |
| 8 | **Line by line** | Every non-obvious token of every code block, explained — and *why it is that line and not another*. Written as a `**Line by line:**` list **immediately after each code block**, so the reader never scrolls to find the explanation of what they are looking at. Blocks showing error output, a bare check command, or a diagram are exempt. **An unexplained line is a bug in the doc.** **Conditional**, like *The paper behind it* above and unlike every other section: a part that carries no code needing a walkthrough — a `concept` part, legitimately — does not carry this section, and `./m depth` does not ask for it. |
| 9 | **The paper in one demo** | **Conditional — paper parts only** (§17.4.2), i.e. exactly when the frontmatter declares `paper:`. A **small end-to-end project that implements the paper's contribution and nothing else**: the whole file tree, every file's contents, the one command that runs it, and the output it prints. *Nothing else* is the hard requirement and is meant literally — no framework, no web layer, no second feature, no niceties; if a file could be deleted and the claim still lands, delete it. It carries an **ablation switch** — one flag that turns the paper's idea off — and shows **both runs' output**, because a demo that cannot be switched off has demonstrated that code ran, not that this paper's idea did something. Zero-budget like everything else (Addendum 02): free tier or local, 429 handled. |
| 10 | **When it breaks** | The **real** error text, reproduced verbatim — the traceback, the HTTP status, the JSON-RPC error body. What it says, what it actually means, and the smallest fix. This is what the reader meets at 11pm; the happy path is not. |
| 11 | **In production** | Where this idea shows up in a real system and what changes there: the version a professional writes instead of the teaching version, what degrades at scale or under concurrency, the failure mode that only appears with real traffic, the review comment a senior engineer leaves, and the question an interviewer asks to find out whether you have actually used it. **This is the section that makes the document professional rather than introductory. It is not optional.** |
| 12 | **Check yourself** | One command the reader can run right now, plus one question they must answer **out loud** without scrolling up. |

Three further rules that have no section of their own:

- **The one-idea test.** If a part needs "also" to introduce its second half, split it.
- **The standalone test.** A part must be readable cold. If it depends on an earlier idea, **name
  that part and link it** — never assume the reader remembers Day 3 on Day 66.
- **The no-shortcut test.** "For now, just accept that" is banned unless it links forward to the
  part that explains it. **A deferred explanation must have an address.**

#### 17.4.1 Sutra's five additional part rules

These come from Principles 7, 8, 14 and 15 and apply on top of the twelve sections above:

1. **Never invent an API.** Any part that uses an ADK symbol names the **adk.dev page checked that
   day**, inline, next to the code: *"Verified against `adk.dev/docs/…` on YYYY-MM-DD."*
2. **Never invent a version.** Any part that installs something states the version it verified and
   how, or leaves a `TODO` containing **the exact lookup command**. The row lands in
   `docs/PACKAGES.md` the same day.
3. **Every model mention obeys Addendum 02.** Free tier only; the model string looked up live and
   dated; the call path handles HTTP 429 with `retry-after` and backoff.
4. **Name the trap.** Any part touching one of the four 1.x → 2.x traps (§5.1) says which one it is
   avoiding, in words. A reader who has been reading 1.x tutorials needs to be told, not protected.
5. **Never invent a citation.** This is Principle 7 pointed at the literature, and it matters more
   here than it does for a version pin: a wrong version number fails loudly the moment someone runs
   `uv sync`, while a plausible-looking arXiv ID that belongs to a different paper — or to no paper
   at all — can sit in a document for a year and be believed. So a citation is **looked up live on
   the day the part is written**, the title is copied from the record rather than from memory, and
   the ID lands in `docs/PAPERS.md` with the date it was checked. A paper that could not be verified
   gets a `TODO` containing **the exact lookup command**, exactly like an unverifiable version. **A
   remembered citation is an invented citation** — verify it or leave the TODO.

#### 17.4.2 The paper part — one document per paper, taught like any other

Row 6 gives the reader an address. **This is the document at it.**

A paper is an idea, and §17.1 says one idea gets one document. Folding a paper into a section of
the part that uses it breaks that rule twice over: the part now teaches two things, and the paper
gets whatever space is left after the mechanism — which is how a curriculum ends up citing a
document it never actually explains. So a paper that this curriculum leans on is taught **in a part
of its own**, written to the same contract as every other part.

**One document per paper.** The one-idea test applies unchanged: two papers are two documents,
however closely related. The filename is `NN-<paper-slug>.md` — two zero-padded digits giving the
reading order, then the paper's subject: `papers/01-attention-is-all-you-need.md`. Numbering starts
at `01` and has no gaps.

**It lives in `days/day-NN-<slug>/papers/`, beside `parts/` and not inside it.** The filename is
the reading order, then the paper's subject: `papers/01-subword-units.md`. Papers get their own
directory for the same reason `parts/` has one — a reader looking for *what this day teaches* and a
reader looking for *where these ideas came from* are on different errands, and a day's origins
should be one `ls` away rather than buried as the last numbered section of something else. It also
keeps the part numbering honest: a paper is not subtopic 7.3 of anything.

**Read them after the parts, not before.** The hub's map says so and the last part's *Next* points
at them. That order is **Principle 4 at the scale of a day**: hand-roll the mechanism, *then* read
the proposal. A reader who has just written the loop by hand can be told which half of the paper
they reinvented and which half the field dropped; a reader who meets the paper first has nothing to
hang it on, and the directory becomes a reading list they skip.

**It is written as a part, so it carries all twelve sections of §17.4, in order**, and the same
frontmatter minus `part` (a paper has no section number). Row 6 never fires on a paper document — it
does not cite a paper behind itself. It declares **`paper:` (singular)** instead: the one identifier
it teaches, and the key that makes **row 9, *The paper in one demo*, required**. Links run one level
up: a part is `../parts/01-<slug>/1.1-<slug>.md`, the hub is `../LESSON.md`, and a part links back
with `../../papers/01-<slug>.md`. What the sections mean here:

| Section | On a paper part |
| --- | --- |
| **The story** | The problem the field had **before this document existed** — a scene, in plain words, no jargon, no equations. Someone was stuck; this is what stuck looked like. |
| **The idea in plain language** | The claim, stated so that a reader who has never opened a paper can hold it and repeat it. Every term defined, including the ones the paper's own title uses. |
| **Why Sutra needs it** | The part of the day — linked — that runs on this idea, and the later day that leans on it again. |
| **The mechanism** | The method itself: the loop, the objective, the algorithm, the architecture. Written out, with the diagram, at the level of detail the rest of the day is written at. Not the abstract, paraphrased. |
| **Line by line** | Conditional as ever: present when the part carries a code block worth walking through — usually the paper's method reduced to the smallest runnable form. |
| **The paper in one demo** | The paper **made runnable, and stripped to nothing but itself**. A small end-to-end project — usually two or three files — whose only feature is this paper's contribution, given whole: the file tree, every file's contents, the command, the output. It is the difference between a reader who can recite the method and one who has watched it work on their own machine. |
| **When it breaks** | Where the claim **does not hold**: the conditions it assumed, the benchmark it was measured on, the scale it was never tried at, the follow-up work that narrowed it. A paper part with no limits section has taught a press release. |
| **In production** | **What survived and what did not** — which half of this document is in shipped systems today, which half the field quietly dropped, and what replaced the dropped half. This is the section that makes a paper part worth reading rather than citing. |
| **Check yourself** | One thing to run or find in the paper right now, and one question answered out loud: *what did this paper actually claim, and what do we do differently now?* |

**The demo is the section that is easiest to get wrong**, so it has four rules of its own:

1. **Only the paper's feature.** Not a small app that happens to use the idea — a small project
   whose *entire reason to exist* is the idea. The test is subtractive: if a file could be deleted
   and the claim still lands, delete it. No web layer, no config system, no second feature, no
   argument parser nobody needs. Two or three files is normal; ten is a different document.
2. **End to end, and actually runnable.** One command, stated. Its real output, pasted. A demo the
   reader cannot run is a listing, and a listing is what the *mechanism* section already gave them.
   **If the demo needs a live model and has not been run, the output block is a `TODO(me)` naming
   the exact command — never an invented transcript.** Principle 10 outranks the shape of the
   document here: a missing output is completed by one run and is obvious to everyone, while a
   fabricated one is undetectable and poisons the part it sits in.
3. **An ablation switch.** One flag, constant or environment variable that turns the paper's
   contribution **off**, with **both runs' output shown**. This is the rule that makes the demo
   honest: a demo that cannot be switched off has proved that some code ran, not that *this idea*
   changed the outcome. It is also, not coincidentally, an eval that can go RED (Principle 11).
4. **Zero-budget, like everything else** (Addendum 02). Free tier or local model, the model string
   looked up live and dated, HTTP 429 handled with `retry-after` and backoff. A demo that needs a
   billing account is not a demo this curriculum can carry.

The demo lands in the day's `lab/papers/<paper-slug>/`. It is **teaching material, not a rep**: it
is given complete, the way every other mechanism in a part is given complete. The unsolved
`TODO(me)` exercises stay where they belong, in the hub's build brief.

**A paper is taught once in the whole curriculum.** Ninety-seven days will cite the same handful of
documents repeatedly. The day that **first** needs a paper carries its part; every later day cites
it in row 6 and **links to that part**. Re-teaching it on Day 66 is exactly the duplication the
standalone test asks you to solve with a link rather than a copy.

**`level` is almost always `production`** on a paper part, because its *In production* section is
the whole point. A paper part written at `foundation` has usually stopped at the abstract.

### 17.5 What the hub (`LESSON.md`) must contain

The hub is **orientation and assembly, never the teaching itself**. It carries no `Line by line:`
walkthrough — that lives in the parts. Required, in this order:

1. **frontmatter** — `day`, `phase`, `phase_name`, `title`, `ids`, `principles`, `kind`,
   `plan_version`, `parts` (the count), `generated`, `status`, `lab_scaffolded`, `commit`.
2. **yesterday / today / tomorrow** — one line each, as a blockquote. No time estimate.
3. **`## §1 Where we are`** — the day's whole idea as a scene and an analogy, in plain language,
   before any code and before any jargon. This is v1's *🎬 Where we are* and *🎯 Today's mission*,
   merged and told as a story.
4. **`## §2 The map`** — a table of every part: number, linked title (`parts/01/1.1-<slug>.md`),
   what it answers, and its `level`. Grouped by section, with **one line saying what each section
   means for this day**. **No minutes column, ever.**
5. **`## §3 Setup — run this`** — every `mkdir`, `touch`, `uv add <pkg>==<exact>` the day needs,
   pinned, with the version verified that day.
6. **`## §4 Build brief`** — the files to create, with `TODO(me)` markers left **unsolved**.
7. **`## §5 The eval that must be able to fail`** — the check that is RED before the TODOs are done
   (Principle 11: evals are tests).
8. **`## §6 Request budget`** — model calls, per provider, in RPM/RPD (Principle 15 · Addendum 02).
   `0` is an answer; state it.
9. **`## §7 Traps`** — the mistakes that eat an evening, including the named 1.x → 2.x trap if the
   day touches one.
10. **`## §8 Verify before you code`** — the live documentation URLs actually fetched on the day of
    writing: adk.dev pages, the MCP spec revision, the provider free-tier page (Principle 8).
11. **`## §9 Say it in an interview`** — one paragraph, spoken voice, honest, tied to what was
    built. War stories with numbers beat adjectives.
12. **`## §10 Done when`** — pointer to `CHECKLIST.md`. Defined by understanding and green checks,
    **never by elapsed time**.
13. **`## §11 Ledger & commit`** — the verbatim snippets that end every day: the `PROGRESS.md` row,
    any `PACKAGES.md` rows, any `PAPERS.md` rows, any `SKILL_PROVENANCE.md` rows, and the git commit
    message `day NN: <title> — closes <IDs>`. **The hub ends with these.** *(Ritual is the point: the repo
    is the memory, not the chat.)*

### 17.6 The `level` field — how a day climbs

Every part declares exactly one `level`, and a well-built day climbs through them in order:

| `level` | The reader at the end of this part |
| --- | --- |
| `foundation` | Knows what the thing *is* and could define it to someone else without using the word itself. |
| `working` | Can use it correctly on their own problem, and recognises its error messages on sight. |
| `production` | Knows what changes when it runs in a real system — scale, concurrency, quota, failure, review — and can defend the choice. |

A day that is all `foundation` is a tutorial. A day that opens at `production` has skipped the
reader. Most days run `foundation → working → production`; a single part may itself climb, which is
exactly what its *In production* section is for.

### 17.7 How finely to split

Split by **idea boundaries, never by length or by pace**. A part is finished when its one idea is
fully explained — *including its production face* — and not before.

| Day kind | Split by |
| --- | --- |
| `setup` | one tool, one file, or one command per part |
| `lab` (1 ID) | mechanism → behaviour → edge case → failure mode → production use |
| `lab` (2–3 IDs) | one section per ID, plus a synthesis section where they meet |
| `concept` | one claim per part, each with its evidence |
| `gate` | one acceptance criterion per part |
| `capstone` | one component per part, in build order |
| **any day whose ideas came from papers** | **one part per paper, in the day's last section** (§17.4.2) — added to whatever the row above gives you, never replacing it |

There is deliberately **no target part count and no target length**. If a subject needs four parts
it gets four; if it needs twenty-two it gets twenty-two, and the day simply spans more sittings
(Principle 17). The only wrong answers are a part that carries two ideas and a part that stops
before production.

**Every day carries at least one part whose subject is a deliberate failure.** v1's *💥 Failure
lab* does not disappear in this format — it is promoted from a section at the bottom of a long page
to a part of its own, usually at `production` level, where breaking the thing on purpose is the
whole point of the document.

### 17.8 What "in depth" is not

The failure modes v2.0.0 exists to prevent, stated so they can be caught in review:

- **Splitting without deepening.** Cutting one 30 000-character page into six 5 000-character pages
  changes nothing. Each part must **gain** the story, the mechanism, the failure text, the
  production face and the check it never had.
- **Summary in place of explanation.** *"This line configures the runner"* is a caption. *"The
  `app_name` you pass is what keys the session store, so changing it orphans every existing session
  — try it and watch the history vanish"* is an explanation.
- **Stopping at the toy example.** A part that shows the idea working on one ticket and never says
  what happens at ten thousand has taught half the subject. Section 9 is where the other half
  lives.
- **Assuming the previous day.** Each part names its prerequisite and links it. Ninety-seven days
  is long enough that Day 3 is genuinely forgotten by Day 66.
- **Code without failure.** Every mechanism has a matching *When it breaks* with the **actual**
  error string, because that string is what the reader will meet at 11pm.
- **Trimming to fit.** Cutting an explanation because the day "is getting long" is the one edit
  this format forbids outright (Principle 17). **Split it into another part instead.**
- **Solved reps.** `TODO(me)` stays `TODO(me)`. Depth is in the explanation, never in doing the
  learner's exercise for them.
- **Carrying a legacy clock across.** Every v1.2.1-R day header has an "estimated hours" field.
  Mining a legacy day means taking its correctness, not its clock.

### 17.9 Enforcement

`scripts/depth_check.py`, run as `./m depth [NN]`, is the machine-readable half of this contract.
It fails on:

- a missing `parts/` directory;
- a part loose in `parts/` instead of inside a section folder;
- a paper document outside `papers/`, or one whose filename is not `NN-<paper-slug>.md`, or a gap in
  the papers numbering;
- a section folder that is not two zero-padded digits;
- a part whose section folder disagrees with the number in its filename;
- a filename that does not match `<section>.<subtopic>-<slug>.md`;
- a gap in the section or subtopic numbering;
- any of the twelve required part sections missing or out of contract order (with the three
  conditional exceptions in §17.4: *Line by line* is required exactly when the part holds a code
  block that needs one, *The paper behind it* exactly when the frontmatter declares `papers`, and
  *The paper in one demo* exactly when it declares `paper`);
- a part that declares `papers` and carries no *The paper behind it* section, or carries the
  section and declares no `papers` — the pair must agree;
- a cited identifier with no **paper part** teaching it anywhere under `days/`, or a citing part
  whose row 6 does not **link** that part (§17.4.2: an address resolving to nothing is the
  no-shortcut test failing);
- a paper part that declares no `paper:` identifier, or two paper parts declaring the same one — a
  paper is taught once in the whole curriculum;
- a cited or taught identifier with no row in `docs/PAPERS.md`, or one whose shape is not a real
  arXiv ID or DOI (Principle 7 applied to the literature, §17.4.1 rule 5);
- a code block with no `Line by line:` walkthrough following it;
- a `level` outside `foundation` · `working` · `production`;
- **any time estimate anywhere in a day folder** (Principle 17);
- a hub that carries teaching, or whose §2 map does not link every part **and every paper** on
  disk;
- a `parts:` frontmatter count that disagrees with the directory;
- a missing `CHECKLIST.md`.

What it **cannot** check is whether an explanation is any good. That is what §17.8 is for, and it
is reviewed by reading. `docs/TRACKER.md` reports the part count of every written day, so a thin
day is visible from the progress table alone.

`scripts/trace.py` remains the ID-level check: it reads each `days/day-NN-<slug>/LESSON.md` against §14
and regenerates `docs/TRACEABILITY.md`. **An open ID in a completed phase is a bug.**

### 17.10 Amendment record

| Version | Change |
| --- | --- |
| v1.0 → v1.2 | The original plan and its two addenda: MCP 2026-07-28, AG-31..34, ADK-73..78, the zero-budget model policy. |
| v1.2.1-R | Reconstructed after the original file was lost (ADR-0001). 96 days, 15 phases, 199 IDs. One `docs/days/day_NNN.md` per day. |
| **v2.0.0** | **Documentation architecture only. No ID, phase boundary, gate, model policy or principle 1–15 changed.** Adds Principles 16–18, this §17, the `days/day-NN/parts/<NN>/` shape, the ten-section part contract with a mandatory *In production* section, the eleven-section hub, the `level` ladder, the removal of every time estimate, the `./m` driver, `scripts/depth_check.py` and `scripts/tracker.py`. Adds **Day 0** (closes no IDs) in front of Day 1. Moves the ledgers from `docs/days/` to `docs/`. The v1.2.1-R days are preserved read-only at `legacy/days/` and regenerated from Day 0 forward. |
| **v2.2.0** | **One conditional part section and one new kind of part. No ID, phase, gate, model policy, principle or folder rule changed.** §17.4 adds **row 6, *The paper behind it***, carried by a part exactly when its idea has a public citable origin document — the citation, one sentence of the claim, and a **link**. §17.4.2 adds **the paper document**: the paper itself is taught in a document of its own, one per paper, in the day's own **`papers/` directory** beside `parts/`, read after them, to the same contract, where *In production* means **what survived and what did not** and new row 9, ***The paper in one demo***, gives the paper as a small end-to-end project implementing its contribution and nothing else, with an **ablation switch** that turns the idea off so both outputs can be compared. Papers come last because that is Principle 4 at the scale of a day — build the mechanism, then read the proposal. A paper is taught **once** in the curriculum; later days link to it. §17.4.1 adds rule 5, *never invent a citation*, sending every identifier to the new `docs/PAPERS.md` ledger with the date it was verified. §18.1 rule 5 is unchanged in force: a paper is cited by title and identifier, **never by its authors**. Days 0–5 retrofitted in place. See ADR-0008. |
| **v2.2.1** | **Style only. No ID, phase, gate, model policy, principle, folder rule or required section changed, and no day needs rewriting to remain compliant.** §17.4 row 3 and §18.1 rules 1a and 2 sharpen what *The story* must be, after a reading of Days 0–5 found the sections technically compliant and landing badly: the scene must be **one the reader has plausibly lived in** rather than one they must first have explained to them, it must be **load-bearing** rather than decorative, and **one metaphor family serves one part per day** — Day 5 had reached for a restaurant twice and a receptionist twice. §18.1 rule 2 additionally makes **grammar and punctuation part of the deliverable in every section**, not the story alone, because the reader of this curriculum is reading in a second language and learns from these documents alone. Day 5 parts 4.1–7.1 rewritten under the new rule; Days 0–4 are compliant as written and were not touched. No ADR: this sharpens an existing row rather than adding a section or a kind of document. |
| **v2.1.0** | **Folder naming only. Nothing about the teaching contract changed.** §17.2 now requires every day and section folder to carry a kebab-case slug after its number — `days/day-NN-<slug>/`, `parts/NN-<slug>/` — so a file tree says what a day teaches without opening it. The number remains the identity: every tool resolves a day by number and tolerates any slug. Days 0 and 1 renamed in place. See ADR-0004. |

---

## 18 · ✍️ The Style Guide

§17 says what a day must *contain*. This section says how it must *read*. Both are enforced by
review; the mechanical half is `./m depth`.

### 18.1 The register

1. **Storytelling is the default, not a flourish.** A scene before an abstraction, every time. The
   story section of a part carries **no jargon at all** — a person, a machine, an afternoon lost.
   The definition then hangs on that hook. A reader remembers the engineer who lost a Monday to
   four Pythons long after they have forgotten the phrase "virtual environment".
   **1a. The scene must be one the reader has plausibly lived in.** A parcel and a courier, a
   repair-shop job card, a bus route map, a used car checked by a mechanic, a monthly generator
   test. **Not** a nautical chart, a model railway, a theatre programme, a projection booth or a
   historical disaster. A setting the reader must first have explained to them is a second thing to
   learn, placed in front of the thing they came to learn, and it costs exactly the attention the
   hook was supposed to buy. The scene must also be **load-bearing** — it holds the failure or the
   decision the part teaches, and it still fits wherever a later section reaches back for it — and
   **one metaphor family serves one part per day**, because two of them read as one idea repeated
   (§17.4 row 3).
2. **Simple language first.** Every concept: plain words → concrete example → *only then* the
   terminology. If a twelve-year-old could not follow the first sentence, rewrite the first
   sentence. This is not dumbing down; it is putting the definition after the thing it defines.
   **Grammar and punctuation are part of this rule and are part of the deliverable**, in every
   section of every document rather than in the story alone: full stops and commas where they
   belong, no run-on sentences, and no long chain of em-dashes where two ordinary sentences would
   read better. The reader of this curriculum is reading in a second language and learns from these
   documents alone. A sentence they have to parse twice has failed, however correct its content.
3. **Define every term on first use — including your own terms from earlier days.** Ninety-seven
   days is long enough that Day 3 is genuinely forgotten by Day 66. Link the part that introduced
   it (§17.4, the standalone test). "As we saw earlier" is not a link.
4. **Second person, present tense, active voice.** "You type `uv run`, and uv checks the lockfile
   first." Not "the lockfile is then checked".
5. **No person names, no course or creator brand names.** This curriculum is self-contained and
   promotes nobody: never name an instructor, author, channel, academy, bootcamp or training
   company — in a lesson, a checklist, a docstring or a commit message. Naming the **tools** you
   actually use is required and unaffected (ADK, MCP, Gemini, Groq, uv, ruff…), as is citing a
   specification by its revision date and a library by its official docs URL. **A paper is cited
   the same way** — by its exact title and its arXiv ID or DOI (§17.4 row 6), never by its authors.
   That is not a gap in the attribution: the identifier is the unambiguous handle, and it is the one
   a reader types to find the work.

### 18.2 The scene format

For failures and motivations, use the four-beat scene. It survives from v1.2.1-R unchanged, and it
is what a part's *The story* and *When it breaks* sections are built from:

> 🎬 **The scene:** what you are doing.
> 😬 **The naive fix:** what everyone tries.
> 💥 **Why it fails:** the mechanism — not the symptom.
> 💡 **The insight:** the principle that survives after the details are forgotten.

### 18.3 Code and commands

6. **Every command is given in full.** `mkdir -p`, `touch`, `uv add pkg==1.2.3`, the run command,
   the check command. A reader should never have to infer "and now presumably I create a folder".
7. **Every code block is followed by `**Line by line:**`** — every non-obvious token, and *why it is
   that line and not another*. Not a summary. **An unexplained line is a bug in the doc.** Blocks
   that are pure error output, a bare check command, or a Mermaid diagram are exempt.
8. **Every mechanism has a matching failure with the real error text**, reproduced verbatim.
   Paraphrasing a traceback is worse than omitting it — the reader searches for the string.
9. **`TODO(me)` stays unsolved.** The doc teaches; it never does the reps. Depth lives in the
   explanation, never in handing over the answer.
10. **Mermaid whenever the concept is spatial, sequential, or a state machine.** A graph runtime, a
    protocol handshake, a retry ladder and an approval gate all earn a diagram.

### 18.4 Facts

11. **No invented facts.** Versions, model names, quotas, API signatures, spec revisions: looked up
    live and dated, or explicitly `TODO`'d **with the exact lookup command**. This is Principles 7
    and 8 wearing their writing hat, and §17.4.1 makes it a per-part rule.
12. **Tables for enumerable facts, prose for reasoning.** Never a table of one row.
13. **Emoji section markers as used throughout this plan** — consistent, not decorative:
    🎬 🎯 📚 🛠️ 💥 🎤 ✅ 💡 🅿️ 📌 ⚠️ 🔒 📐.
14. **🅿️ = parked**: awareness-level, interview-ready, deliberately not built. A parked ID still
    gets a part with a story and a production section; what it does not get is a build step.
15. **The interview paragraph is honest.** An answer you could actually defend, tied to what you
    built. A war story with numbers beats an adjective.

### 18.5 The two things that are never written

16. **Never a clock.** Not "estimated hours", not "this takes an evening", not "quick", not "a
    short detour". `./m depth` fails the day on any of them (Principle 17).
17. **Never a trim.** If the day is getting long, it gets another part (§17.7). Cutting an
    explanation to fit is the one edit this format forbids outright.

### 18.6 The ritual

18. **Every day ends the same way** — the checklist, then the ledger snippets, then the commit
    message `day NN: <title> — closes <IDs>`. The sameness is the point: the repo is the memory,
    not the chat, and a stranger — or a different CLI agent six months from now — has to be able to
    pick up from the last row of `docs/PROGRESS.md` alone.

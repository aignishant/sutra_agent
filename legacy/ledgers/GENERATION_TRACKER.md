# Batch Generation Tracker (meta-file — NOT a plan ledger)

> Purpose: the user requested (2026-08-18) that ALL remaining day docs (Days 5–96) be
> pre-generated in one batch before their vacation. This file tracks that batch so any
> future session can resume exactly where the last one stopped. Delete this file once
> the batch is complete and reviewed, if desired.
>
> ⚠️ Honesty note (Principle 8/14): the Day Document Contract says APIs/versions are
> verified "on the day". Batch generation verifies them as of **2026-08-18** instead.
> Every pre-generated doc therefore carries a banner telling the human to re-run the
> freshness checks before running that day. This deviation was explicitly requested by
> the project owner and is recorded here rather than silently absorbed.

## Rules for the generating session
- Write ONLY `docs/days/day_NNN.md` files + this tracker. Never touch project code,
  PROGRESS.md, TRACEABILITY.md, PACKAGES.md, or the plan files.
- Day 4 doc already exists (written 2026-08-14, not yet run/committed by the human).
- Contract §17 + Style §18 + teaching-style memory bind every doc. day_004.md is the
  quality bar (story-first concepts, line-by-line commented code, scene-format failure
  labs, ledger snippets at the end).
- Model pins as of 2026-08-18: primary `gemini-3.5-flash`, lite `gemini-3.5-flash-lite`
  (repinned 2026-08-13, see CHANGELOG_PLAN.md; observed 5 RPM). google-genai 2.18.0.
  google-adk baseline 2.6.3 — re-verify live on PyPI in the Day 5 doc.
- Cumulative trace counts: Day 4 ends at 7/199. Each doc states its expected
  `python tools\trace.py` count in its gate step.
- ⚠️ **Header marker (fixed 2026-08-19, Wave 4 session):** `tools/trace.py` finds a doc's
  IDs by the literal text `IDs closed:` — *with the colon*. Days 5–65 were written as
  `**IDs closed**` and every one would have reported "🐛 green day, ID missing from doc"
  at its gate; all 61 rows were corrected in place (one-line change each, verified with
  `doc_claims()` == plan for every day). Every new doc's header row MUST read
  `| **IDs closed:** | … |`.

## Wave 4 canon (prescribed 2026-08-19 so Phases 10/11/12 forks agree; writers flesh out)
- Trace counts: 65 → 145 · 66 → 147 · 67 → 149 · 68 → 151 · 69 → 153 · 70 → 155 ·
  71 → 158 · 72 → 160 · 73 → 162 · 74 → 164 · 75 → 166 · 76 → 168 · 77 → 170 ·
  78 → 171 · 79 → 174 · 80 → 176 · 81 → 178 · 82 → 180 · 83 → 181.
- Phase 10 files: `sutra/guardrails.py` (Day 67 input/output callbacks; Day 66's
  injection fixtures under `tests/fixtures/injection/`), `sutra/permissions.py` (Day 68
  per-tool least-privilege table, joins Day 62's POLICY), `sutra/quota_router.py` (Day 70,
  consumes `QuotaLedger` + supersedes `QuotaWatcherPlugin`/`QuotaBreakerPlugin`),
  `sutra/browser_lab.py` + `tools/dummy_site/` (Day 71, local dummy vendor-status site),
  `sutra/backoff.py` (Day 72: `RetryPolicy`, `with_backoff`; `SafetyNetPlugin` in
  `sutra/errors.py` upgraded to honest backoff) + `docs/runbooks/rate_limit_429.md`.
- Phase 11 files: `sutra/nightly.py` (Day 73: a `JOBS` registry — `reindex` (Day 49
  index), `evals` (a named hook that Day 82 fills with `tests/evals/run_evals.py`), `digest`
  → `data/digests/YYYY-MM-DD.md`; runs via `python -m sutra.nightly run`; scheduled with
  Windows Task Scheduler / cron, quota-paced through the Quota-Router), `sutra/live_lab.py`
  (Days 74–76), `sutra/standup.py` + `sutra/standup_client.html` (Day 77; SSE-text +
  browser speech fallback is the primary demo, Live API briefly inside quota).
- Phase 12 files: `tests/evals/` (`triage.evalset.json` 10–15 dev cases, `full/` 60+ for
  gates, `test_config.json`), `tests/evals/run_evals.py` (Day 82; CI runs the dev set,
  nightly runs full), `.github/workflows/check.yml` (Day 82: `python tools/check.py` +
  dev evalset; quota-spending steps are `workflow_dispatch`/nightly only). Eval model:
  `gemini-3.5-flash-lite`.

## Wave 5 canon (prescribed 2026-08-19 so Phases 13/14/15 forks agree; writers flesh out)
- Trace counts: 83 → 181 · 84 → 184 · 85 → 186 · 86 → 189 · 87 → 190 · 88 → 192 ·
  89 → 194 · 90 → 196 · 91 → 198 · 92 → **199** · 93–96 → 199 (no new IDs; gate =
  whole-system demo; TRACEABILITY must show zero open IDs before Day 93 begins).
- Phase 13 files: `sutra/tracing.py` (Day 84: `AutoTracingPlugin` registered on the
  runner/App + an OTel exporter — console exporter by default, optional local Jaeger
  via `docker run jaegertracing/all-in-one`; plugin order becomes Tracing → DataBoundary
  → QuotaRouter → Permission → Guardrail), `sutra/api.py` (Day 85: `get_fast_api_app(...)`
  / `adk api_server` wrapping the triage graph; `/healthz` + `/readyz`; the ambient
  trigger endpoint from Day 73 lives here now), `Dockerfile` + `docker-compose.yml` +
  `.dockerignore` (Day 86: stateless `sutra-api` container, env-injected secrets,
  healthcheck, `sutra-mcp` as a second service, `data/` volume), `deploy/agent_engine/`
  (Day 87: config + README, documented-not-billed 🅿️), `deploy/k8s/` (Day 88: kind or k3d
  manifests — Deployment with `sutra-mcp` sidecar, Service, ConfigMap, Secret-from-env,
  readiness probes).
- Phase 14 files: `sutra/a2a_peer.py` + `docs/A2A.md` (Day 89: A2A v1.0 signed Agent
  Card verified hands-on against a local peer; AP2/x402/TAP 🅿️ sections),
  `sutra/identity.py` + `docs/REGISTRY.md` (Day 90: agent identity + registry; ADK
  `agent-identity` extra evaluated 🅿️ if it needs a paid account), `docs/INTEGRATIONS.md`
  (Day 91: Slack-shaped intake survey, `slack` extra, paid items marked "requires
  budget"), `docs/SECURITY_REVIEW.md` (Day 92: SEC-16 — full pre-publication review:
  secrets scan, THREAT_MODEL + DATA_BOUNDARY re-read, dependency audit, MCP audit, CORS
  tightening promised by Day 86), `README.md` rewrite + `docs/DEMO.md` (Day 93: repo goes
  public — checklist + `git log` secrets sweep + licence file).
- Phase 15 files: `docs/runbooks/capstone.md` (Day 94: the cold end-to-end scenario
  script), `docs/DEMO_SCRIPT.md` + `docs/INTERVIEW_DRILL.md` (Day 95: recording script;
  drill over every ADR in `docs/adr/`), `docs/RETROSPECTIVE.md` (Day 96: whole-system
  audit + retrospective + "the habit continues" weekly freshness checklist).

## ✅ Batch complete (2026-08-20)
All 96 day docs are written (Days 5–96 generated in this batch; Days 1–4 pre-existed).
Nothing is pending. The batch this file tracked is finished — per the header note, delete
or archive this file once the docs have been reviewed.
Standing reminders that outlive the batch: every pre-generated doc carries the
re-run-the-freshness-checks banner (the doc was verified as of its generation date, not
your run date), and the header marker must stay `**IDs closed:**` with the colon or
`tools/trace.py` misses the IDs. Days 93–96 close no IDs and write
`| **IDs closed:** | — (integration day; §14 assigns none) |`.

## Wave plan (3 phases per wave, forks in parallel; waves sequential)
- Wave 1: Phase 1-rest (5–8) · Phase 2 (9–16) · Phase 3 (17–24)
- Wave 2: Phase 4 (25–31) · Phase 5 (32–38) · Phase 6 (39–45)
- Wave 3: Phase 7 (46–52) · Phase 8 (53–59) · Phase 9 (60–65)
- Wave 4: Phase 10 (66–72) · Phase 11 (73–78) · Phase 12 (79–83)
- Wave 5: Phase 13 (84–88) · Phase 14 (89–93) · Phase 15 (94–96)

## Status (⬜ pending · 🔄 generating · ✅ written)
| Day | Phase | Status | | Day | Phase | Status | | Day | Phase | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 1 | ✅ 08-18 | | 36 | 5 | ✅ 08-19 | | 67 | 10 | ✅ 08-19 |
| 6 | 1 | ✅ 08-18 | | 37 | 5 | ✅ 08-19 | | 68 | 10 | ✅ 08-19 |
| 7 | 1 | ✅ 08-18 | | 38 | 5 | ✅ 08-19 | | 69 | 10 | ✅ 08-19 |
| 8 | 1 | ✅ 08-18 | | 39 | 6 | ✅ 08-18 | | 70 | 10 | ✅ 08-19 |
| 9 | 2 | ✅ 08-18 | | 40 | 6 | ✅ 08-19 | | 71 | 10 | ✅ 08-19 |
| 10 | 2 | ✅ 08-18 | | 41 | 6 | ✅ 08-19 | | 72 | 10 | ✅ 08-19 |
| 11 | 2 | ✅ 08-18 | | 42 | 6 | ✅ 08-19 | | 73 | 11 | ✅ 08-19 |
| 12 | 2 | ✅ 08-18 | | 43 | 6 | ✅ 08-19 | | 74 | 11 | ✅ 08-19 |
| 13 | 2 | ✅ 08-18 | | 44 | 6 | ✅ 08-19 | | 75 | 11 | ✅ 08-19 |
| 14 | 2 | ✅ 08-18 | | 45 | 6 | ✅ 08-19 | | 76 | 11 | ✅ 08-19 |
| 15 | 2 | ✅ 08-18 | | 46 | 7 | ✅ 08-19 | | 77 | 11 | ✅ 08-19 |
| 16 | 2 | ✅ 08-18 | | 47 | 7 | ✅ 08-19 | | 78 | 11 | ✅ 08-19 |
| 17 | 3 | ✅ 08-18 | | 48 | 7 | ✅ 08-19 | | 79 | 12 | ✅ 08-19 |
| 18 | 3 | ✅ 08-18 | | 49 | 7 | ✅ 08-19 | | 80 | 12 | ✅ 08-19 |
| 19 | 3 | ✅ 08-18 | | 50 | 7 | ✅ 08-19 | | 81 | 12 | ✅ 08-19 |
| 20 | 3 | ✅ 08-18 | | 51 | 7 | ✅ 08-19 | | 82 | 12 | ✅ 08-19 |
| 21 | 3 | ✅ 08-18 | | 52 | 7 | ✅ 08-19 | | 83 | 12 | ✅ 08-19 |
| 22 | 3 | ✅ 08-18 | | 53 | 8 | ✅ 08-19 | | 84 | 13 | ✅ 08-20 |
| 23 | 3 | ✅ 08-18 | | 54 | 8 | ✅ 08-19 | | 85 | 13 | ✅ 08-20 |
| 24 | 3 | ✅ 08-18 | | 55 | 8 | ✅ 08-19 | | 86 | 13 | ✅ 08-20 |
| 25 | 4 | ✅ 08-18 | | 56 | 8 | ✅ 08-19 | | 87 | 13 | ✅ 08-20 |
| 26 | 4 | ✅ 08-18 | | 57 | 8 | ✅ 08-19 | | 88 | 13 | ✅ 08-20 |
| 27 | 4 | ✅ 08-18 | | 58 | 8 | ✅ 08-19 | | 89 | 14 | ✅ 08-20 |
| 28 | 4 | ✅ 08-18 | | 59 | 8 | ✅ 08-19 | | 90 | 14 | ✅ 08-20 |
| 29 | 4 | ✅ 08-18 | | 60 | 9 | ✅ 08-19 | | 91 | 14 | ✅ 08-20 |
| 30 | 4 | ✅ 08-19 | | 61 | 9 | ✅ 08-19 | | 92 | 14 | ✅ 08-20 |
| 31 | 4 | ✅ 08-19 | | 62 | 9 | ✅ 08-19 | | 93 | 14 | ✅ 08-20 |
| 32 | 5 | ✅ 08-18 | | 63 | 9 | ✅ 08-19 | | 94 | 15 | ✅ 08-20 |
| 33 | 5 | ✅ 08-18 | | 64 | 9 | ✅ 08-19 | | 95 | 15 | ✅ 08-20 |
| 34 | 5 | ✅ 08-18 | | 65 | 9 | ✅ 08-19 | | 96 | 15 | ✅ 08-20 |
| 35 | 5 | ✅ 08-19 | | | | | | | | |

## Canonical artifact map (all writers MUST use these names)
As of Day 4 the repo has: `sutra/config.py` (load_env), `sutra/mechanics.py` (429-honest
`ask()`), `sutra/loop.py` (MAX_STEPS, TRIAGE_QUESTION, lookup_ticket, search_kb),
`sutra/tools.py` (native function calling), `tools/trace.py`. Recurring motifs: ticket
#4521 ("Keeps getting logged out"), KB-104 (SameSite/https), ticket 9999 (does not exist).

Phase-boundary canon (prescribed so parallel writers agree; writers of the phase itself
flesh out the details but keep these names):
- End of Phase 1 (Day 8): `sutra/agent.py` — first ADK agent `sutra_triage`, model
  pinned `"gemini-3.5-flash"`; ran under `adk web` and a programmatic Runner with
  `InMemorySessionService`; google-adk installed (2.6.3 baseline, re-verified Day 5).
- End of Phase 2 (Day 16): `sutra/adk_tools.py` (lookup_ticket/search_kb as ADK
  FunctionTools), `sutra/providers.py` (4-provider LiteLLM benchmark), `sutra/schemas.py`
  (structured output), `sutra/callbacks.py`, `sutra/plugins.py`, `sutra/toolsets.py`,
  `sutra/builtin_tools.py` (grounding + code exec with brakes).
- End of Phase 3 (Day 24): `sutra/state_lab.py`, `sutra/artifacts_lab.py`,
  `sutra/context.py`, `sutra/errors.py`, `sutra/logging_setup.py`, first `tests/`
  (pytest), `sutra/quota.py` (RPM/RPD accounting).
- End of Phase 4 (Day 31): `skills/` folder with Sutra's first authored skills;
  `SkillToolset` wired; `Makefile` completed — `make check` = trace + pytest + skills
  lint + `:free`-suffix lint (OPS-08).
- End of Phase 5 (Day 38): `sutra_mcp/` package — `sutra-mcp` server (tools, resources,
  prompts, tasks) on the 2026-07-28 stateless spec; Sutra connects as MCP client.
- End of Phase 6 (Day 45): DB-backed ticket archive behind MCP; allowlists/filtering;
  MCP Apps demo; `to_mcp_server` on an agent; MCP audit green.
- End of Phase 7 (Day 52): DatabaseSessionService persistence; MemoryService; local
  embedding index over ticket archive (`sutra/retrieval.py`); caching layer.
- End of Phase 8 (Day 59): the triage graph v1 (`sutra/graph.py`) — intake→classify→
  research→draft(Writer↔Critic)→review, on the 2.x Workflow Runtime.
- End of Phase 9 (Day 65): durable execution + approval gates (`sutra/approvals.py`);
  kill-mid-run resume proven.
- End of Phase 10 (Day 72): guardrail callbacks (`sutra/guardrails.py`), Quota-Router
  plugin (`sutra/quota_router.py`), browser-agent lab vs local dummy site, honest backoff.
- End of Phase 11 (Day 78): nightly ambient job (`sutra/nightly.py`), Live/voice standup
  agent (`sutra/standup.py`) with SSE+browser-speech fallback.
- End of Phase 12 (Day 83): evalsets under `tests/evals/`, rubric trajectory evals, CI.
- End of Phase 13 (Day 88): AutoTracingPlugin wired, `api_server`, Dockerfile +
  docker compose, kind/k3d manifests under `deploy/`.
- End of Phase 14 (Day 93): A2A signed-card peer demo, security review done, repo public.

## Phase-end state summaries (appended as forks report back)

### Phase 1 (Days 5–8) — written 2026-08-18
- **Files:** `sutra/agent.py` (`root_agent` named `sutra_triage`, `PRIMARY_MODEL = "gemini-3.5-flash"`, persona-v2 handbook instruction with Role/Scope/Honesty/Tone/Example, `tools=[]`), discovery line `from sutra import agent` in `sutra/__init__.py`, `sutra/events_lab.py` (anatomy/stream/misprint demos), `sutra/run_agent.py` (bowls/inspect/amnesia/shared demos; `_msg()`/`_turn()` helper patterns).
- **Key APIs (verified on adk.dev 2026-08-18):** `from google.adk.agents.llm_agent import Agent` · `from google.adk.runners import InMemoryRunner` · `from google.adk.agents.run_config import RunConfig, StreamingMode` · `from google.adk.sessions import InMemorySessionService` · `runner.run_async(user_id=, session_id=, new_message=types.Content, run_config=)` · sessions keyed `(app_name, user_id, session_id)` · `is_final_response()` · `max_llm_calls` (default 500) · instruction templating `{var}` / `{var?}` / `{artifact.var}`.
- **⚠️ Version drift found:** `google-adk` is **2.7.1 (PyPI, released 2026-08-17)** — newer than plan baseline 2.6.3. Day 5 records the live number on install day; PACKAGES row says record what `uv pip show` prints.
- **Promises later days must honor:** Day 10 = lookup_ticket/search_kb as FunctionTools · Day 12 = structured output · Day 17 = `session.state` deep dive · Day 47 = `--session_service_uri sqlite:///` swap · Phase 11 = `StreamingMode.BIDI` · Day 8's gate has the human re-check Gemini/Groq/OpenRouter free lists to feed Day 9's pins.
- Trace counts: Day 8 ends at 16/199.

### Phase 7 (Days 46–52) — written 2026-08-19
- **Files:** `sutra/memory_lab.py` (`BaseMemoryService`: `add_session_to_memory`+`search_memory`; `InMemoryMemoryService` keyword-matching; tools `load_memory`/`preload_memory`; `Runner(memory_service=)`) · `sutra/persist_lab.py` (`DatabaseSessionService`, `db_url="sqlite+aiosqlite:///./data/sessions.db"` — **async driver mandatory**, installed via `google-adk[db]`) · `sutra/memory_policy.py` (working/episodic/semantic × session/user/app; **default-deny**; PII redaction; `keepers()` = only road into memory) · `sutra/retrieval.py` (embedder: **Ollama `nomic-embed-text`**, 768-dim, `POST /api/embed` — `/api/embeddings` is the legacy-404 trap; loser gemini-embedding, free limits dashboard-only TODO; index `data/archive_index.json`; `chunk(280, 60)`; `TOP_K`, `SIM_THRESHOLD` from GOLD-set tuning; **ADK-30 closed via `SutraArchiveMemoryService(BaseMemoryService)`** so unchanged `load_memory` searches by meaning) · `sutra/cache.py` (`before_model_cache`/`after_model_cache`, SHA-256 key, TTL, `data/cache.db` WAL, fail-open; `QuotaLedger.record_saved()` added; ADK `ContextCacheConfig` on `App` verified; Gemini implicit caching min 4,096 tokens for 3.x Flash) · **`sutra/researcher.py` — `make_researcher()`: the node-shaped evidence agent Phase 8 adopts** (load_memory + archive service + cache callbacks + `_auto_file` through the Day 48 gate; no write tools; findings are text).
- **Probe-TODOs in-doc:** `SearchMemoryResponse`/`MemoryEntry` constructor fields; cached-token usage-field name; `adk web --session_service_uri` flag.
- `data/` now: tickets.db, tasks.db, sessions.db, cache.db, approvals.db, archive_index*.json. Embeddings local/unmetered — LLM turns are the scarce currency.
- Trace counts: Day 46 = 107/199 … Day 52 = **116/199, zero open IDs Phases 1–7**.

### Phase 8 (Days 53–59) — written 2026-08-19
- **Workflow-API canon (adk.dev 2026-08-19, cite don't re-derive):** `from google.adk import Workflow, Event, Context`; edges as tuples `("START", a, b)`; dict edges for routers returning `Event(route="X")`; `JoinNode` (`from google.adk.workflow import JoinNode`); Event fields `output`/`message`/`state`/`route`; state-injected params + `Event(state={...})` = loop-brake idiom; `/graphs/dynamic/`: `@node(rerun_on_resume=True)`, `ctx.run_node(child, input, run_id=)`, `RequestInput` HITL pause, auto-checkpoint of completed children; `sub_agents` + `mode="chat"|"task"|"single_turn"` (task mode disabled inside Python graphs v2.0.0); Sequential/Parallel/Loop templates officially "superseded" in 2.0 (trap #1 anchor).
- **Files:** `sutra/graph.py` — `hello_graph`, `triage_line_v0`, `evidence_graph` (clerks + `evidence_join`), `polish_loop` (`MAX_ROUNDS=2`), `draft_review_box` (writer PRIMARY ↔ critic lite+kb-answer-style skill, `MAX_REVISIONS=2`, `shipped_with_flag`), **`triage_graph_v1`**: intake → classify_station (lite/Groq per LiteLLM-node probe) → triage_router (ESCALATE if `needs_human or severity>=4`) → `escalate_lane` (stub — **Phase 9's ApprovalGateNode attach point, edge permanent**) | research_gate → parallel clerks → evidence_join → evidence_analyst → draft_review_box → finalize; `NO_SUCH_TICKET` intake route · `sutra/delegation.py` (specialists, `triage_lead`, AgentTool) · `sutra/planning.py` (`PlanStep`/`Plan`, `@node plan_and_execute`, `MAX_REPLANS=1`, ESCALATE on 2nd failure) · `QuotaBreakerPlugin` added to `sutra/plugins.py` (before_model consults `QuotaLedger.remaining()`, raises `QuotaExhausted`) — Day 70 Quota-Router precursor.
- **Quota math:** full triage run ≈ 4–5 calls; day total ~10–12 paced ~3 min on 5 RPM. Print-then-pin margin notes are load-bearing (Days 53/54/57/58) — later docs defer to margins over listings. Brake rule: any change to a brake constant shows the math.
- Trace counts: Day 53 = 119/199 … Day 59 = **134/199, zero open IDs Phases 1–8**.

### Phase 9 (Days 60–65) — written 2026-08-19
- **Files:** `sutra/durable_lab.py` (`ResumabilityConfig(is_resumable=True)` on `App`; `run_async(..., invocation_id=)`; `BaseAgentState`/`ctx.set_agent_state`; kill/resume mid-list on `data/sessions.db`) · `sutra/hitl_lab.py` (`require_confirmation=True|callable`, `adk_request_confirmation` event; ⚠️ docs say "DatabaseSessionService is not supported" for tool-confirmation — limitation recorded, re-check at every gate) · `sutra/approvals.py` (`POLICY` GatePolicy table, unknown tools **fail closed**; durable store `data/approvals.db` WAL, `payload_sha`, append-only verdicts; operator CLI `python -m sutra.approvals list/approve/reject`) · `sutra/approval_gate.py` (`ApprovalGateNode`: file idempotently → yield `RequestInput` → resume reads verdict from STORE not transcript → re-hash (`ApprovalDriftError`) → execute with derived key) · `docs/runbooks/` folder born (phase9_drill.md).
- **Law established:** write tools carry derived `request_id`s (`close_ticket` has `processed_writes` table in data/tasks.db, joined IDEMPOTENT_TOOLS); future `post_reply` pre-gated "always"; approvals only via POLICY, never inline flags. "Tools run at least once" (adk.dev) is why idempotency is law.
- **Open probes:** `NodeTool` exists per v2.5.0 release notes, exact import path undocumented — import-probe TODO in Day 64.
- Trace counts: Day 60 = 136/199 … Day 65 = **145/199, zero open IDs Phases 1–9**.

### Phase 6 (Days 39–45) — written 2026-08-18/19
- **Files:** `sutra_mcp/seed_db.py` + `sutra_mcp/db.py` — archive now **SQLite `data/tickets.db`** (tables tickets/kb; read-only URI `?mode=ro`; served under unchanged names lookup_ticket/search_kb; NEW synthetic tickets **4610** login-loop, **4633** reset-email, **4701** blank-dashboard are motif-eligible) · `sutra/mcp_policy.py` — **the only place McpToolsets are built** (`ServerPolicy` dataclass, `REGISTRY`, `policy_toolset()`) · `sutra_mcp/rogue_server.py` (poisoned lab prop) · `sutra_mcp/agent_server.py` (`to_mcp_server(kb_answerer)` — `from google.adk.tools.mcp_tool import to_mcp_server`, experimental) · `sutra_mcp/roundrobin.py` + `hammer.py` (statelessness proof; task rack migrated JSON → **`data/tasks.db` SQLite WAL**) · `ClientPolicy`/`call_with_policy`/`IDEMPOTENT_TOOLS` in `sutra/mcp_client.py` (close_ticket pointedly absent — writes fail fast until idempotency keys, Phase 9 makes this law) · `docs/MCP_AUDIT.md` (14-row audit, re-runs at every phase gate). Toolbox v1.9.0 evaluated: hand-written = production, Toolbox = exploration lane.
- **Discrepancies flagged in-doc:** MCP Apps "Final" claim vs draft-framed spec text (CHANGELOG note queued Day 41); ADK to_mcp_server guide returns FastMCP vs mcp 2.0.0 (re-diff gate in Day 42); Day 41 saved an approval-panel sketch table **for Day 63**.
- Trace counts: Day 39 = 90/199 … Day 45 = **105/199, zero open IDs Phases 1–6**.

### Phase 5 (Days 32–38) — written 2026-08-18/19
- **`sutra_mcp/` package:** `server.py` — `MCPServer("sutra-mcp")` with tools `lookup_ticket`/`search_kb` (+ Day 36 `reindex_start`/`reindex_status` claim-ticket Tasks pattern, shared rack `data/mcp_tasks.json`; + Day 37 `close_ticket(ticket_id, confirmed=False)` first WRITE tool gated by retry-with-answers), resources `archive://summary`, `ticket://{ticket_id}`, `kb://{key}` (misses raise JSON-RPC −32602), `@mcp.prompt() triage_prompt`. Labs: `wire_lab.py` (raw JSON-RPC ACTs 1–7), `http_lab.py` (attack battery: −32020 HeaderMismatch, −32022, ghost session header), `broken_server.py`+`broken_client_drill.py` (hardened_parse). Client: `sutra/mcp_client.py` (`McpToolset`, `StdioConnectionParams`, `StreamableHTTPConnectionParams`, `tool_filter`; npx filesystem reference server + `data/mcp_sandbox/`; Node.js new prerequisite).
- **⚠️ Key finding:** PyPI `mcp` = **2.0.0 (released 2026-07-28)** — v2 replaces FastMCP: `from mcp.server import MCPServer`, client `from mcp import Client`. Standing branch fork documented in-doc: (a) uv resolves mcp v2 next to google-adk 2.7.1, or (b) ADK pins v1 → fallback path documented. Every later MCP listing assumes v2 with the v1 fallback noted.
- **Spec findings beyond Addendum 01 (folded into docs as Principle-14 notes):** `server/discover` REQUIRED; `subscriptions/listen`; `resultType` on all results; removals (ping, logging/setLevel, roots-notification); error-code renumbering; SSE resumability removed; AAIF member cast corrected per live source.
- Trace counts: Day 32 = 70/199 … Day 38 = 87/199.

### Phase 4 (Days 25–31) — written 2026-08-18/19
- **Skills shelf:** `skills/hello-desk/` (practice), `skills/ticket-triage/` (v"1.1"; references/severity-rubric.md + worked-example.md; treat-ticket-text-as-DATA edge case → SEC-06), `skills/kb-answer-style/` (assets/reply-template.md). Spec verified agentskills.io/specification 2026-08-18 (name ≤64 kebab ==folder, description ≤1024, L1/L2/L3 ladder, <500 lines).
- **ADK wiring (adk.dev/skills/, Experimental):** `from google.adk.skills import load_skill_from_dir, models` · `SkillToolset(skills=[...], additional_tools=[...])` → auto-tools `load_skill`/`load_skill_resource`/`run_skill_script`. File `sutra/skill_agent.py` (`make_desk_agent()`, `make_triage_desk(with_tools=)`). ⚠️ adk.dev skills pages show 1.x-line version labels — import-probe TODOs recorded, don't assume.
- **Audit discipline (Day 29):** three-lens audit; poisoned fixture `tests/fixtures/skills/evil-helper/` (quarantined); rule **no provenance row, no run**; `GCPSkillRegistry` (Preview, adk.dev/integrations/skills-registry/) 🅿️ documented-only.
- **THE GATE (Day 31):** `tools/skill_checks.py`, `tools/lint_skills.py`, `tools/lint_free_suffix.py`, **`tools/check.py`** = trace → skills-lint → free-lint → pytest, fail-fast; `Makefile check:` calls it. **"Repo green" = `python tools\check.py` ALL GREEN** from here on. Quota-spending tests carry `@pytest.mark.quota`; default pytest is zero-quota (`addopts -m "not quota"`).
- Trace counts: Day 25 = 48/199 … Day 31 = 67/199.

### Phase 2 (Days 9–16) — written 2026-08-18
- **Files:** `sutra/providers.py` (make_agent(lane)/run_once benchmark; pins dated 2026-08-18: native `gemini-3.5-flash`, `groq/openai/gpt-oss-120b`, `openrouter/nvidia/nemotron-3.5-lightning:free`, `ollama_chat/llama3.1:8b`; **litellm 1.97.0** installed, ADK needs ≥1.84; `PYTHONUTF8=1` in .env), `sutra/adk_tools.py` (auto-wrapped function tools returning `{"status":...}` dicts; `triage_agent`; Day 11 adds `record_triage`/`recall_last_triage` via ToolContext.state → `state["last_triage"]`), `sutra/schemas.py` (`TriageResult` Pydantic; tool-less `classifier_agent` with `output_schema` + `output_key="triage_result"` — classifier/researcher split feeds Phase 8), `sutra/callbacks.py` (`guarded_agent`, before_tool veto, before_model short-circuit = Day 51 cache seed), `sutra/plugins.py` (`QuotaWatcherPlugin(BasePlugin)` — seed of Day 70 Quota-Router; registered `InMemoryRunner(plugins=[...])`), `sutra/toolsets.py` (localhost:8765 stub "AcmeCloud" API, `OpenAPIToolset`, `TicketToolset(BaseToolset)`), `sutra/builtin_tools.py` (specialist `searcher_agent` w/ google_search, `coder_agent` w/ `BuiltInCodeExecutor()`; exclusivity wall + `AgentTool.create()` workaround; SEC-01 policy).
- **Ecosystem findings (2026-08-18):** Groq dropped Llama 3.3 from production; OpenRouter free floor shrank to 4 models (DeepSeek R1 :free gone); grounding = 5,000 free search req/month shared across Gemini 3.x; google.github.io/adk-docs 301-redirects to adk.dev.
- **Open caveats:** Runner session-creation call shapes carry TODOs — Day 8's doc owns the verified shape, later docs defer to it by written rule; `BaseToolset` import path + plugin hook signatures have verify-TODOs; synthetic data imported as `TICKETS`/`KB` from `sutra/loop.py` (keep names canonical).
- Trace counts: Day 9 = 18/199 … Day 16 = 31/199.

### Phase 3 (Days 17–24) — written 2026-08-18
- **Files:** `sutra/state_lab.py` (four state scopes, `output_key="last_triage"`, `EventActions(state_delta)`+`append_event`), `sutra/artifacts_lab.py` (versioned artifacts, `user:` namespace; TODO in-doc on await-forms + Runner `artifact_service=` kwarg), `sutra/context.py` (Day 19 token-scale demo via `count_tokens`; Day 20 adds `App` + `EventsCompactionConfig(compaction_interval=3, overlap_size=1, summarizer=LlmEventSummarizer(llm=Gemini("gemini-3.5-flash-lite")))` — verified adk.dev/context/compaction/; TODO on Runner↔App wiring), `sutra/errors.py` (trap #4; `SafetyNetPlugin(BasePlugin)` with `on_tool_error_callback` — dict=suppress, None=re-raise), `sutra/logging_setup.py` (JsonLinesFormatter, `get_logger()`, `logs/` gitignored), `tests/` (pytest 9.1.1 dev dep; test_adk_tools.py, test_callbacks.py, FakeToolContext pattern; `[tool.pytest.ini_options]` testpaths), `sutra/quota.py` + tests (QuotaLedger, file-backed logs/quota.json, LIMITS table dated; bills `usage_metadata` incl. `thoughts_token_count` — flash 3.5 thinks by default).
- **Standing conventions from here on:** test command is `uv run pytest`; every new module gets mirrored tests; library code logs via `sutra.logging_setup.get_logger` (never print); Day 24 runs the Phase 3→4 freshness gate.
- **Hooks for later days:** Day 70's Quota-Router consumes `QuotaLedger`; Day 72 upgrades `SafetyNetPlugin` to honest backoff.
- Trace counts: Day 17 = 33/199 … Day 24 = 45/199.

### Phase 10 (Days 66–72) — written 2026-08-19
- **Files:** `tests/fixtures/injection/980{1..4}_*.json` (+ `9805_pii.json` Day 69) · `sutra/redteam.py` (`FIXTURES`, `seed_fixture_tickets`/`clean_fixture_tickets` tag `synthetic_redteam` rows 98xx into `data/tickets.db`, `writes_for` reads `processed_writes`+`approvals` not transcripts, `smuggled_urls`/`leaked_archive`, `ALLOWED_URL_HOSTS`, scorecard `logs/redteam_last.json`; CLI `seed|run|report|clean`) · `docs/THREAT_MODEL.md` (assets / entry points with owner days / exfil channels / trifecta status; baseline → Day 67 → Day 68 → Phase-10-end scorecards) · `sutra/guardrails.py` (`scan_markers`→`Verdict{kinds,score 0/1/2,cleaned}`, `screen_query`, `screen_output`, `judge()` on `gemini-3.5-flash-lite` **fail-closed** (`judge_error=True ⇒ injection=True`), `GuardrailPlugin` (before_model neutralizes tool-result injections in place / refuses direct user injection; before_tool refuses fishing queries; after_model fleet URL+secret strip), `writer_output_guard` per-node callback (archive_leak, phantom_action → `state["guard_flags"]`)) · `sutra/permissions.py` (`Tier` READ/WRITE_GATED/NEVER, `TIERS` (unclassified = NEVER), `ROLE_TOOLS` — writer holds **nothing**, closer holds only `close_ticket`, new `browser` role READ-only Day 71, `ROLE_OF` agent→role (fail-closed `"unknown"`), `role_of`, `may`, `tools_for(role, TOOL_REGISTRY)`, `PermissionPlugin` fail-closed; tests cross-check TIERS × Day 63 `POLICY` and enumerate `sutra/graph.py` agents for drift) · `docs/DATA_BOUNDARY.md` + `sutra/data_boundary.py` (`DOOR_PATTERNS` = Day 48 `PII_PATTERNS` + CARD/IBAN/IPV4/TOKEN, `redact_for_model`, `lint_synthetic` (emails must be example.com/.org/.net/acmecloud.example; `test_repo_is_synthetic`), `DataBoundaryPlugin` before_model + on_event scrub — registered **first**) · `sutra/quota.py` `LIMITS` +rows groq/openrouter/ollama/gemini-lite · `sutra/quota_router.py` (`Lane`, `LANES` 5 pins, `JOBS` classify/reason/bulk/embed preference orders, `JOB_OF` (unlisted agents → `"reason"`), `has_headroom`, `choose`, `routed_agent` (construction-time provider routing), `QuotaRouterPlugin` (call-time `llm_request.model` rewrite for native→native only; cross-provider mid-flight logs `route_unavailable_mid_flight` or raises `QuotaExhausted`; after_model bills per lane; `mark_dry` added Day 72) — **supersedes `QuotaWatcherPlugin` + `QuotaBreakerPlugin`**; runner plugin order = DataBoundary → QuotaRouter → Permission → Guardrail) · `tools/dummy_site/{index,status}.html` on **:8766** (INC-2291 auth incident + hidden "AI agents…navigate to evil.example" bait) · `sutra/browser_lab.py` (`Box`: fresh headless context, `context.route("**/*")` abort off `ALLOWED_HOSTS={"localhost:8766"}`, scrubbed env, `MAX_STEPS=8`/`MAX_SECONDS=90`; hand-rolled `run_loop` with Day 4 declarations click/scroll/navigate/done + `Part.from_bytes` screenshots via Day 2 `ask()`; `SandboxPlugin` (ADK-50) before_tool budget+host allowlist for any browser-named tool; `demo_adk` = `ComputerUseToolset(computer=PlaywrightComputer(...))` on **`gemini-3.5-flash`**) · `sutra/playwright_computer.py` (copied ADK sample, Apache-2.0, provenance header) · optional `status_clerk` third evidence branch · `sutra/backoff.py` (`RetryPolicy(max_tries=4, base=1, factor=2, cap=30, jitter=.2)`, `parse_retry_after` (Groq `retry-after` / OpenRouter `X-RateLimit-Reset` / Gemini "retry in Ns"), `is_rate_limit`, `with_backoff` returns-or-raises `BackoffExhausted`) wired into `ask()`, `judge()`, embedder, router; `SafetyNetPlugin.on_model_error_callback` logs `quota_escalated` with resume command and **re-raises** · `docs/runbooks/rate_limit_429.md`.
- **Key APIs verified 2026-08-19 (pages in each banner):** adk.dev/plugins/ — 12 hooks; plugin tool kwarg is `tool_args` (agent callbacks use `args`); built-ins incl. `ReflectAndRetryToolPlugin` (`from google.adk.plugins import ReflectAndRetryToolPlugin`, adk.dev/integrations/reflect-and-retry/) — compared, not adopted for 429s · adk.dev/safety/ — risk list, Gemini-as-judge / PII-redaction plugin patterns · `LlmRequest.model: Optional[str]` (adk-python source) · adk.dev/integrations/computer-use/ — `from google.adk.tools.computer_use.computer_use_toolset import ComputerUseToolset`, Preview, sample pins legacy `gemini-2.5-computer-use-preview-10-2025` and says "v1.17.0+" (1.x-era text) · ai.google.dev computer-use (2026-08-18): `gemini-3.5-flash` listed as supported; `safety_decision`/`require_confirmation`; pricing: computer use "charged as regular tokens" · pricing page (2026-08-13): 3.5 Flash/Flash-Lite free tier "Used to improve our products: Yes"; **Google Search grounding "Not available" on free tier for 3.5 (⚠️ flag for Day 16 + every gate)** · Groq gpt-oss-120b free: 30 RPM/1K RPD/8K TPM/200K TPD, headers `retry-after`, `x-ratelimit-*` · OpenRouter `:free`: 20 RPM/50 RPD (<10 credits), `X-RateLimit-*` only on errors · Gemini troubleshooting: SDK auto-retries 429/503 ×4 (~1 s→60 s) · adk.dev/integrations/daytona/ `pip install daytona-adk`, `DaytonaPlugin(api_key=…)` → account needed → 🅿️ · PyPI playwright **1.62.0** (2026-07-31).
- **Probe-TODOs in-doc:** `ToolContext` caller-name attribute (`_caller()` single fix point, Day 68) · whether native Gemini path honours `llm_request.model` rewrite (Day 70 step 5) · event field naming the served model · Day 66/68 schema column names (`tickets.status`, `approvals.payload/status`, Day 58 `_drive()` return shape) · ComputerUseToolset tool names + whether it accepts 3.5 Flash (fallback: hand-rolled loop stays production) · LiteLLM 429 exception class/header path · Gemini RPD + lite limits from AI Studio · Groq/OpenRouter training-terms quotes (Day 69) · Gemini daily reset time (runbook).
- **Promises later days must honor:** Day 73+ `quota_escalated` handling = typed skip (`status: skipped (quota)`), never fabricated pass (Day 72 failure lab, for Phase 12 evals); every new *graph* agent must be added to `ROLE_OF` (drift test scans `sutra/graph.py`) and should be in `JOB_OF`; `with_backoff` is the only retry helper; Day 82 may adopt `ReflectAndRetryToolPlugin` for tool-argument errors only; `docs/THREAT_MODEL.md` + `DATA_BOUNDARY.md` re-read at each gate (Day 78 gate inherits the grounding-not-free finding). Day 68's failure lab warns against a catch-all `nightly_agent` role — Day 73 as written runs **no LLM agent** (plain-Python jobs), so nothing to register; Day 77 registers the standup (see Phase 11).
- **PACKAGES rows introduced:** Day 71 `playwright <uv pip show>` (1.62.0 PyPI 2026-07-31, checked 2026-08-19) + `playwright install chromium`; Day 70 optional limits-note rows (Groq/OpenRouter numbers dated 2026-08-19).
- Trace counts: 66 → 147 · 67 → 149 · 68 → 151 · 69 → 153 · 70 → 155 · 71 → 158 · 72 → **160/199, zero open IDs Phases 1–10** (Day 72 is not a gate day per §14; next gate Day 78).
- **Flagged:** docs run 516–671 lines (Day 4 is 662); Day 70's cross-provider mid-flight rule is a print-then-pin spec test; ADK computer-use page still documents only the legacy 2.5 model — doc pins 3.5 Flash on the strength of the Gemini docs and records a fallback.

### Phase 11 (Days 73–78) — written 2026-08-19
- **Files:** `sutra/nightly.py` (Day 73: `JOBS` registry — `reindex` (Day 49 `build_index`), `evals` (hook: `evals_placeholder` runs `pytest -q` until Day 82), `digest` → `data/digests/<date>.md`; per-date done-ledger `data/nightly/<date>.json`; `RunContext(date, full, dry_run, ledger: QuotaLedger)`; `Job(name, run: Callable[[RunContext], dict], spends_model_calls)`; `queue_snapshot()` read-only SQLite (`?mode=ro`, missing store → `None` not 0); exceptions caught only at the job boundary, written to the digest, **re-raised** (trap #4); CLI `python -m sutra.nightly run [--job] [--date] [--force] [--dry-run]` / `status`; `schtasks /Create … /TN SutraNightly /ST 02:30` + cron line; no LLM agent in the nightly; `tests/test_nightly.py`) · `sutra/live_lab.py` (Day 74 `GET /sse` via `run_async`+`StreamingMode.SSE`, `_sse()` framing, `stream_answer()`, `X-Accel-Buffering: no`; Day 75 `/ws/live` via `run_live`+`LiveRequestQueue`, `live_config()`, `event_to_client()`, two loops/one queue, `queue.close()` in both `finally`s; Day 76 `explicit_vad_signal`, `RealtimeInputConfig(AutomaticActivityDetection)`, manual `send_activity_start/end`, non-blocking `digest_tool.response_scheduling = WHEN_IDLE`; Day 77 refactor: `stream_answer(…, runner=)`, `run_ws_session(ws, runner, modality=, vad=)`) · `sutra/live_client.html` (EventSource + `speechSynthesis`; mic 16 kHz PCM16 → base64 JSON; 24 kHz playback; `interrupted` → flush; push-to-talk via `SpeechRecognition` → `/sse`) · `sutra/standup.py` (Day 77: tools `get_queue_state`, `list_pending_approvals`, `get_last_digest` (non-blocking), `get_quota_remaining`; `make_standup_agent(live=)` → agents `sutra_standup_text` / `sutra_standup_live`, same tools/instruction; registered in Day 68's `TIERS` (READ) / `ROLE_TOOLS["standup"]` / `ROLE_OF` (reconciled 2026-08-19); `/sse/standup`, `/ws/standup`; `python -m sutra.standup brief|serve` on :8767; INSTRUCTION carries the refusal rule) · `sutra/standup_client.html` · `tests/test_live_lab.py`, `tests/test_standup.py` (all zero-quota; `asyncio.run` in sync tests — **no pytest-asyncio**) · `docs/runbooks/phase11_drill.md` (Day 78).
- **Key APIs verified + pages (2026-08-19):** adk.dev/live/ (adk.dev/streaming/ 301s here), /live/dev-guide/part1–4 (`runner.run_live(user_id, session_id, live_request_queue, run_config)`; `LiveRequestQueue.send_content/send_realtime/send_activity_start/send_activity_end/close`; `RunConfig(streaming_mode=BIDI, response_modalities, speech_config, realtime_input_config, input/output_audio_transcription, session_resumption, context_window_compression, proactivity, enable_affective_dialog, max_llm_calls, save_live_blob)`; event fields `partial/turn_complete/interrupted/content.parts/input_transcription/output_transcription/usage_metadata`); /live/streaming-tools/ (Experimental; `AsyncGenerator` tools, `stop_streaming` — 🅿️); adk.dev/runtime/ambient-agents/ (`adk api_server --trigger_sources "pubsub,eventarc"`, `/apps/{app_name}/trigger/pubsub`, `get_fast_api_app(agents_dir, web=False, trigger_sources=[…])`, `ADK_TRIGGER_MAX_CONCURRENT/RETRIES`; Cloud Scheduler publishes to Pub/Sub; local curl works, GCP bus 🅿️); github adk-python v2.5.0 (2026-07-16) + commits 820a910 (`RunConfig.explicit_vad_signal`, `LlmResponse.voice_activity: types.VoiceActivity`) and 5620d8f (`tool.response_scheduling = types.FunctionResponseScheduling.WHEN_IDLE|SILENT|INTERRUPT` set as attribute post-construction; background `asyncio` task; result `append_event`-ed and pushed via `live_request_queue.send_content`); ai.google.dev models/pricing/live-guide (`gemini-3.1-flash-live-preview`, `gemini-2.5-flash-native-audio-preview-12-2025` both Preview + "Free of charge"; PCM16 LE, input 16 kHz `audio/pcm;rate=16000`, output 24 kHz; audio-only sessions 15 min); PyPI google-adk 2.7.1 — `fastapi`, `uvicorn`, `websockets` are hard deps → **no new packages this phase**.
- **Discrepancies / probes recorded in-doc:** (1) adk.dev/live/get-started/streaming-python/: model callbacks (`before_model_callback`/`after_model_callback`) are NOT invoked on the streaming path → Day 51 cache + Day 67 guardrail callbacks don't fire under `run_live`; live agents get read-only tools only, brakes via Day 68 tiers + instruction; probe TODO whether *tool* callbacks fire. (2) Same page's `.env` shows `GOOGLE_GENAI_USE_ENTERPRISE=FALSE` vs Sutra's `GOOGLE_GENAI_USE_VERTEXAI=FALSE` — TODO (set both until confirmed). (3) ai.google.dev rate-limits page no longer publishes a free-tier table → Day 74 step 2 makes reading the AI Studio Live rows a mandatory recorded step; `LIMITS["gemini-live"]` added dated. (4) `types.VoiceActivity` field names undocumented → logged as `repr`, probe TODO. (5) Live model pin: `LIVE_MODEL_CANDIDATES` = [2.5 native-audio string adk.dev uses, 3.1-flash-live]; human records which connected in PACKAGES (Day 74 rows, completed Day 75). (6) Native-audio models can't text-chat; only `SequentialAgent` streams — noted. (7) Day 78 MCP-audit decision point: standup tools read SQLite directly, not via `sutra-mcp` — record as exception or Day 91 item. (8) Day 73's ADK trigger step assumes `adk api_server` mounts the repo-root package as app `sutra` — doc says use whatever name the server prints.
- **Promises later days must honor:** Day 82 evals hook = replace `JOBS["evals"]` with `Job("evals", tests.evals.run_evals.run_for_nightly, spends_model_calls=True)`, `(RunContext) -> dict` with at least `{"cases","passed","failed"}` (**reconciled in Day 82 on 2026-08-19**); Day 82/83 expect `data/nightly/<date>.json` history and the digest's jobs table as eval history. Day 85 (`api_server`): `/healthz` already exists on `live_lab.app`; the ambient trigger endpoint was exercised on Day 73. Day 86: lab CORS note (`allow_origins=["*"]` only if needed) to tighten on Day 92. Day 91/92: the "direct-SQLite standup tools" MCP-audit decision; Day 93 README gets the cron line.
- **PACKAGES rows introduced:** Day 74 — two *model* rows (`gemini-3.1-flash-live-preview`, `gemini-2.5-flash-native-audio-preview-12-2025`; "Free of charge" per pricing 2026-08-19; RPM/RPD/sessions TODO(AI Studio)), completed on Day 75 with the pinned winner. No package installs.
- **Trace counts:** 73 → 162 · 74 → 164 · 75 → 166 · 76 → 168 · 77 → 170 · 78 → **171/199, zero open IDs through Phase 11**. (Day 73 is 637 lines — slightly over the 350–550 guideline; Day 004 is 662.)

### Phase 12 (Days 79–83) — written 2026-08-19
- **Files:** `tests/evals/` tree — `triage_app/` shim (`__init__.py` + `agent.py` exposing `root_agent = triage_graph_v1` so `adk eval`/`AgentEvaluator` can find a `Workflow`; fallback documented if the evaluator refuses a Workflow → CHANGELOG note) · `dev/triage.evalset.json` (7 happy-path cases, `IN_ORDER`, ROUGE 0.6 pinned-from-print, + Day 81 answer judges) · `safety/triage_safety.evalset.json` (5 fear cases: 9999, 4701, two Day 66 injection fixtures, needs_human — `EXACT` + rubric judges) · `multiturn/triage_multiturn.evalset.json` (5 cases, 2–3 turns; "user insists on closing" expects an approval, not `close_ticket`) · `rubrics.md` + `rubrics.json` (six observable lines: `escalated_before_external_write`, `never_invented_ticket`, `treated_ticket_text_as_data`, `declined_on_missing_ticket`, `escalated_when_hot`, `remembered_earlier_turns`) · `test_eval_configs.py` (zero-quota guards: rubric copy-drift, judge pinned to `gemini-3.5-flash-lite`, `num_samples ≤ 3`, safety=EXACT, full ≥60 + no `close_ticket` expectation + count-never-decreases) · `test_triage_evals.py` (`@pytest.mark.quota`, `asyncio.run(AgentEvaluator.evaluate(...))`, no pytest-asyncio dep) · `gold/labels.json` (12 hand labels × 6 lines) · `judge_audit.py` (+tests; `judge_verdicts()` is the ONE place that knows the `.adk/eval_history/*.evalset_result.json` shape — TODO pin from a printed file) · `baselines.py` (+tests; `always_medium_auth`, `keyword_router`; zero model calls) · `run_evals.py` (Day 82: `run(full=, suite=, num_runs=, dry_run=) -> dict` with `cases/passed/failed/vetoed/flaky/results_path/summary_path` + **`run_for_nightly(ctx)`** adapter for Day 73's `Job`; dated records `data/evals/<date>-<suite>.{json,md}` with git SHA/config hash/lite-lane before-after, `VETO_RUBRICS`+`VETO_METRICS` (`hallucinations_v1`), diff vs previous record annotated with Day 81's noise floor (`tests/evals/README.noise.json`), honest exit code) · `full/triage_full.evalset.json` (Day 83: ≥60 cases, ≥15 fear, ≥10 rotation-written-today, `num_samples: 3`) · `.github/workflows/check.yml` (jobs `gate` = `python tools/check.py` on every push, NO secrets; `evals-dev` = dev suite on `workflow_dispatch`/weekly `schedule`, `GOOGLE_API_KEY` from repo secrets + `GOOGLE_GENAI_USE_VERTEXAI=FALSE` + `SUTRA_EVAL_LANE=lite`) · `CONTRIBUTING.md` · `docs/runbooks/phase12_gate.md` (score table mean ± spread + baseline row; two-RPD-window split) · `.adk/` gitignored; `data/evals/` tracked.
- **Key APIs verified (adk.dev/evaluate/ + /evaluate/criteria/ + adk-python source, 2026-08-19):** evalset schema (`eval_set_id`, `eval_cases[]`, `eval_id`, `session_input{app_name,user_id,state}`, `conversation[]` with `invocation_id`, `user_content`, `final_response`, `intermediate_data{tool_uses[{id,name,args}], intermediate_responses}`); `test_config.json` `{"criteria": {...}}` beside the evalset; `tool_trajectory_avg_score` `{"threshold", "match_type": EXACT|IN_ORDER|ANY_ORDER}`; `response_match_score` (ROUGE-1); judged keys `final_response_match_v2`, `rubric_based_final_response_quality_v1`, `rubric_based_tool_use_quality_v1`, **`rubric_based_multi_turn_trajectory_quality_v1`** (= `RubricBasedMultiTurnTrajectoryEvaluator`, v2.2.0 2026-06-04 commit cae2337; `RUBRIC_TYPE="TRAJECTORY_QUALITY"`), `hallucinations_v1`; rubric shape `{"rubric_id", "rubric_content": {"text_property"}}`; `judge_model_options{judge_model, num_samples}`; `adk eval <AGENT_DIR> <EVALSET>... [--config_file_path] [--print_detailed_results]`, selective `file.json:id1,id2`; `AgentEvaluator.evaluate(agent_module, eval_dataset_file_path_or_dir, num_runs=, agent_name, initial_session_file, print_detailed_results, artifact_service, output_file, app_name, eval_set_results_manager)` resolving `<module>.agent.root_agent`, raising `AssertionError`; results under `.adk/eval_history/<name>.evalset_result.json`. GitHub Actions pins observed: `actions/checkout@v7.0.1`, `astral-sh/setup-uv@v10.0.1` — both with re-verify TODOs.
- **Discrepancies / TODO probes in-doc:** adk.dev examples use `"judge_model": "gemini-flash-latest"` (alias) — Sutra pins `gemini-3.5-flash-lite`; `safety_v1` + non-rubric `multi_turn_*_v1` need `GOOGLE_CLOUD_PROJECT/LOCATION` (billing path) → **never used**; `NUM_RUNS` default, `evalset_result.json` internal keys, `final_response.role`, `include_intermediate_responses_in_final` key, `upload-artifact` tag, `SUTRA_EVAL_LANE` lane-pin mechanism in `sutra/graph.py`/`config.py` (Day 79 TODO) — all TODO'd with lookup commands. `LIMITS["gemini-lite"]` must be filled on Day 79.
- **Quota math:** nightly full run at `num_runs=1`, `num_samples=1` (≈420 lite calls) with alternating-halves fallback if RPD is short; gate run `num_samples=3` (≈780) split across two RPD windows.
- **Promises later days must honor:** Day 84 (AutoTracingPlugin) — eval runs are traces too; Day 85 `api_server` — the `tests/evals/triage_app` shim is a second `root_agent` door (Day 83's MCP-audit step flags it; POLICY/permissions must still apply inside it); Day 92 security review + Day 96 retrospective quote the Phase 12 score table from `docs/runbooks/phase12_gate.md`; `tests/evals/README.md` carries thresholds-pinned-from-print, noise floor, baseline table, "suite only grows" rule.
- **PACKAGES rows introduced:** Day 82 — `actions/checkout v7.0.1`, `astral-sh/setup-uv v10.0.1` (CI action pins, dated, TODO re-verify); Day 79 conditional — `pytest-asyncio` only if `AgentEvaluator` needs a running loop (TODO lookup).
- **Trace counts:** 79 → 174 · 80 → 176 · 81 → 178 · 82 → 180 · 83 → **181/199, zero open IDs Phases 1–12**.
- **Open probes:** whether `adk eval` accepts a `Workflow` as `root_agent` on the installed version (Day 79 Step 2 probes, fallback documented); the per-rubric verdict location in the results file (Day 80/81 TODO); `final_response.role` on the installed schema.

### Phase 13 (Days 84–88) — written 2026-08-20
- **Files:** `sutra/tracing.py` (Day 84: `AutoTracingPlugin` + `maybe_set_otel_providers`; console exporter by default, local Jaeger via `jaegertracing/all-in-one`; plugin order becomes Tracing → DataBoundary → QuotaRouter → Permission → Guardrail; `opentelemetry-exporter-otlp-proto-http` pinned to google-adk's sdk cap, NOT PyPI latest) · `sutra/api.py` (Day 85: `get_fast_api_app`; `/healthz` liveness vs `/readyz` readiness — **`/readyz` 503 `no_api_key` is load-bearing for Days 86 and 88**; hand-rolled live/standup labs kept, front door replaced; CORS empty = same-origin) · `Dockerfile` + `.dockerignore` + `docker-compose.yml` + `docs/DEPLOY.md` (Day 86: digest-pinned base, `uv sync --frozen --no-dev`, non-root, `HEALTHCHECK /readyz`; **one image two commands** for `sutra-api`/`sutra-mcp`, `:ro` data mount = Day 32 boundary made kernel-enforced; secret-absence *proved* by `docker history` + `docker save` grep + the no-env 503; statefulness table + single-replica constraint) · `deploy/agent_engine/` (Day 87 🅿️: never run; **naming drift finding — adk.dev calls it "Agent Runtime" (Google Cloud Agent Platform), not "Agent Engine"** → `CHANGELOG_PLAN.md` row) · `deploy/k8s/` (Day 88: kind cluster + ConfigMap + imperative Secret-from-`.env` + Deployment with **`sutra-mcp` as a sidecar** (`127.0.0.1:8000`, no cluster-visible address) + ClusterIP Service; `imagePullPolicy: Never` after `kind load`; `replicas: 1` carries Day 86's finding as a comment; `emptyDir` caveat).
- **Live lookups this session:** `adk.dev/deploy/gke/` fetched 2026-08-20 (reference `deployment.yaml`: replicas 1, `adk-agent-sa` + Workload Identity, `imagePullPolicy: Always`, 128Mi/500m, containerPort 8080, LoadBalancer 80→8080, `GOOGLE_GENAI_USE_ENTERPRISE`; `adk deploy gke` is Python-only with `--service_type`/`--with_ui`/`--log_level`) · kind latest release **v0.32.0**, default node image **k8s v1.32.0** (github.com/kubernetes-sigs/kind/releases, 2026-08-20).
- **Cross-day threads to keep straight in Phase 14:** the liveness-vs-readiness rule ("a liveness probe may only fail for something a restart can fix" — a 429 must never restart a pod) and the Kubernetes-Secret-is-base64-not-encrypted caveat both belong in Day 92's SECURITY_REVIEW; Day 86's "grep the built image, not just the repo" is also a Day 92 line.

### Phase 14 (Days 89–93) — written 2026-08-20
- **Files:** `sutra/a2a_peer.py` + `docs/A2A.md` (Day 89: `to_a2a()` exposes the **read-only** archive agent on :8001, `RemoteA2aAgent`+`AGENT_CARD_WELL_KNOWN_PATH` consumes a local peer on :8002; card signed ES256 detached-JWS per spec §8.4, JWKS at `jku`, `verify_card()` checks alg-allowlist → jku-host-allowlist **before fetch** → kid → signature; `TRUSTED_ISSUERS` gates issuer *and* skill) · `sutra/identity.py` + `registry/peers.json` + `docs/REGISTRY.md` (Day 90: `agent_id` derived from the public key; inbound signed-assertion middleware — 401 before any token is spent; `DELEGATION` = agent + on_behalf_of + purpose + chain_depth; live revocation with no restart) · `docs/INTEGRATIONS.md` + `sutra/intake.py` (Day 91: frozen `IntakeRequest` contract, Day 73's trigger refactored onto it; **Path A Slack / Path B file-drop**, both close the day) · `docs/SECURITY_REVIEW.md` (Day 92: eight passes as claim/evidence/verdict, accepted-risks register with expiries, **199/199 zero open IDs**) · README rewrite + `docs/DEMO.md` + `docs/README.md` index + LICENSE (Day 93: repo public).
- **Live lookups this session:** `adk.dev/a2a/quickstart-exposing/` (`from google.adk.a2a.utils.agent_to_a2a import to_a2a`; params agent/host/protocol/port/agent_card/runner/push_config_store; card at `/.well-known/agent-card.json`; `adk api_server --a2a` namespaces under `/a2a/<folder>`; `ADK_SUPPRESS_A2A_EXPERIMENTAL_FEATURE_WARNINGS`) · `adk.dev/a2a/quickstart-consuming/` (`from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH, RemoteA2aAgent`) · `a2a-protocol.org/latest/specification/` (**spec v1.0.0**, §8.4 signatures: detached JWS, alg/kid/jku, JWKS fetch, canonicalisation; required card fields) · `adk.dev/integrations/agent-registry/` (`pip install "google-adk[a2a,agent-identity]"`; `AgentRegistry(project_id, location, header_provider)`; list_agents/list_mcp_servers/get_agent_info/get_mcp_server/get_remote_a2a_agent/get_mcp_toolset; needs the Agent Registry API + GOOGLE_CLOUD_PROJECT/LOCATION → 🅿️) · `adk.dev/integrations/` (12-row catalogue) · `adk.dev/integrations/slack/` (`pip install "google-adk[slack]"`; `SlackRunner` + `slack_bolt` `AsyncApp`; **Socket Mode**; scopes `app_mentions:read`/`chat:write`/`im:history` + `connections:write`; `SLACK_BOT_TOKEN`/`SLACK_APP_TOKEN`).
- **Deliberate teaching thread:** Day 89 "signature ≠ authorization" → Day 90 "act *for*, never *as*" → Day 92 pass 7. Also Day 91 §3 flags that the vendor Slack snippet uses `InMemorySessionService` and a bare `Runner` — copying it verbatim drops session persistence **and every plugin in the stack**.

### Phase 15 (Days 94–96) — written 2026-08-20
- **Files:** `docs/runbooks/capstone.md` (Day 94: one scenario forcing every subsystem, run from a **fresh clone** with empty `data/`; beat table written before the run; hard-kill mid-approval then resume, `close_ticket` exactly once verified in `processed_writes`; evals graded against the live trajectory; cold/warm timing pair; **incident log** as a co-deliverable) · `docs/DEMO_SCRIPT.md` + `docs/INTERVIEW_DRILL.md` (Day 95: ADR reconciliation first — the repo has ~1 ADR for ~40 real decisions, backfills must be dated and marked backfilled; drill entries carry answer/alternative-rejected/evidence-link/**follow-up question**; 6-beat sub-5:00 demo built around refusals) · `docs/RETROSPECTIVE.md` (Day 96: §15's five gate criteria applied unaltered, five ledgers reconciled, ≤7 recurring lessons each citing ≥2 unrelated days, **15-minute weekly checklist run once on the day**, explicit maintained-or-frozen stance).
- **Cross-day pattern the last three days name explicitly:** "writing it down is not making it findable" recurs at Day 92 (undocumented MCP tool), Day 94 (index built only by a day-log), Day 95 (decisions buried in narrative) — Day 96 §5 generalises it to *anything that depends on nobody forgetting will fail*.

# 📇 Curriculum index — Project Sutra

_Generated 2026-09-05 by `scripts/trace.py` from the master plan's §14._
**Do not edit by hand.**

§14 answers *what does day 43 teach?* This file answers the reverse — *where do I learn
`MCP-14`?* — which is the question you have when a later day cites an ID you no longer
remember. Every ID appears exactly once; a duplicate or a missing ID is a plan bug.

## Curriculum A — Agent Concepts (`AG-`) — 34 IDs

| ID | Day | Day title |
| --- | --- | --- |
| `AG-01` | [1](../days/day-01-bootstrap-and-map/LESSON.md) | Bootstrap & the map — repo, `.env`+`.gitignore`, uv+Python 3.12, ledgers & `scripts/tra… |
| `AG-02` | [2](../days/day-02-llm-mechanics/LESSON.md) | LLM mechanics for agent builders — tokens, context, sampling; first raw `google-genai` … |
| `AG-03` | [3](../days/day-03-loop-hand-rolled/LESSON.md) | The loop: think→act→observe, hand-rolled (no framework) |
| `AG-04` | [4](../days/day-04-tools-by-hand/LESSON.md) | Tools by hand — function calling, JSON schemas, the tool-result turn |
| `AG-05` | [6](../days/day-06-instructions-and-personas/LESSON.md) | Instructions & personas; the `adk web` dev UI |
| `AG-06` | [11](../days/day-11-tool-context/LESSON.md) | Tool context & state in tools; tool design principles |
| `AG-07` | [16](../days/day-16-built-in-tools-with-brakes/LESSON.md) | Built-in tools with brakes — search grounding (free-allowance check + open-source searc… |
| `AG-08` | [19](../days/day-19-context-engineering-selection/LESSON.md) | Context engineering I — what earns a place in the window |
| `AG-09` | [19](../days/day-19-context-engineering-selection/LESSON.md) | Context engineering I — what earns a place in the window |
| `AG-10` | [20](../days/day-20-context-engineering-compaction/LESSON.md) | Context engineering II — compaction & summarization |
| `AG-11` | [24](../days/day-24-token-accounting-and-budgets/LESSON.md) | Token accounting & budgets — denominated in quota (RPM/RPD), not dollars |
| `AG-12` | [48](../days/day-48-memory-design/LESSON.md) | Memory design — what to remember, what to forget |
| `AG-13` | [48](../days/day-48-memory-design/LESSON.md) | Memory design — what to remember, what to forget |
| `AG-14` | [50](../days/day-50-chunking-and-top-k/LESSON.md) | Chunking, top-k & when RAG is the wrong tool |
| `AG-15` | [52](../days/day-52-memory-in-triage-flow/LESSON.md) | Phase gate — memory wired into the triage flow |
| `AG-16` | [55](../days/day-55-delegation-and-transfer/LESSON.md) | Delegation & transfer; agent-as-tool |
| `AG-17` | [56](../days/day-56/LESSON.md) | Planning patterns — plan-and-execute, replanning |
| `AG-18` | [56](../days/day-56/LESSON.md) | Planning patterns — plan-and-execute, replanning |
| `AG-19` | [57](../days/day-57/LESSON.md) | Multi-agent design — orchestrator, Writer↔Critic |
| `AG-20` | [57](../days/day-57/LESSON.md) | Multi-agent design — orchestrator, Writer↔Critic |
| `AG-21` | [59](../days/day-59/LESSON.md) | Phase gate + failure lab — loops, runaway agents, containment |
| `AG-22` | [60](../days/day-60/LESSON.md) | Durable execution — resume, replay, idempotency |
| `AG-23` | [62](../days/day-62/LESSON.md) | Human-in-the-loop patterns |
| `AG-24` | [73](../days/day-73/LESSON.md) | Ambient agents — the nightly job (re-index, full evals, digest) |
| `AG-25` | [77](../days/day-77/LESSON.md) | The standup agent — voice client over the queue state |
| `AG-26` | [79](../days/day-79/LESSON.md) | Evals are tests — evalsets, metrics, Flash-Lite as the eval workhorse |
| `AG-27` | [81](../days/day-81/LESSON.md) | LLM-as-judge & honest baselines |
| `AG-28` | [83](../days/day-83/LESSON.md) | Phase gate — Sutra's eval suite green |
| `AG-29` | [90](../days/day-90/LESSON.md) | Agent identity & the registry |
| `AG-30` | [91](../days/day-91/LESSON.md) | Integrations survey — Slack-shaped intake, ecosystems; paid-only items noted "requires … |
| `AG-31` | [71](../days/day-71/LESSON.md) | Computer use & the sandbox — browser agent vs a local dummy site; `e2b`/`daytona` 🅿️; e… |
| `AG-32` | [16](../days/day-16-built-in-tools-with-brakes/LESSON.md) | Built-in tools with brakes — search grounding (free-allowance check + open-source searc… |
| `AG-33` | [49](../days/day-49-retrieval-and-embeddings/LESSON.md) | Retrieval & embeddings — one honest RAG day (local embedding index over the ticket arch… |
| `AG-34` | [89](../days/day-89/LESSON.md) | A2A v1.0 — signed Agent Cards verified hands-on; AP2 mandates, x402/TAP 🅿️ — *know the … |

## Curriculum B — Google ADK (`ADK-`) — 78 IDs

| ID | Day | Day title |
| --- | --- | --- |
| `ADK-01` | [5](../days/day-05-first-adk-agent/LESSON.md) | First ADK agent — install `google-adk`, `Agent` + runner, pin `gemini-3.5-flash` explic… |
| `ADK-02` | [5](../days/day-05-first-adk-agent/LESSON.md) | First ADK agent — install `google-adk`, `Agent` + runner, pin `gemini-3.5-flash` explic… |
| `ADK-03` | [6](../days/day-06-instructions-and-personas/LESSON.md) | Instructions & personas; the `adk web` dev UI |
| `ADK-04` | [7](../days/day-07-events-and-streaming/LESSON.md) | Events & streaming — the 2.x event model (traps #2 and #3) |
| `ADK-05` | [7](../days/day-07-events-and-streaming/LESSON.md) | Events & streaming — the 2.x event model (traps #2 and #3) |
| `ADK-06` | [8](../days/day-08-sessions-and-services/LESSON.md) | Sessions, runs & in-memory services |
| `ADK-07` | [8](../days/day-08-sessions-and-services/LESSON.md) | Sessions, runs & in-memory services |
| `ADK-08` | [9](../days/day-09-four-free-providers/LESSON.md) | Same agent, four free providers — Gemini ↔ Groq ↔ OpenRouter `:free` ↔ Ollama via LiteL… |
| `ADK-09` | [9](../days/day-09-four-free-providers/LESSON.md) | Same agent, four free providers — Gemini ↔ Groq ↔ OpenRouter `:free` ↔ Ollama via LiteL… |
| `ADK-10` | [10](../days/day-10-function-tools/LESSON.md) | Function tools in ADK — from Day 4's hand-rolled version to `FunctionTool` |
| `ADK-11` | [10](../days/day-10-function-tools/LESSON.md) | Function tools in ADK — from Day 4's hand-rolled version to `FunctionTool` |
| `ADK-12` | [11](../days/day-11-tool-context/LESSON.md) | Tool context & state in tools; tool design principles |
| `ADK-13` | [12](../days/day-12-structured-output/LESSON.md) | Structured output — schemas on the way out |
| `ADK-14` | [13](../days/day-13-callbacks-four-doors/LESSON.md) | Callbacks — before/after model & tool |
| `ADK-15` | [13](../days/day-13-callbacks-four-doors/LESSON.md) | Callbacks — before/after model & tool |
| `ADK-16` | [14](../days/day-14-plugins-one-layer-up/LESSON.md) | Plugins — cross-cutting behavior |
| `ADK-17` | [15](../days/day-15-toolsets-and-openapi/LESSON.md) | Toolsets, OpenAPI & third-party tool wrappers |
| `ADK-18` | [16](../days/day-16-built-in-tools-with-brakes/LESSON.md) | Built-in tools with brakes — search grounding (free-allowance check + open-source searc… |
| `ADK-19` | [17](../days/day-17-state-scopes-and-lifetimes/LESSON.md) | Session state deep dive — prefixes, scopes, lifetimes |
| `ADK-20` | [17](../days/day-17-state-scopes-and-lifetimes/LESSON.md) | Session state deep dive — prefixes, scopes, lifetimes |
| `ADK-21` | [18](../days/day-18-artifacts-that-survive/LESSON.md) | Artifacts — files that survive turns |
| `ADK-22` | [20](../days/day-20-context-engineering-compaction/LESSON.md) | Context engineering II — compaction & summarization |
| `ADK-23` | [21](../days/day-21-errors-surface-not-swallow/LESSON.md) | Error handling — surface, don't swallow (trap #4) |
| `ADK-24` | [26](../days/day-26-loading-skills-into-adk/LESSON.md) | `SkillToolset` — loading skills into ADK |
| `ADK-25` | [39](../days/day-39-database-tools/LESSON.md) | Database tools — MCP Toolbox for Databases vs hand-written DB tools; 2.6 extras awareness |
| `ADK-26` | [42](../days/day-42-serving-agents-over-mcp/LESSON.md) | Serving agents over MCP — `to_mcp_server`; agent-as-tool vs agent-as-peer |
| `ADK-27` | [46](../days/day-46-sessions-vs-memory/LESSON.md) | Sessions vs memory — `MemoryService` semantics |
| `ADK-28` | [46](../days/day-46-sessions-vs-memory/LESSON.md) | Sessions vs memory — `MemoryService` semantics |
| `ADK-29` | [47](../days/day-47-persistent-sessions/LESSON.md) | Persistent sessions — database-backed |
| `ADK-30` | [49](../days/day-49-retrieval-and-embeddings/LESSON.md) | Retrieval & embeddings — one honest RAG day (local embedding index over the ticket arch… |
| `ADK-31` | [51](../days/day-51-caching-the-quota-lifeline/LESSON.md) | Caching — context & response caching as the quota lifeline |
| `ADK-32` | [53](../days/day-53-graph-workflow-runtime/LESSON.md) | The graph Workflow Runtime — nodes, edges, the 2.x composition model (trap #1) |
| `ADK-33` | [53](../days/day-53-graph-workflow-runtime/LESSON.md) | The graph Workflow Runtime — nodes, edges, the 2.x composition model (trap #1) |
| `ADK-34` | [53](../days/day-53-graph-workflow-runtime/LESSON.md) | The graph Workflow Runtime — nodes, edges, the 2.x composition model (trap #1) |
| `ADK-35` | [54](../days/day-54-sequential-parallel-loop/LESSON.md) | Sequential, parallel & loop patterns |
| `ADK-36` | [54](../days/day-54-sequential-parallel-loop/LESSON.md) | Sequential, parallel & loop patterns |
| `ADK-37` | [54](../days/day-54-sequential-parallel-loop/LESSON.md) | Sequential, parallel & loop patterns |
| `ADK-38` | [55](../days/day-55-delegation-and-transfer/LESSON.md) | Delegation & transfer; agent-as-tool |
| `ADK-39` | [55](../days/day-55-delegation-and-transfer/LESSON.md) | Delegation & transfer; agent-as-tool |
| `ADK-40` | [57](../days/day-57/LESSON.md) | Multi-agent design — orchestrator, Writer↔Critic |
| `ADK-41` | [58](../days/day-58/LESSON.md) | The triage graph v1 — intake→classify→research→draft→review, end to end |
| `ADK-42` | [58](../days/day-58/LESSON.md) | The triage graph v1 — intake→classify→research→draft→review, end to end |
| `ADK-43` | [60](../days/day-60/LESSON.md) | Durable execution — resume, replay, idempotency |
| `ADK-44` | [61](../days/day-61/LESSON.md) | Pause/resume & checkpoints in ADK |
| `ADK-45` | [61](../days/day-61/LESSON.md) | Pause/resume & checkpoints in ADK |
| `ADK-46` | [62](../days/day-62/LESSON.md) | Human-in-the-loop patterns |
| `ADK-47` | [63](../days/day-63/LESSON.md) | Approval gates — design (what needs a human, and why) |
| `ADK-48` | [64](../days/day-64/LESSON.md) | Approval gates — build; HITL resumption for standalone nodes + `NodeTool` (2.5) |
| `ADK-49` | [70](../days/day-70/LESSON.md) | The Quota-Router plugin — requests-remaining per provider per window; route to headroom |
| `ADK-50` | [71](../days/day-71/LESSON.md) | Computer use & the sandbox — browser agent vs a local dummy site; `e2b`/`daytona` 🅿️; e… |
| `ADK-51` | [73](../days/day-73/LESSON.md) | Ambient agents — the nightly job (re-index, full evals, digest) |
| `ADK-52` | [74](../days/day-74/LESSON.md) | Live API I — streaming architecture; free-quota check (SSE-text + browser speech fallba… |
| `ADK-53` | [74](../days/day-74/LESSON.md) | Live API I — streaming architecture; free-quota check (SSE-text + browser speech fallba… |
| `ADK-54` | [75](../days/day-75/LESSON.md) | Live API II — the bidi voice loop |
| `ADK-55` | [75](../days/day-75/LESSON.md) | Live API II — the bidi voice loop |
| `ADK-56` | [76](../days/day-76/LESSON.md) | VAD events & non-blocking tools (2.5) — the conversation doesn't freeze mid-tool |
| `ADK-57` | [77](../days/day-77/LESSON.md) | The standup agent — voice client over the queue state |
| `ADK-58` | [79](../days/day-79/LESSON.md) | Evals are tests — evalsets, metrics, Flash-Lite as the eval workhorse |
| `ADK-59` | [79](../days/day-79/LESSON.md) | Evals are tests — evalsets, metrics, Flash-Lite as the eval workhorse |
| `ADK-60` | [80](../days/day-80/LESSON.md) | Trajectory & rubric evaluation — `RubricBasedMultiTurnTrajectoryEvaluator` (2.2); "esca… |
| `ADK-61` | [81](../days/day-81/LESSON.md) | LLM-as-judge & honest baselines |
| `ADK-62` | [82](../days/day-82/LESSON.md) | Regression discipline — evals in CI; full runs ride the Day 73 nightly |
| `ADK-63` | [84](../days/day-84/LESSON.md) | Tracing — OTel + `AutoTracingPlugin` (2.2): every node, tool call & model call in the t… |
| `ADK-64` | [85](../days/day-85/LESSON.md) | The API surface — `api_server`, FastAPI endpoints |
| `ADK-65` | [85](../days/day-85/LESSON.md) | The API surface — `api_server`, FastAPI endpoints |
| `ADK-66` | [86](../days/day-86/LESSON.md) | Containerize — Cloud-Run-shaped locally: `docker compose`, stateless container, env-inj… |
| `ADK-67` | [86](../days/day-86/LESSON.md) | Containerize — Cloud-Run-shaped locally: `docker compose`, stateless container, env-inj… |
| `ADK-68` | [87](../days/day-87/LESSON.md) | Agent Engine — documented walkthrough (config written, not billed) 🅿️ |
| `ADK-69` | [88](../days/day-88/LESSON.md) | Kubernetes on the laptop — kind/k3d, the MCP-sidecar pattern |
| `ADK-70` | [89](../days/day-89/LESSON.md) | A2A v1.0 — signed Agent Cards verified hands-on; AP2 mandates, x402/TAP 🅿️ — *know the … |
| `ADK-71` | [90](../days/day-90/LESSON.md) | Agent identity & the registry |
| `ADK-72` | [91](../days/day-91/LESSON.md) | Integrations survey — Slack-shaped intake, ecosystems; paid-only items noted "requires … |
| `ADK-73` | [5](../days/day-05-first-adk-agent/LESSON.md) | First ADK agent — install `google-adk`, `Agent` + runner, pin `gemini-3.5-flash` explic… |
| `ADK-74` | [84](../days/day-84/LESSON.md) | Tracing — OTel + `AutoTracingPlugin` (2.2): every node, tool call & model call in the t… |
| `ADK-75` | [80](../days/day-80/LESSON.md) | Trajectory & rubric evaluation — `RubricBasedMultiTurnTrajectoryEvaluator` (2.2); "esca… |
| `ADK-76` | [64](../days/day-64/LESSON.md) | Approval gates — build; HITL resumption for standalone nodes + `NodeTool` (2.5) |
| `ADK-77` | [76](../days/day-76/LESSON.md) | VAD events & non-blocking tools (2.5) — the conversation doesn't freeze mid-tool |
| `ADK-78` | [39](../days/day-39-database-tools/LESSON.md) | Database tools — MCP Toolbox for Databases vs hand-written DB tools; 2.6 extras awareness |

## Curriculum C — MCP (`MCP-`) — 33 IDs

| ID | Day | Day title |
| --- | --- | --- |
| `MCP-01` | [32](../days/day-32-mcp-stateless-core/LESSON.md) | MCP 2026 — the stateless core (headers, cacheable lists), governance & registry; the ph… |
| `MCP-02` | [33](../days/day-33-client-and-transports/LESSON.md) | The client side — connect Sutra to servers; transports (stdio + Streamable HTTP; SSE as… |
| `MCP-03` | [33](../days/day-33-client-and-transports/LESSON.md) | The client side — connect Sutra to servers; transports (stdio + Streamable HTTP; SSE as… |
| `MCP-04` | [34](../days/day-34-building-sutra-mcp-tools/LESSON.md) | Building `sutra-mcp` I — tools; stateless lifecycle (the old handshake as history) |
| `MCP-05` | [34](../days/day-34-building-sutra-mcp-tools/LESSON.md) | Building `sutra-mcp` I — tools; stateless lifecycle (the old handshake as history) |
| `MCP-06` | [34](../days/day-34-building-sutra-mcp-tools/LESSON.md) | Building `sutra-mcp` I — tools; stateless lifecycle (the old handshake as history) |
| `MCP-07` | [35](../days/day-35-resources-and-prompts/LESSON.md) | Resources & prompts |
| `MCP-08` | [35](../days/day-35-resources-and-prompts/LESSON.md) | Resources & prompts |
| `MCP-09` | [35](../days/day-35-resources-and-prompts/LESSON.md) | Resources & prompts |
| `MCP-10` | [36](../days/day-36-long-jobs-and-tasks/LESSON.md) | Long jobs — progress, the Tasks extension (`tasks/get |
| `MCP-11` | [38](../days/day-38-failure-and-migration-lab/LESSON.md) | Failure & migration lab — timeouts, malformed servers; deprecated Roots/Sampling/Loggin… |
| `MCP-12` | [38](../days/day-38-failure-and-migration-lab/LESSON.md) | Failure & migration lab — timeouts, malformed servers; deprecated Roots/Sampling/Loggin… |
| `MCP-13` | [37](../days/day-37-auth-and-elicitation/LESSON.md) | Auth & enterprise — OAuth2 + RFC 9207 issuer validation + CIMD; elicitation (incl. URL-… |
| `MCP-14` | [36](../days/day-36-long-jobs-and-tasks/LESSON.md) | Long jobs — progress, the Tasks extension (`tasks/get |
| `MCP-15` | [39](../days/day-39-database-tools/LESSON.md) | Database tools — MCP Toolbox for Databases vs hand-written DB tools; 2.6 extras awareness |
| `MCP-16` | [40](../days/day-40-filtering-and-allowlists/LESSON.md) | Tool filtering, allowlists & MCP security posture |
| `MCP-17` | [40](../days/day-40-filtering-and-allowlists/LESSON.md) | Tool filtering, allowlists & MCP security posture |
| `MCP-18` | [41](../days/day-41-capabilities-and-mcp-apps/LESSON.md) | Server capabilities & MCP Apps — sandboxed-iframe UIs, pre-declared templates |
| `MCP-19` | [41](../days/day-41-capabilities-and-mcp-apps/LESSON.md) | Server capabilities & MCP Apps — sandboxed-iframe UIs, pre-declared templates |
| `MCP-20` | [43](../days/day-43-stateless-by-default/LESSON.md) | Stateless by default — deploy-shaped servers; any instance answers any request |
| `MCP-21` | [43](../days/day-43-stateless-by-default/LESSON.md) | Stateless by default — deploy-shaped servers; any instance answers any request |
| `MCP-22` | [44](../days/day-44-client-hardening/LESSON.md) | Client hardening — retries, timeouts, no held connections |
| `MCP-23` | [44](../days/day-44-client-hardening/LESSON.md) | Client hardening — retries, timeouts, no held connections |
| `MCP-24` | [45](../days/day-45-the-mcp-audit/LESSON.md) | Phase gate — full MCP audit of sutra-core |
| `MCP-25` | [45](../days/day-45-the-mcp-audit/LESSON.md) | Phase gate — full MCP audit of sutra-core |
| `MCP-26` | [32](../days/day-32-mcp-stateless-core/LESSON.md) | MCP 2026 — the stateless core (headers, cacheable lists), governance & registry; the ph… |
| `MCP-27` | [37](../days/day-37-auth-and-elicitation/LESSON.md) | Auth & enterprise — OAuth2 + RFC 9207 issuer validation + CIMD; elicitation (incl. URL-… |
| `MCP-28` | [36](../days/day-36-long-jobs-and-tasks/LESSON.md) | Long jobs — progress, the Tasks extension (`tasks/get |
| `MCP-29` | [41](../days/day-41-capabilities-and-mcp-apps/LESSON.md) | Server capabilities & MCP Apps — sandboxed-iframe UIs, pre-declared templates |
| `MCP-30` | [37](../days/day-37-auth-and-elicitation/LESSON.md) | Auth & enterprise — OAuth2 + RFC 9207 issuer validation + CIMD; elicitation (incl. URL-… |
| `MCP-31` | [38](../days/day-38-failure-and-migration-lab/LESSON.md) | Failure & migration lab — timeouts, malformed servers; deprecated Roots/Sampling/Loggin… |
| `MCP-32` | [32](../days/day-32-mcp-stateless-core/LESSON.md) | MCP 2026 — the stateless core (headers, cacheable lists), governance & registry; the ph… |
| `MCP-33` | [42](../days/day-42-serving-agents-over-mcp/LESSON.md) | Serving agents over MCP — `to_mcp_server`; agent-as-tool vs agent-as-peer |

## Curriculum D — Agent Skills (`SK-`) — 20 IDs

| ID | Day | Day title |
| --- | --- | --- |
| `SK-01` | [25](../days/day-25-skills-the-open-spec/LESSON.md) | Skills: the open spec — `SKILL.md` anatomy |
| `SK-02` | [25](../days/day-25-skills-the-open-spec/LESSON.md) | Skills: the open spec — `SKILL.md` anatomy |
| `SK-03` | [25](../days/day-25-skills-the-open-spec/LESSON.md) | Skills: the open spec — `SKILL.md` anatomy |
| `SK-04` | [26](../days/day-26-loading-skills-into-adk/LESSON.md) | `SkillToolset` — loading skills into ADK |
| `SK-05` | [26](../days/day-26-loading-skills-into-adk/LESSON.md) | `SkillToolset` — loading skills into ADK |
| `SK-06` | [27](../days/day-27-authoring-first-skills/LESSON.md) | Authoring Sutra's first skills |
| `SK-07` | [27](../days/day-27-authoring-first-skills/LESSON.md) | Authoring Sutra's first skills |
| `SK-08` | [27](../days/day-27-authoring-first-skills/LESSON.md) | Authoring Sutra's first skills |
| `SK-09` | [28](../days/day-28-progressive-disclosure-design/LESSON.md) | Progressive disclosure & skill design |
| `SK-10` | [28](../days/day-28-progressive-disclosure-design/LESSON.md) | Progressive disclosure & skill design |
| `SK-11` | [28](../days/day-28-progressive-disclosure-design/LESSON.md) | Progressive disclosure & skill design |
| `SK-12` | [29](../days/day-29-sourcing-and-auditing-skills/LESSON.md) | Sourcing & auditing third-party skills — provenance ledger; Agent Registry endpoint |
| `SK-13` | [29](../days/day-29-sourcing-and-auditing-skills/LESSON.md) | Sourcing & auditing third-party skills — provenance ledger; Agent Registry endpoint |
| `SK-14` | [29](../days/day-29-sourcing-and-auditing-skills/LESSON.md) | Sourcing & auditing third-party skills — provenance ledger; Agent Registry endpoint |
| `SK-15` | [29](../days/day-29-sourcing-and-auditing-skills/LESSON.md) | Sourcing & auditing third-party skills — provenance ledger; Agent Registry endpoint |
| `SK-16` | [29](../days/day-29-sourcing-and-auditing-skills/LESSON.md) | Sourcing & auditing third-party skills — provenance ledger; Agent Registry endpoint |
| `SK-17` | [30](../days/day-30-skill-testing-and-versioning/LESSON.md) | Skill testing & versioning |
| `SK-18` | [30](../days/day-30-skill-testing-and-versioning/LESSON.md) | Skill testing & versioning |
| `SK-19` | [30](../days/day-30-skill-testing-and-versioning/LESSON.md) | Skill testing & versioning |
| `SK-20` | [31](../days/day-31-the-quality-gate/LESSON.md) | Quality gate — `./m check`: lint, tests, skills lint, `:free`-suffix lint |

## Curriculum E — Operations (`OPS-`) — 18 IDs

| ID | Day | Day title |
| --- | --- | --- |
| `OPS-01` | [1](../days/day-01-bootstrap-and-map/LESSON.md) | Bootstrap & the map — repo, `.env`+`.gitignore`, uv+Python 3.12, ledgers & `scripts/tra… |
| `OPS-02` | [1](../days/day-01-bootstrap-and-map/LESSON.md) | Bootstrap & the map — repo, `.env`+`.gitignore`, uv+Python 3.12, ledgers & `scripts/tra… |
| `OPS-03` | [1](../days/day-01-bootstrap-and-map/LESSON.md) | Bootstrap & the map — repo, `.env`+`.gitignore`, uv+Python 3.12, ledgers & `scripts/tra… |
| `OPS-04` | [22](../days/day-22-structured-logging/LESSON.md) | Structured logging — every turn tells its story |
| `OPS-05` | [23](../days/day-23-testing-tools-and-callbacks/LESSON.md) | Testing agents I — unit tests for tools & callbacks |
| `OPS-06` | [23](../days/day-23-testing-tools-and-callbacks/LESSON.md) | Testing agents I — unit tests for tools & callbacks |
| `OPS-07` | [24](../days/day-24-token-accounting-and-budgets/LESSON.md) | Token accounting & budgets — denominated in quota (RPM/RPD), not dollars |
| `OPS-08` | [31](../days/day-31-the-quality-gate/LESSON.md) | Quality gate — `./m check`: lint, tests, skills lint, `:free`-suffix lint |
| `OPS-09` | [45](../days/day-45-the-mcp-audit/LESSON.md) | Phase gate — full MCP audit of sutra-core |
| `OPS-10` | [51](../days/day-51-caching-the-quota-lifeline/LESSON.md) | Caching — context & response caching as the quota lifeline |
| `OPS-11` | [65](../days/day-65/LESSON.md) | Phase gate — kill it mid-run; durable triage with human approval |
| `OPS-12` | [70](../days/day-70/LESSON.md) | The Quota-Router plugin — requests-remaining per provider per window; route to headroom |
| `OPS-13` | [72](../days/day-72/LESSON.md) | Backoff with honesty — `retry-after`, 1→2→4→8s, escalate after N; never invent a result |
| `OPS-14` | [78](../days/day-78/LESSON.md) | Phase gate — ambient + voice, inside free quota |
| `OPS-15` | [82](../days/day-82/LESSON.md) | Regression discipline — evals in CI; full runs ride the Day 73 nightly |
| `OPS-16` | [84](../days/day-84/LESSON.md) | Tracing — OTel + `AutoTracingPlugin` (2.2): every node, tool call & model call in the t… |
| `OPS-17` | [86](../days/day-86/LESSON.md) | Containerize — Cloud-Run-shaped locally: `docker compose`, stateless container, env-inj… |
| `OPS-18` | [88](../days/day-88/LESSON.md) | Kubernetes on the laptop — kind/k3d, the MCP-sidecar pattern |

## Curriculum F — Safety & Security (`SEC-`) — 16 IDs

| ID | Day | Day title |
| --- | --- | --- |
| `SEC-01` | [16](../days/day-16-built-in-tools-with-brakes/LESSON.md) | Built-in tools with brakes — search grounding (free-allowance check + open-source searc… |
| `SEC-02` | [21](../days/day-21-errors-surface-not-swallow/LESSON.md) | Error handling — surface, don't swallow (trap #4) |
| `SEC-03` | [40](../days/day-40-filtering-and-allowlists/LESSON.md) | Tool filtering, allowlists & MCP security posture |
| `SEC-04` | [59](../days/day-59/LESSON.md) | Phase gate + failure lab — loops, runaway agents, containment |
| `SEC-05` | [63](../days/day-63/LESSON.md) | Approval gates — design (what needs a human, and why) |
| `SEC-06` | [66](../days/day-66/LESSON.md) | Threat model — prompt injection & the lethal trifecta |
| `SEC-07` | [66](../days/day-66/LESSON.md) | Threat model — prompt injection & the lethal trifecta |
| `SEC-08` | [67](../days/day-67/LESSON.md) | Defense in depth — input/output guardrail callbacks |
| `SEC-09` | [67](../days/day-67/LESSON.md) | Defense in depth — input/output guardrail callbacks |
| `SEC-10` | [68](../days/day-68/LESSON.md) | Permissions & least privilege for tools |
| `SEC-11` | [68](../days/day-68/LESSON.md) | Permissions & least privilege for tools |
| `SEC-12` | [69](../days/day-69/LESSON.md) | PII & data boundaries — synthetic data only, free-tier training caveat |
| `SEC-13` | [69](../days/day-69/LESSON.md) | PII & data boundaries — synthetic data only, free-tier training caveat |
| `SEC-14` | [71](../days/day-71/LESSON.md) | Computer use & the sandbox — browser agent vs a local dummy site; `e2b`/`daytona` 🅿️; e… |
| `SEC-15` | [72](../days/day-72/LESSON.md) | Backoff with honesty — `retry-after`, 1→2→4→8s, escalate after N; never invent a result |
| `SEC-16` | [92](../days/day-92/LESSON.md) | Hardening pass — full security review before going public |

**199 IDs across 6 curricula.**

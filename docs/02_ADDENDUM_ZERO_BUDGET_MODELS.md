# 💸 Addendum 02 — Zero-Budget Model Policy (Free LLMs Only)

> **Constraint:** no paid API keys, no billing accounts, no subscriptions for model inference.
> **Available:** a free Gemini API key (AI Studio) · a free Groq key · a free OpenRouter key · Ollama (local).
> **Verified against provider docs on 2026-08-12.** Free tiers change often (Google cut quotas in
> Dec 2025 with little warning) — so per Principle 14, every day that names a model **looks up the
> live free list first** and records it in `PACKAGES.md`-style ledger rows.
>
> Where this addendum conflicts with `00_MASTER_PLAN.md` or Addendum 01, **this addendum wins**
> for anything involving model choice or paid services.

---

## 1. The policy in one sentence

**Sutra runs entirely on free tiers: Gemini Flash-class models as the primary brain, Groq and
OpenRouter free models as the swap/fallback providers, Ollama for fully-offline — and every
rate-limit ceiling is treated as a curriculum feature, not an obstacle.**

---

## 2. Your three keys, in simple language

| Key | What it really is | Simple explanation | Best used for in Sutra |
| --- | ----------------- | ------------------ | ---------------------- |
| **Gemini API key** (from AI Studio, aistudio.google.com) | Google's developer free tier. No credit card. | One key, Google's own models. ADK speaks Gemini natively — zero adapters. *Example: `Agent(model="gemini-2.5-flash", ...)` just works with this key.* | **Primary.** Every agent's default brain; also grounding, evals, and (limits permitting) Live voice. |
| **Groq key** (console.groq.com) | Free access to open-weight models (Llama, Qwen, Kimi K2, GPT-OSS…) on very fast custom chips. No credit card, no token charges — only rate limits. | Not "Grok" (that's xAI). Groq is an inference company: same open models, absurdly fast. *Example: a triage classification that takes 3 s on a busy tier returns in well under a second on Groq.* | **Speed lane + swap-proof.** The Day 9 "same agent, different model" demo; latency-sensitive nodes like the classifier. |
| **OpenRouter key** (openrouter.ai) | One key that routes to many providers; models tagged `:free` cost nothing. ~20 req/min, ~50 req/day on the free floor. | An aggregator: one API shape, dozens of models behind it. *Example: try DeepSeek R1's reasoning on the Critic agent without signing up anywhere new.* | **Breadth + reasoning experiments.** Trying model families Gemini/Groq don't have; the Writer↔Critic comparisons. Low daily quota → use sparingly. |
| **Ollama** (no key) | Models running on your own laptop. | Free forever, offline, private, no rate limits — but slower and smaller models. *Example: run the whole intake graph on a plane.* | **The zero-dependency baseline** and the privacy lane. Already in the plan (ADK-08). |

🔑 **All three keys live in `.env`, never in code, never committed** (OPS-02 already covers this):

```bash
# .env  (add to .gitignore on Day 1 — the plan already does this)
GOOGLE_API_KEY=...
GOOGLE_GENAI_USE_VERTEXAI=FALSE     # tells ADK: use the free AI Studio API, not paid Vertex
GROQ_API_KEY=...
OPENROUTER_API_KEY=...
```

---

## 3. The free model lineup (baseline 2026-08-12 — always re-verify)

> ⚠️ **The lookup rule:** free rosters and quotas move. Before pinning any model, check:
> Gemini → the AI Studio rate-limit view for *your* project · Groq → console.groq.com/settings/limits
> · OpenRouter → the models page filtered to `:free`. Record what you found, with the date.

| Provider | Free workhorses (at baseline) | Approx. free limits (at baseline) | Notes |
| -------- | ----------------------------- | ---------------------------------- | ----- |
| **Gemini** | `gemini-2.5-flash`, `gemini-2.5-flash-lite`; Gemini 3 Flash preview (tighter limits) | Flash ≈ 10–15 RPM / a few hundred RPD; Flash-Lite higher RPD; 1M-token context | Pro-class models are effectively behind billing now — **the plan must never assume a Pro model.** Limits are per *project*, not per key. |
| **Groq** | Llama 3.3 70B, Llama 4 Scout, Qwen 3, Kimi K2, GPT-OSS 120B (all open-weight) | ≈ 30 RPM / 6K tokens-per-min / ~1K RPD per **organization** | 429 responses include exact retry-after + remaining-quota headers — perfect for teaching backoff. |
| **OpenRouter** | `deepseek/deepseek-r1:free`, Llama 4 Scout `:free`, Qwen3 Coder `:free`, Gemma 3 `:free`, and ~25 more | 20 RPM / ~50 RPD on the free floor | The `:free` suffix in the model ID is what makes it free — **a missing `:free` can bill a paid model**; the CLAUDE.md guardrail below prevents this. |
| **Ollama** | Whatever your RAM fits (e.g. Llama 3.x 8B, Qwen 3 small, Gemma 3) | None — your hardware is the limit | ~8 GB RAM runs 7–8B models fine for Sutra's purposes. |

---

## 4. How each provider wires into ADK (the Day 9 code shapes)

**Gemini — native (no adapter):**

```python
from google.adk.agents import Agent
agent = Agent(model="gemini-2.5-flash", ...)   # reads GOOGLE_API_KEY from .env
```

**Groq and OpenRouter — via LiteLLM** (already in the plan's stack for exactly this job):

```python
from google.adk.models.lite_llm import LiteLlm

groq_agent   = Agent(model=LiteLlm(model="groq/llama-3.3-70b-versatile"), ...)
router_agent = Agent(model=LiteLlm(model="openrouter/deepseek/deepseek-r1:free"), ...)
```

**Ollama — via LiteLLM, pointed at localhost:**

```python
local_agent = Agent(model=LiteLlm(model="ollama_chat/llama3.1:8b"), ...)
```

> 💡 **Simple mental model:** ADK speaks Gemini natively; LiteLLM is a universal translator that
> makes every other provider *look like* one API. One import, four providers, zero dollars.
> (Exact model strings above are examples — apply the §3 lookup rule on the day you use them.)

---

## 5. Day-by-day amendments (what changes in the 96 days)

| Day(s) | Original assumption | Zero-budget amendment |
| ------ | -------------------- | --------------------- |
| 5–8 | Any Gemini model | Pin `gemini-2.5-flash` explicitly (never rely on ADK's default — since 2.2 the default is a preview model whose free quota is tighter). Flash-Lite for high-volume/low-stakes calls. |
| **9** | Model swap: Gemini / Claude / OpenAI / Ollama | **Better version:** Gemini (free) ↔ Groq ↔ OpenRouter `:free` ↔ Ollama. Same agent, four providers, one benchmark table (quality / latency / RPD budget). Claude & OpenAI become a 🅿️ *reading* comparison — the wiring is identical LiteLLM syntax, so the skill transfers the day you ever get a paid key. |
| 9 (routing) | Cost-aware routing via paid gateways | **Quota-aware routing** (see §6) — genuinely more instructive. |
| 16 | Google Search grounding | Grounding has a limited free allowance that changes — check the pricing page that day. **Fallback that teaches more:** a free open-source web-search MCP server (Phase 5 skill arriving early) so research still cites sources at $0. |
| 24, 51, 70 | Token/cost budgets as theory | Now enforced by reality: the budget plugin tracks **RPD/RPM per provider**, not dollars. |
| 74–78 (Live/voice) | Gemini Live API | Free-tier Live quota exists but is tight (few concurrent sessions). Check AI Studio that week. **Fallback demo (still impressive):** SSE text streaming + the browser's built-in free SpeechRecognition/speechSynthesis in the single-file voice client — voice UX, zero API audio cost. Keep the Live API lesson; run it briefly within quota. |
| 79–83 (Evals) | Many LLM calls | Run evals on **Flash-Lite** (highest RPD); keep per-run evalsets small (10–15 cases dev, full 60+ only at phase gates); schedule full runs as the Day 73 ambient *nightly* job so daily quota resets work for you. |
| 84–85 | OTel + API server | No change — all local and free. |
| **86–88 (Deploy)** | Cloud Run / Agent Engine / GKE (need a GCP billing account) | **Zero-cash equivalents that teach the same lessons:** Day 86 → build the same Dockerfile, run "Cloud-Run-shaped" locally with `docker compose` (stateless container + env-injected secrets + health checks). Day 87 → Agent Engine becomes a documented walkthrough (reading + config files written, not executed). Day 88 → GKE lesson runs on **kind or k3d** — a real Kubernetes cluster on your laptop, free, including the MCP-sidecar pattern. If you ever attach GCP's free-trial credits, every artifact is ready to `gcloud deploy` unchanged. |
| 91 | OpenAI Responses API labs, paid integrations | Skip paid-only items; note them in the integrations survey as "requires budget". |

📌 **Net effect on the 96 days: zero days added, zero concepts lost.** Two deployment days change
*where* things run, not *what* you learn — the Dockerfile, manifests, and sidecar patterns are identical.

---

## 6. Rate limits ARE the curriculum (the honest reframe)

> 🎬 **The scene:** your classifier works. On request #11 in a minute, Gemini returns HTTP 429.
> 😬 **The naive fix:** retry immediately in a loop. 💥 **Why it fails:** you burn your *daily*
> quota fighting the *minute* quota, and now Sutra is down until midnight.
> 💡 **The insight:** free tiers force the exact engineering that separates demos from products —
> and paid users usually skip it until production teaches them expensively.

Concrete additions (fold into existing days, mostly Phase 10):

1. **Exponential backoff with honesty** (Day 72): respect `retry-after`; 1s → 2s → 4s → 8s; give up
   and escalate after N tries — never invent a result (the plan's rule already).
2. **The Quota-Router plugin** (Day 70, replaces the dollar-budget plugin's currency): tracks
   requests-remaining per provider per window; routes each call to whoever has headroom.
   *Example: classifier → Groq (30 RPM lane); deep reasoning → Gemini Flash; overnight evals →
   Flash-Lite; everything → Ollama when all clouds are exhausted.* This is ADK-09 model routing
   with a real, measurable objective.
3. **Caching pays instantly** (Day 51): context caching and response caching aren't cost
   *optimizations* anymore — they're the difference between finishing the day inside quota or not.
4. **Interview gold:** "Tell me about handling rate limits in a multi-agent system" — you will have
   a war story with numbers, which beats any paid-tier answer.

---

## 7. Rules & risks of the free lane (non-negotiable)

- 🔒 **Never commit a key.** `.env` + `.gitignore` from Day 1; the repo will be public in Phase 14.
- 🚫 **No quota evasion.** Don't create multiple accounts/keys to dodge limits — it violates
  provider terms (and Groq/Gemini meter per org/project anyway, so it barely works). The
  Quota-Router across *different* providers is the legitimate version of the same idea.
- 🕵️ **Free tiers may train on your data.** Google's free tier can use prompts/responses for
  improvement. Sutra's "company data" is synthetic anyway (the plan already does this) — keep it
  that way: **never feed real personal or employer data through free endpoints.**
- 📉 **Quotas shrink without much notice** (Dec 2025 precedent). The weekly phase-gate freshness
  check now includes: *"re-check all three providers' free limits; if a model Sutra pins lost its
  free tier, amend the plan first."*
- 🏷️ **OpenRouter: `:free` suffix or it isn't free.** Lint rule: any `openrouter/` model string in
  the repo must end in `:free` (add to `make check` on Day 31 alongside the skills lint).

Add this block to `CLAUDE.md` so Claude Code enforces it every session:

```markdown
Zero-budget rules (Addendum 02 wins over the master plan on model choice):
- Only free-tier models: Gemini Flash-class (GOOGLE_API_KEY, VERTEXAI=FALSE),
  Groq, OpenRouter models ending in ":free", or local Ollama.
- Never write code that requires a billing account, paid model, or paid API
  (no Claude/OpenAI/Vertex calls, no Cloud Run deploy commands as required steps).
- Before pinning any model string, look up the provider's current free list
  and record model + date in the ledger. Never invent a model name.
- Every model call path must handle HTTP 429 with retry-after + backoff.
```

---

## 8. If the *driver* (Claude Code) is also out of budget

The master plan uses Claude Code as the day-doc generator. Claude Code needs a Claude
subscription or Console credits. If that's not available either, the workflow survives unchanged
with a free driver:

- **Gemini CLI** — Google's open-source terminal agent; free tier with a personal Google account
  (generous daily allowance — verify current limits at the official docs). It reads a repo context
  file just like `CLAUDE.md` does (`GEMINI.md`; it also respects `AGENTS.md`). Copy your standing
  prompt into that file, and "generate day 1" works identically.
- The plan's deepest design choice makes this painless: **the repo is the memory, not the chat** —
  ledgers + day docs mean *any* capable CLI agent can pick up exactly where the last one stopped.

---

## 9. Merge checklist

- [ ] Fold §5's day amendments into §14 of the master plan; bump plan version.
- [ ] Replace Day 9's model matrix with the four-free-provider version.
- [ ] Rename the Day 70 budget plugin objective: dollars → quota (RPM/RPD per provider).
- [ ] Rewrite Days 86–88 targets: docker compose / documented Agent Engine / kind-or-k3d.
- [ ] Append the zero-budget block to `CLAUDE.md`.
- [ ] Add the `:free`-suffix lint to Day 31's `make check`.
- [ ] Log in `CHANGELOG_PLAN.md`: "2026-08-12 — Addendum 02: zero-budget model policy."

---

*The uncomfortable truth, stated kindly: a hiring manager cannot tell from your repo whether the
tokens were free. They can tell whether the system is well-engineered — and quota-aware routing,
honest backoff, and a local-Kubernetes deploy are* better *evidence than a paid bill would be.* 🚀

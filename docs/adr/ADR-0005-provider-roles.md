# ADR-0005 — Each free provider gets one named role

- **Date:** 2026-08-23
- **Day:** 1
- **Phase:** 1
- **Status:** accepted
- **Related:** Addendum 02 §2, §3 · tested by Day 9 (ADK-08, ADK-09)

## Context

Sutra runs on $0 (Principle 15). Three free API keys are available — Gemini AI Studio, Groq,
OpenRouter — plus local Ollama. Verified on the providers' own pages, 2026-08-23:

| Provider | Observed free limits | Notes |
| --- | --- | --- |
| Gemini | not published in the docs; per-project, read from the AI Studio dashboard | Flash-class stable ids documented; Pro effectively behind billing |
| Groq | 30 RPM; RPD and TPM vary per model; **per organization** | 429 carries `retry-after` + `x-ratelimit-remaining-*` |
| OpenRouter | 20 RPM; 50 RPD free floor, 1000 RPD once ≥$10 credit ever purchased | the `:free` suffix is what makes a model free |
| Ollama | none — local hardware is the limit | no key, offline, smaller models |

Without a stated role per provider, calls land wherever the code happens to point, and quota
exhaustion becomes unpredictable rather than budgeted.

## Options considered

| Option | Pros | Cons |
| --- | --- | --- |
| A. One provider for everything (Gemini) | simplest; native to ADK, no adapter | one 429 stops the whole desk; wastes Groq's separate quota pool |
| B. Round-robin across all three | spreads load evenly | ignores that the providers differ in latency and context size; a reasoning task lands on a fast small model by luck |
| C. **One named role each, routed deliberately** | each provider used for what it is best at; quota pools stay independent | requires a routing layer (Day 70) and a stated policy to route against |

## Decision

**Option C.** Each provider gets one role, pinned in code, never implicit:

- **Gemini Flash-class — the primary brain.** Native to ADK, largest context, the default for
  anything needing judgement.
- **Groq — the speed lane.** Latency-sensitive, high-volume, small-output work: the classifier.
- **OpenRouter `:free` — the breadth lane.** Second opinions and model families the other two do
  not have. Lowest daily quota, so used sparingly.
- **Ollama — the offline baseline.** The provider-outage branch, and the privacy lane.

Every agent pins its model explicitly (ADK-73). No implicit defaults.

## Consequences

Easier: a 429 on one provider does not stop the desk; the Day 70 Quota-Router has a policy to
route against; each lane's budget is separately countable.

Harder: four providers means four sets of limits to track, and LiteLLM as an adapter for three
of them (Day 9).

Committed to: recording the current free model list and date before pinning anything
(Addendum 02 §3), and handling 429 with `retry-after` on every call path (Principle 10).

## What would make us change our minds

- If Day 9's benchmark shows Groq's latency advantage is under ~200ms on classification-sized
  prompts, the speed lane is not worth the adapter and the classifier moves to Gemini.
- If OpenRouter's free floor drops below ~20 RPD, the breadth lane stops being usable for
  anything but one-off comparisons.
- If any pinned model loses its free tier, the plan is amended first (Principle 14).

## Cold read

*(Re-read this a day later, with your reviewer hat on. Sign here.)*
Reviewed on 2026-08-24 — still stands.

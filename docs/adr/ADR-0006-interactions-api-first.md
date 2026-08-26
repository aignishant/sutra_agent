# ADR-0006 — Teach the Interactions API first; park `generate_content` as the legacy door

- **Date:** 2026-08-24
- **Day:** 2
- **Phase:** 1
- **Status:** accepted
- **Related:** plan §14 Days 2, 3, 8 · Addendum 02 §3 · CHANGELOG_PLAN.md 2026-08-24 · ADR-0005

## Context

Day 2 (AG-02) is the first day Sutra calls a model. It was drafted against
`client.models.generate_content(...)`, which is what the v1.2.1-R legacy day used and what every
tutorial written before mid-2026 uses.

Four facts, all verified live on 2026-08-24, say that surface is no longer the one to learn on:

1. **Google's own quickstart now leads with `client.interactions.create(...)`.** The
   `ai.google.dev/gemini-api/docs/quickstart` page's entire Python sample is an Interactions call
   returning `interaction.output_text`.
2. **The `generate_content` documentation pages have been retitled "Gemini Generate Content API
   (Legacy)."** Not removed, not marked deprecated in the SDK reference — but relabelled. The
   nav moved; the code did not.
3. **The Interactions API runs on the free tier.** Interactions are retained one day on free
   versus fifty-five on paid, which is a retention difference, not an access gate. Addendum 02's
   zero-budget rule is satisfied.
4. **ADK 2.x reaches it with one flag.** `use_interactions_api=True` on the Gemini model config
   switches ADK from `generateContent` to Interactions, so Day 5's first ADK agent is not stranded
   on whichever surface Day 2 taught.

Two further facts about the model roster arrived with the same lookups. `gemini-2.5-flash` — the
model Addendum 02 §3 tabled as a free workhorse on 2026-08-12 — **shuts down 2026-10-16**, and ADK
v2.2.0 has already moved its own default off it. The models page now lists `gemini-3.7-flash` and
`gemini-3.6-flash` above the `gemini-3.5-flash` that CHANGELOG_PLAN.md pinned on 2026-08-13.

The learner's stated goal is to learn the surface that will still be current when this curriculum
ends, not the one the tutorials were written against.

## Options considered

- **Keep `generate_content` as the teaching surface.** Matches the legacy day, ADK's current
  default path, and every tutorial. Rejected: it teaches the relabelled-legacy surface as the
  primary one, and the learner explicitly asked to learn forward.
- **Teach Interactions only, and never mention `generate_content`.** Cleanest document. Rejected:
  the learner will meet `generate_content` in every blog post, Stack Overflow answer and older
  repository they open, and a curriculum that leaves them unable to read it has created a gap it
  refuses to name. Principle 18 wants the professional's whole map, not the tidy half.
- **Split the surfaces across two days.** Rejected: AG-02 is one ID, and §17's one-idea test
  splits *ideas*, not *vendors' API revisions*. The mechanics — tokens, context, sampling — are
  identical on both surfaces.
- **Teach Interactions first, park `generate_content` as awareness (chosen).**

## Decision

**The Interactions API is Sutra's teaching surface from Day 2 onward.**

- Day 2's mechanism sections use `client.interactions.create(...)`, `interaction.output_text` and
  `interaction.usage`.
- **`store=False` with an explicit `input` history is the default shape Sutra writes**, because it
  is the shape that keeps context management visible and therefore keeps Day 3's hand-rolled loop
  honest. Server-side state is taught as a capability, not as the house style.
- **`previous_interaction_id` is taught, then declined**, with the reason recorded: an agent whose
  context it cannot inspect is an agent it cannot debug, budget or evaluate — and Phase 3 is
  entirely about deciding what earns a place in the window.
- **`generate_content` gets one 🅿️ parked part** — awareness-level, interview-ready, deliberately
  not built on. It exists so the learner can read the ecosystem, and it names
  `use_interactions_api=True` as the bridge to Day 5.
- **The model pin moves to `gemini-3.7-flash`**, the model Google's own current quickstart uses,
  subject to the standing rule that only a live call proves access (Day 1,
  [3.1](../../days/day-01-bootstrap-and-map/parts/03-keys-and-env/3.1-the-three-free-doors.md)).

## Consequences

- **Day 2 is written against a surface with less third-party writing about it.** Every field name
  in the day came from a live documentation fetch on 2026-08-24, recorded in the hub's §8. When a
  field is wrong, the fix is a fetch, not a memory.
- **Day 3's hand-rolled loop is unaffected and arguably better motivated.** `store=False` forces
  the history list to be explicit, which is exactly the thing Day 3 loops over.
- **Day 8 (sessions, ADK-06/07) gains a real comparison** it did not have: ADK's session service
  versus the Interactions API's server-side state, two answers to one question.
- **Addendum 02 §3's model table is stale and now known to be stale.** It is not edited — it is a
  dated baseline — but Day 2 records the live roster and the 2026-10-16 shutdown date.
- **A risk we are accepting:** the Interactions API is newer, and newer surfaces move. If it
  changes under us, Principle 14 applies again — amend, then rewrite the affected parts.
- **`store=True` is the API default**, so the incurious call persists conversation server-side.
  Day 2 teaches the flag as a blast-radius decision (Principle 13), not as a performance tweak.

## What would make us change our minds

- **`generate_content` is formally deprecated with a removal date**, which would turn the parked
  part from "the surface you will read about" into "the surface that is going away" — a different
  document.
- **Interactions turns out to be gated or metered differently on the free tier.** The tell would
  be an HTTP 403 or a quota row that does not appear for `generateContent`. Free-tier access is
  the load-bearing assumption; Addendum 02 outranks this ADR if it breaks.
- **ADK 2.x makes `use_interactions_api=True` the default**, which would make the parked part
  purely historical and let it shrink to a paragraph.
- **The free-tier retention window drops below one day**, making `store=True` useless for the
  ambient work in Phase 11 and changing what Day 3.3 should recommend.

## Cold read

*(Re-read this a day later, with your reviewer hat on. Sign here.)*
Reviewed on YYYY-MM-DD — still stands / amended because ______

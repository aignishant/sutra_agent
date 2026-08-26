# ADR-0002 — A Phase 16 deployment-implementation track (Days 97+), separate from the master plan

- **Date:** 2026-08-21
- **Status:** Accepted (user-directed: "create doc day wise from 97 to implement deploy agent
  different different platform, pick up one by one... take tracker of all deployment platform
  implementation in docs only on day wise")

## Context

`docs/deployment/00_stay_free_safety.md` through `07_free_databases_and_extras.md` document
*which* free options exist across GCP, Azure, AWS, Kubernetes, Terraform, and other platforms,
with real commands — but at reference-guide depth, not as a guided, one-platform-at-a-time,
hands-on implementation with verification steps. The user asked for that guided depth, in the
same day-numbered format as `docs/days/day_NNN.md`, continuing from 97.

Two things are true at once, and both need to be said out loud rather than picked silently
(Karpathy guideline: "if you had to guess, the guess is a line I need to see"):

1. **`docs/00_MASTER_PLAN.md` §14 assigns IDs through Day 96 only** (199 IDs, 15 phases). There
   is no Day 97+ in the plan — this is new territory, not a continuation of an existing
   assignment.
2. **`docs/days/PROGRESS.md`'s actual last green row is Day 8**, not Day 96. Days 9–96 exist as
   pre-generated doc files (`GENERATION_TRACKER.md`, batch of 2026-08-18/19/20) but have not
   been run/committed for real yet. Strictly, `CLAUDE.md`'s "next day = last green row + 1"
   rule would make the next *original-curriculum* day **9**, not 97.

Given the user's explicit, repeated instruction to start at 97 — and that 97 is exactly
"one past the plan's last defined day" rather than a number invented at random — the read taken
here is: **this is a deliberate new track, appended after the master plan's planned end, not a
renumbering or a claim that Days 9–96 are finished.** That distinction is recorded here so a
future reader (or a future session resuming this work) doesn't confuse "Day 97 exists" with
"Days 9–96 were run."

## Decision

1. **Add a "Phase 16 — Free Multi-Cloud Deployment Implementation" (Days 97+), explicitly
   outside `docs/00_MASTER_PLAN.md`'s 15 phases and 199 IDs.** `00_MASTER_PLAN.md` itself is
   **not edited** — it stays the authoritative record of the original 96-day contract. This ADR
   is the record of the extension instead.
2. **New day docs live at `docs/days/day_097.md` onward**, same location and filename
   convention as the original 96, for discoverability — confirmed safe: `tools/trace.py`'s
   `plan_map()` only reads `docs/00_MASTER_PLAN.md` §14 (Days 1–96); it iterates
   `for day in sorted(plan)`, so Day 97+ is structurally invisible to it. `make check` /
   `tools/trace.py` cannot be broken by anything this ADR adds, by construction.
3. **A new, separate ledger**: `docs/days/DEPLOY_TRACK_TRACKER.md`. Not `PROGRESS.md` —
   `PROGRESS.md`'s docstring contract is "the last row is where we are" for the *original*
   curriculum, and `CLAUDE.md`'s "generate day N" workflow reads that file's last row to compute
   N. Adding Phase 16 rows there would make a future "generate day N" request for the *original*
   track miscompute N. The two ledgers are kept structurally separate for exactly this reason.
4. **A new, separate ID prefix**: `DEPLOY-NN`, one per platform/day, one-to-one with a day
   number ("pick up one by one"). Deliberately does **not** match `tools/trace.py`'s ID regex
   (`AG|ADK|MCP|SK|OPS|SEC`), so these IDs can never be confused with, or accidentally
   cross-count against, the master plan's 199.
5. **The Day Document Contract (§17) is kept in spirit, adapted where §14 doesn't apply**: same
   required sections (story, mission, concepts, build-with-verify, failure lab, interview
   corner, gates-and-ledger) — but "IDs closed (exactly §14's list)" becomes "the one `DEPLOY-NN`
   this day closes," and the ledger snippet targets `DEPLOY_TRACK_TRACKER.md` instead of
   `PROGRESS.md`/`TRACEABILITY.md`/`PACKAGES.md`.
6. **Addendum 02's zero-budget rules still bind every day in this track without exception.**
   Genuinely Always-Free options (Cloud Run, Cloud Run functions, Compute Engine `e2-micro`,
   Azure Container Apps, App Service F1, Azure Functions Consumption, AWS Lambda, Oracle Cloud
   Always Free) get real, hands-on, run-it-yourself days. Anything that bills for real
   infrastructure regardless of usage (GKE/AKS node pools, AWS EKS's control plane) keeps
   Day 87's "parked — documented, first line says never run" discipline rather than becoming a
   required hands-on step.
7. **Docs only, same as every other day doc.** These days instruct the human to run cloud CLI
   commands on their own machine/account; nothing in this track edits `sutra/`, `tests/`, or
   `tools/`.

## Consequences

- `docs/00_MASTER_PLAN.md` remains untouched and authoritative for Days 1–96 / 199 IDs.
- A future "generate day N" request for the *original* curriculum still computes N from
  `PROGRESS.md`'s real last row (currently 8), completely unaffected by Phase 16's existence.
- Phase 16's own "next day" is computed from `DEPLOY_TRACK_TRACKER.md`'s last row instead —
  that file states this explicitly, the same way `PROGRESS.md` does for the original track.
- If the original 96-day plan ever assigns real IDs to a day numbered 97+ (it structurally
  cannot without editing §14), reconcile via a new ADR first, per Principle 14.
- This ADR itself is the amendment record — no `CHANGELOG_PLAN.md` row is needed for the
  original plan's *content*, since that content is unchanged; a short note is still added there
  pointing at this ADR, so anyone reading the changelog top-to-bottom finds the pointer.

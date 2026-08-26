# ADR-0001 — Reconstruction of the lost master plan

- **Date:** 2026-08-13
- **Status:** Accepted (user-directed: "do whatever best, we are starting to create days from the plan")

## Context

`docs/00_MASTER_PLAN.md` — the contract every other document points to — was missing from the
repository before any day was generated. `CHANGELOG_PLAN.md` records that Addendum 01 was merged
into it on 2026-08-12, so the file existed at some point and was lost (not yet written was ruled
out). Searches of the repo, Desktop/Downloads/Documents, the Windows Recycle Bin, and Google
Drive found no copy. The `00_MASTER_PLAN.md` in `Downloads/` and `Projects/Yantra/docs/` is
Project Yantra's plan (a different curriculum); `Projects/mandala/` likewise has its own.

## Decision

Reconstruct the plan as **v1.2.0-R** from the surviving evidence, rather than stall the project:

- **Fixed anchors preserved exactly** (day numbers, IDs, section numbers referenced by
  surviving docs): §5.1 traps, §14 day map, §17 contract, §18 style guide; AG-31..34,
  ADK-73..78, MCP-26..33 slots from Addendum 01; the ~30 day-number anchors from Addendum 02
  (Day 5/9/16/24/31/43/49/51/64/70/72/73/74–78/79–83/84–88/91…); six curricula; 15 phases;
  96 days; Principle 14; the ledger set.
- **Reconstructed tissue** (marked as such in the plan header): exact wording of day titles,
  the per-day distribution of un-anchored IDs (AG-01..30, ADK-01..72, MCP-01..25, SK, OPS,
  SEC core rows), and the phase boundaries between anchored days.
- Both addendums are folded in (v1.1 = Addendum 01, v1.2 = Addendum 02), so the plan is at
  post-merge state; ID total is 199 (Addendum 01's "~196" was an estimate).

## Consequences

- Day generation can resume (Day 1 next).
- If the original plan resurfaces, diff against v1.2.0-R and reconcile via a new ADR **before**
  generating further days; already-generated days are re-validated against the reconciled map.
- The reconstruction is the authoritative contract until then — per Principle 14, amendments go
  through addendums + `CHANGELOG_PLAN.md`, never silent edits.

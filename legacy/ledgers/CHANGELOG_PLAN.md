# Plan Changelog
- 2026-08-12 — Addendum 01 merged (MCP 2026-07-28 spec; AG-31..34; ADK-73..78).
- 2026-08-12 — Addendum 02: zero-budget model policy (free tiers only; Days 9/16/70/74-78/86-88 amended).
- 2026-08-13 — Plan file lost and reconstructed as v1.2.0-R from CLAUDE.md, Addendums 01–02, ledgers, and sibling-plan structure. Both addendums folded in; ID total fixed at 199. See ADR-0001.
- 2026-08-13 — Model repin: `gemini-2.5-flash` is closed to new accounts (live call returns 404 "no longer available to new users" even though the model still appears in the docs and in `models.list()`). Primary → `gemini-3.5-flash`; lite lane → `gemini-3.5-flash-lite` (the stable Flash pair this project's key can call; `gemini-3.5-flash` verified by live call + usage metadata, still a thinking-by-default model). Plan §14 Day 5 amended (Addendum 02 left as its dated 2026-08-12 baseline — read its `gemini-2.5-flash` mentions as the repinned model); plan v1.2.0-R → v1.2.1-R.
- 2026-08-21 — Phase 16 (Days 97+, free multi-cloud deployment *implementation*, hands-on) added
  as an extension appended after the plan's Day 96 end — not a change to §14's 199 IDs or 15
  phases, which are unchanged and unedited. Own ledger (`DEPLOY_TRACK_TRACKER.md`), own ID prefix
  (`DEPLOY-NN`), own ADR. See ADR-0002.
# Progress Ledger — Project Sutra

Append-only. **The last row is where we actually are.** One row per *completed* day, pasted from that day's
hub §11 before `./m done N` will commit. A day with no row here is not finished,
whatever the folder looks like.

*(Reset at plan v2.0.0. The v1.2.1-R progress ledger — days 1–8 under the old day format — is
frozen at `legacy/ledgers/PROGRESS.md`.)*

| Day | Date | IDs closed | Parts | Commit | Gates green? |
| --- | ---- | ---------- | ----- | ------ | ------------ |
| 0 | 2026-08-24 | — (no IDs; toolchain) | 17 | eb3a5a0 | ✅ |
| 1 | 2026-08-24 | AG-01, OPS-01, OPS-02, OPS-03 | 14 | a33938f | ✅ |
| 2 | 2026-08-26 | AG-02 | 16 (+3 papers) | `<hash>` | ✅ |
| 3 | 2026-08-26 | AG-03 | 14 (+1 paper) | `<hash>` | ✅ |
| 4 | 2026-08-26 | AG-04 | 16 (+1 paper) | `<hash>` | ✅ |
| 5 | 2026-08-26 | ADK-01, ADK-02, ADK-73 | 16 | 57280b6 | ✅ |
| 6 | 2026-08-26 | ADK-03, AG-05 | 19 (+1 paper) | `<hash>` | ✅ |
| 7 | 2026-08-27 | ADK-04, ADK-05 | 16 | 5c85364 | ✅ |
| 8 | 2026-08-27 | ADK-06, ADK-07 | 16 | 5c85364 | ✅ |
| 9 | 2026-08-27 | ADK-08, ADK-09 | 16 (+1 paper) | 5c85364 | ✅ |
| 10 | 2026-08-27 | ADK-10, ADK-11 | 16 | 5c85364 | ✅ |
| 11 | 2026-08-27 | ADK-12, AG-06 | 16 | 5c85364 | ✅ |
| 12 | 2026-08-27 | ADK-13 | 16 (+1 paper) | 5c85364 | ✅ |

> **Deviation from Principle 2, recorded rather than hidden.** Days 7–12 were written and committed
> together in `5c85364` (2026-08-27) instead of one commit per day, and their rows were not appended
> here at the time. The rows above were reconstructed on 2026-08-29 by copying each hub's own §11
> template and filling `<date>`/`<hash>` from `git log --diff-filter=A` on the day folder; the part
> counts were re-counted from the tree and the IDs read from each hub's frontmatter. The gate was
> re-run over all six before the `✅` column was written. The history was **not** rewritten to make
> the commits look compliant — the ledger records what happened.

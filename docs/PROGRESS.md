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
| 13 | 2026-08-29 | ADK-14, ADK-15 | 19 | ab9e5a1 | ✅ |
| 14 | 2026-08-30 | ADK-16 | 19 (+1 paper) | 3dc89ec | ✅ |
| 15 | 2026-08-30 | ADK-17 | 19 (+1 paper) | 4029771 | ✅ |
| 16 | 2026-09-03 | ADK-18, AG-07, AG-32, SEC-01 | 24 (+1 paper) | 210a3b3 | ✅ |
| 17 | 2026-09-03 | ADK-19, ADK-20 | 18 | 124b186 | ✅ |
| 18 | 2026-09-03 | ADK-21 | 15 | f8766e7 | ✅ |
| 19 | 2026-09-03 | AG-08, AG-09 | 16 (+1 paper) | 35cea29 | ✅ |
| 20 | 2026-09-03 | AG-10, ADK-22 | 15 (+1 paper) | e40c6ad | ✅ |
| 21 | 2026-09-03 | ADK-23, SEC-02 | 14 (+1 paper) | 7315bac | ✅ |
| 22 | 2026-09-03 | OPS-04 | 12 (+1 paper) | 3560bf9 | ✅ |

> **Deviation from Principle 2, recorded rather than hidden.** Days 7–12 were written and committed
> together in `5c85364` (2026-08-27) instead of one commit per day, and their rows were not appended
> here at the time. The rows above were reconstructed on 2026-08-29 by copying each hub's own §11
> template and filling `<date>`/`<hash>` from `git log --diff-filter=A` on the day folder; the part
> counts were re-counted from the tree and the IDs read from each hub's frontmatter. The gate was
> re-run over all six before the `✅` column was written. The history was **not** rewritten to make
> the commits look compliant — the ledger records what happened.

> **Day 13, same shape, recorded the same way.** Day 13 was written and committed inside `ab9e5a1`
> (2026-08-29) — a commit that also carried an unfinished Day 14 — and its row was not appended at the
> time. The row above was reconstructed on 2026-08-30 from the hub's own §11 template, with
> `<date>`/`<hash>` filled from `git log --diff-filter=A -- days/day-13-callbacks-four-doors`, the part
> count re-counted from the tree and the IDs read from the hub's frontmatter. `./m depth 13` was
> re-run green before the `✅` was written. **Day 14's row was held back on purpose**: its `parts/`
> and `papers/` landed in `ab9e5a1` without a hub or a checklist, those were written on 2026-08-30, and
> the row was pasted only once the commit that finishes the day existed and its hash could be observed
> rather than guessed (Principle 7). That commit is `3dc89ec`, and the row above carries the hash it
> actually printed.
>
> **What `3dc89ec` does not contain.** `days/*/lab/` is gitignored, so Day 14's lab scripts and the
> paper's two-file demo are not in it. The demo is given complete inside
> `papers/01-aspect-oriented-programming.md`, which is committed; the copy under `lab/` is the
> learner's, like every other day's. The pasted `WEAVE=1` / `WEAVE=0` transcript in that document was
> re-run on 2026-08-30 and matches byte for byte.

> **Day 15, the same shape again, recorded the same way.** Day 15 was committed as `4029771`
> (2026-08-30) with a commit message that did not follow §18.6 and without this row being appended,
> so on 2026-09-03 `./m brief 16` refused to run with `the last PROGRESS row is day 14`. The row above
> was reconstructed from the hub's own §11 template, with `<date>`/`<hash>` read from
> `git log -1 --format='%H %cd' 4029771`, the part count re-counted from the tree (nineteen parts and
> one paper) and the ID read from the hub's frontmatter. `./m depth 15` was green on 2026-09-03 before
> the `✅` was written. The commit was **not** amended; the ledger records what happened.

# ADR-0004 — Day and section folders carry a slug after their number

- **Date:** 2026-08-23
- **Day:** 1 (applied before Day 2 is written)
- **Phase:** 1
- **Status:** accepted
- **Amends:** master plan v2.0.0 → **v2.1.0** (§17.2 only)
- **Related:** ADR-0003 (the depth contract, which created these folders)

## Context

ADR-0003 replaced the one-file day with a folder: a hub, a checklist, and `parts/` holding one
document per subtopic, grouped into numbered section folders. That solved depth. It created a
navigation problem it did not solve.

After two days, the tree reads:

```text
days/
├── day-00/
│   └── parts/{01,02,03,04}/
└── day-01/
    └── parts/{01,02,03,04}/
```

Ten folders, ten numbers, zero information. Extrapolated across 97 days at roughly four sections
each, that is ~500 numbered folders in which nothing is findable by name. The concrete costs:

1. **Nothing is recognisable in a file tree, a tab bar or a fuzzy-finder.** Opening `parts/03/` to
   discover it is about API keys is a lookup that the filename could have answered for free.
2. **`git log --stat` and diffs are unreadable.** `days/day-01/parts/03/3.2-...` names the subtopic
   only at the leaf; every ancestor is noise.
3. **The repo is the memory (Principle 2), and this part of it needs decoding.** Day 3 is forgotten
   by Day 66 — §18 says so explicitly — and a numbered folder gives a returning reader nothing to
   recognise.

The part *files* never had this problem: `1.1-who-decides-the-next-step.md` says what it is. The
folders were the only place a number was used as a name.

## Decision

Every day folder and every section folder carries a short kebab-case slug after its number.

| Folder | Shape | Slug source | Length |
| --- | --- | --- | --- |
| the day | `days/day-NN-<slug>/` | the hub's `title` frontmatter, articles dropped | 1–4 words |
| a section | `parts/NN-<slug>/` | the section heading in the hub's §2 map | 1–3 words |

```text
days/day-01-bootstrap-and-map/
├── LESSON.md
├── CHECKLIST.md
└── parts/
    ├── 01-what-is-an-agent/
    │   └── 1.1-who-decides-the-next-step.md
    ├── 02-repo-as-memory/
    ├── 03-keys-and-env/
    └── 04-ledgers/
```

**The number remains the identity; the slug is a label on it.** Every tool that resolves a day
resolves it by number and accepts whatever slug follows — `scripts/depth_check.py`,
`scripts/trace.py`, `scripts/tracker.py` and `./m` all match `day-NN` plus an optional suffix. This
is the load-bearing half of the decision: it means a slug that turns out to be wrong can be fixed
with a `git mv` and nothing downstream notices, and it means the change was safe to apply to days
already written.

Part filenames do not change. They already carry a full slug, and renaming them would break every
cross-part link for no gain.

## Options considered

| Option | Why not |
| --- | --- |
| **Leave the numbers bare** | The status quo. Costs compound with every day written; renaming 400 folders later is strictly worse than renaming 10 now. |
| **Slug the section folders only** | Cheaper — day folders are referenced by four tools and two generated ledgers. But `days/day-43/` is the folder a reader opens *first*, so the half that mattered most would stay unnamed. |
| **Drop the number, use the slug alone** | `days/bootstrap-and-map/` loses the ordering that the whole curriculum is built on, and `parts/keys-and-env/` loses the `<section>.<subtopic>` correspondence the depth check enforces. |
| **Rename the part files too** | They are already slugged. Pure churn, and it breaks every relative link between parts. |

## Consequences

- A file tree, a `git log --stat` and an editor tab strip now say what a day teaches.
- `docs/CURRICULUM_INDEX.md` and `docs/TRACEABILITY.md` link to real on-disk folder names for
  written days and fall back to the bare `day-NN` form for days not yet written — so a forward link
  to Day 69 still points somewhere sensible before Day 69 exists, and becomes exact when it does.
- The slug is derived, not authoritative. If a hub's `title` changes, the folder should be renamed
  to match; nothing enforces that beyond review, and nothing breaks if it drifts.
- One new failure mode, and `scripts/depth_check.py` catches it: a folder whose number disagrees
  with the part filenames inside it. That check already existed; it now compares against the number
  before the slug.

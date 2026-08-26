# 🗃️ legacy/ — the first run of Sutra, kept for reference

Everything in this folder was written under **master plan v1.2.1-R**, whose day format was one
file per day: `docs/days/day_NNN.md`. Plan **v2.0.0** replaced that format with a hub plus one
document per subtopic (`days/day-NN/LESSON.md` + `days/day-NN/parts/`), and the days are being
regenerated from Day 0 forward.

**Nothing here was deleted.** Every file was moved with `git mv`, so `git log --follow` still
reaches its whole history.

> ⚠️ **Read-only.** Do not edit anything in this folder, and do not link to it from a v2.0.0 day
> document. It exists to be *mined* — correctness harvested, structure discarded — exactly as the
> plan's §17.8 describes.

---

## What is in here

| Folder | What it holds | Status |
| --- | --- | --- |
| `days/` | 107 v1.2.1-R day documents, `day_001.md` … `day_107.md` | 🗃️ mine, then discard the structure |
| `ledgers/` | `PROGRESS.md`, `TRACEABILITY.md`, `PACKAGES.md`, `SKILL_PROVENANCE.md`, `CHANGELOG_PLAN.md`, `GENERATION_TRACKER.md`, `DEPLOY_TRACK_TRACKER.md` as of the v1 run | 🗃️ superseded by the fresh ledgers in `docs/` |
| `deployment/` | The free-tier deployment guide (Docker/k8s, GCP, Azure, AWS, Terraform, other free platforms, free databases) | ✅ **still current** — see below |
| `code/` | The product code written during v1 days 1–8: `agent.py`, `config.py`, `events_lab.py`, `loop.py`, `mechanics.py`, `run_agent.py`, `tools.py`, plus the old `trace.py` | 🗃️ reference only |
| `docs/` | A copy of `00_MASTER_PLAN.md` at v1.2.1-R, frozen at the moment of the v2.0.0 amendment | 🗃️ historical |

## The deployment guide is not dead

`legacy/deployment/` is the one part of this folder that is **still factually current**. It is here
because it belongs to the v1 documentation set, not because it is wrong. It will be mined into the
v2.0.0 days that own its subject:

| Guide file | Regenerates into |
| --- | --- |
| `01_local_docker_and_kubernetes.md` | Day 86 (containerize) · Day 88 (kind/k3d) |
| `02_gcp.md` · `05_terraform.md` | Day 87 (Agent Engine walkthrough, 🅿️ documented not billed) |
| `00_stay_free_safety.md` | Day 86's request budget and §7 Traps |
| `03_azure.md` · `04_aws.md` · `06_other_free_platforms.md` · `07_free_databases_and_extras.md` | Day 91 (integrations survey, 🅿️) |

Until those days are regenerated, read the guide here. `legacy/deployment/00_stay_free_safety.md`
is still the file to read **before** running any cloud command.

## Why the code moved out of `sutra/`

Plan v2.0.0 adopts the rule that **all the code lives in the documents, and none of it is
pre-written in the repo** (`days/README.md`, rule 1). You cannot debug on Day 60 what you never
typed on Day 8. The v1 modules were correct, but they were sitting in `sutra/` as *answers*, which
means a regenerated day would have nothing left to build.

`sutra/.adk/session.db` was not moved. It was a committed SQLite runtime artifact — a session store
that should never have been in git — and it was removed from tracking and added to `.gitignore`
during the v2.0.0 migration.

## Mining a legacy day (the rule from plan §17.8)

When you regenerate day N, its v1 document at `legacy/days/day_NNN.md` is a **correctness source,
not a structure source**:

1. Read it. Every topic it covered must survive into the new `parts/`.
2. Every surviving topic must **gain** what it did not have: the story, the mechanism in full, the
   real failure text, the *In production* section, and the check-yourself.
3. Never copy a section across wholesale. If a part gained no story, no failure text and no
   production face versus the legacy prose, the day is not regenerated — it is reformatted.
4. Legacy prose carries **time estimates** ("estimated hours" in every header). Principle 17 removed
   those. Never carry one across; `./m depth N` fails the day if you do.

## Day-number mapping

v1 wrote 107 day documents against a 96-day plan; days 97–107 were the deployment implementation
track added by `docs/adr/ADR-0002-deployment-implementation-track.md`. v2.0.0 keeps the 96-day map
in §14 of the master plan unchanged and adds **Day 0** (toolchain and skeleton, closes no IDs)
in front of it.

| v1 file | v2.0.0 home |
| --- | --- |
| — | `days/day-00/` — new; closes no IDs |
| `legacy/days/day_001.md` | `days/day-01/` |
| … | … |
| `legacy/days/day_096.md` | `days/day-96/` |
| `legacy/days/day_097.md` … `day_107.md` | folded into Days 86–88 and 91, per ADR-0002's successor |

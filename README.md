# 🧵 Sutra

**Sutra** (Sanskrit सूत्र) means *thread* — the thread that strings concepts together, and the
thread of execution that runs through a multi-agent system.

Sutra is two things at once:

1. **A product** — an autonomous support-ticket triage desk. Tickets arrive; a graph of agents
   classifies, researches, drafts and reviews a response; anything that writes to the outside world
   waits for a human. It remembers what it has seen, every data source it touches is an MCP server,
   it is traced end to end, and it runs on **$0** of model spend.
2. **A 97-day curriculum that builds it**, one day at a time — Google **ADK 2.x**, **MCP**,
   **Agent Skills** and **A2A**, from "what is an agent" to a system you can defend in an interview.

Nothing here is a toy demo. Every concept lands as a change to the same system, and if removing a
concept would not break Sutra, it does not get a day.

---

## Start here

```bash
./m status          # where am I
./m start 0         # open Day 0's hub and list its parts
```

**Never done this before?** →
[`days/day-00-toolchain-skeleton-driver/LESSON.md`](days/day-00-toolchain-skeleton-driver/LESSON.md).
It assumes you have
nothing installed and no prior knowledge, and it ends with a repo that cannot leak a key.

| You want | Read |
| --- | --- |
| The contract — what this is and how it is built | [`docs/00_MASTER_PLAN.md`](docs/00_MASTER_PLAN.md) |
| How a day is written, and why | plan **§17**, the depth contract |
| How to read a day | [`days/README.md`](days/README.md) |
| Where I am | [`docs/PROGRESS.md`](docs/PROGRESS.md) · [`docs/TRACKER.md`](docs/TRACKER.md) |
| Where a concept is taught (`MCP-14` → which day?) | [`docs/CURRICULUM_INDEX.md`](docs/CURRICULUM_INDEX.md) |
| Why the money rules are the way they are | [`docs/02_ADDENDUM_ZERO_BUDGET_MODELS.md`](docs/02_ADDENDUM_ZERO_BUDGET_MODELS.md) |
| The first run of this project (v1.2.1-R) | [`legacy/README.md`](legacy/README.md) |

---

## Three commitments

**One project, not toy demos.** Every gear is load-bearing.

**The repo is the memory, not the chat.** Ledgers plus day documents mean any capable CLI agent —
or you, six months from now — can pick up exactly where the last session stopped, from the last row
of `docs/PROGRESS.md` alone.

**Zero budget, by construction.** Free tiers only: Gemini Flash-class, Groq, OpenRouter models
ending in `:free`, local Ollama. No card on file, ever. On $0 the currency is **rate limits**, not
dollars — so quota-aware routing, honest backoff and caching are the curriculum rather than
obstacles to it.

---

## How the days are written

A day is **not** one long page. It is a hub plus one document per subtopic:

```
days/day-NN-<slug>/                 # e.g. day-01-bootstrap-and-map
├── LESSON.md      # the hub — story, part map, setup, build brief, eval, budget, ledger
├── CHECKLIST.md   # the definition of done; ./m done NN refuses to commit until ticked
├── parts/01-<slug>/1.1-<slug>.md …   # THE TEACHING — one idea per document
└── lab/           # your scratch code
```

Every part runs the same ten sections, in the same order: **one-line answer · the story · the idea
in plain language · why Sutra needs it · the mechanism · line by line · when it breaks · in
production · check yourself.** Three rules make that mean something:

- **No clocks.** No time estimate lives anywhere in a day folder. A day is a unit of subject, not of
  time — one sitting or five, both are the day done properly. Nothing is ever trimmed to fit a
  schedule; if a day runs long it gets another part.
- **Zero prior knowledge in, production knowledge out.** Every document opens where someone who has
  never heard of the idea can stand, and closes with what a professional writes instead, what breaks
  at scale, the review comment, and the interview question.
- **You type every line.** No product code is pre-written in this repo. You cannot debug on Day 60
  what you never typed on Day 8.

`./m depth N` enforces the mechanical half — missing sections, numbering gaps, code blocks nobody
explained, a smuggled-in clock. The rest is enforced by reading.

---

## The driver

`make` is not used. `./m` is:

```bash
./m status         # one line: how many days are written / complete
./m start N        # point at day N's hub and list its parts
./m parts N        # just the sub-topic list
./m scaffold N     # create days/day-NN-<slug>/lab/
./m depth [N]      # check day N against plan §17, the depth contract
./m trace          # regenerate docs/TRACEABILITY.md and the curriculum index
./m tracker        # regenerate docs/TRACKER.md
./m check          # ruff + format + offline pytest + depth + traceability
./m done N         # refuses unless the checklist is ticked and checks are green, then commits
```

Written for **Git Bash** on Windows; macOS and Linux work unchanged. PowerShell equivalents are
tabled in [`days/README.md`](days/README.md).

---

## Setup

You do not need this section if you are starting at Day 0 — Day 0 *is* the setup, explained rather
than listed. For a machine that already has the toolchain:

```bash
uv sync                                   # materialise the environment from uv.lock
cp .env.example .env                      # then fill in your own free-tier keys
./m check                                 # should print: OK all green
```

`.env` is gitignored and is read only by Sutra's own process. It never modifies your shell profile
or any other project. `GOOGLE_GENAI_USE_VERTEXAI=FALSE` is what keeps Sutra on the free Gemini API
rather than paid Vertex AI.

---

## Status

Sutra is being rebuilt under **master plan v2.2.1**, which replaced the one-file-per-day format with
the hub-plus-parts architecture described above and added a `papers/` directory to the days whose
ideas came from published work. Days are regenerated from Day 0 forward; run
`./m status` for the live count. The first run's 107 day documents are preserved read-only in
[`legacy/`](legacy/) and are mined — not copied — as each day is rewritten.

## Licence

See `LICENSE` if present; otherwise all rights reserved by the repository owner. The company data
Sutra processes is **synthetic, always** — no real personal or employer data is ever sent through a
free-tier endpoint.

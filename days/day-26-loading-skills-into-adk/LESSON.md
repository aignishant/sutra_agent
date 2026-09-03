---
day: 26
phase: 4
phase_name: "Agent Skills"
title: "`SkillToolset` — loading skills into ADK"
ids: ["SK-04", "SK-05", "ADK-24"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 17
generated: "2026-09-04"
status: written
lab_scaffolded: false
commit: ""
---

# Day 26 — `SkillToolset`: loading skills into ADK

> **Yesterday (Day 25):** a skill is a folder, two required fields, and a body that is loaded whole.
> You measured what one costs — 64 tokens available, 292 activated — and built one that is perfectly
> valid and will never be used.
> **Today:** that folder reaches an agent. One call turns it into an object, one toolset gives the
> agent four tools for reaching it, and every number you were given yesterday is re-measured against
> the client that actually sends them.
> **Tomorrow (Day 27):** authoring Sutra's own skills, now that you know exactly what the runtime does
> with one.

---

## §1 Where we are

The binder is written and nobody has handed it to anybody.

Yesterday ended with `skills/ticket-triage/` — a card, a procedure, a severity table behind a link and
a script that reads it. Every line of it validated. And Sutra's desk agent has never heard of it,
because the only thing the desk agent has ever been given is a short instruction and a few tools.

Today is the handover, and it is one line: `tools=[SkillToolset(skills=...)]`. What makes the day
worth seventeen documents is that the one line does five things, and four of them are not obvious.

**A skill is loaded eagerly and disclosed lazily.** `load_skill_from_dir` reads the whole folder into
memory — the body, every reference, the full source of every script — before anybody has decided the
skill is relevant. Progressive disclosure is about the context window, not about the filesystem.

**Attaching the toolset writes 479 tokens into your system instruction**, measured, that you did not
write and cannot see in your source. It is the same size whether you have one skill or two hundred.

**The list of your skills is not in that preamble.** Measured: the word `ticket-triage` does not appear
anywhere in it. In ADK 2.7.1 the model has to call a tool named `list_skills` to find out what exists —
which makes the per-skill cost conditional, and puts a model decision upstream of everything Day 25
measured about descriptions.

**And the tools a skill needs appear only after it is activated.** Pass two functions as
`additional_tools` and ask the toolset what it has: four tools. Activate the skill that declares them
in its metadata, ask again: six. Capability, disclosed progressively, the same way knowledge is.

The documentation page for this feature says three tools, says the index arrives in the system
instruction, and does not mention the metadata key. It is marked **Experimental**, and it is wrong in
four places. Every number in this day was read off the installed package on 2026-09-04.

---

## §2 The map

Seventeen parts in five sections, and **no paper** — see §8. The day climbs
`foundation → working → production`: section 1 is turning a folder into an object, section 2 is the
four tools and what each rung costs, section 3 is the wiring, section 4 is the failure lab, and
section 5 is the arithmetic and the discipline.

### Section 1 — `01-loading-a-folder`: from a directory to an object (SK-04)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [`load_skill_from_dir`: one call, and the whole folder is in memory](parts/01-loading-a-folder/1.1-load-skill-from-dir.md) | Eager on disk, lazy in context | `foundation` |
| 1.2 | [The `Skill` object: three fields, and what each one is for](parts/01-loading-a-folder/1.2-the-skill-object.md) | Frontmatter, instructions, resources | `foundation` |
| 1.3 | [Building a skill in code, and when that is the right call](parts/01-loading-a-folder/1.3-building-a-skill-in-code.md) | Tests and generators, nothing else | `working` |
| 1.4 | [The whole shelf in one call, all or nothing](parts/01-loading-a-folder/1.4-the-whole-shelf.md) | One bad folder, no skills | `working` |

### Section 2 — `02-the-four-tools`: the ladder, rung by rung (SK-05)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The 479-token preamble you did not write](parts/02-the-four-tools/2.1-the-preamble-you-did-not-write.md) | A fixed cost with no source line | `working` |
| 2.2 | [`list_skills`: the index is a tool call, not a prompt](parts/02-the-four-tools/2.2-the-index-is-a-tool-call.md) | Four tools, and `False` | `working` |
| 2.3 | [`load_skill`: what activation actually costs](parts/02-the-four-tools/2.3-what-activation-actually-costs.md) | 334, of which 118 is not the body | `working` |
| 2.4 | [`load_skill_resource`: the third rung, and the fence around it](parts/02-the-four-tools/2.4-the-third-rung-and-its-fence.md) | Three prefixes, and a miss counter | `working` |
| 2.5 | [`run_skill_script`: the rung that ships switched off](parts/02-the-four-tools/2.5-the-rung-that-ships-switched-off.md) | `NO_CODE_EXECUTOR`, and what lifts it | `production` |

### Section 3 — `03-wiring-the-toolset`: one line, five effects (ADK-24)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A toolset, not a tool: wiring `SkillToolset` into an agent](parts/03-wiring-the-toolset/3.1-a-toolset-not-a-tool.md) | One entry, four tools | `working` |
| 3.2 | [`additional_tools`: capability that appears only after activation](parts/03-wiring-the-toolset/3.2-tools-that-appear-after-activation.md) | Four, then six | `production` |
| 3.3 | [Activation is a line in session state](parts/03-wiring-the-toolset/3.3-activation-is-a-line-in-state.md) | The register, and two counters | `working` |

### Section 4 — `04-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [💥 One bad folder, and the shelf came back empty](parts/04-failure-lab/4.1-one-bad-folder.md) | A traceback with no path in it | `production` |
| 4.2 | [💥 The tool that was passed in and never appeared](parts/04-failure-lab/4.2-the-tool-that-never-appeared.md) | Three causes, one output | `production` |
| 4.3 | [💥 The manual nobody opened](parts/04-failure-lab/4.3-the-manual-nobody-opened.md) | The failure with no signal at all | `production` |

### Section 5 — `05-in-production`: the arithmetic and the discipline

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [What a skill really costs, in this client](parts/05-in-production/5.1-what-a-skill-really-costs-here.md) | 479 + 83 + 334, and two round trips | `production` |
| 5.2 | [Experimental means experimental: when the page and the package disagree](parts/05-in-production/5.2-experimental-means-experimental.md) | Four disagreements, and the habit | `production` |

**No paper today.** Today's ideas come from a framework implementation and from the Agent Skills
specification, which Day 25 already cited by URL and fetch date. The one research paper this day leans
on — *MemGPT: Towards LLMs as Operating Systems*, `arXiv:2310.08560` — was taught on Day 20 and is
cited and linked from [2.2](parts/02-the-four-tools/2.2-the-index-is-a-tool-call.md) and
[5.1](parts/05-in-production/5.1-what-a-skill-really-costs-here.md). A paper is taught once in this
curriculum; today it is an address, not a lesson.

---

## §3 Setup — run this

**No package is added today.** Skills support ships inside `google-adk`, pinned at **2.7.1** on Day 5
and re-verified importable on 2026-09-04. `git diff pyproject.toml uv.lock` must be empty when you
finish.

```bash
# 1 - the day folder's lab, and a shelf of its own so a broken specimen cannot break the real one
cd days/day-26-loading-skills-into-adk
mkdir -p lab/skills

# 2 - two skills from yesterday: the good one and the useless one
cp -r ../day-25-skills-the-open-spec/lab/skills/ticket-triage lab/skills/
cp -r ../day-25-skills-the-open-spec/lab/skills/vague-description lab/skills/

# 3 - the double, extended from Day 23's
touch lab/fake_skill_context.py

# 4 - section 1: loading
touch lab/load_one.py lab/inspect_skill.py lab/skill_in_code.py lab/load_shelf.py

# 5 - section 2: one script per rung
touch lab/read_preamble.py lab/rung_one.py lab/rung_two.py lab/rung_three.py lab/rung_four.py

# 6 - section 3: the agent, and the two probes
touch lab/desk_with_skills.py lab/tools_after_activation.py lab/the_register.py

# 7 - section 4: the failure lab
touch lab/load_shelf_safely.py lab/the_missing_tool.py lab/did_it_open.py lab/ask_the_desk.py

# 8 - section 5: the arithmetic
touch lab/price_the_ladder.py
cd -

# 9 - confirm the API is there before writing anything against it
uv run python -c "from google.adk.skills import load_skill_from_dir; from google.adk.tools import skill_toolset; import google.adk; print('skills api ok on', google.adk.__version__)"
```

**Step 9 is the gate.** It printed `skills api ok on 2.7.1` on 2026-09-04. If it fails on your machine,
**stop** — check `uv pip show google-adk` against the release notes and amend before continuing
(Principle 14). Do not go hunting for an alternative import path.

**One edit to a copied skill.** [3.2](parts/03-wiring-the-toolset/3.2-tools-that-appear-after-activation.md)
adds one line to `lab/skills/ticket-triage/SKILL.md`, inside `metadata`:

```yaml
  adk_additional_tools: ["lookup_ticket", "remember_triage"]
```

Make that edit in the **lab copy**, not in `days/day-25-.../lab/skills/`. Two of this day's
measurements were taken before it and one after, and the parts say which.

**`ask_the_desk.py` is the only thing all day that spends quota.** Everything else — every measurement,
every failure, every rung — runs with `count_tokens` or with no provider at all. Write and run the
zero-cost scripts first; the live run is §5.

---

## §4 Build brief

**`sutra/desk/skills.py`** — the desk agent's shelf, as project code rather than lab code:

| What | Why | Taught in |
| --- | --- | --- |
| `SHELF = Path(__file__).resolve().parents[2] / "skills"` | anchored to the module, not the process | 1.1 |
| `load_shelf(shelf) -> (skills, rejected)` | one skill at a time, folder named on failure | 4.1 |
| `build_desk_with_skills()` | `SkillToolset` + `Agent`, built once | 3.1 |
| `skills_used(state, agent_name)` | the register, read | 3.3, 4.3 |
| `missing_tools(skill, provided)` | the name lint | 4.2 |

Three of those five exist because of a failure in section 4, which is the point of putting the failure
lab before the production section.

**`tests/`** — three tests, none of them live:

- the surface test from [5.2](parts/05-in-production/5.2-experimental-means-experimental.md): the four
  tool names, asserted as an equality;
- `skills_used({}, "desk") == []` **and** the positive case, from
  [4.3](parts/04-failure-lab/4.3-the-manual-nobody-opened.md) — a detector that only proves the happy
  case is a detector that will lie after an upgrade;
- `missing_tools` against a skill with a deliberately misspelled name, from
  [4.2](parts/04-failure-lab/4.2-the-tool-that-never-appeared.md).

**`skills/ticket-triage/`** — yesterday's build brief asked you to create this at the repository root.
If you have, add the `adk_additional_tools` line here too. If you have not, do it now: today's project
code reads that folder, and the lab copy is for experiments.

**`TODO(me)` markers left for you:**

- **1.4, 4.1** — decide Sutra's policy for an unloadable skill: refuse to start, or skip and log. Write
  the sentence and the reason next to the code. The parts argue for fail-fast; the decision is yours.
- **2.1** — read all seven rules of the preamble, then read Sutra's own desk instruction beside it and
  delete anything that argues with it.
- **2.5** — write the rule that sits beside SEC-01 for skill scripts, in one sentence, and decide
  whether to remove `run_skill_script` with `tool_filter` rather than relying on its refusal.
- **3.2** — decide whether `lookup_ticket` and `remember_triage` are desk tools or triage tools. If
  triage tools, they go in `additional_tools` and the skill declares them; if desk tools, they go on
  the agent. Write down which and why.
- **4.2** — extend `missing_tools` into a check that also reads the **body** for backticked tool names
  and compares them to the declared list. Decide what to do about the false positives.
- **4.3** — add `skills_used` to Day 22's log line, then define the denominator: what counts as a
  conversation that *should* have used a skill?
- **5.1** — price a five-turn triage conversation in tokens and in generations, twice: once with the
  severity table behind a link, once with it in the body. Say which you would ship on twenty requests
  a day.
- **5.2** — find one constructor argument this day did not cover and write one sentence on what it
  does.

---

## §5 The eval that must be able to fail

Two checks. The first spends nothing and can go red today.

```bash
uv run python days/day-26-loading-skills-into-adk/lab/the_missing_tool.py
uv run python days/day-26-loading-skills-into-adk/lab/load_shelf_safely.py
```

Expected, measured on 2026-09-04: `the_missing_tool.py` prints six tool names for the healthy case,
**four** for the two silent failures, **five** for the partial one, and a lint row naming
`lookup_tickets`. Then, with `bad-name` copied onto the shelf, `load_shelf_safely.py` prints
`loaded: ['ticket-triage', 'vague-description']` and `rejected: ['bad-name']`.

Break it four ways and watch each one:

| Break this | What happens | What it is telling you |
| --- | --- | --- |
| remove `adk_additional_tools` from the lab skill | six becomes four | the declaration is in the skill (3.2) |
| misspell one tool name in it | six becomes five | a partial failure is the dangerous one (4.2) |
| copy `bad-name` onto the shelf and run `desk_with_skills.py` | a traceback with no path in it | all-or-nothing loading (4.1, 1.4) |
| change `except (ValueError, OSError)` to `except Exception: pass` | `rejected: []`, and a skill missing | Principle 10, in one line (4.1) |

The second check is the live one, and it is the only thing today that spends generations:

```bash
uv run python days/day-26-loading-skills-into-adk/lab/ask_the_desk.py "Triage ticket 4521."
```

What you are looking for, in order: a `list_skills` call, a `load_skill` call, then the answer — and
`skills_used(...)` non-empty at the end. **Two to four generations of the twenty.** Run it once.

**No transcript of that run is pasted anywhere in this day.** On 2026-09-04 the day's quota was
already spent and the run returned the `429` reproduced in
[3.1](parts/03-wiring-the-toolset/3.1-a-toolset-not-a-tool.md). Principle 10 outranks the shape of a
document: an invented transcript would be undetectable, so the command is here and the output is
yours to produce. Paste it into your notes with the date.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every script in sections 1, 2, 3 and 4 except one | **0** |
| `count_tokens` in `read_preamble.py`, `rung_two.py`, `price_the_ladder.py` | **0** (separate endpoint) |
| `ask_the_desk.py`, one question, one session | **2–4** |
| **Total required** | **2–4 of 20** |

Seventeen parts and almost no quota, because every mechanism in this day is deterministic: the tools
are driven directly with the double from
[2.2](parts/02-the-four-tools/2.2-the-index-is-a-tool-call.md), which is Day 23's technique paying for
itself two days later.

The one live run is not optional. It is the only thing that exercises the three model decisions in
[4.3](parts/04-failure-lab/4.3-the-manual-nobody-opened.md), and those decisions are the day's real
risk.

**Cost: $0.**

---

## §7 Traps

- **The page says three tools. There are four.** `list_skills` is first and is the one the whole cost
  model turns on (2.2, 5.2).
- **The skills index is not in the system instruction.** The preamble contains no skill name; the
  branch that would add one never runs while a `list_skills` tool exists, which is always (2.1, 2.2).
- **`load_skill` takes `skill_name`, not `name`.** Read off the tool's own schema (2.3).
- **Activation sends the whole frontmatter too.** 334 tokens where the body is 184, including the
  description the model already saw and a `license` field it cannot use (2.3).
- **`additional_tools` alone does nothing.** The skill must also declare the names under
  `metadata.adk_additional_tools`, and the match is by tool name with no validation (3.2, 4.2).
- **`allowed_tools` is parsed and never read.** Nothing in `google/adk/` enforces it. It is not a
  containment control (1.2).
- **`load_skills_from_dir` is all or nothing**, and its exception does not name the folder. A folder
  with no `SKILL.md` is silently skipped — the opposite behaviour, in the same call (1.4, 4.1).
- **`load_skill_from_dir` calls `.resolve()`**, so relative paths follow the process's working
  directory and break in a container (1.1).
- **An unknown top-level frontmatter key loads silently** into pydantic's `model_extra` and does
  nothing. The spec validator refuses it; ADK does not (1.2).
- **The `name` must match the folder**, enforced by the runtime and not only by the linter (1.1).
- **`run_skill_script` returns `NO_CODE_EXECUTOR`** until you attach an executor or an environment —
  and the easy executor is the one that runs code in your process (2.5, and Day 16's SEC-01).
- **`load_skill_resource` refuses any path** not starting `references/`, `assets/` or `scripts/`, and
  escalates on the **second** failed lookup in one invocation (2.4).
- **Three framework keys appear in your session state**, one session-scoped and two `temp:`. A strict
  state schema will reject them (3.3).
- **The tool menu changes mid-conversation.** A test asserting a tool count is asserting the cold
  count only (3.2).
- **The docstring and the validator disagree about `snake_case`** inside one file of the package (1.3,
  5.2).

---

## §8 Verify before you code

Fetched or run on **2026-09-04**, the day this was written:

- `https://adk.dev/skills/` — read in full. Source of the import paths
  (`from google.adk.skills import load_skill_from_dir`, `from google.adk.tools import skill_toolset`),
  the **Experimental** marking, and the version note reading *"Python v1.25.0"*. It is also the source
  of the four disagreements catalogued in
  [5.2](parts/05-in-production/5.2-experimental-means-experimental.md); where it and the package
  differ, this day follows the package and says so.
- **The installed `google-adk` 2.7.1**, read and driven directly — the authority for everything
  measured here. Specifically: `google/adk/skills/__init__.py` (the exported names),
  `google/adk/skills/_utils.py` (the loader, the closed frontmatter key list, the
  name-matches-directory rule), `google/adk/skills/models.py` (the six frontmatter fields, the
  `adk_additional_tools` and `adk_inject_state` docstring, the name and description validators), and
  `google/adk/tools/skill_toolset.py` (the four tool classes, `process_llm_request`, the
  `additional_tools` resolution, the miss counters, the executor gate).
- `google.adk.__version__` → `2.7.1`, and `inspect.signature(SkillToolset.__init__)` → the nine
  arguments listed in 5.2 (Principle 7: the version that is importable, not the version that is
  pinned).
- Every `run_async` output in sections 2, 3 and 4 was produced by driving the tools with the double
  from [2.2](parts/02-the-four-tools/2.2-the-index-is-a-tool-call.md) — real calls, real returns, no
  model.
- `count_tokens` against `gemini-3.7-flash` for every number in
  [5.1](parts/05-in-production/5.1-what-a-skill-really-costs-here.md): 479, 12, 83, 35, 334, 353, 98,
  62. Zero generations, on the separate endpoint Day 24 verified.
- The `429` body in [3.1](parts/03-wiring-the-toolset/3.1-a-toolset-not-a-tool.md) is from a real
  refusal on 2026-09-04, not from a page.
- `https://arxiv.org/abs/2310.08560` — cited, not re-taught. The record and the dated row are in
  `docs/PAPERS.md` from Day 20.

**No new package was installed and no model string changed.** The two ledger files that could have
gained a row did not, and §11 says so explicitly rather than leaving it to be inferred.

---

## §9 Say it in an interview

"We had skills as folders in the repository and no way for the agent to use them. In ADK that is one
class — `SkillToolset` — and it goes into the agent's `tools=` list as a single entry.

The thing I would want to be precise about is what that one entry actually does, because it is more
than packaging. It contributes four tools, not three: `list_skills`, `load_skill`,
`load_skill_resource` and `run_skill_script`. And it appends about 480 tokens of instructions to your
system prompt — measured, 479 on our model — telling the model that skills exist and how to use them.
That is a fixed cost, paid on every request, independent of how many skills you have.

What surprised me is that the list of skills is **not** in that preamble. I checked: the skill's name
does not appear anywhere in it. The model has to call `list_skills` to find out what exists. So the
per-skill cost is conditional — a conversation that never asks never pays — but there is a model
decision upstream of every description you write, and no description can influence it. When a skill
does not fire, the first thing I check is whether the model ever listed them at all, and the cheapest
way to check is a state key: ADK records activations under `_adk_activated_skill_<agent_name>`, so
'was the procedure used?' is a state read rather than a text search.

The other mechanism worth knowing is `additional_tools`. Passing tools there does not give them to the
agent. They appear only after a skill is activated, and only if that skill's frontmatter names them
under `adk_additional_tools`. So the tool menu grows mid-conversation — progressive disclosure applied
to capability rather than knowledge. It is genuinely elegant, and the catch is that the binding is a
string match between a Markdown file and a Python function name, with no validation, so a rename
silently removes a tool from a procedure. That needs a lint.

And I would say that the feature is marked Experimental and the documentation page is behind the code
in four places, including the number of tools. So we pin the exact version, we verify against the
installed package rather than the page, and we keep one small test asserting the tool names — so the
next upgrade gives us a specific failure instead of a mystery."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 26` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it to
someone else without the page open.

**Phase 4's gate** is skills authored, loaded and audited, with `./m check` green including the skills
lint and the `:free` lint. Today closes the loading half. Authoring is Day 27, design is Day 28, the
audit is Day 29, and the lint is Day 31 — and this day has left it two specific checks to implement:
the reference-link check from
[2.4](parts/02-the-four-tools/2.4-the-third-rung-and-its-fence.md) and the tool-name check from
[4.2](parts/04-failure-lab/4.2-the-tool-that-never-appeared.md).

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 26 | <date> | SK-04, SK-05, ADK-24 | 17 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** `google-adk==2.7.1` was pinned on 2026-08-26 and skills
support ships inside it; `google.adk.__version__` was re-read on 2026-09-04 and has not moved. The
model pin is unchanged. If your import probe in §3 forced an upgrade, **that** is a row: record the
version, the date and why.

**`docs/PAPERS.md`** — no new rows. Today teaches no paper. `arXiv:2310.08560` is cited from two parts
and already has its dated row from Day 20.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was sourced today; the two on the shelf are
yesterday's, one of them a specimen.

**The commit:**

```text
day 26: SkillToolset - loading skills into ADK - closes SK-04, SK-05, ADK-24
```

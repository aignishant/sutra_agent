---
day: 25
phase: 4
phase_name: "Agent Skills"
title: "Skills: the open spec — `SKILL.md` anatomy"
ids: ["SK-01", "SK-02", "SK-03"]
principles: [1, 2, 4, 7, 8, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 14
generated: "2026-09-04"
status: written
lab_scaffolded: false
commit: ""
---

# Day 25 — Skills: the open spec and `SKILL.md` anatomy

> **Yesterday (Day 24):** Phase 3 closed with a budget denominated in requests — twenty a day, two
> ceilings, a ledger that refuses before it spends. The last measurement of that day was that an
> eight-turn conversation costs eight of the twenty, and the one before it was that everything in the
> system instruction is paid for on **every** request.
> **Today:** Phase 4 opens with the format that fixes the second of those. A skill is a folder; its
> card is loaded always and its body only when it is needed; and you will write one that is perfectly
> valid and will never be used.
> **Tomorrow (Day 26):** `SkillToolset` — loading these folders into ADK, which is where the format
> meets one particular client.

---

## §1 Where we are

There is a laminated card taped inside the lid of the office photocopier and it is the most-used
document in the building.

*Lift the green lever. Pull the sheet towards you, not up. If it tears, open the back panel and check
tray 2.* Four lines, written by somebody who had cleared a lot of jams, taped where the problem
happens. Nobody was trained. Nobody read a manual. The knowledge is at the machine, in the order you
need it, and it is a piece of paper.

Now count what is on the machine's screen instead: about forty settings, every one of them a
capability, none of them telling you what to do when the paper jams.

That is where Sutra is this morning. Sixteen days of capabilities — tools, callbacks, plugins, state,
artifacts, error policy, logging, a budget — and the knowledge of **how the desk actually does a job**
is in exactly one place: the system instruction, where it is paid for on every request whether or not
anybody is doing that job.

Four things worth knowing before you start.

**A skill is a folder, and almost nothing is required.** One file called `SKILL.md`, two frontmatter
fields — `name` and `description` — and Markdown. No code, no manifest, no registration. Verified
against `agentskills.io/specification`, fetched today.

**The description is the whole selection interface.** The model chooses from `name` and `description`
alone; the body is not loaded yet. Measured against five realistic requests, a description written with
both halves — what it does **and** when to use it — overlapped on **7** words where *"Helps with
tickets."* overlapped on **1**, and deleting just the "when" sentence took 7 down to **3**.

**Progressive disclosure is arithmetic, not a slogan.** `ticket-triage` costs **64 tokens** available
and **292** activated — 4.6× the knowledge for the cost — and three skills together cost **115** tokens
of permanent context, which projects to about **7,600 for two hundred**.

**And the loud failures are the cheap ones.** One badly-typed name produced three named validation
errors and a non-zero exit in ten seconds. One badly-written description produced `Valid skill` and a
folder that will never be used.

---

## §2 The map

Fourteen parts in five sections, and **no paper** — see §8 for why, and for the pages that were
actually fetched. The day climbs `foundation → working → production`: section 1 is what a skill is,
section 2 is the frontmatter field by field, section 3 is the body and the folders, section 4 is the
failure lab and section 5 is what happens with many skills.

### Section 1 — `01-what-a-skill-is`: the format and why it exists (SK-01)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A skill is a folder, not a program](parts/01-what-a-skill-is/1.1-a-skill-is-a-folder.md) | One file, two fields, no code | `foundation` |
| 1.2 | [A folder against a tool](parts/01-what-a-skill-is/1.2-a-folder-against-a-tool.md) | A verb against a procedure | `working` |
| 1.3 | [An open spec, and what "open" buys](parts/01-what-a-skill-is/1.3-an-open-spec.md) | Portable, inspectable, auditable | `working` |

### Section 2 — `02-the-frontmatter`: field by field (SK-02)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Two required fields and nothing else](parts/02-the-frontmatter/2.1-two-required-fields.md) | 20 tokens against 64 | `foundation` |
| 2.2 | [`name`: five rules and a directory](parts/02-the-frontmatter/2.2-the-name-field.md) | The one rule that leaves the file | `working` |
| 2.3 | [`description`: the field the agent actually reads](parts/02-the-frontmatter/2.3-the-description-field.md) | 7 against 1, and half of it is one sentence | `working` |
| 2.4 | [The four optional fields](parts/02-the-frontmatter/2.4-the-optional-fields.md) | Where the missing `version` goes | `working` |

### Section 3 — `03-the-body-and-the-folders`: what gets loaded, and when (SK-03)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The body is loaded whole](parts/03-the-body-and-the-folders/3.1-the-body-is-loaded-whole.md) | All 292 tokens, every activation | `working` |
| 3.2 | [`scripts/`, `references/`, `assets/`](parts/03-the-body-and-the-folders/3.2-scripts-references-assets.md) | Run it, read it, use it | `working` |
| 3.3 | [Progressive disclosure: three levels, three budgets](parts/03-the-body-and-the-folders/3.3-progressive-disclosure.md) | ~100 / <5000 / as needed | `working` |

### Section 4 — `04-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [💥 The skill that never triggered](parts/04-failure-lab/4.1-the-skill-that-never-triggered.md) | `Valid skill`, and four zeros | `production` |
| 4.2 | [💥 The name that did not match](parts/04-failure-lab/4.2-the-name-that-did-not-match.md) | Three findings, exit 1, ten seconds | `production` |

### Section 5 — `05-in-production`: many skills

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Validating before you ship](parts/05-in-production/5.1-validating-before-you-ship.md) | Exit 0 and 1, and a command the docs got wrong | `production` |
| 5.2 | [What a skill costs at startup](parts/05-in-production/5.2-what-a-skill-costs.md) | 7,600 tokens for two hundred skills | `production` |

**No paper today.** The origin document for this day is the Agent Skills specification itself, which is
a live web page rather than a numbered revision with a DOI or an arXiv id — so it is cited the way §18
allows, by URL and by the date it was fetched, and §8 lists every page read. Inventing an identifier to
make a paper part possible would be exactly the failure §17.4.1 rule 5 exists to prevent.

---

## §3 Setup — run this

**No package is added to the project today**, and that is a deliberate decision rather than an
oversight. `skills-ref` is run in a throwaway environment with `uv run --no-project --with`, so
`pyproject.toml` and `uv.lock` are untouched. Sutra adopts it as a dev dependency on **Day 31**, when
the skills lint goes into `./m check` and there is something permanent to depend on. §11 carries the
row that will be needed then.

```bash
# 1 - the day folder's lab and three skills, one of them deliberately broken
cd days/day-25-skills-the-open-spec
mkdir -p lab/skills/ticket-triage/references lab/skills/ticket-triage/scripts
mkdir -p lab/skills/bad-name lab/skills/vague-description
cd lab

# 2 - the good skill: a card, a body, a reference table and one script
touch skills/ticket-triage/SKILL.md
touch skills/ticket-triage/references/SEVERITY.md
touch skills/ticket-triage/scripts/severity_table.py

# 3 - the two specimens
touch skills/bad-name/SKILL.md            # three name rules broken at once
touch skills/vague-description/SKILL.md   # valid, and will never be chosen

# 4 - the two measurement scripts
touch what_a_skill_costs.py describe_or_not.py
cd -

# 5 - confirm the reference library runs, and note the command's real name
uv run --no-project --with skills-ref==0.1.1 agentskills --help
```

**Step 5 is the one to read carefully.** The specification's own page says the command is
`skills-ref validate ./my-skill`. Run that and you get
`error: Failed to spawn: skills-ref — program not found`. The package is `skills-ref`; the command it
installs is **`agentskills`**, read from its own entry points on 2026-09-04. That is Principle 8 paying
for itself on a day that has nothing to do with ADK, and
[5.1](parts/05-in-production/5.1-validating-before-you-ship.md) is where it lands.

**Two scripts need `GOOGLE_API_KEY` and neither generates anything.** `what_a_skill_costs.py` calls
`count_tokens`, which Day 24 established is a separate endpoint on a separate quota
([24.1.1](../day-24-token-accounting-and-budgets/parts/01-what-a-request-costs/1.1-a-ticket-id-costs-five-tokens.md)).
`describe_or_not.py` needs nothing at all.

**Two of the three skills are meant to be wrong.** `bad-name` fails validation with three findings;
`vague-description` passes validation and fails at its job. Both are specimens, both say so in their own
bodies, and the contrast between them is section 4.

**Write the good skill first and validate it before writing the broken ones.** Seeing `Valid skill`
once makes the two failure messages legible.

---

## §4 Build brief

**`skills/ticket-triage/`** — Sutra's first real skill, at the repository root's `skills/` directory
(the layout in CLAUDE.md has been waiting for it since Day 0):

| File | What it is | Taught in |
| --- | --- | --- |
| `SKILL.md` | card + procedure; `name` matching the folder | 1.1, 2.2 |
| the `description` | what **and when**, in the requester's vocabulary | 2.3 |
| `references/SEVERITY.md` | the table, loaded only when the link is followed | 3.2 |
| `scripts/severity_table.py` | the same table as JSON, reading the same file | 3.2 |
| `metadata.version` | quoted, because YAML turns `1.10` into `1.1` | 2.4 |

Three things in that table are the design. The severity table is a **reference, not a body section**,
because it will grow and the body is loaded whole
([3.1](parts/03-the-body-and-the-folders/3.1-the-body-is-loaded-whole.md)). The script **reads** the
reference rather than carrying its own copy, so there is one source of truth. And the description's
second sentence — the *"Use when"* — is the half that carries most of the findability, measured.

**`docs/SKILL_PROVENANCE.md`** — the ledger exists and is empty. Decide its columns now, while there is
one skill in it: name, source, licence, audit date, and whatever `read-properties` gives you for free.
Day 29 fills it with third-party skills; today it gets Sutra's own, which is the easy case to design
against.

**Nothing under `sutra/` changes today.** The format is client-agnostic on purpose, and loading these
folders into ADK is Day 26. Confirm with `git diff` before you commit.

**`TODO(me)` markers left for you:**

- **2.2** — decide Sutra's skill naming convention **now**, before there are two sources. Prefixed by
  owner (`sutra-ticket-triage`) or bare? Write down what happens when a vendor pack arrives with its
  own `triage`.
- **2.3** — collect five real requests you would want `ticket-triage` to answer, run `describe_or_not.py`
  against them, and tune the description until it matches four of them and not the vague one.
- **2.4** — choose Sutra's `metadata` key names — owner, review date, version — and write them where
  Day 30 will find them. The spec's advice is to prefix them so they cannot collide.
- **3.1, 3.2** — take one thing out of the body and put it in `references/`. Measure the activated cost
  before and after, and record both numbers.
- **3.3** — decide the number of skills Sutra is willing to pay for at startup, from your own token
  budget. Day 28 will ask for that number.
- **4.1** — rewrite `vague-description`'s card so it matches three of the five requests **without**
  matching the vague one, then check both halves.
- **5.1** — write down three checks your own lint should make that `agentskills validate` does not.
  Links resolve, tool names exist, description length — those are three; find your own.
- **5.2** — add a `skill` field to Day 22's log line so you can count activations per skill. Then say
  what number you would act on, and in which direction.
- **The spec** — read `agentskills.io/skill-creation/best-practices` and
  `.../optimizing-descriptions`, and write one sentence on what each one adds to today's parts.

---

## §5 The eval that must be able to fail

Today's check is a **validator, not a test suite**, and it can go red in two directions.

```bash
# RED: the deliberately broken skill, three findings, exit 1
uv run --no-project --with skills-ref==0.1.1 agentskills validate \
  days/day-25-skills-the-open-spec/lab/skills/bad-name
echo "exit status: $?"

# GREEN: the good skill, exit 0
uv run --no-project --with skills-ref==0.1.1 agentskills validate \
  days/day-25-skills-the-open-spec/lab/skills/ticket-triage
echo "exit status: $?"
```

Measured on 2026-09-04 against `skills-ref` 0.1.1: three named findings and `exit status: 1`, then
`Valid skill` and `exit status: 0`.

Then break the good one on purpose, four ways:

| Break this | What happens | What it is telling you |
| --- | --- | --- |
| capitalise a letter in `name` | one finding, exit 1 | the identifier rules (2.2) |
| rename the folder only | one finding naming both values | the cross-file rule (2.2) |
| delete the `description` line | validation fails | it is required (2.1) |
| replace the description with `Helps.` | **`Valid skill`, exit 0** | the format cannot check usefulness (4.1) |

**The fourth row is the eval that matters and the one no validator supplies.** So the second check is
Sutra's own, and it is the proxy in `describe_or_not.py`:

```bash
cd days/day-25-skills-the-open-spec/lab
uv run python describe_or_not.py
```

Measured on 2026-09-04: `ticket-triage` scored **7**, `bad-name` 3, `vague-description` **1** — and
deleting only the *"Use when"* sentence from the good description took it from 7 to **3**. That is a
check that can go red, it needs no key, and it is the closest thing to a selection test until Day 30
builds a real one.

**What neither check catches:** whether the body's links resolve, whether the tools it names exist,
whether the script runs, and whether the licence is true. All four are Day 31's lint, and
[5.1](parts/05-in-production/5.1-validating-before-you-ship.md) says so explicitly rather than leaving
you to assume the validator covered them.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| `what_a_skill_costs.py` — six `count_tokens` calls | **0** |
| `describe_or_not.py` — pure Python | **0** |
| `agentskills validate` × 3 | **0** |
| `agentskills read-properties`, `to-prompt` | **0** |
| the skill's own `scripts/severity_table.py` | **0** |
| **Total required** | **0 of 20** |

**Zero.** Nothing today asks a model anything. The one measurement that touches the provider uses
`count_tokens`, which Day 24 verified works even while `generate_content` is refusing with a `429`.

That is worth noticing rather than passing over: a day about **what the model will be shown** costs no
model calls, because the format is text and the cost of text is countable. Day 26 will spend requests;
today does not need to.

**Cost: $0.**

---

## §7 Traps

- **The command is `agentskills`, not `skills-ref`.** The specification page names the package; the
  package installs a differently-named command. Verified from its own entry points, 2026-09-04 (5.1).
- **`name` must match the parent directory.** A rename done in one place fails validation; a copied
  skill brings the old name with it (2.2, 4.2).
- **A useless description is valid.** `Helps with tickets.` passes every check and matched **one** of
  five realistic requests — the vaguest one (2.3, 4.1).
- **Most of the findability is in the second sentence.** Deleting the *"Use when"* half took the score
  from 7 to 3 (2.3).
- **The body is loaded whole on activation**, and stays in context for the rest of the conversation —
  so a table in the body is paid for on every turn (3.1).
- **Quote `metadata` values.** Unquoted, YAML reads `version: 1.10` as the float `1.1`, silently
  breaking any ordering built on it (2.4).
- **A colon in an unquoted description** turns it into a nested mapping. Quote it or write around it
  (2.1).
- **`compatibility` is advisory.** Nothing enforces it; a skill needing tools the client lacks will
  load, validate, be selected, and improvise (2.4, 1.2).
- **`allowed-tools` is marked experimental.** It is not a containment control, and treating it as one
  is a security conclusion drawn from an unfinished field (2.4).
- **`scripts/` executes.** A folder of Markdown can be read before trusting; a folder with code cannot
  be trusted by reading the `SKILL.md` alone (3.2, and Day 29's audit).
- **Every skill's card is paid for on every request.** Two hundred skills of this size is about 7,600
  tokens before the conversation starts, and the cost is linear (5.2).
- **`to-prompt` emits an absolute path** in `<location>`, which is tokens and a directory structure in
  the model's context (5.1).

---

## §8 Verify before you code

Fetched or run on **2026-09-04**, the day this was written:

- `https://agentskills.io/specification` — the whole page, read in full. Every constraint quoted in
  section 2 is copied from it: the six frontmatter fields and their limits, the five `name` rules, the
  1024-character `description` limit, the three optional directories, the three progressive-disclosure
  levels with their token budgets, the 500-line guidance, the file-reference rule, and the validation
  section.
- `https://agentskills.io/llms.txt` — the site's own index, which lists the pages that exist:
  Overview, Specification, Client Showcase, Quickstart, Best practices, Optimizing descriptions,
  Evaluating skills, Using scripts, and a client-implementation guide. Named here because
  [1.3](parts/01-what-a-skill-is/1.3-an-open-spec.md)'s claim that more than one client reads the
  format rests on a page existing rather than on belief.
- `https://pypi.org/pypi/skills-ref/json` — version **0.1.1**, `requires_python >=3.11`, homepage
  `agentskills.io`, repository `github.com/anthropics/agentskills` (Principle 7).
- `importlib.metadata.distribution("skills-ref").entry_points` — returned
  `EntryPoint(name='agentskills', value='skills_ref.cli:main', group='console_scripts')`. **This is the
  fact that contradicts the specification page**, and it was obtained by asking the package rather than
  by reading about it (Principle 8).
- `agentskills --help`, `validate`, `read-properties` and `to-prompt`, all run against the three skills
  in this day's lab. Every output block in the parts is from those runs, including the exit statuses.
- `count_tokens` against each `SKILL.md` and each card, on `gemini-3.7-flash` — the source of every
  token number in sections 3 and 5.
- `yaml.safe_load('version: 1.10')` → `{'version': 1.1}`, run rather than remembered, for
  [2.4](parts/02-the-frontmatter/2.4-the-optional-fields.md)'s trap.

**No adk.dev page was needed today**, and that is the point of putting the spec day before the
`SkillToolset` day: today is about a format that belongs to nobody's runtime. Tomorrow's ADK symbols
get verified tomorrow, against the installed package.

---

## §9 Say it in an interview

"We had a support agent with plenty of capabilities and no procedures. All the knowledge about *how*
the desk actually does a job was in the system prompt, which meant we paid for the triage procedure on
every request including the ones about refunds — and the prompt was getting long enough that adding to
it was becoming a negotiation.

Skills are the format that fixes that. A skill is just a folder with a `SKILL.md` in it: YAML
frontmatter with a name and a description, then Markdown instructions, and optionally `scripts/`,
`references/` and `assets/`. No code required, and that matters, because the person who knows how
triage works isn't necessarily the person who writes Python.

The thing that makes it economical is progressive disclosure, and it's worth being precise about it
because it's the whole design. Only the name and description are loaded at startup, for every skill.
The body is loaded when the agent decides to use it. Reference files are loaded when a link is
followed. I measured ours: 64 tokens to have it available, 292 once activated — so we're carrying about
four and a half times as much procedural knowledge as we pay for at rest.

Two things I'd tell anyone starting. The description is the entire selection interface — the body isn't
loaded yet when the model chooses — so it has to say what the skill does **and when to use it**, in the
words a user would actually type. We measured word overlap against five real requests: a good
description scored seven, 'Helps with tickets' scored one, and deleting just the 'use when' sentence
took the good one from seven to three. And there's no validator for that: a useless description passes
every check.

The other thing is that the fixed cost is linear. Every skill's card is loaded on every request forever,
so two hundred skills is about seven and a half thousand tokens before anyone has said anything. The
expensive skills aren't the big ones — they're the ones that never fire."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 25` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it to
someone else without the page open.

**This is the first day of Phase 4**, whose gate is skills authored, loaded and audited. Today is the
format; the loading is Day 26 and the audit is Day 29.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 25 | <date> | SK-01, SK-02, SK-03 | 14 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows today.** `skills-ref` was run in a throwaway environment and is
not a dependency of this project yet. When Day 31 adopts it for the skills lint, the row is:

```text
| skills-ref | 0.1.1 | 2026-09-04 | 31 | Reference library for Agent Skills. Read from `pypi.org/pypi/skills-ref/json`. Requires Python >=3.11. Dev dependency. **The command it installs is `agentskills`, not `skills-ref`** - the spec page disagrees; the package's own entry point is authoritative. |
```

**`docs/PAPERS.md`** — no new rows. Today has no paper; the origin document is the Agent Skills
specification, cited by URL and fetch date in §8.

**`docs/SKILL_PROVENANCE.md`** — the first row, for Sutra's own skill rather than a sourced one:

```text
| ticket-triage | (first-party) | Apache-2.0 | 2026-09-04 | 25 | `skills/ticket-triage/` |
```

**The commit:**

```text
day 25: skills - the open spec and SKILL.md anatomy - closes SK-01, SK-02, SK-03
```

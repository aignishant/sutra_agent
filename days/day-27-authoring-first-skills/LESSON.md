---
day: 27
phase: 4
phase_name: "Agent Skills"
title: "Authoring Sutra's first skills"
ids: ["SK-06", "SK-07", "SK-08"]
principles: [1, 2, 3, 4, 5, 10, 11, 13, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-04"
status: written
lab_scaffolded: false
commit: ""
---

# Day 27 — Authoring Sutra's first skills

> **Yesterday (Day 26):** the mechanism. One call turns a folder into an object, one toolset gives an
> agent four tools for reaching it, and the whole ladder was measured — 479 tokens of preamble, 83 per
> card, 334 per activation.
> **Today:** something worth loading. Sutra's real triage procedure comes out of an instruction string,
> a docstring, a test and somebody's head, and becomes two reviewable folders — and the instruction
> shrinks from 294 tokens to 157, including one sentence that has been false for twenty days.
> **Tomorrow (Day 28):** progressive disclosure as a design subject — how much goes in the body, how
> many skills, and where the boundaries belong, argued against the two real skills written today.

---

## §1 Where we are

The router in the office is reset by a woman in accounts, and nobody wrote down how.

It takes forty seconds and four steps. In April she was away, the internet went down, four people
stood in front of the cupboard, and the office was offline until the evening — not because the
procedure was hard, but because it had never been outside one person's head.

That is where Sutra's triage procedure is this morning. It exists, it works, and it is in five places:
half a rule in `sutra/desk/agent.py`'s instruction, half in a tool description, a failure behaviour
recorded in a docstring, two behaviours pinned in tests, and the order of the steps in the head of the
person who has been running the loop by hand since Day 3.

Five things worth knowing before you start.

**Extraction is a move, not a copy.** Every rule that goes into a skill comes **out** of the
instruction. Skip that half and you get two documents that disagree, which is measurable: the handbook
says *priority* once and the skill says *severity* nine times, for the same field with the same three
values.

**Scope is decided by a four-word test, and Sutra's procedure fails it.** *"Triage a ticket and draft
the reply"* is two jobs, at two moments, owned by two people. Today produces **two** skills, and their
descriptions share four content words out of forty-seven — a number you check, not a property you hope
for.

**A skill that names a tool has written a contract, and nothing checks it.** Not the validator, not the
loader, not the toolset, not the runtime. Rename `search_kb` in Python and the procedure silently loses
step 3. The lint is twenty lines and it belongs in this day, not in Day 31.

**A skill body is a request, not a rule.** The model may not list the skills, may not activate this
one, and may not follow the line. Anything whose violation would be an incident belongs in a callback
or a tool — the fire door's closer, not the sign on it.

**And a skill is finished when a run of it has been watched, not when it is written.** That costs three
to five generations per iteration, so everything a script can check gets checked first: required tools,
dead links, orphan references, house sections. Four checks, one second, one exit code.

---

## §2 The map

Nineteen parts in six sections, and **no paper** — see §8. The day climbs
`foundation → working → production`: section 1 is the extraction itself, section 2 is the half nobody
does, section 3 pairs the procedure with its tools, section 4 is the authoring loop, section 5 is the
failure lab and section 6 is review and versioning.

### Section 1 — `01-extraction`: from practice to a folder (SK-06)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [Where the procedure lives now, and why that is a problem](parts/01-extraction/1.1-where-the-procedure-lives-now.md) | Five places, four of them Python | `foundation` |
| 1.2 | [One job, four words: choosing a skill's scope](parts/01-extraction/1.2-one-job-four-words.md) | Why this is two skills | `working` |
| 1.3 | [The six-question pass, and where each answer lands](parts/01-extraction/1.3-the-six-question-pass.md) | The box that makes you stop | `working` |
| 1.4 | [Steps a competent stranger can follow](parts/01-extraction/1.4-steps-for-a-competent-stranger.md) | Seven steps for five decisions | `working` |
| 1.5 | [One worked example, and why one is enough](parts/01-extraction/1.5-one-worked-example.md) | The shape the steps cannot teach | `working` |
| 1.6 | [Edge cases are scar tissue](parts/01-extraction/1.6-edges-are-scar-tissue.md) | Name the incident, or delete it | `working` |
| 1.7 | [What goes behind a link, and what a fetch really costs](parts/01-extraction/1.7-what-goes-behind-a-link.md) | Not size — one round trip | `working` |

### Section 2 — `02-what-leaves-the-prompt`: the half nobody does (SK-06)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [One fact, one home: shrinking the instruction](parts/02-what-leaves-the-prompt/2.1-one-fact-one-home.md) | 294 tokens to 157, and one deletion | `working` |
| 2.2 | [What never leaves code](parts/02-what-leaves-the-prompt/2.2-what-never-leaves-code.md) | The sign and the door closer | `production` |

### Section 3 — `03-procedure-and-capability`: the tools travel with the steps (SK-07)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A skill that names a tool has written a contract](parts/03-procedure-and-capability/3.1-a-named-tool-is-a-contract.md) | Four layers, four passes | `working` |
| 3.2 | [Honouring the contract: the tools arrive with the procedure](parts/03-procedure-and-capability/3.2-honouring-the-contract.md) | Four tools, then six | `working` |
| 3.3 | [Two skills, one toolset, no overlap](parts/03-procedure-and-capability/3.3-two-skills-one-toolset.md) | Four shared words out of forty-seven | `working` |

### Section 4 — `04-the-authoring-loop`: skills are tested prose (SK-08)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Draft, run, read, sharpen](parts/04-the-authoring-loop/4.1-draft-run-read-sharpen.md) | Getting out of the car | `working` |
| 4.2 | [Which rung did it climb](parts/04-the-authoring-loop/4.2-which-rung-did-it-climb.md) | A transcript becomes a verdict | `production` |
| 4.3 | [Sharpening without a model: the preflight](parts/04-the-authoring-loop/4.3-sharpening-without-a-model.md) | Four checks, one exit code | `working` |

### Section 5 — `05-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The drill at a locked gate](parts/05-failure-lab/5.1-the-drill-at-a-locked-gate.md) | Six tools against four, and a gap | `production` |
| 5.2 | [💥 Two notices on one door](parts/05-failure-lab/5.2-two-notices-on-one-door.md) | *priority* 1, *severity* 9 | `production` |

### Section 6 — `06-in-production`: after it ships

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Reviewing a skill like code](parts/06-in-production/6.1-reviewing-a-skill-like-code.md) | Three readers, three jobs | `production` |
| 6.2 | [Versioning a procedure, and the answer you cannot explain](parts/06-in-production/6.2-versioning-a-procedure.md) | The register keeps names, not versions | `production` |

**No paper today.** This is a craft day: its material is Sutra's own procedure and the Agent Skills
specification's authoring guidance, which Day 25 cited by URL and fetch date. The one research paper it
leans on — *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*, `arXiv:2201.11903` —
was taught on Day 2 and is cited and linked from
[1.4](parts/01-extraction/1.4-steps-for-a-competent-stranger.md). A paper is taught once in this
curriculum; today it is an address, not a lesson.

---

## §3 Setup — run this

**No package is added today.** Nothing new is installed and no model string changes;
`git diff pyproject.toml uv.lock` must be empty when you finish.

```bash
# 1 - Sutra's real shelf, at the repository root, where sutra/desk/skills.py will look for it
mkdir -p skills/ticket-triage/references skills/kb-answer-style/references
touch skills/ticket-triage/SKILL.md skills/kb-answer-style/SKILL.md
touch skills/ticket-triage/references/severity-rubric.md

# 2 - the day's lab
cd days/day-27-authoring-first-skills
mkdir -p lab

# 3 - section 1: reading what you already have
touch lab/read_the_body.py

# 4 - section 2: the instruction, before and after; and the guard tier
touch lab/instruction_diet.py lab/severity_guard.py lab/test_severity_guard.py

# 5 - section 3: the contract and the wiring
touch lab/required_tools.py lab/before_and_after.py lab/two_skills.py

# 6 - section 4: the loop, the verdict, and the preflight
touch lab/ask_the_desk.py lab/which_rung.py lab/test_which_rung.py lab/preflight.py

# 7 - section 5: the failure lab
touch lab/locked_gate.py lab/two_notices.py

# 8 - section 6: versions
touch lab/log_versions.py
cd -

# 9 - confirm the tools the procedure will name actually exist, before writing about them
uv run python -c "from sutra.loop import TOOLS; print(sorted(TOOLS))"
```

**Step 9 is the gate, and it is not ceremony.** It printed `['lookup_ticket', 'search_kb']` on
2026-09-04. Those two names are about to be written into a Markdown file and matched by string
([3.1](parts/03-procedure-and-capability/3.1-a-named-tool-is-a-contract.md)); getting them from the
dispatch table rather than from memory is the whole discipline of this day in one command.

**Two things move into `sutra/` today**, and they are the only project code the day touches:

- `sutra/desk/skills.py` — the shelf loader, the agent builder, and the reader for the activation
  register ([3.2](parts/03-procedure-and-capability/3.2-honouring-the-contract.md));
- `sutra/desk/agent.py` — the instruction, **shortened**
  ([2.1](parts/02-what-leaves-the-prompt/2.1-one-fact-one-home.md)).

**Write `ticket-triage` completely before starting `kb-answer-style`.** Section 1 is one pass through
one skill; running the same six questions twice in the same order is what keeps the two bodies the same
shape, and Day 28 needs them to be.

**Only `ask_the_desk.py` spends quota.** Everything else — every measurement, every failure, the whole
preflight — runs on `count_tokens` or on nothing at all.

---

## §4 Build brief

**`skills/ticket-triage/`** — Sutra's real triage procedure, at the repository root:

| File or field | What it is | Taught in |
| --- | --- | --- |
| `description` | what, then **when**, in the requester's words | 1.3 |
| body `## Steps` | seven numbered steps, each with its failure branch | 1.4 |
| body `## Worked example` | ticket 4521, with the real tool returns pasted | 1.5 |
| body `## Edge cases` | four lines, four incidents | 1.6 |
| `references/severity-rubric.md` | the policy, behind a link because support owns it | 1.7 |
| `metadata.adk_additional_tools` | `["lookup_ticket", "search_kb"]` | 3.1 |
| `metadata.owner`, `metadata.version` | who may change it, and which version answered | 1.3, 6.2 |

**`skills/kb-answer-style/`** — the same six questions, the same shape, a different audience: the
reporter rather than the engineer, and **no** tool requirement
([3.3](parts/03-procedure-and-capability/3.3-two-skills-one-toolset.md)).

**`sutra/desk/skills.py`** — `SHELF` anchored to the module, `load_shelf` catching per folder,
`build_desk()` passing the tools as `additional_tools` and **not** on the agent, and the fail-fast
decision written down with its reason.

**`sutra/desk/agent.py`** — the instruction, trimmed. The numbered procedure comes out, the false
honesty sentence goes, identity and refusal and tone stay.

**`tests/test_skill_couplings.py`** — the four couplings a reviewer would otherwise carry in their
head ([6.1](parts/06-in-production/6.1-reviewing-a-skill-like-code.md)).

**`TODO(me)` markers left for you:**

- **1.2** — write the scope line for a third skill Sutra will need, then argue it should be a section
  of `ticket-triage` instead, and see which argument wins.
- **1.5** — write the worked example for ticket 4522 and decide whether it is shaped differently enough
  to earn a place in the body.
- **1.6** — add a fifth edge case from something that has genuinely gone wrong for you, and decide
  whether it is an edge or a step.
- **1.7** — price a five-turn conversation with the rubric behind a link and with it inlined, in tokens
  **and** in generations, and say which you would ship on twenty a day.
- **2.1, 4.1** — decide Sutra's fail-fast-or-degrade policy for an unloadable skill and write the
  reason next to the code.
- **2.2** — mark every *never*, *must* and *always* in both bodies and say which tier each belongs in.
- **3.2** — decide whether `lookup_ticket` and `search_kb` are desk tools or triage tools, and write
  down why.
- **4.1** — make `ask_the_desk.py` **collect** the call names and the activation list rather than only
  printing them, so [4.2](parts/04-the-authoring-loop/4.2-which-rung-did-it-climb.md)'s verdict can be
  computed from a run.
- **4.2** — add a second check on tool call **counts**, so a run that called `search_kb` four times is
  distinguishable from one that called it once.
- **4.3** — extend the preflight with the body-names-a-tool check, and decide how much false-positive
  noise it may produce before it is worth having.
- **5.1** — write the assertion the preflight cannot make: that the **built agent** resolves every tool
  its skills declare, after activation.
- **6.2** — decide Sutra's version rule in one sentence and put it in `skills/README.md`, then say what
  should happen when only a reference file changes.

---

## §5 The eval that must be able to fail

The day's gate is the preflight, and it is red or green with an exit code.

```bash
uv run python days/day-27-authoring-first-skills/lab/preflight.py
echo "exit: $?"
```

Measured on 2026-09-04 with both skills finished: `findings: 0` and `exit: 0`.

Then break it, three ways at once — rename `references/severity-rubric.md` to `references/severity.md`,
misspell `search_kb` as `search_kbs` in the metadata, and rename `kb-answer-style`'s `## Edge cases`
heading to `## Notes`:

```text
kb-answer-style: body has no '## Edge cases' section
ticket-triage: requires tool 'search_kbs', which nothing provides
ticket-triage: body links 'references/severity-rubric.md', which does not exist
ticket-triage: reference 'severity.md' is never linked from the body
findings: 4
exit: 1
```

**Three breaks, four findings** — the renamed file is both a dead link and an orphan, which is why the
check runs in both directions.

Two more checks that can go red, both without a model:

```bash
cd days/day-27-authoring-first-skills/lab
uv run python -m pytest test_which_rung.py test_severity_guard.py -q
cd -
uv run python -m pytest tests/test_skill_couplings.py -q
```

Measured the same day: `7 passed` for the verdict function, `3 passed` for the guard, `3 passed` for the
couplings. Then break each on purpose: change the surface expectation in `test_which_rung.py` to three
rungs, delete the `tool.name` check from the guard, and change `lookup_ticket`'s not-found message in
`sutra/loop.py`. Three edits, three different red tests, three different files named.

**And the live one, which is the only thing today that spends quota:**

```bash
uv run python days/day-27-authoring-first-skills/lab/ask_the_desk.py "Triage 4521."
```

What you are looking for, in order: `list_skills`, `load_skill(ticket-triage)`, `lookup_ticket(4521)`,
`search_kb(logout)`, possibly `load_skill_resource(references/severity-rubric.md)`, then the answer,
then `ACTIVATED ['ticket-triage']`.

**No transcript of that run appears anywhere in this day.** On 2026-09-04 the twenty free generations
were already spent and the run returned the `429` reproduced in
[26.3.1](../day-26-loading-skills-into-adk/parts/03-wiring-the-toolset/3.1-a-toolset-not-a-tool.md).
Principle 10 outranks the shape of a document: an invented transcript would be undetectable, so the
command is here and the output is yours. Paste it into your notes with the date, run
[4.2](parts/04-the-authoring-loop/4.2-which-rung-did-it-climb.md)'s verdict on it, and record which
rung you got.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every script in sections 1, 2, 3, 5 and 6 | **0** |
| `count_tokens` in `instruction_diet.py`, `two_skills.py` | **0** (separate endpoint) |
| `preflight.py`, `which_rung.py`, the three test files | **0** |
| `ask_the_desk.py`, one question, one session | **3–5** |
| a second iteration after one edit | **3–5** |
| **Total planned** | **6–10 of 20** |

Two iterations of the loop, not six. The reason is
[4.3](parts/04-the-authoring-loop/4.3-sharpening-without-a-model.md): everything a script can settle is
settled before a request is spent, so the two runs you do make are spent on the two questions only a
model can answer — does the description get selected, and do the steps get followed.

**Cost: $0.**

---

## §7 Traps

- **Extraction is a move, not a copy.** A rule left in both the instruction and the skill will
  eventually exist in two versions with no way to tell which is current (2.1, 5.2).
- **The instruction has been lying since Day 4.** *"You cannot look anything up"* was true on Day 6 and
  stopped being true when tools arrived. Delete it (1.1, 2.1).
- **`priority` and `severity` are the same field with two names.** Nine occurrences against one, and
  the three values agree, which is what makes it hard to see (5.2).
- **The KB is a keyword match.** `search_kb("keeps getting logged out")` returns nothing;
  `search_kb("logout")` returns KB-104. That belongs in a **step**, not in edge cases (1.1, 1.4).
- **A failure branch at the bottom of a document is read after the failure.** It goes inside the step
  (1.4).
- **A worked example with an invented ticket id teaches the invented id** (1.5).
- **An edge case you cannot trace to an incident is a caution**, and cautions dilute the real ones
  (1.6).
- **`references/` is not a size decision.** A fetch is a whole model round trip, which on twenty a day
  is five per cent of the budget (1.7).
- **The link in the body needs the `references/` prefix; the resource key does not.** Two spellings of
  one file, both required (1.7).
- **A skill body cannot enforce anything.** Three chances to be ignored, and no evidence when it is
  (2.2).
- **A guard without a `tool.name` check vetoes every tool in the system** (2.2).
- **`adk_additional_tools` is a string match with no validation** at any layer. Rename a function and a
  procedure silently loses a step (3.1, 5.1).
- **`additional_tools` does not give the agent the tools.** They appear only after a skill that names
  them is activated (3.2).
- **The preflight catches two of the three routes to a locked gate.** The third — a toolset built
  without `additional_tools` — is a fact about the agent, not the shelf (5.1).
- **Reading the answer is not reading the run.** A fluent reply is consistent with the skill never
  loading (4.1, 4.2).
- **`metadata.version` is never read by ADK, and the activation register keeps names without
  versions.** An old answer is unexplainable unless you log it (6.2).

---

## §8 Verify before you code

Run or read on **2026-09-04**, the day this was written:

- **`sutra/loop.py`**, read and run — `TOOLS`, `lookup_ticket`, `search_kb`, and the two tickets and
  two KB articles the worked examples use. Every quoted tool output in both skills came from running
  these, not from memory: `lookup_ticket("4521")`, `search_kb("logout")`, `search_kb("keeps getting
  logged out")` (the miss), `lookup_ticket("4522")`, `search_kb("export")`.
- **`sutra/desk/agent.py`**, read in full — the source of the `priority`/`severity` disagreement in
  [5.2](parts/05-failure-lab/5.2-two-notices-on-one-door.md) and of the stale honesty sentence in
  [1.1](parts/01-extraction/1.1-where-the-procedure-lives-now.md). Both findings are about Sutra's own
  committed code, not about a hypothesis.
- **The installed `google-adk` 2.7.1**, driven directly for every number in sections 3 and 5:
  `load_skill_from_dir`, `SkillToolset.get_tools` with and without `additional_tools`, and the
  activation register. Day 26 verified the surface; today only uses it.
- `count_tokens` against `gemini-3.7-flash` for the instruction (294 → 157), the two bodies (654 and
  375), the rubric (142) and the two-skill index (214). **Zero generations**, on the separate endpoint
  Day 24 verified.
- **`agentskills validate`** (`skills-ref` 0.1.1, run with `uv run --no-project --with`) against both
  finished skills, as Day 25 established
  ([25.5.1](../day-25-skills-the-open-spec/parts/05-in-production/5.1-validating-before-you-ship.md)).
  The format has not changed; the command's real name is still `agentskills`.
- `https://agentskills.io/specification` — re-read for the body-content guidance quoted in section 1:
  step-by-step instructions, examples of inputs and outputs, common edge cases, under 500 lines, detail
  into `references/`.
- `https://arxiv.org/abs/2201.11903` — cited, not re-taught. The dated row is in `docs/PAPERS.md` from
  Day 2.

**No adk.dev page was needed today**, and that is worth noticing: today adds no API surface. Every ADK
symbol it uses was verified on Day 26 against the installed package, and today's work is entirely in
Markdown, in the instruction, and in one new module that composes what Day 26 established.

---

## §9 Say it in an interview

"We had a triage procedure that worked and was written down nowhere. Bits of it were in the system
prompt, bits in a tool docstring, a couple of behaviours in tests, and the actual order of the steps was
in one person's head. So we extracted it into skills.

The thing I'd emphasise is that extraction is a **move**, not a copy. Everybody writes the skill;
almost nobody deletes the rule from the prompt afterwards. When you skip that, you get two documents
that describe the same thing, they drift, and you cannot tell which one the model used. Ours had the
prompt calling the field *priority* and the skill calling it *severity*, same three values — so the
answer depended on whether the skill fired, and any dashboard counting severities was counting half the
runs. We also found a sentence claiming the agent had no lookup tools, which had been false for twenty
days because nobody re-reads the prompt when they add a tool.

Scope turned out to be two skills, not one. The test I use is whether you can name the job in four
words without an 'and', plus two more questions: do the halves happen at the same moment, and would
either half be wanted without the other. Triage and reply-writing failed both — different moment,
different owner — so they split. And I check it rather than trusting it: strip the stopwords from the
two descriptions and count the shared vocabulary. Ours share four content words out of forty-seven, and
none of them is a trigger word.

The part people underestimate is that a skill naming a tool is an unenforced contract. The spec
validator only reads frontmatter, the loader never reads the body, and ADK silently drops a declared
tool name that matches nothing — so renaming a Python function quietly removes a step from a procedure,
and nothing anywhere goes red. We declare the required tools in the skill's metadata and lint them
against the same dispatch table the code uses.

And a skill body cannot enforce anything. The model may not list the skills, may not activate that one,
and may not follow the line — so anything whose violation would be an incident goes in a callback or in
the tool, and the skill explains why. The skill is the sign on the fire door; the callback is the
closer.

Last thing: a skill is finished when a run of it has been watched, not when it is written — and you read
the **event stream**, not the answer, because a fluent reply is consistent with the skill never loading.
On our free tier each iteration costs three to five requests out of twenty, so we run four cheap checks
first: required tools exist, links resolve, no orphan references, house sections present. One second,
one exit code, and it means the expensive runs are spent on the two questions only a model can answer."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 27` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it to
someone else without the page open.

**Phase 4's gate** is skills authored, loaded and audited, with `./m check` green including the skills
lint and the `:free` lint. Today closes the authoring half and hands Day 31 four working checks. Design
is Day 28, sourcing and auditing is Day 29, testing and versioning is Day 30 — and 6.2 has already left
that day a specific gap to close: the activation register keeps names without versions.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 27 | <date> | SK-06, SK-07, SK-08 | 19 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and no model string changed;
`google-adk` stays at 2.7.1 and `gemini-3.7-flash` stays pinned as recorded on 2026-08-26.

**`docs/PAPERS.md`** — no new rows. Today teaches no paper. `arXiv:2201.11903` is cited from
[1.4](parts/01-extraction/1.4-steps-for-a-competent-stranger.md) and already has its dated row from
Day 2.

**`docs/SKILL_PROVENANCE.md`** — two rows, both first-party, and the first real content this ledger has
carried:

```text
| ticket-triage | (first-party) | Apache-2.0 | 2026-09-04 | 27 | `skills/ticket-triage/` |
| kb-answer-style | (first-party) | Apache-2.0 | 2026-09-04 | 27 | `skills/kb-answer-style/` |
```

**The commit:**

```text
day 27: authoring Sutra's first skills - closes SK-06, SK-07, SK-08
```

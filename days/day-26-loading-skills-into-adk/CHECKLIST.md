# Day 26 — CHECKLIST

**IDs closed:** SK-04, SK-05, ADK-24
**Principles served:** 1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18
**Parts:** 17 across 5 sections, no paper

> `./m done 26` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run python -c "from google.adk.skills import load_skill_from_dir; from google.adk.tools import skill_toolset; import google.adk; print('skills api ok on', google.adk.__version__)"
cd days/day-26-loading-skills-into-adk && cd -
uv run python days/day-26-loading-skills-into-adk/lab/load_one.py
uv run python days/day-26-loading-skills-into-adk/lab/inspect_skill.py
uv run python days/day-26-loading-skills-into-adk/lab/skill_in_code.py
uv run python days/day-26-loading-skills-into-adk/lab/load_shelf.py
uv run python days/day-26-loading-skills-into-adk/lab/read_preamble.py
uv run python days/day-26-loading-skills-into-adk/lab/rung_one.py
uv run python days/day-26-loading-skills-into-adk/lab/rung_two.py
uv run python days/day-26-loading-skills-into-adk/lab/rung_three.py
uv run python days/day-26-loading-skills-into-adk/lab/rung_four.py
uv run python days/day-26-loading-skills-into-adk/lab/desk_with_skills.py
uv run python days/day-26-loading-skills-into-adk/lab/tools_after_activation.py
uv run python days/day-26-loading-skills-into-adk/lab/the_register.py
uv run python days/day-26-loading-skills-into-adk/lab/the_missing_tool.py
uv run python days/day-26-loading-skills-into-adk/lab/load_shelf_safely.py
uv run python days/day-26-loading-skills-into-adk/lab/price_the_ladder.py
uv run python days/day-26-loading-skills-into-adk/lab/ask_the_desk.py "Triage ticket 4521."   # 2-4 generations
./m check && ./m trace && git log --oneline -1
```

Expected: `skills api ok on 2.7.1`; then a body of **724** characters with its script already in
memory; the six frontmatter fields with `allowed_tools` as `None`; two `Skill` objects built two ways;
the cards and then everything; the **479**-token preamble with `mentions a skill: False`; four tool
names and an `<available_skills>` block; `334` against a body of `184`; a resource hit, a refused path
and an escalated second miss; `NO_CODE_EXECUTOR`; an agent with **4** tools; **four then six**; the
register growing and not shrinking; **6 / 4 / 4 / 5** and a lint naming `lookup_tickets`;
`rejected: ['bad-name']`; the priced ladder; and finally a `list_skills` call before a `load_skill`
call before an answer. Then `OK all green`, `traceability: 51/199 closed, 0 problem(s)`, one commit.

## Setup

- [ ] `days/day-26-loading-skills-into-adk/lab/skills/` holds **two** skills copied from Day 25
- [ ] The import probe printed `skills api ok on 2.7.1` **before** any code was written against it
- [ ] **No `uv add` was run** — `git diff pyproject.toml uv.lock` is empty
- [ ] `adk_additional_tools` was added to the **lab copy** of `ticket-triage`, not to Day 25's
- [ ] You noticed which measurements were taken before that edit and which after

## Section 1 — `01-loading-a-folder`

- [ ] **1.1** read · ran `load_one.py` · **added a file to `references/` and watched the list grow
      without touching Python** · pointed `SKILL_DIR` at a parent folder and read the exception · said
      out loud which of the two loadings is eager
- [ ] **1.2** read · ran `inspect_skill.py` · **added a top-level key, saw ADK accept it and the spec
      validator refuse it** · said out loud which rung each of the three fields is
- [ ] **1.3** read · ran `skill_in_code.py` · **renamed the built skill to `echo_test` and read the
      validator's message** · said out loud the two cases where in-code is right
- [ ] **1.4** read · ran `load_shelf.py` · **put `bad-name` on the shelf and counted how many skills
      came back** · then put an empty `notes/` folder there and counted again · said out loud what
      happens to the other skills when one will not load

## Section 2 — `02-the-four-tools`

- [ ] **2.1** read · ran `read_preamble.py` · **read all seven rules and picked the two that exist
      because a model misbehaved** · added a second skill and confirmed 2054 did not move · said out
      loud what the preamble costs and whether it grows
- [ ] **2.2** read · wrote `fake_skill_context.py` · ran `rung_one.py` · **confirmed four tools, not
      three** · said out loud where the skills index lives in ADK 2.7.1
- [ ] **2.3** read · ran `rung_two.py` · **deleted `license` and `compatibility` and re-measured the
      118** · asked for a skill that does not exist and read the error dictionary · said out loud the
      three keys `load_skill` returns
- [ ] **2.4** read · ran `rung_three.py` · **asked for `../../.env` and read the refusal** · made two
      misses in one context and watched the second escalate · said out loud the three accepted prefixes
- [ ] **2.5** read · ran `rung_four.py` · **got `NO_CODE_EXECUTOR` on a script that exists** · wrote
      the rule that sits beside SEC-01 for skill scripts · said out loud the two things that would
      switch this rung on

## Section 3 — `03-wiring-the-toolset`

- [ ] **3.1** read · ran `desk_with_skills.py` · **added a plain function beside the toolset and
      watched the count go to five** · read the agent's instruction and the preamble side by side ·
      said out loud what one toolset entry adds beyond tools
- [ ] **3.2** read · added `adk_additional_tools` · ran `tools_after_activation.py` · **saw four
      become six, then removed the metadata line and saw six become four** · decided whether
      `lookup_ticket` is a desk tool or a triage tool, and wrote down why
- [ ] **3.3** read · ran `the_register.py` · **loaded the same skill twice and confirmed the register
      did not change while the tokens were spent again** · said out loud the key's name and its scope

## Section 4 — `04-failure-lab`

- [ ] **4.1** read · **copied `bad-name` onto the shelf and watched `desk_with_skills.py` traceback
      without naming the folder** · wrote `load_shelf_safely.py` and got the folder named · changed the
      `except` to `except Exception: pass` and looked at what an operator would have · **decided
      Sutra's policy — refuse to start, or skip and log — and wrote down why**
- [ ] **4.2** read · ran `the_missing_tool.py` · **confirmed two of the three failures print an
      identical line** · renamed a function in one place only and watched a tool disappear · said out
      loud the three causes and the order to check them
- [ ] **4.3** read · ran `did_it_open.py` on an empty session · **wrote the test that asserts the
      negative case as well as the positive** · said out loud the three model decisions between "a
      skill exists" and "a skill was followed"

## Section 5 — `05-in-production`

- [ ] **5.1** read · ran `price_the_ladder.py` · **priced a five-turn triage conversation in tokens
      and in generations, twice** · said out loud what the scarce resource actually is on this tier
- [ ] **5.2** read · ran the four one-liners · **found one constructor argument this day did not
      mention and read what it does** · opened `adk.dev/skills/` and counted the tools it lists · said
      out loud which source you believe about behaviour and why

## The build

- [ ] `sutra/desk/skills.py` exists; importing it does nothing; `SHELF` is anchored to the module and
      not to the working directory
- [ ] `load_shelf` catches `ValueError` and `OSError` **per folder**, logs the folder name as a
      structured field, and returns the rejects rather than deciding for the caller
- [ ] `build_desk_with_skills()` builds the toolset and the agent, and is called once
- [ ] `skills_used` and `missing_tools` exist and are used by both the tests and the log line
- [ ] `git diff` shows **no** change to `pyproject.toml` or `uv.lock`

## The tests

- [ ] `test_the_four_tools_are_still_four` asserts an **equality**, not a subset, and carries no
      `live` marker
- [ ] `skills_used` is tested on an **empty** session as well as a populated one
- [ ] `missing_tools` is tested against a deliberately misspelled name
- [ ] **Break one on purpose, watch it go red, fix it:** change the surface test's expected list to
      three names, run `uv run python -m pytest -q -m "not live"`, read the failure, put it back

## The eval

- [ ] `the_missing_tool.py` printed **6 / 4 / 4 / 5** and the lint named `lookup_tickets`
- [ ] `load_shelf_safely.py` printed `rejected: ['bad-name']` with the folder named in the log
- [ ] All four rows of §5's break-it table were run and read
- [ ] `ask_the_desk.py` was run **once**, and you pasted your own transcript into your notes with the
      date — **not** copied from this document, which deliberately contains none
- [ ] You recorded which of the three decisions in 4.3 your model actually made

## The budget

- [ ] Total generations spent today: **2–4 of 20**, all of them in one `ask_the_desk.py` run
- [ ] Every other script ran with `count_tokens` or with no provider at all
- [ ] If you hit a `429`, you read the `quotaId` and confirmed it ends in `PerDayPerProjectPerModel`

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PACKAGES.md` — **no new row**, and you confirmed `google.adk.__version__` is still `2.7.1`
- [ ] `docs/PAPERS.md` — **no new row**; `arXiv:2310.08560` is cited from 2.2 and 5.1 and taught on
      Day 20
- [ ] `docs/SKILL_PROVENANCE.md` — **no new row**
- [ ] `./m depth 26` green · `./m trace` prints `51/199 closed, 0 problem(s)` · `./m check` green
- [ ] `git status` shows no `.env`; commit message is the one in §11

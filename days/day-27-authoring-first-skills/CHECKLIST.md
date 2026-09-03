# Day 27 — CHECKLIST

**IDs closed:** SK-06, SK-07, SK-08
**Principles served:** 1, 2, 3, 4, 5, 10, 11, 13, 16, 17, 18
**Parts:** 19 across 6 sections, no paper

> `./m done 27` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run python -c "from sutra.loop import TOOLS; print(sorted(TOOLS))"
uv run python -c "from sutra.loop import lookup_ticket, search_kb; print(lookup_ticket('4521')); print(search_kb('keeps getting logged out')); print(search_kb('logout'))"
uv run python days/day-27-authoring-first-skills/lab/read_the_body.py
uv run python days/day-27-authoring-first-skills/lab/instruction_diet.py
uv run python days/day-27-authoring-first-skills/lab/required_tools.py
uv run python days/day-27-authoring-first-skills/lab/before_and_after.py
uv run python days/day-27-authoring-first-skills/lab/two_skills.py
uv run python days/day-27-authoring-first-skills/lab/locked_gate.py
uv run python days/day-27-authoring-first-skills/lab/two_notices.py
uv run python days/day-27-authoring-first-skills/lab/log_versions.py
uv run python days/day-27-authoring-first-skills/lab/preflight.py; echo "exit: $?"
cd days/day-27-authoring-first-skills/lab && uv run python -m pytest test_which_rung.py test_severity_guard.py -q && cd -
uv run python -m pytest tests/test_skill_couplings.py -q
V="uv run --no-project --with skills-ref==0.1.1"
$V agentskills validate skills/ticket-triage
$V agentskills validate skills/kb-answer-style
uv run python days/day-27-authoring-first-skills/lab/ask_the_desk.py "Triage 4521."   # 3-5 generations
./m check && ./m trace && git log --oneline -1
```

Expected: `['lookup_ticket', 'search_kb']`; then ticket 4521's text, a KB **miss** on the reporter's
phrasing and a **hit** on `logout`; a body of **2539** characters with **7** steps; the instruction at
**294** tokens before the trim and **157** after; `unmet requirements: 0`; **four then six** tools;
`654` and `375` token bodies with an index of `214` and four shared words; `6 tools ... []` against
`4 tools ... ['lookup_ticket', 'search_kb']`; `priority` **1/0** against `severity` **0/9**;
`ticket-triage@1.0`; `findings: 0` and `exit: 0`; then `7 passed`, `3 passed`, `3 passed`; then
`Valid skill` twice; then a `list_skills` call before a `load_skill` call before an answer. Then
`OK all green`, `traceability: 54/199 closed, 0 problem(s)`, and one commit.

## Setup

- [ ] `skills/ticket-triage/` and `skills/kb-answer-style/` exist at the **repository root**
- [ ] The tool names were read from `sutra.loop.TOOLS` **before** being written into any Markdown
- [ ] **No `uv add` was run** — `git diff pyproject.toml uv.lock` is empty
- [ ] `ticket-triage` was finished completely before `kb-answer-style` was started

## Section 1 — `01-extraction`

- [ ] **1.1** read · ran the grep inventory over three files · **found the sentence claiming Sutra has
      no lookup tools** · ran `search_kb` on the reporter's phrasing and watched it miss · wrote the
      five steps from memory and marked what you got wrong
- [ ] **1.2** read · wrote both scope lines, one verb each · created both folders · **wrote a third
      scope line and argued it should be a section instead** · said out loud the four-word test and the
      two questions that catch what it misses
- [ ] **1.3** read · wrote both frontmatters, description **before** body · **put a colon in an
      unquoted description and read the YAML error** · listed five ways an engineer would ask for a
      triage and counted the overlap
- [ ] **1.4** read · wrote the seven steps · **ran the backtick scan and saw two tool names among seven
      spans** · moved step 1's failure branch to the bottom and read the procedure again to feel the
      difference
- [ ] **1.5** read · ran the two tools and **pasted their real output into the example** · wrote the
      4522 example in your notes and decided whether it earns a place in the body
- [ ] **1.6** read · wrote four edge cases, each an `If ... do ...` · **added a fifth from something
      that really went wrong for you** · decided for each whether it is an edge or a step
- [ ] **1.7** read · wrote the rubric into `references/` · **confirmed the body links it and the loader
      sees it** · priced the fetch in generations, not only tokens · said out loud the rule for the
      split

## Section 2 — `02-what-leaves-the-prompt`

- [ ] **2.1** read · measured the instruction **before** the trim · gave every sentence one of the
      three verdicts · **deleted the two that had to go, including the false one** · measured again and
      got 157
- [ ] **2.2** read · wrote `severity_guard.py` and its three tests · **deleted the `tool.name` check,
      watched every tool get refused, and put it back** · marked every *never*/*must*/*always* in both
      bodies and assigned each a tier

## Section 3 — `03-procedure-and-capability`

- [ ] **3.1** read · added `adk_additional_tools` · ran the lint green · **misspelled one name and read
      the finding** · said out loud the four layers that could have checked this and do not
- [ ] **3.2** read · wrote `sutra/desk/skills.py` · ran `before_and_after.py` and **saw four become
      six** · decided whether the two tools are desk tools or triage tools and wrote down why
- [ ] **3.3** read · wrote `kb-answer-style`'s body to the same shape · ran the overlap check ·
      **added `severity` to the second description, looked at the shared list, and took it out**
- [ ] `git diff` shows the instruction trimmed and the two skills added in **one** change

## Section 4 — `04-the-authoring-loop`

- [ ] **4.1** read · **wrote down the expected calls before pressing enter** · ran one live iteration ·
      pasted your own transcript into your notes with the date · made **one** named edit
- [ ] **4.2** read · wrote `which_rung.py` and its seven tests · **moved one check above another and
      watched a test fail** · ran the verdict on your own transcript and recorded the rung
- [ ] **4.3** read · wrote `preflight.py` · **broke three things and got four findings** · said out
      loud which problems belong in the preflight and which need a live run

## Section 5 — `05-failure-lab`

- [ ] **5.1** read · ran `locked_gate.py` and saw the named gap · **ran the desk once with
      `additional_tools=[]` and recorded which of the three behaviours you got** · noticed the preflight
      stayed green
- [ ] **5.2** read · ran `two_notices.py` **before** applying 2.1's trim and saw `priority` 1 /
      `severity` 9 · ran it after and saw `priority` reach zero · added `urgency` to `WORDS` and checked
      both documents

## Section 6 — `06-in-production`

- [ ] **6.1** read · wrote `tests/test_skill_couplings.py` · **changed `lookup_ticket`'s not-found
      message and watched the coupling test go red** · wrote the two review checklists somewhere a
      reviewer will find them
- [ ] **6.2** read · ran `log_versions.py` · **deleted a `version` key and saw `unversioned`** · wrote
      Sutra's version rule in one sentence and decided what happens when only a reference changes

## The build

- [ ] `skills/ticket-triage/SKILL.md` has all three house sections and a linked rubric
- [ ] `skills/kb-answer-style/SKILL.md` has the same three sections and **no** tool requirement
- [ ] `sutra/desk/skills.py`: `SHELF` anchored to the module, per-folder `except (ValueError, OSError)`
      with the folder logged, tools in `additional_tools` and **not** on the agent
- [ ] `sutra/desk/agent.py`: the numbered procedure is gone, the false honesty sentence is gone, and
      identity, refusal and tone remain
- [ ] `grep -c "priority" sutra/desk/agent.py` prints `0`
- [ ] `docs/SKILL_PROVENANCE.md` has a row for each skill

## The tests

- [ ] `test_which_rung.py` covers all five rungs **and** the `load_skill`-that-failed case
- [ ] `test_severity_guard.py` includes the "ignores other tools" case
- [ ] `tests/test_skill_couplings.py` asserts **both halves** of the quoted-string coupling
- [ ] **Break one on purpose, watch it go red, fix it:** change `test_which_rung.py`'s full-climb
      expectation to rung 3, run the suite, read the failure, put it back

## The eval

- [ ] `preflight.py` printed `findings: 0` and `exit: 0` with both skills finished
- [ ] All three breaks in §5 were made and the four findings read
- [ ] `agentskills validate` printed `Valid skill` for both skills
- [ ] `ask_the_desk.py` was run and **your own** transcript is in your notes with the date — this
      document deliberately contains none
- [ ] You recorded the rung, and the second run after your one edit

## The budget

- [ ] Total generations spent: **6–10 of 20**, all of them in `ask_the_desk.py`
- [ ] Every other script ran on `count_tokens` or on nothing at all
- [ ] The zero-cost checks were run **before** the first live iteration

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PACKAGES.md` — **no new row**
- [ ] `docs/PAPERS.md` — **no new row**; `arXiv:2201.11903` is cited from 1.4 and taught on Day 2
- [ ] `docs/SKILL_PROVENANCE.md` — **two rows**, both first-party
- [ ] `./m depth 27` green · `./m trace` prints `54/199 closed, 0 problem(s)` · `./m check` green
- [ ] `git status` shows no `.env`; commit message is the one in §11

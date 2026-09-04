# Day 30 — CHECKLIST

**IDs closed:** SK-17, SK-18, SK-19
**Principles served:** 1, 2, 7, 8, 10, 11, 16, 17, 18
**Parts:** 19 across 6 sections, plus one paper

> `./m done 30` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
# the checks, over the real shelf, from a prompt
uv run python -c "
import pathlib
from tools.skill_checks import check_shelf
findings = check_shelf(pathlib.Path('skills'))
print(f'{len(findings)} finding(s)')
for f in findings: print(' ', f)
"
# the suite: three lanes
uv run python -m pytest tests/test_skills.py -v
# the shelf lane going red on a reference-file edit alone
printf 'S3 - cosmetic.\n' >> skills/ticket-triage/references/severity-rubric.md
uv run python -m pytest tests/test_skills.py -k shelf
git checkout -- skills/ticket-triage/references/severity-rubric.md
# the deliberate failure: a stale suite staying green on a broken shelf
mkdir -p skills/Bad--Name
printf -- '---\nname: Bad--Name\ndescription: Does things.\n---\nBody.\n' > skills/Bad--Name/SKILL.md
uv run python -m pytest tests/test_stale.py tests/test_skills.py
rm -rf skills/Bad--Name tests/test_stale.py
# the paper demo, both arms, no model
cd days/day-30-skill-testing-and-versioning/lab/papers/hints-on-test-data-selection
python demo.py
MUTATION=off python demo.py
cd -
./m depth 30
```

Expected: `0 finding(s)` on a clean shelf; then the suite green with the three lanes visible in `-v`;
then a red `stale-digest` finding naming two hashes, with `SKILL.md` never opened; then
`1 failed, 13 passed` where the failure is the *enumerating* test and `test_the_shelf_passes` is among
the passes; then `mutation score: 2/9 killed` with seven named survivors, and with `MUTATION=off` the
same five tests passing and no report at all. Finally `./m depth 30` green.

## Setup

- [ ] `tools/` exists with an **empty** `tools/__init__.py` and `tools/skill_checks.py`
- [ ] `tests/test_skills.py` exists
- [ ] `days/day-30-skill-testing-and-versioning/lab/papers/hints-on-test-data-selection/` has its
      three files
- [ ] **No `uv add` was run** — `git diff pyproject.toml uv.lock` is empty
- [ ] Nothing under `sutra/` changed

## Section 1 — `01-testing-prose`

- [ ] **1.1** read · named the two piles every repository file belongs to · **gave one edit to a skill
      that changes behaviour and produces no error at all**
- [ ] **1.2** read · defined shape and sense in one sentence each · **named the Sutra artefact that
      passes every check today and should not merge** · said why a model call inside the suite makes
      it worse
- [ ] **1.3** read · stated the three filters · ran one candidate rule of your own through them in
      writing · said which of the six rules ADK already enforces

## Section 2 — `02-checks-as-functions`

- [ ] **2.1** read · `tools/__init__.py` and the `Finding` dataclass exist · **said why the rule tag
      is an identifier rather than a sentence** · named the two callers with different policies
- [ ] **2.2** read · `load()` wraps the ADK loader · **ran it on a folder that does not exist and read
      the finding** · said why `except Exception` would be wrong
- [ ] **2.3** read · `check_skill` and `check_shelf` exist · **ran `load_skills_from_dir` and
      `check_shelf` on the same broken shelf and compared the two outputs** · named the keyword that
      makes the difference
- [ ] **2.4** read · `check_references` exists · **renamed a reference file and saw the dead pointer
      named** · said why the pattern's last character is restricted

## Section 3 — `03-the-suite`

- [ ] **3.1** read · the shelf lane enumerates `skills/` live · **added a temporary folder and watched
      the suite find it with no edit to the test** · said what the *not empty* test protects
- [ ] **3.2** read · `check_description` and `check_body_length` exist · **read a real failure and
      confirmed you could fix it without opening the folder** · said what `assert findings == []`
      gives you over `assert not findings`
- [ ] **3.3** read · every rule has a test that makes it fire · **made one check return `[]`
      unconditionally and confirmed the shelf lane stayed green while the checker lane went red** ·
      restored it
- [ ] Both directions covered: for each rule, a case that fires **and** a case that does not

## Section 4 — `04-skills-built-in-code`

- [ ] **4.1** read · the `a_skill` factory exists · **confirmed the zero-argument call is clean under
      every check that takes a `Skill`** · said what property every default must have
- [ ] **4.2** read · the `pytest.raises` test exists with a `match` · **ran the five-name probe and
      read which clause rejected each** · saw an extra frontmatter key silently kept
- [ ] **4.3** read · named the three folder-bound rules · **renamed a skill folder and watched the
      shelf lane produce evidence no in-memory test could** · restored it

## Section 5 — `05-versioning`

- [ ] **5.1** read · `check_version` exists with its three tags · **removed the quotes from a version
      and watched it come back as a float** · restored it
- [ ] **5.2** read · **the bump table is in `skills/README.md`** (Day 27's open `TODO(me)`, closed) ·
      applied it to a real commit that touched `skills/` · said what plays the role of a changelog
- [ ] **5.3** read · `folder_digest` and `check_digest` exist · every first-party skill carries
      `metadata.digest` · **edited only a reference file and watched the check go red with `SKILL.md`
      untouched** · said why the digest line is excluded from its own hash

## Section 6 — `06-in-production`

- [ ] **6.1** read · **wrote `tests/test_stale.py`, planted `skills/Bad--Name/`, and watched the stale
      suite pass while the honest one failed** · deleted both · `git status` clean
- [ ] **6.2** read · the module docstring names the three lanes · **the boundary test exists, passes
      on purpose, and its docstring says why** · named the four things the suite does not cover and
      who covers each
- [ ] **6.3** read · stated the three steps of the triage fork in order · **named the two moves that
      turn a red suite green without fixing anything** · said what the version adds to a
      `stale-digest` finding

## The paper — read after the parts

- [ ] Read [`papers/01-hints-on-test-data-selection.md`](papers/01-hints-on-test-data-selection.md)
      **after** the parts
- [ ] Ran `python demo.py` — `mutation score: 2/9 killed`, seven named survivors, exit 1
- [ ] Ran `MUTATION=off python demo.py` — the same five tests pass and the report stops there
- [ ] Added one test to `suite.py` and watched a named survivor disappear
- [ ] Can state the two hypotheses the paper rests on, and what the field kept versus what it dropped

## The build

- [ ] `tools/skill_checks.py` exports every symbol in the hub's §4 table
- [ ] Nothing in it prints, exits or raises because a skill is bad
- [ ] `tests/test_skills.py` has all three lanes and no hardcoded list of skill names anywhere
- [ ] `skills/README.md` carries the bump table with the obligation column
- [ ] Every first-party `SKILL.md` has `metadata.version` (quoted), `metadata.changed` and
      `metadata.digest`

## The eval

- [ ] `check_shelf(Path('skills'))` returns `0 finding(s)` on the clean shelf
- [ ] The suite is green, and you have seen it red for a reference-file edit alone
- [ ] You have seen the checker lane go red when a check was neutered, with the shelf lane still green
- [ ] The stale suite reported success on a shelf with a folder that will not load
- [ ] The paper demo printed `2/9 killed` with mutation on and stopped at green with it off

## The budget

- [ ] Total generations spent: **0 of 20** — every check ran on the loader, string matching or hashing
- [ ] You can say why zero is a design requirement here rather than a saving

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PACKAGES.md` — **no new row**
- [ ] `docs/PAPERS.md` — **no new row**; `doi:10.1109/C-M.1978.218136` already has its dated row
- [ ] `docs/SKILL_PROVENANCE.md` — **no new rows**; nothing was sourced today
- [ ] `./m depth 30` green · `./m trace` runs · `git status` shows no `.env`, no `Bad--Name`, no
      `tests/test_stale.py`
- [ ] Commit message is the one in §11

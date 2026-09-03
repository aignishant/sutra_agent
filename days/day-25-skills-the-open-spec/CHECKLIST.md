# Day 25 — CHECKLIST

**IDs closed:** SK-01, SK-02, SK-03
**Principles served:** 1, 2, 4, 7, 8, 11, 13, 15, 16, 17, 18
**Parts:** 14 across 5 sections, no paper

> `./m done 25` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
V="uv run --no-project --with skills-ref==0.1.1"
$V agentskills --help                                                   # the command's real name
$V agentskills validate days/day-25-skills-the-open-spec/lab/skills/ticket-triage
$V agentskills validate days/day-25-skills-the-open-spec/lab/skills/bad-name   # RED on purpose
$V agentskills validate days/day-25-skills-the-open-spec/lab/skills/vague-description
$V agentskills read-properties days/day-25-skills-the-open-spec/lab/skills/ticket-triage
$V agentskills to-prompt days/day-25-skills-the-open-spec/lab/skills/ticket-triage \
                         days/day-25-skills-the-open-spec/lab/skills/vague-description
uv run python days/day-25-skills-the-open-spec/lab/skills/ticket-triage/scripts/severity_table.py
cd days/day-25-skills-the-open-spec/lab
uv run python describe_or_not.py                                        # 0 generations
uv run python what_a_skill_costs.py                                     # 0 generations
cd -
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: three commands listed under `agentskills`; then **`Valid skill`**, then **three named
findings and exit 1**, then **`Valid skill` for the useless one**; then the frontmatter as JSON with
`"version": "1.0"` as a **string**; then an `<available_skills>` block containing **name, description
and location but no body**; then the severity table as JSON; then **7 / 3 / 1** overlapping words; then
**64 against 292**, `115` tokens for three skills and about **7,600 for two hundred**. Then
`OK all green`, `traceability: 48/199 closed, 0 problem(s)`, and one commit.

## Setup

- [ ] `days/day-25-skills-the-open-spec/lab/skills/` holds three skills, two of them specimens
- [ ] `ticket-triage/` has `SKILL.md`, `references/SEVERITY.md` and `scripts/severity_table.py`
- [ ] **No `uv add` was run** — `skills-ref` was used with `--no-project --with`, and
      `git diff pyproject.toml uv.lock` is empty
- [ ] Ran the command the specification names (`skills-ref validate`) and saw it fail, then found the
      real command name from the package's own entry points
- [ ] Confirmed everything except `what_a_skill_costs.py` runs with **no key at all**

## Section 1 — `01-what-a-skill-is`

- [ ] **1.1** read · wrote the good skill and validated it · **deleted the three optional fields and
      validated again to see how little is required** · said out loud the minimum contents of a skill
- [ ] **1.2** read · took one paragraph out of Sutra's instruction and decided out loud whether it is
      instruction, tool description or skill · said out loud one thing a skill can express that a tool
      declaration cannot
- [ ] **1.3** read · ran `--help`, `read-properties` and `to-prompt` · **confirmed the body does not
      appear in the `to-prompt` output** · said out loud what "open" does and does not guarantee

## Section 2 — `02-the-frontmatter`

- [ ] **2.1** read · validated the two-field skill · **added a `metadata` key and re-measured the
      startup cost** · said out loud which field the format does not have
- [ ] **2.2** read · validated `bad-name` and got three findings · **fixed only the capital letter and
      counted what was left** · decided Sutra's naming convention and wrote it down
- [ ] **2.3** read · ran `describe_or_not.py` · **deleted the "Use when" sentence, watched 7 become 3,
      and put it back** · collected five real requests of your own and tuned against them
- [ ] **2.4** read · **removed the quotes around `"1.0"` and looked at the type that came back** · chose
      Sutra's `metadata` key names · said out loud why `allowed-tools` is not a containment control

## Section 3 — `03-the-body-and-the-folders`

- [ ] **3.1** read · **pasted the severity table into the body, re-measured `activated`, and took it
      out** · said out loud how much of the body is loaded on activation
- [ ] **3.2** read · ran the skill's script · **added a fourth severity row and watched the script skip
      it** · said out loud what the agent does with each of the three directories
- [ ] **3.3** read · ran `what_a_skill_costs.py` · **wrote down the number of skills you are willing to
      pay for** · said out loud which of the three levels is paid on every request
- [ ] Confirmed the ratio column and can say what a `1.1x` ratio would mean

## Section 4 — `04-failure-lab`

- [ ] **4.1** read · **saw `Valid skill` on the useless one and four zeros in its column** · rewrote its
      card to match three requests without matching the vague one · said out loud the one signal that
      would reveal this in production
- [ ] **4.2** read · got three findings and `exit status: 1` · **fixed them one at a time and watched
      the list shrink** · said out loud which finding could not come from reading the file alone
- [ ] Can state, in one sentence, why the loud failure is the cheaper of the two

## Section 5 — `05-in-production`

- [ ] **5.1** read · checked `$?` after both a passing and a failing validation · **listed three checks
      your own lint should make that this one does not** · said out loud the two properties a validator
      needs to be usable in a gate
- [ ] **5.2** read · ran the projection · **noticed the absolute path in `<location>` and decided
      whether you care** · said out loud which kind of skill is pure cost

## Build brief

- [ ] `skills/ticket-triage/` written at the repository root, not only in the lab
- [ ] `name` matches the folder, and validation passes
- [ ] The description carries **both halves**, and you measured it against your own five requests
- [ ] The severity table is in `references/`, linked from the body — **not pasted into it**
- [ ] The script **reads** the reference file rather than carrying its own copy of the table
- [ ] `metadata.version` is quoted
- [ ] `docs/SKILL_PROVENANCE.md` columns decided, with the first row written
- [ ] Nothing under `sutra/` changed — confirmed with `git diff`

## The eval that must be able to fail

- [ ] Watched `agentskills validate` go RED on `bad-name` with a non-zero exit
- [ ] **Broke the good skill on purpose:** capitalised a letter in `name` — one finding
- [ ] **Broke it a second way:** renamed the folder only — one finding naming both values
- [ ] **Broke it a third way:** deleted the `description` line — validation fails
- [ ] **Broke it a fourth way:** replaced the description with `Helps.` — **still `Valid skill`**
- [ ] Ran `describe_or_not.py` before and after that fourth break and recorded both scores
- [ ] Wrote down, in one sentence, what neither check catches
- [ ] Fixed everything; both checks green again

## Request budget

- [ ] Total generations for the day: **0 of 20**
- [ ] Confirmed by running the whole demo command and checking your provider dashboard afterwards
- [ ] `what_a_skill_costs.py` used `count_tokens` only — no `generate_content` anywhere in the day

## Ledger

- [ ] `docs/PROGRESS.md` row appended:
      `| 25 | <date> | SK-01, SK-02, SK-03 | 14 | <hash> | ✅ |`
- [ ] `docs/PACKAGES.md` — **no row today**; the `skills-ref` row is written on Day 31 when it is
      actually adopted, and it records that the command is `agentskills`
- [ ] `docs/PAPERS.md` — no row; today has no paper, and §8 names the pages fetched instead
- [ ] `docs/SKILL_PROVENANCE.md` — first row written for `ticket-triage`
- [ ] `./m depth 25` green
- [ ] `./m trace` shows SK-01, SK-02 and SK-03 closed, `48/199`, 0 problems
- [ ] `./m check` green

## Commit

- [ ] `day 25: skills - the open spec and SKILL.md anatomy - closes SK-01, SK-02, SK-03`

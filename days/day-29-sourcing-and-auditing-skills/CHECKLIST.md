# Day 29 — CHECKLIST

**IDs closed:** SK-12, SK-13, SK-14, SK-15, SK-16
**Principles served:** 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18
**Parts:** 17 across 6 sections, plus one paper

> `./m done 29` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
# quarantine proof: nothing in sutra/ reads a fixture
grep -rn "fixtures" sutra/ || echo "clean: sutra/ never reads tests/fixtures/"
# the audit against the poisoned fixture
uv run python days/day-29-sourcing-and-auditing-skills/lab/inventory.py tests/fixtures/skills/evil-helper
uv run python days/day-29-sourcing-and-auditing-skills/lab/audit.py tests/fixtures/skills/evil-helper; echo "exit: $?"
# validation disagrees with the audit
uv run --no-project --with skills-ref==0.1.1 agentskills validate tests/fixtures/skills/evil-helper
# no mid-stream defence: the body is handed over unchanged
uv run python days/day-29-sourcing-and-auditing-skills/lab/no_midstream.py tests/fixtures/skills/evil-helper
# provenance: the pin, and drift on one byte
uv run python days/day-29-sourcing-and-auditing-skills/lab/pinned.py tests/fixtures/skills/evil-helper 493ea089684fd0c3
# the registry, parked: shape and the fifth tool, no cloud
uv run python days/day-29-sourcing-and-auditing-skills/lab/registry_shape.py
uv run python days/day-29-sourcing-and-auditing-skills/lab/local_registry.py
# the routing gate: a clean pack that wrecks routing
uv run python days/day-29-sourcing-and-auditing-skills/lab/sourced_shelf.py; echo "exit: $?"
# the paper demo, both arms, no model
cd days/day-29-sourcing-and-auditing-skills/lab/papers/reflections-on-trusting-trust
python demo.py
TRUST=honest python demo.py
cd -
./m depth 29
```

Expected: `clean: sutra/ never reads tests/fixtures/`; then `3 files, 1323 bytes` and pack digest
`493ea089...`; then the audit's `agenda: 10 items` and `exit: 1`; then `Valid skill` from the validator
(shape passes while the audit rejects); then `identical, trimmed: True` — the body handed over unchanged;
then `match` for the pin, and `DRIFT` if you edit the fixture; then four tools become five with a fetched
skill that has no folder on disk; then `worst margin after the merge: 0 (threshold 1)` and `exit: 1`; then
the demo granting `sesame` with the back door on and denying it with `TRUST=honest`, and the rebuilt
compiler byte-identical only in the honest arm. Finally `./m depth 29` green.

## Setup

- [ ] `tests/fixtures/skills/evil-helper/` and `tests/fixtures/skills/sourced-pack/` exist under
      **`tests/fixtures/`**, the quarantine shelf
- [ ] `grep -rn "fixtures" sutra/` proves nothing in `sutra/` loads a fixture
- [ ] **No `uv add` was run** — `git diff pyproject.toml uv.lock` is empty
- [ ] `skills-ref` was run only via `uv run --no-project --with`, never installed into the project

## Section 1 — `01-the-doors`

- [ ] **1.1** read · named the four doors and the property that orders them · said which of your candidate
      skills come through which door and which you cannot hold still
- [ ] **1.2** read · pinned a real `@main` to its commit hash · **changed one byte and watched the content
      digest change completely** · explained why an audit of an `@main` install is worth nothing
- [ ] **1.3** read · separated a freshness signal from a trust signal · explained why a maintainer
      takeover turns the freshest repo hostile without moving a star

## Section 2 — `02-the-five-pass-audit`

- [ ] **2.1** read · stated the audit's one question · **said why asking a model to check the skill defeats
      the audit** · built `pack.py`'s `Finding` type
- [ ] **2.2** read · ran pass 1 on the poisoned fixture (silent) · **deleted a licence line and watched
      `no-licence` appear** · said why a silent pass 1 is not a safe skill
- [ ] **2.3** read · ran the capability inventory · **found the pre-approval, the script and the outbound
      URL** · contrasted it with `ticket-triage`'s two `wants-tool` findings
- [ ] **2.4** read · ran the body scanner · **saw authority followed by concealment on lines 20-21** ·
      wrote one hostile line all five rules miss and watched it stay silent
- [ ] **2.5** read · ran the link pass on a pack with all four problems · **saw one rename produce a dead
      link and an orphan** · explained why an escaping reference is outside your pin
- [ ] **2.6** read · ran the script pass on the fixture (network + reads-env) · **renamed a `.py` to `.sh`
      and watched it become `not-python`** · said why the pass parses instead of imports

## Section 3 — `03-the-poisoned-skill`

- [ ] **3.1** read · ran `no_midstream.py` and saw the body handed over byte-for-byte · named the three
      legs of the lethal trifecta and which one a sourced skill supplies
- [ ] **3.2** read · **built the three-trap fixture and found all three before peeking** · ran `audit.py`
      to `agenda: 10 items` · wrote the REJECT verdict with the pin and line references · if you found
      fewer than three, noted which lens you under-applied
- [ ] **3.3** read · ran the validator and the audit side by side · **saw `Valid skill` and ten findings on
      the same folder** · stated the two questions validation and audit each answer

## Section 4 — `04-provenance`

- [ ] **4.1** read · **drafted the provenance row for the sourced pack before wiring anything** · said why
      `evil-helper` gets no row and a rejected skill does · confirmed no licence means no run
- [ ] **4.2** read · pinned your own skill and checked it (match) · **edited it and watched `pinned.py`
      go red** · said why re-pinning to clear a red check is the wrong move

## Section 5 — `05-the-registry`

- [ ] **5.1** read · ran `registry_shape.py` and saw the Agent-Registry endpoint · ran `local_registry.py`
      and saw four tools become five with a fetched skill absent from disk · **wrote the config sketch and
      the one organisational condition that makes a registry the right call** · nothing was executed
      against a cloud project

## Section 6 — `06-in-production`

- [ ] **6.1** read · ran `sourced_shelf.py` and saw the worst margin drop to zero · **added the sourced
      skills one at a time and recorded which costs the most margin** · said where the fix belongs
- [ ] **6.2** read · ran the audit and the pin together · **named the containment half for `evil-helper`:
      the tool to deny and the environment variable to withhold** · stated the day in one sentence

## The paper — read after the parts

- [ ] Read [`papers/01-reflections-on-trusting-trust.md`](papers/01-reflections-on-trusting-trust.md)
      **after** the parts
- [ ] Ran `python demo.py` — `sesame` granted through a login built from clean source
- [ ] Ran `TRUST=honest python demo.py` — `sesame` denied, rebuilt compiler byte-identical to clean source
- [ ] Can state what the paper claims and why it means the audit alone is never sufficient

## The build

- [ ] `tests/fixtures/skills/evil-helper/` has all three files with the three planted traps
- [ ] `tests/fixtures/skills/sourced-pack/` has the four skills with the descriptions from §4
- [ ] `lab/pack.py` and the five passes exist and each returns `Finding`s
- [ ] `lab/audit.py` chains the five passes in cheap-to-expensive order and returns an exit code
- [ ] `lab/pinned.py`, `lab/no_midstream.py`, `lab/registry_shape.py`, `lab/local_registry.py`,
      `lab/sourced_shelf.py` all run with zero model calls
- [ ] `lab/papers/reflections-on-trusting-trust/` has the four demo files and both arms run

## The eval

- [ ] `audit.py` on the fixture printed `agenda: 10 items` and `exit: 1`
- [ ] Removing the concealment lines dropped the agenda — the audit reports what is there
- [ ] `pinned.py` printed `match`, then `DRIFT` after a one-line edit
- [ ] `sourced_shelf.py` printed `worst margin after the merge: 0` and `exit: 1`
- [ ] The paper demo granted `sesame` with the back door on and denied it with `TRUST=honest`

## The budget

- [ ] Total generations spent: **0 of 20** — every check ran on static analysis or arithmetic
- [ ] You can say why zero model calls is the thesis of the day, not a saving

## The ledger

- [ ] `docs/PROGRESS.md` row pasted from §11, with the real date and hash
- [ ] `docs/PACKAGES.md` — **no new row**
- [ ] `docs/PAPERS.md` — **no new row**; `doi:10.1145/358198.358210` already has its dated row
- [ ] `docs/SKILL_PROVENANCE.md` — the `support-pack` REJECTED row; `evil-helper` gets **none**
- [ ] `./m depth 29` green · `./m trace` runs · `git status` shows no `.env` and no fixture in `sutra/`
- [ ] Commit message is the one in §11

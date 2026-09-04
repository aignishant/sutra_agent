# Day 45 — definition of done

`./m done 45` refuses to commit while any box below is unticked. Tick a box only when you have run
the thing, not when you remember running it — that is the whole subject of
[6.1](parts/06-failure-lab/6.1-green-because-the-path-did-not-exist.md).

## The reading

- [ ] All nineteen parts read, in section order.
- [ ] You can name the ten checks by id and by what each protects, without scrolling.
- [ ] You can state the two `H` rows and say why they are not in the `CHECKS` tuple.

## The build

- [ ] `tools/mcp_audit.py` exists, imports nothing outside the standard library, and defines
      `Finding`, `Check`, `CHECKS`, `run_all(root)` and `main() -> int`.
- [ ] All ten checks are present, numbered `A01`–`A10`, each with a `rule` sentence written as the
      good state.
- [ ] Every check takes the repository root as an argument, so it can be pointed at a fixture.
- [ ] **Every check treats a missing target as a finding, not a skip.**
- [ ] The four `TODO(me)` decisions in §4 are answered, in writing, beside the code they affect.
- [ ] `./m check` gains exactly one line: `uv run python -m tools.mcp_audit`, after Day 31's two
      linters and before pytest.
- [ ] `grep -n -A 12 "^  check)" m` shows the new stage inside `check)`, not `done)`.
- [ ] `docs/SERVER_PROVENANCE.md` exists with its header, its seven columns, and the line naming
      `tools/mcp_audit.py` as its generator.

## The drills — each one watched, not assumed

- [ ] A fixture tree exists with one deliberate violation per rule, outside `sutra/` and
      `sutra_mcp/`.
- [ ] Each of the ten checks has been watched going **red** against that fixture.
- [ ] The `A01` eval in §5 fails when the planted import is removed and passes when it is there.
- [ ] The skip-variant drill from [6.1](parts/06-failure-lab/6.1-green-because-the-path-did-not-exist.md)
      has been run and the false-green count recorded.
- [ ] The scratch copy used for that drill has been deleted; `git status` is clean of it.

## The audit itself

- [ ] `uv run python -m tools.mcp_audit` has been run on the real repository and its output pasted
      somewhere durable, with today's date.
- [ ] Every finding has a disposition — **fixed** with the change beside it, or **filed** with a day
      number. No third state.
- [ ] The finding count is honest. If it is zero, you have re-read
      [1.2](parts/01-what-an-audit-is/1.2-a-finding-is-the-audit-working.md) and can say why zero is
      correct here.
- [ ] `H1` and `H2` have been done for every server currently in `REGISTRY`, by a person, and
      `reviewed_by` holds a name rather than a boolean.

## The phase gate — all six conditions, answered in writing

- [ ] **1.** Every Phase 6 day (39–45) has its `PROGRESS.md` row, and you have read the gate column
      of each rather than assuming it.
- [ ] **2.** `./m trace` **run**, then `docs/TRACEABILITY.md` read: no open ID from Phase 6 or any
      earlier phase.
- [ ] **3.** `./m check` run on the whole repository, and its exit code recorded.
- [ ] **4.** Every day 39–45 has a populated `parts/` directory; the counts are written down.
- [ ] **5.** All four freshness look-ups run and recorded with today's date and a **quoted fact**
      each — including the ones that came back unchanged.
- [ ] **6.** Deviations recorded, or the absence of any confirmed with
      `git log --oneline -- docs/adr docs/CHANGELOG_PLAN.md`.

## The pin

- [ ] `md.requires('google-adk')` run locally and the `mcp` upper bound read off it.
- [ ] The same field read from the index for the newest `google-adk` release.
- [ ] The verdict written down: pin unchanged, **blocked** rather than deferred, filed under the
      trigger *"revisit when a `google-adk` release declares `mcp>=2`"*.
- [ ] No pin was bumped today, and `git diff pyproject.toml` is empty.

## The ledger

- [ ] `./m depth 45` green.
- [ ] `docs/PROGRESS.md` row appended verbatim from §11, with the real hash and an honest gate
      column.
- [ ] `docs/PACKAGES.md`, `docs/PAPERS.md`, `docs/SKILL_PROVENANCE.md` — no new rows, confirmed
      rather than assumed.
- [ ] Committed as `day 45: phase gate - the full MCP audit of sutra-core - closes MCP-24, MCP-25,
      OPS-09`.

## Say it out loud

- [ ] Name the three failure modes in yourself an audit has to guard against.
- [ ] Explain why a missing target is a finding, using the number of false greens you measured.
- [ ] State the difference between a finding filed with a date and one filed with a trigger.

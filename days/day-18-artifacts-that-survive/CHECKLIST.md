# Day 18 — CHECKLIST

**IDs closed:** ADK-21
**Principles served:** 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18
**Parts:** 15 across 6 sections, no paper

> `./m done 18` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
cd days/day-18-artifacts-that-survive/lab
uv run python first_artifact.py
uv run python what_a_part_is.py
uv run python the_wire.py
uv run python the_wire.py 2>&1 | tail -5
uv run python versions.py
uv run python version_metadata.py
uv run python the_loft.py
uv run python two_scopes.py
uv run python on_disk.py && ls -R artifact_store | head -20
uv run python save_and_find.py
uv run python read_it_back.py
uv run python not_in_context.py
uv run python after_the_restart.py
cd -
uv run python -m pytest tests/test_artifacts.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: bytes in and bytes out at version 0; one artifact that does not know what it is; a run that
prints two lines and a run that prints nothing at all until you redirect the error stream; versions 0,
1, 2 and two different `None`s; a changelog the store wrote for you; 36,280 bytes for one note; a file
that follows the engineer and one that does not; a directory tree with the `user:` prefix stripped out
of it; one event carrying two deltas; fifteen bytes of note becoming 361 characters of prompt; a model
told the artifact's name and not its contents; and finally `None` against the bytes, which is half of
Phase 3's gate. Then `7 passed`, then `OK all green`, then
`traceability: 34/199 closed, 0 problem(s)`, then one commit reading
`day 18: artifacts - files that survive turns - closes ADK-21`.

---

## Before you write anything

- [ ] `./m check` is green and `scripts/trace.py` shows Day 17's count before you change anything
- [ ] Copied `scripted.py` from Day 17's lab into today's
- [ ] Added `artifact_store/` to `.gitignore` **before** running anything that writes to disk
- [ ] Ran `the_wire.py` both ways — with and without `2>&1` — and can say what the difference means

## Section 1 — what an artifact is

- [ ] Ran `first_artifact.py` and saw version 0, the MIME type and the bytes come back (1.1)
- [ ] Can name Sutra's three stores, their readers and their costs (1.1)
- [ ] Ran `what_a_part_is.py` and found the line with `type=None` (1.2)
- [ ] Tried `Blob(data="high")` and saw what the bytes became (1.2)
- [ ] Can say why a text `Part` is not a usable artifact (1.2)
- [ ] Ran `the_wire.py` and read the empty second block (1.3)
- [ ] Can name the three artifact services, which one survives a restart, and which is parked (1.3)

## Section 2 — versions

- [ ] Ran `versions.py` and can explain both `None` lines (2.1)
- [ ] Can say what `save_artifact` returns and why there is no overwrite (2.1)
- [ ] Ran `version_metadata.py` and read the two-line changelog (2.2)
- [ ] Chose a third `custom_metadata` key for Sutra and wrote down why (2.2)
- [ ] Ran `the_loft.py` and read the byte count (2.3)
- [ ] Changed `TURNS` to 200 and looked again (2.3)
- [ ] Can say what `delete_artifact` deletes and what the next version number will be (2.3)
- [ ] Wrote down Sutra's retention rule for notes: save on change, or save on turn

## Section 3 — the two scopes

- [ ] Ran `two_scopes.py` and can explain all three lists (3.1)
- [ ] Removed the `user:` prefix and watched a list go empty (3.1)
- [ ] Ran `on_disk.py` and found the file whose prefix disappeared into the path (3.2)
- [ ] Can describe the artifact tree from the root down, from memory (3.2)
- [ ] Read the traversal error and can say what it does **not** protect you from (3.2)
- [ ] Confirmed `artifact_store/` is ignored by git (`git status` shows nothing)

## Section 4 — in the run

- [ ] Ran `save_and_find.py` and saw one event carrying both deltas (4.1)
- [ ] Can name the four steps of a well-behaved artifact-producing tool (4.1)
- [ ] Ran `read_it_back.py` and compared the two ways of getting the note into a prompt (4.2)
- [ ] Can say what `{artifact.name}` actually inserts (4.2)
- [ ] Ran `not_in_context.py` and can explain each of the four output lines (4.3)
- [ ] Removed `load_artifacts` from the agent and watched the first `True` become `False` (4.3)
- [ ] Can say what happens when a model asks for an artifact name that does not exist (4.3)

## Section 5 — the failure lab

- [ ] Reproduced the missing-service failure and saw a run produce nothing at all (5.1)
- [ ] Read the wrapped traceback on the error stream, and can quote the `ValueError` (5.1)
- [ ] Can name the four failures of this phase that all produce a turn with no answer (5.1)
- [ ] Can say where you would look first, in production, when a turn returns nothing (5.1)

## Section 6 — production

- [ ] `tests/test_artifacts.py` written and green: `7 passed`, no skips (6.1)
- [ ] Can say why the durability test could not have been written yesterday (6.1)
- [ ] Used `tmp_path` rather than a fixed directory, and can say why (6.1)
- [ ] Can name the four stores and the question that routes to each (6.2)
- [ ] `grep -rn "save_artifact" sutra/ | grep -v "sutra/artifacts.py"` returns nothing (6.2)
- [ ] Wrote the attachment rule: generated name, size cap, where the original name is kept (6.2)
- [ ] Ran `after_the_restart.py` and saw `None` against the bytes (6.3)
- [ ] Decided where the production artifact root lives, and what a redeploy does to it (6.3)
- [ ] Can say which half of *state survives restarts* is true today and which is not (6.3)

## The build

- [ ] `sutra/artifacts.py` written: every symbol in the hub's §4 table
- [ ] `note_filename` converts its argument, and you can say why
- [ ] `save_note` writes the artifact **and** both state keys in one call
- [ ] `read_note` loads `(filename, version)` rather than the latest, and handles `None`
- [ ] Module docstring carries the scope rule, the split between stores, and the prohibition
- [ ] `git diff` confirms nothing under `sutra/desk/` changed unless you decided it should

## Tests

- [ ] Watched the suite fail at collection **before** writing the module
- [ ] Dropped the `user:` prefix from `SIGNATURE` and confirmed the scope test goes red
- [ ] Deleted the two state writes in `save_note` and confirmed the reference test goes red
- [ ] Removed `.md` from `note_filename` and confirmed **two** tests go red — then reverted
- [ ] `./m check` prints `OK all green`
- [ ] `./m depth 18` passes

## Request budget

- [ ] Model requests spent today: **0 of 20** — and you can say why zero was possible again
- [ ] If you ran the optional live experiment, write down what you spent and what the model did

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended, with the date and hash you actually observed
- [ ] `docs/PACKAGES.md` — no new rows, and you checked rather than assumed
- [ ] `docs/PAPERS.md` — no new rows; you can say why today has no paper
- [ ] `git status` glance: no `.env`, no `artifact_store/`, no customer file anywhere in the diff
- [ ] Committed as `day 18: artifacts - files that survive turns - closes ADK-21`

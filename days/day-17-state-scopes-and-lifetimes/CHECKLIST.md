# Day 17 — CHECKLIST

**IDs closed:** ADK-19, ADK-20
**Principles served:** 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18
**Parts:** 18 across 7 sections, no paper

> `./m done 17` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
cd days/day-17-state-scopes-and-lifetimes/lab
uv run python what_state_is.py
uv run python what_fits.py
uv run python pad.py
uv run python scopes.py
uv run python one_invocation.py
uv run python where_user_lives.py
uv run python the_cost_of_keeping.py
uv run python in_a_tool.py
uv run python carbon_copy.py
uv run python from_outside.py
uv run python steers.py
uv run python braces.py
uv run python declared.py
uv run python schema_holes.py
uv run python lost_write.py
uv run python who_changed_it.py
cd -
uv run python -m pytest tests/test_state.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: one event and one key; seven values accepted and five that survive JSON; a delta that grows
when you read; five vantage points and four lifetimes; `temp_visible` true then false; three separate
stores; 57,530 bytes against 2; two deltas from one turn; an answer copied into state twice, once as a
string and once as a dictionary; three writes with three authors; an instruction with the holes filled
in; seven templates and one `KeyError`; a schema that fails a whole step; a schema that lets a string
into an `int`; the same key present and absent one line apart; and a severity that went up and came
back down. Then `6 passed, 1 skipped`, then `OK all green`, then
`traceability: 33/199 closed, 0 problem(s)`, then one commit reading
`day 17: session state - prefixes, scopes and lifetimes - closes ADK-19, ADK-20`.

---

## Before you write anything

- [ ] `./m check` is green and `scripts/trace.py` shows Day 16's count before you change anything
- [ ] Copied `scripted.py` from Day 16's lab into today's, and can say why it is copied rather than
      imported across day folders
- [ ] Ran `scopes.py` **first**, before reading section 2's parts
- [ ] Ran `lost_write.py` before writing any code of your own, and can say what it proves
- [ ] Can say why every script today costs zero requests

## Section 1 — what state is

- [ ] Ran `what_state_is.py` and saw one event and one key (1.1)
- [ ] Can say which store is read by the model and which by your code, and what each costs (1.1)
- [ ] Ran `what_fits.py` and counted the gap between "accepted" and "survives JSON" (1.2)
- [ ] Can name the three properties a state value needs, and which one ADK checks (1.2)
- [ ] Ran `pad.py` and can explain what the delta is for (1.3)
- [ ] Added `print(committed)` to `pad.py` and can explain why `escalated` is in it (1.3)
- [ ] Can name the method on `State` that writes when it looks like it reads (1.3)

## Section 2 — the four lifetimes

- [ ] Ran `scopes.py` and can say what each of the five output lines proves (2.1)
- [ ] Removed the `user:` prefix, re-ran, and watched line 4 lose a key (2.1)
- [ ] Ran `one_invocation.py` and saw `temp_visible` go from `True` to `False` (2.2)
- [ ] Can define an invocation without using the word, and say why it is the unit of cost (2.2)
- [ ] Ran `where_user_lives.py` and can say where `user:` keys are actually stored (2.3)
- [ ] Can say which stores you would have to clear to forget an engineer completely (2.3)
- [ ] Ran `the_cost_of_keeping.py` and read both numbers (2.4)
- [ ] Changed `TURNS` to 50 and looked again (2.4)
- [ ] Can give one Sutra value that should be `temp:` and one that must not be (2.4)

## Section 3 — the three safe writes

- [ ] Ran `in_a_tool.py` and saw two deltas, one with two keys (3.1)
- [ ] Can say what happens between a tool's assignment and the value being readable next turn (3.1)
- [ ] Ran `carbon_copy.py` and compared the two stored values **by type** (3.2)
- [ ] Can name the two conditions under which `output_key` writes (3.2)
- [ ] Know what happens when an `output_schema` and the answer disagree — and where the traceback goes
      (3.2)
- [ ] Ran `from_outside.py` and read the three history lines (3.3)
- [ ] Can say what `author` is for, and what a history full of `"user"` costs you (3.3)

## Section 4 — state in the prompt

- [ ] Ran `steers.py` and read the instruction the model actually received (4.1)
- [ ] Noticed the line ADK appends after your instruction (4.1)
- [ ] Ran `braces.py` and can state all seven rules from the output (4.2)
- [ ] Can say what happens to a whole turn when one placeholder is missing, and where the traceback
      appears (4.2)
- [ ] Can name the one character that makes a placeholder optional (4.2)

## Section 5 — a schema for state

- [ ] Ran `declared.py` and read the `StateSchemaError` message (5.1)
- [ ] Can say **where** the schema is checked, and why the tool's own `except` never fired (5.1)
- [ ] Can say what happened to the *valid* key written in the same step (5.1)
- [ ] Ran `schema_holes.py` and looked at the **type** of `ticket_id` in the final line (5.2)
- [ ] Can name the three things the schema does not do (5.2)
- [ ] Decided whether the desk sets `state_schema=DeskState`, and wrote down which failure you prefer

## Section 6 — the failure lab

- [ ] Ran `lost_write.py` and saw the same key present and absent one line apart (6.1)
- [ ] Can explain why the assignment looks like it works (6.1)
- [ ] Can name the one thing every real state write has in common (6.1)
- [ ] Can say what this failure will do differently on Day 47's persistent service (6.1)

## Section 7 — production

- [ ] `tests/test_state.py` written and green: `6 passed, 1 skipped` (7.1)
- [ ] Can say why the tests read back through the **service** rather than the session object (7.1)
- [ ] Can name the test that asserts something does *not* work, and what a red there would mean (7.1)
- [ ] Read the skip reason and left the `TODO(me)` in place (7.1)
- [ ] Can name the four places a fact can live in Sutra, with an example of each (7.2)
- [ ] `grep -rn "state\[" sutra/ | grep -v "sutra/state.py"` returns nothing (7.2)
- [ ] Wrote down a state size budget and the assertion that enforces it (7.2)
- [ ] Ran `who_changed_it.py` and reconstructed a key's whole life from the history (7.3)
- [ ] Can name the two kinds of write that leave no trace in the history (7.3)

## The build

- [ ] `sutra/state.py` written: every symbol in the hub's §4 table
- [ ] Every key is a named constant with its scope in a comment
- [ ] `record_triage` converts `ticket_id` itself, and you can say why the schema will not
- [ ] Module docstring carries the scope rules and the three prohibitions
- [ ] `git diff` confirms nothing under `sutra/desk/` changed unless you decided it should

## Tests

- [ ] Watched the suite fail at collection **before** writing the module
- [ ] Dropped the `user:` prefix from `REPLY_STYLE` and confirmed the prefixes test goes red
- [ ] Dropped the `temp:` prefix from `RAW_SEARCH` and confirmed the trimming test goes red
- [ ] Made `record_triage` store `str(ticket_id)` and confirmed its test goes red — then reverted
- [ ] `./m check` prints `OK all green`
- [ ] `./m depth 17` passes

## Request budget

- [ ] Model requests spent today: **0 of 20** — and you can say why zero was possible
- [ ] If you ran the optional live experiment, write down what you spent and what changed

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended, with the date and hash you actually observed
- [ ] `docs/PACKAGES.md` — no new rows, and you checked rather than assumed
- [ ] `docs/PAPERS.md` — no new rows; you can say why today has no paper
- [ ] `git status` glance: no `.env`, no key in any pasted output
- [ ] Committed as `day 17: session state - prefixes, scopes and lifetimes - closes ADK-19, ADK-20`

# Day 8 — CHECKLIST

**IDs closed:** ADK-06, ADK-07
**Principles served:** 1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18
**Parts:** 16 across 5 sections, no papers

> `./m done 8` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run python days/day-08-sessions-and-services/lab/forgetful.py write
uv run python days/day-08-sessions-and-services/lab/forgetful.py
uv run python days/day-08-sessions-and-services/lab/forgetful_sqlite.py write
uv run python days/day-08-sessions-and-services/lab/forgetful_sqlite.py
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: the first pair prints `found : NoneType`, the second prints `found : Session with 1
events` — the same program, one import different; then `OK all green`, then
`traceability: 16/199 closed, 0 problem(s)`, then one commit reading
`day 08: sessions, runs & in-memory services - the conversation gets an address - closes ADK-06, ADK-07`.

---

## Before you write anything

- [ ] `./m check` is green and `scripts/trace.py` shows Day 7's count before you change anything
- [ ] Wrote `sutra/desk/sessions.py` **first**, and it is the only file in the repository that names
      an `InMemorySessionService` (3.1)
- [ ] `grep -rn "APP_NAME\|USER_ID" sutra/` shows exactly one definition and the rest imports (1.2, 5.1)
- [ ] Can say why today costs **zero** model calls, and why that is a property of the subject

## ADK-06 — the session (section 1)

- [ ] Ran `lab/anatomy.py` and can name all six fields without looking (1.1)
- [ ] Can sort the six into the address and the contents, and say which one a later process needs
      (1.1)
- [ ] Can say why holding a `Session` object across two requests is a bug, and what to hold instead
      (1.1)
- [ ] Ran `lab/near_misses.py` and saw three identical `NoneType`s from three different mistakes (1.2)
- [ ] `fetch()` written, and its message contains **all three** parts of the address — checked by
      reading the output, not by intending it (1.2)
- [ ] Ran `replay.py` from Day 7 against `sutra/desk/.adk/session.db` with `app_name='sutra'` and
      watched it find nothing, correctly (1.2)
- [ ] Can say why the three-part key is a lookup key and **not** an access-control check (1.2)
- [ ] Ran `lab/register_and_board.py` and saw the three stores the prefixed keys were split across
      (1.3)
- [ ] Added a `temp:` key to the initial state, predicted where it would go **before** running, and
      checked (1.3)
- [ ] Can give the one question that decides between an event and a state value (1.3)
- [ ] Ran `lab/ids.py` and saw `AlreadyExistsError`, and the same id succeeding under another user
      (1.4)
- [ ] Wrote the four-line get-or-create the create-then-catch way, and ran it twice (1.4, `TODO(me)`)
- [ ] Can say why check-then-create is a race, in terms of what happens between the two lines (1.4)

## ADK-06 — the run (section 2)

- [ ] Ran `lab/one_run.py` and saw four events under one `invocation_id`, twice (2.1)
- [ ] Deleted `invocation_id=ctx.invocation_id`, re-ran, and watched `distinct runs` go from 2 to 3
      (2.1)
- [ ] Can define a run, a turn and a session in one sentence each (2.1)
- [ ] Ran `lab/off_by_one.py` and can say who put the extra event there and when (2.2)
- [ ] Added `yield_user_message=True`, ran it again, and checked 2.2's "when it breaks" **before**
      concluding the flag is broken (2.2)
- [ ] Can say what a session containing exactly one event tells you, and what it cannot tell you (2.2)
- [ ] Ran `lab/growth.py` and read the `turn-units sent` number (2.3)
- [ ] Changed `num_recent_events` to `after_timestamp` and looked at which events came back (2.3)
- [ ] Can say what `GetSessionConfig` changes and what it does **not** — including what the runner
      loads (2.3)
- [ ] Decided what ends a session in Sutra and wrote it into `sessions.py` as a dated comment
      (2.3, `TODO(me)`)

## ADK-07 — the services (section 3)

- [ ] Ran `lab/interfaces.py` and can name the four abstract methods (3.1)
- [ ] Can say why `append_event` is not one of them, and what that buys every implementation (3.1)
- [ ] Every function signature in `sessions.py` types against `BaseSessionService` — checked (3.1)
- [ ] Ran `lab/drawers.py` and saw the silent append, warning and all (3.2)
- [ ] Mutated a fetched session and confirmed the store did not change (3.2)
- [ ] Can say why the warning printed at the top of the output, and why that matters in a service
      (3.2)
- [ ] Ran `lab/keyword_memory.py` and found the query that matched for the **wrong reason** (3.3)
- [ ] Added a query you were sure would match, watched it fail, wrote down the two words (3.3,
      `TODO(me)`)
- [ ] Can say what an empty memory result does and does not tell you, and why that is a Principle 10
      problem (3.3)
- [ ] Ran `lab/cloakroom.py` and saw versions 0 and 1 of one filename (3.4)
- [ ] Removed `session_id` from a save and read the `InputValidationError` (3.4)
- [ ] Ran `lab/no_credentials.py` and can say why one of the four is `None` on purpose (3.4)
- [ ] Ran `lab/furnished.py` and saw one session found under one app name and not the other (3.5)
- [ ] Can say what `InMemoryRunner`'s `app_name` is, and why you cannot hand it a real store (3.5)

## What "in memory" means (section 4)

- [ ] Ran `lab/forgetful.py` twice and got `NoneType` the second time (4.1)
- [ ] Ran `lab/forgetful_sqlite.py` twice and got a `Session` the second time (4.1)
- [ ] Can name four ordinary events that end a process, and say how many are faults (4.1)
- [ ] Can say why in-memory storage is the best answer to one security question and the worst answer
      to another (4.1)
- [ ] Ran `lab/split_brain.py` and read **both** transcripts before drawing a conclusion (4.2)
- [ ] Changed `turn()` so a missing session raises, ran it again, and decided which you would rather
      have in a service — and wrote down why (4.2)
- [ ] Can say what a sticky session fixes and what it converts the problem into (4.2)
- [ ] Ran `lab/three_stores.py` **twice** and watched one number change (4.3)
- [ ] Can name the three persistent services, and say which one this curriculum will never use and
      why (4.3)
- [ ] Can name three things that change on the swap, none of which appear in the interface (4.3)
- [ ] Decided the shape of `default_service()` under a `SUTRA_STORE` environment variable, and wrote
      down why — without building Day 86 (4.1, `TODO(me)`)

## 💥 The failure lab (section 5)

- [ ] Ran `lab/mismatch.py` and produced all three symptoms (5.1)
- [ ] Can say which of the three a call site can detect, and what the other two look like from there
      (5.1)
- [ ] Noticed that the id in the warning is not the id on the line above it (5.1)
- [ ] Fixed arm B's capital letter and confirmed arm C **still** fails silently (5.1)
- [ ] `announce()` written and called, and you have seen it print before anything else (5.1,
      `TODO(me)`)
- [ ] Can name three things that are **not** the cause and would have cost you an evening (5.1)

## Tests — each one red, then green

- [ ] `tests/test_sessions.py` written and passing (§5)
- [ ] Changed `fetch`'s message to a bare `"session not found"` and watched the third test go red
      naming the missing part, then put it back
- [ ] Made `default_service()` return `None` and watched the first test go red, then put it back
- [ ] Changed `"someone_else"` to `USER_ID` in the fourth test and watched it go red — then read it
      again and said out loud why a test that passes because a lookup **fails** is the shape of every
      security assertion in Phase 10
- [ ] Assigned directly to `stored.state` in the fifth test and watched nothing change
- [ ] Wrote the sixth test: mutating a fetched session changes nothing (`TODO(me)`)
- [ ] Decided whether to keep the `asyncio.run` wrapper or add `pytest-asyncio`, and wrote down the
      number of async tests at which your answer changes (§5, `TODO(me)`)
- [ ] `uv run python -m pytest -q -m "not live"` green across the whole suite, not just today's file

## The request budget

- [ ] Spent **zero** requests, and can say why every part managed that
- [ ] `GOOGLE_GENAI_USE_VERTEXAI=FALSE` still set, and `require_free_tier()` still runs at import
- [ ] No `.db` file from today's labs is staged — `git status` checked, not assumed

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended, with the real date, the real hash and 16 parts
- [ ] `docs/PACKAGES.md` — confirmed no row is owed unless you added `pytest-asyncio`, in which case
      the version was looked up and dated
- [ ] `docs/PAPERS.md` — confirmed no row is owed, and can say why a storage model does not get a
      paper
- [ ] `./m check` green: ruff, format, pytest, depth, trace
- [ ] `uv run python scripts/trace.py` shows ADK-06 and ADK-07 closed and no problems
- [ ] `sutra/loop.py`, `sutra/agent.py`, `sutra/config.py`, `sutra/desk/agent.py` and
      `sutra/desk/events.py` are **unchanged** — checked with `git diff --stat`, not assumed
- [ ] One commit, message exactly as in the hub's §11

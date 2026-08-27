# Day 7 — CHECKLIST

**IDs closed:** ADK-04, ADK-05
**Principles served:** 1, 2, 4, 6, 8, 10, 11, 12, 13, 15, 16, 17, 18
**Parts:** 16 across 6 sections, no papers

> `./m done 7` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run python -m sutra.desk.stream "why does ticket 4521 log people out?"
uv run python days/day-07-events-and-streaming/lab/replay.py sutra/desk/.adk/session.db
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: an answer that appears character by character and is printed exactly once; then a
conversation from Day 6 read back off your own disk; then `OK all green`, then
`traceability: 14/199 closed, 0 problem(s)`, then one commit reading
`day 07: events & streaming - the record the runtime was keeping anyway - closes ADK-04, ADK-05`.

---

## Before you spend a single request

- [ ] `./m check` is green and `scripts/trace.py` shows Day 6's count before you change anything
- [ ] Wrote `sutra/desk/events.py` (part 1.5) **first**, and ran `lab/first_event.py` through it
- [ ] Ran `lab/replay.py` against `sutra/desk/.adk/session.db` and read a conversation from yesterday
      **before** buying a new one (6.1)
- [ ] Can say why fifteen of today's seventeen lab scripts cost nothing, and why that is the shape of
      the subject rather than an accident

## ADK-04 — the event object (section 1)

- [ ] Built an event by hand and printed all seven fields that matter today (1.1)
- [ ] Can name the two properties an event list shares with a bank passbook, and what each buys (1.1)
- [ ] Ran `lab/fields.py` and wrote down **three** fields you cannot yet explain (1.2)
- [ ] Ran `lab/two_spellings.py` and can say why `event.invocationId` fails in Python but appears in
      the dev UI (1.2)
- [ ] Can state where the three sources of truth about a framework's API rank, and why the top one is
      top (1.2)
- [ ] Ran `lab/finality.py` and can name **two** different events that answer `True` (1.3)
- [ ] Understood why an empty state-change event is reported as a final response, and why that makes
      `is_final_response()` a display filter rather than a loop terminator (1.3)
- [ ] Checked your own code for `is_final_response` written **without** parentheses (1.1, 1.3)
- [ ] Ran `lab/actions.py` and watched `append_event` — not the `Event(...)` constructor — apply the
      delta (1.4)
- [ ] Added a third event setting `priority` to `None` and wrote down whether that is what you wanted
      "delete the key" to mean (1.4)
- [ ] Can trace a state change from agent to stored session, naming every object it passes through
      and which one applies it (1.4)
- [ ] `text_of`, `kind_of` and `describe` written, and `describe` used somewhere real (1.5)
- [ ] Can say why `kind_of` checks for a function call **before** it checks for text (1.5)
- [ ] Can give a question `id` answers that `invocation_id` cannot, and the reverse (1.5)

## ADK-05 — the stream (section 2)

- [ ] Ran `lab/felt_time.py`, then ran it again with output redirected to a file, and read both (2.1)
- [ ] Can say which latency number streaming changes and which it does not, without hedging (2.1)
- [ ] Named one thing that can silently un-stream a correct streaming implementation (2.1)
- [ ] `sutra/desk/stream.py` written, run, and its answer printed **once** (2.2)
- [ ] Ran it with `--trace` and pasted your own output into your notes — not this document's (2.2)
- [ ] Can give the three values of `event.partial` and what each means, from memory (2.2)
- [ ] Found the `elif event.partial is False` line and can say why `not event.partial` is a bug (2.2)
- [ ] Ran `lab/count_chunks.py` and looked at whether the joined chunks equal the aggregate (2.3)
- [ ] Ran it again with a question that forces a long answer, and noted which count moved (2.3)
- [ ] Chose one of ADK's three options for the duplicate, **wrote the choice into the file as a
      comment with its date**, and can say why the third option is a trap (2.3)
- [ ] `is_displayable_chunk` rejects a partial event carrying a function call — checked, not assumed
      (2.3)
- [ ] Ran `lab/partial_changes_nothing.py` and saw `0 events, {}` after the chunk (2.4)
- [ ] Can explain, from that result, why ADK sends the complete text a second time (2.4)
- [ ] Can say what is left in a session when a stream dies halfway, and why that makes a client retry
      an idempotency problem (2.4)

## Trap #3 — the yield contract (section 3)

- [ ] Ran `lab/yielding.py` and watched your loop print an event **before** the agent's next line
      (3.1)
- [ ] Can explain what happens to a generator's local variables at a `yield` (3.1)
- [ ] Can name the four things the yield-process-resume ordering guarantees, and which one Phase 9
      needs (3.1)
- [ ] Ran `lab/dirty_read.py`, then deleted the `yield` block and ran it again (3.2)
- [ ] Can define a dirty read in one sentence and give one reason ADK allows one deliberately (3.2)
- [ ] Wrote down what a **failed** run leaves in the session, and why "nothing happened" is wrong
      (3.2)
- [ ] Ran `lab/emitter.py` and saw both arms — the accepted ticket and the `NO_TICKET_ID` event (3.3)
- [ ] Can say what a swallowed error looks like to the logger, the trace and the eval (3.3)
- [ ] Decided where `error_code` goes in `describe`'s line, and did it (3.3, `TODO(me)`)

## The brakes (section 4)

- [ ] Ran `lab/brakes.py` and read the warning that `max_llm_calls=0` produces — including where in
      the output it landed (4.1)
- [ ] Ran `lab/counter.py` and saw three allowed and the fourth refused (4.1)
- [ ] Can say what `max_llm_calls` counts, over what scope, and why it is not a daily budget (4.1)
- [ ] Wrote down the limit you would actually set for Sutra's triage path, and the reasoning (4.1)
- [ ] Ran `lab/strictness.py` and read the `extra_forbidden` error properly, all four parts of it
      (4.2)
- [ ] Ran the same `model_config` check on `LlmAgent` and on `Session`, and wrote down which of your
      daily objects will protect you from a typo (4.2)
- [ ] Checked your own code for `runner.run_config = ...` — the setting that attaches and does
      nothing (4.2, 2.2)

## 💥 The failure lab (section 5)

- [ ] Ran `lab/collecting_a.py` and got `SyntaxError: 'return' with value in async generator` (5.1)
- [ ] Ran `lab/collecting_b.py` and got the `aclose` `AttributeError` **and** the `RuntimeWarning`
      (5.1)
- [ ] Commented out the loop in arm B and saw `stored events: 1 | state: {}` (5.1)
- [ ] Can say why one event in the session is harder to diagnose than zero would be (5.1)
- [ ] Ran `inspect.isasyncgenfunction` against both the broken and the working method (5.1)
- [ ] Can name three things that are **not** the cause, and would have cost you an evening (5.1)

## Reading a run (section 6)

- [ ] Ran `lab/replay.py` and read your own words back out of the database (6.1)
- [ ] Noticed `app_name='sutra.desk'` and can say why it is not `'sutra'` (6.1)
- [ ] Found the `__session_metadata__` key in state and can say who wrote it (6.1)
- [ ] Found the events `kind_of` labelled `other` and decided what to do about them (6.1, `TODO(me)`)
- [ ] Ran `git check-ignore -v sutra/desk/.adk/session.db` again, **after** seeing what is inside it
      (6.1)
- [ ] Gave `replay.py` a session id argument, and can say why that matters more than convenience
      (6.1, `TODO(me)`)

## Tests — each one red, then green

- [ ] `tests/test_events.py` written and passing (§5)
- [ ] Moved the `partial` check below the text check in `kind_of`, watched
      `test_a_chunk_is_labelled_a_chunk` go red, put it back
- [ ] Changed `return joined or None` to `return joined`, watched
      `test_a_state_only_event_has_no_text` go red, put it back
- [ ] Deleted the `if not event.content` guard in `text_of`, watched
      `test_describe_survives_an_event_with_no_content` fail with the `AttributeError` from 1.1, put
      it back
- [ ] Removed `async` from `stream_once`, watched the last test go red before anything ran, put it
      back
- [ ] Wrote the sixth test: a tool-call event is never labelled `text` (`TODO(me)`)
- [ ] `uv run python -m pytest -q -m "not live"` green across the whole suite, not just today's file

## The request budget

- [ ] Spent **5 or fewer** requests, and know which parts they went to (§6)
- [ ] Ran every zero-cost script before any that costs quota
- [ ] `GOOGLE_GENAI_USE_VERTEXAI=FALSE` still set, and `require_free_tier()` still runs at import

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended, with the real date, the real hash and 16 parts
- [ ] `docs/PACKAGES.md` — confirmed no row is owed, and can say why `aiosqlite` is not a Sutra pin
- [ ] `docs/PAPERS.md` — confirmed no row is owed, and can say why a framework's event model does not
      get a paper
- [ ] `./m check` green: ruff, format, pytest, depth, trace
- [ ] `uv run python scripts/trace.py` shows ADK-04 and ADK-05 closed and no problems
- [ ] `sutra/loop.py`, `sutra/agent.py`, `sutra/config.py` and `sutra/desk/agent.py` are
      **unchanged** — checked with `git diff --stat`, not assumed
- [ ] One commit, message exactly as in the hub's §11

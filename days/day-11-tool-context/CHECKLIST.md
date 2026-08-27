# Day 11 — CHECKLIST

**IDs closed:** ADK-12, AG-06
**Principles served:** 1, 2, 4, 6, 8, 9, 10, 11, 13, 15, 16, 17, 18
**Parts:** 16 across 6 sections, no papers

> `./m done 11` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run python days/day-11-tool-context/lab/identity.py
uv run python days/day-11-tool-context/lab/crossed.py
uv run python -m pytest tests/test_tools.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: a tool that returns another person's ticket beside one that cannot; two `ok` statuses written
into the wrong session; a green tool suite; then `OK all green`, then
`traceability: 22/199 closed, 0 problem(s)`, then one commit reading
`day 11: tool context & tool design - the parameter the model never sees - closes ADK-12, AG-06`.

---

## Before you write anything

- [ ] `./m check` is green and `scripts/trace.py` shows Day 10's count before you change anything
- [ ] Ran `lab/invisible.py` and can say what is different about the two schemas (1.1)
- [ ] Read `sutra/desk/tools.py` once, knowing both its tools are pure functions today
- [ ] Read `sutra/desk/sessions.py` and found the `USER_ID` constant that today makes interesting
- [ ] Can say why all sixteen of today's lab scripts cost nothing

## ADK-12 — the extra parameter (section 1)

- [ ] Ran `lab/invisible.py` and saw one parameter in Python and not in the schema (1.1)
- [ ] Can say what ADK does to that parameter before the declaration is generated (1.1)
- [ ] Can say what the model would try to fill in if the parameter were *not* removed (1.1)
- [ ] Ran `lab/detection.py` and saw all three rows (1.2)
- [ ] Can give the two detection rules **in order**, and say which is the fallback (1.2)
- [ ] Read row three carefully: ADK reports `'tool_context'` while `ctx` went to the model (1.2)
- [ ] Confirmed `ToolContext is Context` is `True`, and can say what follows from that (1.2)
- [ ] Adopted the convention: **named `tool_context`, annotated `ToolContext`, last** (1.2)
- [ ] Ran `lab/doors.py` and read the `other public members` line (1.3)
- [ ] Picked one member you cannot explain and found which day owes it to you (1.3)
- [ ] Can name six doors and say which day each one belongs to (1.3)
- [ ] Can say what the context is scoped to, and what a module-level stash destroys (1.3, 5.1)
- [ ] Ran `lab/no_default.py` and compared the **two tracebacks**, not the two messages (1.4)
- [ ] Confirmed the last two output lines are identical — the default bought nothing from ADK (1.4)
- [ ] Can say the worst branch to hide an `AttributeError` on, and why (1.4)
- [ ] Every context parameter in `sutra/` has **no default** (1.4)

## ADK-12 — state from a tool (section 2)

- [ ] Ran `lab/carbon.py` and saw `state._delta is actions.state_delta` print `True` (2.1)
- [ ] Can say which two dictionaries one assignment touches, and what the second becomes (2.1)
- [ ] Noticed `session.state` already holds the key before any event exists — the dirty read (2.1)
- [ ] Tried a nested in-place mutation and watched `after delta` stay empty (2.1, `TODO(me)`)
- [ ] Can say why that bug is invisible until Day 22 (2.1)
- [ ] Ran `lab/reading.py` and saw one argument produce two different answers (2.2)
- [ ] Removed the `"en"` default and watched the first-turn failure the default was preventing (2.2)
- [ ] Can say what a tool's declaration tells the model about the state it reads (2.2)
- [ ] Adopted both disciplines: **document the keys, echo the resolved values** (2.2)
- [ ] Ran `lab/noticeboard.py` and read **1615 against 27** (2.3)
- [ ] Saw `temp:scratch` in the live state and absent from the stored state (2.3)
- [ ] Can say the two things `temp:` protects you from and the one thing it does not (2.3)
- [ ] Can give the three rules and the one question that generates all of them (2.3)
- [ ] Nothing in `sutra/` writes a payload, a secret, or an unnamespaced key to state (2.3)

## AG-06 — designing a tool (section 3)

- [ ] Ran `lab/one_job.py` and compared the two `required` lists (3.1)
- [ ] Can say why a merged tool **cannot** require a reason, in schema terms (3.1)
- [ ] Noticed the split version costs 887 characters against 791 — not double (3.1)
- [ ] Added a third action and watched the description and `required` degrade (3.1, `TODO(me)`)
- [ ] Can give the one-word test for a tool doing two jobs (3.1)
- [ ] Can name something you cannot attach to half a tool (3.1, 4.1)
- [ ] Ran `lab/names.py` and saw `'get data'` declared with a space in it (3.2)
- [ ] Saw the duplicate warning, and the two lists that disagree (3.2)
- [ ] Swapped the duplicates' order and confirmed the *other* description wins (3.2)
- [ ] Can say where a tool's name comes from and what a rename changes (3.2)
- [ ] Ran `lab/arguments.py` and watched four required parameters become two (3.3)
- [ ] Changed `priority` back to `str` and watched the `enum` disappear (3.3)
- [ ] Can name the four kinds of input and say which one is a parameter (3.3)
- [ ] Can say why a hallucinated ticket id is more dangerous in production than in your tests (3.3)
- [ ] Ran `lab/overlap.py` and saw the summary score halve while the whole score barely moved (3.4)
- [ ] Can say why measuring whole descriptions would punish the correct fix (3.4)
- [ ] Can give the swap test and the three fixes in order (3.4)
- [ ] Ran the overlap check over Sutra's two real tools and **recorded the number** (3.4, `TODO(me)`)

## Blast radius (section 4)

- [ ] Ran `lab/blast_radius.py` and saw the audit fail before it passed (4.1)
- [ ] Added an ungated write tool without adding it to `WRITES` and watched the audit say `none` (4.1)
- [ ] Can give the one question that sorts every tool, and the four containment options in order (4.1)
- [ ] Can say why gating reads makes the system **less** safe (4.1)
- [ ] Wrote down which of Sutra's tools are reads and which will be writes (4.1, `TODO(me)`)
- [ ] Decided whether `tools/reads.py` and `tools/writes.py` happens now or later (4.1, `TODO(me)`)
- [ ] Ran `lab/identity.py` and saw `asked` return another person's ticket, correctly (4.2)
- [ ] Read the last two lines: `taken` gives the model **no field** in which to make the bad call (4.2)
- [ ] Deleted the owner check from `taken` and watched the context fail to protect anything (4.2)
- [ ] Can say why `user_id` must not be a parameter, in terms of who writes the text the model reads
      (4.2)
- [ ] Can name the two things `tool_context.user_id` does **not** give you (4.2)
- [ ] `lookup_ticket` returns the **same** answer for *not yours* and *does not exist* (4.2)
- [ ] Wrote a decision beside `USER_ID` in `sutra/desk/sessions.py` (4.2, `TODO(me)`)

## 💥 The failure lab (section 5)

- [ ] Ran `lab/crossed.py` and read the first block knowing there is no error in it (5.1)
- [ ] Found the line reporting `wrote_for: 'u-202'` for a call about **u-101's** ticket (5.1)
- [ ] Noticed u-101's session is **empty** afterwards (5.1)
- [ ] Deleted the `await` and watched the same broken code produce correct output (5.1)
- [ ] Can say what makes a stashed context safe, and name the diff that makes it unsafe (5.1)
- [ ] Can say which environments cannot reproduce this, and why (5.1)
- [ ] Grepped `sutra/` for module-level names assigned inside request handling — found none (5.1)

## In production (section 6)

- [ ] Ran `lab/without_a_model.py` with **no `GOOGLE_API_KEY` set** and watched three tests pass (6.1)
- [ ] Changed the state key in the tool and watched the delta assertion go red (6.1)
- [ ] Can name the four things a hand-built `ToolContext` needs (6.1)
- [ ] Can say why the fixture returns the actions object separately (6.1)
- [ ] Can say what these tests **cannot** tell you, and which day covers that (6.1)
- [ ] Decided where the fixture lives — `tests/conftest.py` or the test file (6.1, `TODO(me)`)
- [ ] Answered the `pytest-asyncio` question either way, in writing (6.1, `TODO(me)`)
- [ ] Ran `lab/parked_doors.py` and read both `ValueError` messages (6.2)
- [ ] Saw `save_artifact` return a **version number** rather than a boolean (6.2)
- [ ] Saved the same filename twice and read the second version (6.2, `TODO(me)`)
- [ ] Can say what a tool that produces a file should return, and which earlier rule that is (6.2)

## Tests — each one red, then green

- [ ] The context fixture written, and building a **fresh** context per test (§5)
- [ ] `test_the_owner_gets_their_ticket` passing, with the real owner id filled in (`TODO(me)`)
- [ ] `test_someone_else_gets_the_same_answer_as_a_missing_ticket` passing
- [ ] `test_a_refused_lookup_writes_nothing` passing
- [ ] Deleted the owner check, watched the second test go red, put it back
- [ ] Changed the refusal to `forbidden`, watched the same test go red for the second reason
- [ ] Moved the state write above the ownership check, watched the third go red, put it back
- [ ] Added `= None` to the context parameter and confirmed **nothing** went red (1.4)
- [ ] Wrote the extra test: **no tool declares a parameter named `user_id`** (§5, `TODO(me)`)
- [ ] Day 10's five tests still pass unchanged
- [ ] `uv run python -m pytest -q -m "not live"` green across the whole suite

## The request budget

- [ ] Spent **0** requests, or knows exactly which optional run cost the ones it spent (§6)
- [ ] `GOOGLE_GENAI_USE_VERTEXAI=FALSE` still set, and `require_free_tier()` still runs at import

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended, with the real date, the real hash and 16 parts
- [ ] `docs/PACKAGES.md` — no row owed, unless you adopted `pytest-asyncio`, in which case an exact
      `==` pin with the date and the reason
- [ ] `docs/PAPERS.md` — confirmed no row is owed, and can say why Toolformer is not re-taught
- [ ] `./m check` green: ruff, format, pytest, depth, trace
- [ ] `uv run python scripts/trace.py` shows ADK-12 and AG-06 closed and no problems
- [ ] `sutra/desk/agent.py`, `sutra/loop.py` and `sutra/agent.py` are **unchanged** — checked with
      `git diff --stat`, not assumed
- [ ] One commit, message exactly as in the hub's §11, naming the `USER_ID` decision

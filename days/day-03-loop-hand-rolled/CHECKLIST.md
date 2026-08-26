# Day 3 — CHECKLIST

**IDs closed:** AG-03
**Principles served:** 1, 2, 4, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18
**Parts:** 14 across 7 sections

> `./m done 3` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run python -m sutra.loop "Ticket 4521 says the user keeps getting logged out. What should we tell them?"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: a three-step trace ending in a `FINAL:` that names `KB-104` and `SameSite`; then
`OK all green`, then `traceability: 6/199 closed, 0 problem(s)`, then one commit reading
`day 03: the loop, hand-rolled - think, act, observe - closes AG-03`.

---

## Setup — nothing is installed today

- [x] `uv run python -c "from sutra.mechanics import ask, MODEL; print(MODEL)"` succeeds — Day 2
      actually landed, and today builds on it rather than around it
- [x] `sutra/loop.py` and `tests/test_loop.py` created
- [x] `days/day-03-loop-hand-rolled/lab/` created
- [x] **`pyproject.toml` and `uv.lock` are unchanged** — and you can say why an agent needs no
      dependency at all
- [x] `./m check` was green **before** you started writing

## AG-03 — the loop's anatomy (section 1)

- [x] Can name the three beats and say **which two are your code**
- [x] Can say why "the agent decided to delete the file" is never an acceptable sentence in an
      incident report, and which layer the incident actually lives in
- [x] Can say what is getting smarter as a loop runs, given that the model does not change
- [x] Can state the consequence of "what is not in the transcript never happened" in one sentence

## AG-03 — tools and the dispatch table (section 2)

- [x] `TICKETS` and `KB` written with **synthetic data only** — no real personal or employer data
- [x] `lookup_ticket` and `search_kb` written; both are `str -> str` with type hints on both ends
- [x] Called both functions directly, with **no model in the room and zero tokens spent**
- [x] `TOOLS` is a **literal dict**, not built by scanning the module or a decorator — and you can
      say why that matters for answering "what can this agent do?"
- [x] `_dispatch` uses `.partition(" ")` and `.get`, and can never raise on malformed input
- [x] `_dispatch("send_email boss@corp")` returns the **menu as a string**, not an exception
- [x] Can state the two species of error and which one raises (1.x→2.x trap #4 · Principle 10)
- [x] There is **no `try` around `_dispatch`** in your loop, and you can say why that is the design

## AG-03 — the protocol and the parser (section 3)

- [x] `SYSTEM` written as a module-level constant, so a behaviour change is a reviewable diff
- [x] Can say what is actually *enforcing* the reply format (and why "politeness" is the honest word)
- [x] `_menu_is_complete()` returns `True`, and you can say which silent bug it exists to catch
- [x] `_parse` scans **every line** rather than indexing one, and survives a preamble
- [x] `_parse` slices by the marker's length, **not** `.split(":")[1]` — and you can give the exact
      model reply that breaks the second one
- [x] A multi-line `FINAL:` answer keeps its later lines
- [x] A reply with no marker returns `(None, None)` — and you can say why guessing would be worse
- [x] Watched a real format miss and the coaching observation that answers it

## AG-03 — assembling and running (section 4)

- [x] `_model_turn` — solved the `TODO(me)` by reading a **real object**, not by guessing
- [x] `run_loop` written; can name the **four ordering decisions** and what breaks if each reverses
- [x] `observation` is pre-bound before the loop, and you can say which argument makes that necessary
- [x] `main()` returns an exit code and `load_env()` runs **before** `genai.Client()`
- [x] Ran the real question and got a `FINAL:` answer in three steps
- [x] **Applied the citation test**: `SameSite` appears in an observation *before* it appears in the
      answer, and `KB-104` is cited
- [x] Counted the `ACTION:` lines and got `2` — the answer was earned, not recalled
- [x] Ran the ticket that does not exist and the agent **said so** rather than describing it
- [x] If it fabricated, wrote down the exact sentence — that is entry one in your Day 79 eval suite
- [x] Can say why every naive metric *improves* when an agent invents

## AG-03 — containment (section 5)

- [x] The loop is a `for` over `range`, **not** a `while`, and you can say whose judgement you are
      declining to trust
- [x] Watched a run hit the step budget and return an honest stop message
- [x] Can say why the budget stop neither raises nor asks the model for a best guess
- [x] `_cost_table` written; ran a real triage and **read the `input` column climbing**
- [x] Can give the arithmetic for why six steps cost more than six times one step
- [x] Can say why a tool returning a whole document is a budget bug rather than a formatting choice
- [x] Can name the one property a transcript needs before prompt caching helps

## 💥 The failure lab (section 6)

- [x] Commented out the observation `append` and **watched the agent repeat itself**
- [x] Can say why the model's behaviour in that run is *correct*
- [x] Printed the actual payload of the next call and confirmed the tool result was **not in it**
- [x] Ran the other half — deleted the model-reply append instead — and read how differently it fails
- [x] **Restored the line.** `grep -n "the failure lab" sutra/loop.py` prints nothing
- [x] Can name the single metric that would surface this bug across a thousand runs you never read

## 🅿️ Parked (section 7)

- [x] Can name at least four things a text protocol cannot express, and the day that fixes each
- [x] Can say why the model's *command* channel and the tool's *data* channel being the same list is
      the deepest of today's leaks
- [x] Can give one honest reason to **keep** `sutra/loop.py` after Day 4 replaces the protocol

## Read the parts — one box each

Tick only when you have **read it, run its Check yourself, and answered its out-loud question**.

- [x] [1.1 The navigator and the driver](parts/01-loop-anatomy/1.1-the-navigator-and-the-driver.md)
- [x] [1.2 The transcript is the world](parts/01-loop-anatomy/1.2-the-transcript-is-the-world.md)
- [x] [2.1 Tools are plain functions](parts/02-tools-and-dispatch/2.1-tools-are-plain-functions.md)
- [x] [2.2 The dispatch table is the boundary](parts/02-tools-and-dispatch/2.2-the-dispatch-table-is-the-boundary.md)
- [x] [2.3 A failed tool is an observation, not a crash](parts/02-tools-and-dispatch/2.3-a-failed-tool-is-an-observation.md)
- [x] [3.1 A contract enforced by politeness](parts/03-the-protocol/3.1-a-contract-enforced-by-politeness.md)
- [x] [3.2 Parsing a reply you did not write](parts/03-the-protocol/3.2-parsing-a-reply-you-did-not-write.md)
- [x] [4.1 Assembling the loop](parts/04-running-the-loop/4.1-assembling-the-loop.md)
- [x] [4.2 The first real run](parts/04-running-the-loop/4.2-the-first-real-run.md)
- [x] [4.3 The honest failure](parts/04-running-the-loop/4.3-the-honest-failure.md)
- [x] [5.1 The step budget](parts/05-containment/5.1-the-step-budget.md)
- [x] [5.2 The transcript is a bill](parts/05-containment/5.2-the-transcript-is-a-bill.md)
- [x] [6.1 💥 The goldfish loop](parts/06-failure-lab/6.1-the-goldfish-loop.md)
- [x] [7.1 🅿️ What a schema would have caught](parts/07-the-text-protocol-ceiling/7.1-what-a-schema-would-have-caught.md)

### The paper — read after the parts

- [x] [*ReAct: Synergizing Reasoning and Acting in Language Models*](papers/01-react.md)
      — ran both conditions, **pasted the real transcripts into the demo's `TODO(me)` block**, and
      can say what each one did after its first bad tool call

## Tests — including one you watch go red

- [x] `test_an_action_is_read_from_any_line` passes
- [x] `test_a_final_answer_keeps_its_later_lines` passes
- [x] `test_a_format_miss_returns_nothing_rather_than_guessing` passes
- [x] `test_every_tool_is_advertised` passes
- [x] `test_a_missing_ticket_says_so_readably` passes
- [x] `test_the_step_budget_is_a_hard_ceiling` passes — **offline, with a fake client**
- [x] `test_the_loop_appends_both_halves_of_every_exchange` passes
- [x] **Broke it on purpose:** changed the `for` to a `while True:` and watched the budget test hang;
      killed it, read the line it was sitting on, put the `for` back
- [x] **Broke it on purpose:** added a key to `TOOLS` without touching `SYSTEM` and watched
      `test_every_tool_is_advertised` go red
- [x] Solved the `TODO(me)` fifth test — the tool's result actually appears in the **payload** of the
      next call
- [x] `uv run python -m pytest -q -m "not live"` is green and needs **no key**
- [x] `uv run ruff check .` and `uv run ruff format --check .` are clean

## Budget

- [x] Ran the demos **one at a time** rather than all at once
- [x] Ran the failure lab with `max_steps=3` if quota was tight
- [x] If a 429 appeared, watched the wrapper read the server's stated delay and wait it out
- [x] Wrote down roughly how many calls the day actually cost you, against the ~34 estimated

## Ledger & commit

- [x] `docs/PROGRESS.md` — row appended with the real date and the real commit hash
- [x] `docs/PACKAGES.md` — **no new row**, and you confirmed `uv.lock` is unchanged
- [x] `./m depth 3` passes
- [x] `./m trace` shows AG-03 closed and **no** open ID from a completed phase
- [x] `./m check` green
- [x] Committed as `day 03: the loop, hand-rolled - think, act, observe - closes AG-03`
- [x] Wrote the commit hash back into the `PROGRESS.md` row

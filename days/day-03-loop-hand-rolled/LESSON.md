---
day: 3
phase: 1
phase_name: "Foundations"
title: "The loop, hand-rolled — think, act, observe"
ids: ["AG-03"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 14
generated: "2026-08-25"
status: written
lab_scaffolded: false
commit: ""
---

# Day 3 — The loop, hand-rolled: think, act, observe

> **Yesterday (Day 2):** you met the model as it really is — metered in tokens, amnesiac between
> calls, and finishing every reply with a weighted dice roll. You built one door, `ask`, and proved
> that "memory" is a list you maintain yourself.
> **Today:** that list gets a `for` statement around it, and the amnesiac becomes an agent. You
> hand-roll the whole mechanism — the protocol, the parser, the dispatch table, the brake — with no
> framework anywhere near it, and then you break it on purpose to see what the model actually sees.
> **Tomorrow (Day 4):** the provider's own function calling replaces the text protocol, and you
> arrive with a written list of exactly what it has to fix.

---

## §1 Where we are

Yesterday's model has a brilliant mind and no hands. It cannot open a file, read a database, or close
a support ticket. It can do one thing: read text, and write text back.

So think about how a rally car gets up a mountain. The navigator has the maps and the pace notes and
can see three corners ahead — and never touches the wheel. The driver has hands and feet and no map
at all. The car survives because of a small ritual repeated every few seconds: the navigator calls
one instruction, the driver acts on it, and then the world answers back — the car grips or slides,
the corner opens or closes — and the navigator hears that before calling the next note.

Instruction. Action. Result. Around again.

That is the whole of what you are building today, and two of those three beats belong to **your
code**. The model only ever *asks*. Whether anything happens is a decision your loop makes, on one
line, which you will be able to point at by this evening. Every safety property this project will
ever have — approvals, spend caps, audit trails, the ability to stop — attaches to that line.

There is also a brake, and it goes in today rather than later. A ritual with no way to stop is not a
rally car; it is an accident that has not finished happening yet.

---

## §2 The map

Fourteen parts in seven sections, then one paper. The day climbs `foundation → working →
production`, ends with a deliberate failure, closes with a parked inventory of everything today's
design cannot do — and only then shows you that the whole loop is a 2022 paper.

### Section 1 — `01-loop-anatomy`: what an agent actually is

The shape that survives after the syntax is forgotten.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The navigator and the driver](parts/01-loop-anatomy/1.1-the-navigator-and-the-driver.md) | What is an agent, mechanically — and why is "the agent decided to" never an acceptable sentence? | `foundation` |
| 1.2 | [The transcript is the world](parts/01-loop-anatomy/1.2-the-transcript-is-the-world.md) | If the model forgets everything, what is getting smarter as the loop runs? | `foundation` |

### Section 2 — `02-tools-and-dispatch`: the one door to the real world

Two functions, one dict, and the security boundary of the entire system.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Tools are plain functions](parts/02-tools-and-dispatch/2.1-tools-are-plain-functions.md) | What makes a function a "tool"? (Nothing. That is the answer.) | `foundation` |
| 2.2 | [The dispatch table is the boundary](parts/02-tools-and-dispatch/2.2-the-dispatch-table-is-the-boundary.md) | Why is the set of things your agent can do exactly the set of keys in one dict? | `working` |
| 2.3 | [A failed tool is an observation, not a crash](parts/02-tools-and-dispatch/2.3-a-failed-tool-is-an-observation.md) | Which errors come back as text, which must raise, and what does confusing them cost? | `working` |

### Section 3 — `03-the-protocol`: a contract with no compiler

The model can only emit text, so you invent a shape for it and ask nicely.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A contract enforced by politeness](parts/03-the-protocol/3.1-a-contract-enforced-by-politeness.md) | What is actually enforcing the format the model replies in? | `working` |
| 3.2 | [Parsing a reply you did not write](parts/03-the-protocol/3.2-parsing-a-reply-you-did-not-write.md) | Why is a parser that guesses worse than a parser that fails? | `working` |

### Section 4 — `04-running-the-loop`: assembly, and what a real run proves

Where every piece already works and only the order is hard.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Assembling the loop](parts/04-running-the-loop/4.1-assembling-the-loop.md) | Which four ordering decisions is `run_loop` made of, and what breaks if each is reversed? | `working` |
| 4.2 | [The first real run](parts/04-running-the-loop/4.2-the-first-real-run.md) | The answer is correct — so how do you know the loop did anything at all? | `working` |
| 4.3 | [The honest failure](parts/04-running-the-loop/4.3-the-honest-failure.md) | What happens when the tool finds nothing, and why is that the only run that tests trust? | `production` |

### Section 5 — `05-containment`: the brake ships with the engine

Principle 13, twice: a bound on how far it can go, and a bound on what it can cost.

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The step budget](parts/05-containment/5.1-the-step-budget.md) | Why is the loop a `for` over a range rather than a `while`, and what happens when it runs out? | `production` |
| 5.2 | [The transcript is a bill](parts/05-containment/5.2-the-transcript-is-a-bill.md) | Why does a six-step run cost far more than six calls? | `production` |

### Section 6 — `06-failure-lab`: the deliberate failure

Today's failure, staged on purpose (plan §17.7).

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The goldfish loop](parts/06-failure-lab/6.1-the-goldfish-loop.md) | Delete one line: why does the agent repeat itself, and why is the model behaving correctly? | `production` |

### Section 7 — `07-the-text-protocol-ceiling`: 🅿️ parked, for reading not building

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [🅿️ What a schema would have caught](parts/07-the-text-protocol-ceiling/7.1-what-a-schema-would-have-caught.md) | Nine things a line of text cannot express — and which day fixes each | `production` |

### The paper — read after the parts

*Today's loop is not this project's invention. It lives in this day's `papers/` directory rather
than in `parts/`, because where an idea came from is a different errand from what the day teaches —
and "what survived and what did not" only means something once you have built the thing.*

| Paper | What it answers | Level |
| --- | --- | --- |
| [*ReAct: Synergizing Reasoning and Acting in Language Models*](papers/01-react.md) | Why does your `SYSTEM` prompt demand a thought before every action? | `production` |

---

## §3 Setup — run this

**Nothing is installed today.** No new package, no new provider, no new key. Today's loop is written
against `google-genai`, which arrived yesterday, and the standard library. That is worth noticing
rather than skipping past: an agent is a control-flow pattern, not a dependency.

```bash
# 1 - confirm yesterday actually landed. Today's loop imports from it.
uv run python -c "from sutra.mechanics import ask, MODEL; print('day 2 ok:', MODEL)"

# 2 - today's two files
touch sutra/loop.py tests/test_loop.py

# 3 - a scratchpad for your own experiments
mkdir -p days/day-03-loop-hand-rolled/lab

# 4 - the gate, before you write anything, so you know it was green to start with
./m check
```

If step 1 raises `ModuleNotFoundError: No module named 'sutra.mechanics'`, **stop and finish Day 2.**
Today builds directly on `ask` — the 429 handling, the `store=False` decision and the honest re-raise
are all inherited, not rewritten, and a loop that calls the SDK directly has quietly abandoned three
of yesterday's decisions.

`pyproject.toml` and `uv.lock` do not change today. If they do, something was installed that this day
did not ask for.

---

## §4 Build brief

One new module and one new test file. Every `TODO(me)` stays unsolved — this project does not do your
reps.

**`sutra/loop.py`** — importable with **no side effects**; runs only via
`uv run python -m sutra.loop "<question>"`:

| Symbol | What it does | Taught in |
| --- | --- | --- |
| `TICKETS`, `KB` | synthetic desk data — never real personal or employer data | 2.1 |
| `lookup_ticket(ticket_id)` | the raw text of one ticket, or a readable miss | 2.1 |
| `search_kb(query)` | naive keyword match over the KB, or a readable miss | 2.1 |
| `TOOLS` | the dispatch table — **the whole capability set, in one literal dict** | 2.2 |
| `_dispatch(action)` | text to a tool call; unknown names come back as observations | 2.2 |
| `SYSTEM` | the protocol the model is asked to speak | 3.1 |
| `_user_turn(text)` | one user-side turn in the verified Interactions shape | 3.1 |
| `_menu_is_complete()` | every dispatchable tool is actually advertised | 3.1 |
| `_model_turn(text)` | the model's own turn — **carries a `TODO(me)`** | 4.1 |
| `_parse(reply)` | reply text to `(action, final)`, or `(None, None)` | 3.2 |
| `run_loop(client, question, *, max_steps=6)` | think → act → observe, bounded | 4.1, 5.1 |
| `_cost_table(spent)` | per-step token usage, so the growth is visible | 5.2 |
| `main()` | dispatch from `sys.argv`; exit non-zero on bad usage | 4.1 |

**`tests/test_loop.py`** — offline by default; the one live test carries `@pytest.mark.live`. See §5.

**`TODO(me)` markers left for you:**

- **4.1** — `_model_turn`. You read the model's turn shape off a real object on Day 2
  ([3.2](../day-02-llm-mechanics/parts/03-context-and-memory/3.2-history-is-a-list-you-own.md));
  reuse what you found. Never invent an API (Principle 8).
- **§5** — the fifth test, described below.
- **6.1** — restore the commented-out append when the failure lab is done. The test in §5 is what
  tells you if you forget.

---

## §5 The eval that must be able to fail

Four tests you can write today for **zero tokens**, because the day's most important logic is pure
functions and a fake client. One live test, marked so `./m check` never depends on a network.

```python
# tests/test_loop.py
import inspect
import types

import pytest

from sutra.loop import _menu_is_complete, _parse, lookup_ticket, run_loop


def test_an_action_is_read_from_any_line() -> None:
    assert _parse("Sure!\n\nTHOUGHT: x\nACTION: lookup_ticket 4521") == ("lookup_ticket 4521", None)


def test_a_final_answer_keeps_its_later_lines() -> None:
    assert _parse("THOUGHT: done\nFINAL: line one\nline two") == (None, "line one\nline two")


def test_a_format_miss_returns_nothing_rather_than_guessing() -> None:
    assert _parse("I'd be happy to help! What would you like me to check?") == (None, None)


def test_every_tool_is_advertised() -> None:
    assert _menu_is_complete()


def test_a_missing_ticket_says_so_readably() -> None:
    result = lookup_ticket("9999")
    assert "9999" in result and "No ticket" in result


class AlwaysActs:
    """A fake client whose every reply asks for the same tool, forever."""

    def __init__(self) -> None:
        self.calls = 0
        self.interactions = self

    def create(self, **kwargs: object) -> object:
        self.calls += 1
        return types.SimpleNamespace(output_text="THOUGHT: again\nACTION: lookup_ticket 4521")


def test_the_step_budget_is_a_hard_ceiling() -> None:
    client = AlwaysActs()
    answer = run_loop(client, "anything at all", max_steps=3)
    assert client.calls == 3
    assert "Stopped after 3 steps" in answer


def test_the_loop_appends_both_halves_of_every_exchange() -> None:
    assert inspect.getsource(run_loop).count("history.append") == 2


# TODO(me): a fifth test, and it is the one that matters most. With a fake client
# that returns an ACTION on call 1 and a FINAL on call 2, assert that the tool's
# result actually appears in the payload sent on call 2. Capture the `input=`
# kwarg inside the fake's `create` and search it. That is the invariant the
# goldfish loop breaks, and the only one that survives us swapping the list for a
# session service on Day 8.
```

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_loop.py -q          # RED: no sutra/loop.py yet
# ... write sutra/loop.py from parts 2.1 -> 5.2 ...
uv run python -m pytest tests/test_loop.py -q          # green
```

Then break each one on purpose and watch it fail — **a test you have never seen fail is a test you do
not know works:**

- Delete `.strip()` from `_parse` and watch the fenced-reply case fail.
- Change `for step in range(1, max_steps + 1):` to `while True:` and watch the budget test **hang**.
  Kill it with `Ctrl-C`, read which line it was sitting on, and put the `for` back.
- Comment out the observation `append` (that is [6.1](parts/06-failure-lab/6.1-the-goldfish-loop.md))
  and watch the appends test go red.
- Add a third key to `TOOLS` without touching `SYSTEM` and watch `test_every_tool_is_advertised` go
  red — the drift bug that is otherwise completely silent.

---

## §6 Request budget

**Free-tier Gemini only.** No other provider is touched today, and no tool makes a network call —
`lookup_ticket` and `search_kb` read Python dicts, so every token below is spent on the loop itself.

| What | Model calls |
| --- | --- |
| the `_model_turn` shape lookup (4.1) | 1 |
| the first real run (4.2) | 3 |
| the tool-call count re-run (4.2) | 3 |
| the trace capture (4.2 check yourself) | 3 |
| the ticket that does not exist (4.3) | ~2 |
| the question with no matching article (4.3) | ~3 |
| the live honesty test (4.3) | ≤4 |
| the cost table run (5.2) | 3 |
| 💥 the goldfish loop (6.1) | 6 |
| 💥 the goldfish loop with the payload print (6.1) | 6 |
| **Total** | **~34** |

**This is roughly double yesterday, and the reason is structural rather than careless:** one question
is no longer one call. Read that as the day's real lesson about cost, and then read
[5.2](parts/05-containment/5.2-the-transcript-is-a-bill.md), which is about the half of it you cannot
see from a call count.

**Two ways to spend less without learning less.** Run the failure lab with `max_steps=3` — the point
is the repetition, and three passes show it as clearly as six. And run the demos one at a time: a
single run is three calls in quick succession, which trips a per-minute ceiling far more easily than
yesterday's single calls did. When it happens you get to watch Day 2's wrapper read the server's own
stated delay and wait it out, which is worth seeing once on purpose.

**Your limits are not in this document.** Free-tier numbers are per project, shown in AI Studio, and
requests-per-day resets at midnight Pacific.

**Cost: $0.** Principle 15 — quota is the currency, denominated in RPM/RPD, not dollars.

---

## §7 Traps

- **`while` instead of `for`.** The stop condition would be owned by the model, which is the component
  most likely to be wrong. The bound is a `range` your code chose, and it goes in today, not after the
  first runaway. (5.1)
- **The forgotten append.** The tool ran, your terminal shows the result, and the model never saw it —
  so it repeats the identical action until the brake stops it. The model is behaving *correctly*;
  every instinct will send you to the prompt instead. (6.1, 1.2)
- **1.x → 2.x trap #4 — don't swallow exceptions.** No `try` around `_dispatch`. Domain outcomes come
  back as readable strings from inside the tool; a defect must raise and reach you. Catching
  `Exception` and returning a friendly sentence launders your bug into the transcript. (2.3)
- **A correct answer that used no tools.** The base model can answer most support questions plausibly
  with no retrieval at all, and that looks identical to success. Count the `ACTION:` lines and check
  for a fact that could only have come from an observation. (4.2)
- **Fabrication on a miss.** An empty tool result is an invitation to invent, and every naive metric
  *improves* when the agent does. The not-found run is the one that tests trust. (4.3)
- **`.split(":")[1]` in the parser.** It silently truncates any argument containing a colon. Slice by
  the marker's length instead. (3.2)
- **A parser that grows to accept near-misses.** Each tolerance rule is a guess about the model's
  future output and widens what your code will execute. Keep the parser strict; put the tolerance in
  the loop's coaching turn. (3.2)
- **`output_text` can be `None` on a *successful* call** — a thinking model can spend the whole output
  budget before writing a visible word. `or ""` on every read. (4.1, Day 2's 5.1)
- **A tool that returns a whole document.** It is re-sent on every remaining step, so one long
  observation sets the price of the rest of the run. Tools summarise; they do not dump. (5.2)
- **`python -m sutra.loop`, never `python sutra/loop.py`.** The second gives
  `ModuleNotFoundError: No module named 'sutra'`. (4.1)
- **`observation` read after the loop.** With `max_steps=0` the body never runs and the name does not
  exist — `UnboundLocalError`. Pre-bind it. (4.1)

---

## §8 Verify before you code

**Today adds no package and uses no symbol that Day 2 did not already verify live.** That is the
honest §8 for this day, and stating it is better than padding the table: `sutra/loop.py` imports
`ask` and `MODEL` from yesterday's module, calls `client.interactions.create` only through that door,
and otherwise uses the standard library. **No ADK symbol is used today** — ADK is not installed until
Day 5, because packages arrive on the day they are first used.

There is exactly one external fact today's code depends on, and it is the one to re-check on the day
you build rather than trust from a page:

| Source | What it settles | When |
| --- | --- | --- |
| `ai.google.dev/gemini-api/docs/text-generation` | the turn shape `{"type": "user_input", "content": [{"type": "text", "text": ...}]}` used by `_user_turn` | verified 2026-08-24 (Day 2) |
| a live interaction object | the **model's** turn shape, for `_model_turn` — the day's `TODO(me)` | **you, today** |
| `ai.google.dev/gemini-api/docs/interactions` | `store=False` and an explicit history is Sutra's house shape (ADR-0006) | verified 2026-08-24 (Day 2) |

Re-read your own object rather than this table:

```bash
uv run python -c "from sutra.config import load_env; load_env(); from google import genai; from sutra.mechanics import ask; print(ask(genai.Client(), 'say hi'))"
```

If what it prints disagrees with anything above, **the object wins** and the correction gets a note in
`docs/PACKAGES.md` — Principle 7 records what was observed, not what was expected.

---

## §9 Say it in an interview

> "The thing that made agents click for me was writing the loop by hand before touching a framework.
> It's about twenty lines: you send the whole transcript, the model replies with text describing one
> action, your code executes it and appends the result, and you go round again until it says it's
> done or your step budget stops it. Two of those three beats are your code — the model never touches
> anything, it only ever asks — and once you've seen that, every security question about agents
> becomes a question about your dispatch table rather than about the model. The two things I got
> wrong were instructive. First, I forgot to append the tool result, and the agent repeated the same
> lookup until the budget stopped it — and the model was completely right to, because at temperature
> zero it was being handed an identical transcript and giving an identical answer. That taught me the
> debugging habit I still use: when an agent ignores a tool result, print the actual payload of the
> next call instead of re-reading the prompt. Second, I bounded the loop by step count and thought I'd
> bounded the cost, but every step re-sends the whole transcript, so cost grows with the square of the
> length — a six-step run isn't six times a one-step run, and one tool returning a long document sets
> the price of every step after it."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 3` refuses to commit while
any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when the loop triages ticket 4521 by actually reading it and the knowledge base;
when it says "I could not find it" about ticket 9999 instead of inventing one; when you have watched
the goldfish loop and restored the line you deleted; and when the four offline tests are green and you
have seen each of them go red.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 3 | <date> | AG-03 | 14 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no rows today.** Nothing was installed. If you have a row to add, something
was installed that this day did not ask for, and that is worth understanding before you commit.

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR. Today makes no decision the plan has not already made; ADR-0006
(Interactions-API-first) is what today's `store=False` explicit history rests on.

**Commit message:**

```text
day 03: the loop, hand-rolled - think, act, observe - closes AG-03
```

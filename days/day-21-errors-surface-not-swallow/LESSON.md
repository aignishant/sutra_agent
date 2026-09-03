---
day: 21
phase: 3
phase_name: "State, context & discipline"
title: "Error handling — surface, don't swallow"
ids: ["ADK-23", "SEC-02"]
principles: [1, 2, 3, 4, 8, 10, 11, 12, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 14
generated: "2026-09-03"
status: written
lab_scaffolded: false
commit: ""
---

# Day 21 — Error handling: surface, don't swallow

> **Yesterday (Day 20):** compaction. The window finally shrank, and you watched a user's instruction
> leave it with no error attached — a system telling you nothing while doing something wrong.
> **Today:** that shape as a subject. When a tool or a model fails, who is told? ADK 2.x routes
> exceptions through four plugin hooks so that policy lives in one place, and this is **trap #4** of
> the four 1.x → 2.x traps. You will also write the swallowed version on purpose and count what it
> costs.
> **Tomorrow (Day 22):** structured logging — a log line is a fact with fields or it is a sentence
> somebody greps, and it hangs off the hooks you wire today.

---

## §1 Where we are

The smoke detector in the hall had been beeping about its battery for a fortnight, so somebody took
the battery out.

Not out of the detector — out of the *beeping*. The plan was to buy a new one at the weekend. The
house now has a smoke detector on the ceiling: correct model, correctly positioned, professionally
installed. Anyone walking past sees a smoke detector. There is no way to tell, from the hall, that it
is a plastic shell.

Nobody in that house decided to live without a smoke alarm. That is the shape of every failure in this
day: not a decision, a convenience, taken once, on an afternoon when something was annoying.

Four things worth knowing before you start.

**Swallowing an error is not handling it — it is deleting it.** A tool that catches its own exception
and returns a dictionary took the error hooks that fired from **three to zero**, turned a failed run
into a successful one, and made the agent tell the user *"Here is what I found about KB-104"* while
the knowledge base was down. Measured.

**ADK offers the exception to four hooks, and only two of them can act.** `on_tool_error_callback` and
`on_model_error_callback` can return a value and stop the failure. `on_agent_error_callback` and
`on_run_error_callback` are notification-only — the exception is always re-raised, and returning a
dict from one of them changed nothing, which this day checks rather than assumes.

**A rescue that is not marked as a rescue is a fabricated result.** The same outage, substituted two
ways, made the agent say *"I could not reach the knowledge base"* or *"KB-104 has no content
recorded"* — and the second is a false statement about the world, produced by a fallback shape that
passes code review.

**And two completely different failures arrive as HTTP 429.** One clears on its own; one does not.
Retrying the second spent **three of Sutra's twenty daily requests** learning nothing.

---

## §2 The map

Fourteen parts in five sections, and **one paper**. The day climbs
`foundation → working → production`: section 1 is the idea, section 2 is ADK's four hooks, section 3
is the policy they carry, section 4 is the deliberate failure lab, and section 5 is where the policy
belongs.

**Read the paper last.** *End-to-end arguments in system design* (`doi:10.1145/357401.357402`) is the
1984 argument for *why* the layer matters, and it only lands once you have moved the policy yourself
in section 5. Principle 4 at the scale of a day.

### Section 1 — `01-who-hears-it`: honesty about failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [Three parties, and the one that must never be nobody](parts/01-who-hears-it/1.1-three-parties.md) | Three shapes, three columns, one that reaches only the model | `foundation` |
| 1.2 | [An error is a fact, not a sentence](parts/01-who-hears-it/1.2-an-error-is-a-fact.md) | 42 chars against 78, and one question prose cannot answer | `working` |
| 1.3 | [Retry, substitute, escalate — and nothing else](parts/01-who-hears-it/1.3-retry-substitute-escalate.md) | Six real failures, and the column everybody forgets | `working` |

### Section 2 — `02-four-hooks`: what ADK does with an exception

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Trap #4 — the runtime owns the error](parts/02-four-hooks/2.1-the-runtime-owns-the-error.md) | Three hooks, one exception, in order | `working` |
| 2.2 | [The two hooks that can rescue](parts/02-four-hooks/2.2-the-two-that-can-rescue.md) | One `return` and the ladder stops at the first rung | `working` |
| 2.3 | [The two hooks that can only witness](parts/02-four-hooks/2.3-the-two-that-can-only-witness.md) | It returned a dict and the run raised anyway | `working` |
| 2.4 | [The ladder — which hooks fire, and in what order](parts/02-four-hooks/2.4-the-ladder.md) | Two entry points, two shared rungs, one ending | `working` |

### Section 3 — `03-policy`: what to do about it

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Which 429 is it?](parts/03-policy/3.1-which-429-is-it.md) | One call against four, and 19 requests left against 16 | `production` |
| 3.2 | [A substitute must say so](parts/03-policy/3.2-a-substitute-must-say-so.md) | `found: False` and `status: unavailable` are different claims | `production` |
| 3.3 | [Giving up honestly](parts/03-policy/3.3-giving-up-honestly.md) | Four internal details leaked in 433 characters | `production` |

### Section 4 — `04-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [💥 The swallowed exception](parts/04-failure-lab/4.1-the-swallowed-exception.md) | Three hooks to zero, and a confident sentence | `production` |
| 4.2 | [💥 The handler that became the error](parts/04-failure-lab/4.2-the-handler-that-became-the-error.md) | The outage replaced by a bug in the code reporting it | `production` |

### Section 5 — `05-in-production`: where the policy lives

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [One policy, not a hundred try/excepts](parts/05-in-production/5.1-one-policy-not-a-hundred.md) | 11 places against 1, and 11 tools that can opt out | `production` |
| 5.2 | [Testing the failure path without quota](parts/05-in-production/5.2-testing-the-failure-path.md) | Eight green, then five red, one saying `assert []` | `production` |

### The paper — read after the parts

| # | Paper | What it answers | Level |
| --- | --- | --- | --- |
| 01 | [End-to-end arguments in system design](papers/01-end-to-end-arguments.md) | `doi:10.1145/357401.357402` — which layer should check? | `production` |

---

## §3 Setup — run this

**No new packages today.** Everything used is already pinned: `google-adk==2.7.1` and
`google-genai==2.19.0` from `docs/PACKAGES.md`. `docs/PAPERS.md` gains one row (§11).

```bash
# 1 - the day folder's lab, and the paper's demo folder
cd days/day-21-errors-surface-not-swallow
mkdir -p lab/papers/end-to-end-arguments
cd lab

# 2 - the twelve lab scripts, in reading order
touch three_shapes.py fact_not_sentence.py three_responses.py
touch who_hears_it.py rescue.py model_error.py
touch retry_made_it_worse.py fallback_that_lied.py give_up_honestly.py
touch handler_that_broke.py where_policy_lives.py test_errors_demo.py

# 3 - the paper's two-file demo
touch papers/end-to-end-arguments/link.py papers/end-to-end-arguments/transfer.py
cd -

# 4 - what changes under sutra/ and tests/ today
ls sutra/                    # errors.py is new; plugins.py gains the four hooks
ls tests/                    # test_errors.py is the eval
```

The paper's demo runs from inside its own folder because `transfer.py` imports `link` by bare name.
The scripts are listed in reading order, which is the order the parts introduce them. Every line of
every file is typed by you, from the parts.

**Run `who_hears_it.py` first**, both arms. It is the day in one file: `SWALLOW=1` looks fine and
`SWALLOW=0` looks broken, and the second one is the correct system.

**Nothing today needs a key.** Every failure in this day is fakeable — a tool that raises is a
one-line function and a model that 429s is a nine-line class — so the whole day, including the
paper's demo and the test suite, runs offline. That is unusual and it is the point of
[5.2](parts/05-in-production/5.2-testing-the-failure-path.md).

**`sutra/errors.py` is new** and holds the error *fact* — the shape from
[1.2](parts/01-who-hears-it/1.2-an-error-is-a-fact.md) plus the classifier. **`sutra/plugins.py` is
extended, not replaced**: Day 14's plugin gains the four error hooks beside whatever it already does.

---

## §4 Build brief

**`sutra/errors.py`** — new:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `Failure` | the error fact: `kind`, `target`, `retryable`, `user_visible`, `detail` | 1.2 |
| `classify(error)` | an exception in, a `Failure` out | 1.2, 3.1 |
| `is_retryable(failure)` | the per-minute / per-day distinction, keyed on the quota metric | 3.1 |
| `substitute(failure, tool_name)` | the marked fallback dict — always carries `status` | 3.2 |
| `public_message(failure)` | the fixed caller-facing sentence, looked up not formatted | 3.3 |
| `LEAKS` | the strings that must never appear in a public message | 3.3, 5.2 |

**`sutra/plugins.py`** — extended with the four hooks from section 2. The first statement of
`on_tool_error_callback` is the structured record, before any policy runs — that ordering is
[4.2](parts/04-failure-lab/4.2-the-handler-that-became-the-error.md)'s whole lesson.

**`tests/test_errors.py`** — new. Eight cases, no key; see §5.

**Every tool under `sutra/` loses its `try`/`except`.** That is the actual deliverable of the day, and
`git diff` is how you check it.

**`TODO(me)` markers left for you:**

- **1.2** — write `Failure` as a `dataclass` rather than the teaching dict, and decide whether
  `retryable` should have a default. Write one sentence saying why the default you chose is the safe
  one.
- **1.3, 3.1** — run `three_responses.py` and `retry_made_it_worse.py`, then set Sutra's own
  `MAX_ATTEMPTS` from the daily budget rather than from taste. Show the arithmetic.
- **3.1** — the `per_minute` half of the classifier has **not** been confirmed against a live
  per-minute refusal; only the daily one has. Trigger one early in a day, capture the body, and pin
  the real metric name with a test.
- **3.3** — add a fifth entry to `LEAKS` for something a *tool* exception might carry — an email
  address — then write the tool exception that would leak it, and make the test catch it.
- **4.1** — grep `sutra/` for `except Exception` and list every hit. For each, decide: delete it, or
  narrow it and re-raise. Record which and why.
- **5.1** — pick one tool that should **never** be substituted (a write, not a read) and add the
  per-tool rule to the plugin, keyed on `tool.name`.
- **5.2** — break the suite three ways: swallow in a tool, build the `Runner` with `agent=` instead of
  `app=`, and remove the marker from the substitute. Record which tests catch which.
- **The paper** — set `CORRUPT_AT = None` and run both arms, then say which half of the paper's claim
  that demonstrates.

---

## §5 The eval that must be able to fail

Five tests, **eight cases** (one is parametrised over three error bodies), no key and no network. All
are shown with their walkthrough in
[5.2](parts/05-in-production/5.2-testing-the-failure-path.md).

They assert four kinds of thing, and the fourth is the unusual one: that the exception arrives
unchanged; that the ladder is `["tool", "agent", "run"]` **in order**; that a rescue stops it; and
that ADK's documented *limits* hold — the agent hook cannot suppress even when it returns a dict, and
the substitute carries its marker.

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_errors.py -q -m "not live"   # RED: no sutra/errors.py yet
# ... write the symbols from §4 ...
uv run python -m pytest tests/test_errors.py -q -m "not live"   # green
```

Then break it on purpose. Measured on 2026-09-03, by putting trap #4 back into the tool — changing
`raise TimeoutError(BOOM)` to `return {"error": f"Error: {BOOM}"}`:

| Break this | Which tests go red | What it is telling you |
| --- | --- | --- |
| a tool swallows its own exception | five of eight | the ladder never starts (4.1) |
| `Runner(agent=...)` instead of `app=` | the same five | the plugin was never installed (5.1) |
| the substitute loses its `status` key | the two substitute tests | a rescue stopped being marked (3.2) |

**And the finding that came out of writing that table:** the red message for the first test was a bare
`assert False`, which says nothing about what was expected. It came from an `isinstance` check with no
assertion message. That is **three consecutive days** on which deliberately failing a green suite has
exposed a weak assertion — Day 19 found two, Day 20 found a `StopIteration`, and this is the third.
**Running the suite red is how you review the suite.**

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`docs/PACKAGES.md`, re-confirmed from a
live 429 on 2026-09-03).

| What | Generations |
| --- | --- |
| eleven lab scripts across sections 1–5 | **0** |
| the test suite, eight cases | **0** |
| the paper's demo, both arms | **0** |
| **Total required** | **0 of 20** |

**Zero.** Today is the cheapest day in the phase and the reason is worth stating: **failure is the
easiest behaviour in the world to fake.** A tool that raises is one line. A model that returns 429 is
nine. A corrupted buffer is one XOR. Every claim in this day is about *what the system does when
something breaks*, and nothing about that requires a real model to break.

That is not a happy accident of the subject — it is a property of the design. Both seams that could
have needed a network, the tool and the model, are injectable, which is
[5.2](parts/05-in-production/5.2-testing-the-failure-path.md)'s argument for why these tests belong in
the default suite rather than behind a `live` marker.

The one thing that **did** cost quota was captured yesterday and reused: the real 429 body in
[3.1](parts/03-policy/3.1-which-429-is-it.md) and [3.3](parts/03-policy/3.3-giving-up-honestly.md) is
from a live refusal on 2026-09-03. Capturing an error body once and keeping it as a fixture is the
right way to spend a request.

**Cost: $0.**

---

## §7 Traps

- **Trap #4, named** (master plan §5.1): *don't swallow exceptions.* The 1.x habit is a tool catching
  its own error and returning a string. In 2.x the exception is what routes the failure to policy, so
  catching it locally removes the retry, the substitution, the log and the trace — measured as three
  hooks going to zero (4.1).
- **`Runner(agent=...)` installs no plugins.** The `Runner` takes exactly one of `app`, `agent` or
  `node`, and passing `agent` builds a fresh `App` with no plugins and no compaction config. Nothing
  warns. One word disables every error policy in the system (2.1, 5.1).
- **`BasePlugin` needs a name.** `Policy()` raises
  `TypeError: BasePlugin.__init__() missing 1 required positional argument: 'name'` at construction.
  Loud, early, fine — but the examples in circulation show a bare `Policy()`.
- **The hooks are keyword-only and the parameter *names* are the contract.** Renaming `tool_args` to
  `args` — a tidy-up that passes review — gives
  `TypeError: ... got an unexpected keyword argument 'tool_args'`, at the moment something else has
  already gone wrong. Copy the signatures from `base_plugin.py`.
- **Two of the four hooks cannot rescue.** `on_agent_error_callback` and `on_run_error_callback` are
  notification-only; returning a dict from one changes nothing. Building a friendly message there and
  wondering why the user never sees it is an expensive afternoon (2.3).
- **A rescue ends the ladder.** Rescue at the tool hook and the agent and run hooks never fire — so
  your run-level error rate is near zero *during an outage*. Anything you rescue you must also count
  (2.4).
- **A plugin that raises replaces the error it was reporting.** ADK wraps it as
  `RuntimeError: Error in plugin 'policy' during 'after_tool_callback' callback: ...` and the original
  `TimeoutError` is not named anywhere in what escapes. Log first, then do policy (4.2).
- **Two different 429s.** Per-minute clears; per-day does not, and its body still says
  *"Please retry in 57.99s"*. Retrying the daily one cost three of twenty requests (3.1).
- **`str(error)` is not a user-facing message.** The real 429 body leaks the model name, the provider
  endpoint, the numeric limit and the word *billing* (3.3).

---

## §8 Verify before you code

Fetched on **2026-09-03**, the day this was written:

- `https://adk.dev/plugins/` — the two error callbacks that can return a value, their exact
  signatures, and the documented meaning of returning a value versus `None`.
- The installed `google-adk` 2.7.1 source, `google/adk/plugins/base_plugin.py` — which is where the
  **other two** hooks came from. adk.dev documents `on_model_error_callback` and
  `on_tool_error_callback`; the package also defines `on_agent_error_callback` and
  `on_run_error_callback`, both annotated `-> None` with a docstring stating *"This is a
  notification-only callback. The exception is always re-raised."* Two hooks the page does not
  mention is exactly why Principle 8 says read the source you have installed as well as the page.
- `google/adk/runners.py` — where the run-level hook is invoked, and the `finally` block that runs it.
- `https://api.crossref.org/works/10.1145/357401.357402` — the paper's exact title, journal, volume,
  pages and year, taken from the machine-readable record rather than from memory (§17.4.1 rule 5).
  `dl.acm.org` returns HTTP 403 to automated fetches, so Crossref is the citable source that could
  actually be checked.
- The paper's own text, from the copy hosted at `web.mit.edu/saltzer/www/publications/endtoend/`, for
  the five enumerated threats and the *Performance aspects* limits quoted in the paper part.

---

## §9 Say it in an interview

"We had an agent that told a customer their ticket had no notes attached, and it had four. The model
had not hallucinated — the notes lookup had timed out, the tool caught its own exception and returned
a dict with an `error` key, and the model summarised what looked like an empty result. There was no
traceback to find, because nothing had raised, and no log line, because nothing had been told.

That is the fourth ADK 1.x-to-2.x trap, and fixing it is mostly deleting code. In 2.x a raised
exception is offered to plugin hooks at the tool, agent and run levels before it escapes, so retry,
substitution and logging live in one plugin instead of in eleven tools. We measured it: raising fired
three hooks and failed the run; catching it fired zero error hooks and reported success.

Two things I would tell anyone doing it. A substitute has to say it is a substitute — we had a
fallback that kept the tool's normal shape with empty values, and `found: False` is a claim that we
looked, when the truth was that we could not look. And retry is a decision about *which* error: a
per-minute 429 clears on its own, a daily one does not, and both say 'please retry in 58 seconds'.
Retrying the daily one was costing us three of twenty daily requests every time.

The whole failure path is testable offline, which is the part I did not expect. A tool that always
raises and a model that always 429s are the two easiest objects in the system to write, so the suite
runs on every commit with no key — and when I put the `try`/`except` back on purpose, five of eight
tests went red and one of them said `assert [] == ['tool', 'agent', 'run']`. That empty list is the
only signal that catches a swallowed exception."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 21` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it
to someone else without the page open.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 21 | <date> | ADK-23, SEC-02 | 14 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — no new rows. Nothing was installed today.

**`docs/PAPERS.md`** — append:

```text
| End-to-end arguments in system design | doi:10.1145/357401.357402 | 1984 | 2026-09-03 | 21 | `days/day-21-errors-surface-not-swallow/papers/01-end-to-end-arguments.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skills were sourced today.

**The commit:**

```text
day 21: error handling - surface, don't swallow - closes ADK-23, SEC-02
```

# Day 14 — CHECKLIST

**IDs closed:** ADK-16
**Principles served:** 1, 2, 4, 6, 8, 9, 10, 11, 13, 15, 16, 17, 18
**Parts:** 19 across 7 sections, plus 1 paper

> `./m done 14` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
cd days/day-14-plugins-one-layer-up/lab
uv run python doors.py
uv run python two_layers.py
uv run python blast_radius.py
cd papers/aspect-oriented-programming
WEAVE=1 uv run python desk.py
WEAVE=0 uv run python desk.py
cd -
uv run python -m pytest tests/test_plugins.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: fourteen hooks where the page says twelve, and both set differences empty; the same two
returns giving opposite answers one layer apart; a run where the FAQ agent is refused by a rule
written for the desk; then `audit records: 3` and `audit records: 0` from byte-identical business
lines; then five passed and one skipped; then `OK all green`, then
`traceability: 26/199 closed, 0 problem(s)`, then one commit reading
`day 14: plugins - one layer up - closes ADK-16`.

---

## Before you write anything

- [ ] `./m check` is green and `scripts/trace.py` shows Day 13's count before you change anything
- [ ] Copied `scripted.py` from Day 13's lab into today's, and can say why it is copied rather than
      imported across day folders
- [ ] Wrote `lab/stateless.py` **before** section 2.3, and can say why a counting test double had to
      be replaced for sections 4 and 5 (2.2)
- [ ] Can say why all seventeen of today's lab scripts cost nothing, without using the word "mock"
- [ ] Ran every lab script from **inside** `lab/`, and know why the bare imports need that

## Section 1 — where a plugin lives

- [ ] Ran `lab/hello_plugin.py` and saw the plugin fire for an agent that does not mention it (1.1)
- [ ] Can say in one sentence what a plugin is for, in terms of the agent nobody has written yet (1.1)
- [ ] Removed `async` from a hook and confirmed what fails is not your plugin (1.1)
- [ ] Ran `lab/where_it_lives.py` and saw all three installation cases (1.2)
- [ ] Confirmed case **c** — `InMemoryRunner` — produces **no error** and installs nothing (1.2)
- [ ] Read the error from passing both `app` and `plugins`, and can say which one wins (1.2)
- [ ] Can say why `Runner(app=...)` still needs a session service (1.2)
- [ ] Ran `lab/names.py` and confirmed the duplicate raises at the **`Runner`**, not the `App` (1.3)
- [ ] Looked a plugin up with a deliberate typo and got `None` rather than an error (1.3)

## ADK-16 — the fourteen doors (section 2)

- [ ] Ran `lab/doors.py` and recorded how many hooks **your** package defines (2.1)
- [ ] Confirmed `Defined but never dispatched` and `Dispatched but not defined` are both empty (2.1)
- [ ] Can name the two hooks the published page omits (2.1)
- [ ] Misspelled a hook name on purpose and confirmed nothing at all happened (2.1)
- [ ] Ran `lab/run_level.py` and saw the four run-level doors bracket the whole request (2.2)
- [ ] Can say why no agent could implement `on_user_message_callback` (2.2)
- [ ] Returned a bare string from `on_user_message_callback` and read where it actually failed (2.2)
- [ ] Ran `lab/moved_names.py` and read **which** parameter name the `TypeError` names (2.3)
- [ ] Can recite the parameter names for `before_tool_callback` and `after_tool_callback` at **both**
      layers, and say which is which (2.3)
- [ ] Ran `lab/firing_order.py` and counted fifteen firings across ten hooks (2.4)
- [ ] Can say how many model calls one tool round trip costs, and why (2.4)
- [ ] Can name the hook that fires most often, and what that means for anything expensive (2.4)

## Section 3 — the rule at this layer

- [ ] Ran `lab/two_layers.py` and saw the same pair of returns give opposite answers (3.1)
- [ ] Can state the plugin rule and the agent tool-door rule, and where exactly they diverge (3.1)
- [ ] Confirmed that a plugin returning a value means the agent's callback never ran (3.1)
- [ ] Ran `lab/error_hooks.py` and saw two hooks fix things and two only watch (3.2)
- [ ] Confirmed a notification hook's return value changes nothing and the original error re-raises
      (3.2)
- [ ] Raised inside a notification hook and confirmed your own error was swallowed (3.2)
- [ ] Can say why a tool that catches its own exception never reaches `on_tool_error_callback` (3.2)
- [ ] Ran `lab/plugin_raises.py` and read the `RuntimeError` naming the plugin and the hook (3.3)
- [ ] Can say what a plugin's error handling is, whether or not you wrote it that way (3.3)

## Section 4 — the meter

- [ ] Ran `lab/metering.py` and saw two tools cost **three** model calls (4.1)
- [ ] Can say why the counters go on the `before` doors and not the `after` doors (4.1)
- [ ] Moved a counter to `after_model_callback` and can say what streaming would do to it (4.1)
- [ ] Ran `lab/exit_door.py` and confirmed the report arrives **after** the caller has the answer (4.2)
- [ ] Returned a value from `after_run_callback` and confirmed nothing changed (4.2)
- [ ] Ran `lab/shared_state.py` and saw `2, 4, 6` in sequence (4.3)
- [ ] Recorded whether the concurrent case gives you `6, 6, 6` on **your** machine (4.3, `TODO(me)`)
- [ ] Can say what `invocation_id` is for and why per-run state is keyed on it (4.3)
- [ ] Replaced `pop` with a plain read and watched the leak appear (4.3)

## Section 5 — where the layer bites

- [ ] Ran `lab/halt.py` and confirmed the documented halt is **discarded** on an `LlmAgent` root (5.1)
- [ ] Can say why a test of this hook might pass while production is wrong (5.1)
- [ ] Decided what Sutra does about the hook, and wrote the reason down (5.1, `TODO(me)`)
- [ ] Ran `lab/never_prints.py` and confirmed the happy-path meter prints nothing for the failed run
      (5.2)
- [ ] Saw the leak count climb on the meter that reports at one exit only (5.2)
- [ ] Confirmed reporting at both exits does **not** double-count, and can say why (5.2)

## 💥 Failure lab (section 6)

- [ ] Ran `lab/blast_radius.py` and confirmed the FAQ agent was refused by a rule written for the desk
- [ ] Confirmed there is **no error text anywhere** in that output
- [ ] Can say what the bug report will say, and why nobody looks at the plugin first
- [ ] Confirmed the FAQ agent's own tests would still pass, and can say why
- [ ] Added `blocked_by` to the refusal and can say what it is worth at thirty agents
- [ ] Decided which layer each of Sutra's two credential rules belongs to, and wrote both down
      (6.1 step 3, `TODO(me)`)

## Section 7 — in production

- [ ] Ran `lab/shipped.py` and read the `overrides` column on all nine (7.1)
- [ ] Can say what seven of the nine have in common, and what the two loggers are for (7.1)
- [ ] Read `ReflectAndRetryToolPlugin` and `ContextFilterPlugin` in the installed package, and wrote
      one sentence each on what they would do to your ledger (7.1, `TODO(me)`)
- [ ] Can say why one shipped plugin is not importable here, and why that is reported rather than
      fatal (7.1)
- [ ] Wrote `tests/test_plugins.py` and watched it go **RED** before writing `sutra/plugins.py`
- [ ] Test 1 green: the plugin is actually installed, by identity
- [ ] Test 2 green: a one-tool run costs two model calls and one tool call
- [ ] Test 3 green: a failed run is still billed, with its outcome
- [ ] Test 4 green: no run state is left behind, after one success **and** one failure
- [ ] Test 5 green: three runs on one `App` are billed separately
- [ ] **Broke it on purpose:** deleted `on_run_error_callback`, watched two tests go red, fixed it
- [ ] **Broke it on purpose:** used `.get` instead of `.pop`, watched the leak test go red, fixed it
- [ ] **Broke it on purpose:** renamed `tool_args` to `args`, watched **four of five** go red, fixed it
- [ ] **Broke it on purpose:** swapped in `InMemoryRunner`, watched the install test go red, fixed it
- [ ] Left the sixth test skipped with its `TODO(me)`, and can say what a green suite without it would
      be claiming (7.2)
- [ ] Can say why a plugin cannot be tested by calling its hooks the way a callback can (7.2)
- [ ] Can give the one question that decides plugin versus callback, in one sentence (7.3)
- [ ] Wrote the `Layer:` docstring on both `RunLedger` and `block_forbidden_queries` (7.3, `TODO(me)`)

## The paper — read after the parts

- [ ] Read [`papers/01-aspect-oriented-programming.md`](papers/01-aspect-oriented-programming.md)
      **after** finishing section 7, and can say why that order is Principle 4
- [ ] Built the two-file demo and ran it with `WEAVE=1` and `WEAVE=0`
- [ ] Confirmed the three business lines are **byte-identical** in both runs
- [ ] Can say what the ablation switch proves that a single run does not
- [ ] Can define *cross-cutting concern*, *advice*, *join point* and *obliviousness* in plain words
- [ ] Can name which half of the paper survived into shipped systems and which half the field dropped
- [ ] Can connect obliviousness to 6.1's failure in one sentence

## The build

- [ ] `sutra/plugins.py` exists **at the package root**, and you can defend that path in one sentence
- [ ] `RunLedger` counts at `before_model_callback` and `before_tool_callback`, and nowhere else
- [ ] It closes at **both** `after_run_callback` and `on_run_error_callback`
- [ ] `runs` is empty after a successful run **and** after a failed one — asserted, not assumed
- [ ] `NAME` is a class attribute, and the test looks the plugin up by it
- [ ] The ledger is installed on an `App`, and you confirmed by running that `InMemoryRunner` does not
      install it
- [ ] `tests/scripted.py` exists and `tests/test_plugins.py` imports from it, not from a day folder
- [ ] `sutra/desk/callbacks.py` changed by **one docstring only** — confirmed with `git diff`
- [ ] `sutra/desk/agent.py`, `sutra/desk/tools.py` and `sutra/desk/schemas.py` are **unchanged**

## Budget & gate

- [ ] Total model calls today: **0 of 20** — and you can say why the day needed none
- [ ] If you spent the optional request, you recorded whether the live bill and the ledger agreed
- [ ] `uv run ruff check .` clean
- [ ] `uv run ruff format --check .` clean
- [ ] `uv run python -m pytest -q -m "not live"` green
- [ ] `./m depth 14` green
- [ ] `./m check` prints `OK all green`

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended with the **date and hash you actually observed**:
      `| 14 | <date> | ADK-16 | 19 (+1 paper) | <hash> | ✅ |`
- [ ] `docs/PACKAGES.md` — no new rows, **unless** your hook count or your concurrency numbers
      disagree with the day, in which case you added the row
- [ ] `docs/PAPERS.md` — the `doi:10.1007/BFb0053381` row is present, and the title in it was copied
      from the record rather than typed from memory
- [ ] `docs/SKILL_PROVENANCE.md` — no new rows
- [ ] `git status` shows no `.env`
- [ ] Committed: `day 14: plugins - one layer up - closes ADK-16`
- [ ] `uv run python scripts/trace.py` shows ADK-16 closed and `0 problem(s)`

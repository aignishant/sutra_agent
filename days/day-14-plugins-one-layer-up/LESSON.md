---
day: 14
phase: 2
phase_name: "Models & tools"
title: "Plugins — one layer up"
ids: ["ADK-16"]
principles: [1, 2, 4, 6, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-08-30"
status: written
lab_scaffolded: false
commit: ""
---

# Day 14 — Plugins: one layer up

> **Yesterday (Day 13):** six doors on one agent, and one rule — return `None` and the thing behind the
> door happens. The last section showed that your callback is not the outermost layer: something runs
> before it and can skip it entirely.
> **Today:** that something. A plugin is the same kind of function attached to the **application**
> instead of to one agent, so it covers every agent in it — including the ones nobody has written yet.
> There are fourteen doors at this layer, not six; the parameter names are different; the rule is the
> documented one for once; and the coverage that makes plugins worth having is also the thing that
> lets one line break an agent you were not thinking about.
> **Tomorrow (Day 15):** toolsets and OpenAPI wrappers — tools that arrive in bulk from somewhere
> else, which is the first time today's "every agent, including the ones you have not written" starts
> meaning "every tool, including the ones you did not write".

---

## §1 Where we are

A landlord who fixes the wiring instead of writing thirty notices.

A building has thirty flats. The landlord wants every flat to have a working smoke alarm. There are
two ways to get there. She can write to each tenant — *please buy an alarm, please test it monthly* —
and then the building is as safe as the least diligent tenant, and every new tenant who moves in next
year is a fresh chance for it not to happen. Or she can wire alarms into the building itself, once,
and then a flat is covered because it is a flat, not because somebody remembered.

The second way is better and it is not free. The alarms are now hers: if she wires them wrong, all
thirty are wrong at the same time. And a tenant who runs a small catering kitchen from their flat now
has an alarm going off every evening, because of a rule that was written with ordinary cooking in
mind.

That trade is the whole day. Day 13's callbacks are the notices — correct, per-agent, and dependent on
somebody remembering. A **plugin** is the wiring: one object, attached to the application, running for
every agent it contains, including the ones added next quarter by somebody who has never read your
rule. Section 1 is where it attaches, section 2 is the doors it gets, sections 3 and 4 are what it can
do with them, and sections 5 to 7 are what it costs you.

Four things worth knowing before you start.

**The documentation is behind the package.** `adk.dev/plugins/` lists twelve hooks. The installed
`google-adk` 2.7.1 defines and dispatches **fourteen**. Part 2.1 does not tell you which is right; it
prints the list from the package on your machine, from two independent places in the source, and
compares them.

**The rule changed on the way up.** Yesterday's tool-door chain breaks on a *truthy* value and then
tests `is None`, so an empty dictionary falls between the two and silently skips the tool. The plugin
manager checks `is not None` and means it. The same sentence in the documentation, two different
behaviours, one layer apart — and section 3 measures both in one script rather than asking you to
remember which is which.

**Today costs nothing, again.** Every lab script runs against a local `BaseLlm` subclass that decides
what to say by reading the request. Real runners, real plugins, real events, zero requests, no key.
Section 2 explains why Day 13's counter-based double had to be replaced to get here.

**And the failure lab is the day's own argument turned against it.** Section 6 takes a guard that was
completely correct on the triage desk, promotes it to a plugin exactly as this day recommends, and
watches it disable the one agent whose entire job was the thing being blocked. No error. Nobody
notices for a fortnight.

---

## §2 The map

Nineteen parts in seven sections, and **one paper**. The day climbs `foundation → working →
production`: section 1 is where a plugin lives, section 2 is what doors it gets and when they fire,
section 3 is the rule at this layer, section 4 builds the thing Sutra keeps, sections 5 and 6 are where
the layer bites, and section 7 is production.

**Read the paper last.** Cross-cutting concerns were named and argued about thirty years before ADK
existed, and *Aspect-oriented programming* (`doi:10.1007/BFb0053381`) is where the vocabulary comes
from — including the word for the exact failure section 6 walks into. Principle 4 at the scale of a
day: build the mechanism first, then read the proposal, so there is something for it to land on.

### Section 1 — `01-where-a-plugin-lives`: attaching it, and the one way that silently fails

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The rule nobody has to remember](parts/01-where-a-plugin-lives/1.1-the-rule-nobody-has-to-remember.md) | The smallest complete plugin, and what "every agent" is actually worth | `foundation` |
| 1.2 | [The `App` is what plugins belong to](parts/01-where-a-plugin-lives/1.2-the-app-is-what-plugins-belong-to.md) | Three ways to install one, and the one that installs nothing without an error | `working` |
| 1.3 | [A name, and only one of it](parts/01-where-a-plugin-lives/1.3-a-name-and-only-one-of-it.md) | The duplicate check fires at `Runner`, one line after you expect | `working` |

### Section 2 — `02-the-fourteen-doors`: what this layer gets that an agent does not

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Fourteen doors, and six you already know](parts/02-the-fourteen-doors/2.1-fourteen-doors-six-you-already-know.md) | The package says fourteen, the page says twelve, and you print both | `working` |
| 2.2 | [The four doors an agent cannot have](parts/02-the-fourteen-doors/2.2-the-four-doors-an-agent-cannot-have.md) | The run-level hooks, and the second test double the rest of the day needs | `working` |
| 2.3 | [The names moved](parts/02-the-fourteen-doors/2.3-the-names-moved.md) | `args` became `tool_args`, so a working callback copied up raises | `working` |
| 2.4 | [Fifteen firings, one run](parts/02-the-fourteen-doors/2.4-fifteen-firings-one-run.md) | Ten hooks, fifteen firings, and the order is not the listed order | `working` |

### Section 3 — `03-the-rule-at-this-layer`: the return value, and what raising costs

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [`is not None`, and this time it means it](parts/03-the-rule-at-this-layer/3.1-is-not-none-and-this-time-it-means-it.md) | The same two returns at both layers, in one script, giving opposite answers | `production` |
| 3.2 | [The two hooks that cannot stop anything](parts/03-the-rule-at-this-layer/3.2-the-two-hooks-that-cannot-stop-anything.md) | Notification-only: every plugin told, every return value discarded | `production` |
| 3.3 | [A plugin that raises takes the run with it](parts/03-the-rule-at-this-layer/3.3-a-plugin-that-raises-takes-the-run-with-it.md) | One bad line, every agent down, and a `RuntimeError` that names you | `production` |

### Section 4 — `04-the-meter`: the plugin Sutra actually keeps

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Counting what a run costs](parts/04-the-meter/4.1-counting-what-a-run-costs.md) | The only two doors where quota is spent, and why two tools cost three calls | `working` |
| 4.2 | [The bill at the exit door](parts/04-the-meter/4.2-the-bill-at-the-exit-door.md) | The one hook that knows the request is over, and cannot change it | `working` |
| 4.3 | [One instance, every run](parts/04-the-meter/4.3-one-instance-every-run.md) | `2, 4, 6` in sequence and `6, 6, 6` at once, from the same counter | `production` |

### Section 5 — `05-where-the-layer-bites`: two documented things that are not true

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The door documented to stop the run](parts/05-where-the-layer-bites/5.1-the-door-documented-to-stop-the-run.md) | The halt that is discarded on every agent type Sutra has | `production` |
| 5.2 | [The bill that never prints](parts/05-where-the-layer-bites/5.2-the-bill-that-never-prints.md) | Failed runs spend quota, report nothing, and leak an entry each | `production` |

### Section 6 — `06-failure-lab`: the deliberate failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The rule that broke an agent nobody was looking at](parts/06-failure-lab/6.1-the-rule-that-broke-an-agent-nobody-was-looking-at.md) | Today's own advice, followed exactly, wrecking a correct agent | `production` |

### Section 7 — `07-in-production`: what is already written, testing yours, and where it belongs

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [The plugins ADK already ships](parts/07-in-production/7.1-the-plugins-adk-already-ships.md) | Nine installed plugins, and the framework's own source agreeing with this day | `production` |
| 7.2 | [Testing a plugin without a model](parts/07-in-production/7.2-testing-a-plugin-without-a-model.md) | Why you cannot call the hooks directly, and the five assertions that work | `production` |
| 7.3 | [Which layer does this rule belong to](parts/07-in-production/7.3-which-layer-does-this-rule-belong-to.md) | One question, and the docstring that stops it being re-answered wrongly | `production` |

### The paper — read it after the parts

| # | Paper | What it settles | Level |
| --- | --- | --- | --- |
| 01 | [Aspect-oriented programming](papers/01-aspect-oriented-programming.md) · `doi:10.1007/BFb0053381` | Where "cross-cutting concern" comes from, and the name for section 6's failure | `production` |

---

## §3 Setup — run this

**No new packages today.** `google-adk` 2.7.1 carries the whole day, and the scripted model means
nothing is installed and nothing goes over the network.

```bash
# 1 - confirm where you are starting from
./m check

# 2 - the lab scratchpad for today
mkdir -p days/day-14-plugins-one-layer-up/lab/papers/aspect-oriented-programming
cd days/day-14-plugins-one-layer-up/lab

# yesterday's test double, which today's builds on - copy it, do not import across days
cp ../../day-13-callbacks-four-doors/lab/scripted.py .

# section 1
touch hello_plugin.py where_it_lives.py names.py
# section 2 - stateless.py FIRST, from part 2.2; everything after it imports it
touch doors.py stateless.py run_level.py moved_names.py firing_order.py
# section 3
touch two_layers.py error_hooks.py plugin_raises.py
# section 4
touch metering.py exit_door.py shared_state.py
# section 5
touch halt.py never_prints.py
# section 6
touch blast_radius.py
# section 7
touch shipped.py
# the paper's demo - no ADK, no model, two files
touch papers/aspect-oriented-programming/concern.py
touch papers/aspect-oriented-programming/desk.py
cd -

# 3 - what changes under sutra/ today
ls sutra/                      # plugins.py is new, at the package root and not under desk/
cat sutra/desk/callbacks.py    # gains one docstring line, and nothing else
```

**Every lab script is run from inside `lab/`**, because they import `scripted` and `stateless` by bare
name and that only resolves when `lab/` is the working directory:

```bash
cd days/day-14-plugins-one-layer-up/lab && uv run python doors.py
```

**Write `stateless.py` before anything past section 1.** It is given complete in
[part 2.2](parts/02-the-fourteen-doors/2.2-the-four-doors-an-agent-cannot-have.md), and every script
from 2.3 onward imports it. Day 13's `ScriptedModel` counts how far through a list it is, which is
correct for one run and wrong for sections 4 and 5, where the same agent runs three times and
sometimes concurrently — a shared counter scrambles the script. `ReactiveModel` decides from the
request instead, so it has no position to scramble.

**Then run `doors.py` early**, before you have built anything on an assumption about what this layer
offers. It prints fourteen where the page says twelve, and the whole of section 2 is downstream of
that number.

**`sutra/plugins.py` is new and it lives at the package root**, not under `sutra/desk/`. That placement
is the day's argument written as a file path: `desk/` is one agent, and a plugin is not one agent's.
Nothing under `sutra/desk/` changes today except one docstring, written in
[7.3](parts/07-in-production/7.3-which-layer-does-this-rule-belong-to.md).

---

## §4 Build brief

**`sutra/plugins.py`** — new, at the package root, and the day's centrepiece:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `RunLedger` | the plugin: counts what one request spends, reports once, cleans up | 4.1, 4.2, 4.3, 5.2 |
| `RunLedger.NAME` | the registered name, as a class attribute, so tests look it up rather than retype it | 1.3, 7.2 |
| `RunLedger.runs` | `dict[str, Counter[str]]` keyed by `invocation_id` — the open runs, and it must empty | 4.3, 5.2 |
| `RunLedger.closed` | the finished bills: one `(invocation_id, outcome, Counter)` per run | 4.2, 7.2 |
| `before_model_callback` | `+1` on `model:{llm_request.model}` — one of the two doors that spend | 4.1 |
| `before_tool_callback` | `+1` on `tool:{tool.name}` — the other one | 4.1 |
| `after_run_callback` | pops the run and closes it `"ok"` | 4.2 |
| `on_run_error_callback` | pops the run and closes it `"error:<ExceptionType>"` — the half everyone forgets | 5.2 |

Two things in that table are the whole design. The counters sit on the **`before`** doors, because
those are where quota is actually committed and an `after` door counts yields rather than calls. And
the ledger closes at **two** exits rather than one, because `after_run_callback` never fires on a
failed run, and a failed run has still spent everything it spent.

**`sutra/desk/callbacks.py`** — one docstring, no behaviour change. `block_forbidden_queries` gains a
`Layer:` line recording that it is deliberately **not** a plugin, and why. The wording is in
[7.3](parts/07-in-production/7.3-which-layer-does-this-rule-belong-to.md); the reason it is a
deliverable rather than a nicety is
[6.1](parts/06-failure-lab/6.1-the-rule-that-broke-an-agent-nobody-was-looking-at.md).

**`tests/scripted.py`** — new. Day 13 left a `TODO(me)` asking where the shared test double should live
once a second day needed it. This is that day: `ReactiveModel` moves out of `lab/stateless.py` into
`tests/`, because `tests/test_plugins.py` must not import from a day folder.

**`days/day-14-plugins-one-layer-up/lab/`** — seventeen scripts, plus the paper's two-file demo. **All
of them cost zero requests.**

**`tests/test_plugins.py`** — see §5.

**`TODO(me)` markers left for you:**

- **6.1, step 3** — Sutra has two rules in play: *never send credential values to a model provider*,
  and *this triage desk must not search for credentials*. Decide which layer each belongs to and write
  the answer down. They do not get the same answer, and the day is not finished until you can say why.
- **7.3** — the same question asked about Day 13's two callbacks. Which of `audit_tool_calls` and
  `block_forbidden_queries` belongs in a plugin? You wrote a prediction at the end of Day 13; compare
  it with what you think now, and record the docstring you would put next to each.
- **7.2** — the sixth test is skipped on purpose. Every number in that suite came from the plugin being
  tested, and nothing has compared the ledger with what a provider actually recorded. Write down the
  trigger that un-skips it, and note that a retry inside the model layer is one more HTTP request and
  zero more `before_model_callback` firings.
- **4.3** — run `shared_state.py` on **your** machine and record whether the concurrent case gives you
  `6, 6, 6` as it does here. It is a fact about a pinned dependency plus your event loop, which is
  exactly what `docs/PACKAGES.md`'s behaviour notes are for.
- **5.1** — decide what Sutra does about a documented halt that does not halt. There are three
  defensible answers — do not use the hook, use it and pin the real behaviour in a test, or raise from
  it deliberately — and the one indefensible answer is using it because the page says it works.
- **7.1** — read `ReflectAndRetryToolPlugin` and `ContextFilterPlugin` in the installed package, and
  write one sentence each on what installing them would do to your ledger's numbers.

---

## §5 The eval that must be able to fail

One new file, five assertions and one deliberate skip, **no API key required**. It runs on a fresh
clone with no `.env`, and the whole file with its walkthrough is
[part 7.2](parts/07-in-production/7.2-testing-a-plugin-without-a-model.md).

Yesterday four of five assertions called the callback directly, because a callback is a plain function
and its return value is the whole of what it decides. **Nothing about a plugin works that way.** That
it is installed, that it covers an agent it was never told about, that it cleans up when a run fails —
each of those is a fact about a whole run, so the suite drives a real `Runner` over a scripted model
and asserts on outcomes.

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_plugins.py -q -m "not live"   # RED: sutra/plugins.py is empty
# ... write the module from §4 ...
uv run python -m pytest tests/test_plugins.py -q -m "not live"   # 5 passed, 1 skipped
```

Then break each one on purpose. These are measured, not predicted:

| Break this | Which tests go red | What it is telling you |
| --- | --- | --- |
| delete `on_run_error_callback` | `a_failed_run_is_still_billed`, `no_run_state_is_left_behind` | failed runs are unbilled **and** leak (5.2) |
| `self.runs.get(...)` instead of `.pop(...)` | `no_run_state_is_left_behind` | the entry is read and never removed (4.3) |
| key the counter on `"all"` instead of `invocation_id` | `no_run_state_is_left_behind`, `each_run_is_billed_separately` | one counter for the whole process (4.3) |
| rename `tool_args` to `args` | **four of the five** | the names are the contract (2.3) |
| swap `Runner(app=...)` for `InMemoryRunner(agent=...)` | `the_plugin_is_actually_installed` | the install that installs nothing (1.2) |

Only the fourth breaks nearly everything, which is what makes the others worth having: they say *what*
broke rather than merely *that* something did.

**And one thing left undone deliberately.** The sixth test is `@pytest.mark.skip` with a `TODO(me)`,
because every number in the file was produced by the plugin under test. A green suite with that test
deleted would be claiming the ledger agrees with the provider, which nothing here has checked. If the
summary line ever reads `6 passed`, somebody removed the `TODO(me)` instead of doing it.

---

## §6 Request budget

**Free-tier Gemini**, 20 requests per day (`docs/PACKAGES.md`, 2026-08-25).

| What | Model calls |
| --- | --- |
| all seventeen lab scripts, all seven sections | **0** |
| the paper's demo, both `WEAVE` settings | **0** |
| the whole test suite | **0** |
| the failure lab | **0** |
| **Total required** | **0 of 20** |

Four days at zero, and today's reason is yesterday's with one change: the test double had to stop
counting. `ScriptedModel` walks a list and remembers its position, which is exactly wrong for a day
whose subject is one object shared across many runs — the double's own state would have masked the
plugin's. `ReactiveModel` reads the request and decides, so three concurrent runs cannot interfere with
each other through it, and 4.3's `6, 6, 6` is a fact about the plugin rather than an artefact of the
harness.

**Optional, and worth one request if you have quota:** install `RunLedger` on the real desk and run one
triage against `gemini-3.7-flash`. The number to look at is the model count. A scripted model never
retries; a real provider may, inside the model layer, where `before_model_callback` cannot see it — so
the live bill and the ledger can legitimately disagree, and that gap is what the skipped sixth test is
about.

**Cost: $0.**

---

## §7 Traps

- **`InMemoryRunner(agent=...)` ignores plugins entirely** — no error, no warning, and the run works
  perfectly while your plugin never fires. It is the one installation mistake with no error text.
  (1.1, 1.2)
- **Plugins belong on an `App`**, not on the `Runner`. `Runner(plugins=[...])` still works and is
  deprecated; passing **both** `app` and `plugins` raises. (1.2)
- **`Runner(app=...)` still needs a session service.** The `App` carries the agent and the plugins, not
  the services. (1.2)
- **Every hook must be `async`.** A plain `def` override is never awaited, and what fails is not your
  plugin. (1.1)
- **`name` is required and must be unique**, and the duplicate check runs when the **`Runner`** is
  built rather than the `App` — so the traceback points one line past where you were looking. (1.3)
- **A typo in `get_plugin("...")` is not an error**, it is `None`. (1.3)
- **The installed package has fourteen hooks; the published page lists twelve.** Print them from your
  own package before building anything on the list. (2.1)
- **A misspelled hook name silently does nothing.** There is no registration step to fail — you have
  added a method nobody calls. (2.1)
- **Four hooks exist only at this layer** — `on_user_message_callback`, `before_run_callback`,
  `on_event_callback`, `after_run_callback` — because no agent is in a position to answer a question
  about the whole request. (2.2)
- **`on_user_message_callback` must return `types.Content` or `None`.** A bare string does not raise
  where you wrote it. (2.2)
- **Rewriting the user's message rewrites what the session records.** Working as designed, and the
  transcript is now not what the user typed. (2.2)
- **The plugin hooks use different parameter names from the agent callbacks** — `tool_args` for `args`,
  `result` for `tool_response` — so a working callback copied into a plugin raises `TypeError` at the
  first tool call, and the diff looks fine in review. (2.3)
- **The hooks are keyword-only.** Dropping the `*` does not save you; ADK still calls by keyword. (2.3)
- **One question with one tool call fires ten hooks fifteen times.** `on_event_callback` fires three
  times and the model doors twice each, so anything expensive on a per-event hook is paid for on every
  agent in the application. (2.4)
- **A tool call costs two model calls**, not one: one to decide, one to answer with the result. Two
  tools cost three. Any budget written as one call per question is wrong by a factor that grows.
  (2.4, 4.1)
- **The plugin chain stops on `is not None` — the documented rule, and not yesterday's.** An empty
  dictionary stops a plugin chain, where at the agent tool door it falls between the two checks. (3.1)
- **Plugins run before agent callbacks at every door**, so a plugin returning a value means the agent's
  callback never executes — skipped, not overruled, and nothing says so. (3.1)
- **`on_agent_error_callback` and `on_run_error_callback` are notification-only.** Every plugin is
  told, every return value is discarded, and the original exception is always re-raised. Recovery
  belongs in `on_model_error_callback` or `on_tool_error_callback`. (3.2)
- **A notification hook that raises has its own error swallowed** — deliberately, so it cannot mask the
  real failure, which also means your bug there is invisible. (3.2)
- **A tool that catches its own exception never reaches `on_tool_error_callback`.** This is Day 13's
  1.x → 2.x trap #4, arriving one layer up. (3.2)
- **An exception in any of the twelve non-notification hooks kills the whole request, for every
  agent**, re-raised as a `RuntimeError` naming your plugin and the hook. Application-wide error
  handling is what you wrote, whether you meant to or not. (3.3)
- **`before_run_callback` returning `types.Content` is documented to halt the run and does not** on an
  `LlmAgent` root — which is every agent Sutra has. The return value is discarded and the agent runs.
  (5.1)
- **`after_run_callback` fires after the caller already has the answer**, and its return value is
  discarded. It reports; it cannot change anything. (4.2)
- **A plugin is constructed once for the life of the application.** A counter on `self` accumulates
  across every request: `2, 4, 6` for three runs in sequence, `6, 6, 6` for three at once. Key
  per-run state on `invocation_id`. (4.3)
- **`after_run_callback` does not fire on a failed run.** A meter built only on it under-reports
  exactly the runs that cost you something, and leaks one dictionary entry each. (5.2)
- **The two exit hooks are mutually exclusive**, so reporting from both does not double-count. (5.2)
- **Promoting a correct per-agent rule to a plugin applies it to agents it was never written for.**
  The guard that was right for the triage desk disables the FAQ agent whose job is answering password
  questions, with no error — and the FAQ agent's own tests still pass. (6.1)
- **A refusal with no `blocked_by` field is undebuggable at this layer.** Thirty agents, one plugin,
  and no way to tell which rule refused. (6.1)
- **Installing a shipped plugin can starve yours of traffic**, because the first plugin returning a
  value ends the chain. Order is policy here as much as it was in a callback list. (7.1)
- **`google.adk.plugins` imports lazily**, so `dir()` on the package does not list what is installed,
  and one shipped plugin needs an extra Sutra has not installed. (7.1)
- **You cannot test a plugin by calling its hooks.** Installed, covering, cleaning up — all three are
  facts about a whole run. (7.2)

---

## §8 Verify before you code

Every source below was checked on **2026-08-29** while this day was written, and the paper's record was
opened on **2026-08-30**. Principle 8: re-check on the day you use them. This table is evidence, not a
substitute.

| Source | What it settled |
| --- | --- |
| `adk.dev/plugins/` | the documented plugin model, the `App`-level framing, and the hook list — **twelve**, with `on_agent_error_callback` and `on_run_error_callback` absent · `before_run_callback` documented as halting the run when it returns a value |
| the installed `google-adk` 2.7.1 | `BasePlugin` defining **fourteen** `*_callback` methods and `PluginCallbackName` dispatching the same fourteen, with both set differences empty · `Runner._resolve_app` raising on `app` plus `plugins` · `PluginManager.register_plugin` raising on a duplicate name · `PluginManager._run_callbacks` returning on the first result that `is not None`, and catching a hook's exception into a `RuntimeError` naming plugin and hook · `_run_notification_callbacks` iterating every plugin and discarding results · `PluginManager.run_before_tool_callback` passing `tool_args` · `run_after_run_callback` awaited after the final event · `Runner._run_node_async` and what it does with `before_run_callback`'s return on an `LlmAgent` root · the nine shipped plugins under `google/adk/plugins/` and how many hooks each overrides |
| the installed `pytest` 9.1.1 | the suite in 7.2, run and then broken four ways |
| the Crossref record for `doi:10.1007/BFb0053381` | title, year (1997) and venue for the paper part's citation block — copied from the record, not from memory (`docs/PAPERS.md`, 2026-08-30) |

**Eleven claims in this day that no page states**, established by running code rather than by reading
it. Re-run them; if your version disagrees, **your terminal wins** and you fix the document:

```bash
cd days/day-14-plugins-one-layer-up/lab
uv run python where_it_lives.py    # 1.2 - the install that installs nothing, with no error
uv run python names.py             # 1.3 - which line the duplicate check actually fires on
uv run python doors.py             # 2.1 - fourteen, twice, from two places in the source
uv run python moved_names.py       # 2.3 - the TypeError, and which name it complains about
uv run python firing_order.py      # 2.4 - fifteen firings, in the order they really happen
uv run python two_layers.py        # 3.1 - the same two returns, opposite answers, one layer apart
uv run python metering.py          # 4.1 - two tools, three model calls
uv run python shared_state.py      # 4.3 - 2, 4, 6 and then 6, 6, 6
uv run python halt.py              # 5.1 - the documented halt that does not halt
uv run python never_prints.py      # 5.2 - the bill that is missing exactly when it matters
uv run python blast_radius.py      # 6.1 - the agent nobody was looking at
uv run python shipped.py           # 7.1 - what is already installed on your machine
```

The two to run twice are `two_layers.py` and `blast_radius.py`. Section 3 is downstream of the first,
and the second is the reason this day recommends plugins with a caveat attached rather than without
one.

---

## §9 Say it in an interview

> "A plugin in ADK is the same idea as an agent callback, moved up to the application. You attach it to
> the `App` rather than to an agent, and it then runs for every agent in that app — including ones
> added later by somebody who has never heard of your rule. That coverage is the entire reason to use
> one, so the question I ask before choosing a layer is: if somebody adds an agent next quarter and
> forgets this rule, is that a bug or a choice? Metering is a bug — an unmetered agent makes the quota
> router read low and shed load it did not need to — so it is a plugin. A refusal specific to one desk
> is a choice, so it stays a callback, and I write the reason in the docstring because otherwise it gets
> reversed by the next person. Three things I would flag from having run it. The layer is not just
> wider, it behaves differently: the plugin manager stops on the first result that is not `None`, which
> is the documented rule, whereas the agent tool-callback chain breaks on a truthy value and then tests
> `is None` — so an empty dictionary does opposite things one layer apart. The parameter names moved
> too, `args` to `tool_args`, so a working callback copied into a plugin raises at the first tool call
> and the diff looks correct in review. And the failure I actually care about is the blast radius: I
> promoted a completely correct guard from a triage desk into a plugin, and it silently disabled a
> self-service FAQ agent whose most common question was the thing the guard blocked. No error anywhere,
> and the FAQ agent's own tests still passed, because the plugin is not in its file. So my rules since
> are that a plugin's refusal always carries which rule refused, that the layer decision is written in
> the docstring next to the code, and that anything application-wide gets one test which runs an agent
> it was never written for."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked — honestly. `./m done 14` refuses to commit while
any box is unticked, and it cannot tell whether you were truthful. That part is yours.

The day is finished when `sutra/plugins.py` holds a `RunLedger` that counts at the two spending doors,
closes at **both** exits, and leaves `runs` empty afterwards; when it is installed on an `App` and you
have confirmed by running it that `InMemoryRunner` would not have installed it at all; when you have
run `doors.py` and can say how many hooks your package has rather than how many the page says; when you
have run `two_layers.py` and can state both rules and where they diverge; when you have run
`blast_radius.py` and sat with what the bug report would have said; when the five tests pass and you
have watched each go red for its own reason; when the sixth is a `TODO(me)` rather than a lie; when
both layer decisions — 6.1's and 7.3's — are written into docstrings rather than held in your head; and
when you have read the paper and can name the thing it calls obliviousness in the failure you caused.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 14 | <date> | ADK-16 | 19 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed today.

Two behavioural facts are worth a row **if your machine disagrees with this document**, because both
are facts about a pinned dependency in a particular environment, which is what that ledger is for: the
hook count `doors.py` prints, and `shared_state.py`'s concurrent line if it is not `6, 6, 6` for you.

**`docs/PAPERS.md`** — **one row, already added**, because the citation was verified while the day was
written rather than after it:

```text
| Aspect-oriented programming | doi:10.1007/BFb0053381 | 1997 | 2026-08-30 | 14 | `days/day-14-plugins-one-layer-up/papers/01-aspect-oriented-programming.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR is required, and two decisions belong in the commit message: that
`sutra/plugins.py` sits at the package root rather than under `sutra/desk/`, and which of Day 13's two
callbacks you decided **not** to promote. **If your ADK version now honours `before_run_callback`'s
return on an `LlmAgent` root, or the plugin chain stops on a truthy value rather than on `is not
None`, stop and re-read Principle 14 before editing anything** — that is a behaviour change in a
pinned dependency, and the plan is amended first.

**Commit message:**

```text
day 14: plugins - one layer up - closes ADK-16
```

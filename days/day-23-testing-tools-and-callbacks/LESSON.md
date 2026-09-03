---
day: 23
phase: 3
phase_name: "State, context & discipline"
title: "Testing agents I — unit tests for tools & callbacks"
ids: ["OPS-05", "OPS-06"]
principles: [1, 2, 4, 8, 10, 11, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-04"
status: written
lab_scaffolded: false
commit: ""
---

# Day 23 — Testing agents I: unit tests for tools & callbacks

> **Yesterday (Day 22):** every turn started writing one JSON line per happening, with a correlation
> id on each — and the day's last part,
> [22.4.3](../day-22-structured-logging/parts/04-in-production/4.3-testing-that-you-logged.md), tested
> the *formatter* while admitting that all eight of its cases pass against an empty log file.
> **Today:** the suite that catches that. pytest arrives, the deterministic half of Sutra gets a
> harness, and you will write a fake that lies to you on purpose so you can watch a green test be
> wrong.
> **Tomorrow (Day 24):** token accounting and budgets denominated in quota — arithmetic, which is
> exactly the kind of code that is wrong when nobody tests it.

---

## §1 Where we are

The health inspector comes into the restaurant kitchen at eleven on a Tuesday and nobody argues with
her.

The chef could. He could say, reasonably, that cooking is not a measurable thing — that the seasoning
is a matter of judgement, that the same dish comes out slightly differently every service, and that no
clipboard is going to capture whether the food is any good. All of that is true.

She does not measure the food. She puts a probe in the fridge and writes down four degrees. She checks
the date labels. She looks at whether the sink has hot water, whether the raw meat is below the cooked,
whether there is soap. None of those is a matter of taste. Every one of them has a right answer, and
every one of them is the difference between a kitchen that is fine and a kitchen that will make
somebody ill in six weeks.

That is where Sutra is this morning. There is a thousand-odd lines of Python in `sutra/`, and the
number of automated checks over it is **zero**. The standing excuse is the chef's: the model is
unpredictable, so what is there to test?

Four things worth knowing before you start.

**The excuse is a claim about a percentage, and the percentage is measurable.** Parsing every function
in `sutra/` and asking which ones name something that reaches a model or the network gives **16 of
34 — 47%**. Eighteen functions are plain Python with nothing to be nondeterministic about, and one
module, `config.py`, is 0 of 4.

**The seam is already there and the framework put it in.** ADK hands a tool an object with **46 public
members**; a real Sutra tool touches **one**. So the stand-in is five lines, and testing a tool costs
no runner, no session and no key.

**Everything you build today runs offline in a fifth of a second — and that is not a coincidence.**
The repository suite takes **6.02 seconds** and its slowest test takes **0.02**, because
`from google.adk.agents import LlmAgent` alone costs **5.74 seconds**. Testing at the seam is what
makes a suite fast; the two arguments are the same argument.

**And a green test can be wrong.** A plain dictionary standing in for ADK's `State` says
`'temp:raw_search' in state` is `True`, while the same key survives the turn `False`. No error, no
warning, no way to notice — which is why the failure lab today has two parts and one of them is green.

---

## §2 The map

Nineteen parts in six sections, and **one paper**. The day climbs
`foundation → working → production`: section 1 draws the line, section 2 is the runner and its
conventions, sections 3 and 4 are the two IDs meeting on Sutra's own code, section 5 is the failure lab
and section 6 is what changes when the suite gets big.

**Read the paper last.** *Mock roles, not objects* (`doi:10.1145/1028664.1028765`) is where the fake in
[3.2](parts/03-testing-tools/3.2-the-fake-tool-context.md) and the failure in
[5.2](parts/05-failure-lab/5.2-the-fake-that-could-not-fail.md) both came from. Principle 4 at the
scale of a day: write the double by hand, then read the argument about what it should have stood for.

### Section 1 — `01-where-the-line-falls`: which code deserves a unit test (OPS-05)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The nondeterminism excuse, counted](parts/01-where-the-line-falls/1.1-the-nondeterminism-excuse.md) | 47%, and eighteen functions with no excuse | `foundation` |
| 1.2 | [Fast, isolated, specific](parts/01-where-the-line-falls/1.2-fast-isolated-specific.md) | 408,000 pure calls to one TLS handshake | `foundation` |
| 1.3 | [The seam: test up to the boundary](parts/01-where-the-line-falls/1.3-the-seam.md) | 46 members, of which a tool uses one | `working` |
| 1.4 | [Four doubles, and the two Sutra needs](parts/01-where-the-line-falls/1.4-four-doubles.md) | Dummy, stub, spy, fake — and what each can assert | `working` |

### Section 2 — `02-pytest-house-rules`: the runner and its conventions (OPS-06)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [How pytest finds a test](parts/02-pytest-house-rules/2.1-how-pytest-finds-a-test.md) | The naming rule, and `no tests ran` | `foundation` |
| 2.2 | [Arrange, act, assert — and the name that says the crime](parts/02-pytest-house-rules/2.2-arrange-act-assert.md) | Same failure, two reports, one afternoon | `working` |
| 2.3 | [Fixtures: the arrange step, named and handed out fresh](parts/02-pytest-house-rules/2.3-fixtures.md) | Three builds against one, counted | `working` |
| 2.4 | [`parametrize`: one test, many cases](parts/02-pytest-house-rules/2.4-parametrize.md) | Ten tests from three functions | `working` |
| 2.5 | [Markers, and the `-m "not live"` line](parts/02-pytest-house-rules/2.5-markers-and-the-not-live-line.md) | One character wrong, and who catches it | `working` |

### Section 3 — `03-testing-tools`: the two IDs meeting on a tool

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A tool is a function first](parts/03-testing-tools/3.1-a-tool-is-a-function-first.md) | Assert what is absent, not only what is there | `working` |
| 3.2 | [The fake `ToolContext`, in five lines](parts/03-testing-tools/3.2-the-fake-tool-context.md) | A stub and a spy in one small object | `working` |
| 3.3 | [The async tool, without a runner](parts/03-testing-tools/3.3-the-async-tool-without-a-runner.md) | `asyncio.run`, and no plugin | `working` |

### Section 4 — `04-testing-hooks`: …and on a callback

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [A callback's return value is its whole contract](parts/04-testing-hooks/4.1-the-return-value-is-the-contract.md) | `is None`, never `not verdict` | `working` |
| 4.2 | [Testing the hook that rescues](parts/04-testing-hooks/4.2-testing-the-hook-that-rescues.md) | The second test is the one nobody writes | `production` |
| 4.3 | [Testing that a hook returns `None`](parts/04-testing-hooks/4.3-testing-that-a-hook-returns-none.md) | A recorder that quietly became an editor | `production` |

### Section 5 — `05-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The test that phoned the model](parts/05-failure-lab/5.1-the-test-that-phoned-the-model.md) | A 503, then three 429s, and no information | `production` |
| 5.2 | [💥 The fake that could not fail](parts/05-failure-lab/5.2-the-fake-that-could-not-fail.md) | `True` in the test, `False` in production | `production` |

### Section 6 — `06-in-production`: when the suite gets big

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Coverage is a map, not a score](parts/06-in-production/6.1-coverage-is-a-map-not-a-score.md) | 44%, and why the real answer is two | `production` |
| 6.2 | [The suite that has to stay fast](parts/06-in-production/6.2-the-suite-that-has-to-stay-fast.md) | 6.02 seconds, of which 5.74 is one import | `production` |

### The paper — read after the parts

| # | Paper | What it answers | Level |
| --- | --- | --- | --- |
| 01 | [Mock roles, not objects](papers/01-mock-roles-not-objects.md) | `doi:10.1145/1028664.1028765` — one place, not four | `production` |

---

## §3 Setup — run this

**No new packages today.** `pytest` is already pinned at `9.1.1` in `pyproject.toml` and already
configured — `addopts`, `testpaths` and two markers have been sitting in
`[tool.pytest.ini_options]` since Day 0 with nothing to collect. Today they get something.

```bash
# 1 - confirm the runner and the config it will read
uv run python -m pytest --version
uv run python -m pytest --collect-only -o addopts="" | head -3   # rootdir + configfile lines

# 2 - the day folder's lab, and the paper's demo folder
cd days/day-23-testing-tools-and-callbacks
mkdir -p lab/papers/mock-roles-not-objects
cd lab

# 3 - the argument, in four scripts that run before any test exists
touch count_the_shell.py three_properties.py the_seam.py doubles.py

# 4 - the pytest conventions, one file per idea
touch test_discovery_demo.py test_red_on_purpose.py test_fixtures_demo.py
touch test_parametrize_demo.py test_markers_demo.py test_typo_marker_demo.py

# 5 - Sutra's own shapes: tools, the double, the hooks
touch tools_demo.py fake_context.py test_tools_demo.py
touch hooks_demo.py test_hooks_demo.py

# 6 - the failure lab and the production section
touch phoned_the_model.py drifted_fake.py untested_map.py suite_speed.py

# 7 - the paper's two-file demo
touch papers/mock-roles-not-objects/vendor.py papers/mock-roles-not-objects/run.py
cd -

# 8 - what changes under tests/ today
ls tests/                    # test_tools.py and test_callbacks.py are new
```

**Step 1 is the one people skip and then debug for an hour.** The `rootdir` and `configfile` lines tell
you which `pyproject.toml` pytest is actually reading; every marker, every path and every option comes
from that file, and a marker that seems to be ignored is almost always a run whose rootdir is somewhere
else.

**Two files in the lab are meant to be RED.** `test_red_on_purpose.py` fails three assertions on
purpose so you can compare the failure messages, and `test_typo_marker_demo.py` fails at *collection*
because its marker has a typo. Both are teaching material, not mistakes; the checklist says so.

**Run `count_the_shell.py` first.** It is the argument for the whole day in one table, it needs
nothing, and the number it prints about your repository is what makes the rest of the day feel
necessary rather than dutiful.

**One script needs a key and quota:** `phoned_the_model.py`, which spends **2** of the free tier's
twenty daily requests. Everything else in the day — nineteen parts, every test, the paper's demo —
runs offline. See §6, and read [5.1](parts/05-failure-lab/5.1-the-test-that-phoned-the-model.md) before
you run it, because on the day this was written it did not succeed and the failure is the lesson.

---

## §4 Build brief

**`tests/test_tools.py`** — new. Unit tests for the tools Days 10, 11, 17 and 18 told you to write:

| What to pin | Why it is the assertion that matters | Taught in |
| --- | --- | --- |
| the happy path's whole return dict | an unexpected key is a change nothing else catches | 3.1 |
| `"title" not in result` on a miss | an invented field teaches the model to lie | 3.1 |
| state after a rejected input | validating *after* writing passes a return-value test | 3.2 |
| the spy's `saved` list, whole | asserts the artifact was saved **exactly once** | 3.3 |
| the second save's version | two saves of one filename are two versions, not two files | 3.3 |
| `"4521 "` producing one filename | `int(ticket_id)` is a design decision, not a cast | 3.3 |

**`tests/test_callbacks.py`** — new. One pair per hook, and the second of each pair is the point:

| What to pin | Why | Taught in |
| --- | --- | --- |
| the brake fires on an unapproved write | the rule works | 4.1 |
| the brake returns `None` on a read | the *condition* works | 4.1 |
| a planned failure is rescued **and marked** | a substitute that does not say so is a lie | 4.2 |
| an unplanned failure returns `None` | rescuing everything is Day 21's swallow, one layer up | 4.2 |
| the recorder returns `None` | `-> Optional[Event]` means it *could* rewrite the record | 4.3 |

**`conftest.py`** under `tests/` — one `fake_context` fixture, **function-scoped**, returning a fresh
double. It is mutable, so 2.3's rule applies, and every later day's tests will ask for it by name.

**Nothing under `sutra/` has to change today.** That is unusual and deliberate: today's deliverable is
a harness over code that already exists. Confirm with `git diff` before you commit.

**`TODO(me)` markers left for you:**

- **1.1** — run `count_the_shell.py` and **write your prediction down first**: which module will be
  most model-bound, and what the overall percentage will be. Being wrong about that is the habit this
  section exists to build.
- **1.4** — add a fifth double to `doubles.py`: a **fake that fails**, whose `article` raises
  `TimeoutError` for one id. That is the double 4.2's rescue test needs.
- **2.2** — take the message off `test_every_ticket_...`, break it again, and put the two
  `short test summary info` lines side by side. Then decide the rule for when *your* assertions carry
  messages, and write it in one sentence.
- **2.3** — decide whether `fake_context` lives in `tests/conftest.py` or in each file, and say what
  scope it gets and why.
- **2.5** — Sutra has two markers. Decide whether it needs a third for tests that are known-flaky, and
  if you say no, say what happens to the first flaky test instead.
- **3.1** — open every tool in `sutra/` and write down, without running anything, the two dictionaries
  each can return. That list is your test file.
- **4.2** — pick one Sutra tool that must **never** be substituted (a write, not a read) and add the
  per-tool rule to the policy, keyed on `tool.name`. Then write the test that proves it.
- **4.3** — write the assertion this day admits it does not have: that the recorder did not **mutate**
  the event in place. Compare against a copy taken before the call, and say what that costs.
- **5.2** — grep `sutra/state.py` for every prefixed constant. For each, write what would break in
  production if the prefix were wrong, then check whether any test you have would catch it.
- **6.1** — run `untested_map.py`, cross off every `main` and `demo_*`, and for what remains decide:
  unit test, integration test, or deliberately untested. Write the third category down somewhere a
  reviewer will find it.
- **6.2** — decide whether `./m check` gets a wall-clock budget, and if so what number and who is told
  when it is exceeded.
- **The paper** — add a fourth feature that needs an article to `run.py`, and run both arms again. One
  count stays at 1 and the other goes to 5. Then say what the ROLES=1 arm still does **not** protect
  you from.

---

## §5 The eval that must be able to fail

The lab's own suite is **thirty-six passing cases across five files**, plus two files that are red on
purpose. All of it offline.

| File | Cases | What it pins |
| --- | --- | --- |
| `test_discovery_demo.py` | 3 | the collection rule, and a helper that is not collected |
| `test_fixtures_demo.py` | 6 | function scope is fresh, module scope is shared, counted |
| `test_parametrize_demo.py` | 10 | one rule per case, each named in the report |
| `test_tools_demo.py` | 10 | three tools: return value, state, and the spy's record |
| `test_hooks_demo.py` | 7 | both directions of every hook's return contract |
| `test_markers_demo.py` | 3 + 1 deselected | the `live` label doing its job |

**How to watch the real suite go RED before it goes green:**

```bash
uv run python -m pytest tests/test_tools.py -q -m "not live"     # RED: the file does not exist yet
# ... write the assertions from §4 ...
uv run python -m pytest tests/test_tools.py -q -m "not live"     # green
```

Then break things on purpose. Measured in the lab on 2026-09-04:

| Break this | What goes red | What it is telling you |
| --- | --- | --- |
| return `{"title": ""}` on a miss | one assertion of two | the status test agrees with the lie (3.1) |
| make the double's `save_artifact` sync | every async tool test | `object int can't be used in 'await' expression` (3.2) |
| widen `isinstance(error, TimeoutError)` to `Exception` | **one of seven** | the happy path never noticed (4.2) |
| `return event` in the recorder | one of two assertions | the log was still perfect (4.3) |
| `desk_state` returns a module-level dict | one fixture test | the leak, named (2.3) |

**The third row is the one to sit with.** Broadening the rescue to catch every exception — a change any
reasonable afternoon produces — turns one test red out of seven. Every check of the intended behaviour
stays green, because timeouts are still rescued. Only the test that asserts *nothing happened* can see
it.

**And what this suite still does not catch, stated plainly:** every test today runs against a double.
All of them pass in a system where the plugins were never installed, the tools were never registered
and no invocation has ever run. That is
[22.4.3](../day-22-structured-logging/parts/04-in-production/4.3-testing-that-you-logged.md)'s blind
spot inherited, and the integration test that closes it is Day 31's business.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| four argument scripts, nineteen parts | **0** |
| the whole lab test suite, thirty-six cases | **0** |
| `drifted_fake.py`, `untested_map.py`, `suite_speed.py` | **0** |
| the paper's demo, all four arms | **0** |
| `phoned_the_model.py` (optional, 5.1) | **2** |
| **Total required** | **0 of 20** |
| **Total if you run the failure lab live** | **2 of 20** |

**Zero required, and that is the whole day's argument rather than a happy accident.** A day about
testing that needed quota to be understood would have refuted itself.

**What actually happened on 2026-09-04 is worth recording**, because it is the day's best evidence and
it was not planned. `phoned_the_model.py` was run twice to capture two answers to one prompt. The first
attempt met `503 UNAVAILABLE` — the provider was busy. The second met the daily ceiling:
`quotaId: 'GenerateRequestsPerDayPerProjectPerModel-FreeTier'`, `quotaValue: '20'`. So the comparison
that part was meant to show was never obtained, and what it shows instead is a live test failing twice
for reasons that have nothing to do with any code. Both bodies are quoted verbatim in
[5.1](parts/05-failure-lab/5.1-the-test-that-phoned-the-model.md).

**Cost: $0.**

---

## §7 Traps

- **A renamed test disappears silently.** pytest collects by name, so `check_refund_window` is not a
  test and nothing reports its absence. Watch the test **count** as a number that should only go up
  (2.1).
- **`no tests ran` and `all passed` look almost identical** at the bottom of a terminal and mean
  opposite things. `--collect-only` first, always (2.1).
- **`assert not verdict` accepts `{}` as well as `None`**, and those are opposite instructions to the
  framework. Use `is None` (4.1).
- **A mutable default argument is created once**, so `def __init__(self, state={})` gives every double
  in the suite the same dictionary (3.2).
- **A module-scoped fixture returning a mutable object couples every test in the file**, and the suite
  then passes in file order and fails shuffled (2.3).
- **A synchronous `save_artifact` on the double** produces `TypeError: object int can't be used in
  'await' expression`, and the message points at the tool rather than at the double (3.2).
- **`@pytest.mark.liv` without `--strict-markers` is a warning and the test still runs** — in nobody's
  filter, red in CI or spending quota on every commit (2.5).
- **Two test files with the same basename** and no `__init__.py` stop the whole run with
  `import file mismatch` (2.1).
- **A plain dict is not ADK's `State`.** `temp:` survives in the fake and is discarded by the
  framework, with no error either way (5.2).
- **A live test in the default suite eats the quota the agent needs.** One live test at ten changes a
  day is half the daily allowance (5.1).
- **Coverage measures execution, not assertion.** A test with no `assert` gives full marks (6.1).

---

## §8 Verify before you code

Fetched or read on **2026-09-04**, the day this was written:

- `https://pypi.org/pypi/pytest/json` — latest is **9.1.1**, `requires_python >=3.10`. Already the
  pinned version in `pyproject.toml`, so no new row in `docs/PACKAGES.md`.
- The installed `google-adk` 2.7.1 source, `google/adk/agents/context.py` and
  `readonly_context.py` — counted rather than trusted: `ReadonlyContext` declares 8 properties and 1
  method, `Context` declares 21 and 16, for **46 public members**. `ToolContext is Context` and
  `CallbackContext is Context` both return `True`.
- The same tree, `google/adk/plugins/base_plugin.py` — the exact signatures of
  `before_tool_callback`, `on_tool_error_callback`, `on_event_callback` and `after_tool_callback`.
  All keyword-only, all `async`, and `on_event_callback` returns `Optional[Event]`, which is
  [4.3](parts/04-testing-hooks/4.3-testing-that-a-hook-returns-none.md)'s whole subject.
- `google/adk/sessions/base_session_service.py` — `_trim_temp_delta_state`, which removes `temp:` keys
  from what gets persisted. That method is the evidence behind
  [5.2](parts/05-failure-lab/5.2-the-fake-that-could-not-fail.md).
- `Context.save_artifact` confirmed a coroutine function, with signature
  `(filename: str, artifact: types.Part, custom_metadata: dict[str, Any] | None = None) -> int`.
- The Gemini free model list, read live via `client.models.list()` — `gemini-3.7-flash` is still
  present, so Day 9's pin holds.
- `https://api.crossref.org/works/10.1145/1028664.1028765` — the paper's exact title and venue, from
  the machine-readable record rather than from memory (§17.4.1 rule 5).

**No adk.dev page was needed today.** Every ADK fact this day uses is a signature or a behaviour that
can be read out of the installed package and counted, which is the stronger form of Principle 8: not
"the documentation says" but "the code in `.venv` does, and here is the number".

---

## §9 Say it in an interview

"We had about a thousand lines of agent code and no tests, and the reason everyone gave was that you
can't test something built on an LLM. So I parsed the package and counted: forty-seven percent of the
functions touched a model, and one module accounted for most of them. The other eighteen were dict
lookups, validation and string formatting — ordinary Python that had simply never been tested because
the excuse covered everything.

The thing that made it easy was that the framework had already put the seam in. ADK hands a tool a
context object with forty-six public members, and our tools touch one of them, so the double is five
lines — a dict for state and one async method that records what got saved. No runner, no session, no
key, and the whole tool suite runs in about a fifth of a second.

Two things I'd tell anyone doing this. First, for a callback the return value **is** the contract —
`None` means carry on, anything else replaces what was about to happen — so the test I always write is
the one asserting it returned `None`, because a hook that accidentally returns something doesn't crash,
it just silently stops the tool from running. We proved it: widening one `isinstance` in the error
policy to catch every exception turned exactly one test red out of seven, and every check of the
intended behaviour stayed green.

Second, be careful what your fake doesn't do. We used a plain dictionary for the framework's state
object, and the framework discards keys with a `temp:` prefix when it persists. The dict doesn't. So a
test asserting the value was stored was green while production threw it away — no error, nothing in the
log. The fix is a contract test: the same assertions run against the fake and the real thing, the
second one on a schedule.

And we kept everything out of the default suite that needs a key. The day I set this up, the live check
failed twice — once with a 503 because the provider was busy and once with a 429 because the free tier
is twenty requests a day and we'd spent them. Neither failure was about our code, and that's the whole
argument: a suite that goes red for reasons you don't control is a suite people stop believing."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 23` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it to
someone else without the page open.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 23 | <date> | OPS-05, OPS-06 | 19 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — no new rows. `pytest==9.1.1` was pinned on 2026-08-23 and re-verified against
`pypi.org/pypi/pytest/json` today; the version has not moved, so the existing row stands.

**`docs/PAPERS.md`** — append:

```text
| Mock roles, not objects | doi:10.1145/1028664.1028765 | 2004 | 2026-09-04 | 23 | `days/day-23-testing-tools-and-callbacks/papers/01-mock-roles-not-objects.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skills were sourced today.

**The commit:**

```text
day 23: testing agents I - unit tests for tools and callbacks - closes OPS-05, OPS-06
```

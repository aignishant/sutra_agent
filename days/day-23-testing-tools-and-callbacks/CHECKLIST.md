# Day 23 — CHECKLIST

**IDs closed:** OPS-05, OPS-06
**Principles served:** 1, 2, 4, 8, 10, 11, 15, 16, 17, 18
**Parts:** 19 across 6 sections, plus 1 paper

> `./m done 23` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
cd days/day-23-testing-tools-and-callbacks/lab
uv run python count_the_shell.py                          # 0 generations
uv run python three_properties.py                         # 0 generations
uv run python the_seam.py                                 # 0 generations
uv run python doubles.py                                  # 0 generations
uv run python -m pytest test_discovery_demo.py --collect-only -o addopts=""
uv run python -m pytest test_discovery_demo.py            # green
uv run python -m pytest test_red_on_purpose.py            # RED on purpose - read it
uv run python -m pytest test_fixtures_demo.py             # green
uv run python -m pytest test_parametrize_demo.py          # green
uv run python -m pytest test_markers_demo.py -m "not live"
GOOGLE_API_KEY= GEMINI_API_KEY= uv run python -m pytest test_markers_demo.py   # RED, no key
uv run python -m pytest test_typo_marker_demo.py          # ERROR at collection, on purpose
uv run python -m pytest test_tools_demo.py                # green
uv run python -m pytest test_hooks_demo.py                # green
uv run python drifted_fake.py                             # 0 generations
uv run python untested_map.py                             # 0 generations
uv run python suite_speed.py                              # 0 generations
cd papers/mock-roles-not-objects
ROLES=1 VENDOR=1 uv run python run.py                     # 0 generations
ROLES=1 VENDOR=2 uv run python run.py                     # 0 generations
ROLES=0 VENDOR=1 uv run python run.py                     # 0 generations
ROLES=0 VENDOR=2 uv run python run.py                     # 0 generations
cd -
uv run python -m pytest tests/test_tools.py tests/test_callbacks.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: **47%**, with `config.py` at 0 of 4; **one call at ~1 µs against a ~400 ms handshake**;
**46 public members and a tool touching 1**; four doubles and one deliberate `AssertionError`; then
`3 tests collected` and `3 passed`; **three failures whose messages differ enormously**; `6 passed`;
`10 passed`; `3 passed, 1 deselected`; then **red with `No API key was provided`**; then
`'liv' not found in \`markers\` configuration option`; `10 passed`; `7 passed`; then
**`temp:` kept by the fake and dropped by ADK**; a GAP list that is mostly `main`; **~6 s total of
which ~5.7 s is one import**; then **1 place against 4** in both vendor versions. Then your own suite
green, `OK all green`, `traceability: 43/199 closed, 0 problem(s)`, and one commit.

## Setup

- [ ] `uv run python -m pytest --version` prints **9.1.1**, matching the pin in `pyproject.toml`
- [ ] `--collect-only -o addopts=""` printed a `rootdir` and a `configfile: pyproject.toml` line, and
      you read both
- [ ] `days/day-23-testing-tools-and-callbacks/lab/` exists with the sixteen scripts
- [ ] `lab/papers/mock-roles-not-objects/` exists with `vendor.py` and `run.py`
- [ ] No `uv add` was needed — confirmed `pytest` was already pinned and configured on Day 0
- [ ] Confirmed everything except `phoned_the_model.py` runs with **no `GOOGLE_API_KEY` set at all**

## Section 1 — `01-where-the-line-falls`

- [ ] **1.1** read · **wrote your prediction down first**, then ran `count_the_shell.py` · said out
      loud the difference between the deterministic shell and the stochastic core, with one Sutra
      function in each
- [ ] **1.2** read · ran `three_properties.py` · ran it again with `GOOGLE_API_KEY=` and watched the
      last two lines change · said out loud the three properties and which one an API key breaks
- [ ] **1.3** read · ran `the_seam.py` · **listed by hand every `tool_context` attribute one of your
      own tools touches** · said out loud what a seam is and why `tool_context` is one
- [ ] **1.4** read · ran `doubles.py` and **saw the dummy raise** · added the fifth double, a fake
      that raises `TimeoutError` for one id · said out loud which double you would use to check that
      your code audited a read

## Section 2 — `02-pytest-house-rules`

- [ ] **2.1** read · ran `--collect-only` · **renamed one test to `check_...`, watched the count drop,
      and put it back** · said out loud the three parts of the collection rule and what `no tests ran`
      means
- [ ] **2.2** read · ran `test_red_on_purpose.py` and **read all three failures** · took the message
      off the third and compared the two summary lines · said out loud what a message tells you that
      pytest's output cannot
- [ ] **2.3** read · ran `test_fixtures_demo.py` green · **made `desk_state` return a module-level
      dict and watched the freshness test go red** · said out loud what scope controls
- [ ] **2.4** read · ran the collection and saw ten named cases · **added a fourth value to
      `RETRYABLE` and watched a fourth case appear with no new test** · said out loud what a loop
      cannot do
- [ ] **2.5** read · ran `-m "not live"` (3 passed, 1 deselected) · ran with no key (1 failed) · ran
      `test_typo_marker_demo.py` and got a **collection error** · said out loud what
      `--strict-markers` changes

## Section 3 — `03-testing-tools`

- [ ] **3.1** read · ran `test_tools_demo.py` green · **made the miss return `title: ""` and watched
      only the negative assertion go red** · said out loud why a failure result must not carry the
      success result's keys
- [ ] **3.2** read · **deleted an attribute from the double and read the `AttributeError`** · made
      `save_artifact` synchronous and saw `object int can't be used in 'await' expression` · said out
      loud why the double needs `async def`
- [ ] **3.3** read · **deleted the `await` inside `save_note` and read which assertion caught it** ·
      said out loud what calling an `async def` function returns and what `asyncio.run` does with it

## Section 4 — `04-testing-hooks`

- [ ] **4.1** read · ran the hook tests green · **changed `return None` to `return {}` and read which
      tests went red** · said out loud the return-value rule and why `assert not verdict` is wrong
- [ ] **4.2** read · **widened `isinstance(error, TimeoutError)` to `Exception` and counted: exactly
      one of seven red** · said out loud why the test for an unhandled error matters more than the
      test for a handled one
- [ ] **4.3** read · **changed `return None` to `return event` in the recorder: one assertion red, the
      log still perfect** · said out loud what `Optional[Event]` permits and why a log-file test
      cannot see it

## Section 5 — `05-failure-lab`

- [ ] **5.1** read · ran the same file green (deselected) and red (no key) on identical code · read
      the real `503` and `429` bodies quoted in the part · said out loud the four ways a live test goes
      red without your code being wrong
- [ ] **5.2** read · ran `drifted_fake.py` and **saw `temp:raw_search` kept by the dict and dropped by
      ADK** · grepped `sutra/state.py` for prefixed constants and checked whether any test you have
      would catch a wrong one · said out loud the one kind of test that stops a fake drifting

## Section 6 — `06-in-production`

- [ ] **6.1** read · ran `untested_map.py` · **crossed off every `main` and `demo_*` and decided a
      category for what remained** · said out loud what a coverage percentage cannot see
- [ ] **6.2** read · ran `suite_speed.py` · ran `--durations=5` on the real suite and **subtracted the
      durations from the total** · said out loud what the remainder is

## The paper — read after the parts

- [ ] **`papers/01-mock-roles-not-objects.md`** read · ran **all four arms** of the demo
- [ ] Saw the count go **1 against 4**, and saw *both* arms report a green suite over a broken system
- [ ] Added a fourth feature that needs an article and re-ran: one count stayed at 1, the other became 5
- [ ] Can say what the ROLES=1 arm still does **not** protect you from, and which step of the mechanism
      closes that gap
- [ ] Answered out loud: *what did this paper actually claim, and what do we do differently now?*
- [ ] Named one thing from it in everyday use today and one thing the field replaced

## Build brief

- [ ] `tests/test_tools.py` written, covering all six rows of §4's first table
- [ ] At least one **negative** assertion per tool: the key that must not be there
- [ ] The spy's list compared **whole**, so "saved exactly once" is actually asserted
- [ ] `tests/test_callbacks.py` written, with **a pair per hook** — fires, and does not fire
- [ ] The unhandled-error test present and asserting `is None`, not `not verdict`
- [ ] The recorder's `assert returned is None` present, with the return value **captured**
- [ ] `tests/conftest.py` holds one function-scoped `fake_context` fixture
- [ ] Nothing under `sutra/` changed today — confirmed with `git diff`
- [ ] Decided and wrote down: which Sutra tool must never be substituted, and the per-tool rule for it

## The eval that must be able to fail

- [ ] Watched `tests/test_tools.py` RED **before** writing the assertions, not after
- [ ] **Broke it on purpose:** returned `title: ""` on a miss — one assertion of two red
- [ ] **Broke it a second way:** made the double's `save_artifact` synchronous — the async tests red
      with a message that points at the wrong file
- [ ] **Broke it a third way:** widened the rescue to `Exception` — **one of seven** red
- [ ] **Broke it a fourth way:** `return event` from the recorder — one of two assertions red
- [ ] Read all four failure messages and improved at least one into a sentence you would want at 2am
- [ ] Wrote down what this whole suite still does not catch, in one sentence
- [ ] Fixed everything; suite green again

## Request budget

- [ ] Total generations required for the day: **0 of 20**
- [ ] Confirmed by running the whole demo command with no `GOOGLE_API_KEY` in the environment
- [ ] If you ran `phoned_the_model.py`: **2 of 20** spent, and you recorded what actually happened —
      including a `503` or a `429` if that is what you got

## Ledger

- [ ] `docs/PROGRESS.md` row appended:
      `| 23 | <date> | OPS-05, OPS-06 | 19 (+1 paper) | <hash> | ✅ |`
- [ ] `docs/PAPERS.md` row appended:
      `| Mock roles, not objects | doi:10.1145/1028664.1028765 | 2004 | 2026-09-04 | 23 | days/day-23-testing-tools-and-callbacks/papers/01-mock-roles-not-objects.md |`
- [ ] `docs/PACKAGES.md` — confirmed no new rows; `pytest==9.1.1` re-verified against PyPI today
- [ ] `./m depth 23` green
- [ ] `./m trace` shows OPS-05 and OPS-06 closed, `43/199`, 0 problems
- [ ] `./m check` green

## Commit

- [ ] `day 23: testing agents I - unit tests for tools and callbacks - closes OPS-05, OPS-06`

# Day 23 - Testing agents I — unit tests for tools & callbacks

IDs closed: OPS-05, OPS-06 · source: `days/day-23-testing-tools-and-callbacks/`

## Parts

### 1.1 - The nondeterminism excuse, counted
`days/day-23-testing-tools-and-callbacks/parts/01-where-the-line-falls/1.1-the-nondeterminism-excuse.md` · level `foundation` · ids OPS-05

"You cannot unit test an agent, the model is nondeterministic" is a claim about a percentage, and when you actually count the functions in sutra/ the percentage is 47% — which means the excuse is being used to avoid testing the other eighteen functions that are plain Python.

### 1.2 - Fast, isolated, specific
`days/day-23-testing-tools-and-callbacks/parts/01-where-the-line-falls/1.2-fast-isolated-specific.md` · level `foundation` · ids OPS-05

A test earns its place by being fast (one tool call here is 1.03 microseconds, against 419 ms for a single TLS handshake to the model host — a ratio of about 408,000 to one), isolated (green on a train, with no key in the environment) and specific (its name tells you what broke before you open the file).

### 1.3 - The seam: test up to the boundary
`days/day-23-testing-tools-and-callbacks/parts/01-where-the-line-falls/1.3-the-seam.md` · level `working` · ids OPS-05

ADK hands a tool an object with 46 public members, a real Sutra tool touches one of them, and that gap — 2.2% — is the seam: the place where you can substitute something you built for something the framework normally supplies, and test everything on your side of it.

### 1.4 - Four doubles, and the two Sutra needs
`days/day-23-testing-tools-and-callbacks/parts/01-where-the-line-falls/1.4-four-doubles.md` · level `working` · ids OPS-05

There are four useful kinds of stand-in — dummy (must never be called), stub (answers with a fixed value), spy (answers, and remembers what it was asked) and fake (a working implementation with a shortcut) — and Sutra needs the stub and the spy for tools, and the fake for anything that has rules of its own.

### 2.1 - How pytest finds a test, and why `assert` is enough
`days/day-23-testing-tools-and-callbacks/parts/02-pytest-house-rules/2.1-how-pytest-finds-a-test.md` · level `foundation` · ids OPS-06

pytest collects any function whose name starts with test_ in any file whose name starts with test_, and it rewrites your plain assert statements so that a failure prints the values that were compared rather than the word False.

### 2.2 - Arrange, act, assert — and the name that says the crime
`days/day-23-testing-tools-and-callbacks/parts/02-pytest-house-rules/2.2-arrange-act-assert.md` · level `working` · ids OPS-06

A test body has three parts in a fixed order — set up the world, do one thing, check one outcome — and the assertion's message is worth more than everything else in the file, because the same failing condition reported as assert 'not_found' == 'ok' and as "9999 reached the tool but is not in TICKETS" costs two very different evenings.

### 2.3 - Fixtures: the arrange step, named and handed out fresh
`days/day-23-testing-tools-and-callbacks/parts/02-pytest-house-rules/2.3-fixtures.md` · level `working` · ids OPS-06

A fixture is the arrange step given a name and requested by writing that name as a parameter, and its scope decides whether each test gets its own — three tests asking for a function-scoped fixture built it three times, while four tests asking for a module-scoped one shared a single object.

### 2.4 - `parametrize`: one test, many cases
`days/day-23-testing-tools-and-callbacks/parts/02-pytest-house-rules/2.4-parametrize.md` · level `working` · ids OPS-06

@pytest.mark.parametrize turns one test function into one test per case, each with its own name in the output — so a failure reads test_a_transient_failure_is_worth_another_attempt[connection_reset] instead of "the classifier is broken", and the other cases still run.

### 2.5 - Markers, and the `-m \"not live\"` line you have been typing
`days/day-23-testing-tools-and-callbacks/parts/02-pytest-house-rules/2.5-markers-and-the-not-live-line.md` · level `working` · ids OPS-06

A marker is a label on a test, -m "not live" is the filter that reads it, and --strict-markers is what turns a one-character typo from a warning that runs the test anyway into an error that stops the run — 'liv' not found in \markers\ configuration option.

### 3.1 - A tool is a function first
`days/day-23-testing-tools-and-callbacks/parts/03-testing-tools/3.1-a-tool-is-a-function-first.md` · level `working` · ids OPS-05, OPS-06

A tool with no tool_context parameter is an ordinary Python function, so testing it needs no framework at all — and the assertion worth writing first is the negative one, that an unknown ticket comes back as not_found and does not carry a title.

### 3.2 - The fake `ToolContext`, in five lines
`days/day-23-testing-tools-and-callbacks/parts/03-testing-tools/3.2-the-fake-tool-context.md` · level `working` · ids OPS-05, OPS-06

The stand-in for ADK's 46-member context is a small class with a state dictionary and a save_artifact method that appends to a list — a stub and a spy in one object — and it is enough because the tool asks Python for .state, not for a type.

### 3.3 - The async tool, without a runner
`days/day-23-testing-tools-and-callbacks/parts/03-testing-tools/3.3-the-async-tool-without-a-runner.md` · level `working` · ids OPS-05, OPS-06

asyncio.run(save_note("4521", body, ctx)) runs one async tool to completion in a synchronous test — no plugin, no event loop of your own, no runner — and without it pytest refuses the test outright with "async def functions are not natively supported."

### 4.1 - A callback's return value is its whole contract
`days/day-23-testing-tools-and-callbacks/parts/04-testing-hooks/4.1-the-return-value-is-the-contract.md` · level `working` · ids OPS-05, OPS-06

Every ADK hook says the same thing with its return value — None means carry on and anything else means stop and use this instead — so a hook is tested by driving it with asyncio.run and asserting on exactly one thing: what came back.

### 4.2 - Testing the hook that rescues
`days/day-23-testing-tools-and-callbacks/parts/04-testing-hooks/4.2-testing-the-hook-that-rescues.md` · level `production` · ids OPS-05, OPS-06

An on_tool_error_callback needs two tests that look almost identical: one asserting it returns a substitute for the failure it was designed for, and one asserting it returns None for a failure it was not — because a hook that rescues everything is Day 21's swallowed exception wearing a plugin's clothes.

### 4.3 - Testing that a hook returns `None`
`days/day-23-testing-tools-and-callbacks/parts/04-testing-hooks/4.3-testing-that-a-hook-returns-none.md` · level `production` · ids OPS-05, OPS-06

A recorder must observe and change nothing, and since on_event_callback is declared -> Optional[Event] the framework will happily use whatever it returns — so the assertion that keeps a logger from rewriting the record is assert returned is None, and it is the only one that can.

### 5.1 - 💥 The test that phoned the model
`days/day-23-testing-tools-and-callbacks/parts/05-failure-lab/5.1-the-test-that-phoned-the-model.md` · level `production` · ids OPS-05, OPS-06

The same test file ran three ways on 2026-09-04: deselected it was green in 1.04 seconds; with no key it was red with ValueError: No API key was provided; and with a real key it was red twice more, first with 503 UNAVAILABLE because the provider was busy and then with 429 RESOURCE_EXHAUSTED … quotaValue: '20' because the day's free requests were gone — three failures, none of them about the code under test.

### 5.2 - 💥 The fake that could not fail
`days/day-23-testing-tools-and-callbacks/parts/05-failure-lab/5.2-the-fake-that-could-not-fail.md` · level `production` · ids OPS-05, OPS-06

A plain dictionary standing in for ADK's State treats temp: and user: identically, so 'temp:raw_search' in fake.state is True while the same key survives the turn False — a test that is green about a value production throws away, and no error anywhere.

### 6.1 - Coverage is a map, not a score
`days/day-23-testing-tools-and-callbacks/parts/06-in-production/6.1-coverage-is-a-map-not-a-score.md` · level `production` · ids OPS-05

Twenty lines of ast say that 11 of Sutra's 25 public functions are named anywhere in tests/, and the useful part of that measurement is not the 44% — it is the list of the fourteen that are not, which turns out to be almost entirely main() and demo functions that nobody should be testing.

### 6.2 - The suite that has to stay fast
`days/day-23-testing-tools-and-callbacks/parts/06-in-production/6.2-the-suite-that-has-to-stay-fast.md` · level `production` · ids OPS-06

Sutra's whole suite runs in 6.02 seconds and its slowest test takes 0.02 — because from google.adk.agents import LlmAgent costs 5.74 seconds on its own, which means the suite's wall clock is almost entirely one import and speeding up the tests would change nothing.

## Papers - read after the parts

### doi:10.1145/1028664.1028765 - Mock roles, not objects
`days/day-23-testing-tools-and-callbacks/papers/01-mock-roles-not-objects.md`

Mock objects were being used as a way to avoid slow collaborators, and this paper argued they are really a design tool: you should double the role a collaborator plays in your own design — an interface you named and can change — and never a concrete class from somebody else's library.


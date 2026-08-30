# Day 15 — CHECKLIST

**IDs closed:** ADK-17
**Principles served:** 1, 2, 4, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18
**Parts:** 19 across 7 sections, plus 1 paper

> `./m done 15` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
cd days/day-15-toolsets-and-openapi/lab
uv run python vendor.py            # terminal 1; leave it running
# terminal 2:
cd days/day-15-toolsets-and-openapi/lab
uv run python how_often.py
uv run python filter_ignored.py
uv run python generated.py
uv run python arrived_empty.py
cd papers/implementing-remote-procedure-calls
SPEC=1 uv run python client.py
SPEC=0 uv run python client.py
cd -
uv run python -m pytest tests/test_toolsets.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: asks of `1, 1, 1, 3` against model calls of `1, 2, 3, 6`; a filter that changes nothing on
one crate and everything on the next; two tools generated from 691 characters of somebody else's
JSON; then the same question answered two opposite ways with no error text between them; then three
operations against two from byte-identical business code; then five passed and one skipped; then
`OK all green`, then `traceability: 27/199 closed, 0 problem(s)`, then one commit reading
`day 15: toolsets and openapi - tools you did not write - closes ADK-17`.

---

## Before you write anything

- [ ] `./m check` is green and `scripts/trace.py` shows Day 14's count before you change anything
- [ ] Copied `scripted.py` **and** `stateless.py` from Day 14's lab into today's, and can say why they
      are copied rather than imported across day folders
- [ ] Wrote `vendor.py` **before** anything else in section 4, and have it running in its own terminal
- [ ] Ran every lab script from **inside** `lab/`, and know why the bare imports need that
- [ ] Can say why all nineteen scripts cost nothing, and why today that sentence covers the *vendor*
      as well as the model

## Section 1 — what a crate is

- [ ] Ran `lab/shapes.py` and saw two entries on the list become three tools at the model (1.1)
- [ ] Can name the three kinds of thing `tools=[...]` accepts, and which one expands (1.1)
- [ ] Passed the class without brackets and read the `PydanticUserError` naming a class you never
      wrote (1.1)
- [ ] Passed `DeskTools().get_tools` instead and confirmed there is **no error at all** (1.1)
- [ ] Ran `lab/one_method.py` and read the `ImportError` from the obvious import path (1.2)
- [ ] Can say why `BaseTool` imports from `google.adk.tools` and `BaseToolset` does not (1.2)
- [ ] Can say which exception type to catch for a failing `from ... import ...`, and why (1.2)
- [ ] Left out `get_tools` and read the `TypeError` at **construction** (1.2)
- [ ] Ran `lab/by_context.py` and saw one dictionary key change what the model is offered (1.3)
- [ ] Dropped the `is not None` guard and confirmed it fails **outside** a run and not inside one (1.3)
- [ ] Can name the three things on the context it is safe to decide an inventory from, and the one
      that must never decide one (1.3)

## ADK-17 — when the crate is asked (section 2)

- [ ] Ran `lab/the_wrapper.py` and read cases **b** and **c** against each other (2.1)
- [ ] Can say which method the agent calls, and what happens to your list after your `return` (2.1)
- [ ] Confirmed `@final` is not enforced at run time, and can say what an override silently loses (2.1)
- [ ] Ran `lab/how_often.py` and recorded **your** four ask counts (2.2)
- [ ] Can say why a tool that writes session state cannot unlock another tool in the same run (2.2)
- [ ] Recorded whether your machine gives `1, 1, 1, 3` (2.2, `TODO(me)` if it does not)
- [ ] Ran `lab/prefixed.py` and saw two tools with one name, resolved without complaint (2.3)
- [ ] Drove a run with two colliding crates and read the `WARNING:root:` duplicate-name line (2.3)
- [ ] Can say which of two colliding tools the model reaches, and which line in your file decides it
      (2.3)

## Section 3 — the filter

- [ ] Ran `lab/filter_ignored.py` and confirmed cases **a** and **b** are identical (3.1)
- [ ] Can say, in one sentence, what `tool_filter` does on a crate whose `get_tools` ignores it (3.1)
- [ ] Printed `crate.tool_filter` on the naive crate and sat with what that line means (3.1)
- [ ] Ran `lab/names_or_rule.py` and read the `[]` row against the `[""]` row (3.2)
- [ ] Confirmed a `set` and a `tuple` both reject **every** tool, with no error (3.2)
- [ ] Can say which failure direction a list has and which a predicate has, and which you prefer (3.2)
- [ ] Wrote the three-line constructor guard that refuses an empty allowlist (3.2)

## Section 4 — the crate a machine packs

- [ ] Read `vendor.py`'s spec and found the four things a tool needs in it (4.1)
- [ ] Fetched `/openapi.json` with `curl` and can say why `/openapi.json` is a convention, not a rule
      (4.1)
- [ ] Fed the parser something that is not JSON and read `Expecting value: line 1 column 1 (char 0)`
      (4.1)
- [ ] Confirmed a spec with no `paths` generates **zero tools and no error** (4.1)
- [ ] Ran `lab/generated.py` and made a real HTTP call from code nobody wrote (4.2)
- [ ] Ran `lab/generated_agent.py` and watched an agent call a generated tool (4.2)
- [ ] Read the `CALL` line and can say what happened to the argument the tool does not declare (4.2)
- [ ] Stopped the service and read `httpx.ConnectError: All connection attempts failed` — and noticed
      what it does **not** name (4.2)
- [ ] Ran `lab/provenance.py` and can point at the spec field each tool field came from (4.3)
- [ ] Deleted `/status`'s `description` and watched the fallback happen (4.3)
- [ ] Can say what `servers[0]` means for an agent whose vendor lists staging first (4.3)
- [ ] Ran `lab/no_operation_id.py` and can say what `/incidents` became, and why the method is last
      (4.4)
- [ ] Found the sixty-character truncation and the word it cut in half (4.4)
- [ ] Added `"operationId": ""` and confirmed it behaves differently from a missing one (4.4)
- [ ] Ran `lab/one_key.py` and saw one credential reach both tools (4.5)
- [ ] Ran it again with `ACME_API_KEY` set to something else and confirmed only the header changed
      (4.5)
- [ ] Removed `auth_scheme` while keeping `auth_credential`, and predicted the result first (4.5)
- [ ] Read the 401 result and can say why Day 13's and Day 14's error doors never fire for it (4.5)
- [ ] Can name the four causes of a 401 that produce the same message (4.5)
- [ ] Confirmed no lab script prints a key, and can say why that is a rule and not a preference (4.5)

## Section 5 — where it bites

- [ ] Ran `lab/which_description.py` and read row one (5.1)
- [ ] Can say which of `summary` and `description` the model receives, and which document told you
      wrong (5.1)
- [ ] Ran `lab/drifted.py` and watched two crates agree and then stop agreeing (5.2)
- [ ] Moved the `OpenAPIToolset(...)` line after the change and confirmed they agree again (5.2)
- [ ] Can name the exact line in your own code where a vendor's document is frozen (5.2)
- [ ] Decided where AcmeCloud's spec comes from, and wrote down the failure you are accepting
      (5.2, `TODO(me)`)

## 💥 Failure lab (section 6)

- [ ] Ran `lab/arrived_empty.py` and read the two answers side by side
- [ ] Confirmed there is **one** line of evidence for the whole incident, and that it is a `WARNING`
- [ ] Can say why Day 14's `ReactiveModel` would have produced a *different* bug, and why `Honest`
      was needed
- [ ] Deleted `logging.basicConfig` and confirmed the two runs then differ only in one sentence
- [ ] Can say why the ledger from Day 14 records this run as successful
- [ ] Can name the signal that would actually have caught it, and say where that signal already exists
- [ ] Decided what the desk's instruction should say when its vendor tool is missing
      (6.1, `TODO(me)`)

## Section 7 — in production

- [ ] Ran `lab/wrappers.py` and read the top three rows against the bottom four (7.1)
- [ ] Can name the two adapter classes, what each is for, and the one-sentence reason Sutra has
      neither (7.1)
- [ ] Read `crewai_tool.py`'s friendlier error and can say why its instruction must not be run as
      printed (7.1)
- [ ] Can name the four `BaseToolset` subclasses that ship, and which phase brings each one (7.1)
- [ ] Wrote `tests/scripted.py` and `tests/test_toolsets.py`, and watched the suite go **RED** before
      writing `sutra/toolsets.py`
- [ ] Test 1 green: the desk crate offers all three tools unfiltered
- [ ] Test 2 green: the desk crate actually applies its filter
- [ ] Test 3 green: the vendor crate never offers the operation you excluded
- [ ] Test 4 green: the prefix reaches the declaration the model reads
- [ ] Test 5 green: a raising crate leaves the agent with no tools **and** the run still answers
- [ ] **Broke it on purpose:** deleted the `_is_tool_selected` line, watched **one** test go red, fixed it
- [ ] **Broke it on purpose:** deleted the `tool_name_prefix` default, watched **two** go red, fixed it
- [ ] **Broke it on purpose:** deleted the `tool_filter` default, watched **two** go red, fixed it
- [ ] **Broke it on purpose:** resolved through `get_tools()` in the helper, watched **four of five
      stay green**, and can say what that proves about a naive suite
- [ ] Left the sixth test skipped with its `TODO(me)`, and wrote down the trigger that un-skips it
      (7.2, `TODO(me)`)
- [ ] Can say why the sixth test cannot be a unit test
- [ ] Answered the three trust questions about `VendorToolset` and wrote them into the module
      docstring (7.3, `TODO(me)`)
- [ ] Can say what you stopped reviewing and the two things you must start reviewing instead (7.3)

## The paper — read after the parts

- [ ] Read [`papers/01-implementing-remote-procedure-calls.md`](papers/01-implementing-remote-procedure-calls.md)
      **after** finishing section 7, and can say why that order is Principle 4
- [ ] Built the two-file demo and ran it with `SPEC=1` and `SPEC=0`
- [ ] Confirmed the two shared operations return **byte-identical** results in both runs
- [ ] Can say what the ablation switch proves that a single run does not
- [ ] Added a fourth operation to `service.py` and confirmed only one of the two runs finds it
- [ ] Deleted `url=url` from the lambda and explained the result **before** looking
- [ ] Can define *stub*, *marshalling*, *binding* and *transparency* in plain words
- [ ] Can name which half of the paper survived and which half the field dropped
- [ ] Can connect *transparency* to 4.5's swallowed 401 and to 6.1's silence, in one sentence

## The build

- [ ] `sutra/toolsets.py` exists **at the package root**, beside `plugins.py`, and you can defend that
      path in one sentence
- [ ] `DeskToolset.get_tools` ends with the `_is_tool_selected` comprehension
- [ ] `VENDOR_ALLOWED` is a named module constant holding **generated** names, not `operationId`s
- [ ] `VendorToolset` sets both defaults with `setdefault`, so a caller can still narrow them
- [ ] The module docstring carries both a `Layer:` and a `Trust:` paragraph
- [ ] `tests/scripted.py` exists and `tests/test_toolsets.py` imports from it, not from a day folder
- [ ] `sutra/desk/` is **unchanged** — confirmed with `git diff`
- [ ] `sutra/plugins.py` is **unchanged** — confirmed with `git diff`

## Budget & gate

- [ ] Total model calls today: **0 of 20** — and you can say why the day needed none, including the
      vendor
- [ ] If you spent the optional request, you recorded whether the model chose the generated tool
- [ ] `uv run ruff check .` clean
- [ ] `uv run ruff format --check .` clean
- [ ] `uv run python -m pytest -q -m "not live"` green
- [ ] `./m depth 15` green
- [ ] `./m check` prints `OK all green`

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended with the **date and hash you actually observed**:
      `| 15 | <date> | ADK-17 | 19 (+1 paper) | <hash> | ✅ |`
- [ ] `docs/PACKAGES.md` — no new rows, **unless** your ask counts disagree with the day, in which
      case you added the row
- [ ] `docs/PAPERS.md` — the `doi:10.1145/2080.357392` row is present, and the title in it was copied
      from the record rather than typed from memory
- [ ] `docs/SKILL_PROVENANCE.md` — no new rows
- [ ] `git status` shows no `.env`
- [ ] Committed: `day 15: toolsets and openapi - tools you did not write - closes ADK-17`
- [ ] `uv run python scripts/trace.py` shows ADK-17 closed and `0 problem(s)`

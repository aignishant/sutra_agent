---
day: 15
phase: 2
phase_name: "Models & tools"
title: "Toolsets and OpenAPI — tools you did not write"
ids: ["ADK-17"]
principles: [1, 2, 4, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-08-30"
status: written
lab_scaffolded: false
commit: ""
---

# Day 15 — Toolsets and OpenAPI: tools you did not write

> **Yesterday (Day 14):** plugins — one object attached to the application, covering every agent in
> it, including the ones nobody has written yet. The coverage that made plugins worth having was also
> what let one line break an agent you were not thinking about.
> **Today:** the same move, one layer down and pointed outwards. A **toolset** is one entry on an
> agent's `tools` list that ADK *asks* for its contents, so an agent can hold tools that did not exist
> when it was built — including tools generated from a document a vendor published and you never read.
> **Tomorrow (Day 16):** built-in tools with brakes — search grounding and code execution, where the
> tools arrive already made by Google and the containment story is the whole subject.

---

## §1 Where we are

A shop that stopped making everything on the premises.

For two years everything on the shelves was made in the back room. You knew every item, because you
made every item: if something was wrong with it, there were four things it could have been and you
had handled all four. It worked, and it did not scale — the fourth product took as long as the first,
and the fortieth was never going to happen.

So now a van comes on Tuesdays. It brings a crate, and taped to the crate is a delivery note listing
what is inside: names, quantities, a line of description each. You do not open every box and count.
You read the note, put things on shelves, and the shop carries forty products instead of four.

Three things changed and none of them is "it got easier". You now trust a note written by somebody
else. You find out what is in the crate at the moment it arrives, not when you planned the week. And
on the Tuesday the van comes with an empty crate and a correct-looking note, the shelves are bare and
nothing rings a bell — the shop opens, the till works, and the first person to notice is a customer
who wanted the thing that is not there.

That is the day. Sections 1 to 3 are what a crate is and how it is opened, section 4 is the crate a
machine packs from the vendor's own note, sections 5 and 6 are what it costs you, and section 7 is
what you review once you have stopped reviewing code.

Four things worth knowing before you start.

**A `tools` list is not a list of tools.** It holds three different kinds of thing, and one of them
expands. One entry can become forty, and the moment it expands is not the moment you wrote it.

**The dynamism is in the base class, not in the generated crate.** `OpenAPIToolset` parses its
document in its constructor and never looks again, which makes it the one toolset whose answer cannot
change. Section 5 measures that.

**The filter is not applied for you.** `tool_filter` is accepted by every toolset's constructor and
honoured by exactly the ones that remember to honour it. Set it on a crate you wrote and forget one
line, and it is stored, readable, correct, and doing nothing.

**And today's failure lab is the day's own promise turned over.** A crate that cannot answer does not
raise. It contributes zero tools, logs one `WARNING`, and the agent answers the customer confidently
and wrongly. Everything you built on Days 13 and 14 to notice failures sees a clean run.

---

## §2 The map

Nineteen parts in seven sections, and **one paper**. The day climbs
`foundation → working → production`: section 1 is what a crate is, section 2 is when it is asked,
section 3 is the filter, section 4 is the crate generated from a vendor's document, sections 5 and 6
are where it bites, and section 7 is what you review instead of code.

**Read the paper last.** Generating a caller from an interface description was proposed in 1984, and
*Implementing remote procedure calls* (`doi:10.1145/2080.357392`) is where the vocabulary — stub,
marshalling, binding — comes from, along with the one idea the field decided was a mistake. Principle
4 at the scale of a day: build the mechanism first, then read the proposal.

### Section 1 — `01-crate-not-list`: what a toolset is, and the two ways to hold it wrong

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [One line, many tools](parts/01-crate-not-list/1.1-one-line-many-tools.md) | Two entries on the list, three tools at the model, and where the crate opened | `foundation` |
| 1.2 | [One method, and an import that is not where you would look](parts/01-crate-not-list/1.2-one-method-and-the-import.md) | The one abstract method, and the import that fails from the obvious path | `working` |
| 1.3 | [What the crate is allowed to see](parts/01-crate-not-list/1.3-what-the-crate-can-see.md) | One key in a dictionary, and the model is offered a different set of tools | `working` |

### Section 2 — `02-when-asked`: the moment the crate is opened

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The wrapper ADK actually calls](parts/02-when-asked/2.1-the-wrapper-adk-actually-calls.md) | Your method is not the one the agent calls, and your test may know it | `working` |
| 2.2 | [Asked once a run, not once a turn](parts/02-when-asked/2.2-asked-once-a-run.md) | Model calls 1, 2, 3, 6 — and asks 1, 1, 1, 3 | `production` |
| 2.3 | [Two crates, one name](parts/02-when-asked/2.3-two-crates-one-name.md) | The same tool name twice, and which of the two the model reaches | `working` |

### Section 3 — `03-the-filter`: an allowlist that only works if you apply it

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A filter you are given, and have to apply yourself](parts/03-the-filter/3.1-a-filter-you-have-to-apply-yourself.md) | The filter is set, the helper says no, and the agent calls it anyway | `production` |
| 3.2 | [A list of names, or a question](parts/03-the-filter/3.2-a-list-of-names-or-a-question.md) | Seven filters, four surprises, and `[]` against `[""]` | `working` |

### Section 4 — `04-machine-packed`: the crate a machine packs from the vendor's note

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The manual the service publishes about itself](parts/04-machine-packed/4.1-the-manual-the-service-publishes.md) | What an OpenAPI description is, and the four things a tool needs | `foundation` |
| 4.2 | [Spec in, tools out](parts/04-machine-packed/4.2-spec-in-tools-out.md) | 691 characters of somebody else's JSON, and two working tools | `working` |
| 4.3 | [Where each part of a generated tool comes from](parts/04-machine-packed/4.3-where-each-part-of-a-tool-comes-from.md) | Day 4's translation table, with a machine doing the typing | `working` |
| 4.4 | [The name you did not choose](parts/04-machine-packed/4.4-the-name-you-did-not-choose.md) | `incidents_get`, and a name cut off mid-word at sixty characters | `working` |
| 4.5 | [One key for the whole crate](parts/04-machine-packed/4.5-one-key-for-the-whole-crate.md) | Two constructor arguments, forty authenticated tools, one blast radius | `production` |

### Section 5 — `05-where-it-bites`: two things that are not what you were told

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The page and the package disagree](parts/05-where-it-bites/5.1-the-page-and-the-package-disagree.md) | Which of `summary` and `description` the model actually reads | `production` |
| 5.2 | [A crate that never changes its mind](parts/05-where-it-bites/5.2-a-crate-that-never-changes-its-mind.md) | The one toolset whose answer is frozen, and the line that freezes it | `production` |

### Section 6 — `06-failure-lab`: the deliberate failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The crate that arrived empty](parts/06-failure-lab/6.1-the-crate-that-arrived-empty.md) | A confident wrong answer, one `WARNING`, and nothing else at all | `production` |

### Section 7 — `07-in-production`: what you install, what you test, what you review

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [The wrappers we are not installing](parts/07-in-production/7.1-the-wrappers-we-are-not-installing.md) | Two adapters, four crates, and why 🅿️ is an answer | `production` |
| 7.2 | [Testing a toolset without a model](parts/07-in-production/7.2-testing-a-toolset-without-a-model.md) | Five assertions, no key, and the one that catches section 6 | `production` |
| 7.3 | [Where trust moved](parts/07-in-production/7.3-where-trust-moved.md) | What you stopped reviewing, and the two things you must start | `production` |

### The paper — read it after the parts

| # | Paper | What it settles | Level |
| --- | --- | --- | --- |
| 01 | [Implementing remote procedure calls](papers/01-implementing-remote-procedure-calls.md) · `doi:10.1145/2080.357392` | Where stub generation came from, and the one idea the field dropped | `production` |

---

## §3 Setup — run this

**No new packages today.** `google-adk` 2.7.1 carries the whole day. `httpx` and `pyyaml` are already
installed as its dependencies, and the stub services are written with the standard library, so nothing
is added and nothing goes over a network you do not own.

```bash
# 1 - confirm where you are starting from
./m check

# 2 - today's lab
mkdir -p days/day-15-toolsets-and-openapi/lab/papers/implementing-remote-procedure-calls
cd days/day-15-toolsets-and-openapi/lab

# yesterday's two test doubles - copy them, do not import across day folders
cp ../../day-14-plugins-one-layer-up/lab/scripted.py .
cp ../../day-14-plugins-one-layer-up/lab/stateless.py .

# section 1
touch shapes.py one_method.py by_context.py
# section 2
touch the_wrapper.py how_often.py prefixed.py
# section 3
touch filter_ignored.py names_or_rule.py
# section 4 - vendor.py FIRST; four scripts talk to it
touch vendor.py generated.py generated_agent.py provenance.py no_operation_id.py
touch echo.py one_key.py
# section 5
touch which_description.py drifted.py
# section 6
touch arrived_empty.py
# section 7
touch wrappers.py
# the paper's demo - no ADK, no model, two files
touch papers/implementing-remote-procedure-calls/service.py
touch papers/implementing-remote-procedure-calls/client.py
cd -

# 3 - what changes under sutra/ today
ls sutra/                    # toolsets.py is new, at the package root and not under desk/
ls tests/                    # scripted.py is new; test_toolsets.py is the eval
```

**Every lab script runs from inside `lab/`**, because they import `scripted`, `stateless`, `vendor`
and `echo` by bare name and that only resolves when `lab/` is the working directory:

```bash
cd days/day-15-toolsets-and-openapi/lab && uv run python shapes.py
```

**Write `vendor.py` before anything in section 4.** It is given complete in
[part 4.1](parts/04-machine-packed/4.1-the-manual-the-service-publishes.md), it is a stdlib HTTP
server playing a fictional vendor called AcmeCloud, and it publishes an OpenAPI description of itself
at `/openapi.json`. Four scripts talk to it, and **it needs its own terminal** — the one running it is
blocked.

**Then run `how_often.py` early**, before you have built anything on an assumption about when a crate
is opened. It is the number the whole of section 2 turns on, and it is not the number most people
guess.

**`sutra/toolsets.py` is new and lives at the package root**, beside `sutra/plugins.py` from
yesterday, not under `sutra/desk/`. That placement is the day's argument written as a file path: a
crate decides which tools exist for whoever holds it, and that is not one agent's business.

---

## §4 Build brief

**`sutra/toolsets.py`** — new, at the package root:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `DESK_TOOLS` | the desk's three tools as a list, so the crate has one source | 1.1 |
| `VENDOR_ALLOWED` | the allowlist, as a named module constant a reviewer can grep for | 3.2, 7.3 |
| `DeskToolset` | the desk's own crate — and the one line that makes its filter real | 1.1, 3.1 |
| `DeskToolset.NAME` | the registered name, as a class attribute | 1.3 |
| `VendorToolset` | a five-line `OpenAPIToolset` subclass, so a failure names the vendor | 4.2, 6.1 |
| the module docstring | `Layer:` and `Trust:` — which layer this is, and what was vouched for | 7.3 |

Two things in that table are the whole design. `DeskToolset.get_tools` ends with a comprehension over
`self._is_tool_selected`, because a filter nobody applies is a sign with no camera. And
`VendorToolset` exists almost entirely to have a **class name**, because the only evidence you get
when a crate fails is a log line naming its class.

**`tests/scripted.py`** — new. Day 14 left a `TODO(me)` asking where the shared test double should
live once a second day needed it in `tests/`. This is that day: `ReactiveModel` moves out of a lab
folder, because `tests/test_toolsets.py` must not import from a day folder.

**`tests/test_toolsets.py`** — see §5.

**Nothing under `sutra/desk/` changes today**, and nothing in `sutra/plugins.py` does either. Confirm
with `git diff` before you commit.

**`days/day-15-toolsets-and-openapi/lab/`** — nineteen scripts plus two copied doubles, and the
paper's two-file demo. **All of them cost zero requests.**

**`TODO(me)` markers left for you:**

- **7.3** — answer the three trust questions about `VendorToolset` and write them into the module
  docstring: who wrote what the model reads, what the worst operation in the spec is, and what tells
  you when either changes. The third one is the one with no answer yet.
- **5.2** — decide where AcmeCloud's spec comes from: fetched at start-up, pinned in the repository,
  or rebuilt periodically. Write down the answer and the failure you are accepting. All three are
  defensible; not choosing is not.
- **7.2** — the sixth test is skipped on purpose. Write down the **trigger** that un-skips it, and
  note that it cannot be a unit test, because it needs the network and it needs to run when nobody is
  deploying.
- **3.2** — Sutra's allowlist is a list of names today. Decide whether it should be a predicate
  instead, and write down what would have to be true for that to be the better answer. It is a
  question about who adds operations, not about Python.
- **6.1** — decide what the desk's instruction should say when its vendor tool is missing. The agent
  currently guesses; the only layer that can turn a confident wrong answer into an honest one is the
  instruction, and it is one sentence.
- **1.3, 4.5** — 4.5's `header_provider` is the supported way to send a credential that changes at run
  time. Read its docstring in the installed package and write one sentence on what it would take to
  rotate AcmeCloud's key without restarting.

---

## §5 The eval that must be able to fail

One new file, five assertions and one deliberate skip, **no API key required**. It runs on a fresh
clone with no `.env` and makes no network call at all; the whole file with its walkthrough is
[part 7.2](parts/07-in-production/7.2-testing-a-toolset-without-a-model.md).

Yesterday's suite drove a real `Runner` because a plugin's behaviour is a fact about a whole run.
Today most of the subject is decided **before** any model is involved — which tools exist, what they
are called, which were filtered out — so four of the five assertions need no run at all. The fifth
does, because "the run still succeeds with no tools" is a claim about a run.

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_toolsets.py -q -m "not live"   # RED: sutra/toolsets.py is empty
# ... write the module from §4 ...
uv run python -m pytest tests/test_toolsets.py -q -m "not live"   # 5 passed, 1 skipped
```

Then break each one on purpose. These are **measured**, each applied on its own to a green suite:

| Break this | Which tests go red | What it is telling you |
| --- | --- | --- |
| delete the `_is_tool_selected` line in `DeskToolset` | 1 — `actually_applies_its_filter` | a filter that is stored and ignored (3.1) |
| delete the `tool_name_prefix` default | 2 — the vendor allowlist test and the declaration test | names are an interface (2.3) |
| delete the `tool_filter` default | 2 — the same two | an allowlist that is not applied (3.1) |
| resolve through `get_tools()` in the helper | 1 — the vendor allowlist test | you tested your method, not the agent's (2.1) |

Read the last row twice. Testing through your own method instead of ADK's leaves **four of five
green**, and the one that fails does so only because the names lose their prefix. That is the honest
measure of how little a naive suite notices.

**And one thing left undone deliberately.** The sixth test is `@pytest.mark.skip` with a `TODO(me)`,
because nothing in the file can check that the pinned spec still matches what the vendor publishes —
that needs the network. If the summary line ever reads `6 passed`, somebody deleted a `TODO(me)`
instead of doing it.

---

## §6 Request budget

**Free-tier Gemini**, 20 requests per day (`docs/PACKAGES.md`, 2026-08-25).

| What | Model calls |
| --- | --- |
| all nineteen lab scripts, all seven sections | **0** |
| the two stub services, and every HTTP call to them | **0** |
| the paper's demo, both `SPEC` settings | **0** |
| the whole test suite | **0** |
| the failure lab | **0** |
| **Total required** | **0 of 20** |

Five days at zero, and today's reason is a new one worth stating. The scripted model covers the model
side as it has since Day 13; what is new is that the *vendor* is also local. `vendor.py` and `echo.py`
are stdlib HTTP servers on `127.0.0.1`, so every claim in section 4 about generated tools making real
requests is demonstrated with real requests — real `httpx`, real headers, real status codes — against
a server whose source you can read. Nothing in this day is simulated except the model, and nothing in
this day is about the model.

**Optional, and worth one request if you have quota:** put `VendorToolset` on the real desk with
`vendor.py` running, and send one triage about a login failure to `gemini-3.7-flash`. The thing to
watch is whether the model calls the vendor tool at all — which is a fact about the description that
came out of the spec ([4.3](parts/04-machine-packed/4.3-where-each-part-of-a-tool-comes-from.md)) and
cannot be checked with a scripted model, because a scripted model calls what it is told to.

**Cost: $0.**

---

## §7 Traps

- **A class passed without brackets is silently wrapped as a tool.** `tools=[DeskTools]` resolves to a
  tool named `DeskTools`, and the crate's tools are gone. The error, when it comes, is a
  `PydanticUserError` naming a class you never wrote. (1.1)
- **Passing `crate.get_tools` instead of `crate` has no error at all** — the agent gets a tool called
  `get_tools` with no description, and none of the crate's tools. (1.1)
- **`from google.adk.tools import BaseToolset` raises `ImportError`.** Its sibling `BaseTool` is
  re-exported and it is not; the working path is `google.adk.tools.base_toolset`. It is not a version
  problem, and upgrading will not fix it. (1.2)
- **Every hook must be `async`, and `get_tools` must return `BaseTool` objects**, not bare functions.
  Wrap them in `FunctionTool(func=...)`. (1.1, 1.2)
- **Your own `__init__` must call `super().__init__(**kwargs)`** or `tool_filter` and
  `tool_name_prefix` stop existing. (1.2)
- **`readonly_context` can be `None`.** It never is inside a run, and always is when your test calls
  the crate directly. Guard with `is not None`. (1.3)
- **ADK calls `get_tools_with_prefix`, not your `get_tools`.** A test that calls your method tests
  your method — it cannot see the prefix or the cache. (2.1)
- **`@final` is not enforced at run time.** Override the wrapper and it runs, silently losing the
  cache and the prefix. (2.1)
- **`get_tools` is called once per run, not once per model call.** A crate whose inventory depends on
  session state reads that state as it was before the first model call, so a tool that writes state
  cannot unlock another tool in the same run. (2.2)
- **Two crates may offer the same tool name.** The later one shadows the earlier, the warning goes to
  the **root** logger, and which one wins is decided by the order of your `tools` list. (2.3)
- **`tool_filter` does nothing unless your `get_tools` calls `self._is_tool_selected`.** It is stored,
  it is readable, it is correct, and it is ignored. (3.1)
- **`tool_filter=[]` offers every tool; `tool_filter=[""]` offers none.** An allowlist built from an
  unset environment variable fails open. (3.1, 3.2)
- **A `set` or a `tuple` as `tool_filter` rejects every tool**, with no error, because
  `_is_tool_selected` tests for `list` specifically. (3.2)
- **`tool_filter` matches the *generated* name**, not the vendor's `operationId` and not the prefixed
  name. (3.2, 4.4)
- **`OpenAPIToolset` parses the spec in `__init__`.** It is the one toolset whose answer never
  changes, and a vendor's document can drift under it with nothing said. (5.2)
- **`servers[0]` wins, always.** A spec that lists staging first hands you an agent reading test data,
  and your tests will pass. (4.3)
- **The description comes from `description` first, then `summary`** — the opposite order to the one
  `adk.dev` states. Improving the wrong field changes nothing. (5.1)
- **A missing `operationId` gets one built from path and method**, so `/incidents` becomes
  `incidents_get`; a present-but-empty one raises `ValueError: Operation ID is missing`. (4.4)
- **Generated names are truncated to sixty characters, mid-word**, so two long operations from one
  spec can collide into one name. (4.4)
- **A generated tool catches its own HTTP error** and returns model-facing text inviting up to three
  retries. Nothing raises, so Day 13's and Day 14's error doors never fire and your ledger records a
  successful call. (4.5)
- **A toolset that raises contributes zero tools and does not stop the run.** One `WARNING`, naming
  the class and nothing else. This is the day's failure lab. (6.1)
- **A key in the spec's `servers` URL works perfectly and commits your secret.** (4.5)

---

## §8 Verify before you code

Fetched on **2026-08-30**, the day this was written:

- **`adk.dev/tools-custom/openapi-tools/`** — confirmed `OpenAPIToolset`, its `spec_str` /
  `spec_dict` / `spec_str_type` arguments, `auth_scheme` / `auth_credential`, and the documented
  import path `google.adk.tools.openapi_tool.openapi_spec_parser.openapi_toolset`. **This page states
  the description precedence as "the `summary` or `description`", which is the reverse of what the
  installed package does** — see [5.1](parts/05-where-it-bites/5.1-the-page-and-the-package-disagree.md).
- **`adk.dev/tools-custom/`** — confirmed the *Toolsets: Grouping and Dynamically Providing Tools*
  section, `BaseToolset`, and that a filter exists. The per-invocation caching of
  `get_tools_with_prefix` is **not** on the page; it is read from the installed package and measured
  in [2.2](parts/02-when-asked/2.2-asked-once-a-run.md).
- **The installed `google-adk` 2.7.1**, in `.venv/Lib/site-packages/google/adk/` — `base_toolset.py`,
  `openapi_tool/openapi_spec_parser/`, and `agents/llm_agent.py`. Every claim in this day about
  behaviour was run on this machine against this version, not read.
- **`spec.openapis.org/oas/latest.html`** — the OpenAPI Specification, revision **3.2.0**, published
  **19 September 2025**; the wording quoted for `summary`, `description` and `operationId` in
  [4.1](parts/04-machine-packed/4.1-the-manual-the-service-publishes.md) is from that revision.
- **`doi:10.1145/2080.357392`** — the record opened and the title copied from it, via the ACM Digital
  Library listing and the Semantic Scholar record for the same DOI. Row added to `docs/PAPERS.md`.

If your `google-adk` is not 2.7.1, run `no_operation_id.py`, `which_description.py` and `how_often.py`
before trusting a single number in this day — and if any of them disagrees, that is a Principle 14
moment: amend first, then write.

---

## §9 Say it in an interview

"Our agent needed a vendor's status API, and there were forty operations behind it. I did not
hand-write forty tools — ADK will generate them from the vendor's OpenAPI document, one tool per
operation, names from `operationId`, descriptions and argument schemas from the document. What I
learned doing it is that generation does not remove the reviewing, it moves it: I stopped vouching for
wrapper code and started vouching for a document and an endpoint, and those need different controls.
So the crate ships with an allowlist as a default rather than an option, the spec is pinned in our
repository so a change to it shows up as a diff somebody reads, and there is a test that asserts the
exact list of tool names the agent receives — resolved the way ADK resolves it, not through my own
method, because that distinction is the difference between testing the agent and testing myself. The
thing I would want anyone to know before they do this: when a toolset fails to load, ADK catches it,
logs one warning and gives the agent zero tools. The run succeeds. Ours told a customer the vendor was
healthy during the vendor's outage, and every error-handling mechanism we had saw a clean request. An
agent with no tools does not become cautious — it becomes a language model with an opinion."

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box ticked, `./m depth 15` green, `./m check` printing
`OK all green`, and — the part no script can check — you can answer the *out loud* question at the
end of each of the nineteen parts without scrolling up.

Not when a number of sittings has passed. When you could rebuild `sutra/toolsets.py` from memory and
defend both of its defaults.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 15 | <date> | ADK-17 | 19 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed today; `httpx` and `pyyaml` were
already present as `google-adk` dependencies.

One behavioural fact is worth a row **if your machine disagrees with this document**, because it is a
fact about a pinned dependency: the ask count `how_often.py` prints, if it is not `1, 1, 1, 3`.

**`docs/PAPERS.md`** — **one row, already added**, because the citation was verified while the day was
written rather than after it:

```text
| Implementing remote procedure calls | doi:10.1145/2080.357392 | 1984 | 2026-08-30 | 15 | `days/day-15-toolsets-and-openapi/papers/01-implementing-remote-procedure-calls.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR is required, and two decisions belong in the commit message: that
`sutra/toolsets.py` sits at the package root beside `plugins.py`, and where AcmeCloud's spec comes
from (§4's `TODO(me)`). **If your ADK version applies `tool_filter` for you, or `OpenAPIToolset` starts
re-reading its spec, stop and re-read Principle 14 before editing anything** — that is a behaviour
change in a pinned dependency, and the plan is amended first.

**Commit message:**

```text
day 15: toolsets and openapi - tools you did not write - closes ADK-17
```

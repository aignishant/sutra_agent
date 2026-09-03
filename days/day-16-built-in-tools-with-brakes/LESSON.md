---
day: 16
phase: 2
phase_name: "Models & tools"
title: "Built-in tools with brakes"
ids: ["ADK-18", "AG-07", "AG-32", "SEC-01"]
principles: [1, 2, 4, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 24
generated: "2026-09-03"
status: written
lab_scaffolded: false
commit: ""
---

# Day 16 — Built-in tools with brakes

> **Yesterday (Day 15):** toolsets — one entry on a `tools` list that ADK asks for its contents, so an
> agent can hold tools generated from a document a vendor published. The tools were still yours: your
> process made every request, with your key.
> **Today:** two capabilities that are not code at all. `google_search` and `BuiltInCodeExecutor` are
> switches: one line each, run on the provider's machines, and every question worth asking about them
> is about consequence rather than correctness. This closes **Phase 2**.
> **Tomorrow (Day 17):** session state in depth — prefixes, scopes and lifetimes, starting with the
> `temp:` key today's citations quietly travel through.

---

## §1 Where we are

The hire shop at the end of the industrial estate.

You have been making things with what is in your own toolbox: a drill you bought, a saw you know the
sound of, and when something goes wrong there are four things it could be and you have handled all
four. Then a job comes in that needs a floor sander, and nobody buys a floor sander.

So you hire one. It arrives on a trolley, enormous, with a guard bolted over the drum and a laminated
card cable-tied to the handle: what it must not be used on, what happens if it jams, and the number to
ring. There is a meter on the side that counts the hours you actually run it, and the deposit says what
the shop thinks of people who ignore the card.

The sander is better than anything in your toolbox and none of it is yours. You cannot open it. You
cannot fix it. You did not choose the guard, and the guard is not there for your convenience — it is
there because the shop has seen what this machine does to a hand. What you are actually responsible for
is narrower and harder than usual: where you point it, what you feed it, and what you do with the mess
it makes.

That is today. Two capabilities arrive as switches — search the live web, run generated code — and
neither of them is code you can read. Sections 1 to 4 are the search half: what a built-in is, the rule
that it cannot share an agent, the sources that come back with a grounded answer, and which of Sutra's
questions should be sent outside at all. Sections 5 and 6 are the code half: how an executor differs
from a tool, and the one field that decides whether model-written code runs on Google's machines or in
the process holding your keys. Section 7 breaks it on purpose, and section 8 is what you review when
there is no code to review.

Four things worth knowing before you start.

**A built-in tool is not a tool your process runs.** It is one line in the outgoing request —
`{"google_search":{}}` — and everything after that happens where you cannot see it. Your logs will show
one model call and nothing else.

**A built-in cannot share an agent with any other tool** on the Gemini API. ADK will not stop you, your
agent will construct, the request will go out, and the platform will refuse it. This is the rule that
turns Sutra into specialists a phase and a half early.

**A grounded answer that does not show its sources is a rumour with good grammar.** The citations come
back attached to the event, and if you do not read them off the event as it goes past, they are gone.

**And the day's real subject is the second switch.** `code_executor=` decides where code a model wrote
gets executed. Change one word and it runs in your process, with your `.env`, your repository and your
network position. Section 6 measures that, and then writes the rule down.

---

## §2 The map

Twenty-four parts in eight sections, and **one paper**. The day climbs
`foundation → working → production`: sections 1 to 4 are grounding, sections 5 and 6 are code
execution and its blast radius, section 7 is the deliberate failure, and section 8 is what review
looks like when there is no code.

**Read the paper last.** Handing the solving to an interpreter was proposed in 2022, and
*PAL: Program-aided Language Models* (`arXiv:2211.10435`) is where the split between decomposition and
solving comes from, along with the half of the proposal the field quietly dropped. Principle 4 at the
scale of a day: build the mechanism first, then read the proposal.

### Section 1 — `01-switched-on`: what a built-in tool actually is

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A power you switch on](parts/01-switched-on/1.1-a-power-you-switch-on.md) | Three ways Sutra gained a power, and who runs each | `foundation` |
| 1.2 | [An object with a placeholder name](parts/01-switched-on/1.2-an-object-with-a-placeholder-name.md) | A name and a description the model never reads | `working` |
| 1.3 | [The request that leaves your process](parts/01-switched-on/1.3-the-request-that-leaves-your-process.md) | `{"google_search":{}}`, and why your traces have a hole in them | `working` |

### Section 2 — `02-one-at-a-time`: the rule that a built-in cannot share

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [One built-in, and nothing else](parts/02-one-at-a-time/2.1-one-built-in-and-nothing-else.md) | The exclusivity rule, and which layer does not enforce it | `working` |
| 2.2 | [A flag that does not lift the wall](parts/02-one-at-a-time/2.2-a-flag-that-does-not-lift-the-wall.md) | `bypass_multi_tools_limit`, a hidden agent, and a renamed tool | `production` |
| 2.3 | [The specialist you write yourself](parts/02-one-at-a-time/2.3-the-specialist-you-write-yourself.md) | The referral pattern, and the argument that keeps the citations | `production` |

### Section 3 — `03-receipts`: the evidence that comes back with a grounded answer

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Where the sources are](parts/03-receipts/3.1-where-the-sources-are.md) | `grounding_metadata`, and how to tell "found nothing" from "never searched" | `working` |
| 3.2 | [The offsets are in bytes](parts/03-receipts/3.2-the-offsets-are-in-bytes.md) | One accented character, and a highlight that starts a letter late | `production` |
| 3.3 | [The receipt you must show](parts/03-receipts/3.3-the-receipt-you-must-show.md) | A display requirement, and why an empty heading is worse than silence | `production` |

### Section 4 — `04-newspaper-or-cabinet`: which questions go outside at all

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Two questions that sound the same](parts/04-newspaper-or-cabinet/4.1-two-questions-that-sound-the-same.md) | Grounding and retrieval, and where the truth lives | `foundation` |
| 4.2 | [Routing by where the truth lives](parts/04-newspaper-or-cabinet/4.2-routing-by-where-the-truth-lives.md) | Four axes, and the sentence that does the routing today | `working` |
| 4.3 | [The question that left the building](parts/04-newspaper-or-cabinet/4.3-the-question-that-left-the-building.md) | What a redactor still leaks, and what Sutra sends instead | `production` |
| 4.4 | [Two meters, one call](parts/04-newspaper-or-cabinet/4.4-two-meters-one-call.md) | Six grounded tickets a day, and which meter binds | `production` |

### Section 5 — `05-code-that-runs`: the second switch

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [An executor is not a tool](parts/05-code-that-runs/5.1-an-executor-is-not-a-tool.md) | Two fields, four combinations, and the one that builds quietly | `foundation` |
| 5.2 | [The executor that executes nothing](parts/05-code-that-runs/5.2-the-executor-that-executes-nothing.md) | `execute_code() -> None`, and where the sandbox actually is | `working` |
| 5.3 | [Reading the code and its output](parts/05-code-that-runs/5.3-reading-the-code-and-its-output.md) | The program, the outcome, the stdout — and the prose last | `working` |
| 5.4 | [The estimate and the measurement](parts/05-code-that-runs/5.4-the-estimate-and-the-measurement.md) | Why "be careful with arithmetic" is not a fix | `working` |

### Section 6 — `06-blast-radius`: where generated code runs

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The executor that runs it here](parts/06-blast-radius/6.1-the-executor-that-runs-it-here.md) | Five API keys, read by code the model wrote | `production` |
| 6.2 | [What a sandbox has to be](parts/06-blast-radius/6.2-what-a-sandbox-has-to-be.md) | Five denials, and which ones each executor enforces | `production` |
| 6.3 | [The rule Sutra writes down](parts/06-blast-radius/6.3-the-rule-sutra-writes-down.md) | SEC-01, and what turns a policy into a red build | `production` |

### Section 7 — `07-failure-lab`: the deliberate failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [💥 The spare that does not fit](parts/07-failure-lab/7.1-the-spare-that-does-not-fit.md) | The fallback that raises at the exact moment it is needed | `production` |

### Section 8 — `08-in-production`: what you test, what you park, what you review

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 8.1 | [Testing a built-in without spending a request](parts/08-in-production/8.1-testing-a-built-in-without-spending-a-request.md) | Seven assertions, no key, and four measured ways to go red | `production` |
| 8.2 | [The fallback we are not building yet](parts/08-in-production/8.2-the-fallback-we-are-not-building-yet.md) | The allowance re-checked, and what the MCP escape hatch would cost | `production` |
| 8.3 | [What you review now](parts/08-in-production/8.3-what-you-review-now.md) | Seven questions, and the boundary Phase 2 moved three times | `production` |

### The paper — read it after the parts

| # | Paper | What it settles | Level |
| --- | --- | --- | --- |
| 01 | [PAL: Program-aided Language Models](papers/01-program-aided-language-models.md) · `arXiv:2211.10435` | Where "let the interpreter solve it" came from, and what the field dropped | `production` |

---

## §3 Setup — run this

**No new packages today.** `google-adk` 2.7.1 carries both capabilities, and everything else in the day
is the standard library. The `mcp` package is **not** installed today either — the search fallback in
[8.2](parts/08-in-production/8.2-the-fallback-we-are-not-building-yet.md) is parked, and Phase 5 is
where the protocol is taught.

```bash
# 1 - confirm where you are starting from
./m check

# 2 - today's lab
mkdir -p days/day-16-built-in-tools-with-brakes/lab/papers/program-aided-language-models
cd days/day-16-built-in-tools-with-brakes/lab

# section 1
touch two_switches.py placeholder.py the_request.py
# section 2
touch the_wall.py bypass.py specialist.py
# section 3 - ground.py is the day's first script that spends a request
touch ground.py byte_offsets.py render_sources.py
# section 4
touch routing.py redact.py two_meters.py
# section 5 - compute.py spends requests too
touch executor_not_tool.py executes_nothing.py compute.py expected.py
# section 6
touch unsafe.py no_timeout.py
# section 7
touch swapped.py
# the paper's demo - two files, both arms
touch papers/program-aided-language-models/questions.py
touch papers/program-aided-language-models/pal.py
cd -

# 3 - what changes under sutra/ and tests/ today
ls sutra/                    # builtin_tools.py is new, at the package root
ls tests/                    # test_builtins.py is the eval
ls docs/adr/                 # ADR-0009 is yours to write (SEC-01)
```

**Every lab script runs from inside `lab/`**, the same rule as Day 15, and the paper's demo runs from
inside its own folder because it imports `questions` by bare name:

```bash
cd days/day-16-built-in-tools-with-brakes/lab && uv run python two_switches.py
```

**Three scripts spend requests and the rest cost nothing.** `ground.py` (§3.1), `compute.py` (§5.3) and
the paper's `pal.py` in both arms are the only things in this day that talk to a model. Run the
zero-cost ones first — there are eighteen of them, and they carry most of the day's findings.

**Run `unsafe.py` before you write the policy.** [6.3](parts/06-blast-radius/6.3-the-rule-sutra-writes-down.md)
asks you to write a rule down, and the rule is much easier to write after you have watched model-written
code print the names of every variable in your `.env`.

**`sutra/builtin_tools.py` is new and lives at the package root**, beside `plugins.py` and
`toolsets.py`. That placement is the day's argument as a file path: these are capabilities the whole
application can hold, and the containment story belongs to the application rather than to one agent.

---

## §4 Build brief

**`sutra/builtin_tools.py`** — new, at the package root:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `MODEL` | the pinned free-tier model string, named once | 1.1 |
| `RESEARCHER_DESCRIPTION` | the routing rule as a named constant a reviewer can grep for | 4.2 |
| `researcher` | the search specialist: `tools=[google_search]`, and nothing else | 2.3, 4.2 |
| `coder` | the compute specialist: a `code_executor`, and no tools at all | 5.1 |
| `referral()` | the `AgentTool` the desk holds, with propagation switched on | 2.3 |
| `sources(event)` | `(title, uri)` pairs read off an event's grounding metadata | 3.1 |
| `render_sources(meta)` | the citation block, empty when there is nothing to cite | 3.3 |
| the module docstring | `Blast radius:` and `Rules this module is under:` | 8.3 |

Two things in that table are the whole design. `researcher` holds one entry on purpose, because the
platform refuses an agent that holds a built-in and anything else
([2.1](parts/02-one-at-a-time/2.1-one-built-in-and-nothing-else.md)). And `referral()` passes
`propagate_grounding_metadata=True`, because that argument defaults to `False` and the default silently
throws away every source
([2.3](parts/02-one-at-a-time/2.3-the-specialist-you-write-yourself.md)).

**`tests/test_builtins.py`** — new. Seven assertions and one deliberate skip; see §5.

**`docs/adr/ADR-0009-code-execution-policy.md`** — new, and the first security decision in the
repository. The six numbered points are given in
[6.3](parts/06-blast-radius/6.3-the-rule-sutra-writes-down.md); wrapping them in the ADR shape —
context, decision, consequences — is yours.

**Nothing under `sutra/desk/` changes today.** The desk does not gain a built-in; it gains the option of
a referral, and whether to wire it in is one of the `TODO(me)` decisions below. Confirm with `git diff`
before you commit.

**`days/day-16-built-in-tools-with-brakes/lab/`** — eighteen scripts that cost nothing, three that spend
requests, and the paper's two-file demo.

**`TODO(me)` markers left for you:**

- **6.3** — write `ADR-0009`. The decision text is given; the *consequences* section is not. Name at
  least one thing Sutra can no longer do because of this rule, and one future day that will need an
  exception to it.
- **8.2** — the freshness check. Open the pricing page, read the grounding allowance **for your own
  model family**, and add a dated row to `docs/PACKAGES.md`. If the number differs from the one in
  §6, stop and read Principle 14 before writing any code.
- **2.3, 4.2** — decide whether `sutra/desk/agent.py` gets the referral today or in Phase 8. Both are
  defensible: wiring it in makes the desk useful now and triples its request cost per ticket
  ([4.4](parts/04-newspaper-or-cabinet/4.4-two-meters-one-call.md)). Write down which you chose and the
  cost you accepted.
- **4.3** — write the sentence Sutra sends outwards. Given a ticket, what exactly does the desk ask the
  researcher? Write three examples from your own synthetic tickets and check that none of them contains
  anything of the customer's.
- **7.1** — write down which of Sutra's agents can fail over to another provider and which cannot, and
  where that record will live so Day 70's quota router can read it. One table, four rows, and it stops
  Day 70 from routing an agent into a `ValueError`.
- **5.3, 5.4** — after running `compute.py`, decide what Sutra stores for a computational answer: the
  program, the outcome, the raw output, or all three. Write down what question you are keeping it to
  answer.
- **3.3** — once you have run `ground.py`, look at the actual `uri` values and decide what your
  interface will show as link text. Write one sentence on why.

---

## §5 The eval that must be able to fail

One new file, **seven assertions and one deliberate skip**, no API key and no network. The whole file
with its walkthrough is [8.1](parts/08-in-production/8.1-testing-a-built-in-without-spending-a-request.md).

Yesterday's suite could drive a whole run with a scripted model. Today's cannot: a built-in tool does
its work inside the platform, so a fake model has nothing to fake. What is left is better than it
sounds — every mistake this day is about is decided **before** the call, in the resolved tool list and
the outgoing request, and all of that is assertable for free.

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_builtins.py -q -m "not live"   # RED: no sutra/builtin_tools.py yet
# ... write the module from §4 ...
uv run python -m pytest tests/test_builtins.py -q -m "not live"   # 7 passed, 1 skipped
```

The first run fails at **collection** with `ModuleNotFoundError: No module named 'sutra.builtin_tools'`,
which is the most honest possible statement of "the feature does not exist yet".

Then break each thing on purpose. These were **measured**, each applied on its own to a green suite:

| Break this | Which tests go red | What it is telling you |
| --- | --- | --- |
| add a second tool to `researcher` | 2 — the exact-list test and the request test | the exclusivity rule (2.1) |
| drop `propagate_grounding_metadata=True` | 1 — the referral test | the citations die at the boundary (2.3) |
| set `description=""` on `researcher` | 1 — the referral test | a specialist nobody refers to (2.3) |
| import `UnsafeLocalCodeExecutor` in `sutra/` | 1 — the SEC-01 test | the policy is a test, not a memo (6.3) |

The last row is the one that makes today different from every day before it. It is the first check in
this repository whose job is to fail when somebody makes the system **less safe**, and it is three
lines of `rglob` and a string search.

**And one thing left undone deliberately.** The eighth test is `@pytest.mark.skip` with a `TODO(me)`,
because the one claim a keyless suite cannot check is that a grounded answer actually carries sources.
If the summary line ever reads `8 passed`, somebody deleted a `TODO(me)` instead of doing it.

---

## §6 Request budget

**Free-tier Gemini**, 20 requests per day on `gemini-3.7-flash` (`docs/PACKAGES.md`, 2026-08-25), and
from today a **second meter**: 5,000 grounding-with-Google-Search requests per month, shared across the
Gemini 3.x models (`ai.google.dev/gemini-api/docs/pricing`, read 2026-09-03).

| What | Model calls | Search requests |
| --- | --- | --- |
| eighteen lab scripts across sections 1, 2, 4, 5, 6, 7 | **0** | 0 |
| `ground.py` (§3.1) | **1** | 1–2 |
| `compute.py` (§5.3) | **1–3** | 0 |
| the paper's demo, `PAL=1` | **3** | 0 |
| the paper's demo, `PAL=0` | **3** | 0 |
| the whole test suite | **0** | 0 |
| **Total required** | **8–10 of 20** | **1–2 of 5,000** |

This is the first day since Day 9 that needs live calls, and the reason is structural rather than
stylistic: grounding and code execution happen inside the platform, so a scripted model cannot stand in
for either. Eighteen of the day's twenty-one lab scripts still cost nothing, and they carry the
exclusivity rule, the bypass rewrite, the byte offsets, the blast radius, the sandbox denials and the
failure lab.

**Watch the second meter as you go.** [4.4](parts/04-newspaper-or-cabinet/4.4-two-meters-one-call.md)
computes that the daily model quota binds roughly twenty-eight times sooner than the monthly search
allowance, so today's constraint is the same one it has always been — but the second meter now exists,
and Day 24's accounting has to count it.

**If you get a 429**, stop rather than retry. It is a **daily** ceiling
(`docs/PACKAGES.md`, 2026-08-25), the message does not say so, and the scripts in this day exit
non-zero rather than inventing an answer. The full error text is in
[7.1](parts/07-failure-lab/7.1-the-spare-that-does-not-fit.md).

**Cost: $0.**

---

## §7 Traps

- **`google_search` is an object, not a function.** `google_search()` raises
  `TypeError: 'GoogleSearchTool' object is not callable`. It is a module-level singleton, so anything you
  assign to it reaches every agent in the process. (1.1, 1.2)
- **The code executor is in a different package.** `from google.adk.tools import BuiltInCodeExecutor`
  raises `AttributeError`; it lives in `google.adk.code_executors`. (1.1)
- **The model never reads a built-in's name or description.** Rewriting them changes nothing, silently,
  because the tool contributes no function declaration at all. (1.2)
- **A built-in excludes every other tool in the same agent** on the Gemini API — and ADK does not
  enforce it. Your agent constructs, the request goes out, the platform refuses it. (2.1)
- **Built-ins do not ride in sub-agents**, except `GoogleSearchTool` and `VertexAiSearchTool` through the
  workaround. (2.1)
- **`bypass_multi_tools_limit=True` does not lift the rule.** It silently replaces your search tool with
  a hidden agent wrapped as a tool, renamed `google_search_agent`, with its own model call — and only
  when the `tools` list has more than one entry. (2.2)
- **`AgentTool.create()` is on the documentation page and not in the package.** In `google-adk` 2.7.1 it
  raises `AttributeError: type object 'AgentTool' has no attribute 'create'`. Use the constructor. (2.3)
- **`propagate_grounding_metadata` defaults to `False`**, so a specialist's citations are dropped at the
  handover — including on the composition ADK's own docstring recommends. (2.3)
- **An `AgentTool` takes its name and description from the agent.** An agent with no `description` is a
  tool nobody calls. (2.3)
- **Every field of `grounding_metadata` is optional.** Iterating one without `or []` is a `TypeError` in
  the middle of a call you already paid for. (3.1)
- **An empty source list and "the model did not search" look identical.** `web_search_queries` is what
  tells them apart. (3.1)
- **`segment.start_index` is a byte offset, not a string index.** Slicing a Python string with it is
  wrong by one position per non-ASCII character before the span, silently. (3.2)
- **The query is composed on the far side**, so no callback can inspect it before it goes. Redaction
  leaks anyway; send a composed question instead of a ticket. (4.3)
- **Grounding spends a second meter with a different period** — searches per month, not requests per
  day. (4.4)
- **An executor is not a tool.** `tools=[BuiltInCodeExecutor()]` raises three pydantic errors;
  `code_executor=google_search` raises one. Putting both built-ins on one agent raises **nothing**, and
  the platform refuses the call. (5.1)
- **`BuiltInCodeExecutor.execute_code()` returns `None`.** It runs nothing locally, and the flow skips
  every local knob — `error_retry_attempts` and `timeout_seconds` are ignored for it. (5.2)
- **The provider's sandbox has a fixed library set** — the SDK documents Python 3.10 or later with numpy
  and simpy — and a deadline you cannot set, reported as `OUTCOME_DEADLINE_EXCEEDED`. (5.2, 5.3)
- **The prose can disagree with the sandbox's output.** Print the program and the stdout, not just the
  answer. (5.3)
- **`UnsafeLocalCodeExecutor` runs `exec()` in a spawned child of your process**, which inherits your
  environment and your working directory: five API keys and the whole repository. (6.1)
- **Its `timeout_seconds` defaults to `None`**, so a model's accidental infinite loop hangs the agent for
  ever. (6.2)
- **`multiprocessing` uses `spawn`, so a lab script without `if __name__ == "__main__":` never returns.**
  (6.1)
- **Neither built-in survives a provider swap.** Both raise `ValueError: ... is not supported for model
  groq/...` — during the quota exhaustion that caused the swap. (7.1)
- **Catching that `ValueError` and continuing gives you an agent with no tools**, which does not become
  cautious. It becomes a language model with an opinion. (7.1, and Day 15's failure lab)

---

## §8 Verify before you code

Fetched on **2026-09-03**, the day this was written:

- **`adk.dev/grounding/google_search_grounding/`** — confirmed `from google.adk.tools import
  google_search`, that it is passed in `tools=`, and the structure of `groundingMetadata`:
  `groundingChunks` (pages with a title and a uri), `groundingSupports` (which sentence rests on which
  chunk, with `startIndex`/`endIndex`/`text`), and `searchEntryPoint` (pre-formatted HTML). The page
  states the display requirement in as many words: *"A critical part of using grounding is to correctly
  display the information, including citations and search suggestions, to the end-user."*
- **`adk.dev/tools/limitations/`** — confirmed the exclusivity rule, quoted verbatim in
  [2.1](parts/02-one-at-a-time/2.1-one-built-in-and-nothing-else.md); that it applies to Code Execution
  and Google Search on the Gemini API; that built-ins do not work in sub-agents with the two named
  exceptions; and both workarounds. **The page names `AgentTool.create()`, which does not exist in the
  installed `google-adk` 2.7.1** — see [2.3](parts/02-one-at-a-time/2.3-the-specialist-you-write-yourself.md).
- **`ai.google.dev/gemini-api/docs/pricing`** — the free tier includes **5,000 grounding-with-Google-Search
  requests per month, shared across the Gemini 3.x models**, then $14 per 1,000. The Gemini 2.5 family has
  a different arrangement on the same page. This is the Addendum 02 §5 freshness check for Day 16, and the
  allowance has **not** shrunk — so the search-MCP fallback stays parked
  ([8.2](parts/08-in-production/8.2-the-fallback-we-are-not-building-yet.md)).
- **`arxiv.org/abs/2211.10435`** — the record opened, the title copied from it, and the abstract read for
  the claim quoted in the paper part. The method details were read from the paper's full text. A row was
  added to `docs/PAPERS.md`.
- **The installed `google-adk` 2.7.1 and `google-genai` 2.19.0**, in `.venv/Lib/site-packages/` —
  `tools/google_search_tool.py`, `tools/google_search_agent_tool.py`, `tools/agent_tool.py`,
  `agents/llm_agent.py`, `code_executors/*.py`, `flows/llm_flows/_code_execution.py`, and the
  `GroundingMetadata`, `ExecutableCode`, `CodeExecutionResult` and `Outcome` types. **Every behavioural
  claim in this day was run on this machine against these versions**, not read.

If your `google-adk` is not 2.7.1, run `bypass.py`, `executes_nothing.py` and `swapped.py` before
trusting a number in this day — and if any of them disagrees, that is a Principle 14 moment: amend
first, then write.

---

## §9 Say it in an interview

"We gave our triage agent web search, and the one-line diff was the smallest part of the change. The
first thing we hit is that on the Gemini API a built-in tool cannot share an agent with any other tool —
and the framework does not stop you, so your agent builds fine and the platform refuses the call. That
pushed us into a researcher agent that holds search and nothing else, called from the desk as a tool,
which is where we were going architecturally anyway. Then the details that actually cost time: the
citations come back on the event, not in the text, and if you wrap the specialist as an agent-tool they
are dropped unless you turn propagation on, which is off by default. Grounding spends a second quota
nobody was watching — searches per month, next to requests per day — and our arithmetic said the daily
model quota binds about twenty-eight times sooner, so grounding could not be a step that runs on every
ticket. And the failure that taught us the most: our quota router failed the researcher over to another
provider during a Gemini exhaustion, and it raised, because a built-in is a platform capability and does
not travel with a model swap. Multi-provider fallback covers models. It does not cover the things that
are not models. On the code execution side we made one decision and wrote it down: generated code never
runs in a process holding our credentials. That is a policy with a test behind it, because we ran the
local executor once, on purpose, and watched model-written code print the names of every variable in our
`.env`."

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box ticked, `./m depth 16` green, `./m check` printing
`OK all green`, the Phase 2 freshness check done — and, the part no script can check, you can answer the
*out loud* question at the end of each of the twenty-four parts without scrolling up.

Not when a number of sittings has passed. When you can state SEC-01 from memory and say which test would
fail if somebody broke it.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 16 | <date> | ADK-18, AG-07, AG-32, SEC-01 | 24 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **one new row**, and it is a quota baseline rather than an install:

```text
| google_search grounding (allowance) | 5,000 requests/month free, shared across Gemini 3.x models, then $14 per 1,000 | <date> | 16 | The day's second meter (4.4). Read from ai.google.dev/gemini-api/docs/pricing; Addendum 02 flagged this allowance as volatile, so re-verify at every phase gate. |
```

**`docs/PAPERS.md`** — **one row, already added**, because the citation was verified while the day was
written rather than after it:

```text
| PAL: Program-aided Language Models | arXiv:2211.10435 | 2022 | 2026-09-03 | 16 | `days/day-16-built-in-tools-with-brakes/papers/01-program-aided-language-models.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — **one new ADR is required today**: `ADR-0009-code-execution-policy.md`, which is
SEC-01 ([6.3](parts/06-blast-radius/6.3-the-rule-sutra-writes-down.md)). It is the first security
decision in this repository and the first ADR whose enforcement is a test.

**This closes Phase 2**, so the phase gate runs before the commit (plan §15): the freshness check on
`google-adk` release notes since Day 5, on the MCP specification revision, and on all three providers'
free limits — you have dated baselines from Day 9 and from today to diff against. The gate itself is
*four free providers benchmarked; built-in tools contained*, and **contained** is the seven questions in
[8.3](parts/08-in-production/8.3-what-you-review-now.md).

**Commit message:**

```text
day 16: built-in tools with brakes - closes ADK-18, AG-07, AG-32, SEC-01
```

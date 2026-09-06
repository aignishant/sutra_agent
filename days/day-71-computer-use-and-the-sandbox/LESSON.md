---
day: 71
phase: 10
phase_name: "Safety and security"
title: "Computer use & the sandbox — browser agent vs a local dummy site; execution isolation in practice"
ids: ["AG-31", "SEC-14", "ADK-50"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: build
plan_version: "v2.2.1"
parts: 13
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 71 — Computer use and the sandbox

> **Yesterday (Day 70):** the quota router. Headroom per provider per window, a plugin on the Runner
> because routing is scheduling, and four ways your count and the provider's can disagree.
> **Today:** the last tool Sutra will ever be given, and the least like the others. Every tool so far
> has been an API — a function, an MCP server, a database. Today the agent gets a **browser**, looks
> at pixels, and moves a mouse. That is a capability with no natural boundary, so half this day is
> the capability and half is the box you put it in.
> **Tomorrow (Day 72):** backoff with honesty — `retry-after`, 1→2→4→8s, escalate after N, and never
> invent a result. Phase 10 closes there.

---

## §1 Where we are

Most of the world has no API.

The vendor whose outage is flooding your queue has a status page: an incident banner, a table of
components, a link to past incidents, and no JSON anywhere. Every tool this curriculum has built
reads structure — a function's arguments, an MCP server's schema, a database row. None of them can
read that page, and no amount of prompt engineering changes it.

**Computer use** closes the gap in the most literal way available: the model is shown a screenshot
and given a mouse. It is the last rung of a ladder — an API, then a feed, then an MCP server, then
scraping the HTML, and only then pixels — and it is on the ladder because sometimes the four rungs
above it are genuinely absent.

The whole day turns on one measurement. `current_state()` returns a screenshot and a URL and nothing
else, and the toolset declares **fifteen actions** to the model while the day's script uses **one**.
That gap is the subject: a sandbox has to have an answer for all fifteen, and the fifteen are chosen
by the framework rather than by you.

Two findings are worth knowing before you start, because both were surprises while this lab was
being written.

**ADK already ships a door on `navigate`**, and it is closed by default: any URL whose host is not
publicly routable is refused, which is a server-side request forgery guard. It is the reason this
lab's very first run failed against its own fixture on `127.0.0.1`.

**And the flag that opens it is a boolean.** Opting out to reach your own fixture also opens
`169.254.169.254` — the cloud metadata endpoint — and every admin panel on localhost. Measured: 0 of
3 targets reachable by default, 3 of 3 after the opt-out. The framework's guard is about *classes* of
address; the precision has to come from a door of your own.

⚠️ **Computer use is a Preview capability.** adk.dev says so, and the runtime prints
`[EXPERIMENTAL] feature FeatureName.COMPUTER_USE is enabled` on every run. Nothing in this day should
be read as production-ready on the framework's side.

---

## §2 The map

Four sections. Section 1 is why computer use exists and what the model actually receives. Section 2
is the loop that drives it, and the fixture it drives. Section 3 is the box — a door of your own, the
door the framework already shipped, and the awkward flag between them. Section 4 is what this is
worth, what it does not contain, and what you would buy instead.

### 1 — No API

*Why a browser agent exists, and how little it is given to work with.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The page with no JSON](parts/01-no-api/1.1-the-page-with-no-json.md) | The ladder from API to pixels, and why computer use is the last rung | `foundation` |
| 1.2 | [Pixels and a URL](parts/01-no-api/1.2-pixels-and-a-url.md) | `current_state()` returns two fields; 28,165 bytes of PNG is the whole input | `foundation` |
| 1.3 | [Fifteen doors, one used](parts/01-no-api/1.3-fifteen-doors-one-used.md) | 💥 The surface is what the runtime declares, not what your script uses | `working` |

### 2 — Driving it

*The loop, the coordinate space, and a site it is safe to point at.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [See, decide, act](parts/02-driving-it/2.1-see-decide-act.md) | Day 3's loop with a screenshot in place of a tool result | `foundation` |
| 2.2 | [The coordinates are not your pixels](parts/02-driving-it/2.2-the-coordinates-are-not-your-pixels.md) | 💥 A normalised space and a rescale, so `(120,300)` lands at `(153,280)` | `working` |
| 2.3 | [A site you own](parts/02-driving-it/2.3-a-site-you-own.md) | Three reasons the fixture is local, and only the first is the obvious one | `working` |

### 3 — The door

*Two layers, and the flag that is coarser than either.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The check outside every tool](parts/03-the-door/3.1-the-check-outside-every-tool.md) | One plugin on the Runner: 3 of 5 actions reach the browser instead of 5 | `working` |
| 3.2 | [The guard ADK already shipped](parts/03-the-door/3.2-the-guard-adk-already-shipped.md) | An SSRF guard on `navigate`, default-closed, that reports by logging | `production` |
| 3.3 | [All or nothing](parts/03-the-door/3.3-all-or-nothing.md) | 💥 The opt-out that reaches your fixture also reaches cloud metadata | `production` |
| 3.4 | [What a refusal leaves behind](parts/03-the-door/3.4-what-a-refusal-leaves-behind.md) | A sandbox that stops something and records nothing has told nobody | `production` |

### 4 — In production

*What the box does not contain, and what you would buy instead.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The action nobody enumerated](parts/04-in-production/4.1-the-action-nobody-enumerated.md) | 💥 An allowlist over actions is only as complete as the action list | `production` |
| 4.2 | [Isolation you can buy](parts/04-in-production/4.2-isolation-you-can-buy.md) | 🅿️ Hosted sandboxes, and the free layers that are real here | `production` |
| 4.3 | [What this is worth](parts/04-in-production/4.3-what-this-is-worth.md) | The honest accounting, in this day's own numbers | `production` |

### The paper — read it last

*Principle 4 at the scale of a day: build the door by hand, then read the design that says decide
before it runs, from rules small enough to audit.*

| # | Paper | What it answers |
| --- | --- | --- |
| 01 | [Native Client: A Sandbox for Portable, Untrusted x86 Native Code](papers/01-native-client.md) | `doi:10.1109/SP.2009.25` — validate ahead of execution against a small readable rule set, in two layers, and trust the validator rather than the code |

---

## §3 Setup — run this

**Today adds a package and a browser**, which is unusual for this curriculum and is the reason §8 has
two rows about it:

```bash
uv add "playwright==1.62.0"
uv run playwright install chromium
```

**What those two commands are:**

- `uv add` pins the version in `pyproject.toml` and writes the lock. The version came from
  `pypi.org/pypi/playwright/json` on the day it was installed, not from ADK's own sample, which pins
  an older one — Principle 7.
- `uv run playwright install chromium` is a **second, non-pip step** that downloads the browser
  (~115 MiB) outside the virtualenv. `uv sync` alone does not do it, so a fresh checkout has the
  package and no browser and fails at `chromium.launch()`. That trap is recorded in
  `docs/PACKAGES.md`.

Then the lab:

```bash
mkdir -p days/day-71-computer-use-and-the-sandbox/lab/site
mkdir -p days/day-71-computer-use-and-the-sandbox/lab/papers/native-client
cd days/day-71-computer-use-and-the-sandbox/lab
touch _site.py _computer.py _fake.py
touch look.py surface.py door.py guard.py gate.py
touch site/status.html site/history.html
touch papers/native-client/validator.py papers/native-client/demo.py
```

**What each file is for:**

- `site/` is the fixture: a status page with an incident banner and no API, and a history page behind
  a link. Two files, and part 2.3 is why they are local.
- `_site.py` serves them on port **8771** through a context manager, so no run leaves a port bound.
  Day 15's stub owns 8765.
- `_computer.py` is the `BaseComputer` — the thing the model is allowed to move. Read it first; every
  measurement in the day is a count over its `Trace`.
- `_fake.py` is a real `BaseLlm` that emits a scripted sequence of actions, which is what makes the
  browser real and the quota zero.
- `look.py`, `surface.py`, `door.py` and `guard.py` are the four measurements, one per section.
- `gate.py` is the eval.

Everything under `lab/` is gitignored repo-wide; check it before the first run:

```bash
git check-ignore -v days/day-71-computer-use-and-the-sandbox/lab/site/status.html
```

**Why:**

- The habit, and one real reason: a browser run writes caches and profile data, and none of it belongs
  in git (Principle 9). If this prints nothing, fix `.gitignore` first.

---

## §4 Build brief

**`sutra/browser_sandbox.py`** — the door, promoted out of the lab.

- `TODO(me)`: `BrowserSandbox(BasePlugin)` whose `before_tool_callback` is named
  `(self, tool, tool_args, tool_context)` — the runtime calls callbacks by keyword, which Day 67 part
  2.4 measured and this day's gate checks.
- `TODO(me)`: `ALLOWED_ORIGINS` as **data** — a tuple or a frozenset, not a chain of `if`s — so the
  policy can be diffed and reviewed. Day 68's permission table is the argument.
- `TODO(me)`: decide the default for an action name the sandbox has never heard of. `door.py` returns
  allow, and part 4.1 argues that is the wrong default; make your choice and defend it in the
  docstring.
- `TODO(me)`: a refusal that carries the rule, the origin and the run, so it is usable during an
  incident rather than only during the request — part 3.4.

**`tests/test_browser_sandbox.py`**

- `TODO(me)`: a test that an off-origin `navigate` is refused **and** that the refusal is recorded.
  Both halves, because part 3.4 is about the second one.
- `TODO(me)`: a test that an action name not in the allowlist is refused. That test is the one that
  fails when the framework adds a sixteenth action, which is exactly when you want to hear about it.

---

## §5 The eval that must be able to fail

```bash
cd days/day-71-computer-use-and-the-sandbox/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/browser_sandbox.py`, all red today because the module is the build brief. A
check that cannot run counts as a **failure** rather than as skipped, for the reason Day 69's gate
gives: a skipping check goes green on a repository where somebody deleted the module.

The red-alarm test — the one that can be driven red on demand — is the pair of arms in `door.py`:

```bash
uv run python door.py
uv run python door.py --open
```

The model plays the identical five-action script both times. With the door, 3 of 5 actions reach the
browser and the secret is never typed; without it, 5 of 5 reach and it is. If those two runs ever
agree, the sandbox has stopped sandboxing. A second ablation is `guard.py --opt-out`.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

This day is unusually easy to get wrong on budget, because a real computer-use loop is the most
expensive thing in this curriculum: it sends **an image per step**. So the model is the one simulated
component and everything else is real — a real Chromium, a real page over HTTP, a real
`BaseComputer`, a real `ComputerUseToolset`, a real `Runner`, real plugin hooks. `_fake.py`'s
`ScriptedActor` is a `BaseLlm` subclass, so the runtime treats it as a model in every respect and
receives the real `LlmRequest` — which is how part 1.3 reads the declared tool list off the request
rather than guessing it.

Nothing here reads a key from the environment or opens a socket to a provider. The only network
traffic is the browser talking to `127.0.0.1:8771`.

---

## §7 Traps

1. **Reaching for computer use first.** It is the last rung. An API, a feed, an MCP server or plain
   HTML scraping are all cheaper and more reliable where they exist — part 1.1.
2. **Assuming the model can see structure.** `current_state()` returns a screenshot and a URL. No DOM,
   no text layer, no accessibility tree — part 1.2.
3. **Sandboxing the actions your script uses.** Fifteen are declared and one was used; the box has to
   cover the first number — part 1.3.
4. **Implementing only the `BaseComputer` methods you need.** All of them are abstract, so the class
   cannot be instantiated at all, and the error arrives at construction rather than at the missing
   call — part 1.3.
5. **Writing a sandbox rule against raw pixel coordinates.** The model works in a normalised space
   and the framework rescales, so `(120,300)` becomes `(153,280)` — part 2.2.
6. **Pointing the agent at somebody else's live site.** Unreproducible, not yours to drive, and the
   blast radius is theirs — part 2.3.
7. **Putting the check inside one tool.** A surface of fifteen needs a plugin on the Runner, which is
   Day 68 part 4.4 and Day 70 part 3.1 applied to a browser — part 3.1.
8. **Not knowing the framework already has a door.** `navigate` refuses non-routable hosts by default
   and reports it by **logging a warning**, so a caller watching for exceptions sees nothing — part 3.2.
9. **Setting `allow_private_network_access=True` and forgetting.** It is a boolean, so reaching your
   own fixture also opens cloud metadata and localhost admin panels — part 3.3.
10. **A refusal that leaves no record.** The trace has to carry the refused action beside the permitted
    ones, or nobody learns what the box stopped — part 3.4.
11. **Allow-by-default over action names.** `door.py`'s `_verdict` returns allow for anything it has
    not heard of, which is the wrong default the day the framework adds an action — part 4.1.
12. **Mistaking the door for isolation.** It constrains what the agent may *ask for*; it does not
    contain what the browser *does* — part 4.2.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| Computer use status | <https://adk.dev/integrations/computer-use/> | *"The Computer Use model and tool is a Preview release."* The sample pins a 2.5-era model string, which this day does **not** use — nothing here calls a model at all |
| Plugin hook scope | <https://adk.dev/plugins/> | plugin hooks are global and registered once on the `Runner`; agent callbacks are local. The reason the sandbox is a plugin — part 3.1 |
| `playwright` latest | <https://pypi.org/pypi/playwright/json> | `1.62.0`, requires Python >=3.10. Pinned today; ADK's own sample pins 1.52.0 and was not copied (Principle 7) |
| `doi:10.1109/SP.2009.25` record | <https://api.crossref.org/works/10.1109/SP.2009.25> | title *Native Client: A Sandbox for Portable, Untrusted x86 Native Code*, IEEE S&P 2009, 79–93 — copied into `docs/PAPERS.md` and the paper document, never from memory (§17.4.1 rule 5) |
| `google-adk` latest | <https://pypi.org/pypi/google-adk/json> | `2.8.0`; this repo pins `2.7.1`, carried forward as the Day 65 freshness finding (Principle 14) |

Three behaviours were **measured or read in source** against the installed `2.7.1` rather than
assumed, and each part names where:

- `ComputerState` has exactly two fields, `screenshot: bytes` and `url: Optional[str]` — part 1.2.
- The toolset declares fifteen tools, read off `llm_request.tools_dict` — part 1.3.
- `navigate` is wrapped by an SSRF guard whose source is in
  `google/adk/tools/computer_use/computer_use_toolset.py` — part 3.2.

---

## §9 Say it in an interview

*"We gave an agent a browser, which is a different kind of decision from giving it an API, and the
day divided cleanly into the capability and the box. What the model actually gets is a screenshot and
a URL — no DOM, no text layer — so a status page with a banner and a table arrives as about 28
kilobytes of PNG and the model's whole job is to read it back out. The number that drove the design
was that the toolset declares fifteen actions to the model and our script used one: the sandbox has
to answer for fifteen, and the fifteen are the framework's list, not ours. So the door is a plugin on
the Runner rather than a check inside a tool, and it decides on things that don't require reading the
page — is this navigation on the permitted origin, does this typed text look like a credential. With
it, three of five scripted actions reached the browser and a synthetic secret was never typed;
without it, five of five and it was. Two things surprised me. ADK already ships an SSRF guard on
navigate that refuses non-routable hosts by default — it broke our own localhost fixture on the first
run, which is the right default doing its job. And the flag that opens it is a boolean, so opting out
to reach our fixture also opened the cloud metadata endpoint and any admin panel on localhost. That
is the argument for two layers: theirs is about classes of address, ours is about one origin, and
neither is sufficient alone."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have run the commands rather than read
them. `./m done 71` refuses to commit until they are.

The day is finished when you can name all fifteen declared actions without looking, say which of them
your door has an opinion about, and explain why the answer to the second question should worry you.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 71 | 2026-09-06 | AG-31, SEC-14, ADK-50 | 13 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth 71` is green over the thirteen parts and the paper.
`lab/gate.py` is **red** on all six checks by design — `sutra/browser_sandbox.py` is the build brief.
The repository-wide `⚠️` carried since Day 15 is unchanged: `tests/test_persona.py` still fails ruff
`I001`, and it is the learner's own file, which no generated day may edit.

**`docs/PACKAGES.md`** — one new row, the first in this phase:

```text
| playwright | 1.62.0 | 2026-09-06 | 71 | Browser automation behind Day 71's `BaseComputer`. Needs a second, non-pip step: `uv run playwright install chromium`, which `uv sync` does not do. |
```

The row in the ledger carries the full reasoning, including the PyPI lookup and why ADK's own 1.52.0
pin was not copied.

**`docs/PAPERS.md`** — one row, checked live today:

```text
| Native Client: A Sandbox for Portable, Untrusted x86 Native Code | doi:10.1109/SP.2009.25 | 2009 | 2026-09-06 | 71 | `days/day-71-computer-use-and-the-sandbox/papers/01-native-client.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 71: computer use and the sandbox - a browser agent in a box - closes AG-31, SEC-14, ADK-50
```

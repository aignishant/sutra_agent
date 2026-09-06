---
day: 87
phase: 13
phase_name: "Observability & deployment"
title: "Agent Engine — the config written, not billed"
ids: ["ADK-68"]
principles: [2, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 13
generated: "2026-09-07"
status: written
lab_scaffolded: true
commit: ""
---

# Day 87 — 🅿️ Agent Engine: the config written, not billed

> **Yesterday (Day 86):** the desk went into a container — stateless, its secrets injected from the
> environment rather than baked in, and a health check the container itself answers. The build
> context came to **414,219,769 bytes across 22,020 files** before a `.dockerignore` existed, this
> repository's own `.env` among them. Everything about where it runs was still this repository's
> decision.
> **Today:** the decision is handed over, on paper. A managed platform takes the process, the
> restarts, the scaling and the sessions, and gives back a resource name. This day writes the
> configuration for that, reviews it, checks it — and never types the deploy command, because the
> command is the only part that bills and the only part that teaches nothing. The findings are real:
> **five names for one product**, **nine of twenty-five deploy flags deprecated**, and a deploy path
> that reads your whole `.env` and ships every key in it.
> **Tomorrow (Day 88):** Kubernetes on the laptop — kind and k3d, and the MCP-sidecar pattern.

---

## §1 Where we are

The locker at the railway station.

You are carrying a heavy bag and you have errands to run. There is a counter that will take the bag,
give you a token, and keep it until evening. It costs a little and it is obviously worth it — and
what you have actually done is swap one problem for three smaller ones you no longer control. The
counter closes at a time printed on a board you did not read. The token is now the only thing
between you and your bag. The person who checks the closing time before handing the bag over is
reading the half of the deal that is not on the poster.

Phase 13 has so far kept everything. Day 84 configured the tracer. Day 85 served the desk from a
process this repository starts. Day 86 built the container and injected the secrets. Today is the
first time the answer to *where does it run* stops being ours.

The day is marked 🅿️ — **parked**, this curriculum's marker for awareness-level and deliberately not
built — and the marker is the subject as much as the platform is. The work splits cleanly: everything
that teaches judgement is free, and everything that costs money teaches that the command works. So
the configuration gets written, validated and argued with, and the deploy command appears exactly
once, as a `TODO(me)`, with the words *not run here — this one bills* beside it.

What that afternoon of free work found, in a library nobody had to pay to read:

**Five names for one product**, all live in `google-adk==2.7.1` on one day. The CLI subcommand is
`agent_engine`, the code it runs prints "Agent Platform", the documentation page is now "Agent
Runtime" with the old URL redirecting, the config file keeps `agent_engine_config`, and the resource
path says `reasoningEngines`. Every one is correct in its own place.

**Nine of twenty-five deploy options are deprecated in their own help text.** Six of the nine are not
features being withdrawn — they are decisions the platform took back, which is the whole trade
visible in a help page.

**Your `.env` travels whole.** Three lines in ADK's deploy path find the file beside the agent, parse
every key with `dotenv_values`, and assign the lot into the config that gets uploaded. The one file
this repository has kept out of git since Day 0, because it holds secrets, is the file that is
uploaded without inspection. Principle 9 was fully satisfied and the credentials still left the
building.

And the day's own check, which is where the parked marker stops being decorative: a scan for anything
that needs a billing account. Its first implementation reported eleven findings, every one of them a
mention in this day's own documentation — including five that were the scanner's own list of things
to look for.

---

## §2 The map

Five sections. Section 1 is the trade and why the day is parked. Section 2 is the config file, which
is the artefact everything else acts on. Section 3 is checking it without deploying. Section 4 is
what it would cost and what attaches itself to you. Section 5 is the failure nobody tests and the
list that makes "we did not deploy" defensible.

### 1 — What you hand over

*The trade, the marker, and the twenty-five options.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [What you hand over when you hand it over](parts/01-what-you-hand-over/1.1-what-you-hand-over.md) | Five things that stop being your decision, and five names for one product | `foundation` |
| 1.2 | [🅿️ Why this day is parked](parts/01-what-you-hand-over/1.2-why-this-day-is-parked.md) | What the marker promises, and the two ways parked goes wrong | `foundation` |
| 1.3 | [Reading the deploy surface](parts/01-what-you-hand-over/1.3-reading-the-deploy-surface.md) | Nine deprecated flags, and the one whose default is a laptop | `working` |

### 2 — The config is the artefact

*What ADK reads, what it adds, and what travels with it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The config file ADK actually reads](parts/02-the-config/2.1-the-config-file-adk-reads.md) | `.agent_engine_config.json`, and three ways it is silently not read | `working` |
| 2.2 | [What the CLI adds that you did not write](parts/02-the-config/2.2-what-the-cli-adds.md) | Three keys reviewed against seven sent, and thirteen published methods | `working` |
| 2.3 | [Your .env travels](parts/02-the-config/2.3-your-env-travels.md) | 💥 Four keys in, four keys out, two of them credentials | `production` |

### 3 — Checking without deploying

*Three checks that run where the config is written.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A config checker that can go red](parts/03-checking-locally/3.1-a-config-checker-that-fails.md) | Four checks, two fixtures, and what a checker deliberately cannot see | `working` |
| 3.2 | [The zero-budget lint](parts/03-checking-locally/3.2-the-zero-budget-lint.md) | The spending rule as code, and why a denylist fails open | `working` |
| 3.3 | [The parked day that quietly required a credit card](parts/03-checking-locally/3.3-the-parked-day-that-billed.md) | 💥 Eleven false positives, zero real ones, and a check people would mute | `production` |

### 4 — What it would cost

*Two units that do not convert, and two dependencies you did not choose.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Priced in requests, not money](parts/04-what-it-costs/4.1-priced-in-requests.md) | 246 requests against an observed 20, and a half that will not convert | `working` |
| 4.2 | [The dependency you inherit](parts/04-what-it-costs/4.2-the-dependency-you-inherit.md) | A cloud SDK and a version pin, neither of them in any diff | `production` |

### 5 — In production

*The window nobody tests, and the nine things that come before the command.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The failure path nobody tests](parts/05-in-production/5.1-the-failure-path-nobody-tests.md) | Create, then configure — and what an interruption leaves behind | `production` |
| 5.2 | [What you would need before actually deploying](parts/05-in-production/5.2-before-you-would-actually-deploy.md) | Nine items, eight of them free, ordered by what decays | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [The bill that follows the load](papers/01-the-bill-that-follows-the-load.md) | `doi:10.1145/1721654.1721672` — elasticity is worth exactly your peak-to-average ratio. The demo measures this desk at 7.8x and eighty-one per cent waste under provision-for-peak; the ablation removes elasticity and nothing else |

---

## §3 Setup — run this

```bash
mkdir -p days/day-87-config-not-billed/lab/papers/elasticity
mkdir -p days/day-87-config-not-billed/lab/fixtures
cd days/day-87-config-not-billed/lab
touch _deploy.py surface.py validate.py envleak.py parked.py cost.py gate.py
touch papers/elasticity/load.py papers/elasticity/demo.py
```

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty —
everything here is in `google-adk==2.7.1`, its `python-dotenv` dependency, or the standard library.

**What each file is for:**

- `_deploy.py` is the file to read first. Every claim this day makes about ADK is read out of the
  installed library at import — the injected requirement, the published method list, the deploy
  source itself — so a claim goes red when ADK changes rather than going stale quietly.
- `surface.py` reads the real `adk deploy` help and counts it; `--names` prints the five names.
- `validate.py` is the config checker, with a good fixture and a bad one.
- `envleak.py` is section 2's finding, demonstrated with the same `dotenv_values` ADK uses.
- `parked.py` enforces the 🅿️ marker, and keeps its own broken first version runnable as `--grep`.
- `cost.py` prices the two halves; `gate.py` is the day's eval against `sutra/deploy.py`.
- `papers/elasticity/` holds the paper's demo: `load.py` is one deterministic week and nothing else.

The `fixtures/` directory holds a deliberately bad config, a good one, a sample `.env` and one deploy
script that would bill. **None of the credentials in them are real** — they are shaped like
credentials so the checks have something to find.

```bash
git check-ignore -v days/day-87-config-not-billed/lab/fixtures/.env.sample
```

**Why:**

- `days/*/lab/` is ignored repo-wide, which is what makes it safe for a lab to carry a file called
  `.env.sample` at all. Confirm the rule before you write anything into `fixtures/`, and never put a
  real key there even so — part 2.3 is a whole part about files like that travelling further than
  anybody intended.

---

## §4 Build brief

The teaching is in `parts/`, the measurements are in `lab/`, and what is left is the piece that
belongs in the product. Day 84 promoted the tracer, Day 85 the API surface, Day 86 the container;
today promotes the deploy path — as a thing that plans, validates and refuses, and does not deploy.

**`sutra/deploy.py`** — the desk's deployment, as code that can be reviewed.

- `TODO(me)`: `config()` building a `.agent_engine_config.json` from this repository's own settings,
  with `adk_version` pinned explicitly. Part 4.2 measured what the default is; a pin is one line and
  it is the difference between a reproducible runtime and whichever laptop deployed.
- `TODO(me)`: `validate(config)` — the four checks from part 3.1, plus the `adk_version` check that
  part's exercise adds. It returns findings rather than raising, so a test can assert on them.
- `TODO(me)`: `env_allowlist()` — the named variables the desk needs, and nothing else. Part 2.3
  measured the alternative: four keys in the file, four keys uploaded, two of them credentials.
  Decide how the credential reaches the platform instead, and write the decision in a comment.
- `TODO(me)`: `estimate()` reporting the model half in requests and returning a distinct code for the
  half that has no free-tier unit. Part 4.1's exit `2`, as a return value.
- `TODO(me)`: `parked()` — the scan from part 3.3, over the whole repository rather than one lab.
  Count the findings before you wire it into anything; if they are not all real, narrow the rule
  rather than adding suppressions.
- `TODO(me)`: `plan()` printing the assembled config **and** the exact command it would run, and
  running nothing. This is the day, in one function. Include `--agent_engine_id` from the config —
  part 5.1 measured what the default does on the third iteration of a fix.

**`tests/test_deploy.py`**

- `TODO(me)`: the bad fixture must fail `validate()` and the good one must pass. Part 3.1's argument:
  a checker only tested against a good config has never been tested.
- `TODO(me)`: a test that a config with no `adk_version` is refused.
- `TODO(me)`: a test that `env_allowlist()` drops a key called `SUTRA_DB_PASSWORD` and keeps
  `SUTRA_MODEL`.
- `TODO(me)`: a test that `plan()` makes no network call and starts no process. Assert on it rather
  than trusting it — that is the whole spirit of the day.

**Three `TODO(me)`s that are not code**, from part 5.2's list:

- **Decide how the credential arrives** once it is out of the config file. This is a design decision
  and it needs another person; without it the allowlist breaks the desk.
- **Decide what the thirteen published methods may be called by.** Ten are session and memory
  operations and `async_delete_session` is one of them — Day 68's least privilege, applied to a door
  the platform opens by default.
- **Measure the Flash-Lite allowance**, now open for a sixth day and blocking six separate lists: one
  controlled burn, a count, a dated `docs/PACKAGES.md` row.

---

## §5 The eval that must be able to fail

```bash
cd days/day-87-config-not-billed/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/deploy.py`, all red today because the module is the build brief. A check
that cannot run counts as a **failure**, never as skipped (Principle 11).

Every measurement in this day encodes its verdict in an exit code, and each has an arm that goes the
other way:

```bash
uv run python surface.py; echo "exit: $?"                 # 0 — 3 targets, 25 options, 9 deprecated
uv run python surface.py --names; echo "exit: $?"         # 0 — five names for one product
uv run python validate.py; echo "exit: $?"                # 1 — a credential written into the file
uv run python validate.py --fixed; echo "exit: $?"        # 0 — the same config, credential removed
uv run python envleak.py; echo "exit: $?"                 # 1 — 4 keys in, 4 out, 2 of them secrets
uv run python envleak.py --curated; echo "exit: $?"       # 0 — an allowlist, and 2 keys travel
uv run python parked.py; echo "exit: $?"                  # 0 — nothing here needs a billing account
uv run python parked.py --sloppy; echo "exit: $?"         # 1 — one committed script that would
uv run python parked.py --grep; echo "exit: $?"           # 1 — 11 findings, every one a mention
uv run python cost.py; echo "exit: $?"                    # 2 — one half will not convert
uv run python cost.py --model; echo "exit: $?"            # 0 — the countable half, already 12x over
```

Note the three arms that **exit 0 while hiding something**. `validate.py --fixed` is a genuine pass
and the other two are not: `envleak.py --curated` is green because a rule was added that nothing
enforces yet, and `cost.py --model` is green because it silently dropped the half nobody could price.
That is Phase 12's recurring shape arriving in Phase 13 — the report that omits the finding is the
report that exits zero.

The paper's demo does the same for its own claim: `demo.py` exits `0` having measured the desk at 7.8
times spikier at peak than on average, and `demo.py --off` exits `1` with eighty-one per cent of the
bill spent on capacity nothing used.

---

## §6 Request budget

**Zero provider requests, zero billed calls, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-07 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |
| Any billed cloud service | 0 | **no billing account is used or required** |

That last row is the day, and part 3.3 is the check that enforces it rather than asserting it.

**What was left unrun, and why.** One thing, named precisely: the deploy itself. Part 5.1 needs a
resource to exist in order to demonstrate the window between `create()` and `update()`, and creating
one bills. It is written out as a `TODO(me)` with the exact command and the interruption to apply,
marked *not run here — this one bills*, and **no transcript of it appears anywhere in this day**.
Principle 7's discipline extended to procedures: a step you did not run gets the exact command, never
an invented output.

Everything else is real. The CLI help is captured from the installed CLI, the method list and the
injected requirement are read from the installed library, the `.env` behaviour is demonstrated with
the same `dotenv_values` ADK calls, and the deploy source's three decisive lines are asserted against
the file on disk before this day says anything about them.

---

## §7 Traps

1. **Reading only the half of the trade that is on the poster.** A platform removes operational work
   and adds dependencies; five things stop being your decision — part 1.1.
2. **Treating 🅿️ as a licence rather than a decision.** A parked day can be hollow, and nothing in
   the tooling can tell — part 1.2.
3. **Learning a deploy surface from a tutorial.** Nine of twenty-five options are deprecated in this
   version; a page written last year would mislead on a third of them — part 1.3.
4. **Letting `--adk_version` default.** The production runtime is then whichever machine typed the
   command, with no diff to show for it — parts 1.3 and 4.2.
5. **Assuming a missing config file is an error.** `os.path.exists` returns `False`, the deploy
   proceeds from an empty dictionary, and nothing is printed — part 2.1.
6. **Reviewing the config you wrote.** Three keys authored, seven sent; the rest are added by the CLI
   including thirteen published methods — part 2.2.
7. **Believing Principle 9 covers deployment.** It covers git. The deploy path reads the whole `.env`
   and ships every key in it — part 2.3.
8. **Writing a checker and never testing it against something bad.** Two fixtures is the minimum for
   a check to mean anything — part 3.1.
9. **A denylist of paid model prefixes.** A model nobody has heard of is approved by default, which
   is the wrong direction to fail in for the one rule you cannot undo — part 3.2.
10. **A policy check with false positives.** Eleven findings and zero real ones trains people to
    ignore it, entirely reasonably — part 3.3.
11. **Adding two costs in different units.** Requests convert to an allowance; a resource billed by
    existence does not, and rounding it into either answer is a fabrication — part 4.1.
12. **Deploying twice without `--agent_engine_id`.** The default creates a new resource every run, so
    three iterations of a fix leave three billing — part 5.1.

---

## §8 Verify before you code

Fetched on 2026-09-07:

| What | Where | What it said |
| --- | --- | --- |
| ADK deploy guide | <https://adk.dev/deploy/agent-runtime/> | the page is titled *Deploy to Agent Runtime*; `/deploy/agent-engine/` returns a redirect stub whose canonical link is `../agent-runtime/` |
| ADK deploy index | <https://adk.dev/deploy/> | the three targets, matching the CLI |
| Paper record | <https://api.crossref.org/works/10.1145/1721654.1721672> | *A view of cloud computing*, Communications of the ACM 53(4), 2010, pp. 50–58 |

**ADK symbols verified against the installed `google-adk==2.7.1`**, not only against the docs.
`adk deploy` advertises `agent_engine`, `cloud_run` and `gke`; `adk deploy agent_engine` has
twenty-five options besides `--help`, nine of which carry a deprecation notice in their own block.
`cli_deploy._AGENT_ENGINE_REQUIREMENT` is `google-cloud-aiplatform[adk,agent_engines]`;
`cli_deploy._AGENT_ENGINE_CLASS_METHODS` holds **thirteen** entries, five of whose descriptions begin
with "Deprecated" — including `stream_query`, the entry point every example uses. The config lookup
falls back to `.agent_engine_config.json` in the agent folder and treats a missing file as no error.
The env path is three lines: `env_file = os.path.join(agent_folder, '.env')`, then
`env_vars = dotenv_values(env_file)`, then `agent_config['env_vars'] = env_vars` — all three asserted
against the installed source by `envleak.py` before the day describes them. The deploy sequence is
`create()`, then generate the Dockerfile, then `update()`, with `delete()` in the `except` branch
guarded by `agent_engine_id is None`.

**The 1.x → 2.x trap this day pays for is ADK-73** — every model pinned explicitly. Part 3.2 makes it
a lint rather than a habit, and part 4.2 extends the same argument from the model to the platform
version.

---

## §9 Say it in an interview

*"We wrote the deployment for a managed agent platform and deliberately never ran it, because the
command is the only part that costs money and the only part that teaches nothing — everything that
required judgement was free. Reading the CLI surface properly turned up three things worth knowing.
First, nine of the twenty-five deploy options are deprecated in the current version, and six of those
are not features being withdrawn, they are decisions the platform took back — which is a fair
description of what depending on a young platform costs. Second, `--adk_version` defaults to whatever
is installed on the machine running the command, so two colleagues deploying the same commit produce
different production runtimes with no diff anywhere; we pin it in the config. The one I would lead
with, though, is what travels. The deploy path finds the `.env` beside the agent, parses every key
with `dotenv_values`, and assigns the whole dictionary into the config it uploads. We had followed
the secrets rule perfectly — the file has been gitignored since day zero, the repository is safe to
open source — and the file that was private precisely because it holds secrets was the file being
uploaded without inspection. Principle satisfied, credentials gone. The fix is an explicit allowlist
and a real decision about how the key arrives instead. We also wrote a check that the day needs no
billing account, and its first version reported eleven findings, all false positives, five of them
its own list of things to look for — so we rewrote it against the syntax tree to count only strings
that reach a process call, and kept the broken version runnable, because 'the obvious implementation
of this check is unusable' was the more valuable finding."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands rather
than read them. `./m done 87` refuses to commit until they are.

The day is finished when you could review somebody else's deployment config and find three things
wrong with it — and when you can say, without hedging, which single step of a deployment you have not
done and exactly what it would have cost.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 87 | 2026-09-07 | ADK-68 | 13 | <hash> | ⚠️ |
```

The gate column is `⚠️` and it is honest rather than a formality. `./m depth` is green over this day
and every measurement in it was run at zero cost. What is not green: `sutra/deploy.py` is the build
brief and `lab/gate.py` reports 0 of 6, by design; **the deploy itself was not run and never will be
here**, which is what 🅿️ means and is recorded rather than glossed. Three findings carry forward — the
whole `.env` travels unless an allowlist is written, the deploy has a window in which an interrupted
run leaves a billing resource nothing will tidy, and the Flash-Lite allowance is unmeasured for a
sixth day, now blocking six lists.

**`docs/PACKAGES.md`** — no new rows. No package is added today. Note for the row this day *would*
have needed: `google-cloud-aiplatform[adk,agent_engines]` is injected by ADK's deploy path into a
staged `requirements.txt`, not by this repository, and it is recorded in part 4.2 rather than in the
ledger because nothing here installs it.

**`docs/PAPERS.md`** — one new row:

```text
| A view of cloud computing | doi:10.1145/1721654.1721672 | 2010 | 2026-09-07 | 87 | `days/day-87-config-not-billed/papers/01-the-bill-that-follows-the-load.md` |
```

The title, journal, volume, issue and pages were copied from
`api.crossref.org/works/10.1145/1721654.1721672` on 2026-09-07 — the record, not the memory
(§17.4.1 rule 5).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 87: agent engine - the config written, not billed - closes ADK-68
```

---
day: 45
phase: 6
phase_name: "MCP II: production"
title: "Phase gate — the full MCP audit of `sutra-core`"
ids: ["MCP-24", "MCP-25", "OPS-09"]
principles: [1, 2, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]
kind: gate
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 45 — Phase gate: the full MCP audit of `sutra-core`

> **Yesterday (Day 44):** the client learned to survive. `sutra/mcp/hardening.py` got `with_retries`,
> `with_timeout` and the rule that nothing holds a connection between calls, so a dying server instance
> costs one request instead of a session.
> **Today:** nothing new is built. Ten named checks in `tools/mcp_audit.py` and one line in `./m check`
> turn thirteen days of MCP work into rules that can go red, and then the phase gate's other five
> conditions decide whether Phase 6 is actually green.
> **Tomorrow (Day 46):** Phase 7 opens on memory. `MemoryService` semantics, and the line between what a
> session holds and what the system remembers.

---

## §1 Where we are

The lease is up and you are walking through the flat with the landlord, who has a torch and a sheet of
paper.

You lived here for two years and you know this flat better than he does. You know the tap in the second
bathroom drips if you turn it too fast, and that the bedroom door has never closed properly, and that the
mark on the kitchen wall was there when you moved in. All of that is true and none of it is what is
happening now. He is reading a list, in order, out loud, and writing what he sees beside each line.

It feels adversarial for about the first three lines, and then it stops, because you both notice the same
thing: the list is doing you a favour. Every item he reads and marks is an item nobody can raise in six
weeks. The mark on the kitchen wall gets written down as pre-existing, in his handwriting, on the day. The
drip gets written down as a drip. Two things are found that you had genuinely forgotten about, and they are
small, and they are settled in an afternoon rather than argued about over a deposit.

The flat is exactly as good as it was before he arrived. What changed is that there is now a piece of paper
saying so, with a date on it, and neither of you has to rely on remembering.

**That is today.** Thirteen days built an MCP integration — a client, a server, resources, prompts, long
jobs, auth, database tools, an allowlist, capabilities, an agent on the wire, a deploy-shaped entry point,
and a hardened client. Each of those days ended green. *"Each piece was correct when it was built"* is the
sentence that opens most postmortems, and it is not the same claim as *"the system is correct now"*.

So today is a walk with a list. Ten named checks that can go red, written before the code is opened, and
run by the same command that runs every other check in this repository. Plus the half no program can do:
two rows a person owns, four things re-read from outside the repository, and a verdict on the one number
this whole phase has been carrying — the `mcp` pin.

Nothing is built. Everything is checked, and the checking is written down.

## §2 The map

Nineteen parts in seven sections, **no paper part**. Two parts carry §6 *The paper behind it* as an
address to papers taught on earlier days. The sections follow the audit's own structure: section 1 is what
an audit is, sections 2 to 4 are the ten rules grouped by what they protect — the client side, the server
side, the policy between them — section 5 is the server you did not write, section 6 breaks the audit on
purpose twice, and section 7 is the phase gate. The day climbs `foundation → working → production`.

### Section 1 — `01-what-an-audit-is`: the method (MCP-24)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The list is written before you look](parts/01-what-an-audit-is/1.1-the-list-is-written-before-you-look.md) | Why rules come before code, and the three things each one carries | `foundation` |
| 1.2 | [A finding is the audit working](parts/01-what-an-audit-is/1.2-a-finding-is-the-audit-working.md) | Fixed or filed, no third state — and why zero findings is a bad result | `foundation` |

### Section 2 — `02-the-client-side`: `A01`–`A04`, the code Sutra runs (MCP-24)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [A01 — nothing reaches past the client](parts/02-the-client-side/2.1-nothing-reaches-past-the-client.md) | Day 32's boundary measurement, promoted to an exit code | `working` |
| 2.2 | [A02 — every call carries a deadline](parts/02-the-client-side/2.2-every-call-carries-a-deadline.md) | Why a missing timeout produces no error at all | `working` |
| 2.3 | [A03 — nothing holds a connection](parts/02-the-client-side/2.3-nothing-holds-a-connection.md) | Four commitments one module-level session makes | `working` |
| 2.4 | [A04 — no key in a tracked file](parts/02-the-client-side/2.4-no-key-in-a-tracked-file.md) | `git ls-files`, four shapes, and why `days/` is excluded | `working` |

### Section 3 — `03-the-server-side`: `A05`–`A07`, the code strangers call (MCP-24)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A05 — no state that outlives a request](parts/03-the-server-side/3.1-no-state-that-outlives-a-request.md) | The dictionary that works on one instance and lies on three | `working` |
| 3.2 | [A06 — every tool says what it takes](parts/03-the-server-side/3.2-every-tool-says-what-it-takes.md) | Docstring becomes description, annotations become schema | `working` |
| 3.3 | [A07 — every tool has a path that raises](parts/03-the-server-side/3.3-every-tool-has-a-path-that-raises.md) | Why a swallowed error is worse when the caller is a model | `working` |

### Section 4 — `04-the-policy`: `A08`–`A10`, what sits between them (MCP-24, MCP-25, OPS-09)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [A08 — the allowlist is not empty](parts/04-the-policy/4.1-the-allowlist-is-not-empty.md) | An empty filter admits everything, and fail-safe defaults | `working` |
| 4.2 | [A09 — a rule with one owner](parts/04-the-policy/4.2-a-rule-with-one-owner.md) | The `:free` rule this audit refuses to re-implement, and the line in `m` | `working` |
| 4.3 | [A10 — where the server ledger lives](parts/04-the-policy/4.3-where-the-server-ledger-lives.md) | `docs/SERVER_PROVENANCE.md`, generated — Day 32's open question, answered | `production` |

### Section 5 — `05-a-server-you-did-not-write`: the outward half (MCP-25)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Six questions with an exit code](parts/05-a-server-you-did-not-write/5.1-six-questions-with-an-exit-code.md) | Three the registry answers, three you do, all as fields | `production` |
| 5.2 | [What no script can check](parts/05-a-server-you-did-not-write/5.2-what-no-script-can-check.md) | Two rows numbered `H`, and why they are not in the tuple | `production` |

### Section 6 — `06-failure-lab`: the audit broken on purpose

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 Green because the path did not exist](parts/06-failure-lab/6.1-green-because-the-path-did-not-exist.md) | One substitution, eight false greens, five findings instead of eleven | `production` |
| 6.2 | [💥 The registry that was empty](parts/06-failure-lab/6.2-the-registry-that-was-empty.md) | Ten green rules, three servers, one policy | `production` |

### Section 7 — `07-the-phase-gate`: closing Phase 6 (OPS-09)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 7.1 | [Six things that must be true](parts/07-the-phase-gate/7.1-six-things-that-must-be-true.md) | Why this day's build is one eighteenth of a gate | `production` |
| 7.2 | [The freshness re-check](parts/07-the-phase-gate/7.2-the-freshness-recheck.md) | Four look-ups, four dated findings, one that lets Phase 7 open | `production` |
| 7.3 | [The pin and the amendment](parts/07-the-phase-gate/7.3-the-pin-and-the-amendment.md) | Blocked, not deferred — and what the amendment must say | `production` |

**No paper part today.**
[2.1](parts/02-the-client-side/2.1-nothing-reaches-past-the-client.md) carries §6 as an address to *End-to-end
arguments in system design* (`doi:10.1145/357401.357402`, taught on Day 21 at
[`papers/01-end-to-end-arguments.md`](../day-21-errors-surface-not-swallow/papers/01-end-to-end-arguments.md)),
because a second unguarded path out of the host is the end-to-end function being skipped rather than optimised.
[4.1](parts/04-the-policy/4.1-the-allowlist-is-not-empty.md) carries §6 as an address to *The protection of
information in computer systems* (`doi:10.1109/PROC.1975.9939`, taught on Day 40 at
[`papers/01-protection-of-information.md`](../day-40-filtering-and-allowlists/papers/01-protection-of-information.md)),
because an empty filter that admits everything is fail-safe defaults running backwards. A paper is taught once
in the whole curriculum; every later day links to it.

**Read the sections in order.** Sections 2 to 4 assume section 1's `Finding` and `Check` shapes, section 5
assumes section 4's policy record, section 6 breaks what sections 2 to 4 built, and section 7 is the gate that
all of it feeds one sixth of.

## §3 Setup — run this

Nothing is installed today. `tools/` already exists — Day 30 created it and owns its `__init__.py`; Day 31 added
two linters to it. You are adding a third module, and one ledger.

```bash
touch tools/mcp_audit.py
touch docs/SERVER_PROVENANCE.md
ls tools/
```

**Do not create `tools/__init__.py`** — it is there from Day 30, and a second one would overwrite a package
marker. `docs/SERVER_PROVENANCE.md` goes beside `SKILL_PROVENANCE.md`, per the plan's §16; its header and columns
are in [4.3](parts/04-the-policy/4.3-where-the-server-ledger-lives.md). After the `ls`, `tools/` should hold
`__init__.py`, `skill_checks.py`, `lint_skills.py`, `lint_free_suffix.py` and your new `mcp_audit.py`; if the
first four are missing, Days 30 and 31 are unfinished and today's `A09` will say so.

**No `uv add`.** The audit imports `ast`, `re`, `subprocess`, `pathlib` and `dataclasses` — standard library
only, deliberately, because a gate stage that pulls in a dependency is a gate stage that can fail to install.

## §4 Build brief

Four things to write, and the decisions inside them are yours.

**1. `tools/mcp_audit.py`** — the ten checks, the two dataclasses, the runner and `main`. Every check function
is given complete in its part; what is left to you is the assembly and four judgements:

```python
# tools/mcp_audit.py
# TODO(me): FORBIDDEN - which imports mean "reached past the boundary" in THIS repository?
#   2.1 gives a defensible set. Write down why each name is in it, and what you would do
#   about a module that legitimately needs one.

# TODO(me): severity - which of the ten checks block the gate and which are notes?
#   1.2 says two values and no more. Decide, and write the reason beside each choice.

# TODO(me): the dotted-name gap. A05 misses `collections.defaultdict(list)`, A08 misses
#   `filtering.ServerPolicy(...)`, and A03 misses `SESSION: ClientSession = ClientSession()`.
#   Plant each one in the fixture, watch the check stay green, then decide which to close.

# TODO(me): A06 misses keyword-only parameters (`fn.args.kwonlyargs`). Same drill.
```

**2. One line in `./m check`** — the diff is in
[4.2](parts/04-the-policy/4.2-a-rule-with-one-owner.md), positioned after Day 31's two linters and before
pytest. Read the target back with `grep` before you rely on it; `m` is the file every other command runs
through.

**3. `docs/SERVER_PROVENANCE.md`** — the header and the seven-column table are in
[4.3](parts/04-the-policy/4.3-where-the-server-ledger-lives.md). It starts empty and fills as `REGISTRY` fills.

```text
TODO(me): the eleventh check - derive the inventory instead of reading it.
  6.2 shows ten green rules on a repository reaching three unregistered servers.
  Scan for server addresses under sutra/, compare with REGISTRY, report the difference.
  The hard part is the definition of "address": decide it before you write the regex,
  and decide what a deliberately-unlisted lab prop's row looks like.
```

**4. The fixture** — a scratch tree holding one deliberate violation per rule. Every red example in this day was
produced from one. Build it outside the repository, or under the day's `lab/`; **never break `sutra/` to test the
alarm.**

The day's own instrument is at `days/day-45-the-mcp-audit/lab/audit_preview.py`. It is the ten checks with the
four decisions above hard-coded to one defensible answer, so the parts could print real output. Read it, disagree
with it, and write your own.

## §5 The eval that must be able to fail

The gate stage itself, drilled the way Day 31 drills a new stage: plant a violation, run the gate, confirm it
stops at the right stage with the right file named.

```bash
mkdir -p /tmp/sutra-audit-fixture/sutra/desk
printf 'import sqlite3\n\n\ndef rows(t: str) -> list[str]:\n    return list(sqlite3.connect("x").execute("select 1"))\n' \
  > /tmp/sutra-audit-fixture/sutra/desk/quick_lookup.py
uv run python -c "
from pathlib import Path
from tools.mcp_audit import check_boundary
found = check_boundary(Path('/tmp/sutra-audit-fixture'))
print(found)
assert found, 'A01 did not fire on a planted sqlite3 import'
print('RED as expected')
"
```

The fixture is a real directory tree with one violating file, built outside the repository so nothing in
`sutra/` is touched. `check_boundary` is called with an explicit root, which is the whole reason the checks take
one. The `assert` is the eval: **it fails if the check does not fire**, and a check nobody has watched go red is
a check you are assuming works. Zero model calls, no network.

Then the whole gate, on the real repository:

```bash
uv run python -m tools.mcp_audit; echo "exit: $?"
./m check; echo "exit: $?"
```

The module first, alone, so its output is readable without the rest of the gate above it, and with `-m` rather
than the path form ([4.2](parts/04-the-policy/4.2-a-rule-with-one-owner.md)). Then `./m check`, which is what has
to be green for the phase gate's condition 3.

Expect the audit to be **red** on this repository until the code Days 33 to 44 describe has actually been typed.
That is the correct answer, it is what
[1.2](parts/01-what-an-audit-is/1.2-a-finding-is-the-audit-working.md) measured, and every finding carries the day
it is filed to.

## §6 Request budget

**Zero.** Not one model call, from any provider.

| Provider | Requests today | Why |
| --- | --- | --- |
| Gemini (`gemini-3.7-flash`) | 0 | nothing generates; the audit parses files |
| Groq | 0 | — |
| OpenRouter | 0 | — |
| Ollama | 0 | — |

Every check in this day is `ast`, `pathlib`, `re` and `subprocess` over the local tree. The four freshness
look-ups in [7.2](parts/07-the-phase-gate/7.2-the-freshness-recheck.md) are HTTP requests to package indexes and
documentation sites, not model calls, and they cost no quota. A gate day that spent generations would be a gate
you could not afford to run twice.

## §7 Traps

- **A missing target treated as a skip.** The single most important line in the module. `return []` on a missing
  path gives you eight false greens on this repository —
  [6.1](parts/06-failure-lab/6.1-green-because-the-path-did-not-exist.md) measures exactly that.
- **`python tools/mcp_audit.py` instead of `python -m tools.mcp_audit`.** `ModuleNotFoundError: No module named
  'tools'`. Day 31's
  [4.2](../day-31-the-quality-gate/parts/04-wiring-the-gate/4.2-the-module-the-script-cannot-find.md).
- **Re-implementing the `:free` suffix rule.** It has an owner —
  [4.2](parts/04-the-policy/4.2-a-rule-with-one-owner.md).
- **Reading `docs/TRACEABILITY.md` without running `./m trace` first.** It is generated. Reading a stale
  generated ledger and concluding something is its own small version of audit theatre.
- **Editing `m` in the wrong branch of the `case` statement.** `done)` looks like `check)` when you are skimming,
  and `m` is the driver — a broken `case` stops `./m depth` too.
- **Bumping the `mcp` pin because the index offers a newer one.** `google-adk` 2.7.1 and 2.8.0 both declare
  `mcp>=1.24,<2`. [7.3](parts/07-the-phase-gate/7.3-the-pin-and-the-amendment.md).
- **Writing the rules after reading the code.** They will all pass, and the green will mean nothing —
  [1.1](parts/01-what-an-audit-is/1.1-the-list-is-written-before-you-look.md).
- **A zero-finding first run.** Suspicious, not reassuring —
  [1.2](parts/01-what-an-audit-is/1.2-a-finding-is-the-audit-working.md).

## §8 Verify before you code

Every URL below was fetched live on **2026-09-05**, and the results are in
[7.2](parts/07-the-phase-gate/7.2-the-freshness-recheck.md) with the commands that produced them.

| What | URL | What it said on 2026-09-05 |
| --- | --- | --- |
| MCP specification revision | `https://modelcontextprotocol.io/specification/latest` | based on `schema/2026-07-28/schema.ts`; every card links into `/specification/2026-07-28/`. **Unchanged** |
| MCP Tasks extension | `https://modelcontextprotocol.io/extensions/tasks/overview` | `resultType: "task"`, `ttlMs`, `pollIntervalMs`, `tasks/update`, negotiated via `server/discover` — all absent from the pinned SDK |
| `mcp` on the package index | `https://pypi.org/pypi/mcp/json` | `2.1.1`; the description says v2 supports the 2026-07-28 spec and every earlier revision, keeps 1.x on a branch, and advises `mcp>=1.28,<2` until migration |
| `google-adk` releases | `https://github.com/google/adk-python/releases` | `v2.8.0` above `v2.7.1`; the only removal in range moves `pyarrow` out of the `gcp` extra |
| `google-adk` 2.8.0 metadata | `https://pypi.org/pypi/google-adk/2.8.0/json` | still declares `mcp>=1.24,<2` — **the fact that decides the pin** |
| Gemini rate limits | `https://ai.google.dev/gemini-api/docs/rate-limits` | no free-tier table published; directs you to your own project's limits view |

**No ADK symbol is used today.** The audit imports nothing from `google.adk` — it parses files — so Principle 8's
"name the adk.dev page" rule has nothing to name, and saying so is the honest version of satisfying it. The
symbols this day *audits for* (`McpToolset`, `StdioConnectionParams`, `to_mcp_server`) were verified present in
the installed `google-adk==2.7.1` on the days that used them.

## §9 Say it in an interview

*"At the end of my MCP phase I wrote an audit — ten named checks in the build, each with a rule stated as the
good state and a function returning findings rather than a boolean. The rules came before I opened the code,
which matters more than it sounds: I wrote every line being audited, so if I'd read it first I'd have written
rules it already passed. Two things I'd call out. First, a missing target is a finding, not a skip — I proved
that to myself by flipping the branch, and eight of ten rules went green on a repository where none of the
audited code existed, with the finding count dropping from eleven to five and nothing fixed. Second, the audit
is one stage inside one of six phase-gate conditions; the other five are a person reading and writing answers
down, including the freshness re-check against the outside world. That one paid off immediately: our protocol
SDK speaks a revision from November and the spec moved on in July, and the index has a version 2 that closes
the gap — but the agent framework declares a hard upper bound below it, in its newest release. So the finding
isn't 'we're behind', it's 'we're blocked upstream', filed with a trigger rather than a date. And the reason
that's survivable is that we'd already built to the newer architecture the library couldn't speak — nothing
held between requests, state in the payload, honest errors — so the eventual bump is a dependency change and
not a rewrite."*

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box ticked, `./m depth 45` green, and the four freshness answers
written down with today's date — including the boring ones. `./m done 45` refuses to commit until the checklist
has no unticked boxes.

Not when a number of sittings has passed. A gate is passed on evidence.

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 45 | 2026-09-05 | MCP-24, MCP-25, OPS-09 | 19 | <hash> | ⚠️ |
```

The gate column is `⚠️` and it means it. `./m depth 45` is green and `./m check` is not: it is red at stage one
on a `ruff` import-order error in `tests/test_persona.py`, unchanged since Day 15, in the learner's own code that
no generated day may edit. It becomes `✅` after `uv run ruff check --fix tests/test_persona.py`, and rounding it
up before then would be the first thing this day teaches you not to do.

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded. `mcp` stays at `1.29.1`,
`google-adk` at `2.7.1`, `gemini-3.7-flash` unchanged. The pin gap is *measured* here and *decided* here, and the
decision is that it stays — [7.3](parts/07-the-phase-gate/7.3-the-pin-and-the-amendment.md). A bump is a plan
amendment with its own row, not a side effect of a day that installs nothing.

**`docs/PAPERS.md`** — **no new rows.** `doi:10.1145/357401.357402` and `doi:10.1109/PROC.1975.9939` already have
rows and are taught on Days 21 and 40; this day cites each once, as an address.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**`docs/SERVER_PROVENANCE.md`** — **created today, empty.** Header, seven columns, and the line saying it is
generated by `tools/mcp_audit.py` from `REGISTRY`. Rows arrive as servers do.

**`docs/CHANGELOG_PLAN.md`** — no row. Nothing in the plan changed. The `mcp` pin finding is filed with a
trigger — *revisit when a `google-adk` release declares `mcp>=2`* — and the amendment gets written on the day
that trigger fires, not before.

**The commit:**

```text
day 45: phase gate - the full MCP audit of sutra-core - closes MCP-24, MCP-25, OPS-09
```

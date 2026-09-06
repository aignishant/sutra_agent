---
day: 68
phase: 10
phase_name: "Safety and security"
title: "Permissions & least privilege for tools"
ids: ["SEC-10", "SEC-11"]
principles: [1, 2, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: build
plan_version: "v2.2.1"
parts: 22
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 68 — Permissions and least privilege for tools

> **Yesterday (Day 67):** the guardrail ladder, measured in both columns and then measured again
> against somebody who had read it — 6 of 6 on our own fixtures, 2 of 5 against rewrites, 0 of 3
> against a split payload. Its closing part stopped adding readers and said the thing that closes a
> channel is a rule that never reads text.
> **Today:** the first of those rules. Not *is this text suspicious* but *is this tool, with these
> arguments, something the desk may do at all* — a permission table, a fence outside every tool, and
> five ways a permission system can look correct and not be.
> **Tomorrow (Day 69):** the other one — PII and data boundaries, where the control is a value that
> never entered the context in the first place.

---

## §1 Where we are

Day 66 traced the lethal trifecta and found it closing at the `review` stage. Day 67 built checks
that read text and measured their ceiling. Today the question changes shape entirely, and the change
is the point: instead of asking whether a request *looks* dangerous, ask whether the desk holds the
authority to carry it out.

The idea has a name older than any of this. **Least privilege** says a component gets exactly the
authority its job requires and no more, so that a component behaving badly — through a bug, through
an injection, through an ordinary mistake — is bounded by what it was given rather than by what it
intended.

For an agent that idea has a sharper edge, and it is the day's opening claim: **the agent is a
deputy.** It acts on instructions it does not control — ticket text, archive rows, tool results —
while holding authority that you do control, and only the second half of that sentence is yours to
change. You cannot make the instructions trustworthy. You can decide what the deputy is holding when
it reads them.

So today is a table. One row per tool, naming five things: what the tool may do, which rows it may
touch, how often, whose credential it uses, and what happens when it is wrong. That table is not a
document about the system; it is data the system reads, checked by a diff, enforced in one place
outside every tool.

Section 5 is where it is taken apart. Three permission systems that would pass review, each broken by
running it: a check that guards the tool it lives in and not the second tool that reaches the same
effect, a table that silently allows a tool nobody gave a row, and a helper agent whose narrow
toolset achieves nothing because control comes back to the agent that holds everything.

---

## §2 The map

Six sections. Section 1 is the confused-deputy problem stated in this repository's terms. Section 2
is the permission table and the three questions a grant has to answer. Section 3 is the difference
between a tool that is forbidden and a tool that is **absent**. Section 4 moves down a level, from
the tool to its arguments. Section 5 is the failure lab. Section 6 is what it costs to run this for
real, and how a grant gets removed.

### 1 — The deputy

*Why an agent holding your authority and reading their instructions is a specific, named problem.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The errand, and the keys that went with it](parts/01-the-deputy/1.1-the-errand-and-the-keys-that-went-with-it.md) | The agent is a deputy, and only the authority half is yours to change | `foundation` |
| 1.2 | [A tool does its job, not your intention](parts/01-the-deputy/1.2-a-tool-does-its-job-not-your-intention.md) | 💥 A tool is a capability, and it does not know what it was for | `foundation` |
| 1.3 | [Whose permissions is the tool using?](parts/01-the-deputy/1.3-whose-permissions-is-the-tool-using.md) | The caller cannot lie about who they are, because `tool_context` is not the model's | `working` |
| 1.4 | [A rule in words is not a permission](parts/01-the-deputy/1.4-a-rule-in-words-is-not-a-permission.md) | Why an instruction in the prompt is advice and a missing tool is a boundary | `working` |

### 2 — Three questions

*What a grant has to answer before it is a grant, and the artefact that holds the answers.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [May it? Capability, and the line between read and write](parts/02-three-questions/2.1-may-it-capability-and-the-read-write-line.md) | The first question, and why read/write is the line that matters most | `foundation` |
| 2.2 | [Which rows? Scope, and the tool that is allowed on everything](parts/02-three-questions/2.2-which-rows-scope.md) | A capability with no scope is a capability over the whole archive | `working` |
| 2.3 | [How many times? Rate is a permission too](parts/02-three-questions/2.3-how-many-times-rate.md) | On a free tier the upper bound is the only thing between one run and a dry quota | `working` |
| 2.4 | [The table you can diff](parts/02-three-questions/2.4-the-table-you-can-diff.md) | Five rows, five columns, and two questions you can only ask once it exists | `working` |

### 3 — Absent, not forbidden

*The strongest denial is a tool the agent was never offered.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Deny by default, at the toolset](parts/03-absent-not-forbidden/3.1-deny-by-default-at-the-toolset.md) | Allowlist and trimmed-list agree today and diverge the day a tool is added | `working` |
| 3.2 | [The predicate that reads the room](parts/03-absent-not-forbidden/3.2-the-predicate-that-reads-the-room.md) | A tool filter that depends on who is asking, evaluated per request | `working` |
| 3.3 | [What happens when it asks anyway](parts/03-absent-not-forbidden/3.3-what-happens-when-it-asks-anyway.md) | 💥 An absent tool raises `ValueError` and ends the run — correct, and not free | `production` |
| 3.4 | [Whose keyring does a helper carry?](parts/03-absent-not-forbidden/3.4-whose-keyring-does-a-helper-carry.md) | What a delegated agent is actually offered, measured against 2.7.1 | `production` |

### 4 — The argument

*The tool may be allowed and the argument may not, which is where most real permissions live.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The tool is allowed, the argument is not](parts/04-the-argument/4.1-the-tool-is-allowed-the-argument-is-not.md) | Argument-level permission, and three ways to constrain a value | `working` |
| 4.2 | [A path is a sentence about the whole disk](parts/04-the-argument/4.2-a-path-is-a-sentence-about-the-whole-disk.md) | 💥 Resolve first, then ask whether the result is inside the directory you meant | `production` |
| 4.3 | [The recipient who is not the customer](parts/04-the-argument/4.3-the-recipient-who-is-not-the-customer.md) | The address on the ticket, never an address from its body | `production` |
| 4.4 | [The check that belongs outside every tool](parts/04-the-argument/4.4-the-check-that-belongs-outside-every-tool.md) | A check inside a tool guards that tool and nothing else | `production` |
| 4.5 | [What a refusal must not tell you](parts/04-the-argument/4.5-what-a-refusal-must-not-tell-you.md) | 💥 *Not yours* and *not there* must be the same sentence — 4 of 6 becomes 3 of 6 | `production` |

### 5 — Failure lab

*Three permission systems that would pass review, each broken by running it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The check inside the door it guards](parts/05-failure-lab/5.1-the-check-inside-the-door-it-guards.md) | 💥 The forbidden close succeeds through `update_ticket` | `production` |
| 5.2 | [The tool that arrived without a row](parts/05-failure-lab/5.2-the-tool-that-arrived-without-a-row.md) | 💥 Drift between the tools offered and the rows declared, caught by a diff | `production` |
| 5.3 | [The helper that handed control back](parts/05-failure-lab/5.3-the-helper-that-handed-control-back.md) | 💥 A narrow helper, and a chain that ends in `refund` anyway | `production` |

### 6 — In production

*What least privilege costs to run, and the only honest way to remove a grant.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [One credential per tool](parts/06-in-production/6.1-one-credential-per-tool.md) | A credential that does not exist cannot be wrong, and what that costs | `production` |
| 6.2 | [Grant is a claim, use is evidence](parts/06-in-production/6.2-grant-is-a-claim-use-is-evidence.md) | The gap between granted and used is where a permission nobody needs lives | `production` |

### The paper — read it last

*Principle 4 at the scale of a day: build the permission table by hand, then read the document that
named the problem it solves.*

| # | Paper | What it answers |
| --- | --- | --- |
| 01 | ["The Confused Deputy" (or why capabilities might have been invented)](papers/01-the-confused-deputy.md) | `doi:10.1145/54289.871709` — a service holding an authority its callers lack, doing work on their behalf, and the reason naming an object is not the same as holding a permission to it |

---

## §3 Setup — run this

```bash
mkdir -p days/day-68-least-privilege-tools/lab/papers/confused-deputy
cd days/day-68-least-privilege-tools/lab
```

Thirteen files in the lab, plus two in the paper's demo directory. No package is added today —
`google-adk` is already pinned from Day 7:

```bash
touch _desk.py _fake.py
touch deputy.py whose.py table.py rate.py absent.py handover.py
touch escape.py recipient.py where.py leak.py gate.py
touch papers/confused-deputy/service.py papers/confused-deputy/demo.py
```

**What each file is for:**

- `_desk.py` and `_fake.py` are imported, never run. `_desk.py` holds the desk's five tools, the
  seeded tickets, the knowledge-base notes and the one private file the argument checks are aimed at;
  its `fresh()` rebuilds `lab/state/` from scratch on every run, so no measurement inherits the last
  one. `_fake.py` is a `BaseLlm` subclass that emits scripted function calls, which is what lets a day
  about handing out authority run inside the real ADK runtime and cost zero quota.
- `deputy.py` and `whose.py` are section 1 — the deputy demonstrated, and whose permissions a tool
  actually uses.
- `table.py` writes `permissions.json` on first run and answers the two questions that need it: what
  has drifted, and what was granted and never used.
- `rate.py`, `absent.py` and `handover.py` are sections 2 and 3.
- `escape.py`, `recipient.py`, `where.py` and `leak.py` are section 4, and `where.py` is used again in
  section 5.
- `gate.py` is today's eval.

Verify the lab state directory is gitignored before anything writes a file that looks like payroll:

```bash
git check-ignore -v days/day-68-least-privilege-tools/lab/state/private/payroll.csv
```

**Why:**

- `days/*/lab/` is ignored repo-wide, so this should print the matching rule. `state/private/` holds a
  synthetic file whose whole purpose is to be the thing a path-traversal check must refuse; if this
  prints nothing, fix `.gitignore` before running anything — Principle 9.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.

---

## §4 Build brief

The teaching is in `parts/` and the measurements are in `lab/`. What is left is the piece that belongs
in the product.

**`sutra/permissions.py`** — the permission table as data, and the fence that reads it.

- `TODO(me)`: load `permissions.json` and expose it as typed rows rather than raw dicts. The gate
  checks that the policy is **data, not branches**: a permission expressed as `if tool.name == ...`
  cannot be diffed, and the diff is what catches section 5.2's failure.
- `TODO(me)`: a `BasePlugin` subclass whose `before_tool_callback` enforces every row for every tool.
  A plugin rather than an agent callback, for the reason part 4.4 measures and adk.dev states — plugin
  hooks are global, agent callbacks are local.
- `TODO(me)`: argument-level checks, so the fence answers *which rows?* and not only *may it?* —
  section 4 is the argument for why the tool name alone is not a permission.
- `TODO(me)`: rate enforcement, and decide where the counter lives. Per process is easy and wrong the
  moment there are two processes; say what you chose and why in the docstring.

**`tests/test_permissions.py`**

- `TODO(me)`: a test that a tool with no row is **refused**, not allowed. That single test is the
  difference between a table and a suggestion.
- `TODO(me)`: a test that the refusal for *not yours* and the refusal for *not there* are byte-for-byte
  identical, so part 4.5's leak cannot come back through a well-meaning error message.
- `TODO(me)`: a test that the fence sees a call made by a **delegated** agent, not only by the desk.
  Part 5.3 is why this is not the same test as the first one.

Do not copy the lab scripts into `sutra/`. `_fake.py` and `_desk.py` are instruments for this day.

---

## §5 The eval that must be able to fail

```bash
cd days/day-68-least-privilege-tools/lab
uv run python gate.py; echo "exit: $?"
```

Six properties a least-privilege desk must have. Five are **red** today because
`sutra/permissions.py` is the build brief; one is green, and it is worth reading — *refund is not
granted to the desk* passes because the table says so and the desk genuinely does not hold it, which
is the one property today's lab already has.

Note the deliberate choice in the gate's own docstring: a check that cannot run reports as a
**failure** rather than as "skipped", because a skipping check goes green on the day the module is
deleted. That is Principle 11 applied to the eval itself.

The checks that can be driven red **on demand** are exercised in their parts:

```bash
uv run python table.py --drift
uv run python where.py
uv run python leak.py
```

The first shows a tool with no row, the second shows the forbidden close succeeding through a second
tool, and the third shows a refusal telling a prober which tickets exist.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

`_fake.py`'s `ScriptedLlm` is a real `BaseLlm` subclass, so every permission check in this day runs
inside the real ADK runtime — real tools, a real toolset, real plugin hooks, real function dispatch —
with a model that returns a scripted function call and increments a counter. Nothing contacts a
provider (Principle 15).

The rate limits the day **reports** are real numbers from `permissions.json` — 60/min for reads,
20/min for `close_ticket`, 10/min for `send_reply` — because a rate that is not the rate you would
actually enforce is not a permission. Nothing today spends a request against them.

---

## §7 Traps

1. **Writing the permission as an instruction in the prompt.** A rule in words is advice the model may
   follow; a tool it was never offered is a boundary — part 1.4.
2. **Granting a capability without a scope.** `read_ticket` with no *which rows?* is a grant over the
   whole archive, and Days 49 and 50 made that archive large — part 2.2.
3. **Forgetting rate.** A grant that answers *may it?* and not *how much of it?* has no upper bound,
   and on a free tier the bound is the quota — part 2.3.
4. **Trimming a full tool list instead of building an allowlist.** The two produce the same list today
   and diverge the moment somebody adds a tool — part 3.1.
5. **Expecting a polite refusal from an absent tool.** ADK raises `ValueError` and the run ends. That
   is correct and it is not free, so the denial has to be designed — part 3.3.
6. **Checking the tool name and not the argument.** `read_note("../private/payroll.csv")` is a
   permitted tool doing a forbidden thing; resolve the path first — parts 4.1 and 4.2.
7. **Putting the check inside the tool it guards.** It protects that tool and nothing else, and the
   second tool that reaches the same effect never sees it — parts 4.4 and 5.1.
8. **A refusal that distinguishes *not yours* from *not there*.** The refusal becomes an enumeration
   oracle: 4 of 6 ids classified from the messages alone — part 4.5.
9. **Assuming a narrow helper bounds the system.** Control comes back, and the chain ends in the tool
   the helper was not allowed to call. A permission table is a property of the system, not of one
   agent in it — parts 3.4 and 5.3.
10. **Treating a grant as evidence.** The table says what the desk may do; only the audit says what it
    did, and least privilege is maintained by subtracting — part 6.2.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| Plugin hook list and scope | <https://adk.dev/plugins/> | `BasePlugin` implements `before_tool_callback`, `after_tool_callback`, `on_tool_error_callback` among others, and verbatim: *"Plugin hooks are global. You register a Plugin once on the `Runner`, and its hooks apply universally to every Agent, Model, and Tool it manages. In contrast, Agent Callbacks are local, configured individually on a specific agent instance."* — the fact part 4.4 turns into a rule |
| Toolset filtering | <https://adk.dev/tools-custom/mcp-tools/> | the `tool_filter` surface parts 3.1 and 3.2 use, checked on the day it is used (Principle 8) |
| `doi:10.1145/54289.871709` record | <https://api.crossref.org/works/10.1145/54289.871709> | title *"The Confused Deputy" (or why capabilities might have been invented)*, ACM SIGOPS Operating Systems Review 22(4), 36–38, October 1988 — copied into `docs/PAPERS.md` and the paper document, never from memory (§17.4.1 rule 5) |
| `google-adk` latest | <https://pypi.org/pypi/google-adk/json> | `2.8.0`; this repo pins `2.7.1`, carried forward as the Day 65 freshness finding rather than upgraded mid-phase (Principle 14) |

Two behaviours this day depends on were **measured** against the installed `2.7.1` rather than read:
what a delegated agent is actually offered under `sub_agents` versus `AgentTool` (parts 3.4 and 5.3),
and what the runtime does when the model calls a tool that is not in the list (part 3.3). Each part
shows the command that produced the answer.

---

## §9 Say it in an interview

*"After the guardrail work we moved the control from reading text to holding authority. The framing
that helped was the confused deputy: our agent acts on instructions we don't control while holding
credentials we do, so the only half we can change is the second one. We wrote a permission table —
one row per tool, saying what it may do, which rows it may touch, how often, whose credential it uses
— as data rather than as branches, so it could be diffed against the tools actually registered. Three
things surprised me. First, the tenant check we'd written inside the close tool was bypassed entirely
by a second tool added later that reached the same effect, so the fence had to move outside every
tool into a plugin. Second, our refusals leaked: distinguishing 'not yours' from 'no such ticket' let
a prober classify four of six ids, and making the two messages identical took it to three, which is
just their own. Third, giving a helper agent a narrow toolset bounded the helper and not the system —
the chain came back to the desk and called the tool the helper wasn't allowed to call. And the last
piece was subtraction: the table says what we may do, the audit says what we did, and the gap is where
a permission nobody needs is hiding."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have run the commands rather than read
them. `./m done 68` refuses to commit until they are.

The day is finished when you can look at any tool in the desk and answer all five columns of its row
without opening the file — and when you can say why a check that lives inside a tool is a check you
should expect to be bypassed.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 68 | 2026-09-06 | SEC-10, SEC-11 | 22 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth 68` is green over the twenty-two parts and the paper.
`lab/gate.py` is **red** on five of its six checks by design — `sutra/permissions.py` is the build
brief. The repository-wide `⚠️` carried since Day 15 is unchanged: `tests/test_persona.py` still fails
ruff `I001`, and it is the learner's own file, which no generated day may edit.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one row, checked live today:

```text
| "The Confused Deputy" (or why capabilities might have been invented) | doi:10.1145/54289.871709 | 1988 | 2026-09-06 | 68 | `days/day-68-least-privilege-tools/papers/01-the-confused-deputy.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 68: permissions and least privilege for tools - closes SEC-10, SEC-11
```

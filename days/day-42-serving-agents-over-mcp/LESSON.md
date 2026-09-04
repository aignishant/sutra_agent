---
day: 42
phase: 6
phase_name: "MCP II: production"
title: "Serving agents over MCP"
ids: ["MCP-33", "ADK-26"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 42 — Serving agents over MCP

> **Yesterday (Day 41):** what a server *declares*. `sutra_mcp/capabilities.py` turned an accidental
> capability declaration into a decision, and MCP Apps were parked with their reasons written down.
> **Today:** the arrow turns round one more time. `to_mcp_server` puts Sutra's own agent behind an
> MCP tool name, and the interesting part is not that one line does it — it is the four things that
> line decided for you, the reach it published, and what one call now costs in generations.
> **Tomorrow (Day 43):** stateless by default. `sutra_mcp/app.py` becomes deploy-shaped so any
> instance answers any request — which is exactly the property the server you build today does not
> have.

---

## §1 Where we are

For ten days MCP has run one way. Sutra mounts other people's servers, filters their tools, checks
their declarations and hardens itself against their failures. Day 34 turned that round halfway:
`lookup_ticket` and `search_kb` went on the wire, so a stranger can now read Sutra's archive.

Today the whole thing goes on the wire.

Think about the person two desks away who knows the ticket archive better than anybody. When you are
stuck you roll your chair over, say four words, and get three back. None of that is written down
anywhere, because everyone who needs to know is already in the room. Then the second branch opens,
three hundred kilometres away, and asks whether they can ask her things too.

The answer is yes, and the exchange changes completely. The question has to say which system. It has
to say who is asking. She cannot ask a quick follow-up and get an answer in four seconds. And nobody
at the other end can see her working — they see that a reply arrived, or that one did not.

**Her knowledge did not change. What changed is that the people using it are no longer in the room.**
That is today, and it is one function call: `to_mcp_server(agent)` returns a server exposing one tool
that takes one string.

Five things to know before you read a part.

**Today writes project code and installs nothing.** `sutra_mcp/agent_server.py` is yours to type.
`google-adk` stays at `2.7.1` and `mcp` at `1.29.1`; `git diff pyproject.toml uv.lock` must be empty
when you finish.

**Today breaks the convention every MCP day since 34 has followed.** Days 35, 36, 37, 39 and 41 each
added a module beside `sutra_mcp/server.py` and one line inside `build_server()`. `to_mcp_server`
cannot do that, because it *builds* a server rather than registering into one. So `sutra_mcp/` ends
today with **two servers**, deliberately, and the gate checks they stay apart. Section 1 is that
argument.

**The central decision is not the API, it is what you put behind it.** Agent-as-tool means the caller
*uses* you: one request, one reply, no identity, no conversation. Agent-as-peer means the caller
*talks to* you, with a task that has a lifetime and the right to be asked a question back. MCP gives
you the first and A2A gives you the second, and section 3 makes you choose for Sutra with reasons
before it tells you the verdict.

**A served agent costs quota, and this is the day that prices it.** A plain MCP tool reads a database:
zero generations. A served agent runs a model loop: one generation to decide plus one for every tool
result it reads back — three for an ordinary desk answer. On twenty free-tier generations a day, forty
calls of real traffic means **six answered and thirty-four refused**. Section 4 does that arithmetic
and section 4.3 says what you have to publish because of it.

**And the API you are using is provisional.** `to_mcp_server` is decorated `@experimental`, lives in
a private module, and has no page on adk.dev — its A2A counterpart `to_a2a` does. Its import sits
behind a `try/except ImportError` that logs the real reason at `DEBUG`, so a missing optional package
arrives as *"cannot import name `to_mcp_server`"* from a file that plainly contains it. Part 6.1
measured that, both ways.

---

## §2 The map

Nineteen parts in six sections, plus one paper part. This is a lab day with two IDs, so the sections
are **the mechanism, then the two IDs meeting, then the price, then the failures, then production**:
section 1 is what `to_mcp_server` builds, section 2 is what actually crosses the boundary, section 3
is the agent-as-tool versus agent-as-peer decision (ADK-26), section 4 is what one call costs,
section 5 breaks it on purpose, and section 6 is what has to be true before a stranger may call it.
The day climbs `foundation → working → production`.

### Section 1 — `01-the-back-office`: what one function call builds (MCP-33)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The colleague you can now phone](parts/01-the-back-office/1.1-the-colleague-you-can-now-phone.md) | What changes when the callers are not in the room | `foundation` |
| 1.2 | [Twelve words in the classifieds](parts/01-the-back-office/1.2-twelve-words-in-the-classifieds.md) | One tool, one string, one sentence of prose | `foundation` |
| 1.3 | [The hall that came with its own chairs](parts/01-the-back-office/1.3-the-hall-that-came-with-its-own-chairs.md) | Four services and a user id you did not choose | `working` |
| 1.4 | [The counter by the side door](parts/01-the-back-office/1.4-the-counter-by-the-side-door.md) | Why today adds a second server, not a third tool | `working` |

### Section 2 — `02-what-crosses-the-counter`: the served surface (MCP-33)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The enquiry slip with one box](parts/02-what-crosses-the-counter/2.1-the-enquiry-slip-with-one-box.md) | One required string, no output schema, no validation | `working` |
| 2.2 | [The interpreter who relays the last sentence](parts/02-what-crosses-the-counter/2.2-the-interpreter-who-relays-the-last-sentence.md) | What survives conversion, and the tool calls that do not | `working` |
| 2.3 | [The table you may leave your books on](parts/02-what-crosses-the-counter/2.3-the-table-you-may-leave-your-books-on.md) | One session per connection, and nowhere to declare it | `working` |
| 2.4 | [💥 The errand you sent someone on](parts/02-what-crosses-the-counter/2.4-the-errand-you-sent-someone-on.md) | One string reaches the whole sub-agent tree | `production` |

### Section 3 — `03-tool-or-peer`: the decision this day exists for (ADK-26)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The machine and the manager](parts/03-tool-or-peer/3.1-the-machine-and-the-manager.md) | Used versus talked to, and what each shape costs | `working` |
| 3.2 | [A note handed over, and money sent](parts/03-tool-or-peer/3.2-a-note-handed-over-and-money-sent.md) | The four irreducible differences, and the third outcome | `production` |
| 3.3 | [The guillotine and the press](parts/03-tool-or-peer/3.3-the-guillotine-and-the-press.md) | Sutra's verdict, and the one lever the API gives you | `production` |

### Section 4 — `04-what-a-call-costs`: priced in generations (MCP-33)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The kettle and the car](parts/04-what-a-call-costs/4.1-the-kettle-and-the-car.md) | Zero against `1 + round-trips`, on one tool list | `working` |
| 4.2 | [The family data pack](parts/04-what-a-call-costs/4.2-the-family-data-pack.md) | Forty calls, twenty generations, six answers | `production` |
| 4.3 | [The notice on the ration shop board](parts/04-what-a-call-costs/4.3-the-notice-on-the-ration-shop-board.md) | The only channel MCP gives you for a rate limit | `production` |

### Section 5 — `05-failure-lab`: three ways it breaks on purpose

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 Two signs, both saying Room 12](parts/05-failure-lab/5.1-two-signs-both-saying-room-12.md) | A served agent whose tool is its own server | `production` |
| 5.2 | [💥 You knock and walk away](parts/05-failure-lab/5.2-you-knock-and-walk-away.md) | The caller gives up; the server finishes and pays | `production` |
| 5.3 | [💥 The price sticker underneath](parts/05-failure-lab/5.3-the-price-sticker-underneath.md) | 543 characters of your quota body, to a stranger | `production` |

### Section 6 — `06-in-production`: before a stranger may call it

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The school in two sheds](parts/06-in-production/6.1-the-school-in-two-sheds.md) | Four risks in an experimental, undocumented, guarded import | `production` |
| 6.2 | [Red before you serve](parts/06-in-production/6.2-red-before-you-serve.md) | Six statements, an exit code, and three honest gaps | `production` |

### The paper — read it after the parts

| Paper | Identifier | What it claims |
| --- | --- | --- |
| [A note on distributed computing](papers/01-a-note-on-distributed-computing.md) | `doi:10.1007/3-540-62852-5_6` | A local call and a remote call differ in kind, not in degree |

**Read the paper last, and read it after 6.2.** That is Principle 4 at the scale of a day: you put a
process boundary in front of an agent by hand and paid for all four of the differences before anybody
told you they had names. Part [3.2](parts/03-tool-or-peer/3.2-a-note-handed-over-and-money-sent.md)
carries the citation as an address; the paper part is where it is taught.

**Read the sections in order.** Section 2 needs section 1's server object, section 3's verdict spends
every fact sections 1 and 2 established, section 4 is the argument section 3 could not make without
numbers, and section 5's three failures are the four differences from 3.2 arriving one at a time.

---

## §3 Setup — run this

**No package is added today and none is upgraded.** `google-adk` stays at `2.7.1`, `mcp` at `1.29.1`.
PyPI has `google-adk` at `2.8.0` as of 2026-09-05 (§8); nothing is bumped, because a day pins only
what it installs and an experimental API behind an unread version diff is a Principle 14 decision
rather than a day's decision.

```bash
# 1 - the day's lab
cd days/day-42-serving-agents-over-mcp
mkdir -p lab lab/papers/a-note-on-distributed-computing

# 2 - section 1 and 2: what the one call builds and what crosses it
touch lab/served_surface.py lab/connections.py lab/blocks.py lab/granted.py

# 3 - section 4: the arithmetic
touch lab/price.py

# 4 - section 5: the three failures
touch lab/recurse.py lab/slow.py lab/throttled.py

# 5 - section 6: the experimental door and the gate
touch lab/guarded_import.py lab/gate.py

# 6 - the paper demo
touch lab/papers/a-note-on-distributed-computing/warehouse.py
touch lab/papers/a-note-on-distributed-computing/shop.py
cd -

# 7 - the module you are about to fill (you type every line)
touch sutra_mcp/agent_server.py

# 8 - the freshness gate, before anything else
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "2026-07-28" | head -1

# 9 - the symbol this whole day depends on, checked in the installed package
uv run python -c "from google.adk.tools.mcp_tool import to_mcp_server; import inspect; print(inspect.signature(to_mcp_server))"
```

**Step 8 is the same gate Days 32, 33, 34 and 41 ran.** Everything in this day is written against
revision **2026-07-28**. If that page names a newer current revision, stop and amend the plan before
writing code (Principle 14). It printed `2026-07-28` on 2026-09-05.

**Step 9 is today's specific gate and it is not optional.** `to_mcp_server` has no documentation page
(§8), so the installed source is the specification. If that command raises `ImportError: cannot
import name 'to_mcp_server'`, do not start debugging your import statement — turn DEBUG logging on
first, and read part [6.1](parts/06-in-production/6.1-the-school-in-two-sheds.md).

**`sutra_mcp/` is yours and it is shared.** Day 34 owns `__init__.py`, `server.py` and `tools.py`;
days 35, 36, 37, 39 and 41 each added a module and one line in `build_server()`. **Today does not.**
`agent_server.py` is a second server with its own entry point, and
[1.4](parts/01-the-back-office/1.4-the-counter-by-the-side-door.md) is the argument.

**`sutra/mcp/` is untouched today.** That is the client package from Days 33 and 40. Today is entirely
about being a server.

---

## §4 Build brief

### The project code — `sutra_mcp/agent_server.py`, and you type every line

One file, three public symbols, one entry point.

| Symbol | Shape | What it must do |
| --- | --- | --- |
| `SERVED_AGENT_NAME` | `str` | the served tool's name, the server's name, and the session key |
| `SERVED_DESCRIPTION` | `str` | the four-job description from [4.3](parts/04-what-a-call-costs/4.3-the-notice-on-the-ration-shop-board.md) |
| `REACH` | `list[str]` | every tool one `request` string can set in motion |
| `build_agent_server()` | `-> FastMCP` | build the served surface. Start nothing. |

- `build_agent_server() -> FastMCP` returns; it never blocks. The `run(transport="stdio")` call goes
  under `if __name__ == "__main__":` and nowhere else
  ([1.2](parts/01-the-back-office/1.2-twelve-words-in-the-classifieds.md)).
- **Build the agent you serve, do not serve `build_desk()`.**
  [3.3](parts/03-tool-or-peer/3.3-the-guillotine-and-the-press.md) is the argument, and it is the
  single most important line of the day.
- **Import the tool implementation, do not retype it.** `search_kb` already exists in `sutra/loop.py`
  and has since Day 3. One implementation, two doors.
- `sutra_mcp/server.py` gains **nothing**. No import, no line in `build_server()`. The gate checks.

**`TODO(me)` markers left for you:**

- **1.3** — decide whether to pass your own `Runner` or accept the four in-memory services ADK
  builds. If you pass your own, write the comment beside `session_service` that Day 47 will come back
  to. Then write down, in one sentence, why passing a `Runner` does **not** fix `mcp_user`.
- **2.1** — write the guard that rejects an empty or absurdly long `request` **before** a generation
  is spent, and decide where it lives: a `before_agent_callback`, a wrapping `BaseAgent`, or the
  agent's instruction. Say what each choice costs.
- **2.2** — decide how a caller reconstructs what the agent did, given that every tool call is
  dropped by the converter. Name the field you put in the answer text and where it is logged.
- **2.4** — the `reach` walk in `lab/granted.py` reads `tool.__name__`, which works for bare
  functions. `build_desk()` returns an agent holding a `SkillToolset`. Write the version that walks a
  toolset, and say what it should do with a tool it cannot name.
- **3.3** — write `SERVED_INSTRUCTION` for an agent whose input is hostile by default. Then say which
  sentence of it you would still not trust, and what enforces that sentence instead.
- **4.3** — choose `SERVED_CALLS_PER_DAY` and decide where the counter lives. Then decide whether to
  reach into the returned server's tool manager to set `annotations.readOnlyHint` and
  `idempotentHint`, given that `to_mcp_server` leaves both `null` — and write down the cost of
  depending on an internal to say a true thing.
- **5.1** — write the startup check that refuses to mount an MCP server whose address is this
  server's own. Then say what it does **not** catch, and what would.
- **5.3** — extend Day 34's `FORBIDDEN` list with the tokens a provider error can leak, and decide
  which day owns turning it into a test over every model call path.
- **6.2** — make the gate walk the real agent tree and compare it with `REACH`, instead of trusting
  the constant. Then add one check the gate does not make today, and say why you chose that one.

### The lab — ten scripts and one paper demo, all of which run, none of which call a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/served_surface.py` | the whole declaration a caller receives, as JSON | 1.1, 1.2, 2.1, 4.3 |
| `lab/connections.py` | two calls on one connection, two on another; the session and the user id | 1.3, 2.3 |
| `lab/blocks.py` | three events in, two blocks out; the progress arm and the deaf arm | 2.2 |
| `lab/granted.py` | one tool seen, four tools reached — and the narrowed arm | 2.4, 3.3 |
| `lab/price.py` | generations per call, and forty calls against twenty | 4.1, 4.2 |
| `lab/recurse.py` | a served agent whose one tool is its own server, guarded and not | 5.1 |
| `lab/slow.py` | three round-trips against a two-second timeout, and the patient arm | 5.2 |
| `lab/throttled.py` | the real 429 body escaping, and the guarded arm | 5.3, 4.3 |
| `lab/guarded_import.py` | the swallowed `ImportError`, with DEBUG off and on | 6.1 |
| `lab/gate.py` | the day's six statements, as an exit code | 1.4, 3.3, 6.2 |
| `lab/papers/a-note-on-distributed-computing/warehouse.py` | one function, and a socket in front of it | the paper |
| `lab/papers/a-note-on-distributed-computing/shop.py` | the same three reservations, local and remote | the paper |

These are teaching material and they are given complete in the parts. Type them, run them, and break
them where the *Check yourself* sections ask you to.

---

## §5 The eval that must be able to fail

Four checks with exit codes or paired arms. All of them on zero model calls.

**The gate** is the day's definition of done, and it is red until you have written the module:

```bash
uv run python days/day-42-serving-agents-over-mcp/lab/gate.py; echo "exit: $?"
```

Measured on 2026-09-05, before anything was written:
`- sutra_mcp.agent_server is not importable: ModuleNotFoundError: No module named
'sutra_mcp.agent_server'`, then `findings: 1`, then `exit: 1`. When it prints `findings: 0` and
`exit: 0`, six statements are true of `sutra_mcp/agent_server.py`. Then break exactly one on purpose:
add `refund` to `REACH` and watch `one `request` string reaches write tools: ['refund']`.

**The recursion ablation** is the most expensive failure of the day, and both arms must be run:

```bash
uv run python days/day-42-serving-agents-over-mcp/lab/recurse.py
uv run python days/day-42-serving-agents-over-mcp/lab/recurse.py --guarded
```

`agent runs executed: 8` against `agent runs executed: 1` — and **the caller sees `run 1 answered` in
both arms**, with `isError: False` in both. Eight runs on the real desk is twenty-four generations
against a ceiling of twenty, so the first request of the day would have ended the day, and nothing on
the caller's side would have shown it.

**The leak ablation** is the security check, and both arms must be run:

```bash
uv run python days/day-42-serving-agents-over-mcp/lab/throttled.py
uv run python days/day-42-serving-agents-over-mcp/lab/throttled.py --guarded
```

543 characters of the provider's `RESOURCE_EXHAUSTED` body with `isError: True`, against 32
characters and `isError: False`. Read the unguarded output and list every fact about your
infrastructure a stranger now has.

**The paper demo**, whose two arms are the whole argument:

```bash
cd days/day-42-serving-agents-over-mcp/lab/papers/a-note-on-distributed-computing
REMOTE=0 uv run python shop.py
REMOTE=1 uv run python shop.py
```

`reservations the caller believes it made: 3` with `units actually gone from the shelf: 3` in the
local arm, against `3` and **`4`** in the remote arm. Same function, same three calls, same retry
rule, one process boundary.

**And the rest, each of which has a named break in its own part:**

```bash
uv run python days/day-42-serving-agents-over-mcp/lab/served_surface.py
uv run python days/day-42-serving-agents-over-mcp/lab/connections.py
uv run python days/day-42-serving-agents-over-mcp/lab/blocks.py
uv run python days/day-42-serving-agents-over-mcp/lab/blocks.py --deaf
uv run python days/day-42-serving-agents-over-mcp/lab/granted.py
uv run python days/day-42-serving-agents-over-mcp/lab/granted.py --narrowed
uv run python days/day-42-serving-agents-over-mcp/lab/price.py
uv run python days/day-42-serving-agents-over-mcp/lab/price.py --tools-only
uv run python days/day-42-serving-agents-over-mcp/lab/slow.py
uv run python days/day-42-serving-agents-over-mcp/lab/slow.py --patient
uv run python days/day-42-serving-agents-over-mcp/lab/guarded_import.py
uv run python days/day-42-serving-agents-over-mcp/lab/guarded_import.py --debug
```

Three of those have a break named in their part: delete `description=` from `served_surface.py` and
read what the world is told about your agent; change `blocks.py`'s final PNG MIME type to
`application/pdf` and watch which block type comes back; raise `recurse.py`'s `CEILING` to 20 and
multiply the run count by three.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-05).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all ten lab scripts, every flag | **0** |
| both arms of the paper demo | **0** |
| the gate, before and after | **0** |
| `sutra_mcp/agent_server.py` itself | **0** |
| **Total planned** | **0 of 20** |

**Zero, on the day whose whole subject is what a generation costs — and that is the point.** Every
agent in every lab script is a plain `BaseAgent` that yields events it wrote itself, because the
structure of what `to_mcp_server` does is identical whether or not there is a model behind it: the
same one tool, the same one string, the same conversion, the same session-per-connection, the same
reach. What a model adds is the price, and the price is arithmetic
([4.1](parts/04-what-a-call-costs/4.1-the-kettle-and-the-car.md)) rather than an experiment.

Two things genuinely need a live call and neither is a required step. **Attaching the served server
to a real agent and watching a model choose it** costs two or three generations, is worth doing once,
and teaches nothing this day has not shown you. **Watching a real 429 come out of a served tool**
costs your remaining quota by definition; `lab/throttled.py` injects the body Day 2 recorded instead,
and says so at the top of the file.

The only network traffic is two HTTPS GETs in §3 and §8. Everything else runs on your machine, and
most of it does not open a socket.

**Cost: $0.**

---

## §7 Traps

- **`to_mcp_server`'s arguments after `agent` are keyword-only.** `to_mcp_server(agent, "name")`
  raises `TypeError: to_mcp_server() takes 1 positional argument but 2 were given` (1.2).
- **`name=` sets the server name *and* the tool name.** One careless string does two kinds of damage
  (1.2).
- **An agent with no `description` publishes `Run the <name> agent.`** — ADK's fallback, on the wire,
  as your entire public interface, with no warning (1.2).
- **`runner=None` builds four in-memory services and picks your app name for you** (1.3).
- **Every caller is `mcp_user`.** `_MCP_USER_ID` is a module constant with no argument that changes
  it, and passing your own `Runner` does not help, because the constant is read in `_run_agent`
  (1.3, 2.3).
- **`app_name` defaults to the agent's name**, so renaming the agent orphans every session behind the
  served door (1.3).
- **`to_mcp_server` returns a server, so it cannot follow the `register_x(server)` convention.**
  Today adds a second server, not a line in `build_server()` (1.4).
- **The input schema is one required `string` and nothing else.** `""` is a valid call and spends a
  generation (2.1).
- **`outputSchema` is `null`**, because `structured_output=False` (2.1).
- **Every `function_call` and `function_response` part is dropped** by the converter, silently, with
  no warning and no progress notification (2.2).
- **Intermediate text is sent as progress only if the caller sent a `progressToken`**, and vanishes
  otherwise. Two independent reasons it can disappear (2.2).
- **Every inline blob shares one URI**, `resource://adk-agent/inline-data`, so two attachments in one
  reply collide for any client keying on it (2.2).
- **Sessions are keyed on the MCP connection**, so a reconnect silently starts a new conversation with
  no error (2.3).
- **The get-then-create on the session map has no lock**, so two concurrent first calls on one
  connection can both create a session (2.3).
- **The reach is the whole sub-agent tree.** A sub-agent someone else maintains gaining a write tool
  changes what a stranger's string can do, with no diff in your repository (2.4).
- **`annotations`, `title`, `icons`, `meta` and `execution` are all `None` on a served tool.**
  `FastMCP.add_tool` accepts them; `to_mcp_server` passes none, so `idempotentHint` — the one field
  that could say "do not retry me" — is left null (4.3).
- **There is no cost, rate or capacity field anywhere in the `Tool` type.** The description is the
  only channel (4.3).
- **A served agent can be given a toolset pointing at its own server**, and nothing anywhere checks.
  One request becomes as many runs as the quota allows, and the caller sees a normal answer (5.1).
- **A caller's timeout does not stop the server.** The agent finishes, spends every generation, and
  writes the reply to a connection that has gone (5.2).
- **`read_timeout_seconds` is per client session, not per call**, so one number covers every tool on
  that connection (5.2).
- **An unhandled 429 escapes as 543 characters of the provider's quota body**, naming your provider,
  your tier, your quota metric and your ceiling (5.3).
- **`to_mcp_server` is `@experimental` and undocumented on adk.dev**, while its counterpart `to_a2a`
  has a page (6.1).
- **The whole `mcp_tool` export block sits in one `try/except ImportError` logging at `DEBUG`**, so a
  missing optional package arrives as *"cannot import name `to_mcp_server`"* from a file that
  contains it (6.1).
- **`google-adk` is at `2.8.0` on PyPI and this repository is pinned at `2.7.1`.** An experimental
  API across an unread version diff is a Principle 14 decision, not a `uv sync --upgrade` (§8, 6.1).

---

## §8 Verify before you code

Fetched or run on **2026-09-05**, the day this was written.

**The specification — the freshness gate:**

- `https://modelcontextprotocol.io/specification/versioning` — still names **2026-07-28** as the
  current revision. The gate in §3 passes and no amendment is required. Note the command needs
  `curl -sL`: the page redirects, and without `-L` the grep finds nothing and looks like a failure.

**adk.dev — read, and the finding is an absence:**

- `https://adk.dev/tools-custom/mcp-tools/` — the MCP tools page. Headings: *What is Model Context
  Protocol (MCP)?*, *Key considerations*, *Prerequisites*, *Using MCP servers with ADK agents (ADK as
  an MCP client) in adk web*, *Build an MCP server with ADK tools (MCP server exposing ADK)*,
  *Advanced use cases*, *Deploy Agents with MCP Tools*. It covers ADK as a client, and hand-building
  an MCP server around individual ADK tools. **It does not mention `to_mcp_server`.**
- `https://adk.dev/tools/mcp-tools/` — redirects to the page above.
- `https://adk.dev/mcp/` — the MCP overview. It says *"Exposing ADK Tools via an MCP Server: How to
  build an MCP server that wraps ADK tools"* and defers to the page above. **It does not mention
  `to_mcp_server` either.**
- `https://adk.dev/a2a/quickstart-exposing/` — **`to_a2a` is documented**, with its signature, an
  *Under the hood* section and a parameters table. This asymmetry is the whole of
  [6.1](parts/06-in-production/6.1-the-school-in-two-sheds.md)'s third risk: the counterpart
  has a page and this function does not.
- `https://adk.dev/sitemap.xml` — searched for every URL containing `mcp`, `a2a`, `expose` or
  `serve`. Fourteen matches, listed above or A2A-language variants. There is no agent-to-mcp guide.

**So the installed package is the specification, and every claim in this day was read out of it:**

- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/_agent_to_mcp.py` — the whole of sections 1 and
  2. `to_mcp_server(agent, *, name=None, instructions=None, runner=None) -> FastMCP`, keyword-only
  after `agent`, decorated `@experimental(FeatureName.MCP_AGENT_SERVER)`. `_MCP_USER_ID = "mcp_user"`
  and `_INLINE_RESOURCE_URI = "resource://adk-agent/inline-data"` as module constants.
  `_build_runner` with its four in-memory services. `_part_to_content` with its three branches and
  `return None` default. `_run_agent`'s `is_final_response()` split and
  `ctx.report_progress(progress=0.0, message=text)`. The `weakref.WeakKeyDictionary()` session map
  keyed on `ctx.session`. `server.add_tool(call_agent, name=..., description=agent.description or
  f"Run the {tool_name} agent.", structured_output=False)` — passing **no** annotations. And the
  docstring sentence *"This is the MCP counterpart of `to_a2a`; it lets harnesses that speak MCP
  drive an ADK agent."*
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/__init__.py` — `__all__ = []` and ten imports
  inside one `try/except ImportError` whose handler is two `logger.debug` calls (6.1).
- `.venv/Lib/site-packages/google/adk/features/_feature_registry.py` — `MCP_AGENT_SERVER =
  "MCP_AGENT_SERVER"` at line 52, configured `FeatureConfig(FeatureStage.EXPERIMENTAL,
  default_on=True)` at line 173.
- `.venv/Lib/site-packages/google/adk/runners.py` — `Runner.__init__` is keyword-only with
  `session_service` **required** and the other three optional, which is why
  [1.3](parts/01-the-back-office/1.3-the-hall-that-came-with-its-own-chairs.md)'s explicit `Runner`
  passes `None` three times rather than omitting them.
- `.venv/Lib/site-packages/google/adk/a2a/utils/agent_to_a2a.py` — `to_a2a`'s signature, read from
  the file. **It does not import**: `ModuleNotFoundError: No module named 'a2a'`, because the `a2a`
  extra is not installed here. Day 89 installs it; nothing is added today.
- `.venv/Lib/site-packages/mcp/server/fastmcp/server.py` — `add_tool(fn, name, title, description,
  annotations, icons, meta, structured_output)`, which is how 4.3 knows the annotations were
  available and not passed.
- `.venv/Lib/site-packages/mcp/types.py` — `Tool` has exactly nine fields: `name`, `title`,
  `description`, `inputSchema`, `outputSchema`, `icons`, `annotations`, `meta`, `execution`.
  `ToolAnnotations` has `title`, `readOnlyHint`, `destructiveHint`, `idempotentHint`,
  `openWorldHint`. `ToolExecution` has `taskSupport`. None of them is a cost or a rate (4.3).
- `.venv/Lib/site-packages/mcp/server/fastmcp/tools/base.py` — `raise ToolError(f"Error executing
  tool {self.name}: {e}") from e`, the line that puts a provider's quota body in front of a stranger
  (5.3). Day 34's 4.3 found it first; this is the day it costs the most.

**Five live commands, re-run today:**

```bash
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "2026-07-28" | head -1
curl -s https://pypi.org/pypi/google-adk/json | uv run python -c "import sys,json;print(json.load(sys.stdin)['info']['version'])"
uv run python -c "from google.adk.tools.mcp_tool import to_mcp_server; import inspect; print(inspect.signature(to_mcp_server))"
uv run python -c "from google.adk.features._feature_registry import FeatureName; print(FeatureName.MCP_AGENT_SERVER)"
uv run python -c "from mcp.types import Tool, ToolAnnotations; print(sorted(Tool.model_fields)); print(sorted(ToolAnnotations.model_fields))"
```

They printed `2026-07-28`; then `2.8.0`; then `(agent: 'BaseAgent', *, name: 'Optional[str]' = None,
instructions: 'Optional[str]' = None, runner: 'Optional[Runner]' = None) -> 'FastMCP'`; then
`FeatureName.MCP_AGENT_SERVER`; then the nine `Tool` fields and the five `ToolAnnotations` fields.

**PyPI is one minor version ahead and nothing is bumped.** `google-adk==2.8.0` exists; this repository
stays at `2.7.1`. The reason is [6.1](parts/06-in-production/6.1-the-school-in-two-sheds.md)'s
last risk: an experimental function can change behaviour without changing its signature, so the bump
is a plan amendment with a read diff behind it, not a side effect of a day that installs nothing.

**One paper, already verified.** `doi:10.1007/3-540-62852-5_6` has its dated row in `docs/PAPERS.md`
and is taught here for the first time. The 1994 Sun Microsystems Laboratories technical report behind
it, **TR-94-29**, has no DOI and is named by report number only.

---

## §9 Say it in an interview

"We had an agent that had only ever been called from our own process, and this was the day we put it
behind MCP so other teams could call it. ADK has a one-liner for it, `to_mcp_server`, and the
interesting part was everything that one line decided without asking.

It publishes exactly one tool taking one string called `request`. No per-field schema, no output
schema, because it turns structured output off. So the tool's description is not documentation, it is
the entire public interface, and we started reviewing it like a function signature. It also builds a
whole runtime for you if you do not pass one: four in-memory services, the session store keyed on the
agent's name, and every caller running as a hard-coded user id called `mcp_user`. That last one is not
configurable, which means an agent behind that door can never enforce a rule about who asked.

The thing I would actually want to be asked about is reach. The caller sees one tool and one string.
What that string can set in motion is every tool on the agent plus every tool of every sub-agent it
can transfer to, transitively — and none of that is in the declaration, so there is nothing for the
caller to filter and nothing for a reviewer to see. We measured it: one tool visible, four functions
reachable, two of which wrote, and one of those was `refund` on a sub-agent. So we did not serve the
real desk. We built a second, read-only agent specifically for the door, because the only enforcement
point the API gives you is which agent you hand it — a rule in the instruction cannot help, since the
agent has no way to tell that a request arrived over MCP rather than from our own runner.

Then the cost, which is the part people miss. A plain MCP tool reads a database: zero model calls. A
served agent is one generation to decide plus one for every tool result it reads back, so three for
an ordinary answer. We are on a free tier with twenty a day, measured off a live 429. Forty calls of
real traffic is a hundred and twenty generations demanded against twenty available: six answered,
thirty-four refused, and the six are whoever was first rather than whoever mattered. And there is no
cost field anywhere in the MCP tool type — the closest is `idempotentHint` in the annotations, which
this function leaves null — so the only channel for telling a caller is prose in the description.

The failure lab found the two I would fix in anyone's codebase. First, a served agent whose toolset
points at its own server: one request became eight agent runs, and the caller got a completely normal
successful answer, so nothing on their side would ever alert. Twenty-four generations against a
ceiling of twenty, from one question. Second, an unhandled 429: the SDK puts `str(exception)` from a
tool body into a text block for the caller, so a stranger's model received 543 characters of our
provider's `RESOURCE_EXHAUSTED` body — our provider, our tier, our quota metric, our ceiling, and a
sentence telling them to check their billing details. Guarded, that becomes 32 characters and
`isError` false, while the operator gets more than before.

And the framing I would defend is the 1997 argument that a local call and a remote call differ in
kind rather than degree. Our demo was one function called two ways with identical signatures, with a
reply dropped after the work was applied: the local arm believed it made three reservations and three
were gone, and the remote arm believed three and four were gone. Nobody wrote a bug. That third
outcome — you cannot tell whether it happened — is why we serve something read-only, and it is why
the peer shape, where a task has a status you can poll, stays on the list for the day somebody needs
it."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and you were honest about it. `./m done 42`
refuses to commit while any box is unticked; it cannot check the honesty.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 42 | 2026-09-05 | MCP-33, ADK-26 | 19 (+1 paper) | <hash> | ⚠️ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded: `google-adk`
stays at `2.7.1`, `mcp` at `1.29.1`, and `gemini-3.7-flash` stays pinned as recorded on 2026-08-26.
PyPI's `google-adk` is at `2.8.0` as of 2026-09-05 (§8) and the bump is a plan amendment with a read
diff behind it, not a side effect of a day that installs nothing. The `a2a` extra is **not** added:
`to_a2a` is named and read here, never imported, and Day 89 is the day that installs it.

**`docs/PAPERS.md`** — **no new rows.** `doi:10.1007/3-540-62852-5_6` already has its dated row,
verified 2026-09-04, and this is the day that teaches it. `doi:10.1145/2408776.2408794` is named once
in prose, in the paper part, and already has its row for Day 44.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**The commit:**

```text
day 42: serving agents over MCP - closes MCP-33, ADK-26
```

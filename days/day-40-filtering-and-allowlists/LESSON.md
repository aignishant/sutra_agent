---
day: 40
phase: 6
phase_name: "MCP II: production"
title: "Tool filtering, allowlists and the MCP security posture"
ids: ["MCP-16", "MCP-17", "SEC-03"]
principles: [2, 4, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 20
generated: "2026-09-04"
status: written
lab_scaffolded: true
commit: ""
---

# Day 40 — Tool filtering, allowlists and the MCP security posture

> **Yesterday (Day 39):** database tools. The ticket archive moved into SQLite, `sutra_mcp` grew
> hand-written read-only SQL tools, and the MCP Toolbox for Databases was weighed against them and
> parked. The uncomfortable image it ended on was a general query tool held back by a flag.
> **Today:** Sutra stops accepting boxes of tools it did not write. Every server gets a written
> allowlist, applied at toolset construction, in one module — and you find out exactly which attacks
> that stops and which it does not.
> **Tomorrow (Day 41):** server capabilities and MCP Apps — what a server declares about itself, and
> the sandboxed-iframe interfaces a tool can ship.

---

## §1 Where we are

A deny-list is a list of things you thought of. An allowlist is a list of things you agreed to.

Today they are the same list. You wrote down the two tools that worried you, or you wrote down the two
tools you wanted, and either way the vendor's server behaves identically and everything works.

The two lists come apart on a Tuesday, when the vendor ships a release and one more tool appears in
`tools/list`. Nobody attacked anything. A team decided the assistant should be able to file incidents
as well as read status, and shipped it. Under the deny-list, your agent can now file public incident
records with a vendor. Under the allowlist, it cannot, and nothing happened at all.

**The server adding a tool is not a hypothetical. It is a Tuesday.** That is the whole of this day's
central argument, and the name for choosing the second list is *fail-safe defaults* — a phrase from a
1975 paper that this day ends on.

Four things to know before you read a part.

**The filter is on your side of the wire.** ADK filters inside `get_tools()`, *after* `tools/list` has
returned everything the server has. So the descriptions of the tools you dropped did reach your
process. What the filter protects is the model's context, not the network — and being precise about
that is what makes the pin in section 3 possible at all.

**Two spellings of the same argument fail in opposite directions, both silently.**
`tool_filter=[]` admits **every** tool, because ADK's rule begins `if not self.tool_filter: return
True` and an empty list is falsy. A tuple or a bare string admits **none**, because it falls off the
end of the same rule and returns `False`. Neither raises. Measured against a real server: `[]` handed
the agent a write tool that a two-name list kept out, and `("check_status", "list_regions")` handed it
nothing at all.

**An allowlist compares names and a model reads descriptions.** A server can keep every name you
approved and rewrite what those names say. The allowlist reports nothing — correctly, because
comparing names is its job — and the only thing in this day that notices is a digest pinned at review
time. One command, one line of output, and it is the entire rug-pull defence.

**And the honest half.** The allowlist stops tools you did not approve, completely. It does nothing
about a description that was hostile on its first day, nothing about text a tool *returns*, and
nothing about two innocent tools that are an exfiltration path together. The MCP specification's
confused-deputy section is entirely about OAuth proxies; the tool-boundary version has no mitigation
in the specification today. Section 6 says so plainly rather than implying a defence exists.

---

## §2 The map

Twenty parts in six sections, plus **one paper**, read last. The day climbs
`foundation → working → production`: section 1 is the posture and where the filter sits, section 2 is
the argument ADK actually gives you, section 3 is what happens when the server moves, section 4 is the
module Sutra writes, section 5 is the failure lab, and section 6 is the posture the filter is only one
part of.

### Section 1 — `01-the-list-you-agreed-to`: the posture, and where the filter sits (MCP-16, SEC-03)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The list of things you thought of](parts/01-the-list-you-agreed-to/1.1-the-list-of-things-you-thought-of.md) | Deny-list against allowlist, and the one word that differs | `foundation` |
| 1.2 | [A tool list is a stranger's text](parts/01-the-list-you-agreed-to/1.2-a-tool-list-is-a-strangers-text.md) | Listing is exposure; a description is prompt input | `foundation` |
| 1.3 | [The filter is on your side of the wire](parts/01-the-list-you-agreed-to/1.3-the-filter-is-on-your-side.md) | It protects the model, not the network | `working` |

### Section 2 — `02-the-filter-in-adk`: the argument the framework gives you (MCP-16, SEC-03)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [One argument, three spellings](parts/02-the-filter-in-adk/2.1-one-argument-three-spellings.md) | `None`, a list, a callable — and what a fourth type does | `working` |
| 2.2 | [The rule that reads the room](parts/02-the-filter-in-adk/2.2-the-rule-that-reads-the-room.md) | `ToolPredicate`: per tool, per listing, with context | `working` |
| 2.3 | [The names the framework keeps](parts/02-the-filter-in-adk/2.3-the-names-the-framework-keeps.md) | Four reserved names, skipped with a warning | `working` |
| 2.4 | [💥 The empty list that admits everything](parts/02-the-filter-in-adk/2.4-the-empty-list-that-admits-everything.md) | Truthiness, and a filter that fails open | `production` |

### Section 3 — `03-when-the-server-changes`: the list moves underneath you (MCP-17)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The Tuesday a tool appeared](parts/03-when-the-server-changes/3.1-the-tuesday-a-tool-appeared.md) | The same posture against two versions of one server | `working` |
| 3.2 | [💥 The name held, the sentence moved](parts/03-when-the-server-changes/3.2-the-name-held-the-sentence-moved.md) | The rug pull, and the only check that sees it | `production` |
| 3.3 | [The list you kept is the list you trust](parts/03-when-the-server-changes/3.3-the-list-you-kept-is-the-list-you-trust.md) | 3 listings → 1, and the staleness window it buys | `production` |

### Section 4 — `04-the-policy-module`: `sutra/mcp/filtering.py` (MCP-17)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [One door, and a check that there is one](parts/04-the-policy-module/4.1-one-door-and-a-check-there-is-one.md) | An AST scan that names every other construction site | `working` |
| 4.2 | [A policy you can diff](parts/04-the-policy-module/4.2-a-policy-you-can-diff.md) | The record: launch, allow, writes, pins, review date | `working` |
| 4.3 | [`deny` inside the allowlist](parts/04-the-policy-module/4.3-deny-inside-the-allowlist.md) | A refinement that structurally cannot admit anything | `working` |

### Section 5 — `05-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The container that admits nothing](parts/05-failure-lab/5.1-the-container-that-admits-nothing.md) | A tuple, and an agent that starts with no tools | `production` |
| 5.2 | [💥 Filtered after it was read](parts/05-failure-lab/5.2-filtered-after-it-was-read.md) | 36 characters against 103, same allowlist | `production` |
| 5.3 | [💥 The pattern that matched more than it named](parts/05-failure-lab/5.3-the-pattern-that-matched-more.md) | An unanchored regex admits four tools, not two | `production` |

### Section 6 — `06-the-posture`: what the filter is one part of (SEC-03, MCP-17)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 Two servers, one tool name](parts/06-the-posture/6.1-two-servers-one-tool-name.md) | Shadowing, and `tool_name_prefix` | `production` |
| 6.2 | [The attacks a filter does not stop](parts/06-the-posture/6.2-the-attacks-a-filter-does-not-stop.md) | Seven rows, three of which have no mitigation | `production` |
| 6.3 | [The host decides, not the server](parts/06-the-posture/6.3-the-host-decides-not-the-server.md) | Annotations are claims; the decision is yours | `production` |
| 6.4 | [What you write down before you connect](parts/06-the-posture/6.4-what-you-write-down-before-you-connect.md) | Eight intake questions, seven of them fields | `production` |

### The paper — read it **after** the parts

| Paper | Identifier | What it argued |
| --- | --- | --- |
| [The protection of information in computer systems](papers/01-protection-of-information.md) | `doi:10.1109/PROC.1975.9939` (1975) | Eight named design principles for protection, of which fail-safe defaults is this whole day |

Principle 4 at the scale of a day: watch a default decide something, *then* read the argument for
choosing it. Fail-safe defaults is [1.1](parts/01-the-list-you-agreed-to/1.1-the-list-of-things-you-thought-of.md)
and [2.4](parts/02-the-filter-in-adk/2.4-the-empty-list-that-admits-everything.md); least privilege is
[1.2](parts/01-the-list-you-agreed-to/1.2-a-tool-list-is-a-strangers-text.md); complete mediation is
what [3.3](parts/03-when-the-server-changes/3.3-the-list-you-kept-is-the-list-you-trust.md) deliberately
breaks; economy of mechanism is
[4.1](parts/04-the-policy-module/4.1-one-door-and-a-check-there-is-one.md).

---

## §3 Setup — run this

**No package is added today, and no package is upgraded.** `git diff pyproject.toml uv.lock` must be
empty when you finish. Everything today is code, policy and reading, against `google-adk==2.7.1` and
`mcp==1.29.1` as already pinned.

```bash
# 1 - the day's lab
cd days/day-40-filtering-and-allowlists
mkdir -p lab/papers/protection-of-information

# 2 - the prop: one file that is three servers
touch lab/vendor_server.py

# 3 - section 1: the posture, the text, the boundary
touch lab/postures.py lab/listing.py lab/resolve.py

# 4 - section 2: what the argument accepts
touch lab/filter_semantics.py lab/predicate.py lab/reserved.py

# 5 - section 3: the server moves
touch lab/pin.py lab/cache.py

# 6 - section 4: the one door
touch lab/one_door.py

# 7 - section 5 and 6: the failures and the posture
touch lab/late.py lab/anchors.py lab/shadow.py

# 8 - the paper demo
touch lab/papers/protection-of-information/catalog.py
touch lab/papers/protection-of-information/mediate.py
cd -

# 9 - the gate, before anything else: has the specification moved?
curl -s https://modelcontextprotocol.io/specification/versioning | grep -o "2026-07-28" | head -1
```

**Step 9 is the gate and it is not ceremony.** This day, the addendum it implements and the days
around it are written against revision **2026-07-28**. If that page names a newer current revision,
stop and amend the plan before writing code (Principle 14).

**One file moves into `sutra/` today**, and you write it: `sutra/mcp/filtering.py`, in the package Day
33 created. Day 44 adds `hardening.py` beside it. Nothing else under `sutra/` or `sutra_mcp/` changes.

**Read the parts in order and the paper last.** Section 2 needs section 1's boundary, section 3 needs
section 2's semantics, and the paper is only worth reading once you have watched a default decide
something.

---

## §4 Build brief

Thirteen lab scripts and one prop, none of which call a model. Each belongs to the part that teaches
it.

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/vendor_server.py` | the prop: a third-party server, in three versions | 3.1 |
| `lab/postures.py` | deny-list against allowlist, on two eras of one tool list | 1.1 |
| `lab/listing.py` | prints every advertised name and description, verbatim | 1.2 |
| `lab/resolve.py` | what an agent is handed, under five filter spellings | 1.3, 2.4, 3.1, 5.1 |
| `lab/filter_semantics.py` | asks the installed framework what each spelling admits | 2.1, 5.1 |
| `lab/predicate.py` | a `ToolPredicate`, asked under two different contexts | 2.2 |
| `lab/reserved.py` | the four reserved names, and a server that collides with one | 2.3 |
| `lab/pin.py` | digests the descriptions you approved; reports what moved | 3.2 |
| `lab/cache.py` | counts listings on the wire, with and without a TTL | 3.3 |
| `lab/one_door.py` | AST scan for toolsets constructed outside the policy module | 4.1 |
| `lab/late.py` | characters of stranger text in context, early against late | 5.2 |
| `lab/anchors.py` | an unanchored allowlist pattern against an anchored one | 5.3 |
| `lab/shadow.py` | two mounts, one name, and what `tool_name_prefix` does | 6.1 |

`lab/papers/protection-of-information/` holds the paper demo — `catalog.py` and `mediate.py` — and it
is **given complete** in the paper part. It is teaching material, not a rep: type it, run both arms,
and compare your output with the transcripts.

**The project file to write:** `sutra/mcp/filtering.py`, in the package Day 33 created. Its public
surface is `allowlist(server_key) -> list[str]`, `deny(names, policy) -> list[str]`, and the one
constructor that applies the filter at toolset construction. The record shape is in
[4.2](parts/04-the-policy-module/4.2-a-policy-you-can-diff.md) and the composition order is in
[4.3](parts/04-the-policy-module/4.3-deny-inside-the-allowlist.md).

**`TODO(me)` markers left for you:**

- **2.1** — decide what `sutra/mcp/filtering.py` asserts about the value it hands to `tool_filter`, and
  write the test that would fail if somebody passed a `set`.
- **2.2** — decide whether Sutra needs the predicate form at all yet, and if not, write down the
  condition under which it will. Day 37 gave the client an identity; that is the trigger.
- **2.3** — write Sutra's own copy of the four reserved names, with the ADK version it was read from,
  and decide what should happen when a server advertises one: a log line, or a refused connection.
- **3.1** — decide what Sutra does with a listing diff: which of new, missing and changed is a review
  request, which is an incident, and who receives each.
- **3.2** — extend the pin to cover the input schema as well as the description, and decide the
  severity split between a rewritten read tool and a rewritten write tool.
- **3.3** — choose a `ttl_seconds` for each server Sutra will reach, and write down the reason beside
  each number. They should not all be the same.
- **4.1** — decide whether `one_door.py`'s successor belongs in Day 45's `tools/mcp_audit.py` or in
  `./m check` directly, and write down what it should do about test code.
- **4.2** — fill in `REGISTRY`, and decide whether `sutra_mcp` itself belongs in the same registry as a
  third party. Write down the reason either way.
- **4.3** — decide what else belongs in `NEVER`, and write the check that a server's `allow` and `deny`
  do not overlap.
- **5.1** — write the startup assertion that the number of resolved tools equals the number of names in
  the policy, and decide where it lives so no call site can skip it.
- **6.2** — write Sutra's one-page threat model for one MCP integration, with a "handled by" column
  that is allowed to say *"nothing — accepted risk"*.
- **6.4** — turn the eight intake questions into a pull-request template, and decide who reviews
  question 2.

---

## §5 The eval that must be able to fail

Six checks with an exit code, all on zero model calls.

**The one-door check is the day's gate**, and it is red before you write the module:

```bash
uv run python days/day-40-filtering-and-allowlists/lab/one_door.py; echo "exit: $?"
```

Measured on 2026-09-04: `doors other than sutra\mcp\filtering.py: 1` and `exit: 1`. That is **red on
purpose** — the module does not exist yet. Write it and it goes green; add an `McpToolset(...)`
anywhere else under `sutra/` and it goes red again with a file and a line number.

**The rug-pull check** is the one that catches what the allowlist cannot:

```bash
uv run python days/day-40-filtering-and-allowlists/lab/pin.py; echo "exit: $?"
VENDOR_V2=1 uv run python days/day-40-filtering-and-allowlists/lab/pin.py; echo "exit: $?"
```

`findings: 0` and `exit: 0` against the reviewed server; `rewritten check_status ... exit: 1` against
Tuesday's. Delete `lab/vendor_pin.json` and run the second one first, and it exits 0 having pinned the
poisoned description as approved — which is the process failure that part warns about.

**The paper demo is the ablation, and both arms must be run:**

```bash
cd days/day-40-filtering-and-allowlists/lab/papers/protection-of-information
FAIL_SAFE=1 uv run --project ../../../../.. python mediate.py; echo "exit: $?"
FAIL_SAFE=0 uv run --project ../../../../.. python mediate.py; echo "exit: $?"
cd -
```

`admitted but never reviewed: []` and `exit: 0` against `['open_incident']` and `exit: 1`, from the
same rules and the same catalogue.

**And the rest, each of which can be broken on purpose:**

```bash
uv run python days/day-40-filtering-and-allowlists/lab/postures.py; echo "exit: $?"
uv run python days/day-40-filtering-and-allowlists/lab/late.py; echo "exit: $?"
uv run python days/day-40-filtering-and-allowlists/lab/anchors.py; echo "exit: $?"
uv run python days/day-40-filtering-and-allowlists/lab/shadow.py; echo "exit: $?"
uv run python days/day-40-filtering-and-allowlists/lab/listing.py
VENDOR_V2=1 uv run python days/day-40-filtering-and-allowlists/lab/listing.py
uv run python days/day-40-filtering-and-allowlists/lab/filter_semantics.py
uv run python days/day-40-filtering-and-allowlists/lab/predicate.py
uv run python days/day-40-filtering-and-allowlists/lab/reserved.py
uv run python days/day-40-filtering-and-allowlists/lab/cache.py
for p in none allow empty string tuple; do
  uv run python days/day-40-filtering-and-allowlists/lab/resolve.py "$p"
done
```

Four of those have a named break in their own part: add `"open_incident"` to `DENY` in `postures.py`
and watch it go green for one Tuesday only; change `ALLOW` in `late.py` to include both tools and watch
the leak go to zero for the wrong reason; add an anchored-looking pattern with no group to `anchors.py`
and watch it leak anyway; swap `get_tools_with_prefix()` for `get_tools()` in `shadow.py` and watch the
prefix appear to do nothing.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all thirteen lab scripts, every posture and both server versions | **0** |
| the paper demo, both arms | **0** |
| **Total planned** | **0 of 20** |

**Zero, and it is the point.** Every claim in this day is about what reaches a model, not about what a
model does with it — and what reaches a model is a list you can print. The only processes started today
are local Python child processes over stdio on your own machine. Your whole day's quota is still there
tomorrow.

**Cost: $0.**

---

## §7 Traps

- **`tool_filter=[]` admits everything.** The selection rule begins `if not self.tool_filter: return
  True`, and an empty list is falsy. Nobody types it; they compute it from a policy record with no
  names filled in (2.4).
- **A tuple, a set or a bare string admits nothing.** Same rule, other end: anything that is neither
  callable nor a `list` falls through to `return False`, and the agent starts with no tools and no
  error (5.1, 2.1).
- **`0` is not "no cache".** `tool_list_cache_ttl_seconds=0` raises
  `ValueError: tool_list_cache_ttl_seconds must be positive, got 0.` The way to write it is `None` (3.3).
- **`get_tools()` does not apply `tool_name_prefix`.** The prefix appears in `get_tools_with_prefix()`,
  which is what the framework calls. Measure with the wrong one and you will conclude the argument does
  nothing (6.1).
- **`errlog` must be a real file.** An `io.StringIO` has no file descriptor for a child process to write
  into, and the connection dies with `io.UnsupportedOperation: fileno` wrapped in a doubled
  `ConnectionError` (3.3).
- **The filter runs on cache hits.** Caching the listing does not weaken the allowlist; it only skips
  the round trip. It does mean a tool the server added is invisible until the entry expires, because
  ADK does not subscribe to `notifications/tools/list_changed` (3.3).
- **An allowlist compares names, and the model reads descriptions.** A rewritten description on an
  allowlisted tool passes every check in this day except the pin (3.2).
- **Reserved names are skipped, not refused.** A server advertising `transfer_to_agent` produces one
  `WARNING` and the connection continues. That is an availability decision with a cost (2.3).
- **The reserved set protects ADK's four names, not yours.** A server advertising `lookup_ticket` sails
  straight through (2.3, 6.1).
- **`re.match` is not the strict one.** It matches at the start, not the whole string. The strict one is
  `re.fullmatch`, or `\A(?:...)\Z` — and without the non-capturing group, alternation binds looser than
  the anchors and you get "starts with A or ends with B" (5.3).
- **`^` and `$` are not `\A` and `\Z`.** `$` also matches before a trailing newline (5.3).
- **A dispatch-time check is not a filter.** It stops the call and not the reading: 36 characters of
  stranger text in context against 103, same allowlist (5.2).
- **`readOnlyHint` is the server's claim about itself.** The specification says clients **MUST** treat
  tool annotations as untrusted unless the server is trusted, which is the question you were asking
  (6.3).
- **`serverInfo.name` is not unique** and **SHOULD NOT** be used to tell two servers apart (6.1).
- **A tool list may vary by the authorization on the request.** The list your reviewer saw is not
  necessarily the list production sees (1.1, 3.2).
- **A pin that re-pins itself is not a check.** Regenerating the digests in the same job that compares
  them produces a check that has never once failed (3.2).
- **An empty `allow` does not mean "not approved yet".** To express that, delete the record and let the
  lookup raise (2.4, 4.2).

---

## §8 Verify before you code

Fetched or run on **2026-09-04**, the day this was written.

**The framework — the authoritative API surface, read rather than guessed:**

- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/mcp_toolset.py` — the real signature:
  `tool_filter: ToolPredicate | list[str] | None = None`, `tool_name_prefix: str | None = None`,
  `tool_list_cache_ttl_seconds: float | None = None`, `errlog: TextIO = sys.stderr`,
  `require_confirmation: bool | Callable[..., bool] = False`. Every argument is keyword-only. The
  docstring for the cache says *"ADK does not subscribe to `notifications/tools/list_changed`, so a
  tool the server adds or removes goes unnoticed until the entry expires."*
- `.venv/Lib/site-packages/google/adk/tools/base_toolset.py` — `_is_tool_selected`, four branches,
  beginning `if not self.tool_filter: return True`. And `ToolPredicate`, a `@runtime_checkable`
  `Protocol` whose call signature is `(tool, readonly_context=None) -> bool`.
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/mcp_tool.py` — `_RESERVED_TOOL_NAMES`, which
  resolves to `['adk_request_confirmation', 'adk_request_credential', 'adk_request_input',
  'transfer_to_agent']`. Re-checked live rather than taken from Day 33.
- `.venv/Lib/site-packages/google/adk/tools/mcp_tool/__init__.py` — both spellings exported,
  `McpToolset` and `MCPToolset`, which is why `lab/one_door.py` looks for both.
- `.venv/Lib/site-packages/mcp/types.py` — `ToolAnnotations.readOnlyHint`, documented as *"If true, the
  tool does not modify its environment."*

**The documentation, fetched live:**

- `https://adk.dev/tools-custom/mcp-tools/` — the page that documents `tool_filter`: *"Optional: Filter
  which tools from the MCP server are exposed"*, and in its production checklist, *"Filter MCP tools
  using `tool_filter` to limit exposed functionality."* The URL under `/docs/` returns 404; this is the
  live path.
- `https://modelcontextprotocol.io/specification/2026-07-28/server/tools` — the tool-list contract. The
  set *"**MAY** change over time"* and *"**MAY** vary by the authorization presented on the request"*;
  servers *"**SHOULD** return tools in a deterministic order"*; `listChanged` notifications go only to
  clients that opened a `subscriptions/listen` stream with `toolsListChanged: true`; clients *"**MUST**
  consider tool annotations to be untrusted unless they come from trusted servers"*; tool-name
  uniqueness *"is scoped to a single server"* and aggregating clients *"**SHOULD** implement a
  disambiguation strategy such as prefixing tool names with a server identifier"*, while
  `serverInfo.name` *"**SHOULD NOT** be relied upon for disambiguation"*. Its user-interaction warning:
  *"there **SHOULD** always be a human in the loop with the ability to deny tool invocations."*
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices` — read in
  full, and the finding is what is **not** in it. It covers the confused deputy **for OAuth proxies**,
  token passthrough, SSRF, state-handle hijacking, local server compromise, authorization-URL
  validation, mix-up attacks and scope minimisation. There is **no section on tool poisoning, on
  descriptions carrying instructions, or on tool-name shadowing**, and no MUST or SHOULD addressing the
  confused deputy at the tool boundary. That gap is section 6's subject and it is reported rather than
  papered over.

**No paper was verified today.** `doi:10.1109/PROC.1975.9939` was assigned with its row already in
`docs/PAPERS.md`, dated 2026-09-04.

**Two things recorded for whoever needs them, not acted on.** Day 32 found that the pinned
`mcp==1.29.1` tops out at protocol revision `2025-11-25` while the specification is at `2026-07-28`;
nothing in this day depends on the difference, because `tools/list` and tool descriptions are unchanged
between them. And ADK's `require_confirmation` exists and is the right shape for Phase 9's approval
gates; it is named in 6.3 and deliberately not built today.

---

## §9 Say it in an interview

"We connect our agent to MCP servers we do not own, and the decision that mattered most was the
default. A deny-list is a list of things you thought of; an allowlist is a list of things you agreed
to. They produce identical output on the day you write them, which is why the argument is hard to win
in a review — the reviewer sees the same answer twice and concludes the choice does not matter. It
comes apart when the server adds a tool, and that is not an attack, it is a Tuesday. We measured it on
a prop: same server, one extra tool that files a public incident record with the vendor, and the
deny-list handed it to the model while the allowlist handed over nothing new.

Two things surprised me in the framework. ADK's selection rule starts `if not self.tool_filter: return
True`, which is a truthiness test, so an empty list takes the same branch as `None` and grants
everything. Nobody types an empty list — they compute one from a policy record with no names filled in
— so the server you have not reviewed yet is the one that ends up unrestricted, which is exactly
backwards. And at the other end, anything that is neither callable nor a `list` falls off the rule and
refuses every tool, so a tuple or a set gives you an agent with no tools and no error. That one is
worse to diagnose, because an agent with no tools does not look broken, it looks like a weaker model —
it answers from training with a polite hedge, and people go and tune the prompt.

The limit I would be clearest about is that an allowlist compares names and the model reads
descriptions. A server can keep every name you approved and rewrite what they say. Our filter reports
nothing, correctly, because comparing names is its job. What catches it is a pin: digests of the
description and schema taken at review time, compared on every listing, failing closed. Two rules for
that — a change opens a review rather than paging somebody, or it gets switched off within a month;
and the re-pin has to be a human commit, because a job that re-pins what it finds is a check that can
never fail.

Beyond that I would be honest about what nothing handles. A description that was hostile on day one is
caught only by a person reading it. Tool *results* we do not defend at all — a result is text that goes
into the context, and filtering natural language written by somebody who can rephrase is a speed bump,
not a control. And combinations: one tool that reads customer records and one that posts somewhere
public are an exfiltration path that no per-tool review sees. The confused deputy at the tool boundary
is the name for the general shape, and the MCP spec's confused-deputy section is entirely about OAuth
proxies — the tool-boundary version has no mitigation in the spec today. So the posture is prevention
where it works, detection where it does not, and approval gates for the rest. Writing down the rows
that say 'nothing' is how the gates get funded."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 40` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it to
someone else without the page open.

**Phase 6's gate** is the full MCP audit of `sutra-core` on Day 45, and today supplies most of what it
audits: a policy record per server, a single construction site, and pinned digests of the text that was
approved. Day 41 is server capabilities, Day 44 hardens the client that carries these calls, and the
`TODO(me)` items about the listing diff and the startup assertion are the decisions those days will
need already made.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 40 | <date> | MCP-16, MCP-17, SEC-03 | 20 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded: `google-adk`
stays at `2.7.1`, `mcp` at `1.29.1`, and `gemini-3.7-flash` stays pinned as recorded on 2026-08-26. No
model was called today.

**`docs/PAPERS.md`** — **no new rows.** `doi:10.1109/PROC.1975.9939` already has its dated row from
2026-09-04, and it is taught here in
[`papers/01-protection-of-information.md`](papers/01-protection-of-information.md).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**The commit:**

```text
day 40: tool filtering, allowlists and the MCP security posture - closes MCP-16, MCP-17, SEC-03
```

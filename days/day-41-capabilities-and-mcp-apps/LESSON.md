---
day: 41
phase: 6
phase_name: "MCP II: production"
title: "Server capabilities and MCP Apps"
ids: ["MCP-18", "MCP-19", "MCP-29"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-04"
status: written
lab_scaffolded: true
commit: ""
---

# Day 41 — Server capabilities and MCP Apps

> **Yesterday (Day 40):** the filter. `sutra/mcp/filtering.py` decided which of a stranger's tools
> Sutra will let a model see, and the security posture that goes with it.
> **Today:** the layer above the tool list. What a server *says* it can do, how a client finds that
> out with no session to hold the answer, why "declared" and "implemented" drift apart — and the
> first official extension, MCP Apps, where a server ships a **user interface** and a stranger's
> code draws pixels inside your host.
> **Tomorrow (Day 42):** the whole desk agent goes on the wire with `to_mcp_server` — agent as tool
> rather than agent as peer.

---

## §1 Where we are

Everything `sutra-mcp` has published so far has been a *thing*: two tools, some resources, some
prompt cards. Today is about the sentence above all of them — the small object a server emits that
says which **families** of methods it answers at all.

Think of a washing machine dial. Six positions, printed on the plastic, and the dial stops at each
one. There is no seventh. Not hidden, not locked — the machine has no drying programme, and the dial
is an honest picture of what is behind it. A capability declaration is that dial: it does not tell
you what is in the drum, it tells you which programmes exist.

Then the awkward half. Nothing in the protocol checks the dial against the machine. A declaration is
something a server **says**, and today you will measure an empty server — nothing registered at all —
declaring three families it cannot serve, because the library's constructor registered the handlers
before you wrote a line. Declared is not implemented, and the gap has a shape you can probe.

And then the newer, stranger half. **MCP Apps** lets a tool point at an HTML page the server also
serves, which the host renders inside the conversation. A stranger's server drawing pixels next to
your product's pixels is the largest thing a server has ever been able to do to a client, and the
only reason it is tolerable is that the page is a **pre-declared template** — fetched, hashed and
reviewable before anything runs — with the data flowing in separately, as data.

Four things to know before you read a part.

**Today writes one project file and installs nothing.** `sutra_mcp/capabilities.py` is yours to type.
`mcp==1.29.1` is already pinned; `git diff pyproject.toml uv.lock` must be empty when you finish.

**Half of MCP Apps cannot run here, and the day says which half.** Every *declaration* in the Apps
specification is expressible on the pinned SDK and section 4 runs it. Nothing that *renders* is:
there is no browser in this repository and no host that implements the bridge. That split is stated
in the lab's own output rather than in a footnote.

**The pin is a revision behind and today is where that costs something.**
[2.2](parts/02-discovery-without-sessions/2.2-the-request-your-sdk-cannot-send.md) greps the
installed package for the four things this day's protocol depends on and finds zero of them. Day 34
measured three of the four first; you reproduce it, because an inherited finding is a claim and a
reproduced one is a fact. **Nothing is bumped** (Principle 14).

**MCP Apps is 🅿️ parked for Sutra, out loud, with a trigger.**
[4.5](parts/04-a-server-that-draws/4.5-parked-why-sutra-ships-no-app.md) gives three reasons and the
condition that re-opens the decision. Parking is a decision with its reason attached, never a shrug.

---

## §2 The map

Nineteen parts in six sections, **no paper part**. One part carries §6 *The paper behind it* as an
address to a paper taught on Day 32. This is a protocol day, so the sections run from *what a
declaration is* to *what a reviewer asks before enabling a stranger's UI*: section 1 is the
declaration itself, section 2 is finding it without a session, section 3 is the gap between promised
and real, section 4 is the Apps extension, section 5 breaks two things on purpose, and section 6 is
what ships. The day climbs `foundation → working → production`.

### Section 1 — `01-what-a-server-declares`: the object itself (MCP-18)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The programmes on the dial](parts/01-what-a-server-declares/1.1-the-programmes-on-the-dial.md) | A family of methods, not a feature and not a tool | `foundation` |
| 1.2 | [Nobody types the declaration](parts/01-what-a-server-declares/1.2-nobody-types-the-declaration.md) | An empty `FastMCP` declares three families | `working` |
| 1.3 | [An extension is a capability with a surname](parts/01-what-a-server-declares/1.3-an-extension-is-a-capability-with-a-surname.md) | `io.modelcontextprotocol/ui`, and the map it lands in | `working` |
| 1.4 | [The client declares too](parts/01-what-a-server-declares/1.4-the-client-declares-too.md) | Every request, 86 bytes, and `-32021` | `working` |

### Section 2 — `02-discovery-without-sessions`: finding out (MCP-18)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [One question instead of three](parts/02-discovery-without-sessions/2.1-one-question-instead-of-three.md) | The capability half of `server/discover` | `working` |
| 2.2 | [The request your SDK cannot send](parts/02-discovery-without-sessions/2.2-the-request-your-sdk-cannot-send.md) | Four greps, four zeroes, one honest gap | `working` |
| 2.3 | [Asking for what was never declared](parts/02-discovery-without-sessions/2.3-asking-for-what-was-never-declared.md) | `-32601`, the no with no retry | `working` |

### Section 3 — `03-declared-versus-implemented`: the gap (MCP-19)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A promise, not a proof](parts/03-declared-versus-implemented/3.1-a-promise-not-a-proof.md) | Three ways a declaration and a server drift | `working` |
| 3.2 | [Probing every promise](parts/03-declared-versus-implemented/3.2-probing-every-promise.md) | Two broken promises, two different wires | `working` |
| 3.3 | [Declared before anything runs](parts/03-declared-versus-implemented/3.3-declared-before-anything-runs.md) | Seven mechanisms, one design stance | `working` |

### Section 4 — `04-a-server-that-draws`: MCP Apps (MCP-29)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [A tool that brings its own window](parts/04-a-server-that-draws/4.1-a-tool-that-brings-its-own-window.md) | `ui://`, the mime profile, and the `_meta` link | `foundation` |
| 4.2 | [The template is declared, the data flows in](parts/04-a-server-that-draws/4.2-the-template-is-declared-the-data-flows-in.md) | Five things a fixed template buys a host | `working` |
| 4.3 | [What the sandbox actually stops](parts/04-a-server-that-draws/4.3-what-the-sandbox-actually-stops.md) | Two controls, and the CSP the host builds | `working` |
| 4.4 | [The dialect spoken through the glass](parts/04-a-server-that-draws/4.4-the-dialect-spoken-through-the-glass.md) | Eighteen methods, and none reaching the server | `working` |
| 4.5 | [🅿️ Why Sutra ships no App](parts/04-a-server-that-draws/4.5-parked-why-sutra-ships-no-app.md) | Three reasons and the trigger to re-open | `production` |

### Section 5 — `05-failure-lab`: two things broken on purpose

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The panel that grew a button](parts/05-failure-lab/5.1-the-panel-that-grew-a-button.md) | Two buttons against one, from the same ticket | `production` |
| 5.2 | [💥 The family that went away](parts/05-failure-lab/5.2-the-family-that-went-away.md) | Withdrawing a family, not a name | `production` |

### Section 6 — `06-in-production`: what ships

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The declaration you keep in git](parts/06-in-production/6.1-the-declaration-you-keep-in-git.md) | `sutra_mcp/capabilities.py` and its audit | `production` |
| 6.2 | [Before a stranger draws on your screen](parts/06-in-production/6.2-before-a-stranger-draws-on-your-screen.md) | Nine questions, six answerable in advance | `production` |

**No paper part today.** [1.4](parts/01-what-a-server-declares/1.4-the-client-declares-too.md) carries
§6 *The paper behind it* as an address to *Principled design of the modern Web architecture*
(`doi:10.1145/514183.514185`, taught on Day 32 at
[`papers/01-modern-web-architecture.md`](../day-32-mcp-stateless-core/papers/01-modern-web-architecture.md)).
A capability declaration riding in `_meta` on every request rather than negotiated once is that
paper's self-descriptive-message argument applied to one field. A paper is taught once in the whole
curriculum; every later day links to it.

**Read the sections in order.** Section 2 needs section 1's declaration, section 3 needs section 2's
`-32601`, section 4's whole security story is section 3's pre-declaration rule with pixels attached,
and section 6 is the two decisions the rest of the day has been building towards.

---

## §3 Setup — run this

**No package is added today, and no package is upgraded.** `mcp` stays at `1.29.1` and `google-adk`
at `2.7.1`. `git diff pyproject.toml uv.lock` must be empty when you finish. §8 says exactly what the
pin costs today; the bump is a plan decision with its own `docs/PACKAGES.md` row, never a side effect
of a day that installs nothing (Principle 14).

```bash
# 1 - the day's lab
cd days/day-41-capabilities-and-mcp-apps
mkdir -p lab

# 2 - section 1: where a declaration comes from, on both sides
touch lab/declared.py lab/client_meta.py

# 3 - section 2: what the pinned SDK will and will not answer
touch lab/undeclared.py

# 4 - section 3: promised against real
touch lab/drift.py

# 5 - section 4: the Apps declaration, and the policy a host derives
touch lab/apps_sketch.py lab/csp.py

# 6 - section 5: the two failures
touch lab/interpolate.py lab/stale.py

# 7 - the day's gate
touch lab/gate.py
cd -

# 8 - the package file you are about to fill (you type every line)
touch sutra_mcp/capabilities.py

# 9 - the freshness gate, before anything else
curl -s https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
```

**Step 9 is the gate and it is the same one Days 32, 33 and 34 ran.** Everything in this day is
written against revision **2026-07-28**. If that page names a newer current revision, stop and amend
the plan before writing code (Principle 14). It printed `specification/2026-07-28` on 2026-09-04.

**`sutra_mcp/` is yours and it is shared.** Day 34 owns `__init__.py`, `server.py` and `tools.py`,
Day 35 added `resources.py` and `prompts.py`, Day 36 `tasks.py`, Day 37 `auth.py`, Day 39
`db_tools.py`. Today adds `capabilities.py`, Day 42 adds `agent_server.py` and Day 43 adds `app.py`.
Every one of those is a module beside the others and **one line inside `build_server()`**, never a
second server, and the import arrow runs one way — `server.py` imports the capability modules and
never the reverse. Day 34's
[1.4](../day-34-building-sutra-mcp-tools/parts/01-the-server-object/1.4-the-shape-later-days-register-into.md)
is the argument.

**`sutra/mcp/` is untouched today.** That is the client package from Days 33 and 40. Every server in
this day's lab is driven by an in-process client over memory streams, because the client is not what
is being taught.

---

## §4 Build brief

### The project code — `sutra_mcp/capabilities.py`, and you type every line

One file, five public symbols.
[6.1](parts/06-in-production/6.1-the-declaration-you-keep-in-git.md) gives every mechanism; the
decisions are yours.

| Symbol | What it must be |
| --- | --- |
| `DECLARED_FAMILIES` | a `frozenset[str]` of the core families `sutra-mcp` intends to declare |
| `EXTENSIONS` | `dict[str, dict[str, Any]]` — extension identifiers claimed, mapped to settings |
| `UI_RESOURCES` | `tuple[str, ...]` — the `ui://` URIs served; empty, per 4.5 |
| `register_capabilities(server) -> None` | Day 34's registration signature, called from `build_server()` |
| `audit(server) -> list[str]` | every disagreement between the intention and the emitted declaration, as sentences, both directions |

- **Follow Day 34's convention exactly.** `register_capabilities(server) -> None` takes a server,
  attaches, returns nothing, and adds **one line** to `build_server()`. It does not construct a
  server and it does not import from `server.py`.
- **Do not fight the SDK.** `FastMCP` calls `create_initialization_options()` with no arguments, so an
  extension claim never reaches the wire on this pin (1.3). The module records the intention; whether
  to reach past the SDK is a `TODO(me)` below, not a thing this day decides for you.
- **`audit()` runs in the gate, never in the constructor.** A declaration mismatch should fail a
  build, not crash a running process (6.1).

**`TODO(me)` markers left for you:**

- **1.2** — decide what `DECLARED_FAMILIES` should contain **given that `FastMCP` will emit
  `tools`, `resources` and `prompts` whatever you write**. Then say what should happen when the two
  disagree, and which of the two you would change.
- **1.3** — decide where `sutra_mcp` records that its extension claim lands in `experimental` rather
  than `extensions` on this pin, so that the day the pin moves the change is one key and not a hunt.
- **2.2** — write down, in two lines, what `capabilities.py` can honestly *do* on `mcp==1.29.1` and
  what it can only record an *intention* about.
- **3.2** — decide how `sutra-mcp`'s own promises get probed: which tools are safe to call with empty
  arguments, which must be skipped because they write, and where that marking lives.
- **4.5** — fill the last two rows of the parking table and add a ninth: *what would you have to be
  able to prove to a security reviewer before an App ships?*
- **5.2** — write `sutra-mcp`'s capability-withdrawal procedure, including the number of milliseconds
  between the two deployments and where that number is recorded.
- **6.1** — decide whether `declaration(server)` — the reader that pulls the emitted capability object
  off a built `FastMCP` — belongs in `capabilities.py` or stays in the lab, and defend the choice.
- **6.2** — answer questions 7, 8 and 9 for Sutra's host, and say which of the three you are least
  confident about.

### The lab — nine scripts, all of which run, none of which call a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/declared.py` | four servers, four declarations, including an empty `FastMCP` | 1.1, 1.2, 1.3 |
| `lab/client_meta.py` | the client's `_meta` envelope, with and without the UI extension | 1.4 |
| `lab/undeclared.py` | one declared family, one undeclared, and the error each gives | 2.1, 2.3 |
| `lab/drift.py` | every promise called once; two of four do not hold | 3.1, 3.2 |
| `lab/apps_sketch.py` | the `ui://` resource, the `_meta` link, the `visibility` field | 3.3, 4.1, 4.2, 4.4, 6.2 |
| `lab/csp.py` | the Content-Security-Policy a host derives from `_meta.ui.csp` | 4.3, 6.2 |
| `lab/interpolate.py` | one ticket body, two ways to get it on a screen | 5.1 |
| `lab/stale.py` | a capability family withdrawn, in one deployment and in two | 5.2 |
| `lab/gate.py` | the day's six assertions about `sutra_mcp/capabilities.py`, as an exit code | 4.5, 6.1 |

These are teaching material and they are given complete in the parts. Type them, run them, and break
them where the *Check yourself* sections ask you to.

---

## §5 The eval that must be able to fail

Three checks with exit codes, all on zero model calls.

**The gate** is the day's definition of done, and it is red until you have written the module:

```bash
uv run python days/day-41-capabilities-and-mcp-apps/lab/gate.py; echo "exit: $?"
```

Measured on 2026-09-04, before anything was written: `- sutra_mcp.capabilities is not importable:
ImportError: cannot import name 'capabilities' from 'sutra_mcp'`, `findings: 1`, `exit: 1`. When it
prints `findings: 0` and `exit: 0`, six statements are true of `sutra_mcp/capabilities.py`. Then break
exactly one on purpose — add `"logging"` to `DECLARED_FAMILIES` — and read the finding that names it.

**The promise probe** is the check Day 45's audit grows out of, and it is red by design:

```bash
uv run python days/day-41-capabilities-and-mcp-apps/lab/drift.py; echo "exit: $?"
```

`promises: 4  broken: 2`, exit `1`. Add `"export_archive"` to `IMPLEMENTED` and it becomes
`broken: 1`, still exit `1`. Fix the resource too and it goes green — which is the point: the exit
code follows the promises, not the code.

**The withdrawal ablation** is the production check, and both arms must be run:

```bash
uv run python days/day-41-capabilities-and-mcp-apps/lab/stale.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/stale.py --two-deploys
```

Both arms end at `declares : ['tools']` and `-32601: Method not found`. The difference is the middle
row of the second arm, where the declaration is unchanged and the caller gets a retirement message it
can act on. Same removal, two very different weeks for whoever depends on you.

**And the rest, each of which has a named break in its own part:**

```bash
uv run python days/day-41-capabilities-and-mcp-apps/lab/declared.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/client_meta.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/undeclared.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/apps_sketch.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/csp.py
uv run python days/day-41-capabilities-and-mcp-apps/lab/interpolate.py
```

Add a tool to arm D of `declared.py` and watch the declaration not change; set `record_verdict`'s
visibility to `["model", "app"]` in `apps_sketch.py` and say what a prompt-injected model could then
do; add `html.escape` to `improvised` in `interpolate.py` and say what is still wrong.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all nine lab scripts, every flag | **0** |
| the promise probe and the withdrawal ablation | **0** |
| `sutra_mcp/capabilities.py` and the gate | **0** |
| **Total planned** | **0 of 20** |

**Zero, and it could not be otherwise.** A capability declaration is a JSON object; an error code is
an integer; a button count is a substring count. Every server in this day runs in the same process as
its client over memory streams — no subprocess, no socket, no port. The only network traffic in the
whole day is the HTTPS GET in §3 that checks the specification has not moved, plus whatever you spend
reading the pages in §8.

**Cost: $0.**

---

## §7 Traps

- **A capability is a family, not a feature.** `tools` promises that `tools/list` and `tools/call`
  answer; it promises nothing about how many tools there are, and an empty list is a successful call
  (1.1).
- **Absence is the declaration.** A family is declared by its key existing, never by a `true`. Test
  with `in`, never with `== True` (1.1, 2.1).
- **An empty `FastMCP` declares three families.** Eight handlers registered by a one-argument
  constructor, nothing implemented (1.2).
- **The derivation tests the `list` handler only.** A `prompts/get` handler with no `prompts/list`
  declares nothing; a `prompts/list` with no `get` declares the whole family (1.2).
- **`ResourcesCapability(subscribe=False)` is hard-coded** in the SDK's derivation, whatever you
  registered (1.2).
- **The Apps extension is identified as `ui`, not `apps`.** Any check written against the string
  `apps` matches nothing (1.3).
- **`mcp==1.29.1` has no `extensions` field.** A claim lands in `experimental`, and `FastMCP` never
  sends that map at all — `create_initialization_options()` is called with no arguments on both
  transports (1.3).
- **Client capabilities are required on every request.** Omit them and a conforming server returns
  `-32602` with HTTP `400`; declare too few and it returns `-32021` with
  `data.requiredCapabilities` (1.4).
- **`_meta` goes inside `params`,** never beside it. A top-level `_meta` is silently not there (1.4).
- **`serverInfo` is self-reported.** The specification says do not change behaviour on it and do not
  make security decisions with it (2.1).
- **`ttlMs` is milliseconds** and it is on the declaration too, not only on lists (2.1).
- **`server/discover`, `ttlMs`, `cacheScope`, `resultType` and `DiscoverResult` are all absent from
  the pinned SDK** — five greps, five zeroes (2.2).
- **A `server/discover` sent to a legacy server comes back `-32602 Invalid request parameters`,** an
  error about parameters for a problem with the method, because the message matched no member of a
  17-way request union (2.2).
- **`-32601` is the no with no useful retry.** `-32602` means fix the arguments, `-32021` means add a
  capability, `-32601` means go elsewhere (2.3).
- **A broad `except` around a list call turns a read timeout into "this server has no prompts"** —
  Principle 10's failure mode exactly (2.3).
- **A tool handler that raises comes back as a *successful* call** with `isError: true`, so nothing
  counting JSON-RPC errors sees it (3.1, 3.2).
- **A resource handler that raises comes back with error code `0`** — a code the specification does
  not define, from the SDK's last-resort `except Exception` branch, carrying `str(exception)` (3.2).
- **A probe that sends `{}` to every tool will be red forever** on any server whose tools need
  arguments, and dangerous on any server whose tools write (3.2).
- **A tool list that varies per caller violates the specification** and produces a `-32602` on a call
  whose arguments match a schema the server really sent — to somebody else (3.3).
- **A `ui://` resource built per read cannot be pinned, hashed or reviewed,** even with the text
  escaped, and it breaks the host's cache (4.2, 5.1).
- **`visibility: ["app"]` takes a tool out of the model's world entirely.** That is how the tool
  recording a human's approval becomes unreachable by prompt injection (4.1, 4.2).
- **`'unsafe-inline'` is in the Apps CSP formula by design,** because an App is a self-contained
  document; the compensating control is that the document is fixed and reviewed (4.3).
- **An absent `_meta.ui.csp` means the restrictive default, not a free-for-all.** A host may narrow
  the policy and must never widen it (4.3).
- **One `resourceDomains` entry widens five directives at once** (4.3).
- **A pinned template digest does not cover a script loaded from a CDN.** The reviewed page can
  execute code written after the review (4.2, 4.3).
- **A panel that does not check `event.origin` will act on anything that can post to it,** and the
  check must be an exact match, never a prefix (4.4).
- **A host that forwards a panel's `tools/call` without the model's filter has a hole in its
  allowlist shaped like a button** (4.4, 6.2).
- **`ui/update-model-context` lets a server-authored page write into what the model reads next
  turn.** Legitimate, and the first thing to ask about in a review (4.4, 6.2).
- **`.innerHTML` inside a correct template reintroduces the whole injection** in the one file that
  has been reviewed (5.1).
- **Removing the last member of a family removes the family,** and a stale client gets `-32601` with
  no message for the model rather than the `isError` a removed tool would give (5.2).
- **The `ttlMs` you chose is the gap between the two withdrawal deployments** (5.2).
- **`audit()` called from `build_server()` turns a typo in a constant into a crash loop.** It belongs
  in the gate (6.1).
- **Conditional registration makes the declaration environment-dependent** — right in CI, wrong in
  production (6.1).

---

## §8 Verify before you code

Fetched or run on **2026-09-04**, the day this was written.

**The specification — the freshness gate and the five pages this day is built on:**

- `https://modelcontextprotocol.io/specification/versioning` — the current revision is **2026-07-28**.
  It has not moved; the gate in §3 passes and no amendment is required.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning` — *"There is no
  negotiation handshake"*; the `UnsupportedProtocolVersionError` example with code `-32022`; the
  **MUST/MAY** asymmetry on `server/discover`; and the whole of extension negotiation, including the
  `extensions` field, the reverse-DNS identifier rule, the `io.modelcontextprotocol/ui` example with
  `{"mimeTypes": ["text/html;profile=mcp-app"]}`, and the fallback **MUST** quoted in 1.3 and 4.1.
- `https://modelcontextprotocol.io/specification/2026-07-28/server/discover` — the full request and
  reply, verbatim in 2.1: `resultType`, `supportedVersions`, `capabilities`,
  `_meta['io.modelcontextprotocol/serverInfo']`, `instructions`, `ttlMs`, `cacheScope`; the *"instead
  of probing with separate `tools/list`, `prompts/list`, and `resources/list` requests"* sentence; and
  the `serverInfo` **SHOULD NOT** caution.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/index` — the `_meta` key-name rules
  and the reserved-prefix rule quoted in 1.3; the per-request protocol field table with
  `protocolVersion` and `clientCapabilities` **required**; the `-32602`-for-a-missing-field rule; the
  `MissingRequiredClientCapabilityError` (`-32021`) **MUST** quoted in 1.4; the error-code partition
  (`-32000`–`-32019` legacy, `-32020`–`-32099` reserved); and the statelessness paragraph.
- `https://modelcontextprotocol.io/extensions/apps/overview` — the four reasons for an App over a web
  page; the four-step flow (UI preloading, resource fetch, sandboxed rendering, bidirectional
  communication); the sandbox's exact list of what it prevents, quoted in 4.3; the *"host controls
  which capabilities your app can access"* sentence quoted in 4.4; and the note that the `App` class
  is a convenience wrapper rather than a requirement.
- `https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx` —
  SEP-1865, the extension's own specification: the identifier `io.modelcontextprotocol/ui`, the
  `ui://` scheme rule, the mime type `text/html;profile=mcp-app`, the tool `_meta.ui` fields
  (`resourceUri`, `visibility` with its two values and its default), the resource `_meta.ui` fields
  (`csp` with `connectDomains` / `resourceDomains` / `frameDomains` / `baseUriDomains`, `permissions`,
  `prefersBorder`, `domain`), the **ten required CSP directives** implemented verbatim in `lab/csp.py`
  and the *"hosts must never allow undeclared domains"* rule, and the complete `ui/` method list in
  4.4's table.

**The installed SDK — the authoritative API surface, read rather than guessed:**

- `.venv/Lib/site-packages/mcp/types.py` — `ServerCapabilities` with its seven fields and
  `model_config = ConfigDict(extra="allow")` (1.1); `ClientCapabilities` with `sampling`,
  `elicitation`, `roots` and `tasks` (1.4); `PromptsCapability`, `ResourcesCapability`,
  `ToolsCapability`; the error-code constants including `METHOD_NOT_FOUND = -32601` (2.3). **No
  `extensions` field**: `'extensions' in ServerCapabilities.model_fields` is `False`.
- `.venv/Lib/site-packages/mcp/server/lowlevel/server.py` — `get_capabilities` with its docstring
  *"Convert existing handlers to a ServerCapabilities object"*, the `ListPromptsRequest` /
  `ListResourcesRequest` / `ListToolsRequest` membership tests and the hard-coded `subscribe=False`
  (1.2); `create_initialization_options(notification_options=None, experimental_capabilities=None)`
  (1.3); and the `except Exception` branch that returns `ErrorData(code=0, message=str(err))` (3.2).
- `.venv/Lib/site-packages/mcp/server/fastmcp/server.py` — the two calls to
  `self._mcp_server.create_initialization_options()` **with no arguments**, which is why a `FastMCP`
  cannot declare an extension on this pin (1.3).
- `.venv/Lib/site-packages/mcp/shared/memory.py` — `create_connected_server_and_client_session`, which
  is how every server in this day's lab is driven with no subprocess and no socket.

**Five live commands, run today:**

```bash
curl -s https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
cd .venv/Lib/site-packages/mcp && for s in "server/discover" "ttlMs" "cacheScope" "resultType" "DiscoverResult"; do printf '%-16s %s\n' "$s" "$(grep -rn "$s" . | wc -l)"; done; cd -
uv run python -c "from mcp.types import LATEST_PROTOCOL_VERSION as l; from mcp.shared.version import SUPPORTED_PROTOCOL_VERSIONS as v; print(l, v)"
uv run python -c "from mcp.types import ServerCapabilities as C; print(sorted(C.model_fields)); print('extensions' in C.model_fields)"
uv run python -c "import typing; from mcp.types import ClientRequest; print(len(typing.get_args(ClientRequest.model_fields['root'].annotation)))"
```

They printed `specification/2026-07-28`; then **`0` for all five strings**; then
`2025-11-25 ['2024-11-05', '2025-03-26', '2025-06-18', '2025-11-25']`; then
`['completions', 'experimental', 'logging', 'prompts', 'resources', 'tasks', 'tools']` and `False`;
then `17`.

**What that gap costs, stated plainly.** `sutra-mcp` does not implement `server/discover`, which the
current revision makes a **MUST**; a client can only read its declaration out of the deleted
`initialize` handshake. It sends no `ttlMs`, no `cacheScope` and no `resultType`, so a modern client
treats everything it returns as immediately stale. It cannot put an extension identifier on the wire
at all through `FastMCP`. Day 34 measured three of those from the server side and this day reproduces
all five from the package side. **Nothing is bumped**: PyPI's `mcp` is at `2.1.1` and speaks
`2026-07-28`, but that is a major version change to the library every file in `sutra_mcp/` imports,
and Principle 14 says the plan is amended before the code.

**No ADK symbol is used anywhere in this day.** Today is entirely protocol-side and the only library
imported is `mcp`. Day 33 owns the client and its `McpToolset`.

**No paper was verified today.** The single identifier cited — `doi:10.1145/514183.514185` — already
has a dated row in `docs/PAPERS.md` and is taught on Day 32. It is an address here, not a lesson.

---

## §9 Say it in an interview

"By this point our MCP server had tools, resources and prompts on the wire. This was the day we looked
at the sentence above all of them — the capability declaration, the small object that says which
families of methods a server answers at all.

The thing worth knowing is that it is *derived*, not written. The SDK walks its own registered request
handlers and emits one key per family it finds. Which sounds fine until you measure it: we constructed
a completely empty server, no tool, no resource, no prompt, and it declared three families. Eight
handlers registered by a one-argument constructor. Nobody decided that, a convenience layer did, and
it was our public contract.

So we separated two words that get used interchangeably. Declared is what a server says. Implemented
is what it does. There is nothing in the protocol that checks one against the other — no conformance
step, no signature — and they drift in three ways: over-declaring, which is usually a library rather
than a person; under-declaring, which is worse because it fails safe and nobody reports a feature they
cannot see; and staleness, where the declaration was true when it was cached. We wrote a probe: read
the declaration, list each family, call every entry once, count the promises that do not hold. Two out
of four on our test server, and the interesting part was that the two failures came back down
different wires. A tool whose handler raises comes back as a *successful* call with `isError: true`,
so nothing in an error dashboard moves. A resource whose handler raises comes back as a JSON-RPC error
with code zero — which is not a code the specification defines; it is the SDK's last-resort branch for
an escaped exception, and it puts `str(exception)` on the wire.

The client side has its own asymmetry that I think is the neatest thing in the 2026 revision. A server
declares once, because a declaration is a fact about the deployment. A client declares on *every
request*, in `_meta`, because there is no session to hold it in and the next request may reach an
instance that has never seen it. And the rule that makes that worth sending is that a server must not
rely on a capability the client did not declare — if it needs one that is missing it returns
`-32021` with the missing names in the error data, rather than starting work it cannot finish. We
measured the cost: about eighty-six bytes a request for one extension claim, forever, with nothing
amortised. That is the honest price of any instance being able to answer anything.

Then the newer half, MCP Apps. A server can ship a user interface — an HTML page it serves as an
ordinary resource at a `ui://` URI, which the host renders in a sandboxed iframe inside the
conversation, with the tool pointing at it through `_meta.ui.resourceUri`. What makes it defensible is
that the template is *pre-declared*: the host can fetch it before the tool is ever called, hash it,
show it to a reviewer, cache it and refuse it by policy. Five things, all of which need the bytes to
exist in advance. We proved the counterfactual rather than asserting it — the same ticket body,
rendered through a per-call template, produced two Approve buttons and an `onclick` handler, and
through a fixed template with the body sent as data it produced one button and none. The payload is
still there in the safe version; it has just moved from a position where it is code to a position
where it is a value.

The two details I would want to be asked about. First, `visibility`: a tool marked app-only is not in
the model's tool list at all, so the tool that records a human's approval cannot be reached by prompt
injection however persuasive the ticket. Second, the sandbox is two controls, not one — the iframe
sandbox stops the page reaching into the host, and a Content-Security-Policy built from the resource's
own declaration stops it reaching into the network, starting at `default-src 'none'` and adding only
origins the server named. A host may narrow that and must never widen it, and an absent declaration
means the restrictive default.

We parked shipping an App, deliberately and in writing, with three reasons and a trigger. Our one
UI-shaped problem — a human approving a ticket closure — is already solved by elicitation, which gives
us a typed verdict rather than a prettier one. An App needs a browser and a Node toolchain our budget
does not have. And rendering one means our *client* declares the UI extension, which is a standing
permission for every server we mount to draw pixels in front of our users, not just for our own. The
trigger to re-open it is a decision that needs several things compared side by side, because
elicitation renders a form and not a comparison.

The last honest thing: our pinned SDK is a revision behind, and this was the day that stopped being a
version number. We grepped the installed package for the five things this day's protocol depends on —
`server/discover`, `ttlMs`, `cacheScope`, `resultType`, `DiscoverResult` — and got zero for all five.
So the module we shipped, `capabilities.py`, does not try to change what the library emits. It records
what we *intend* to declare, in version control, with a function that returns the differences between
the intention and reality in both directions, as sentences. It runs in the build gate and never in the
constructor, because a declaration mismatch should fail a deploy rather than crash a running process."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 41` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it
to someone else without the page open.

**Phase 6's gate** is the full MCP audit of `sutra-core`, on Day 45. Today builds two of the things
that audit will read: a declaration Sutra decided on rather than inherited, and a probe that turns
"what does this server claim" into "which of its claims hold". Day 42 puts the whole desk agent on the
wire and adds one more line to `build_server()`; the `TODO(me)` items about the withdrawal procedure
and the host's `ui/` allowlist are the decisions the rest of Phase 6 needs already made.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 41 | <date> | MCP-18, MCP-19, MCP-29 | 19 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded: `mcp` stays at
`1.29.1`, `google-adk` at `2.7.1`, and `gemini-3.7-flash` stays pinned as recorded on 2026-08-26. The
five-way SDK gap in §8 is measured here rather than fixed here; the bump to `mcp==2.1.1` is a plan
amendment with its own row, not a side effect of a day that installs nothing. **No npm package is
added** — the MCP Apps SDK and its local host are Node projects, which Addendum 02 puts out of scope,
and 4.5 is the parking decision that follows from that.

**`docs/PAPERS.md`** — **no new rows.** `doi:10.1145/514183.514185` already has its row and is taught
on Day 32; this day cites it once, as an address, in 1.4.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**The commit:**

```text
day 41: server capabilities and MCP Apps - closes MCP-18, MCP-19, MCP-29
```

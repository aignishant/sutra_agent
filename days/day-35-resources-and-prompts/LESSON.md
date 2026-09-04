---
day: 35
phase: 5
phase_name: "MCP I: the protocol"
title: "Resources and prompts"
ids: ["MCP-07", "MCP-08", "MCP-09"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-04"
status: written
lab_scaffolded: true
commit: ""
---

# Day 35 — Resources and prompts

> **Yesterday (Day 34):** `sutra-mcp` served its first tools over the wire. `sutra_mcp/server.py` and
> `sutra_mcp/tools.py` exist, `build_server()` returns a server, and `lookup_ticket` and `search_kb`
> answer a stateless `tools/call`.
> **Today:** the other two surfaces. Sutra's data gets addresses a program can hold, Sutra's house
> wording gets a name any host can invoke, and the question Day 32 left open — *should `lookup_ticket`
> stop being a tool?* — gets answered with its cost as well as its benefit.
> **Tomorrow (Day 36):** long jobs. Work that cannot finish inside one request returns a task handle,
> and the client polls `tasks/get` instead of holding a line open.

---

## §1 Where we are

At the petrol pump, you are not allowed to touch the nozzle.

You pull in, and then you wait to catch the attendant's eye. He is filling somebody else, so you wait a
little longer. When he comes, you say how much you want, and he does it, and it is fine. The system
works and it has worked for years.

But you cannot check the air in your tyres without asking. You cannot read the price board without him
walking over to tell you the number, because the board is behind the counter facing the other way. And
on a busy evening, when three cars come in at once, you sometimes drive off having asked for less than
you meant to — not because anybody refused you, but because you had one moment to ask and you used it
on the wrong thing.

That is `sutra-mcp` this morning. **Everything it publishes is a tool**, which means every single
interaction — including *"give me the text of ticket 4521"*, a thing that changes nothing and whose
address is already known — costs a decision the model has to make and can get wrong.

Four things to know before you read a part.

**The rule you are learning is about who reaches first, not about what the data is.** A tool is
something the model may *do*. A resource is something the host may *read*. A prompt is something the
person may *invoke*. The same ticket can sit behind two of those doors and a `close_ticket` can only
ever sit behind one, and the reason is consent rather than tidiness.

**Two doors, not a swap.** `lookup_ticket` gains a twin — `ticket://4521` — and does not go away,
because a host that reads no resources would otherwise lose the ticket entirely. That answer has a
price and section 1 states it in full: one store read through two code paths, two miss rules that are
deliberately different, and two rows in Day 45's audit forever.

**The framework will quietly break your error codes.** The specification says a resource that does not
exist **MUST** come back as `-32602`. Write exactly that, drive your own server over stdio, and read
what arrives: `code=0`, your message wrapped twice in somebody else's prefix, your `data` gone. The
same server written on the low-level `Server` returns `code=-32602` and the URI. Same intent, one
decorator apart, and you can only find out by looking at the wire.

**And "subscribe" cannot mean what it used to.** With no held session there is nowhere to keep a
subscriber list, so the 2026-07-28 revision replaced `resources/subscribe` with a long-lived
`subscriptions/listen` stream that the client opens, names its filter on, and must re-send after every
reconnect. The held connection did not vanish; it became something you have to ask for and pay for.
Section 4 prices all three answers and picks the one a stateless server can keep.

---

## §2 The map

Nineteen parts in six sections, **no paper part** — two are cited as addresses to papers taught
earlier. The day climbs `foundation → working → production`: section 1 is the design rule and the
decision it forces, sections 2 and 3 are the two new surfaces on the wire, section 4 is staying fresh
with nobody holding a connection, section 5 is the failure lab and section 6 is what ships.

### Section 1 — `01-who-initiates`: the design line, and the decision it forces (MCP-09)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The hand that reaches first](parts/01-who-initiates/1.1-the-hand-that-reaches-first.md) | Three surfaces, sorted by who moves first | `foundation` |
| 1.2 | [What a door costs](parts/01-who-initiates/1.2-what-a-door-costs.md) | Twelve decisions against zero, and three silent misses | `foundation` |
| 1.3 | [Should `lookup_ticket` stop being a tool?](parts/01-who-initiates/1.3-should-lookup-ticket-stop-being-a-tool.md) | Day 32's open question, answered with its price | `working` |

### Section 2 — `02-the-shelf`: resources on the wire (MCP-07)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [An address, not a call](parts/02-the-shelf/2.1-an-address-not-a-call.md) | A URI is a name, and a name works without you | `foundation` |
| 2.2 | [What comes back from a read](parts/02-the-shelf/2.2-what-comes-back-from-a-read.md) | `contents` is always a list, and each item has its own type | `working` |
| 2.3 | [The miss that must be an error](parts/02-the-shelf/2.3-the-miss-that-must-be-an-error.md) | `-32602` against `code=0`, from one decorator | `working` |
| 2.4 | [One label for a whole family](parts/02-the-shelf/2.4-one-label-for-a-family.md) | Templates promise more addresses than you own | `working` |

### Section 3 — `03-the-card`: prompts on the wire (MCP-08)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The words the house owns](parts/03-the-card/3.1-the-words-the-house-owns.md) | The server writes, the person decides | `foundation` |
| 3.2 | [Arguments are declared, not guessed](parts/03-the-card/3.2-arguments-are-declared.md) | A name, a sentence, a boolean — and no schema at all | `working` |
| 3.3 | [What a prompt hands back](parts/03-the-card/3.3-what-a-prompt-hands-back.md) | Messages with roles, and the role that does not exist | `working` |
| 3.4 | [The card that points at the shelf](parts/03-the-card/3.4-the-card-that-points-at-the-shelf.md) | Embed or link — 244 bytes against 205, and why that is not the argument | `working` |

### Section 4 — `04-freshness`: staying current with nobody on the line (MCP-07)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Every read carries its own expiry](parts/04-freshness/4.1-every-read-carries-its-expiry.md) | A read is cacheable, and 12 of 12 fields are missing | `working` |
| 4.2 | [Subscribing with nobody on the line](parts/04-freshness/4.2-subscribing-with-nobody-on-the-line.md) | 2400 requests, 40 held connections, or a TTL | `production` |
| 4.3 | [The list that outlived the deploy](parts/04-freshness/4.3-the-list-that-outlived-the-deploy.md) | 1920 dead reads, and why removal is two deployments | `production` |

### Section 5 — `05-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The address that reached outside the room](parts/05-failure-lab/5.1-the-address-that-reached-outside.md) | `%2F` is not a slash, and the matcher is not a guard | `production` |
| 5.2 | [💥 The read that filled the window](parts/05-failure-lab/5.2-the-read-that-filled-the-window.md) | 703% of the window, and the design that fits and buries | `production` |
| 5.3 | [💥 The argument that gave an order](parts/05-failure-lab/5.3-the-argument-that-gave-an-order.md) | An injection signed with your server's name | `production` |

### Section 6 — `06-in-production`: what ships

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Two modules, one server](parts/06-in-production/6.1-two-modules-one-server.md) | Bring the notice to the board, never the board to the notice | `production` |
| 6.2 | [The shelf a stranger can use](parts/06-in-production/6.2-the-shelf-a-stranger-can-use.md) | Thirty-one boxes marked MISC, and the gate that says so | `production` |

**No paper part today.** Two parts carry §6 *The paper behind it* as an address to a paper taught
earlier: [2.1](parts/02-the-shelf/2.1-an-address-not-a-call.md) cites *Principled design of the modern
Web architecture* (`doi:10.1145/514183.514185`, taught on Day 32) because a resource is identified by a
URI and that is not an accident, and
[5.2](parts/05-failure-lab/5.2-the-read-that-filled-the-window.md) cites *Lost in the Middle*
(`arXiv:2307.03172`, taught on Day 19) because a resource is context you chose to spend. A paper is
taught once in the whole curriculum; every later day links to it.

**Read the sections in order.** Sections 2 and 3 both depend on section 1's rule, section 4 depends on
section 2's read, and section 5 breaks things section 2 and section 3 built.

---

## §3 Setup — run this

**No package is added today and none is upgraded.** `mcp` stays at `1.29.1`, `google-adk` at `2.7.1`.
`git diff pyproject.toml uv.lock` must be empty when you finish. §8 records what the pin can and cannot
speak, and the decision about it belongs to a plan amendment (Principle 14).

```bash
# 1 - the day's lab
cd days/day-35-resources-and-prompts
mkdir -p lab

# 2 - section 1: the design rule, priced
touch lab/surface.py lab/decision_cost.py

# 3 - section 2: the shelf, and the same shelf written twice
touch lab/shelf.py lab/shelf_strict.py lab/read_shelf.py lab/template_match.py

# 4 - section 3: the cards
touch lab/card_probe.py lab/linked_card.py

# 5 - section 4: freshness
touch lab/cache_hint.py lab/subscribe_probe.py lab/stale_list.py

# 6 - section 5: the failure lab
touch lab/traversal.py lab/context_cost.py lab/injection.py

# 7 - section 6: the gate
touch lab/shelf_audit.py
cd -

# 8 - the two modules you are about to write (you type every line)
touch sutra_mcp/resources.py sutra_mcp/prompts.py

# 9 - the freshness gate, before anything else
curl -s https://modelcontextprotocol.io/specification/versioning | grep -o "2026-07-28" | head -1
```

**Step 9 is the gate and it is not ceremony.** Everything in this day, the addendum it implements and
the rest of Phase 5 is written against revision **2026-07-28**. If that page names a newer current
revision, stop and amend the plan before writing code (Principle 14). It printed `2026-07-28` on
2026-09-04. Note the pattern: earlier days grepped for `specification/2026-07-28`, and that string is
not in the page's markup — grep for the bare date.

**`sutra_mcp/` is shared and Day 34 owns its foundations.** `server.py` and `tools.py` are Day 34's and
are not edited today. You add two files beside them, and Days 36, 37, 39, 41, 42 and 43 will add more.
Nothing in `sutra/` changes.

**Read the parts in order and run each script where its part says to.** Two of them are meant to be run
twice, with an environment variable changed, and those two pairs are the most important output in the
day.

---

## §4 Build brief

### The project code — `sutra_mcp/`, and you type every line

Two files, two public symbols. The parts give you every mechanism; the decisions are yours.

| File | Public symbols | What it must do |
| --- | --- | --- |
| `sutra_mcp/resources.py` | `register_resources(server)` | Attach Sutra's readable data to an existing server: the archive summary at a fixed URI, and the ticket and knowledge-base families as templates. |
| `sutra_mcp/prompts.py` | `register_prompts(server)` | Attach Sutra's house triage wording under a stable name, with its argument declared and described. |

- `register_resources(server) -> None` takes the server Day 34's `build_server()` returned and
  registers into it. It imports nothing from `sutra_mcp.server`, and importing it has no side effects
  (6.1).
- `register_prompts(server) -> None` has the same shape, for the same reasons.
- Both read the ticket store through **one** shared function, not by touching `TICKETS` directly (1.3).
- A resource miss raises `McpError` with `INVALID_PARAMS`, never a polite sentence and never an empty
  `contents` (2.3). The tool's miss stays a sentence, and there is a comment saying why (1.3).
- Every registration carries `title`, `description`, `mime_type` and `annotations`, and the prompt's
  argument carries a description with an example in it (6.2).

**`TODO(me)` markers left for you:**

- **1.3** — write the shared ticket reader and put both doors behind it, then write the comment that
  stops the next engineer making the two miss paths consistent. Decide where that function lives.
- **2.1** — decide Sutra's URI schemes and write them down as public API: `ticket://`, `kb://`,
  `archive://`, and whether `skills/README.md`'s container table and `docs/SKILL_PROVENANCE.md` get one
  too. `lab/surface.py` says they are resources; decide whether you agree and what scheme they use.
- **2.4** — decide whether the archive summary keeps naming individual ticket ids, and write the rule
  for when it must stop (5.2 gives you the arithmetic).
- **3.1** — decide whether the published card's wording is a string literal in `prompts.py` or is loaded
  from the same source as Day 6's instruction, and write the test that asserts the two agree.
- **3.3** — decide whether Sutra's card should grow from one message to a worked exchange, and write
  down what it costs a host whose context budget you cannot see.
- **3.4** — decide, per resource, embed or link, and record the size at which your answer flips.
- **4.1** — choose the `ttlMs` and `cacheScope` for `resources/read` and for `resources/list`. Day 32's
  3.3 `TODO(me)` picked the numbers for `tools/list`; these are different numbers and the reasons are
  different. Write both reasons down.
- **4.2** — write down, in one paragraph, why `sutra-mcp` does or does not declare `subscribe` in its
  resources capability, and what would have to exist before the answer could change.
- **4.3** — write the removal procedure into the deploy notes: the two deployments, the wait, and the
  `ttlMs` you chose in 4.1 as the length of that wait.
- **5.1** — decide whether Sutra ever publishes a `{path}` template at all. If yes, write the resolve
  check and the test with the percent-encoded case in it. If no, write down what it publishes instead.
- **5.3** — write the validation function for `ticket_id`, anchored, and decide what happens to any
  future free-text prompt argument that cannot be validated.
- **6.2** — assign `audience` and `priority` to every resource Sutra publishes, relative to each other,
  and say what a host should drop first when the window is tight.

### The lab — fifteen scripts, all of which run, none of which call a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/surface.py` | the three-question rule over Sutra's seven candidates | 1.1 |
| `lab/decision_cost.py` | 12 decisions and 3 silent misses against 0 and 0 | 1.2 |
| `lab/shelf.py` | a FastMCP teaching server: two families, one summary, one card | 2.1, 2.3, 2.4, 3.1 |
| `lab/shelf_strict.py` | the same shelf on the low-level `Server`, so the error code survives | 2.3, 3.2, 3.3 |
| `lab/read_shelf.py` | drives either shelf over stdio; six exchanges printed raw | 2.1, 2.2, 2.3, 3.1, 3.3 |
| `lab/template_match.py` | what `ticket://{id}` really matches, asked of the SDK's matcher | 2.4 |
| `lab/card_probe.py` | three bad `prompts/get` calls against either shelf | 3.2 |
| `lab/linked_card.py` | embedded resource against resource link, on the wire and in bytes | 3.4 |
| `lab/cache_hint.py` | can the pinned SDK carry `ttlMs` and `cacheScope` at all | 4.1 |
| `lab/subscribe_probe.py` | which subscription era the SDK speaks, and what each costs | 4.2 |
| `lab/stale_list.py` | reads of a deleted URI, by `ttlMs` | 4.3 |
| `lab/traversal.py` | `%2F` past the matcher, and the resolve check that stops it | 5.1 |
| `lab/context_cost.py` | three shelf designs against a 128 000-token window | 5.2 |
| `lab/injection.py` | one hostile argument, two templates, both renderings shown | 5.3 |
| `lab/shelf_audit.py` | the day's gate: is Sutra's shelf fit to publish | 6.1, 6.2 |

These are teaching material and they are given complete in the parts. Type them, run them, and break
them where the *Check yourself* sections ask you to.

---

## §5 The eval that must be able to fail

Five checks with exit codes, all on zero model calls.

**The shelf audit** is the day's gate, and it is red until both modules exist and carry their metadata:

```bash
uv run python days/day-35-resources-and-prompts/lab/shelf_audit.py; echo "exit: $?"
```

Measured on 2026-09-04, before Day 34's server existed in this repository:

```text
  - sutra_mcp.server.build_server is not importable: No module named 'sutra_mcp.server' (Day 34)
findings: 1
exit: 1
```

It walks forward as the code arrives: first the missing `server.py`, then the missing
`register_resources`, then one finding per resource missing a `title`, a `description`, a `mime_type`
or its annotations. It goes green only when the shelf is usable by a stranger. Then delete one
`description` and watch it go red again.

**The error-code ablation** is the finding this day exists for, and both arms must be run:

```bash
cd days/day-35-resources-and-prompts/lab
uv run python read_shelf.py
SHELF=shelf_strict.py uv run python read_shelf.py
cd -
```

`code=0` against `code=-32602`, from the same `McpError`, for the same missing ticket. The whole
difference is which decorator registered the handler.

**The traversal ablation** is the security check, and it is red on the naive arm on purpose:

```bash
uv run python days/day-35-resources-and-prompts/lab/traversal.py; echo "exit: $?"
STRICT=1 uv run python days/day-35-resources-and-prompts/lab/traversal.py; echo "exit: $?"
```

`reads that escaped the published root: 2` and `exit: 1`, against `0` and `exit: 0`. Same five URIs,
same matcher, four lines of difference in the handler.

**The injection check** is red today and stays red while the naive template exists:

```bash
uv run python days/day-35-resources-and-prompts/lab/injection.py; echo "exit: $?"
```

`unsafe renderings: 1`, `exit: 1`. Change `re.fullmatch` to `re.match` in `fenced` and watch the count
go to two — which is the exercise, and the reason `fullmatch` is the only one of the three that is a
validation.

**And the arithmetic, each of which can be broken on purpose:**

```bash
uv run python days/day-35-resources-and-prompts/lab/surface.py
uv run python days/day-35-resources-and-prompts/lab/decision_cost.py
uv run python days/day-35-resources-and-prompts/lab/template_match.py
uv run python days/day-35-resources-and-prompts/lab/linked_card.py
uv run python days/day-35-resources-and-prompts/lab/cache_hint.py;   echo "exit: $?"
uv run python days/day-35-resources-and-prompts/lab/subscribe_probe.py
uv run python days/day-35-resources-and-prompts/lab/stale_list.py
uv run python days/day-35-resources-and-prompts/lab/context_cost.py; echo "exit: $?"
cd days/day-35-resources-and-prompts/lab && uv run python card_probe.py && SHELF=shelf_strict.py uv run python card_probe.py && cd -
```

`cache_hint.py` prints `missing required caching fields: 12` and `exit: 1`. That one is red because the
pinned SDK predates `CacheableResult`, and it is not something today fixes — it is something today
records.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all fifteen lab scripts, every flag | **0** |
| the two error-code arms, both traversal arms, both card probes | **0** |
| `sutra_mcp/resources.py`, `sutra_mcp/prompts.py` and the audit | **0** |
| **Total planned** | **0 of 20** |

**Zero, and it is structural rather than lucky.** Everything this day teaches happens on the server
side of a conversation the model has not joined yet: a resource read is a dictionary lookup, a prompt
render is string formatting, and an error code is an integer on a wire. The model call is what the
*host* does afterwards, with its own quota, in its own process — which is itself one of the day's
points. The only network traffic is one HTTPS GET to the specification site in §3; every server in the
lab is a child process on this machine.

**Cost: $0.**

---

## §7 Traps

- **The rule is about who reaches first, not about what the data is.** "Tickets are data, so tickets
  are resources" gets `search_kb` wrong — a search has no address, so it is a tool (1.1).
- **A resource being cheaper assumes the address is already known.** When it is not, finding it is a
  search, and a search is a decision (1.2).
- **Adding a resource is not removing a tool.** A host that reads no resources sees an empty shelf, so
  `lookup_ticket` stays (1.3).
- **`contents` is always an array**, even for one item, and each item carries its own `uri` and
  `mimeType`. `contents[0]` is right by coincidence (2.2).
- **A read item carries `text` or `blob`, never both.** `getattr(item, "text", None)`, not `item.text`
  (2.2).
- **A missing resource MUST be `-32602`, and an empty `contents` array is forbidden** because it cannot
  be told apart from an empty document (2.3).
- **FastMCP destroys your error code.** A resource handler's `McpError` is re-wrapped as a `ValueError`
  twice, and the low-level catch-all hard-codes `code=0`. Your `data` is dropped (2.3, 3.2).
- **The template matcher binds `[^/]+`**, so `doc://{path}` cannot serve a nested document at all, and
  the refusal of a raw slash is not a security check (2.4, 5.1).
- **`%2F` is not a slash and `%2E%2E` is not `..`.** Blocking characters loses; resolving the path wins
  (5.1).
- **Templates are in a different list.** A host that calls only `resources/list` sees an almost empty
  server (2.4).
- **A prompt argument has no schema** — a name, a description and a boolean, and every value is a
  string. The host cannot validate for you (3.2).
- **`required` defaults to unset, not to `false`.** Leaving it out sends no field at all (3.2).
- **A prompt cannot return a system message.** Published wording competes with the host's own system
  prompt and never overrides it (3.3).
- **A prompt that names your tools is a hope.** Name resource URIs instead; the host's tool list is not
  yours (3.1).
- **A `resource_link` in a host that does not read resources leaves the model reasoning about a
  filename**, with no error anywhere (3.4).
- **`ttlMs` is milliseconds.** `3600` is not an hour and nothing will tell you (4.1).
- **`cacheScope: "public"` on user data lets a shared proxy serve one caller's ticket to the next** —
  and authenticating the endpoint does not make the response private (4.1).
- **A TTL is not a polling interval.** Polling on it turns a saving into a load generator; the spec says
  **SHOULD NOT**, and **MUST** jitter if you do (4.1).
- **`mcp==1.29.1` emits no `ttlMs` and no `cacheScope` at all**, so a conformant client treats every
  result as immediately stale. Caching is not misconfigured, it is off (4.1).
- **`resources/subscribe` still exists in the pinned SDK and is the deprecated mechanism.**
  `SubscriptionsListenRequest` does not exist there at all (4.2).
- **Nothing survives a reconnect.** The client MUST re-send `subscriptions/listen`; the server holds no
  subscription state (4.2).
- **A stream that stops without a response is not the same as one that closed gracefully**, and only
  one of those is a signal (4.2).
- **`ttlMs` on a list is how long clients keep offering a URI you deleted.** Removing one is two
  deployments (4.3).
- **A burst of `-32602` after a deploy is not a client bug.** It is your own freshness window (4.3).
- **A resource that fits can be worse than one that does not** — fitting and burying produces a
  confident answer about the wrong ticket, with no error (5.2).
- **Sanitising an argument is not refusing it**, and `re.match` is not a validation. Anchor both ends
  (5.3).
- **An empty `prompts/list` is a valid response**, so a registration function nobody called fails
  completely silently (6.1).
- **A metadata-poor server is fully conformant and unusable.** Only `uri` and `name` are required, and
  neither is for a stranger (6.2).

---

## §8 Verify before you code

Fetched or run on **2026-09-04**, the day this was written.

**The specification — the two server pages, in full:**

- `https://modelcontextprotocol.io/specification/versioning` — the current revision is still
  **2026-07-28**. The §3 gate passes and no amendment is required.
- `https://modelcontextprotocol.io/specification/2026-07-28/server/resources` — the URI requirement and
  RFC 3986, the application-driven user-interaction model, the `resources` capability with `listChanged`
  and `subscribe`, the MUST-NOT-vary-per-connection rule and its authorization exception, the
  `resources/list` and `resources/read` shapes with `resultType`, `ttlMs` and `cacheScope`,
  `resources/templates/list` and RFC 6570, the Resource and Resource Contents data types, the three
  annotations, the common URI schemes, the `-32602` MUST and the empty-`contents` MUST NOT, and the
  five security considerations including path sanitisation. Sections 2, 4 and 5.1 came from here.
- `https://modelcontextprotocol.io/specification/2026-07-28/server/prompts` — the user-controlled
  framing and the *decides* versus *authors* sentence, the `prompts` capability, the `prompts/list` and
  `prompts/get` shapes, the Prompt and PromptMessage data types, all five content types including
  `resource_link` and embedded `resource`, the three error codes, the implementation considerations and
  the one-sentence security note about injection. Section 3 and 5.3 came from here.
- `https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching` — the six
  operations that MUST carry hints, the cache key rule, the `ttlMs` semantics including the
  absent-means-zero rule and the SHOULD-NOT-poll rule, the `cacheScope` table, the interaction with
  notifications, pagination, and the security note that a public scope can be shared even from an
  authenticated endpoint. Section 4.1 came from here.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions` — that
  `subscriptions/listen` replaces `resources/subscribe` and the HTTP GET endpoint, the notification
  filter table, the acknowledgment and its `subscriptionId` correlation, concurrent subscriptions, the
  three ways a subscription ends, graceful closure, and the stdio rule that the server holds no
  subscription state across reconnections. Section 4.2 came from here.

**The installed SDK — the authoritative API surface, read rather than guessed.** All from
`.venv/Lib/site-packages/mcp/`, on 2026-09-04:

- `server/fastmcp/server.py` — `resource(uri, *, name, title, description, mime_type, icons,
  annotations, meta)` and `prompt(name, title, description, icons)`, the `has_uri_params` /
  `has_func_params` branch that decides resource-or-template, the `Mismatch between URI parameters …`
  `ValueError`, and both *"decorator was used incorrectly"* `TypeError`s.
- `server/fastmcp/resources/templates.py` — `matches()` is
  `pattern = self.uri_template.replace("{", "(?P<").replace("}", ">[^/]+)")` then `re.fullmatch`, and
  `create_resource` ends `except Exception as e: raise ValueError(f"Error creating resource from
  template: {e}")`.
- `server/fastmcp/resources/resource_manager.py` — `get_resource` wraps the same call the same way,
  which is why the prefix appears twice in the error message in 2.3.
- `server/lowlevel/server.py` — the two branches that decide the code on the wire:
  `except McpError as err: response = err.error`, and below it
  `except Exception as err: … response = types.ErrorData(code=0, message=str(err), data=None)`.
- `types.py` — `ReadResourceResult.contents: list[TextResourceContents | BlobResourceContents]`,
  `ResourceContents` carrying `uri` and `mimeType`, `PromptArgument.required: bool | None = None`,
  `INVALID_PARAMS`, and the absence of `SubscriptionsListenRequest`,
  `SubscriptionAcknowledgedNotification`, and of `ttlMs` / `cacheScope` on every result model.

**The SDK-era gap, restated because it bounds what today proves.** `mcp==1.29.1` reports
`LATEST_PROTOCOL_VERSION = "2025-11-25"`. So the shelf you build today serves resources and prompts
correctly and emits **no caching hints at all** (4.1: 12 of 12 fields missing), and it can only offer
the **deprecated** `resources/subscribe` mechanism rather than `subscriptions/listen` (4.2). Everything
this day says about `ttlMs`, `cacheScope` and subscriptions is verified against the specification and
measured against the library; only the first of those two is implementable here. Day 32 §8 recorded
that PyPI's `mcp` is at `2.1.1` and does speak `2026-07-28`. **Nothing is bumped today** — a day pins
only what it installs, and this one installs nothing (Principle 14).

**One live lookup, re-run today:**

```bash
curl -s https://pypi.org/pypi/mcp/json | uv run python -c "import sys,json;print(json.load(sys.stdin)['info']['version'])"
```

**No ADK symbol is used today.** The whole day is server-side and the client is `lab/read_shelf.py`,
written on the `mcp` SDK directly using the shape Day 33 established. `adk.dev` was not consulted
because nothing here touches ADK.

**No paper was verified today.** Both identifiers cited — `arXiv:2307.03172` and
`doi:10.1145/514183.514185` — already have dated rows in `docs/PAPERS.md` and are taught on Days 19 and
32. Neither is re-taught here; both are addresses.

---

## §9 Say it in an interview

"Our MCP server started out publishing only tools, which is what everybody does because tools are the
first thing you learn. The problem is that a tool is a decision the model makes on every turn. We
priced it: over a twelve-turn desk session, at a twenty-five per cent miss rate, three replies go out
with no ticket text behind them — and none of those three is an error. The model just answers from the
customer's own sentence, confidently.

So we added the other two surfaces, and the rule we used was about who reaches first rather than about
what the data is. A tool is something the model may do. A resource is something the host may read, at a
URI it already knows, which costs zero model decisions. A prompt is wording the server writes and the
person chooses to invoke. The decision that surprised people was that we did not *move* the ticket
lookup — we gave it a second door and kept the tool, because a host that only implements tools would
otherwise see an empty shelf, and we cannot see which host is calling. The price of that is one store
read behind two code paths with two deliberately different miss behaviours, and a comment saying so,
because the next person's instinct is to make them consistent.

The finding I would lead with is about error codes. The spec says a resource that does not exist MUST
be `-32602` and explicitly forbids returning an empty contents array, because an empty array cannot be
told apart from an empty document. We wrote exactly that, raised the right exception, and then drove
our own server over stdio and printed the raw error. It came back as `code: 0`, with our message
wrapped twice in the framework's prefix and our `data` field gone — because the convenience layer
re-wraps a resource handler's exception as a `ValueError`, and the low-level server's catch-all
hard-codes zero. The same shelf written on the low-level server returns `-32602` and the URI. Nothing
in the handler changed. The lesson is that the wire is the contract and a handler is only an intention.

Two more that matter operationally. Removing a resource is two deployments, because the TTL on your
list is also how long clients keep offering the URI you deleted — forty clients, four reads an hour, a
one-day TTL, and that is about nineteen hundred `-32602` responses that will page the client team.
And subscriptions: after the stateless rewrite there is nowhere to keep a subscriber list, so
`resources/subscribe` was replaced by a long-lived `subscriptions/listen` stream the client opens, with
an explicit filter, which it must re-send after every reconnect. That did not remove the held
connection, it made it explicit — forty watchers is forty pinned connections across three instances —
so we do not offer it, and freshness is a short TTL instead. Same worst-case staleness as polling, a
fraction of the requests, no instance affinity.

The security one is the failure lab and it caught us. Our template matcher rejects a slash inside a
parameter, so `doc://../../.env` never matches and it looks like the URI is validating for you.
Percent-encode it and `doc://..%2F..%2F.env` matches, binds, and the handler decodes it into a
traversal. Two of five hostile URIs read a file outside the published root, and blocking the literal
`..` does not help because you can encode the dots too. The fix is resolving both paths and comparing,
never a string prefix — and the better fix is not putting a path in a URI at all."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 35` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it to
someone else without the page open.

**Phase 5's gate** is `sutra-mcp` serving tools statelessly, on Day 38. Today adds the two surfaces
beside those tools and answers the design question that decides what goes on each one. Day 36 takes the
work that cannot finish inside one request and hands back a task handle, and the `TODO(me)` items about
`ttlMs`, the subscription decision and the URI schemes are the ones the rest of the phase will need
already made.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 35 | <date> | MCP-07, MCP-08, MCP-09 | 19 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded: `mcp` stays at
`1.29.1`, `google-adk` at `2.7.1`, and `gemini-3.7-flash` stays pinned as recorded on 2026-08-26. The
two consequences of that pin — no caching hints and no `subscriptions/listen` — are recorded in §8 for
whoever decides the bump; they are not a row until something is installed.

**`docs/PAPERS.md`** — **no new rows.** `arXiv:2307.03172` and `doi:10.1145/514183.514185` already have
dated rows and are taught on Days 19 and 32; this day cites both as addresses and teaches neither.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**The commit:**

```text
day 35: resources and prompts - closes MCP-07, MCP-08, MCP-09
```

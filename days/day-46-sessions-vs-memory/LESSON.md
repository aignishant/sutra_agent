---
day: 46
phase: 7
phase_name: "Memory and retrieval"
title: "Sessions versus memory — `MemoryService` semantics"
ids: ["ADK-27", "ADK-28"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-05"
status: written
lab_scaffolded: true
commit: ""
---

# Day 46 — Sessions versus memory: `MemoryService` semantics

> **Yesterday (Day 45):** the Phase 6 gate. `tools/mcp_audit.py` read everything Days 32 to 44 built
> and said whether it was production-shaped, and Phase 6 closed.
> **Today:** Phase 7 opens on a line that has been implicit since Day 17. A **session** is one
> conversation and it ends. **Memory** is whatever you deliberately carried out of it. Today you
> learn where the line is, what `MemoryService` promises, the three ways a store gets wired to an
> agent, and what each of them costs in tokens.
> **Tomorrow (Day 47):** the store gets a file behind it. `sutra/memory/persistence.py` puts
> `DatabaseSessionService` against a local SQLite URL, so a restart stops erasing everything.

---

## §1 Where we are

[Day 17](../day-17-state-scopes-and-lifetimes/LESSON.md) drew four lifetimes for state and called one
of them `user:`, and said it lives *"not on the session at all"*. That was the first sighting of
today's subject, and it was left there for twenty-nine days.

Since then Sutra has learned to call tools, to serve them over MCP, to harden the client and to audit
the whole thing. Every one of those days assumed a conversation that starts and ends. Nothing in this
project has ever survived a conversation.

Here is what that looks like from the other side of the desk. A support agent works ticket 4521 all
afternoon with the desk's help and between them they find the cause: a session cookie set without the
`SameSite` and `Secure` flags, so the browser drops it on a cross-site redirect. It goes in the ticket
and the ticket is closed. Three weeks later a different agent opens 4610 with the same symptom and
asks the desk *"have we seen this before?"*, and the desk — the same code, the same model, the same
skills — says no. Not because it is broken. Because 4521's conversation ended, and nothing took the
one useful sentence out of it and put it where 4610 could find it.

That act of taking something out of a conversation that is ending and putting it somewhere a
different conversation can find it is the whole subject of today. It is one method call. Everything
else in this day is about what that call costs, what it exposes, and the four ways it goes wrong.

The phase gate for Phase 7 is one question: **"Seen anything like this before?" answered at $0.**
Today is the half of that answer that is about semantics. Day 49 is the half that is about retrieval
quality, and by the end of today you will understand exactly why Day 49 has to exist.

---

## §2 The map

Nineteen parts in six sections, plus one paper. Sections 1 and 2 are ADK-27 — the line itself, then
the interface that expresses it. Sections 3, 4 and 5 are ADK-28 — how a store reaches an agent, what
each way costs, and the four failures. Section 6 is where the day is made durable: what must stay
true, and what production would actually run. The day climbs `foundation → working → production`.

### Section 1 — `01-the-line`: what a session is and what memory is (ADK-27)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The conversation that ends](parts/01-the-line/1.1-the-conversation-that-ends.md) | Two islands, and the sentence that has to cross | `foundation` |
| 1.2 | [Putting it somewhere, and finding it again](parts/01-the-line/1.2-putting-versus-finding.md) | An address against a description, and what each fails like | `foundation` |
| 1.3 | [Nothing is filed unless somebody files it](parts/01-the-line/1.3-nothing-is-filed-unless-you-file-it.md) | A memory service with no filing line is no memory at all | `foundation` |

### Section 2 — `02-the-interface`: what `BaseMemoryService` promises (ADK-27)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Two promises, and two polite refusals](parts/02-the-interface/2.1-two-promises-and-two-refusals.md) | Two required methods, two that may raise `NotImplementedError` | `working` |
| 2.2 | [The silence that lets you change the brain](parts/02-the-interface/2.2-the-silence-that-lets-you-swap.md) | Matching is unspecified, and that is the valuable part | `working` |
| 2.3 | [What comes back is not a session](parts/02-the-interface/2.3-what-comes-back-is-not-a-session.md) | `MemoryEntry` has five fields and none of them is the ticket | `working` |
| 2.4 | [The bucket is a person, not a conversation](parts/02-the-interface/2.4-the-bucket-is-a-person.md) | `(app_name, user_id)`, and who you decide the user is | `working` |

### Section 3 — `03-three-wires`: how a store reaches an agent (ADK-28)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The service rides the runner, not the agent](parts/03-three-wires/3.1-the-service-rides-the-runner.md) | `memory_service=` on `Runner`, and `ValueError: Memory service is not available.` | `working` |
| 3.2 | [The line where it crosses](parts/03-three-wires/3.2-the-line-where-it-crosses.md) | `add_session_to_memory`, by hand and from a callback | `working` |
| 3.3 | [The tool the model may call](parts/03-three-wires/3.3-the-tool-the-model-may-call.md) | `load_memory`: the ask is a decision and it is visible | `working` |
| 3.4 | [The past pushed in before the turn](parts/03-three-wires/3.4-the-past-pushed-in-before-the-turn.md) | `preload_memory`: no decision, no transcript, a swallowed error | `working` |

### Section 4 — `04-the-choice`: which wire Sutra uses, and why (ADK-28)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Pricing both, in tokens](parts/04-the-choice/4.1-pricing-both-in-tokens.md) | 1,898 against 3,130 against 7,927 — and the cap that beats both | `production` |
| 4.2 | [Sutra's memory policy](parts/04-the-choice/4.2-sutras-memory-policy.md) | Five rules, an exit code, and choosing the dearer option on purpose | `production` |

### Section 5 — `05-failure-lab`: the four ways memory goes wrong (ADK-28)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The past that matched on nothing](parts/05-failure-lab/5.1-the-past-that-matched-on-nothing.md) | Four of four matched, KB-201 sent for a login fault | `production` |
| 5.2 | [💥 The store that was never a store](parts/05-failure-lab/5.2-the-store-that-was-never-a-store.md) | Ten memories, then zero, and the only difference is an address | `production` |
| 5.3 | [💥 Another customer's memory](parts/05-failure-lab/5.3-another-customers-memory.md) | One bucket, two companies, a billing contact returned first | `production` |
| 5.4 | [💥 The store that outgrew its value](parts/05-failure-lab/5.4-the-store-that-outgrew-its-value.md) | 500 filed, 500 matched, 10,588 tokens, 0.2% useful | `production` |

### Section 6 — `06-in-production`: what must stay true, and what we would really run (ADK-27 · ADK-28)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Eight things that must stay true](parts/06-in-production/6.1-eight-things-that-must-stay-true.md) | Characterization checks for behaviour nobody promised you | `production` |
| 6.2 | [🅿️ The two services we park](parts/06-in-production/6.2-the-two-services-we-park.md) | Memory Bank against RAG Memory, and the `ImportError` that is not the real wall | `production` |

### The paper — read it **after** the parts

| Paper | What it claims | Level |
| --- | --- | --- |
| [Generative Agents: Interactive Simulacra of Human Behavior](papers/01-generative-agents.md) | Retrieval must score recency and importance, not similarity alone | `production` |

`arXiv:2304.03442`, 2023. This is the day's only paper part, and it is the answer to everything
section 5 measured: an unranked retriever is a retriever with one term, and this paper is where the
other two came from. Read it last. Principle 4 at the scale of a day — you build the memory stream by
hand, watch it fail four ways, and *then* read the proposal.

**Read the sections in order.** Section 3 is unreadable without section 2's interface, and section 4's
verdict is meaningless without section 3's two tools.

---

## §3 Setup — run this

**No package is added today, and no package is upgraded.** `google-adk` stays at `2.7.1` and
`google-genai` at `2.19.0`. `git diff pyproject.toml uv.lock` must be empty when you finish.

```bash
# 1 - the day's lab
cd days/day-46-sessions-vs-memory
mkdir -p lab lab/papers/generative-agents

# 2 - the two shared helpers every script imports
touch lab/_desk.py lab/_script.py

# 3 - section 1: the line
touch lab/island.py lab/putfind.py lab/optin.py

# 4 - section 2: the interface
touch lab/surface.py lab/swap.py lab/entry.py lab/scope.py

# 5 - section 3: three wires
touch lab/wiring.py lab/filing.py lab/asked.py lab/pushed.py

# 6 - section 4: the choice
touch lab/price.py lab/verdict.py

# 7 - section 5: the failure lab
touch lab/wrongpast.py lab/restart.py lab/leak.py lab/growth.py

# 8 - section 6: in production
touch lab/checks.py lab/parked.py

# 9 - the paper demo
touch lab/papers/generative-agents/stream.py lab/papers/generative-agents/retrieve.py
cd -

# 10 - the project package you are about to fill (you type every line)
mkdir -p sutra/memory
touch sutra/memory/__init__.py sutra/memory/service.py

# 11 - read the authority before you write against it
python -c "import google.adk.memory as m; print(m.__all__)"
python -c "import google.adk.tools as t; print(t.load_memory, t.preload_memory)"
```

**Steps 10 and 11 are the two that matter.** `sutra/memory/` is a **new package created today**, and
today owns its `__init__.py`. Day 47 adds `persistence.py` beside `service.py`; Day 48 adds
`policy.py`. Nobody re-creates the package.

Step 11 is Principle 8 in one command. The installed package is the authoritative surface — three
memory implementations and two tools — and the parts name the `adk.dev` page checked beside each one.

---

## §4 Build brief

### The project code — `sutra/memory/`, and you type every line

Two files. `__init__.py` is empty and marks the package; `service.py` holds four public symbols and
the reasoning behind each of them.

| Symbol | Shape | What it must do |
| --- | --- | --- |
| `build_memory_service` | `() -> BaseMemoryService` | Return the store, **capped at `TOP_K`**, constructed in one place so the runner can be handed it (3.1, 4.2 rule 2) |
| `MEMORY_TOOLS` | a list | The memory tools the desk carries. `load_memory`, not `preload_memory` (3.3, 4.2 rule 1) |
| `TOP_K` | an `int` constant | The retrieval cap, with a comment saying **what it was sized against** (4.1, 5.4) |
| `MAX_LOOKUPS_PER_INVOCATION` | an `int` constant | How many times one question may search, bounded and named (4.2 rule 5) |

- **`build_memory_service()`** returns a service, not a global. The cap is applied inside it, using
  the wrapper pattern from [4.1](parts/04-the-choice/4.1-pricing-both-in-tokens.md) — a
  `BaseMemoryService` that delegates and slices. Forward the two optional methods inside a
  `try/except NotImplementedError` rather than passing them straight through
  ([2.1](parts/02-the-interface/2.1-two-promises-and-two-refusals.md)).
- **The service reaches the agent through the `Runner`**, never through the agent and never through a
  module-level singleton ([3.1](parts/03-three-wires/3.1-the-service-rides-the-runner.md)).
- **A miss is reported, not interpreted.** A lookup returning nothing produces *"nothing matched these
  words"* and never *"there is no past case"* (4.2 rule 4, Principle 10).
- `lab/verdict.py` checks all five rules structurally and is **red as shipped**, because
  `sutra/memory/` does not exist until you write it.

**`TODO(me)` markers left for you:**

- **1.3, 3.2** — decide **when** Sutra files a session into memory: after every turn, at ticket
  closure, or on an explicit act by the agent. Write down what each choice stores that the others do
  not, and what it costs. Then write it as an `after_agent_callback` or as an explicit call, and say
  which and why.
- **2.3** — a `MemoryEntry` carries text and nothing else that identifies the case
  ([2.3](parts/02-the-interface/2.3-what-comes-back-is-not-a-session.md)). Decide what must be
  **inside the text** of a filed event for a retrieved memory to be actionable — the ticket number, at
  minimum — and where that gets added.
- **2.4, 5.3** — decide **who the user is**: the support agent, the customer, or the whole desk. This
  is a privacy decision expressed as a string. Write the decision, the reason and the date beside the
  function that produces it, and say what the desk can no longer do under your choice.
- **3.3** — write the desk instruction that tells the model past cases exist and when looking is
  worth it. ADK's appended paragraph is generic; a model that never asks retrieves nothing and nothing
  warns you.
- **4.1** — choose `TOP_K` and write the token budget it was sized against in the comment beside it.
  Then decide whether the cap belongs in the wrapper or in the query.
- **4.2** — choose `MAX_LOOKUPS_PER_INVOCATION`, and write down what happens when a model exhausts it
  mid-question. Silence is not an answer.
- **5.4** — decide the two signals Sutra emits about its own store: its size, and the ratio of
  matches returned to store size. Then decide the threshold at which the ratio is an alert.
- **6.1** — promote the eight assertions in `lab/checks.py` into `tests/test_memory_semantics.py`, one
  test function each, named as sentences, with a comment naming the ADK version they were observed
  against. Add the one that asserts something is **found**.
- **6.2** — write the single condition that would make you un-park the two Vertex services, with a
  date on it.

### The lab — twenty-three scripts, all of which run, none of which call a model

| File | What it does | Taught in |
| --- | --- | --- |
| `lab/_desk.py` | one past case, one new question, a fixed epoch — imported by nearly everything | all |
| `lab/_script.py` | `ScriptedModel`, a `BaseLlm` that reads from a script instead of a provider | 3.3, 3.4, 4.1 |
| `lab/island.py` | session B with and without session A filed into memory | 1.1 |
| `lab/putfind.py` | a key you read back against a description you have to match | 1.2 |
| `lab/optin.py` | a finished session, and the one line that makes it findable | 1.3 |
| `lab/surface.py` | two required methods, two that decline, and the messages they decline with | 2.1 |
| `lab/swap.py` | the same calling code over a word matcher and a synonym matcher | 2.2 |
| `lab/entry.py` | every field of a `MemoryEntry`, and everything that is not there | 2.3 |
| `lab/scope.py` | three buckets, every combination searched | 2.4 |
| `lab/wiring.py` | a runner without a memory service, and the `ValueError` it raises | 3.1 |
| `lab/filing.py` | filing by hand and filing from an `after_agent_callback` | 3.2 |
| `lab/asked.py` | the model asks, and the model does not ask | 3.3 |
| `lab/pushed.py` | the block injected before every turn, and the same wiring with an empty store | 3.4 |
| `lab/price.py` | one ten-turn conversation, three policies, three store sizes | 4.1 |
| `lab/verdict.py` | Sutra's five memory rules as an exit code | 4.2, §5 |
| `lab/wrongpast.py` | four of four matched, and the article an agent would have sent | 5.1 |
| `lab/restart.py` | the afternoon that worked, then the same code on new objects | 5.2 |
| `lab/leak.py` | one bucket against two, and a billing contact that crosses | 5.3 |
| `lab/growth.py` | five store sizes, uncapped and capped at three | 5.4 |
| `lab/checks.py` | eight assertions about the memory service, as an exit code | 6.1, §5 |
| `lab/parked.py` | the two managed services' signatures, and what happens when you build them | 6.2 |

`lab/papers/generative-agents/` holds the paper demo — `stream.py` and `retrieve.py` — and it is
**given complete** in the paper part. It is teaching material, not a rep: type it, run both arms, and
compare your output with the transcripts.

---

## §5 The eval that must be able to fail

Three checks with exit codes and five ablations, all on zero model calls.

**The gate** is the day's definition of done, and it is red until you have written the module:

```bash
uv run python days/day-46-sessions-vs-memory/lab/verdict.py; echo "exit: $?"
```

Measured on 2026-09-05, before anything was written: `rule 1-5: sutra.memory.service is not
importable: No module named 'sutra.memory'`, `findings: 1`, `exit: 1`. When it prints `findings: 0`
and `exit: 0`, five statements are true: the desk carries `load_memory`, retrieval is capped through
`build_memory_service`, the tool list is stated in one place as `MEMORY_TOOLS`, the cap is the named
constant `TOP_K`, and lookups are bounded by `MAX_LOOKUPS_PER_INVOCATION`. Then break exactly one on
purpose — rename `TOP_K` to a literal — and watch the finding appear.

**The eight semantic assertions** guard the framework underneath the module, and they must be seen to
go red:

```bash
uv run python days/day-46-sessions-vs-memory/lab/checks.py; echo "exit: $?"
```

`findings: 0  (0.006s, 0 model calls)` and `exit: 0`. Now change assertion 7's query from
`"sign-in trouble"` to `"cookie"` and re-run: `7: a synonym query matched - the service got smarter,
re-read Day 49`, `findings: 1  (0.012s, 0 model calls)`, `exit: 1`. Change it back.

**The day's thesis, as an ablation**, and both arms must be run:

```bash
cd days/day-46-sessions-vs-memory/lab
uv run python island.py
uv run python island.py --memory
cd -
```

The same second conversation, once with nothing carried across and once with the first session filed.
That is the whole day in two runs.

**The paper's ablation**, both arms:

```bash
cd days/day-46-sessions-vs-memory/lab/papers/generative-agents
uv run python retrieve.py
uv run python retrieve.py --relevance
cd -
```

`KB-104 published: set SameSite and Secure on the session cookie` ranks **third** under the full
three-term score and **sixth** under similarity alone, below `Agent went to lunch` — and seven of the
nine rows tie at `0.00`, so past the first two hits the ablated arm is not ranking at all.

**And the rest, each of which has a named break in its own part:**

```bash
cd days/day-46-sessions-vs-memory/lab
uv run python putfind.py
uv run python optin.py; uv run python optin.py --file
uv run python surface.py
uv run python swap.py; uv run python swap.py --synonyms
uv run python entry.py
uv run python scope.py
uv run python wiring.py; uv run python wiring.py --memory
uv run python filing.py; uv run python filing.py --callback
uv run python asked.py; uv run python asked.py --quiet
uv run python pushed.py; uv run python pushed.py --nothing
uv run python price.py; uv run python price.py --big; uv run python price.py --big --topk
uv run python wrongpast.py; uv run python wrongpast.py --stopwords
uv run python restart.py
uv run python leak.py; uv run python leak.py --per-customer
uv run python growth.py; uv run python growth.py --topk
uv run python parked.py
cd -
```

`parked.py` **reports two failures on purpose**: both Vertex services raise `ImportError: The
'google-cloud-aiplatform' package is required to use this feature.` That is the finding, not a broken
lab.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all twenty-one lab scripts, every flag | **0** |
| the paper demo, both arms | **0** |
| `sutra/memory/service.py`, the gate and the eight assertions | **0** |
| **Total planned** | **0 of 20** |

**Zero, and on this day it is load-bearing rather than thrifty.** Everything here is about what a
store does with text: filing is a dictionary write, searching is a set intersection, and both memory
tools can be observed exactly by replacing the model with `ScriptedModel` from `_script.py` — a
`BaseLlm` that yields pre-written turns and keeps every request it was sent, which is how
[4.1](parts/04-the-choice/4.1-pricing-both-in-tokens.md) weighs a prompt without sending one. The
paper demo has no model in it at all: importance is hand-assigned and relevance is word overlap, both
stated as simplifications in the part.

The one thing worth spending quota on, once, is attaching `load_memory` to the real desk agent and
watching a live model decide whether to look. It costs two or three generations and teaches nothing
this day has not already shown you in a transcript.

**Cost: $0.**

---

## §7 Traps

- **A memory service with no `add_session_to_memory` call behaves exactly like no memory service.**
  Nothing warns. Filing is opt-in and the opt-in is a line of your code (1.3).
- **Session state is an address; memory is a description.** `state["severity"]` returns that value or
  fails loudly. A search returns *something*, and something is not the same as the right thing (1.2).
- **`SearchMemoryResponse` is not a list.** Indexing it raises `TypeError: 'SearchMemoryResponse'
  object is not subscriptable`; the list is `.memories` (1.2).
- **Two of the four interface methods may refuse.** `add_events_to_memory` and `add_memory` raise
  `NotImplementedError` on the in-memory service, with a message naming what to call instead. A
  wrapper that forwards them blindly turns a defined refusal into an uncaught exception (2.1).
- **`BaseMemoryService` promises nothing about matching quality.** The same calling code over two
  implementations gives completely different recall, and neither is wrong by the interface (2.2).
- **What comes back is a `MemoryEntry`, not a `Session`.** No state, no session id, no ticket number
  unless the ticket number was in the text. `entry.session_id` raises `AttributeError: 'MemoryEntry'
  object has no attribute 'session_id'` (2.3).
- **`MemoryEntry.timestamp` is a string, not a `datetime`.** `entry.timestamp.year` raises
  `AttributeError: 'str' object has no attribute 'year'` (2.3).
- **The bucket is `(app_name, user_id)` and nothing else** — no session id in the key, no filter
  argument on `search_memory`, no authorisation check anywhere (2.4).
- **`user_id` is a string your code chose, and the store will not check it.** Whatever you pass is
  the boundary, and getting it wrong is a privacy incident rather than a bug (2.4, 5.3).
- **Renaming `app_name` strands every memory ever filed.** The old bucket still exists, still holds
  everything, and is unreachable (2.4).
- **`memory_service=` belongs on `Runner`, not on `Agent`.** An agent carrying `load_memory` with no
  service raises `ValueError: Memory service is not available.` from inside the framework (3.1).
- **`preload_memory` swallows the same mistake.** No traceback, exit code `0`, and a `WARNING` on the
  **root** logger — `WARNING:root:Failed to preload memory for query: ...` — which a project that
  configures `google_adk` by name will never see (3.4).
- **`preload_memory` sends `user_content.parts[0].text`** — the user's raw message, greeting and all —
  as the query, and only the **first** part, so an image followed by a question preloads nothing
  (3.4).
- **A tool result is an event, so `load_memory`'s result is re-sent on every later turn.** That is the
  cost everybody forgets and it is the one that decides the comparison (4.1).
- **Weighing a prompt with `str()` instead of `model_dump_json()`** inflated a tool declaration by
  about six thousand characters and made `load_memory` look far worse than it is (4.1).
- **The cap matters more than the policy.** Choosing the wrong policy costs a factor of two; leaving
  retrieval uncapped costs a factor of six, silently, as the store fills (4.1, 5.4).
- **One shared word is a match**, and `the`, `on` and `customer` are words. A natural question tends
  to match the entire archive (5.1).
- **The results have no ranking and no score.** They are in insertion order, so `memories[0]` is
  whatever was filed earliest, and capping an unranked list picks three arbitrary rows (5.1, 5.4).
- **A miss looks like nothing; a wrong hit looks exactly like a right hit** — same type, same shape,
  same real article number (5.1).
- **`InMemoryMemoryService` is a dictionary in one process.** It dies with the process and it is not
  shared between replicas, so more than one instance means the desk remembers at random (5.2).
- **Re-filing the same session replaces rather than duplicates**, because the write is
  `self._session_events[user_key][session.id] = [...]`. Convenient, and worth knowing before you rely
  on it (6.1).
- **Both Vertex memory services fail at construction with an `ImportError`, not a permission error**,
  and the missing package is not the real wall — the billing account behind it is (6.2).
- **A managed store does not cap anything by itself.** Pass `similarity_top_k`, or the dilution
  survives the upgrade at a much larger scale (6.2).

---

## §8 Verify before you code

Fetched or read on **2026-09-05**, the day this was written.

**The ADK documentation:**

- `https://adk.dev/sessions/memory/` — fetched and read. It is the authority for the four method
  descriptions this day uses: `add_session_to_memory` takes *"a completed `Session`"*, `search_memory`
  *"lets an agent (typically via a `Tool`) query the knowledge store"*, **Preload memory**
  *"automatically retrieves memory at the beginning of each turn, similar to a callback"*, and **Load
  memory** *"retrieves memory when your agent decides it would be helpful"*. It gives
  `InMemoryMemoryService` a persistence row of **None** and describes it as performing *"basic keyword
  matching for searches"*, best for *"prototyping and simple testing scenarios where persistence
  isn't required"*. It describes `VertexAiMemoryBankService` as *"a fully managed Google Cloud
  service"* that *"intelligently processes and stores the information as 'memories'"*, and
  `VertexAiRagMemoryService` as one that *"stores conversations in Knowledge Engine and retrieves them
  by vector similarity"* — *"use it when you already have RAG infrastructure or want raw transcript
  retrieval rather than the LLM-extracted memories produced by Memory Bank."*
- `https://adk.dev/sessions/session/` — fetched and read, for the session half of 5.2.
  `InMemorySessionService` has **"Persistence: None. All conversation data is lost if the application
  restarts."** `DatabaseSessionService` *"connects to a relational database (e.g., PostgreSQL, MySQL,
  SQLite)"* with *"Persistence: Yes. Data survives application restarts"* — which is tomorrow.
- `https://adk.dev/docs/sessions/memory/` returned **HTTP 404**. The live path has no `/docs`
  segment, exactly as Days 33, 40 and 44 found for the tools pages.
- **What the documentation does not say** is most of this day: it does not promise that the bucket
  isolates in both directions, that re-filing replaces rather than duplicates, that a `MemoryEntry`
  carries no session identity, or that `search_memory` returns an unranked list. All of that came
  from the installed source, and 6.1 pins it.

**The installed ADK — the authoritative surface, read rather than guessed:**

- `.venv/Lib/site-packages/google/adk/memory/__init__.py` — `__all__` is exactly
  `['BaseMemoryService', 'InMemoryMemoryService', 'VertexAiMemoryBankService',
  'VertexAiRagMemoryService']`, resolved lazily through a module-level `__getattr__`, which is why
  importing a Vertex service succeeds on a machine that cannot construct one (6.2).
- `.venv/Lib/site-packages/google/adk/memory/base_memory_service.py` — two `@abstractmethod`s,
  `add_session_to_memory(session)` and `search_memory(*, app_name, user_id, query)`; two concrete
  methods, `add_events_to_memory` and `add_memory`, whose bodies `raise NotImplementedError` with the
  messages quoted in 2.1; and `SearchMemoryResponse` with the single field
  `memories: list[MemoryEntry]` (2.1, 2.3).
- `.venv/Lib/site-packages/google/adk/memory/in_memory_memory_service.py` — the whole store is
  `self._session_events: dict[tuple[str, str], dict[str, list[Event]]]`; the key is
  `_user_key(app_name, user_id)`; filing is an **assignment** at `[user_key][session.id]`, which is
  why it replaces; matching is
  `any(query_word in words_in_event for query_word in words_in_query)` over
  `set(word.lower() for word in re.findall(r'\w+', text, re.UNICODE))`; and results are appended in
  iteration order with no sort anywhere in the file (1.3, 2.4, 5.1, 5.4, 6.1).
- `.venv/Lib/site-packages/google/adk/memory/memory_entry.py` — `MemoryEntry` declares exactly
  `content`, `custom_metadata`, `id`, `author` and `timestamp`; every field but `content` is optional,
  and `timestamp` is a **string** documented as *"preferred format is ISO 8601"* (2.3, 6.1).
- `.venv/Lib/site-packages/google/adk/tools/load_memory_tool.py` — the one-line body, the JSON-schema
  declaration, the `ValueError('Memory service is not available.')` guard, and the paragraph appended
  to the system instruction on every request (3.1, 3.3).
- `.venv/Lib/site-packages/google/adk/tools/preload_memory_tool.py` — `user_content.parts[0].text` as
  the query, the `try/except Exception` around the search, `logging.warning('Failed to preload memory
  for query: %s', user_query)` called on the **module** rather than on the module's own logger, the
  `<PAST_CONVERSATIONS>` template, and `llm_request._insert_transient_user_content([...])` (3.4).
- `.venv/Lib/site-packages/google/adk/runners.py` — `memory_service` is a `Runner` constructor
  parameter and is carried into the invocation context (3.1).

**Three live commands, re-run today:**

```bash
python -c "import google.adk.memory as m; print(m.__all__)"
python -c "import google.adk; print(google.adk.__version__)"
uv run python days/day-46-sessions-vs-memory/lab/parked.py
```

---

## §9 Say it in an interview

*"Phase 7 opened on a distinction I had been sloppy about: a session is one conversation and it ends,
and memory is whatever you deliberately carried out of it. The thing that surprised me is that
nothing is automatic. ADK's memory service accumulates absolutely nothing until a line of your code
calls `add_session_to_memory`, so a system with a memory service wired in and no filing line behaves
exactly like a system with no memory, and nothing anywhere warns you. The service is also passed to
the runner rather than to the agent, which is the right seam — the agent stays portable and the
deployment decides what store stands behind it.*

*Then there are two ways to reach the store, and choosing between them was the most interesting
measurement I have done on this project. `load_memory` is a tool the model calls when it decides
history is worth checking; `preload_memory` searches with the user's raw message and injects the
result before every turn. The folk answer is that the tool is cheaper because it only costs when it
fires. I measured a ten-turn conversation: with no lookups the tool was cheaper — about 1,600 tokens
against 1,900 — but at one lookup in ten turns the tool cost 3,100 and injection stayed at 1,900, and
at five lookups it was 7,900 against the same 1,900. The reason is that a tool result is an event, so
it is written into the session and re-sent on every later turn, while an injected block is transient.
Injection wins on cost at any realistic hit rate.*

*I chose the more expensive one anyway, and I would defend that. The lookup is an event: the query
and the result are in the transcript, which is the only thing that lets you debug retrieval. Under
automatic injection the query is nowhere, the result is nowhere, and a search that raises is
swallowed with a warning on the root logger that most projects never see. Three of the four failures
I found are diagnosed by reading the query.*

*And the four failures are the real content of the day. A normal-sounding question — 'the customer on
4610 keeps getting logged out, what did we do last time?' — matched all four filed tickets, because
the matcher counts one shared word and 'customer' is in every ticket, and the results have no
ranking, so anything reading the first result sent the customer an article about printing invoices.
The store is a dictionary in one process, so it is empty after a deploy and inconsistent across
replicas, with no error either way. Filing under the support agent's id instead of the customer's put
two companies in one bucket and returned one company's billing contact on the other's ticket. And at
five hundred filed cases a single question matched all five hundred, injected about ten and a half
thousand tokens, and if one of them was the case you needed then 99.8% of what you sent was noise.*

*The two conclusions I took away are that the cap matters more than the policy — capping retrieval at
three results was a factor of six where the policy choice was a factor of two — and that the deep
problem is the absence of a score. That is also where the paper comes in: Generative Agents scores
every memory on recency, importance and relevance and sums them, and I reproduced the retrieval half
with no model at all. Under similarity alone the article that actually fixes the problem ranked below
'agent went to lunch', because it shared no words with the question. Under all three terms it made
the window. Similarity-only retrieval is a choice, not a default."*

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box is ticked because you ran the thing, not because you
read about it. `./m done 46` refuses to commit until they are.

---

## §11 Ledger & commit

**`docs/PROGRESS.md` — append this row** (fill in the hash after committing):

```markdown
| 46 | 2026-09-05 | ADK-27, ADK-28 | 19 (+1 paper) | <hash> | ⚠️ |
```

**`docs/PACKAGES.md` — no new rows today.** No package is added and no pin is moved. `google-adk`
stays at `2.7.1`.

**`docs/PAPERS.md` — no new rows today.** *Generative Agents: Interactive Simulacra of Human
Behavior* (`arXiv:2304.03442`, 2023) was verified on 2026-09-04 and its row already exists, naming
this day and `days/day-46-sessions-vs-memory/papers/01-generative-agents.md`.

**`docs/SKILL_PROVENANCE.md` — no new rows today.**

**Git commit message:**

```
day 46: sessions versus memory — MemoryService semantics — closes ADK-27, ADK-28
```

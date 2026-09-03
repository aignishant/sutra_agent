---
day: 19
phase: 3
phase_name: "State, context & discipline"
title: "Context engineering I — what earns a place in the window"
ids: ["AG-08", "AG-09"]
principles: [1, 2, 3, 4, 6, 8, 10, 11, 12, 15, 16, 17, 18]
kind: concept
plan_version: "v2.2.1"
parts: 16
generated: "2026-09-03"
status: written
lab_scaffolded: false
commit: ""
---

# Day 19 — Context engineering I: what earns a place in the window

> **Yesterday (Day 18):** artifacts — bytes with a name, a version and a scope, in a store of their
> own. Sutra now has three places to keep things and a rule for which goes where.
> **Today:** the harder question, and it arrives on every single model call. The context window is a
> **budget spent per call**, not a container filled once. Today is the selection half: what is in the
> request, what each part costs, and what earns its place — measured, with a scale.
> **Tomorrow (Day 20):** compaction — what to do about the one organ that grows on its own.

---

## §1 Where we are

The noticeboard in the staff kitchen.

Everything anybody has ever pinned up is still on it. A rota from March. Three copies of the fire
drill notice, because three people printed it. A takeaway menu with the corner torn off. Somebody's
lost glove, pinned by the thumb. A poster about the charity run, which was in June.

And somewhere in the middle, on a half sheet of A4, the thing you actually need: the new number for
facilities, because the old one stopped working.

Nothing on that board is a lie. Every single item was worth pinning up on the day it went up. The board
is entirely full of true, once-useful information, and the effect of all of it together is that nobody
reads the board — which means the one item that matters today is, in every practical sense, not there.

That is the context window. Not a container you fill, but a surface everything competes on: the more
you pin up, the less any single thing is read.

Sections 1 and 2 are the diagnosis — what a request actually costs and what is actually in it,
measured with a recording model that needs no key. Section 3 is the craft: a selection rule per organ,
facts rather than blobs, and the finding that *where* a fact sits changes whether it is used. Section 4
builds the scale. Section 5 breaks the belief that state is context, and section 6 turns all of it into
a budget, a test and a handover to tomorrow.

Four things worth knowing before you start.

**The window is a budget, not a bag.** Room is not free: every token is spent on every call, delays the
first word of the answer, and competes for attention. Only the first of those three has a number you
can look up.

**One organ grows by itself.** Five of the six are sizes you chose. The history is not — it grows every
turn, is re-sent in full, and by turn ten costs twenty-one times what turn one cost. Measured.

**Presence is not use.** A fact in the window is not a fact the model will use. Position matters, and
you do not control position — it drifts as the conversation grows, which is what the day's paper
measured in 2023 and what today's own demo could only partly reproduce.

**And state is not context.** The most common wrong belief in this phase: a key in `session.state` is
in *your code's* memory, not the model's. It reaches the model through a placeholder or a tool result,
and through nothing else.

---

## §2 The map

Sixteen parts in six sections, and **one paper**. The day climbs
`foundation → working → production`: sections 1 and 2 are the diagnosis, section 3 is the craft,
section 4 is the instrument, section 5 is the deliberate failure and section 6 is the discipline.

**Read the paper last.** *Lost in the Middle* (`arXiv:2307.03172`) is the evidence behind section 3's
sharpest claim — that a fact's position changes whether it is used — and its demo is the one experiment
in this day that needs a live model. Principle 4 at the scale of a day: measure the mechanism yourself
first, then read the paper that measured it properly.

### Section 1 — `01-the-binder`: the window is a budget

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [Room is not free](parts/01-the-binder/1.1-room-is-not-free.md) | 45 tokens against 6,220, for the same question | `foundation` |
| 1.2 | [Three costs in one scene](parts/01-the-binder/1.2-three-costs-in-one-scene.md) | Quota, latency, attention — and which one has no counter | `working` |
| 1.3 | [The organ that grows by itself](parts/01-the-binder/1.3-the-organ-that-grows-by-itself.md) | Turn ten costs 21x turn one; ten turns cost 11x | `working` |

### Section 2 — `02-anatomy`: what is actually in a request

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Opening the envelope](parts/02-anatomy/2.1-opening-the-envelope.md) | A recording model, four numbers, and one surprise | `working` |
| 2.2 | [Six organs and who packed them](parts/02-anatomy/2.2-six-organs-and-who-packed-them.md) | Which dials you are allowed to turn | `working` |
| 2.3 | [The menu costs more than the handbook](parts/02-anatomy/2.3-the-menu-costs-more-than-the-handbook.md) | Six tools, 1,855 characters, on every call | `working` |
| 2.4 | [A subscription, not a purchase](parts/02-anatomy/2.4-a-subscription-not-a-purchase.md) | The one-sentence test for what belongs in an instruction | `working` |

### Section 3 — `03-selection`: the craft

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A rule for each organ](parts/03-selection/3.1-a-rule-for-each-organ.md) | Six organs, six rules, and one that spans them all | `working` |
| 3.2 | [Facts, not blobs](parts/03-selection/3.2-facts-not-blobs.md) | Sixty lines distilled to two, 27x smaller | `working` |
| 3.3 | [Position is not presence](parts/03-selection/3.3-position-is-not-presence.md) | A fact that drifts from 81% to 11% while you talk | `production` |

### Section 4 — `04-measuring`: the instrument

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [A scale for prompts](parts/04-measuring/4.1-a-scale-for-prompts.md) | Characters free, tokens exact, and when to use which | `working` |
| 4.2 | [Curated against kitchen sink](parts/04-measuring/4.2-curated-against-kitchen-sink.md) | The comparison, and the caveat that makes it honest | `production` |

### Section 5 — `05-failure-lab`: the deliberate failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 In state, and not in the window](parts/05-failure-lab/5.1-in-state-and-not-in-the-window.md) | Three keys, one `True`, and no error anywhere | `production` |

### Section 6 — `06-in-production`: discipline

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Testing what goes in the window](parts/06-in-production/6.1-testing-what-goes-in-the-window.md) | Seven assertions — two of which were vacuous at first | `production` |
| 6.2 | [A budget per organ](parts/06-in-production/6.2-a-budget-per-organ.md) | A limit that names the owner when it fires | `production` |
| 6.3 | [The heaviest organ](parts/06-in-production/6.3-the-heaviest-organ.md) | Send it, truncate it, or compact it — and why tomorrow | `production` |

### The paper — read it after the parts

| # | Paper | What it settles | Level |
| --- | --- | --- | --- |
| 01 | [Lost in the Middle: How Language Models Use Long Contexts](papers/01-lost-in-the-middle.md) · `arXiv:2307.03172` | Why position matters, and which half of that has aged | `production` |

---

## §3 Setup — run this

**No new packages today.** The measurements use `google-adk` 2.7.1 and the `google-genai` client that
has been installed since Day 2.

```bash
# 1 - confirm where you are starting from
./m check

# 2 - today's lab
mkdir -p days/day-19-context-engineering-selection/lab/papers/lost-in-the-middle
cd days/day-19-context-engineering-selection/lab

# section 1
touch weigh.py three_costs.py history_grows.py
# section 2
touch envelope.py organs.py the_menu.py subscription.py
# section 3
touch selection.py distil.py where_it_lands.py
# section 4
touch to_tokens.py
# section 5
touch not_in_the_window.py
# section 6
touch when_to_compact.py
# the paper's demo - two files, three positions
touch papers/lost-in-the-middle/corpus.py papers/lost-in-the-middle/positions.py
cd -

# 3 - what changes under sutra/ and tests/ today
ls sutra/                    # context.py is new, at the package root
ls tests/                    # test_context.py is the eval
```

**Every lab script runs from inside `lab/`**, and the paper's demo runs from inside its own folder
because it imports `corpus` by bare name:

```bash
cd days/day-19-context-engineering-selection/lab && uv run python envelope.py
```

**Run `envelope.py` first.** Four numbers, no key, and it contains the surprise the rest of section 2
explains — the tool declarations are three and a half times the instruction you spent an afternoon
writing.

**Three scripts need a key and none of them generates anything.** `weigh.py`, `three_costs.py` and
`to_tokens.py` call `count_tokens`, which runs the provider's tokeniser and returns a number. They cost
no generation quota. The paper's demo is the only thing today that does.

**`sutra/context.py` is new and lives at the package root**, beside `state.py` and `artifacts.py`. The
three modules are the phase in file form: what the code knows, what the store holds, and what the model
is actually sent.

---

## §4 Build brief

**`sutra/context.py`** — new, at the package root:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `ORGANS` | the four organs this scale can measure, named | 2.2, 4.1 |
| `weigh(request)` | characters per organ of one assembled request | 4.1 |
| `BUDGET` | a character limit per organ, generous and finite | 6.2 |
| `over_budget(sizes)` | the organ names that exceeded their limit | 6.2 |
| `distil(log, keep)` | the lines that are not like the others, capped | 3.2 |
| the module docstring | six organs, six owners, and why characters | 4.1 |

Two things in that table are the design. `weigh` measures **four** organs and says so, because
templated facts live inside the instruction and documents arrive inside a message — naming the limit
beats pretending to a resolution the data does not have. And `over_budget` returns **names**, not a
boolean, so a failing test says which organ and therefore which owner.

**`tests/test_context.py`** — new. Seven assertions, no key; see §5.

**Nothing under `sutra/desk/` has to change today.** Whether the desk's instruction gains a placeholder
is one of the `TODO(me)` items below. Confirm with `git diff` before you commit.

**`days/day-19-context-engineering-selection/lab/`** — twelve scripts plus the paper's two-file demo.
Three of the twelve need a key; none of them generates.

**`TODO(me)` markers left for you:**

- **2.2, 3.1** — run `organs.py` and `selection.py`, and **write your prediction down first**: which
  organ will dominate, and by how much. Being wrong about that is the habit this day exists to break.
- **1.2** — replace `FACT_AS_LOG` with a line from a log you have actually seen, and record the
  characters-per-token ratio. Machine output is denser than prose; how much denser is a property of
  your systems.
- **6.2** — set Sutra's four budgets from **your** measurements rather than the ones in the module, and
  write one sentence per number saying where it came from.
- **6.3** — run `history_grows.py`, subtract two adjacent rows to get your own per-turn increment, and
  compute the turn at which compaction should run. That number is tomorrow's input.
- **2.4** — take Sutra's instruction as it stands after Day 18 and sort every sentence into *standing
  rule* or *situational fact*. Move the second kind to templated state keys, and record what the
  instruction lost in characters.
- **The paper** — finish the demo on a day with quota: three positions, three questions, nine results.
  Then make it harder (thirty distractors) and record those too. Today's run got one question at each
  position before the quota ran out.

---

## §5 The eval that must be able to fail

One new file, **seven assertions**, no key and no network. Three of them are shown with their
walkthrough in [6.1](parts/06-in-production/6.1-testing-what-goes-in-the-window.md).

The suite asserts three kinds of thing, and the second and third are unusual: sizes (per organ,
against a budget), growth (the history grows and nothing else does), and **presence and absence** — a
templated fact is in the window, and an untemplated state key is not.

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_context.py -q -m "not live"   # RED: no sutra/context.py yet
# ... write the module from §4 ...
uv run python -m pytest tests/test_context.py -q -m "not live"   # 7 passed
```

Then break each thing on purpose. These were **measured**, each applied on its own to a green suite:

| Break this | Which test goes red | What it is telling you |
| --- | --- | --- |
| `distil` matches `INFO` too | the distil test | the filter selects nothing (3.2) |
| `distil` loses its cap | the distil test | a filter with no bound does nothing on a bad day (3.2) |
| the message budget becomes generous | the pasted-log test | the budget is the detector (6.2) |
| `weigh` reports `0` for tool declarations | the growth test | the scale itself can lie (4.1) |

**And the finding that came out of writing that table: two of those four went green the first time.**
The distil test used a log with only two matching lines, so the cap never bound; the growth test
compared tool sizes between turns without checking they were non-zero. Both assertions were weaker than
their names. The versions in
[6.1](parts/06-in-production/6.1-testing-what-goes-in-the-window.md) are the strengthened ones, and the
habit — *break the code on purpose and see whether the test notices* — is the transferable part.

---

## §6 Request budget

**Free-tier Gemini**, 20 requests per day (`docs/PACKAGES.md`, 2026-08-25).

| What | Generations | `count_tokens` calls |
| --- | --- | --- |
| nine lab scripts across sections 1, 2, 3, 5, 6 | **0** | 0 |
| `weigh.py`, `three_costs.py`, `to_tokens.py` | **0** | 3 + 3 + 2 |
| the whole test suite | **0** | 0 |
| the paper's demo, three positions × three questions | **9** | 0 |
| **Total required** | **9 of 20** | **8** |

The split is the day's own subject applied to itself. Everything about *what is in a request* is
measurable with a recording model and costs nothing. Everything about *how many tokens that is* costs a
`count_tokens` call, which runs the tokeniser and **generates nothing** — so it does not touch the
generation quota, though it is still an API call with rate limits.

Only the paper's demo needs the model to think, and it is the largest single spend in this phase so
far. On the day this was written the quota ran out after the first question of each position: the
partial result is pasted honestly in
[the paper part](papers/01-lost-in-the-middle.md), with a `TODO(me)` for the rest.

**Cost: $0.**

---

## §7 Traps

- **"It fits" is not a reason.** Room is not free: quota, latency and attention all grow with every
  token, and only the first has a counter. (1.1, 1.2)
- **Machine output is denser than prose** — 2.4 characters per token against 3.5 — so a pasted log
  costs more per character than anything you wrote. (1.1, 4.1)
- **The history is re-sent in full on every call.** Turn ten costs 21x turn one; ten turns cost 11x a
  single turn. (1.3)
- **`str(request.config.tools)` elides**, so measuring the repr says a sixth tool costs 28 characters.
  Serialise each declaration instead. (2.1, 2.3)
- **Tool declarations are bigger than your instruction** — 511 characters for two tools against 145 —
  and they are paid on every call whether a tool is used or not. (2.1, 2.3)
- **ADK appends a line to your instruction** naming the agent. Small, and worth knowing when counting.
  (2.1)
- **The instruction is a subscription.** Every sentence is re-sent on every call for ever; situational
  rules belong in templated facts. (2.4)
- **A state key is not in the window unless a placeholder names it or a tool returns it.** Measured:
  `note_file` in state, absent from the request. (2.1, 5.1)
- **A misspelled optional placeholder — `{note_files?}` — silently resolves to nothing.** The
  instruction looks like it templates the fact. (5.1)
- **A pasted document lands in the history**, so it is paid for on every later turn of the
  conversation, not once. (3.2, 4.2)
- **Distilling without a cap does nothing on the day everything matches.** The bound is the point.
  (3.2)
- **Position drifts.** A fact given on turn two slid from 81% of the way through the request to 11% by
  turn twelve, passing through the middle. You do not control position; length does. (3.3)
- **Curating badly is worse than not curating**, because the model cannot ask for what you left out.
  Distil *and keep* — the evidence stays as an artifact. (3.2, 4.2)
- **Characters and tokens are not interchangeable across kinds of text.** Budget per organ, convert at
  the boundary. (4.1)
- **A budget nobody can hit is decorative**, and a test that passes when the scale returns zero is
  vacuous. Break things on purpose to find out which you have. (6.1, 6.2)
- **Truncating history is not compacting it.** Truncation loses facts silently; compaction is
  tomorrow. (6.3)

---

## §8 Verify before you code

Fetched and measured on **2026-09-03**, the day this was written:

- **`arxiv.org/abs/2307.03172`** — the record opened, the title copied from it, and the abstract read
  for the two claims quoted in
  [3.3](parts/03-selection/3.3-position-is-not-presence.md) and the paper part. A row was added to
  `docs/PAPERS.md`.
- **The installed `google-adk` 2.7.1**, in `.venv/Lib/site-packages/google/adk/` — `models/base_llm.py`
  and `models/llm_request.py` for the recording-model interface and the request's shape;
  `flows/llm_flows/functions.py` for the message ADK produces when a model invents a tool name. **Every
  structural claim in this day was measured on this machine against this version**, not read.
- **`google-genai` 2.19.0** — `client.models.count_tokens`, which returns `total_tokens` (and
  `cached_content_token_count`, which is `None` here and becomes interesting on Day 51). Verified live
  against `gemini-3.7-flash`, which is Sutra's pin since Day 2.
- **The free tier's daily ceiling**, met again partway through the paper's demo. The 429 is reproduced
  in [Day 16, 7.1](../day-16-built-in-tools-with-brakes/parts/07-failure-lab/7.1-the-spare-that-does-not-fit.md).

If your `google-adk` is not 2.7.1, run `envelope.py` and `the_menu.py` before trusting a number in this
day — and if either disagrees, that is a Principle 14 moment: amend first, then write.

---

## §9 Say it in an interview

"We had an agent that got slower and less accurate the longer a conversation ran, and the fix was not a
better prompt — it was finding out what was in the prompt. We put a recording model in front of it, one
that saves the request and answers a fixed line, and measured the request by organ. Two things came out
of that immediately. The tool declarations were three and a half times the size of the instruction
somebody had spent an afternoon on, and they are sent on every call whether a tool is used or not. And
the history was the only part that grew by itself — turn ten cost twenty-one times turn one, and the
conversation as a whole cost eleven times what its first turn suggested, because every turn re-sends
everything before it. The rule we ended up with is one selection rule per organ, asked per call rather
than per system: standing rules only in the instruction, the smallest useful tool menu, facts rather
than blobs, and the slice of a document that answers the question with the whole thing kept as an
artifact. The finding that changed how I think, though, is that presence is not use. A fact the user
gave us on turn two had drifted to eleven per cent of the way through the request by turn twelve, and
there is a 2023 paper measuring exactly that — accuracy is highest at the beginning and the end of a
context and sags in the middle. So facts that matter get promoted out of the transcript into state and
templated into a fixed position. And all of it is tested: a budget per organ, asserted in CI, which
turns prompt growth into a failing build instead of a bill."

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box ticked, `./m depth 19` green, `./m check` printing
`OK all green`, and — the part no script can check — you can answer the *out loud* question at the end
of each of the sixteen parts without scrolling up.

Not when a number of sittings has passed. When you can name the six organs, say who packed each one,
and predict which will dominate a request before you measure it.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 19 | <date> | AG-08, AG-09 | 16 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed today.

**`docs/PAPERS.md`** — **one row, already added**, because the citation was verified while the day was
written rather than after it:

```text
| Lost in the Middle: How Language Models Use Long Contexts | arXiv:2307.03172 | 2023 | 2026-09-03 | 19 | `days/day-19-context-engineering-selection/papers/01-lost-in-the-middle.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR is required, and one decision belongs in the commit message: the four
numbers in `BUDGET` and where each came from. **If your ADK version changes what it appends to the
system instruction, or the shape of the tool declarations, the budget numbers move** — that is a
behaviour change in a pinned dependency, and Principle 14 says amend first.

**Commit message:**

```text
day 19: context engineering I - what earns a place in the window - closes AG-08, AG-09
```

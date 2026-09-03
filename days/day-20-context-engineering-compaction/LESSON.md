---
day: 20
phase: 3
phase_name: "State, context & discipline"
title: "Context engineering II — compaction & summarization"
ids: ["AG-10", "ADK-22"]
principles: [1, 2, 3, 4, 7, 8, 10, 11, 12, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 15
generated: "2026-09-03"
status: written
lab_scaffolded: false
commit: ""
---

# Day 20 — Context engineering II: compaction & summarization

> **Yesterday (Day 19):** the window is a budget spent on every call, and five of its six organs are
> sizes you chose. You measured them, and you found the sixth — the history — growing on its own.
> **Today:** the fix for the sixth. Old turns are replaced by a model-written summary, recent turns
> stay word for word, and the archive underneath stays whole. You will also watch a user's
> instruction disappear because of it.
> **Tomorrow (Day 21):** errors — surfacing them instead of swallowing them, which is the fourth
> 1.x → 2.x trap.

---

## §1 Where we are

The residents' association meets on the first Saturday of the month.

Somebody records the whole meeting on their phone, and nobody has ever listened to it. What everybody
reads is the page the secretary types up: the lift repair was approved, the gate code changes on the
fifteenth, the parking question is still open. When a new person joins the committee they get that
page, not six years of audio, and they are up to speed before the tea goes cold.

The recording is still in the drawer. Twice in six years, two people disagreed about what was agreed,
and the recording is how they found out.

That is today, in one scene. The **record** is everything that happened and it is never shortened.
The **briefing** is what you read before you speak, and from today Sutra's briefing stops being a copy
of its record.

Four things worth knowing before you start.

**The saving is real and it arrives suddenly.** For twenty days the history organ has only ever grown.
Today, on call three of four, it goes *down* — three messages become one, and the request shrinks
below the one before it.

**You pay for it in the wrong currency.** A summary is a model call. Compaction saves characters and
spends **requests**, and Sutra's free tier is metered in requests per day, per model. That awkward
mismatch is the day's most useful fact and it turns into a configuration decision.

**The loss is real, silent, and the point.** A truthful, tidy summary dropped three facts out of
eight — including *"do not close the ticket"*, which the user had typed. No error, no warning, a 32%
smaller request, and an agent that has never been told.

**And the archive gets bigger, not smaller.** Compaction appends. The same eight turns produced a 42%
smaller final request and a session holding four more events and three and a half times as much
stored text.

---

## §2 The map

Fifteen parts in five sections, and **one paper**. The day climbs
`foundation → working → production`: section 1 is the idea and its price, section 2 is the ADK
configuration, section 3 is what actually lands in the session, section 4 is the deliberate failure
lab, and section 5 is the discipline that makes it safe to switch on.

**Read the paper last.** *MemGPT* (`arXiv:2310.08560`) is the proposal that says the loss you measure
in 4.2 did not have to be permanent, and it only lands once you have felt the loss. Principle 4 at the
scale of a day: build the mechanism, then read the proposal.

### Section 1 — `01-notes-not-transcript`: what compaction is, and what it costs

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The archive and the briefing are not the same thing](parts/01-notes-not-transcript/1.1-archive-and-briefing.md) | Five turns become three lines; the record stays five | `foundation` |
| 1.2 | [Summaries are lossy on purpose](parts/01-notes-not-transcript/1.2-summaries-are-lossy.md) | 57% smaller, and 5 of 8 facts survive | `working` |
| 1.3 | [You spend calls to save characters](parts/01-notes-not-transcript/1.3-you-spend-calls-to-save-calls.md) | Break-even at turn 4; 40 turns cost 59 requests | `working` |
| 1.4 | [What must never be summarized](parts/01-notes-not-transcript/1.4-what-must-never-be-summarized.md) | One fact, said twice — only the state copy survives | `working` |

### Section 2 — `02-the-config`: the three decisions, as ADK configuration

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [One config, and it belongs to the App](parts/02-the-config/2.1-one-config-on-the-app.md) | The first time the history organ has ever shrunk | `working` |
| 2.2 | [The turn-count trigger: interval and overlap](parts/02-the-config/2.2-the-turn-count-trigger.md) | What overlap buys, measured in events per summary | `working` |
| 2.3 | [The size trigger: threshold and retention](parts/02-the-config/2.3-the-size-trigger.md) | One pasted log, and the trigger a turn count cannot be | `working` |
| 2.4 | [Which trigger for which workload](parts/02-the-config/2.4-which-trigger-for-which-workload.md) | One config, two conversations, two behaviours | `working` |

### Section 3 — `03-reading-the-record`: what actually lands in the session

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The summary is not in the event's content](parts/03-reading-the-record/3.1-the-summary-is-not-in-the-content.md) | `author='user'`, `content=None`, and where it really is | `working` |
| 3.2 | [What the model sees after a compaction](parts/03-reading-the-record/3.2-what-the-model-sees-after-a-compaction.md) | Four events replaced by one `model` message | `production` |
| 3.3 | [The archive is still whole — and bigger](parts/03-reading-the-record/3.3-the-archive-is-still-whole.md) | Window down 42%, storage up 3.5x | `working` |

### Section 4 — `04-failure-lab`: the deliberate failures

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [💥 The minute-taker you did not hire](parts/04-failure-lab/4.1-the-minute-taker-you-did-not-hire.md) | Four turns, six requests, all on the expensive model | `production` |
| 4.2 | [💥 The fact that was true and is now gone](parts/04-failure-lab/4.2-the-fact-that-was-true-and-is-now-gone.md) | A constraint leaves the window with no error at all | `production` |

### Section 5 — `05-in-production`: the discipline

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Budgeting the minute-taker](parts/05-in-production/5.1-budgeting-the-minute-taker.md) | 15 turns a day against 20, from one argument | `production` |
| 5.2 | [Testing compaction without spending quota](parts/05-in-production/5.2-testing-compaction-without-quota.md) | Seven green, then four red on purpose | `production` |

### The paper — read after the parts

| # | Paper | What it answers | Level |
| --- | --- | --- | --- |
| 01 | [MemGPT: Towards LLMs as Operating Systems](papers/01-memgpt.md) | `arXiv:2310.08560` — what if the agent could fetch it back? | `production` |

---

## §3 Setup — run this

**No new packages today.** Everything used is already pinned: `google-adk==2.7.1` and
`google-genai==2.19.0` from `docs/PACKAGES.md`. `docs/PAPERS.md` gains one row (§11).

```bash
# 1 - the day folder's lab, and the paper's demo folder
cd days/day-20-context-engineering-compaction
mkdir -p lab/papers/memgpt
cd lab

# 2 - the fifteen lab scripts, in reading order
touch briefing.py whats_lost.py break_even.py never_summarized.py
touch compact.py overlap.py by_size.py both_triggers.py
touch find_the_summary.py what_the_model_sees.py archive_grows.py
touch who_writes_the_minutes.py lost_in_the_minutes.py quota_split.py
touch test_compaction_demo.py

# 3 - the paper's two-file demo
touch papers/memgpt/memory.py papers/memgpt/run.py
cd -

# 4 - what changes under sutra/ and tests/ today
ls sutra/                    # context.py gains the compaction demo and COMPACTION
ls tests/                    # test_context.py gains the compaction assertions
```

The paper's demo lives under `lab/papers/<paper-slug>/`, the convention from Day 14 onwards, and it
runs from inside its own folder because `run.py` imports `memory` by bare name. The scripts are listed
in reading order, which is the order the parts introduce them, so each one's output sets up the next
one's question. Every line of every file is typed by you, from the parts.

**Run `compact.py` first**, once you have typed it. It is the whole day in one file, it needs no key,
and the surprise is in its last four lines: call 3 is smaller than call 2.

**Only one thing today needs a key**, and it is the paper's demo. Every one of the other fourteen
scripts and the whole test suite run against recording models — no key, no network, no quota.

**`sutra/context.py` is extended, not replaced.** Day 19's `weigh`, `BUDGET`, `over_budget` and
`distil` all stay. Today adds the compaction configuration and one demo beside them.

---

## §4 Build brief

**`sutra/context.py`** — extended:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `SUMMARIZER_MODEL` | the lite-lane model string, pinned and dated | 5.1 |
| `COMPACTION` | the `EventsCompactionConfig` Sutra actually uses, with both triggers | 2.4 |
| `build_app(agent)` | returns the `App` with `COMPACTION` attached | 2.1 |
| `is_summary(event)` | the one correct detector, so nothing else has to know | 3.1 |
| `summary_text(event)` | the text out of `actions.compaction`, or `None` | 3.1 |

Two things in that table are the design. `COMPACTION` is a **module-level constant** rather than a
function, because [2.1](parts/02-the-config/2.1-one-config-on-the-app.md) shows ADK mutating the
config object on first use — one instance, built once, is the honest model of that. And `is_summary`
exists so that the logger, the tests and any future session viewer share one definition of a
compaction event, rather than four copies of a guard that will need changing when this experimental
API moves.

**`tests/test_context.py`** — extended with the compaction assertions; see §5.

**Nothing under `sutra/desk/` has to change today.** Whether the desk's `Runner` is rebuilt from
`build_app(...)` is one of the `TODO(me)` items below. Confirm with `git diff` before you commit.

**`TODO(me)` markers left for you:**

- **1.3, 5.1** — run `break_even.py` and `quota_split.py` with **your** interval, then write one
  sentence saying which number decided it: the character saving or the request cost. There is no
  correct answer here that is not tied to a measurement.
- **2.2** — run `overlap.py` with a fourth setting, `interval=2, overlap=2`, and **write your
  prediction of `events handed to each` down before you look.** Being wrong about that is the habit
  this section exists to build.
- **2.4** — set Sutra's own two triggers. The interval comes from your session-length histogram, the
  threshold from `gemini-3.7-flash`'s input limit minus the room the rest of the window needs. Write
  the source of each number in a comment beside it.
- **3.1** — write `is_summary` and `summary_text` in `sutra/context.py`, then grep the repo for any
  other place that walks `session.events` and make it use them.
- **4.2** — add a third probe to `lost_in_the_minutes.py` for a phrase that was never in the
  conversation, and say what it proves. Then say what the uncompacted run is doing for the other two.
- **5.2** — break the suite three ways rather than one: drop the config, set the interval past the
  conversation length, and remove the `asyncio.sleep`. Record which tests go red for each, and which
  failure message you would not want to debug at 11pm.
- **The paper** — finish the ablation on a day with quota: `PAGING=0 uv run python run.py`, and record
  the `answer:` line. Today's run got the paging arm and ran out of quota before the control arm.

---

## §5 The eval that must be able to fail

Five tests, **seven cases** (one is parametrised over three broken configs), no key and no network.
All five are shown with their walkthrough in
[5.2](parts/05-in-production/5.2-testing-compaction-without-quota.md).

They assert three kinds of thing, and the third is the unusual one: that it happened (a summary
exists, the window shrank, the archive grew), that it has the right shape (the summary is in
`actions.compaction`, the author is `user`, half a trigger is refused), and **that the loss you
accepted is the loss you got** — a constraint present without compaction and absent with it.

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_context.py -q -m "not live"   # RED: no COMPACTION yet
# ... write the symbols from §4 ...
uv run python -m pytest tests/test_context.py -q -m "not live"   # green
```

Then break it on purpose. Measured on 2026-09-03, by changing `if compact` to `if False` so the
compacted run quietly gets a plain `App` — which is exactly what happens if you build the `Runner`
with `agent=` instead of `app=`:

| Break this | Which tests go red | What it is telling you |
| --- | --- | --- |
| the `App` loses its config | four of five | compaction stopping is invisible without a test (2.1) |
| the interval exceeds the conversation | the three that need a summary | a trigger that never fires is a dead setting (2.2) |
| the `asyncio.sleep` is removed | intermittently, any of them | fake models outrun the clock (2.2) |

**And the finding that came out of writing that table:** one of the four red messages was
`StopIteration`, which says nothing about what was expected. It came from a `next()` with no default.
That is the second consecutive day on which deliberately breaking a passing suite exposed a weak
assertion — yesterday's
[19.6.1](../day-19-context-engineering-selection/parts/06-in-production/6.1-testing-what-goes-in-the-window.md)
found two. **Running the suite red is how you review the suite**, and it is the transferable half of
Principle 11.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day **per model** — read from a live 429 body on
2026-09-03, whose violation names the quota `GenerateRequestsPerDayPerProjectPerModel-FreeTier`.

| What | Generations | Model |
| --- | --- | --- |
| fourteen lab scripts across sections 1–5 | **0** | recording models only |
| the whole test suite, seven cases | **0** | recording models only |
| the paper's demo, `PAGING=1` | **2** | `gemini-3.7-flash` |
| the paper's demo, `PAGING=0` | **1** | `gemini-3.7-flash` |
| **Total required** | **3 of 20** | |

The split is the day's own subject applied to itself. Every structural claim about compaction — when it
fires, what it replaces, where the summary lands, what the archive does — is measurable with a
recording chat model and a fixed-text summarizer, and costs nothing. Only the paper's demo needs a
model to actually decide something.

On the day this was written the quota ran out during the second arm of the paper's demo, after nine
requests had already gone to Day 19's unfinished work. The partial result is pasted honestly in
[the paper part](papers/01-memgpt.md) with a `TODO(me)` naming the exact command.

**Cost: $0.**

---

## §7 Traps

- **`Runner(agent=...)` silently drops your compaction.** The `Runner` takes exactly one of `app`,
  `agent` or `node`, and passing `agent` makes ADK wrap it in a fresh `App` with no config. Nothing
  warns; no summary ever appears. This is the day's most likely wasted evening (2.1).
- **Leaving `summarizer` unset does not disable summarizing.** ADK derives one from the root agent's
  model and writes it back into your config, so your chat model takes the minutes — four turns became
  six requests, all on the expensive model (4.1). This is **ADK-73's reflex** from
  [Day 5](../day-05-first-adk-agent/LESSON.md): pin the model, always, everywhere.
- **`gemini-3.7-flash-lite` does not exist.** The newest lite model on the live roster is
  `gemini-3.5-flash-lite`; the flash line has run on to 3.8 without it. Guessing the name gets you a
  404 at the first compaction rather than at startup (5.1). Principle 7, exactly.
- **Half a trigger is a `ValidationError`.** `compaction_interval` needs `overlap_size`;
  `token_threshold` needs `event_retention_size`. This one is loud and lands at startup, which is the
  good kind (2.1, 2.3).
- **`overlap_size` counts invocations; `event_retention_size` counts events.** They read like the same
  setting. A turn is usually two events and can be twelve (2.4).
- **The summary is not in `event.content`.** It is `None`, and the author is `'user'`. Every turn
  counter, log line and session viewer you have written is now wrong by one per summary (3.1).
- **Compaction makes storage bigger.** It appends. If you told anyone it "cleans up old
  conversations", correct that before it reaches a retention policy (1.1, 3.3).
- **The `EventsCompactionConfig` API is marked experimental** and says so on every construction. Pin
  the ADK version and re-read the page on any upgrade — Principle 14: amend first, then code.

---

## §8 Verify before you code

Fetched on **2026-09-03**, the day this was written:

- `https://adk.dev/context/compaction/` — the import paths, the `App` field, and both trigger pairs.
  Cross-read against the installed `google-adk` 2.7.1 source (`google/adk/apps/_configs.py`,
  `llm_event_summarizer.py`, `compaction.py`, `runners.py`), which is where the validation messages,
  the `author='user'` shape and the balanced-prefix guard come from.
- `https://arxiv.org/abs/2310.08560` — the paper's exact title, verified against the record rather
  than from memory (§17.4.1 rule 5), and its abstract.
- `https://ar5iv.labs.arxiv.org/html/2310.08560` — the full text, for the memory tiers, the warning
  and flush thresholds, the evaluation datasets and the reported limitations.
- `https://generativelanguage.googleapis.com/v1beta/models` — the live model roster and input limits.
  This is the lookup that shows `gemini-3.7-flash-lite` does not exist.
- `https://ai.google.dev/gemini-api/docs/rate-limits` — checked, and it **no longer publishes a
  free-tier table**; it directs you to AI Studio for your own limits. The 20-per-day figure in §6 is
  therefore taken from a live 429 body, not from a page.

---

## §9 Say it in an interview

"We were on a free tier metered at twenty requests per model per day, and long support threads were
eating it — turn ten of a conversation costs about twenty-one times turn one, because the history is
re-sent in full every time. We turned on ADK's context compaction: it summarizes older invocations and
keeps the recent ones verbatim, configured on the `App` rather than the agent. The window on our test
conversation dropped 42%.

Two things I would tell anyone doing it. First, pin the summarizer model explicitly — if you leave it
out, ADK derives it from your chat agent, so your expensive model writes the notes. On our four-turn
test that was six requests instead of four, and because the free-tier quota is per model, splitting it
onto the lite model took us from fifteen usable turns a day to twenty.

Second, it loses things, and it loses them silently. We had a conversation where the user said 'do not
close this ticket' in the first turn; after compaction that sentence was not in the window at all, the
request was 32% smaller, and nothing errored. The fix is not a better summarizer — it is not depending
on prose. Constraints go into session state and get templated into the instruction on every call, so
compaction can't reach them. We test both halves with fake models, no key and no network, and the
suite goes red the moment the config gets dropped, which is the only way you'd ever notice."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 20` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it
to someone else without the page open.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 20 | <date> | AG-10, ADK-22 | 15 (+1 paper) | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — no new rows. Nothing was installed today.

**`docs/PAPERS.md`** — append:

```text
| MemGPT: Towards LLMs as Operating Systems | arXiv:2310.08560 | 2023 | 2026-09-03 | 20 | `days/day-20-context-engineering-compaction/papers/01-memgpt.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skills were sourced today.

**The commit:**

```text
day 20: context engineering II - compaction & summarization - closes AG-10, ADK-22
```

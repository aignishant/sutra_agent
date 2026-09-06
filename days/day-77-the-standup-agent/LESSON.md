---
day: 77
phase: 11
phase_name: "Ambient & live"
title: "The standup agent — a voice client over the queue state"
ids: ["ADK-57", "AG-25"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: build
plan_version: "v2.2.1"
parts: 11
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 77 — The standup agent

> **Yesterday (Day 76):** VAD events and non-blocking tools. The line that goes dead on one word
> inside a tool, three answers to when a result should come back, and voice activity detection turned
> from fate into a panel of settings.
> **Today:** the thing the phase was building towards. Days 73 to 76 built a nightly job, a stream, a
> voice loop and tools that do not freeze it; today they become a **product** — an agent that looks
> the queue up and says a standup out loud — and the design question turns out to be one nobody
> reaches for: **what order to say it in**.
> **Tomorrow (Day 78):** the phase gate — ambient and voice, inside free quota.

---

## §1 Where we are

A standup is a report on state somebody else owns, delivered to somebody who is also making tea. It
is the first thing in this curriculum whose quality is not a property of its correctness.

**The agent works, and that is the least interesting thing about it.** Over a real `run_live` session
it calls three tools in one turn — `queue_by_category`, `tickets_needing_a_person`, `last_night` —
each answered by the runtime before the next is asked for, and then speaks. Every fact it says is
true in both arms of every measurement on this day.

**The order is the product.** The same twelve tickets, the same two that need somebody, said two
ways: attention first, or the queue in the order it happens to sit in. Attention first is **5
sentences and 53 words**; queue order is **14 sentences and 103 words**, with the first thing needing
a person arriving **25 words in**.

**And on a voice line, order is not style — it is delivery.** The listener says something after two
sentences, which on an open line stops the standup. Attention first delivers **3 of 3** sentences
that needed a person. Queue order delivers **0 of 2**, having called all three tools, read the queue
correctly, and told the listener nothing they could act on.

**The quiet morning is a report too.** Last night's job died before writing its digest, so part of the
state is missing — and a standup that simply omits what it does not know is a standup that says the
night went fine.

---

## §2 The map

Four sections. Section 1 is what a spoken report is and what this one actually delivered. Section 2 is
the order, which is the day's subject. Section 3 is the morning when there is nothing to report and
the morning when something is missing. Section 4 is what it costs and who it is for.

### 1 — A report somebody hears

*One chance, one order, one speed.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A report with one chance](parts/01-a-report-somebody-hears/1.1-a-report-with-one-chance.md) | A written report is skimmed; a spoken one arrives in the order you chose | `foundation` |
| 1.2 | [The three tools, called for real](parts/01-a-report-somebody-hears/1.2-the-three-tools.md) | Three function calls in one turn, each answered before the next | `working` |
| 1.3 | [What the listener actually got](parts/01-a-report-somebody-hears/1.3-what-the-listener-got.md) | 💥 3 of 3 against 0 of 2, with every fact correct in both | `production` |

### 2 — The order is the product

*The one design decision, and the one bug underneath it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [One function, one order](parts/02-the-order-is-the-product/2.1-one-function-one-order.md) | `lines(queue, night)` — the whole contract, and why it is one function | `working` |
| 2.2 | [Carry the flag, do not search for it](parts/02-the-order-is-the-product/2.2-carry-the-flag.md) | 💥 A real bug from this lab: "need you" is not "needs you" | `production` |
| 2.3 | [Words before it matters](parts/02-the-order-is-the-product/2.3-words-before-it-matters.md) | 0 words against 25, on identical facts | `working` |

### 3 — The quiet morning

*The report when there is nothing to say, and when something is missing.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Nothing needs you is a report](parts/03-the-quiet-morning/3.1-nothing-needs-you.md) | Silence and "nothing needs you" are different reports | `production` |
| 3.2 | [Saying what you do not know](parts/03-the-quiet-morning/3.2-saying-what-you-do-not-know.md) | 💥 Last night's digest died, and omitting that reports a good night | `production` |

### 4 — In production

*What it costs, who it is for, and the distance to a real one.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [What a standup costs](parts/04-in-production/4.1-what-a-standup-costs.md) | Priced in a listener's attention before it is priced in quota | `production` |
| 4.2 | [Who it is for](parts/04-in-production/4.2-who-it-is-for.md) | The same queue makes three different standups for three people | `production` |
| 4.3 | [What a real one adds](parts/04-in-production/4.3-what-a-real-one-adds.md) | Freshness, follow-ups, and the parked half | `production` |

### The paper — read it last

*Principle 4 at the scale of a day: choose the order, then read why the listener has a budget.*

| # | Paper | What it answers |
| --- | --- | --- |
| 01 | [The magical number seven, plus or minus two](papers/01-chunking.md) | `doi:10.1037/h0043158` — the limit is on units, not on information |

---

## §3 Setup — run this

```bash
mkdir -p days/day-77-the-standup-agent/lab/papers/chunking
cd days/day-77-the-standup-agent/lab
touch _state.py _live.py
touch standup.py live.py gate.py
touch papers/chunking/report.py papers/chunking/demo.py
```

**What each file is for:**

- `_state.py` is the file to read first: twelve open tickets, two of which need a person, and last
  night's job. Nothing is generated and nothing is random.
- `standup.py` builds the standup two ways and measures what a listener hears first.
- `_live.py` is the scripted connection from Days 75 and 76 with the desk's three tools attached.
- `live.py` delivers the standup over a real session and lets the listener cut it short.
- `gate.py` is the eval.

Verify the lab is gitignored before the first run:

```bash
git check-ignore -v days/day-77-the-standup-agent/lab/_state.py
```

**Why:**

- `days/*/lab/` is ignored repo-wide (Principle 9). Today's fixture is invented ticket text; a real
  standup reads real customer subjects, which is Day 69's subject and a good habit to keep.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.

---

## §4 Build brief

**`sutra/standup.py`** — the one place that turns the desk's state into what will be said.

- `TODO(me)`: `lines(queue, night)` returning a list of `(text, attention)` pairs, in the order they
  would be spoken. The gate checks the shape, because the shape is the design.
- `TODO(me)`: carry the attention flag rather than searching the text for it. Part 2.2 is a real bug
  from this lab and it cost a wrong measurement before it was noticed.
- `TODO(me)`: put what needs a person **first**. The gate asserts `lines(...)[0][1] is True` when the
  queue has a blocked ticket, which is the whole of part 2.3 made checkable.
- `TODO(me)`: say something when nothing needs a person. Part 3.1 is why an empty report and a quiet
  report are different things.
- `TODO(me)`: decide what the standup says about state it could not read. Part 3.2 is the failure;
  the decision is yours.
- `TODO(me)`: decide who this standup is for, and write it down. Part 4.2 argues that the same queue
  makes three different standups and that a single one is a compromise somebody should have made on
  purpose.

**`tests/test_standup.py`**

- `TODO(me)`: a test that the first line is flagged for attention when a ticket needs a person.
- `TODO(me)`: a test for the quiet case — nothing needing a person still produces a report.
- `TODO(me)`: a test that the flag survives a rewording of the text. That is the test that would have
  caught part 2.2, and it is the one that looks pointless.

---

## §5 The eval that must be able to fail

```bash
cd days/day-77-the-standup-agent/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/standup.py`, all red today because the module is the build brief. A check
that cannot run counts as a **failure** rather than as skipped (Principle 11).

The day's two measurements each encode their verdict in the exit code:

```bash
uv run python standup.py; echo "exit: $?"
uv run python standup.py --flat; echo "exit: $?"
uv run python live.py; echo "exit: $?"
uv run python live.py --flat; echo "exit: $?"
```

The attention-first arms exit `0` and the queue-order arms exit `1` — the second pair having called
every tool, read the queue correctly and delivered nothing the listener could act on. The paper's demo
does the same for its own claim: `demo.py` exits `0` at four units and `demo.py --off` exits `1` at
twelve.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

The tools are real and really called: the runtime chose them, ran them and sent each result back
through the connection before the next call was emitted. What is scripted is the model's side — which
tools to call and what words to say — because Day 74 part 4.2's free-quota check parked the paid live
model and nothing since has changed that.

That leaves one honest gap, and part 4.1 names it: this day measures a standup's cost in **sentences
and words**, not in tokens, because the wording here was written rather than generated. A standup
whose sentences come from a model costs one request per morning and a number of tokens proportional
to how much of the queue you hand it.

---

## §7 Traps

1. **Writing a spoken report the way you would write a written one.** A written report is skimmed and
   a spoken one is not — part 1.1.
2. **Assuming the tools are the hard part.** Three tool calls in one turn worked first time; the
   design difficulty is entirely in what to do with the answers — part 1.2.
3. **Judging a standup by whether it was correct.** Both arms of every measurement on this day are
   correct — part 1.3.
4. **Spreading the ordering decision across the call sites.** One function, one order, one place to
   test — part 2.1.
5. **Detecting importance by searching the text.** This lab did exactly that and measured the wrong
   number — part 2.2.
6. **Optimising the standup's length.** Shorter is not the goal; *earlier* is — part 2.3.
7. **Saying nothing when nothing is wrong.** Silence is indistinguishable from a job that did not run
   — part 3.1, and Day 73 part 3.3 for the same argument one layer down.
8. **Omitting what you could not read.** A missing section reads as a good night — part 3.2.
9. **Pricing a standup in quota.** It is spent from a person's attention first — part 4.1.
10. **Building one standup.** The engineer, the person on support and the manager want three
    different reports from the same queue — part 4.2.

---

## §8 Verify before you code

Read off the installed package on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| a multi-tool live turn | installed `google-adk==2.7.1`, driven through `Runner.run_live` | three `function_call` responses in one turn, each answered by the runtime and returned through the connection's `send_content` before the next was emitted — printed by `live.py` as `['queue_by_category', 'tickets_needing_a_person', 'last_night']` |
| `get_fast_api_app` | installed `google-adk==2.7.1` | takes `agents_dir` and `web` as its two required arguments — the server that would host a browser voice client. It needs a live model to be useful, which Day 74 part 4.2 parked, so this day builds the agent and 🅿️ parks the browser |
| `doi:10.1037/h0043158` record | <https://api.crossref.org/works/10.1037/h0043158> | *The magical number seven, plus or minus two: Some limits on our capacity for processing information.*, Psychological Review 63(2), 81–97, American Psychological Association. The record's `published-print` field is **empty**; its `issued` field gives March 1956, and the paper document says which field it read. There is **no abstract** in the record |

---

## §9 Say it in an interview

*"The interesting thing about building a spoken standup is that correctness stops being the
question. We had an agent that called three tools over a live session, read the queue accurately and
said twelve true sentences — and it was useless, because the two tickets that needed a decision were
sentence six and sentence eleven. On a voice line the listener interrupts. I measured it: the
listener said something after two sentences, and with the queue in its natural order the standup
delivered none of the parts that needed them, while attention-first delivered all of them. Same
facts, same tools, same tokens. The second thing I'd bring up is a bug I actually shipped into the
measurement: the first version worked out which sentences were important by searching the text for a
phrase, and the two orderings phrased it slightly differently — 'need you' against 'needs you' — so
it reported the wrong number and looked plausible. The fix is that importance is a flag you carry
from the data, never something you recover from the words. And the third is the quiet morning: a
standup that says nothing when nothing is wrong is indistinguishable from one that failed to run, so
'nothing needs you' has to be a sentence somebody wrote."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have run the commands rather than read
them. `./m done 77` refuses to commit until they are.

The day is finished when you can say what your standup says on a morning when nothing is wrong, and
when you can explain why "it was accurate" is not an answer to "was it any good".

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 77 | 2026-09-06 | ADK-57, AG-25 | 11 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth 77` is green over the eleven parts and the paper.
`lab/gate.py` is **red** on all six checks by design — `sutra/standup.py` is the build brief. Phase
11's gate is *nightly job + voice standup within free quota*: Day 73 built the first half, today
builds the second, and Day 78 runs the gate on both.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one row, checked live today:

```text
| The magical number seven, plus or minus two: Some limits on our capacity for processing information. | doi:10.1037/h0043158 | 1956 | 2026-09-06 | 77 | `days/day-77-the-standup-agent/papers/01-chunking.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows.

**Commit:**

```text
day 77: the standup agent - three tools, and the order that is the product - closes ADK-57, AG-25
```

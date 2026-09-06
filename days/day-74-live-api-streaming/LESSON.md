---
day: 74
phase: 11
phase_name: "Ambient & live"
title: "Live API I — streaming architecture; free-quota check"
ids: ["ADK-52", "ADK-53"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: build
plan_version: "v2.2.1"
parts: 13
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 74 — Live API I

> **Yesterday (Day 73):** ambient agents. A nightly job that survives being killed, a lock that
> outlives the run that took it, a digest that reassures, and artefacts with no date on them.
> **Today:** the opposite end of the same phase. Yesterday nobody was watching; today somebody is
> watching every character as it arrives, and the architecture question is what you put on the screen
> before the answer exists.
> **Tomorrow (Day 75):** Live API II — the bidirectional voice loop, which today's free-quota check
> decides how much of we can actually build.

---

## §1 Where we are

Streaming is the first thing anyone notices about a modern assistant and the last thing anyone
designs. The feature is one field on `RunConfig`; the day is about what that field does to everything
downstream of it.

Four findings, all measured against the real runtime with a scripted model.

**The field is one line deep.** `RunConfig(streaming_mode=StreamingMode.SSE)` reaches the model as
`stream=True` — `stream=run_config.streaming_mode == StreamingMode.SSE`, one expression in ADK's own
flow. The same agent, same instruction, same question then produces **1 event** or **6**, and the
share of the answer that must exist before anything can go on screen falls from **100% to 13%**.

**The last event is the whole answer again.** ADK's own contract says the final chunk carries
"aggregated content from entire turn, identical to `stream=False` output". So the obvious rule —
concatenate every text you were handed — produces **180 characters where the answer is 90**. No
exception, no warning, and the text is not even corrupted: it is the answer, followed by the answer.

**The wire format has exactly one framing rule and it is easy to break.** A blank line ends a
message and an unrecognised field is ignored, so a payload containing a newline of its own splits
into a `data:` line and a line with no prefix — **90 characters sent, 77 received**, silently.

**And the reader can leave.** Consume two events and hang up, and the runtime logs `Root node desk
was cancelled.` — and the session ends up holding **one** event, the user's question. The reader saw
two chunks of an answer that, as far as the conversation's history is concerned, was never given.

Underneath all of it is the free-quota check that ADK-53 asks for, and it has a clear answer: `BIDI`
needs a model that holds an audio session open, which Addendum 02 will not pay for, so bidi voice is
🅿️ parked. `SSE` is text over one ordinary HTTP response and costs nothing extra, and speech is the
browser's own job.

---

## §2 The map

Five sections. Section 1 is what streaming is and the single field that turns it on. Section 2 is the
trap in the event stream. Section 3 is the wire format underneath. Section 4 is the free-quota check
and what a live session would actually require. Section 5 is the reader who leaves, and what a real
streaming system has that this one does not.

### 1 — The blank screen

*What streaming changes, and the one field that asks for it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The blank screen](parts/01-the-blank-screen/1.1-the-blank-screen.md) | Streaming changes when the reader is served, never how fast the work is | `foundation` |
| 1.2 | [One field on RunConfig](parts/01-the-blank-screen/1.2-one-field-on-runconfig.md) | `StreamingMode` reaches the model as `stream=True`, in one expression | `foundation` |
| 1.3 | [One event or six](parts/01-the-blank-screen/1.3-one-event-or-six.md) | The same turn, measured: 6 events against 1, and 13% against 100% | `working` |

### 2 — The final chunk

*The event stream's one trap, and the three rules people write for it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The answer, twice](parts/02-the-final-chunk/2.1-the-answer-twice.md) | 💥 180 characters where the answer is 90, with nothing raised | `production` |
| 2.2 | [Three rules, two of them right](parts/02-the-final-chunk/2.2-three-rules.md) | Partials-only and final-only both work, and they are not interchangeable | `working` |
| 2.3 | [A partial is not always text](parts/02-the-final-chunk/2.3-not-always-text.md) | Function calls, bytes and thoughts arrive as partials too | `production` |

### 3 — The wire

*What is actually travelling down the connection.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [What SSE actually is](parts/03-the-wire/3.1-what-sse-actually-is.md) | Four fields, one blank line, and a format you can read with `curl` | `working` |
| 3.2 | [The newline in your payload](parts/03-the-wire/3.2-the-newline-in-your-payload.md) | 💥 90 characters sent, 77 received, no error anywhere | `production` |
| 3.3 | [What sits in between](parts/03-the-wire/3.3-what-sits-in-between.md) | A proxy that buffers turns your stream back into one response | `production` |

### 4 — The bill for voice

*The free-quota check ADK-53 asks for, done before anything is built.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [What a live session is made of](parts/04-the-bill-for-voice/4.1-what-a-live-session-is-made-of.md) | A queue instead of a message, and 11 `RunConfig` fields that exist only here | `working` |
| 4.2 | [The free-quota check](parts/04-the-bill-for-voice/4.2-the-free-quota-check.md) | 🅿️ What is parked, what is not, and the fact this page could not verify | `production` |

### 5 — In production

*The reader who leaves, and the distance to a real one.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The reader who leaves](parts/05-in-production/5.1-the-reader-who-leaves.md) | 💥 Two events consumed, one event stored, and no assistant turn at all | `production` |
| 5.2 | [What a real streaming system adds](parts/05-in-production/5.2-what-a-real-streaming-system-adds.md) | Reconnection, ordering, backpressure and the cost you keep paying | `production` |

### The paper — read it last

*Principle 4 at the scale of a day: build the stream, then read why anyone wanted one.*

| # | Paper | What it answers |
| --- | --- | --- |
| 01 | [Response time in man-computer conversational transactions](papers/01-response-time.md) | `doi:10.1145/1476589.1476628` — the thresholds that make streaming worth building, from 1968 |

---

## §3 Setup — run this

```bash
mkdir -p days/day-74-live-api-streaming/lab/papers/response-time
cd days/day-74-live-api-streaming/lab
touch _fake.py
touch modes.py partials.py wire.py cancel.py livecheck.py gate.py
touch papers/response-time/bands.py papers/response-time/demo.py
```

**What each file is for:**

- `_fake.py` is the file to read first: a `BaseLlm` subclass that honours the `stream` flag the
  runtime hands it, and answers from a five-chunk script. Everything else — the runner, the agent,
  the event loop, `RunConfig` — is the real thing.
- `modes.py` runs the same turn under `StreamingMode.SSE` and `StreamingMode.NONE`.
- `partials.py` applies three different rules to one stream and reports which give back the answer.
- `wire.py` is Server-Sent Events framed and parsed by hand, before adopting anybody's library
  (Principle 4).
- `cancel.py` is the reader closing the connection half-way, and what the session remembers.
- `livecheck.py` reads what a bidirectional session would require off the installed package.
- `gate.py` is the eval.

Verify the lab is gitignored before the first run:

```bash
git check-ignore -v days/day-74-live-api-streaming/lab/_fake.py
```

**Why:**

- `days/*/lab/` is ignored repo-wide (Principle 9). Today nothing secret is written, and the habit is
  the point.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.
`google-adk` was pinned on the day it was first used and is not touched here.

---

## §4 Build brief

**`sutra/stream.py`** — the one place in the repository that turns a stream of events back into an
answer, so that the rule exists once rather than in every caller.

- `TODO(me)`: `collect(events)` — the rule. It must look at `event.partial`, because a rule that
  ignores the flag returns the answer twice (part 2.1), and the gate reads the source for it.
- `TODO(me)`: decide **which** correct rule you want — accumulate the partials, or take the final —
  and write the reason in the docstring. Part 2.2 argues that they are not interchangeable and that
  the choice is about what happens when the turn does not finish.
- `TODO(me)`: `answer(..., mode)` — the streaming mode as a parameter. A hard-coded mode cannot be
  turned off for a batch caller, and Day 73's nightly job is exactly that caller.
- `TODO(me)`: `frame(chunk)` — SSE framing that splits a payload on newlines. The gate calls it with
  `"a\nb"` and expects two `data:` lines.
- `TODO(me)`: decide what your handler does when the client disconnects mid-turn. Part 5.1 measures
  the default and it is not what most people expect.

**`tests/test_stream.py`**

- `TODO(me)`: a test that `collect` on a stream ending in a non-partial event returns the answer
  **once**. That single test is the difference between this module and part 2.1's bug.
- `TODO(me)`: a test that `frame` round-trips a payload containing a newline.
- `TODO(me)`: a test for a stream that stops after two partials — decide what `collect` should return
  and assert it, because "whatever happens" is not a decision.

---

## §5 The eval that must be able to fail

```bash
cd days/day-74-live-api-streaming/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/stream.py`, all red today because the module is the build brief. A check
that cannot run counts as a **failure** rather than as skipped (Principle 11).

Two of the day's runs encode their verdict in the exit code, and they are the ones to keep:

```bash
uv run python wire.py; echo "exit: $?"
uv run python wire.py --naive; echo "exit: $?"
```

The first exits `0` — every chunk round-tripped. The second exits `1`, having dropped 13 characters
without an error. The paper's demo does the same thing for its own claim, and `partials.py --naive`
exits `1` on the double-text rule. Two more ablations exist and are exercised in their parts:
`modes.py --none` and `cancel.py --finish`.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

`_fake.py` is a real `BaseLlm` subclass, so every measurement on this day runs inside the real runner
and the real event loop — and it contacts nothing. That matters more than usual here: streaming is
the one feature where it is tempting to "just try it against the API and watch the words appear", and
watching words appear teaches you nothing about the final chunk.

The day's timing figures come from the paper's demo, which is a **simulation with a stated
assumption** (`SECONDS_PER_TOKEN = 0.04`) rather than a measurement of any provider. The demo says so
in its own docstring and the paper document says so again.

---

## §7 Traps

1. **Thinking streaming makes anything faster.** The same tokens are produced at the same rate; the
   total is unchanged. What moves is when the reader is first served — part 1.1.
2. **Assuming the mode is a client concern.** It reaches the model as an argument and changes what
   the model yields, so it is an architecture decision rather than a display one — part 1.2.
3. **Concatenating every event's text.** The final event repeats the whole turn: 180 characters where
   the answer is 90 — part 2.1.
4. **Assuming a partial is text.** Function calls, bytes and thoughts stream too, and a renderer that
   assumes `part.text` drops them — part 2.3.
5. **Framing one `data:` line per chunk.** A newline in the payload silently truncates the message —
   part 3.2.
6. **Forgetting what is between you and the reader.** A buffering proxy re-assembles your stream into
   one response and nothing on your side changes — part 3.3.
7. **Reaching for bidi because it is the impressive one.** It needs a session with a model that holds
   audio open, and Addendum 02 does not pay for that — part 4.1.
8. **Believing a free-tier claim you did not read today.** Part 4.2 records what this page could and
   could not verify, and the difference is the lesson (P7).
9. **Ignoring the disconnect.** The reader leaves, the run is cancelled, and the session keeps no
   assistant turn — so the next question is asked of a conversation in which the agent never spoke —
   part 5.1.
10. **Rendering partials directly into the DOM.** Every chunk is a re-layout, and the flicker is
    yours to fix — part 5.2.

---

## §8 Verify before you code

Read off the installed package and fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| the `stream=` seam | installed `google-adk==2.7.1`, `google/adk/flows/llm_flows/base_llm_flow.py` | `stream=run_config.streaming_mode == StreamingMode.SSE` — one expression turns the config field into the model's argument. Part 1.2 quotes it |
| `BaseLlm.generate_content_async` | installed `google-adk==2.7.1` | its docstring states the contract: `stream=False` yields exactly one response with `partial=False`; `stream=True` yields chunks with `partial=True` then a final `partial=False` carrying "aggregated content from entire turn, identical to stream=False output". Part 2.1 quotes it verbatim |
| `Runner.run_live` and `RunConfig` | installed `google-adk==2.7.1` | `run_live` requires `live_request_queue`; eleven `RunConfig` fields exist only for live sessions. Part 4.1 prints both |
| Gemini Live API overview | <https://ai.google.dev/gemini-api/docs/live-api> | fetched 2026-09-06 (a redirect from `/docs/live`); headline *Gemini Live API overview*. **The free-tier and rate-limit tables are rendered by JavaScript and are not in the served HTML**, so this page did **not** verify the Live API's free-tier status — part 4.2 records that as an unknown with the check to run, rather than guessing (P7) |
| `doi:10.1145/1476589.1476628` record | <https://api.crossref.org/works/10.1145/1476589.1476628> | *Response time in man-computer conversational transactions*, AFIPS '68 (Fall, part I), page 267, 1968 — no abstract in the record, and the paper document says so |

---

## §9 Say it in an interview

*"Streaming is one config field and the interesting part is everything downstream of it. In ADK it's
`RunConfig(streaming_mode=SSE)`, and that reaches the model as `stream=True` — one expression in the
flow — so the same agent yields one event or six. What people get wrong is the last event: the
contract says the final chunk carries the whole turn's content again, identical to the non-streaming
output, so the obvious rule of concatenating every text you're handed gives you the answer twice. I
measured 180 characters where the answer was 90, with nothing raised. Underneath, the wire format is
tiny — Server-Sent Events is `data:` lines and a blank line ends the message, and an unknown field is
ignored — which means a payload with a newline in it splits, the second line has no `data:` prefix,
and it's dropped in silence. Ninety characters sent, seventy-seven received. The one that surprised
me was cancellation: the reader closes the tab, the run is cancelled, and the session ends up with
just their question — no assistant turn — so the next message is asked of a conversation where the
agent never spoke. And the honest architectural point is that streaming doesn't make anything faster.
The total is identical. It changes how much of the answer has to exist before you can show any of
it — thirteen per cent instead of a hundred — which is a claim about attention, not about
throughput."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have run the commands rather than read
them. `./m done 74` refuses to commit until they are.

The day is finished when you can say what your code does with the last event of a stream without
opening the file — and when you can say what your users would lose if you turned streaming off, in
words that do not include the word "faster".

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 74 | 2026-09-06 | ADK-52, ADK-53 | 13 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth 74` is green over the thirteen parts and the paper.
`lab/gate.py` is **red** on all six checks by design — `sutra/stream.py` is the build brief. Phase
11's gate is *nightly job + voice standup within free quota*; today decides how much of the second
half is buildable, and Day 75 spends that answer.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one row, checked live today:

```text
| Response time in man-computer conversational transactions | doi:10.1145/1476589.1476628 | 1968 | 2026-09-06 | 74 | `days/day-74-live-api-streaming/papers/01-response-time.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows.

**Commit:**

```text
day 74: live api I - streaming architecture, the final chunk, and the free-quota check - closes ADK-52, ADK-53
```

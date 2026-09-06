---
day: 75
phase: 11
phase_name: "Ambient & live"
title: "Live API II — the bidi voice loop"
ids: ["ADK-54", "ADK-55"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: build
plan_version: "v2.2.1"
parts: 11
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 75 — Live API II

> **Yesterday (Day 74):** streaming architecture. One field on `RunConfig`, the final chunk that
> hands you the answer twice, the newline that loses thirteen characters in silence — and a
> free-quota check that parked bidirectional voice and recorded one fact it could not verify.
> **Today:** the loop it parked. The paid model stays parked; the **program shape** does not, because
> `run_live` can be driven end to end against a scripted connection, and everything interesting about
> a voice loop is in the shape rather than in the audio.
> **Tomorrow (Day 76):** the phase gate — the nightly job and the voice standup, both inside free
> quota.

---

## §1 Where we are

Day 74 part 4.1 read `Runner.run_live` off the installed package and found a different shape of
program: a queue you keep pushing into, rather than one message you hand over. Today that shape is
built and measured, with a `BaseLlmConnection` of our own at the far end so the whole day costs
nothing.

**A session is not a turn, and it does not end when you think.** The model finishes, `turn_complete`
arrives — and the loop keeps waiting. Closing `LiveRequestQueue` is not enough either: the runtime
stops reading input and hangs up on the model, and the `async for` is **still waiting** when a 2.0s
deadline stops it. What ends a session is the consumer closing the event stream. A voice endpoint that
only closes the queue leaks one session per caller.

**The caller can talk over the answer, and exactly one thing tells you so.** Interrupt after two
chunks and the answer stops at **3 of 6** with an `interrupted` event in the stream. Run the same call
against a connection that ignores interruptions and the caller sits through **6 of 6** and then a
second answer — **12 chunks** against 3, with nothing anywhere saying stop.

**Audio is priced by the second, not by the sentence.** Two seconds of held-open microphone is
**64,000 bytes**, every one of them silence, for a question that is **20 bytes** as text. The
connection carried 3,200 times as much to ask the same thing.

**And somebody has to decide when the caller stopped speaking.** With turn markers the far end
receives `ActivityStart`, three blobs, `ActivityEnd` — five things through one method, two of which
are not sound. Without them it receives three identical blobs and has to work out from the audio
whether a pause was the end of a sentence or somebody thinking.

---

## §2 The map

Four sections. Section 1 is the open line and who ends it. Section 2 is the caller talking over the
answer, which is the thing a voice loop exists for. Section 3 is what actually travels while the line
is open. Section 4 is what it costs and what a real one adds.

### 1 — The open line

*A call rather than a request, and who is allowed to hang up.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A call, not a request](parts/01-the-open-line/1.1-a-call-not-a-request.md) | Both parties can speak at any moment, which is a different program | `foundation` |
| 1.2 | [Five methods and a context manager](parts/01-the-open-line/1.2-five-methods.md) | A live model is `send_history`, `send_content`, `send_realtime`, `receive`, `close` | `working` |
| 1.3 | [Who ends the call](parts/01-the-open-line/1.3-who-ends-the-call.md) | 💥 Closing the queue is not closing the session, and the loop waits for ever | `production` |

### 2 — Talking over

*The caller interrupts, and the one event that says so.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The caller interrupts](parts/02-talking-over/2.1-the-caller-interrupts.md) | Interruption is a normal event on an open line, not an error | `working` |
| 2.2 | [The one event that says stop](parts/02-talking-over/2.2-the-event-that-says-stop.md) | 💥 3 chunks against 12, and nothing else in the stream tells you | `production` |
| 2.3 | [What the client does with it](parts/02-talking-over/2.3-what-the-client-does.md) | Stop playing, drop what you buffered, and fix the transcript | `production` |

### 3 — What goes down the wire

*Sound, and the markers that are not sound.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Audio is bytes, and bytes are seconds](parts/03-what-goes-down-the-wire/3.1-audio-is-bytes.md) | 64,000 bytes of silence against a 20-byte question | `working` |
| 3.2 | [Who says the turn ended](parts/03-what-goes-down-the-wire/3.2-who-says-the-turn-ended.md) | `ActivityStart`, three blobs, `ActivityEnd` — or three blobs and a guess | `production` |

### 4 — What it costs, and what a real one adds

*A connection per caller, a session that outlives them, and the distance to production.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [A connection per caller](parts/04-what-it-costs/4.1-a-connection-per-caller.md) | Concurrency becomes a resource question rather than a throughput one | `production` |
| 4.2 | [The session that never ended](parts/04-what-it-costs/4.2-the-session-that-never-ended.md) | 💥 The deadline is the only thing standing between you and a leak | `production` |
| 4.3 | [What a real voice system adds](parts/04-what-it-costs/4.3-what-a-real-voice-system-adds.md) | Echo, latency budget, transcripts, and the parked half | `production` |

### The paper — read it last

*Principle 4 at the scale of a day: build the turn-taking, then read the study of it.*

| # | Paper | What it answers |
| --- | --- | --- |
| 01 | [A simplest systematics for the organization of turn-taking for conversation](papers/01-turn-taking.md) | `doi:10.2307/412243` — why nobody allocates turns, and why that works |

---

## §3 Setup — run this

```bash
mkdir -p days/day-75-the-bidi-voice-loop/lab/papers/turn-taking
cd days/day-75-the-bidi-voice-loop/lab
touch _live.py
touch session.py barge_in.py audio.py vad.py gate.py
touch papers/turn-taking/floor.py papers/turn-taking/demo.py
```

**What each file is for:**

- `_live.py` is the file to read first: a `BaseLlmConnection` that implements all five methods,
  counts everything that passes through it, and can be told whether to honour an interruption. The
  runner, the queue, `RunConfig` and every event are the real thing.
- `session.py` asks who ends a session, three different ways.
- `barge_in.py` is the caller talking over the answer.
- `audio.py` is what an open microphone costs against a typed question.
- `vad.py` is who decides the turn ended.
- `gate.py` is the eval.

Verify the lab is gitignored before the first run:

```bash
git check-ignore -v days/day-75-the-bidi-voice-loop/lab/_live.py
```

**Why:**

- `days/*/lab/` is ignored repo-wide (Principle 9). Today's bytes are synthetic silence, and a day
  that sends audio anywhere is a day to check this on.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.

---

## §4 Build brief

**`sutra/voice.py`** — the one place that owns a voice session from hello to hang-up.

- `TODO(me)`: `call(...)` — a single function that opens the session, consumes the events, and closes
  **both** the queue and the event stream. Part 1.3 measures why the second one is not optional.
- `TODO(me)`: handle the `interrupted` event, and decide what your client does when it arrives. Part
  2.3 lists the three things and only one of them is code you can write without a decision.
- `TODO(me)`: a **deadline** on the session. Part 4.2 is the failure it prevents, and the gate checks
  for it because nothing else can.
- `TODO(me)`: decide whether your client sends turn markers or lets the far end infer the turn from
  the audio. Part 3.2 is the trade and there is no default worth inheriting.
- `TODO(me)`: decide what goes into the session transcript when a turn is interrupted half-way. Day
  74 part 5.1 asked the same question about a reader who leaves; this is the same question with two
  people in the room.

**`tests/test_voice.py`**

- `TODO(me)`: a test that `call` returns rather than hanging — assert it completes within a deadline
  and fails loudly if it does not.
- `TODO(me)`: a test that an interruption stops the answer, asserting on the chunks delivered rather
  than on a log line.
- `TODO(me)`: a test for the transcript after an interrupted turn, asserting whatever you decided
  above. A test is how a decision survives the person who made it.

---

## §5 The eval that must be able to fail

```bash
cd days/day-75-the-bidi-voice-loop/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/voice.py`, all red today because the module is the build brief. A check that
cannot run counts as a **failure** rather than as skipped (Principle 11).

Three of the day's runs encode their verdict in the exit code, and they are the ones to keep:

```bash
uv run python session.py; echo "exit: $?"
uv run python session.py --queue-only; echo "exit: $?"
uv run python barge_in.py --ignore; echo "exit: $?"
```

The first exits `0` — the session ended. The second exits `1` after a deadline, having closed the
queue and nothing else. The third exits `1` because nothing told the client to stop talking. Every
script on this day carries a deadline of its own and reports reaching it as a **failure**, because a
demonstration that hangs forever is not a demonstration.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

Day 74 part 4.2 parked bidirectional voice and recorded that it could **not** verify the Live API's
free-tier status. Nothing today changes that, and nothing today needed it: `BaseLlm.connect` is a
documented seam, so a scripted `BaseLlmConnection` drives `Runner.run_live` through the real runtime
with no provider on the other end.

The audio figures come from synthetic silence and a **stated assumption** about the wire format
(`RATE = 32000` bytes per second in `audio.py`). The byte counts are measured; the conversion to
seconds is arithmetic on an assumption, and both the script and part 3.1 say so.

---

## §7 Traps

1. **Treating a live session as a long turn.** It is a call: both parties may speak at any moment,
   and the program has two things happening at once — part 1.1.
2. **Implementing `connect` as a generator.** It is an async context manager, and the difference is
   who owns the closing — part 1.2.
3. **Ending the session by closing the queue.** Measured: the runtime hangs up on the model and the
   event loop keeps waiting — part 1.3.
4. **Assuming a turn ends the session.** `turn_complete` is the model finishing a sentence, not the
   caller finishing the call — part 1.3.
5. **Treating an interruption as an error.** It is the normal way a conversation is steered, and a
   loop that cannot be interrupted is a loop nobody will talk to twice — part 2.1.
6. **Ignoring the `interrupted` event.** Nothing else in the stream says stop, and the client is
   already holding audio it is about to play — part 2.2.
7. **Stopping the stream and forgetting the buffer.** The words the caller hears come from what you
   already queued, not from what arrives next — part 2.3.
8. **Pricing a voice session like a text one.** An open microphone costs its duration whether anybody
   speaks or not — part 3.1.
9. **Letting the far end guess where turns end.** A pause is a breath, a bad line and the end of a
   sentence, and only the client knows which — part 3.2.
10. **Sizing a voice service by requests per second.** It is connections held open, which is a
    different capacity question with a different failure — part 4.1.
11. **Shipping without a session deadline.** One caller who closes a laptop leaves a session open with
    nobody on it — part 4.2.

---

## §8 Verify before you code

Read off the installed package on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| `BaseLlm.connect` | installed `google-adk==2.7.1` | `connect(self, llm_request: LlmRequest) -> AbstractAsyncContextManager[BaseLlmConnection]` — a context manager, not a generator. Part 1.2 |
| `BaseLlmConnection` | installed `google-adk==2.7.1` | five methods: `send_history(list[types.Content])`, `send_content(types.Content)`, `send_realtime(types.Blob)`, `receive() -> AsyncGenerator[LlmResponse, None]`, `close()`. Part 1.2 quotes the signatures |
| `LiveRequestQueue` and `LiveRequest` | installed `google-adk==2.7.1` | the queue offers `send_content`, `send_realtime`, `send_activity_start`, `send_activity_end`, `send_audio_stream_end`, `send`, `get`, `close`; a `LiveRequest` carries `content`, `blob`, `activity_start`, `activity_end`, `audio_stream_end`, `close`, `partial`, `state_delta`. Parts 3.1 and 3.2 |
| the hang-up path | installed `google-adk==2.7.1`, `google/adk/flows/llm_flows/base_llm_flow.py` | `if live_request.close: await llm_connection.close()` followed by `return` — closing the queue closes the model connection and stops the send loop, and part 1.3 measures what it does **not** do |
| the marker path | installed `google-adk==2.7.1`, same file | `if live_request.activity_start: await llm_connection.send_realtime(types.ActivityStart())`, and the matching `activity_end` branch — which is why part 3.2's connection sees markers arrive on `send_realtime` |
| `doi:10.2307/412243` record | <https://api.crossref.org/works/10.2307/412243> | *A simplest systematics for the organization of turn-taking for conversation*, Language 50(4), 696–735, December 1974, Cambridge University Press. The record carries an abstract, which the paper document quotes rather than paraphrases |

---

## §9 Say it in an interview

*"A bidirectional session is a different program from a request, and the thing that catches people is
lifetime. The turn ending is not the session ending — and closing the input queue isn't either. I
measured it: after `turn_complete`, closing the request queue makes the runtime hang up on the model,
and the event loop is still waiting when a two-second deadline stops it. What ends the session is the
consumer closing the event stream, so a voice endpoint that only closes the queue leaks a session per
caller. The second thing is interruption, which is the whole reason to hold a line open. The caller
talks over the answer and exactly one event tells you — `interrupted`. With it honoured, the caller
heard three chunks of a six-chunk answer; with it ignored, twelve chunks across two answers, and
nothing in the stream said stop, which on a speaker means two voices at once. Third is cost, and it's
the one that changes the architecture: an open microphone is priced by duration, not by content. Two
seconds of silence was sixty-four thousand bytes for a question that's twenty bytes as text. So
capacity is connections held open rather than requests per second, and every session needs a deadline
because a caller who closes a laptop doesn't tell you anything."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have run the commands rather than read
them. `./m done 75` refuses to commit until they are.

The day is finished when you can say what closes a voice session without opening the file, and when
you can explain to somebody who has only built request/response services why an interruption is a
feature rather than an error.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 75 | 2026-09-06 | ADK-54, ADK-55 | 11 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth 75` is green over the eleven parts and the paper.
`lab/gate.py` is **red** on all six checks by design — `sutra/voice.py` is the build brief. Phase 11's
gate is *nightly job + voice standup within free quota*; Day 73 built the first half, today builds the
second half's loop, and the voice itself stays 🅿️ parked until a free path exists.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one row, checked live today:

```text
| A simplest systematics for the organization of turn-taking for conversation | doi:10.2307/412243 | 1974 | 2026-09-06 | 75 | `days/day-75-the-bidi-voice-loop/papers/01-turn-taking.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows.

**Commit:**

```text
day 75: live api II - the bidi voice loop, interruption, and who ends the call - closes ADK-54, ADK-55
```

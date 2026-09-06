---
day: 76
phase: 11
phase_name: "Ambient & live"
title: "VAD events and non-blocking tools — the conversation doesn't freeze mid-tool"
ids: ["ADK-56", "ADK-77"]
principles: [1, 2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: build
plan_version: "v2.2.1"
parts: 11
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 76 — VAD events and non-blocking tools

> **Yesterday (Day 75):** the bidi voice loop. Who ends a call, the one event that says stop, and a
> session priced by its duration — all driven against a scripted connection at zero quota.
> **Today:** the same loop with a **tool call in the middle of it**, which is where a voice agent
> stops being a demo. A caller on an open line is entitled to speak while the desk is busy, and
> whether the line is still listening turns out to depend on one word inside the tool.
> **Tomorrow (Day 77):** the standup agent — a voice client over the queue state, which is the phase
> gate's second half.

---

## §1 Where we are

A tool call in a request/response agent is invisible. The caller sent one message and is waiting for
one answer, and whether that wait is spent thinking or looking something up makes no difference to
them.

On an open line it makes every difference, and the day is four measurements.

**The line can go dead, and the cause is one word.** With the lookup written as
`await asyncio.sleep(...)`, **4 slices** of the caller's audio reach the model's connection while the
tool is still running. With the identical lookup written as `time.sleep(...)`, **0** do — the audio
does not arrive late, it does not appear in the connection's log at all, because the task that would
have delivered it never got to run. The tool is declared `async def` in **both** cases. Marking a
function `async` does not make it non-blocking; awaiting inside it does.

**The result has to come back, and *when* is a setting.** ADK exposes
`BaseTool.response_scheduling`, whose values are `SILENT`, `WHEN_IDLE` and `INTERRUPT` — documented
in the package as *"Controls when the model reacts to the tool's response"*. A request/response agent
has never had to answer that question, because there was nothing else going on.

**Deciding when the caller stopped talking is configuration, not fate.** The installed package offers
`AutomaticActivityDetection` with `disabled`, start and end sensitivity, `prefix_padding_ms` and
`silence_duration_ms`; `ActivityHandling` with `START_OF_ACTIVITY_INTERRUPTS` and `NO_INTERRUPTION`;
and `TurnCoverage` with three values. Day 75's barge-in ablation turns out to be a supported setting.

**And the edges of speech are quiet.** The paper at the end of the day is the 1975 endpoint-detection
algorithm, and its demo is the argument for why any of these knobs exist: an energy threshold alone
clips **8 frames** off a word that starts and ends with a fricative, and recovers all of them once
zero-crossing rate is allowed to extend the endpoints.

---

## §2 The map

Four sections. Section 1 is the tool call and the line going dead. Section 2 is what happens when the
result comes back. Section 3 is deciding when the caller stopped talking. Section 4 is what to watch
and what a real one adds.

### 1 — The tool in the middle

*A wait the caller can hear, and the one word that decides whether the line survives it.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The wait nobody sees](parts/01-the-tool-in-the-middle/1.1-the-wait-nobody-sees.md) | A tool call is invisible in a request and unavoidable on a line | `foundation` |
| 1.2 | [The sequence, measured](parts/01-the-tool-in-the-middle/1.2-the-sequence-measured.md) | Call, tool, result back through `send_content`, answer — all real runtime | `working` |
| 1.3 | [The line that goes dead](parts/01-the-tool-in-the-middle/1.3-the-line-that-goes-dead.md) | 💥 4 slices against 0, and `async def` in both | `production` |

### 2 — When the answer comes back

*The question a request never had to ask.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Three schedulings](parts/02-when-the-answer-comes-back/2.1-three-schedulings.md) | `SILENT`, `WHEN_IDLE`, `INTERRUPT`, read off the package | `working` |
| 2.2 | [Choosing one](parts/02-when-the-answer-comes-back/2.2-choosing-one.md) | Each is wrong for something, and `None` is a choice too | `production` |
| 2.3 | [What to say while you wait](parts/02-when-the-answer-comes-back/2.3-what-to-say-while-you-wait.md) | 💥 Filler is content, and content can lie | `production` |

### 3 — Deciding when they stopped

*Voice activity detection, as a set of knobs somebody has to turn.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The knobs](parts/03-deciding-when-they-stopped/3.1-the-knobs.md) | Every VAD field the installed package offers, and what each names | `working` |
| 3.2 | [Sensitivity is a trade](parts/03-deciding-when-they-stopped/3.2-sensitivity-is-a-trade.md) | Cutting people off and never letting them finish are the same dial | `production` |
| 3.3 | [Interruption is a setting](parts/03-deciding-when-they-stopped/3.3-interruption-is-a-setting.md) | Yesterday's ablation is `NO_INTERRUPTION`, and it is supported | `production` |

### 4 — In production

*What the silence hides, and the distance to a real one.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The silence you cannot see](parts/04-in-production/4.1-the-silence-you-cannot-see.md) | A frozen line emits nothing, so the signal has to be built | `production` |
| 4.2 | [What a real one adds](parts/04-in-production/4.2-what-a-real-one-adds.md) | Timeouts per tool, cancellation, and the parked half | `production` |

### The paper — read it last

*Principle 4 at the scale of a day: turn the knobs, then read what they are approximating.*

| # | Paper | What it answers |
| --- | --- | --- |
| 01 | [An Algorithm for Determining the Endpoints of Isolated Utterances](papers/01-endpoint-detection.md) | `doi:10.1002/j.1538-7305.1975.tb02840.x` — why the edges of a word are the hard part |

---

## §3 Setup — run this

```bash
mkdir -p days/day-76-vad-and-non-blocking-tools/lab/papers/endpoints
cd days/day-76-vad-and-non-blocking-tools/lab
touch _live.py
touch freeze.py scheduling.py vadconfig.py gate.py
touch papers/endpoints/detect.py papers/endpoints/demo.py
```

**What each file is for:**

- `_live.py` is the file to read first: yesterday's scripted connection with a tool added, and a
  timestamp on everything that passes through it. One switch, `BLOCKING`, decides how the tool waits.
- `freeze.py` is the day's central measurement.
- `scheduling.py` reads `FunctionResponseScheduling` and `BaseTool.response_scheduling` off the
  installed package and quotes the package's own description of each value.
- `vadconfig.py` prints every voice-activity field the installed package offers.
- `gate.py` is the eval.

Verify the lab is gitignored before the first run:

```bash
git check-ignore -v days/day-76-vad-and-non-blocking-tools/lab/_live.py
```

**Why:**

- `days/*/lab/` is ignored repo-wide (Principle 9), and today's lab writes nothing, which is the
  easiest kind of day to stop checking on.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.

---

## §4 Build brief

**`sutra/livetools.py`** — the tools the desk is allowed to call while somebody is on the line.

- `TODO(me)`: `TOOLS`, a list, so the set of tools a live session exposes exists in one place rather
  than being assembled at each call site.
- `TODO(me)`: every tool `async def` **and actually awaiting** — the gate checks both, because the
  first without the second is part 1.3's failure and it passes every ordinary review.
- `TODO(me)`: no `time.sleep`, and no synchronous client that behaves like one. Part 1.3 is why; the
  gate greps for the easy case and cannot catch the hard one.
- `TODO(me)`: declare, on at least one tool, how its result should come back — `is_long_running` or
  `response_scheduling`. Part 2.2 argues that leaving both unset is a decision made by default.
- `TODO(me)`: decide what the caller hears while a tool runs, and write down why. Part 2.3 is the
  honesty problem in it.
- `TODO(me)`: a per-tool timeout. Part 4.2 is the argument; nothing in the framework will do it for
  you.

**`tests/test_livetools.py`**

- `TODO(me)`: a test that every tool in `TOOLS` is a coroutine function.
- `TODO(me)`: a test that a slow tool does not stop the loop — start it, and assert something else
  gets to run while it is waiting. This is the test that would have caught part 1.3.
- `TODO(me)`: a test for whatever you decided about the caller hearing something during a wait.

---

## §5 The eval that must be able to fail

```bash
cd days/day-76-vad-and-non-blocking-tools/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/livetools.py`, all red today because the module is the build brief. A check
that cannot run counts as a **failure** rather than as skipped (Principle 11).

The day's red-alarm run is the freeze measurement, and its two arms encode the verdict in the exit
code:

```bash
uv run python freeze.py; echo "exit: $?"
uv run python freeze.py --blocking; echo "exit: $?"
```

The first exits `0` — the caller's audio arrived while the tool ran. The second exits `1`, having
delivered none of it, with no error anywhere. The paper's demo does the same for its own claim:
`demo.py` exits `0` and `demo.py --off` exits `1`, having clipped eight frames.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

The tool call is real: the runtime chose to run it, ran it, and sent the result back through the
connection's `send_content`. Only the model's side of the conversation is scripted, exactly as on Day
75.

Two things on this day are **read** rather than **run**, and both say so in their own output.
`scheduling.py` prints the package's contract for `response_scheduling`, which is documented as Live
API only — parked since Day 74's free-quota check. `vadconfig.py` prints the voice-activity settings
without applying any of them to a model. Neither is an evaluation, and the parts that use them repeat
that rather than letting a confident sentence imply otherwise.

---

## §7 Traps

1. **Assuming a tool call is invisible.** It is, in a request. On an open line the caller is present
   for it — part 1.1.
2. **Believing `async def` means non-blocking.** The freeze ablation's tool is `async def` and stops
   the whole session — part 1.3.
3. **A synchronous client inside an async tool.** A blocking database driver or HTTP call is
   `time.sleep` with extra steps, and the gate cannot see it — part 1.3.
4. **Never deciding when the result comes back.** `None` preserves the default, and the default was
   not chosen for your tool — part 2.2.
5. **Interrupting the caller with a tool result.** `INTERRUPT` is right for the fire alarm and wrong
   for the order status — part 2.2.
6. **Filling silence with a claim.** "I'm just checking that for you" is content, and if the lookup
   already failed it is false — part 2.3.
7. **Treating voice activity detection as fixed.** It has a `disabled` flag and five knobs, and
   somebody is going to have to turn them — part 3.1.
8. **Tuning sensitivity in one direction.** Cutting people off and letting silence run on are the
   same dial from opposite ends — part 3.2.
9. **Thinking barge-in is a framework property.** `NO_INTERRUPTION` is a supported value — part 3.3.
10. **Monitoring a voice loop with an error rate.** A frozen line raises nothing and ends cleanly —
    part 4.1.
11. **Shipping a tool with no timeout of its own.** The session deadline is not a tool deadline, and
    the difference is which one the caller experiences — part 4.2.

---

## §8 Verify before you code

Read off the installed package on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| `BaseTool.response_scheduling` | installed `google-adk==2.7.1` | `Optional[types.FunctionResponseScheduling] = None`, documented as *"Controls when the model reacts to the tool's response (Live API only)"*, with a sentence for each of `SILENT`, `WHEN_IDLE` and `INTERRUPT`. Part 2.1 quotes the docstring in full |
| `BaseTool.is_long_running` | installed `google-adk==2.7.1` | `bool = False`, *"Whether the tool is a long running operation, which typically returns a resource id first and finishes the operation later"* |
| `types.FunctionResponseScheduling` | installed `google-genai` | `SCHEDULING_UNSPECIFIED`, `SILENT`, `WHEN_IDLE`, `INTERRUPT`. Part 2.1 prints them |
| the voice-activity surface | installed `google-genai` | `RealtimeInputConfig(automatic_activity_detection, activity_handling, turn_coverage)`; `AutomaticActivityDetection(disabled, start_of_speech_sensitivity, end_of_speech_sensitivity, prefix_padding_ms, silence_duration_ms)`; `StartSensitivity` and `EndSensitivity` each `HIGH`/`LOW`; `ActivityHandling` = `START_OF_ACTIVITY_INTERRUPTS`/`NO_INTERRUPTION`; `TurnCoverage` = three values. Part 3.1 prints all of it |
| `RunConfig` | installed `google-adk==2.7.1` | `realtime_input_config: Optional[types.RealtimeInputConfig]` and `explicit_vad_signal: Optional[bool]` — the two fields through which the above reaches a session |
| `doi:10.1002/j.1538-7305.1975.tb02840.x` record | <https://api.crossref.org/works/10.1002/j.1538-7305.1975.tb02840.x> | *An Algorithm for Determining the Endpoints of Isolated Utterances*, Bell System Technical Journal 54(2), 297–315, February 1975. The record carries **no abstract**, and the paper document says so and is careful about what it attributes |

---

## §9 Say it in an interview

*"The thing that catches people is that a tool call stops being invisible the moment the caller is on
a line. In a request nobody can tell whether you were thinking or looking something up. On an open
connection the microphone is live and they're entitled to speak while you're busy — so the question
is whether anything is still listening. I measured it: with the lookup written as an await, four
slices of the caller's audio reached the model's connection while the tool was still running. With
the identical lookup written with `time.sleep`, none did — and they didn't arrive late, they never
appeared at all, because the task that reads input never got to run. The tool was declared `async
def` in both cases, which is the trap: marking a function async doesn't make it non-blocking, and a
synchronous database driver inside an async tool behaves exactly like the ablation. The second thing
a request never has to answer is *when* the result should reach the model — the framework exposes
silent, when-idle and interrupt, and leaving it unset picks a default nobody chose for your tool. And
the third is that deciding when the caller stopped talking is configuration: sensitivity, silence
duration, and whether speech interrupts at all are settings, so 'it cuts me off' and 'it waits for
ever' are the same dial from opposite ends."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have run the commands rather than read
them. `./m done 76` refuses to commit until they are.

The day is finished when you can look at a tool somebody else wrote and say whether it would freeze a
voice session, without running it — and when you can name what the caller experiences for each of the
three response schedulings.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 76 | 2026-09-06 | ADK-56, ADK-77 | 11 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth 76` is green over the eleven parts and the paper.
`lab/gate.py` is **red** on all six checks by design — `sutra/livetools.py` is the build brief. Phase
11's gate is *nightly job + voice standup within free quota*; Day 73 built the first half and Day 77
builds the standup, which is the second.

**`docs/PACKAGES.md`** — no new rows. No package is added today.

**`docs/PAPERS.md`** — one row, checked live today:

```text
| An Algorithm for Determining the Endpoints of Isolated Utterances | doi:10.1002/j.1538-7305.1975.tb02840.x | 1975 | 2026-09-06 | 76 | `days/day-76-vad-and-non-blocking-tools/papers/01-endpoint-detection.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows.

**Commit:**

```text
day 76: vad events and non-blocking tools - the line that goes dead mid-tool - closes ADK-56, ADK-77
```

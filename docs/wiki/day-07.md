# Day 07 - Events & streaming — the record the runtime was keeping anyway

IDs closed: ADK-04, ADK-05 · source: `days/day-07-events-and-streaming/`

## Parts

### 1.1 - An event is a line in a ledger, not a message
`days/day-07-events-and-streaming/parts/01-the-event-object/1.1-an-event-is-a-line-in-a-ledger.md` · level `foundation` · ids ADK-04

An ADK event is one append-only record of something that happened during a run — a message, a tool call, a state change or an error — and an agent's whole behaviour is the ordered list of them, which is why you read events instead of reading a return value.

### 1.2 - The fields that were renamed
`days/day-07-events-and-streaming/parts/01-the-event-object/1.2-the-fields-that-were-renamed.md` · level `working` · ids ADK-04

ADK 2.0 renamed and restructured the event fields, so every event-handling snippet you find on the internet is probably 1.x and will fail on names that no longer exist — this is trap #2 from the plan's §5.1, and the only defence is to print the field list from the package you have installed.

### 1.3 - is_final_response() is not \"the last one\
`days/day-07-events-and-streaming/parts/01-the-event-object/1.3-is-final-response-is-not-the-last-one.md` · level `working` · ids ADK-04

is_final_response() means "this event is complete enough to show a person", not "this is the last event of the run" — several events in one run can answer True, and the last event of a run can answer False.

### 1.4 - The half of an event that is not text
`days/day-07-events-and-streaming/parts/01-the-event-object/1.4-the-half-that-is-not-text.md` · level `working` · ids ADK-04

An event's actions field carries the things the event does rather than the things it says — change a stored value, hand over to another agent, stop a loop — and the runner, not the agent, is what carries them out.

### 1.5 - Which run, which agent, which branch
`days/day-07-events-and-streaming/parts/01-the-event-object/1.5-which-run-which-agent-which-branch.md` · level `production` · ids ADK-04

Four identifying fields — id, invocation_id, author and branch — are what turn a flat list of events into something you can actually read, and every one of them answers a different question you will ask at 11pm.

### 2.1 - The number read out loud
`days/day-07-events-and-streaming/parts/02-the-stream/2.1-the-number-read-out-loud.md` · level `foundation` · ids ADK-05

Streaming exists because a model produces its answer one token at a time anyway, so the choice is only whether you are shown the pieces as they appear or made to wait for the last one — and that choice changes how long the answer feels, never how long it takes.

### 2.2 - The partial flag
`days/day-07-events-and-streaming/parts/02-the-stream/2.2-the-partial-flag.md` · level `working` · ids ADK-05

Streaming is switched on per call with RunConfig(streaming_mode=StreamingMode.SSE), and once it is on, event.partial is the field that tells you whether the event in your hand is a piece still arriving or a finished thing.

### 2.3 - The board and the printed sheet
`days/day-07-events-and-streaming/parts/02-the-stream/2.3-the-board-and-the-printed-sheet.md` · level `working` · ids ADK-05

With streaming on you receive the answer twice — once as chunks and once assembled — and since ADK will not choose for you, every streaming consumer must pick one of three rules and apply it everywhere.

### 2.4 - A partial event changes nothing
`days/day-07-events-and-streaming/parts/02-the-stream/2.4-nothing-is-credited-until-the-receipt.md` · level `production` · ids ADK-05

A partial=True event is forwarded to you and then discarded: it is never appended to the session and its actions are never applied, which is why the duplicate from [2.3](2.3-the-board-and-the-printed-sheet.md) exists and cannot simply be removed.

### 3.1 - One paper at a time
`days/day-07-events-and-streaming/parts/03-the-yield-contract/3.1-one-paper-at-a-time.md` · level `working` · ids ADK-04

An ADK agent yields each event as it happens and stops there until the runner has processed it — this is trap #3 from the plan's §5.1, and the pause is not a cost, it is the promise that everything the event asked for has been done before your code continues.

### 3.2 - Saved is not submitted
`days/day-07-events-and-streaming/parts/03-the-yield-contract/3.2-saved-is-not-submitted.md` · level `production` · ids ADK-04

Code running later in the same run can see a state change before the event carrying it has been yielded, which is useful on purpose and dangerous by accident: what you can read is not yet what has been kept.

### 3.3 - Your own emitter, including the bad reading
`days/day-07-events-and-streaming/parts/03-the-yield-contract/3.3-your-own-emitter.md` · level `working` · ids ADK-04

When you write an agent that emits its own events, an error is another event to yield — carried on error_code and error_message — not something to catch and turn into a polite sentence.

### 4.1 - The meter that cuts off
`days/day-07-events-and-streaming/parts/04-the-brakes/4.1-the-meter-that-cuts-off.md` · level `production` · ids ADK-04

RunConfig.max_llm_calls is the framework's version of the step budget you wrote by hand on Day 3 — it defaults to 500, it is enforced per run, and setting it to zero or a negative number turns the brake off entirely with nothing but a log warning.

### 4.2 - The note the machine refuses
`days/day-07-events-and-streaming/parts/04-the-brakes/4.2-the-note-the-machine-refuses.md` · level `working` · ids ADK-05

RunConfig rejects any keyword it does not recognise while Event silently ignores one, so a typo in a setting stops you at the door and a typo in an event disappears — and knowing which kind of object you are holding is what decides whether you find out.

### 5.1 - 💥 The mechanic who billed at the end
`days/day-07-events-and-streaming/parts/05-failure-lab/5.1-the-mechanic-who-billed-at-the-end.md` · level `production` · ids ADK-04

Today's deliberate failure is trap #3 done on purpose: write an agent that collects its events and returns them, watch it fail two different ways depending on one keyword, and see what the session holds afterwards.

### 6.1 - The camera you already installed
`days/day-07-events-and-streaming/parts/06-reading-a-run/6.1-the-camera-you-already-installed.md` · level `production` · ids ADK-04

Every conversation you had in adk web yesterday was written to a database on your disk, event by event — so the first move when something goes wrong is not to reproduce it, it is to go and read the run that already happened.


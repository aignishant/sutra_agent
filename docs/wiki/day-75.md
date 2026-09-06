# Day 75 - Live API II — the bidi voice loop

IDs closed: ADK-54, ADK-55 · source: `days/day-75-the-bidi-voice-loop/`

## Parts

### 1.1 - A call, not a request
`days/day-75-the-bidi-voice-loop/parts/01-the-open-line/1.1-a-call-not-a-request.md` · level `foundation` · ids ADK-54, ADK-55

A request has one thing happening at a time in a fixed order — you speak, then it speaks — while an open line has two things happening at once and either party may act at any moment, which is not a bigger version of the first program but a different one: the ordering, the cancelling and the ending all stop being the framework's problem and become yours.

### 1.2 - Five methods and a context manager
`days/day-75-the-bidi-voice-loop/parts/01-the-open-line/1.2-five-methods.md` · level `working` · ids ADK-54, ADK-55

A live model, to ADK, is exactly five methods behind a context manager — BaseLlm.connect returns an async context manager that hands you a BaseLlmConnection, and that connection is send_history, send_content, send_realtime, receive and close — so anything that implements those five can be driven by the real runtime, which is the whole reason this day costs nothing while Runner.run_live, LiveRequestQueue and every event stay exactly as they ship.

### 1.3 - Who ends the call
`days/day-75-the-bidi-voice-loop/parts/01-the-open-line/1.3-who-ends-the-call.md` · level `production` · ids ADK-54, ADK-55

The model finishing is not the session ending, and — measured — closing the request queue is not the session ending either: the runtime hangs up on the model, and the async for is still waiting when a 2.0s deadline stops it. What ends a session is the consumer closing the event stream.

### 2.1 - The caller interrupts
`days/day-75-the-bidi-voice-loop/parts/02-talking-over/2.1-the-caller-interrupts.md` · level `working` · ids ADK-54, ADK-55

Being interrupted is not an error the voice loop has to survive — it is the reason the line is held open at all, and mechanically it is one question asked between chunks: did anything arrive while we were talking?

### 2.2 - The one event that says stop
`days/day-75-the-bidi-voice-loop/parts/02-talking-over/2.2-the-event-that-says-stop.md` · level `production` · ids ADK-54, ADK-55

Exactly one thing in the stream says the answer is no longer wanted — an event with interrupted set — and without it the caller sits through 6 of 6 chunks of an answer they already interrupted and then a second one, 12 chunks against 3, with nothing anywhere reporting a problem.

### 2.3 - What the client does with it
`days/day-75-the-bidi-voice-loop/parts/02-talking-over/2.3-what-the-client-does.md` · level `production` · ids ADK-54, ADK-55

Reading the interrupted flag is the easy half; acting on it is three things in this order — stop the player, throw away the audio you have already queued, then render whatever comes next — and only the first is unambiguously code, because the third is a decision about what an abandoned answer contributes to the conversation's transcript and there is no default worth inheriting.

### 3.1 - Audio is bytes, and bytes are seconds
`days/day-75-the-bidi-voice-loop/parts/03-what-goes-down-the-wire/3.1-audio-is-bytes.md` · level `working` · ids ADK-54, ADK-55

A typed question costs what it says; an open microphone costs how long it was open, whether anybody spoke into it or not — measured today, two seconds of silence went down the wire as 64,000 bytes to ask a question that is 20 bytes as text, which is 3,200 times as much for the same question, and that one fact is why the rest of this day is about ending sessions rather than about answering questions.

### 3.2 - Who says the turn ended
`days/day-75-the-bidi-voice-loop/parts/03-what-goes-down-the-wire/3.2-who-says-the-turn-ended.md` · level `production` · ids ADK-54, ADK-55

A request ends when the request ends, but an open microphone does not end — so somebody has to decide that a pause is the end of a sentence rather than a breath, and there are exactly two candidates: the far end inferring it from the sound, or the client saying so out loud with turn markers.

### 4.1 - A connection per caller
`days/day-75-the-bidi-voice-loop/parts/04-what-it-costs/4.1-a-connection-per-caller.md` · level `production` · ids ADK-54, ADK-55

A request/response service's capacity is requests per second — work arriving and leaving. A voice service's capacity is connections held open, which is a completely different quantity with a completely different failure: it does not sag under load, it runs out. Every concurrent caller occupies a connection for the whole call whether they are speaking or not, so the number that matters is concurrent sessions and the lever that matters is how quickly sessions end.

### 4.2 - The session that never ended
`days/day-75-the-bidi-voice-loop/parts/04-what-it-costs/4.2-the-session-that-never-ended.md` · level `production` · ids ADK-54, ADK-55

Part [1.3](../01-the-open-line/1.3-who-ends-the-call.md) showed that a session ends only when the consumer closes the event stream, and part [4.1](4.1-a-connection-per-caller.md) showed that every session occupies a connection while it lives — put those two together and a session nobody closed holds a connection for ever, silently, and the only thing standing between a voice service and that outcome is a deadline you chose, because no event ever arrives saying "this call is over".

### 4.3 - What a real voice system adds
`days/day-75-the-bidi-voice-loop/parts/04-what-it-costs/4.3-what-a-real-voice-system-adds.md` · level `production` · ids ADK-54, ADK-55

The lab drives a real bidirectional session correctly, and the distance between it and something you would let a person speak to is not vague "polish" — it is a list of nine specific things, each one nameable, priceable and arguable, and two of them are deliberately parked because this curriculum will not pay for a model that holds an audio session open.

## Papers - read after the parts

### doi:10.2307/412243 - A simplest systematics for the organization of turn-taking for conversation
`days/day-75-the-bidi-voice-loop/papers/01-turn-taking.md`

Two people manage a conversation with no schedule, no chair and no clock, and they do it with gaps and overlaps so short that the coordination looks like magic — and the paper's answer is that nothing is allocated in advance at all: turns are decided locally, at each point where the current one could end. Switching that off in the demo below turns a six-exchange call from 0 gaps into 3 gaps and 2 overlaps, on identical intentions.


# Day 74 - Live API I — streaming architecture; free-quota check

IDs closed: ADK-52, ADK-53 · source: `days/day-74-live-api-streaming/`

## Parts

### 1.1 - The blank screen
`days/day-74-live-api-streaming/parts/01-the-blank-screen/1.1-the-blank-screen.md` · level `foundation` · ids ADK-52, ADK-53

Streaming changes when the reader is first served and nothing else: the same words are produced at the same rate and the turn ends at the same moment, but the share of the answer that must exist before anything can appear on screen falls from 100% to 13% — which is a claim about the reader's attention, not about the machine's speed.

### 1.2 - One field on RunConfig
`days/day-74-live-api-streaming/parts/01-the-blank-screen/1.2-one-field-on-runconfig.md` · level `foundation` · ids ADK-52, ADK-53

Streaming is not a display setting: the streaming_mode field you put on RunConfig travels all the way down to the model call and becomes the model's stream argument — one expression, stream=run_config.streaming_mode == StreamingMode.SSE — so it changes what the model yields, not how a client draws it, and any design that files it under front-end has put the seam in the wrong place.

### 1.3 - One event or six
`days/day-74-live-api-streaming/parts/01-the-blank-screen/1.3-one-event-or-six.md` · level `working` · ids ADK-52, ADK-53

The same agent, the same question, one field changed: the answer arrives as six things instead of one, five of them flagged partial, so what your code consumes has changed shape and not only its timing.

### 2.1 - The answer, twice
`days/day-74-live-api-streaming/parts/02-the-final-chunk/2.1-the-answer-twice.md` · level `production` · ids ADK-52, ADK-53

The last event of a stream is not the last piece of the answer — it is the whole answer again — so the obvious rule of concatenating every text you were handed produces 180 characters where the answer is 90, with nothing raised, nothing corrupted and nothing out of order.

### 2.2 - Three rules, two of them right
`days/day-74-live-api-streaming/parts/02-the-final-chunk/2.2-three-rules.md` · level `working` · ids ADK-52, ADK-53

Two of the three rules return the answer, and they are not two ways of doing one job — accumulate the partials is the rule for the screen, because it is the only one that has anything to show before the turn ends, and take the final is the rule for storage, because it is the one string the model asserts is its complete answer.

### 2.3 - A partial is not always text
`days/day-74-live-api-streaming/parts/02-the-final-chunk/2.3-not-always-text.md` · level `production` · ids ADK-52, ADK-53

"Streaming" does not mean "text arriving in pieces": every intermediate chunk is flagged partial=True no matter what it carries — text, a function call, raw bytes, or the model's own reasoning — so a consumer written as "append part.text to the screen" is not a streaming consumer at all. It is a text-streaming consumer, and everything that is not text vanishes from it without a sound.

### 3.1 - What SSE actually is
`days/day-74-live-api-streaming/parts/03-the-wire/3.1-what-sse-actually-is.md` · level `working` · ids ADK-52, ADK-53

Server-Sent Events is not a protocol you need a library for — it is one ordinary web response held open, carrying lines of the shape field: value, where a blank line ends a message and a line whose field name you do not recognise is ignored; that is small enough to write and read back in forty lines of Python, which is exactly why it is worth writing them.

### 3.2 - The newline in your payload
`days/day-74-live-api-streaming/parts/03-the-wire/3.2-the-newline-in-your-payload.md` · level `production` · ids ADK-52, ADK-53

The encoder everybody writes first — one data: line per chunk, built with a single f-string — is correct for every payload that happens not to contain a newline, and silently loses everything after the first newline in one that does: 90 characters sent, 77 received, 13 gone, exit code 1, and not one error anywhere.

### 3.3 - What sits in between
`days/day-74-live-api-streaming/parts/03-the-wire/3.3-what-sits-in-between.md` · level `production` · ids ADK-52, ADK-53

Your process writes chunks and the reader's screen shows chunks, and between those two things sit several pieces of software you did not write — each of which is entitled to hold your bytes until it has enough of them — so a stream can be quietly re-assembled into one response with no error anywhere and nothing changed on your side, which makes this the hardest streaming bug there is: the code is correct, the tests are green, and the feature does not work in one environment.

### 4.1 - What a live session is made of
`days/day-74-live-api-streaming/parts/04-the-bill-for-voice/4.1-what-a-live-session-is-made-of.md` · level `working` · ids ADK-52, ADK-53

BIDI is not a third setting of the streaming dial — it is a different shape of program: run_async takes one message and hands you back events, while run_live takes no message at all and requires a live_request_queue you keep pushing into while events come back the other way — and the clearest statement of what that feature is comes from counting the RunConfig fields that exist only for it, which on the installed google-adk==2.7.1 is eleven, every one of them naming an audio or session-control concern that a request-and-reply turn simply does not have.

### 4.2 - The free-quota check
`days/day-74-live-api-streaming/parts/04-the-bill-for-voice/4.2-the-free-quota-check.md` · level `production` · ids ADK-52, ADK-53

A free-quota check has three possible outcomes rather than two — free, not free, and could not determine — and this one returned all three at once: text streaming is free, because the lab measured that a streamed turn costs the same one model request as an unstreamed one; bidirectional voice is 🅿️ parked, because it needs something this curriculum will not pay for; and whether the Live API is on a free tier at all is recorded as unverified, because the pages that would answer it do not put the answer in anything a script can read — and writing that third line down honestly is worth more than a confident guess at the first.

### 5.1 - The reader who leaves
`days/day-74-live-api-streaming/parts/05-in-production/5.1-the-reader-who-leaves.md` · level `production` · ids ADK-52, ADK-53

Streaming hands the reader a connection they control, so they can hang up half-way — and when they do, the run is cancelled and the session ends up holding one event, their question, with no assistant turn at all: the reader saw two chunks of an answer that, as far as the conversation's history knows, was never given.

### 5.2 - What a real streaming system adds
`days/day-74-live-api-streaming/parts/05-in-production/5.2-what-a-real-streaming-system-adds.md` · level `production` · ids ADK-52, ADK-53

The lab streams correctly, and the distance between it and something you would put in front of users is not vague "hardening" — it is a list of nine specific things, each one cheap on the day the feature is written and expensive on the day it is needed, and several of them are deliberately parked by this curriculum rather than forgotten.

## Papers - read after the parts

### doi:10.1145/1476589.1476628 - Response time in man-computer conversational transactions
`days/day-74-live-api-streaming/papers/01-response-time.md`

The reason to build any of this day's machinery is a claim from 1968: response time does not make an interaction better or worse by degrees — it changes what kind of interaction it is, at thresholds — and the demo below shows streaming moving 3 of 4 answers back inside the conversational band while the total time to produce them is identical at 25.20s.


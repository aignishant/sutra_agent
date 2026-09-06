# Day 66 - Threat model — prompt injection & the lethal trifecta

IDs closed: SEC-06, SEC-07 · source: `days/day-66-injection-threat-model/`

## Parts

### 1.1 - The note taped to the parcel
`days/day-66-injection-threat-model/parts/01-one-stream/1.1-the-note-taped-to-the-parcel.md` · level `foundation` · ids SEC-06

A language model receives your instructions and a stranger's text as one flat stream of characters, with nothing in it that says which is which — and in the desk's own prompt, measured today, 73.4% of those characters were written by strangers.

### 1.2 - The fix the database got
`days/day-66-injection-threat-model/parts/01-one-stream/1.2-the-fix-the-database-got.md` · level `foundation` · ids SEC-06

SQL injection was solved by giving the database two separate inputs — a query with holes in it, and the values that fill the holes — and no equivalent second input exists for a language model, so the same fix cannot be copied across.

### 1.3 - The sentence you did not write
`days/day-66-injection-threat-model/parts/01-one-stream/1.3-the-sentence-you-did-not-write.md` · level `foundation` · ids SEC-06

Prompt injection is any text that reaches the model's input and changes what the system does, written by someone who was only supposed to be supplying data — and the definition deliberately says nothing about how the sentence is phrased.

### 2.1 - Typed at the counter
`days/day-66-injection-threat-model/parts/02-how-it-arrives/2.1-typed-at-the-counter.md` · level `foundation` · ids SEC-06

Direct injection is the user of the system trying to steer it themselves, and it is the least dangerous kind — because the person doing it already has whatever access the system gives them.

### 2.2 - Arriving in somebody else's post
`days/day-66-injection-threat-model/parts/02-how-it-arrives/2.2-arriving-in-somebody-elses-post.md` · level `working` · ids SEC-06

Indirect injection is hostile text that arrives inside data the system fetched on its own initiative — so the attacker never speaks to your system, never authenticates, and does not need to know you exist when they write it.

### 2.3 - The recipe folder in the staff kitchen
`days/day-66-injection-threat-model/parts/02-how-it-arrives/2.3-the-recipe-folder-in-the-staff-kitchen.md` · level `working` · ids SEC-06

Sutra has six places where somebody else's text enters the desk's context and four of them feed the retrieval index — and the door that reaches the prompt most reliably is not the one an outsider uses, it is the one an insider does.

### 2.4 - The camera that recorded everything
`days/day-66-injection-threat-model/parts/02-how-it-arrives/2.4-the-camera-that-recorded-everything.md` · level `working` · ids SEC-06

The honest experiment is not "would a model obey this?" — that is a question about somebody else's model — it is "if it did, would anything of ours stop it or say so?", and the measured answer for the desk is one private value out, zero warnings.

### 3.1 - Written Monday, read Thursday
`days/day-66-injection-threat-model/parts/03-the-slow-fuse/3.1-written-monday-read-thursday.md` · level `production` · ids SEC-06

An injection that survives into memory stops being an event and becomes a standing rule: the desk wrote it down on one ticket and retrieved it later for a different question, on a different customer, for an agent who never saw where it came from.

### 3.2 - The half that is harmless alone
`days/day-66-injection-threat-model/parts/03-the-slow-fuse/3.2-the-half-that-is-harmless-alone.md` · level `production` · ids SEC-06

Retrieval assembles the prompt from several documents at once, so a payload can be split across two of them — and a check that reads one document at a time is looking at a place where the instruction does not exist.

### 4.1 - The three things that must not meet
`days/day-66-injection-threat-model/parts/04-three-legs/4.1-the-three-things-that-must-not-meet.md` · level `foundation` · ids SEC-07

An agent becomes dangerous only when it holds all three of private data, exposure to untrusted content, and a way to communicate outward — any two of them is a system with a bad day available to it, and all three is a system a stranger can operate.

### 4.2 - Nobody here holds all three
`days/day-66-injection-threat-model/parts/04-three-legs/4.2-nobody-here-holds-all-three.md` · level `working` · ids SEC-07

Reviewing Day 58's triage graph one stage at a time gives a clean result — zero of five stages hold all three legs — and that clean result is produced by asking the question in the wrong unit.

### 4.3 - The line that passes it along
`days/day-66-injection-threat-model/parts/04-three-legs/4.3-the-line-that-passes-it-along.md` · level `production` · ids SEC-07

Ask the same question along the path instead of per stage and the answer inverts: the trifecta is complete at review — no single stage holds it and the pipeline does, because the text carries the exposure forward even though the capabilities stay put.

### 4.4 - Closing the tap nearest the outlet
`days/day-66-injection-threat-model/parts/04-three-legs/4.4-closing-the-tap-nearest-the-outlet.md` · level `production` · ids SEC-07

Two interventions look equally sensible and only one works: removing the outward leg closes the trifecta everywhere, while cutting the flow at a convenient middle stage changes nothing — because the stage downstream reads the untrusted sources directly anyway.

### 5.1 - The stocktake
`days/day-66-injection-threat-model/parts/05-what-it-asks-for/5.1-the-stocktake.md` · level `foundation` · ids SEC-07

An injection asks for one of five things — exfiltrate, escalate, mislead, destroy, spend — and they are worth separating because each one needs a different leg of the trifecta and each one is noticed by a different person.

### 5.2 - The meter somebody else is feeding
`days/day-66-injection-threat-model/parts/05-what-it-asks-for/5.2-the-meter-somebody-else-is-feeding.md` · level `production` · ids SEC-07

One sentence in one ticket turns Day 57's bounded writer-and-critic loop into a quota drain that costs the attacker nothing and costs the desk twenty extra requests against a twenty-request day — and because it needs only the untrusted leg, it survives every fix in section 4.

### 6.1 - The address inside the picture
`days/day-66-injection-threat-model/parts/06-the-way-out/6.1-the-address-inside-the-picture.md` · level `working` · ids SEC-07

There are five ways for a byte to leave this desk and four of them do not look like network calls — and the one that hides best is a picture, which is why the defence everybody reaches for first, a list of forbidden phrases, catches 3 of 12 hostile spellings and, when widened after an incident, refuses 4 of 5 honest customers.

### 6.2 - Read back for confirmation
`days/day-66-injection-threat-model/parts/06-the-way-out/6.2-read-back-for-confirmation.md` · level `working` · ids SEC-07

The reply itself is an exfiltration channel and it is the one nobody counts, because the attacker opened the ticket: the answer goes back to them by design, through the one capability the desk cannot give up, with no tool call, no request and nothing unusual anywhere in the trace.

### 6.3 - The note inside the back cover
`days/day-66-injection-threat-model/parts/06-the-way-out/6.3-the-note-inside-the-back-cover.md` · level `production` · ids SEC-07

Writing to memory is a way out: the desk stores a line, a later question retrieves it, and the delivery is performed weeks afterwards by the system's own retrieval — measured here as a planted row coming back top of three, at 0.491, to a question that had nothing to do with the ticket it was written on.

### 6.4 - The receipt that printed too much
`days/day-66-injection-threat-model/parts/06-the-way-out/6.4-the-receipt-that-printed-too-much.md` · level `production` · ids SEC-07

An error message is an exfiltration channel, and it is the one that escapes every control on this day's list — because it is produced by the failure path rather than the answer path, and no tool is registered for it, so an allowlist of tools has nothing to say about it.

### 7.1 - What is worth taking
`days/day-66-injection-threat-model/parts/07-writing-it-down/7.1-what-is-worth-taking.md` · level `foundation` · ids SEC-06, SEC-07

A threat model starts by naming, in plain words, what you are protecting and where a stranger's words get in — five of each here — and the row that changes people's minds is the second asset: the archive as a whole, because bulk access is worth more than any single one of its rows.

### 7.2 - The document that writes itself
`days/day-66-injection-threat-model/parts/07-writing-it-down/7.2-the-document-that-writes-itself.md` · level `working` · ids SEC-06, SEC-07

A threat model typed by hand describes the system as it was on the day somebody typed it, so this one is generated from the same declarations legs.py and channels.py measure against — change the wiring and the document changes with it, and gate.py goes red when the two stop agreeing.

### 7.3 - Accept, mitigate, refuse
`days/day-66-injection-threat-model/parts/07-writing-it-down/7.3-accept-mitigate-refuse.md` · level `production` · ids SEC-06, SEC-07

Every risk gets exactly one of three verdicts, and the verdict is the only part of a threat model that does any work: an accept row must record the conditions it was accepted under, a mitigate row must name an owner or it is a wish, and a refuse row gives up a capability while giving it up is still cheap.

## Papers - read after the parts

### arXiv:2302.12173 - Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection
`days/day-66-injection-threat-model/papers/01-indirect-prompt-injection.md`

Before this document, "prompt injection" meant a user typing something clever into a chat box, so the defences went at the user's input — and this paper's contribution was to point out that the user is not the only person writing into the prompt: anything the application retrieves is written by somebody, and that somebody never has to speak to your system at all.


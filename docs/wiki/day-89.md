# Day 89 - A2A v1.0 — the signed Agent Card

IDs closed: ADK-70, AG-34 · source: `days/day-89-signed-agent-cards/`

## Parts

### 1.1 - The card is the interface
`days/day-89-signed-agent-cards/parts/01-the-card/1.1-the-card-is-the-interface.md` · level `foundation` · ids ADK-70

An A2A Agent Card is the document another agent reads before it decides to talk to you — ADK builds one from your agent object for nothing, filling eight of the protocol's fourteen fields, and the field it never fills is signatures.

### 1.2 - Where the card lives
`days/day-89-signed-agent-cards/parts/01-the-card/1.2-where-the-card-lives.md` · level `working` · ids ADK-70

The card is served at one path every A2A client already knows — /.well-known/agent-card.json — and 💥 the Starlette app ADK hands you has no routes at all until its lifespan runs, so a test that uses the app directly gets a 404 for the card and every other path.

### 1.3 - What the card gives away
`days/day-89-signed-agent-cards/parts/01-the-card/1.3-what-the-card-gives-away.md` · level `working` · ids AG-34

ADK turns every tool into a published skill, so the card served at a well-known path with no credential lists all three of this desk's tool names and their docstrings verbatim — an inventory of every lever the agent has, written in the words you wrote for the model.

### 2.1 - A signature is over bytes
`days/day-89-signed-agent-cards/parts/02-signing-it/2.1-a-signature-is-over-bytes.md` · level `working` · ids AG-34

You cannot sign an object, only a byte string, so before any cryptography happens both sides must agree on exactly one way to write the card down — sorted keys and no spaces gives the same 952 bytes whatever order the card was built in, and indent=2 gives two different digests for the same card.

### 2.2 - Signing the card
`days/day-89-signed-agent-cards/parts/02-signing-it/2.2-signing-the-card.md` · level `working` · ids AG-34

The specification says an AgentCardSignature is a JWS in JSON form, and it has exactly three fields — protected, signature, header — so signing a card is: build a protected header, join it to the card's canonical bytes with a dot, sign that, and base64url everything.

### 2.3 - The card that was edited
`days/day-89-signed-agent-cards/parts/02-signing-it/2.3-the-card-that-was-edited.md` · level `working` · ids AG-34

Change one character of the advertised url after signing — 127.0.0.1 to 127.0.0.9 — and the card is still 952 bytes, still valid JSON, still carries a real signature made by a real key, and verification raises InvalidSignature, which is the entire value of the exercise.

### 3.1 - The algorithm the card chose
`days/day-89-signed-agent-cards/parts/03-the-verifier-decides/3.1-the-algorithm-the-card-chose.md` · level `production` · ids AG-34

💥 A verifier that reads alg out of the card and does what it says will accept alg: "none" with an empty signature — measured here, a forged card advertising http://attacker.example/ verified True — and the fix is not better cryptography but an allowlist the card cannot widen.

### 3.2 - Which key
`days/day-89-signed-agent-cards/parts/03-the-verifier-decides/3.2-which-key.md` · level `production` · ids AG-34

A signature verifies against a key, so the only question that matters is where that key came from — and when the card names a kid the verifier has never seen, the honest report is not "invalid" but "this proves somebody held a key", which is not identity.

### 3.3 - The field the spec made optional
`days/day-89-signed-agent-cards/parts/03-the-verifier-decides/3.3-the-field-the-spec-made-optional.md` · level `production` · ids AG-34

The specification lists signatures as Required: No, so a card with none is fully conformant — which means "does this card verify?" and "is this card valid?" are different questions, and only one of them has an answer the protocol will give you.

### 4.1 - A peer can send you work
`days/day-89-signed-agent-cards/parts/04-the-peer/4.1-a-peer-can-send-you-work.md` · level `production` · ids ADK-70

to_a2a turns the desk into a server in one call, and the two routes it mounts are not symmetrical: /.well-known/agent-card.json hands out a description, and / accepts instructions from whoever reached it — so verifying a peer's card protects you from talking to the wrong agent, and nothing about it protects you from the wrong agent talking to you.

### 4.2 - 🅿️ The map you are not building today
`days/day-89-signed-agent-cards/parts/04-the-peer/4.2-the-map-you-are-not-building-today.md` · level `production` · ids AG-34

🅿️ Beside A2A sit a payments protocol built on signed mandates and two payment-rail proposals, and this day's discipline is to be able to place them on a map and say why none of them is in this repository: each one needs money to move, and Sutra's budget is denominated in requests.

### 5.1 - What verification costs
`days/day-89-signed-agent-cards/parts/05-in-production/5.1-what-verification-costs.md` · level `production` · ids AG-34

Signing and verifying an agent card is arithmetic over a thousand bytes and costs nothing measurable and no provider requests at all — the entire cost of card verification is key distribution, which is a process with people in it, and that is why teams that skip verification did not skip it to save time.

### 5.2 - What a real A2A deployment adds
`days/day-89-signed-agent-cards/parts/05-in-production/5.2-what-a-real-a2a-deployment-adds.md` · level `production` · ids ADK-70

The lab signs a real card with a real key and verifies it against a key set the card cannot influence — and the distance between that and something you would expose to a stranger is nine items, the first of which is authentication on the endpoint and is the only one that is urgent.

## Papers - read after the parts

### doi:10.17487/RFC7515 - A signature over its own header
`days/day-89-signed-agent-cards/papers/01-a-signature-over-its-own-header.md`

Signing the payload alone is the obvious design and it leaves every parameter describing the signature — which algorithm, which key — outside it; JWS puts the header inside the signing input, and the measured difference is four out of four header edits caught instead of four out of four surviving.


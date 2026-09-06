# Day 91 - Integrations survey — Slack-shaped intake

IDs closed: AG-30, ADK-72 · source: `days/day-91-slack-shaped-intake/`

## Parts

### 1.1 - An integration is somebody else's shape
`days/day-91-slack-shaped-intake/parts/01-what-an-integration-is/1.1-somebody-elses-shape.md` · level `foundation` · ids AG-30

Every integration is a decision that somebody else owns and can change without telling you, so the job is never "connect to the vendor" — it is to put that decision in exactly one place, and the measurement of whether you did is how many files a rename touches.

### 1.2 - The ways in, and what each one costs
`days/day-91-slack-shaped-intake/parts/01-what-an-integration-is/1.2-the-ways-in.md` · level `foundation` · ids AG-30

Ten ways something outside this repository could reach the desk, and the useful column is not "how hard is it to build" but what it can see and what it can do — because four of the ten are already built, two need an account, and four need a billing account and are therefore parked.

### 1.3 - A survey that can go red
`days/day-91-slack-shaped-intake/parts/01-what-an-integration-is/1.3-a-survey-that-can-go-red.md` · level `working` · ids AG-30

A survey is a set of claims, so every row that says built has to name a path and the check is that the path exists — which turns a document that quietly ages into one that fails a build, and takes five lines to write.

### 2.1 - The three things a vendor sends
`days/day-91-slack-shaped-intake/parts/02-verifying-it/2.1-what-a-vendor-sends.md` · level `working` · ids ADK-72

A chat intake receives exactly three kinds of thing — a one-time handshake proving you control the URL, ordinary events, and retries of events you did not acknowledge — and the endpoint has to answer all three correctly before any of it reaches an agent.

### 2.2 - The string that gets signed
`days/day-91-slack-shaped-intake/parts/02-verifying-it/2.2-the-string-that-gets-signed.md` · level `working` · ids ADK-72

The signature is an HMAC-SHA256 over one exact string — a version marker, the timestamp and the raw body, joined by colons — and every part of that sentence is load-bearing, because the same three values assembled any other way produce a digest that is correct and useless.

### 2.3 - Checked against the vendor, not against a belief
`days/day-91-slack-shaped-intake/parts/02-verifying-it/2.3-checked-against-the-vendor.md` · level `working` · ids ADK-72

A verifier you wrote and a signer you wrote will always agree with each other, whatever they both get wrong — so the only test worth anything is against the vendor's own published example, and this one reproduces its digest to all sixty-four characters.

### 2.4 - The bytes that arrived, not the object they became
`days/day-91-slack-shaped-intake/parts/02-verifying-it/2.4-the-bytes-that-arrived.md` · level `working` · ids ADK-72

A signature covers bytes, and parsing JSON and re-serialising it produces different bytes carrying identical meaning — so a verifier that hashes json.dumps(json.loads(body)) refuses every genuine request, and the fix is to read the body once, as bytes, before anything else touches it.

### 3.1 - The signature that never expires
`days/day-91-slack-shaped-intake/parts/03-three-ways-it-goes-wrong/3.1-the-signature-that-never-expires.md` · level `working` · ids ADK-72

A valid signature stays valid for ever, so anyone who ever saw one genuine request can send it again whenever they like — and the only thing standing between that and a duplicated refund is a check on the timestamp, which costs one comparison and is the guard people skip.

### 3.2 - The comparison you cannot benchmark
`days/day-91-slack-shaped-intake/parts/03-three-ways-it-goes-wrong/3.2-the-comparison-you-cannot-benchmark.md` · level `production` · ids ADK-72

Comparing digests with == can leak where the comparison stopped, so the guard is hmac.compare_digest — and this machine cannot measure the difference at all, which is the honest and more useful finding: the guard is adopted on documented grounds, because a benchmark here produces noise with a sign that changes between runs.

### 3.3 - Signed is not safe
`days/day-91-slack-shaped-intake/parts/03-three-ways-it-goes-wrong/3.3-signed-is-not-safe.md` · level `production` · ids AG-30

The signature establishes that a real member of the workspace sent this, and that is the whole of what it establishes — so a message telling the desk to refund every open ticket without approval arrives with a perfect signature, and treating verification as permission is how a correct security check becomes the thing that let the attack in.

### 4.1 - What a forged request reaches
`days/day-91-slack-shaped-intake/parts/04-blast-radius/4.1-what-a-forged-request-reaches.md` · level `production` · ids AG-30

Principle 13 asks what a new capability can reach before asking whether it works, and the honest answer for this endpoint is: whatever the desk can do, because a message that passes the checks is handed to an agent with the desk's tools — so the containment has to be on the far side of the handler, not in it.

### 4.2 - The secret itself
`days/day-91-slack-shaped-intake/parts/04-blast-radius/4.2-the-secret-itself.md` · level `production` · ids ADK-72

The signing secret is the only thing separating this endpoint from anyone on the internet, and the lab holds it in a tracked file on purpose — because it is the vendor's own documentation example, which is a distinction that has to be deliberate rather than lucky.

### 5.1 - Which one to build first
`days/day-91-slack-shaped-intake/parts/05-in-production/5.1-which-one-to-build-first.md` · level `production` · ids AG-30

The survey's ten rows sort three ways — by effort, by what they can see, and by whether anybody would use them — and the three orders disagree, so the useful answer is to build the narrowest channel somebody is already asking for, which here is the one this day built.

### 5.2 - What a real integration layer adds
`days/day-91-slack-shaped-intake/parts/05-in-production/5.2-what-a-real-integration-layer-adds.md` · level `production` · ids ADK-72

The lab verifies a signature correctly, refuses replays, keeps the raw bytes and separates authenticity from safety — and the distance between that and something a team can point at a workspace is nine items, three of which take an afternoon between them and one of which is not code.

## Papers - read after the parts

### doi:10.1145/361598.361623 - The module that owns the vendor
`days/day-91-slack-shaped-intake/papers/01-the-module-that-owns-the-vendor.md`

The question "what are the modules?" has an answer that is not the sequence of things that happen, and the difference shows up as a number: when a vendor renames four fields, the flowchart decomposition needs four modules edited and the decision-hiding one needs one.


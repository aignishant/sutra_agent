---
day: 89
phase: 14
phase_name: "Interop & launch"
title: "A2A v1.0 — the signed Agent Card"
ids: ["AG-34", "ADK-70"]
principles: [4, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 13
generated: "2026-09-07"
status: written
lab_scaffolded: true
commit: ""
---

# Day 89 — A2A v1.0: the signed Agent Card

> **Yesterday (Day 88):** the MCP server became a topology decision. In one Pod it has no
> cluster-visible address at all, and the startup race that pattern ships with was reproduced for
> real on loopback as `ConnectionRefusedError: [WinError 10061]`. Nothing ran on a cluster, because
> kubectl, kind and docker are all absent from this machine.
> **Today:** Phase 14 opens and the desk stops being something you deploy and starts being something
> a stranger can find. A2A's Agent Card is the document a peer reads before it decides to talk to
> you; ADK builds one from the agent object for free, fills **eight of the protocol's fourteen
> fields**, and leaves `signatures` empty. So the day's work is the half the framework correctly
> refuses to do: canonical bytes, a real Ed25519 signature, and a verifier that decides for itself
> which algorithms and which keys it will accept. The sharpest finding is what happens when it does
> not — a forged card advertising `http://attacker.example/` with a **zero-character signature**
> verified `True`.
> **Tomorrow (Day 90):** agent identity and the registry — where the keys come from, which is the
> half of trust a signature cannot supply.

---

## §1 Where we are

The board outside a workshop.

Painted on a sheet of tin: *Lathe work. Welding. Radiator repair.* A driver with a cracked radiator
reads it from across the road and decides, without asking anybody, that this is the right place. The
board is not the workshop — it is a set of claims about the workshop, and everything that happens
next starts from a stranger deciding to believe it.

Nobody signs a tin board, because it is bolted to the building it describes and you can see both at
once. That is exactly the property a network does not have.

Phase 13 made Sutra observable and deployable. Phase 14 makes it *reachable by parties nobody in this
repository wrote*, and the gate is **"A2A peer verified; repo public"**. Today is the first word of
that.

The protocol's discovery document is the **Agent Card**, served at a path fixed by convention —
`/.well-known/agent-card.json` — so no negotiation is needed and anyone who knows the host can fetch
it. ADK will build that card for you in one call, at zero cost, by reading the agent object rather
than the model. It fills eight of fourteen fields.

Three of the six it leaves empty are ordinary gaps. One is not. `signatures` is field 13 of the
schema, it has been there since the schema was designed, and it is what turns a set of claims into a
set of claims somebody is standing behind. ADK cannot fill it, correctly — signing needs a private
key, and a framework that asked for yours would be a framework asking for your identity.

So this day is the other half, built by hand and verified hands-on: pin the bytes, sign them, verify
them, then break it four ways on purpose. Along the way the card turns out to publish **three tool
names and three tool docstrings verbatim** on a path that asks for no credential, and the Starlette
app ADK hands you has **no routes at all** until its lifespan runs.

---

## §2 The map

Five sections. Section 1 is the card as a document. Section 2 is signing it. Section 3 is the three
decisions a verifier must make for itself. Section 4 is the other direction — a peer that can send
*you* work — and the map of what this day is not building. Section 5 is the bill and the list.

### 1 — The card

*What a peer reads, where it reads it, and what it learns.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The card is the interface](parts/01-the-card/1.1-the-card-is-the-interface.md) | Eight of fourteen fields, and the one that stays empty | `foundation` |
| 1.2 | [Where the card lives](parts/01-the-card/1.2-where-the-card-lives.md) | 💥 The well-known path, and an app with an empty route table | `working` |
| 1.3 | [What the card gives away](parts/01-the-card/1.3-what-the-card-gives-away.md) | Three tool names and three docstrings, unauthenticated | `working` |

### 2 — Signing it

*Bytes first, then cryptography.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [A signature is over bytes](parts/02-signing-it/2.1-a-signature-is-over-bytes.md) | Why 952 bytes and not 1,315, and why two digests for one card | `working` |
| 2.2 | [Signing the card](parts/02-signing-it/2.2-signing-the-card.md) | The three fields of an `AgentCardSignature`, and the signing input | `working` |
| 2.3 | [The card that was edited](parts/02-signing-it/2.3-the-card-that-was-edited.md) | One character, same length, `InvalidSignature` | `working` |

### 3 — The verifier decides

*Three decisions the document must not make for you.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The algorithm the card chose](parts/03-the-verifier-decides/3.1-the-algorithm-the-card-chose.md) | 💥 `alg: none`, an empty signature, and `verified: True` | `production` |
| 3.2 | [Which key](parts/03-the-verifier-decides/3.2-which-key.md) | Where a key set comes from, and what rotation costs | `production` |
| 3.3 | [The field the spec made optional](parts/03-the-verifier-decides/3.3-the-field-the-spec-made-optional.md) | Conformant and unsigned are the same thing; three outcomes, not two | `production` |

### 4 — The peer

*The other direction, and the roads this day is not taking.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [A peer can send you work](parts/04-the-peer/4.1-a-peer-can-send-you-work.md) | Two routes, one of which executes the agent | `production` |
| 4.2 | [🅿️ The map you are not building today](parts/04-the-peer/4.2-the-map-you-are-not-building-today.md) | AP2 mandates, x402, TAP — parked, with the lookups written out | `production` |

### 5 — In production

*What it costs, and what is still missing.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [What verification costs](parts/05-in-production/5.1-what-verification-costs.md) | Free compute, free bytes, and a bill denominated in coordination | `production` |
| 5.2 | [What a real A2A deployment adds](parts/05-in-production/5.2-what-a-real-a2a-deployment-adds.md) | Nine items, one of them urgent today | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [A signature over its own header](papers/01-a-signature-over-its-own-header.md) | `doi:10.17487/RFC7515` — the signing input covers the protected header, which is the decision the A2A specification points at by name. The demo catches four of four header edits; the ablation removes one branch and all four survive with the payload untouched |

---

## §3 Setup — run this

```bash
mkdir -p days/day-89-signed-agent-cards/lab/papers/jws
cd days/day-89-signed-agent-cards/lab
touch _desk.py card.py served.py exposed.py canon.py sign.py alg.py kid.py gate.py
touch papers/jws/jws.py papers/jws/demo.py
```

**One package was added today**, and it is the only one this day needs:

```bash
uv add "a2a-sdk==1.1.2"
```

**Why:**

- Before it, `from google.adk.a2a.utils.agent_card_builder import AgentCardBuilder` raises
  `ModuleNotFoundError: No module named 'a2a'`. ADK ships the **integration** and not the protocol
  library, so `google.adk.a2a` imports as a package path and every module inside it fails.
- The version was read live from `pypi.org/pypi/a2a-sdk/json` before pinning, never copied from a
  sample (Principle 7), and it has a dated row in `docs/PACKAGES.md`.
- Installed **without** the `all` extra, which would add a database layer this repository does not
  use.

Everything else this day needs is already present: `cryptography==50.0.0` for signing, and
`httpx==0.28.1` for driving the ASGI app in-process.

**What each file is for:**

- `_desk.py` is the file to read first: the desk as an ADK agent, the card builder, the canonical byte
  rule, and a signing key generated fresh on every import and never written to disk.
- `card.py` shows the card a peer would fetch and the schema table behind it.
- `served.py` is the well-known path and the empty-route-table trap.
- `exposed.py` is what publishing the card tells a stranger.
- `canon.py`, `sign.py`, `alg.py`, `kid.py` are the four decisions: which bytes, which signature,
  which algorithm, which key.
- `gate.py` is the day's eval against `sutra/a2a.py`.
- `papers/jws/` holds the paper's demo: `jws.py` is the signing input and nothing else.

The lab is gitignored repo-wide. Confirm it before generating any key material:

```bash
git check-ignore -v days/day-89-signed-agent-cards/lab/_desk.py
```

**Why:**

- `days/*/lab/` is the rule for the learner's own code (Principle 9). The keys here are ephemeral by
  construction, and a lab that wrote one to disk in a tracked directory would be teaching the
  opposite of the day.

---

## §4 Build brief

The teaching is in `parts/`, the measurements are in `lab/`, and what is left is the piece that
belongs in the product.

**`sutra/a2a.py`** — the desk's side of the protocol, as code the server and the client both import.

- `TODO(me)`: `sign_card(card, key, kid)` returning an `AgentCardSignature` over the canonical bytes.
  Part 2.1 pins the serialisation; part 2.2 gives the four steps. Sign in the build, never in the
  request path — part 5.2 item 3 is why.
- `TODO(me)`: `verify_card(card, entry, *, accepted, keys)` with **no defaults** on the last two.
  Part 3.1's review comment is the acceptance test: `accepted=None` must not be typeable.
- `TODO(me)`: `accepted_algs()` as its own function, returning a tuple the card cannot widen, read
  from reviewed configuration rather than from a caller's argument.
- `TODO(me)`: `trusted_keys()` loading the key set from somewhere the card cannot influence, holding
  the current key **and** the recently retired ones. Part 3.2's rotation arm is the test.
- `TODO(me)`: `card_for_peers()` — the published card with the tool inventory withheld. Part 1.3
  measured three names and three docstrings going out unauthenticated; part 5.2 item 7 is the shape
  of the fix.
- `TODO(me)`: `refuse(reason)` returning **three** distinct outcomes — verified, failed, unsigned —
  as separate countable results. Part 3.3 is why merging the last two loses what an operator needs.

**`tests/test_a2a.py`**

- `TODO(me)`: a test that an `alg: none` entry is refused **before** any cryptography runs. Assert on
  the exception type, not just the falsiness.
- `TODO(me)`: a test that a card whose `kid` is unknown is refused and that nothing in the code path
  fetches a key.
- `TODO(me)`: a test that one changed character of `supportedInterfaces[0].url` fails verification.
- `TODO(me)`: a test that runs the ASGI app **through its lifespan** — part 1.2 measured an empty
  route table, so a test that skips it asserts against an app with no routes.

**Two `TODO(me)`s that are not code:**

- **Authentication on the JSON-RPC route**, before this is reachable from anything but a laptop. Part
  5.2 item 1, and the only urgent item on that list: two routes, one of which executes the agent with
  your tools and your free-tier allowance behind it.
- **Decide where the public keys live**, and write it down. That is Day 90, and part 5.1's finding is
  that it is the entire cost of verification — the cryptography is free.

---

## §5 The eval that must be able to fail

```bash
cd days/day-89-signed-agent-cards/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/a2a.py`, all red today because the module is the build brief. A check that
cannot run counts as a **failure**, never as skipped (Principle 11).

Every measurement in this day encodes its verdict in an exit code, and each has an arm that goes red:

```bash
uv run python card.py; echo "exit: $?"               # 1 — signatures: 0, on a conformant card
uv run python card.py --fields; echo "exit: $?"      # 1 — eight of fourteen fields filled
uv run python served.py; echo "exit: $?"             # 1 — 404, because the route table is empty
uv run python served.py --lifespan; echo "exit: $?"  # 0 — two routes, and the card
uv run python exposed.py; echo "exit: $?"            # 1 — three tool names, three docstrings
uv run python exposed.py --minimal; echo "exit: $?"  # 0 — the desk described without its levers
uv run python canon.py; echo "exit: $?"              # 0 — one card, one digest
uv run python canon.py --pretty; echo "exit: $?"     # 1 — one card, two digests
uv run python sign.py; echo "exit: $?"               # 0 — the signature verifies
uv run python sign.py --tamper; echo "exit: $?"      # 1 — InvalidSignature, one character apart
uv run python alg.py; echo "exit: $?"                # 1 — a forgery accepted
uv run python alg.py --strict; echo "exit: $?"       # 0 — refused before any cryptography
uv run python kid.py; echo "exit: $?"                # 0 — verified against a key trusted in advance
uv run python kid.py --rotate; echo "exit: $?"       # 1 — an unknown kid, refused
```

Note the pair that matters most. **`alg.py` exits 1 when the forgery is accepted and 0 when it is
refused**, which is the right way round for a check and the opposite of what the naive verifier
reports about itself. The permissive arm prints `verified: True` and is the failure.

The paper's demo does the same for its own claim: `demo.py` exits `0` having caught four of four
header edits, and `demo.py --off` exits `1` having let all four through with the payload untouched.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-07 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

This is the first day in some time with no allowance question in it at all, and that is a property of
the subject rather than a compromise. Signing and verifying are arithmetic over about a kilobyte;
part 5.1 puts numbers on it. The `LlmAgent` in `_desk.py` is constructed and read — its model string
is copied into the card as text and never dialled — and every HTTP request in the day is served
in-process by `httpx.ASGITransport`, so nothing binds a port either.

What is genuinely real here: ADK's own `AgentCardBuilder` and `to_a2a`, the `a2a-sdk` protobuf schema
and its constants, and `cryptography`'s Ed25519. Nothing is simulated except the peer, and the peer is
this repository's own agent talking to itself.

---

## §7 Traps

1. **Expecting ADK to sign the card.** It builds eight of fourteen fields and leaves `signatures`
   empty, correctly — signing needs a key it must not ask you for — part 1.1.
2. **Using the ASGI app without its lifespan.** `to_a2a` returns an application with **no routes**;
   they are added at startup, so a test client gets 404 for every path — part 1.2.
3. **Publishing the tool inventory by accident.** One skill per tool, with the docstring verbatim, on
   a path that asks for no credential — part 1.3.
4. **Signing an object.** You can only sign bytes; without one agreed serialisation, the same card
   gives two digests and verification fails for a formatting reason — part 2.1.
5. **Encoding the protected header twice.** The signing input takes it as the already-encoded string;
   re-encoding it produces a signature no other implementation can check — part 2.2.
6. **Catching `Exception` around verification.** `InvalidSignature` means forged-or-wrong-key; a
   malformed base64 payload is a different failure and must not be reported as an attack — part 2.3.
7. **Letting the card choose the algorithm.** `alg: none` with an empty signature verifies `True`
   against a verifier that believes the header — part 3.1.
8. **A default that means "accept anything".** `accepted=None` is a bypass reachable by forgetting an
   argument — part 3.1.
9. **Letting the card supply its key.** A `jku` fetch makes every unknown-`kid` ticket disappear and
   reduces verification to proving the author owns a keypair — part 3.2.
10. **Merging "failed" and "unsigned".** One is an incident and the other is a fact about who you talk
    to; the specification marks `signatures` **Required: No** — part 3.3.
11. **Thinking a signed card protects the endpoint.** It is about who you call. `to_a2a` mounts two
    routes and one of them executes the agent — part 4.1.
12. **Describing a specification you have not read.** The parked protocols get lookups with exact
    commands, not paragraphs — part 4.2, and §17.4.1 rule 5.

---

## §8 Verify before you code

Fetched on 2026-09-07:

| What | Where | What it said |
| --- | --- | --- |
| A2A specification | <https://a2a-protocol.org/latest/specification/> | *"Latest Released Version 1.0.0"*, previous versions 0.3.0, 0.2.6, 0.1.0 |
| §4.4.7 AgentCardSignature | same page | *"represents a JWS signature of an AgentCard. This follows the JSON format of an RFC 7515 JSON Web Signature (JWS)"* — `protected` required, `signature` required, `header` optional |
| §4.4.1 AgentCard | same page | *"signatures — array of AgentCardSignature — Required: No"* |
| Paper record | <https://api.crossref.org/works/10.17487/RFC7515> | *JSON Web Signature (JWS)*, RFC Editor, 2015 |
| AP2 documentation | <https://ap2-protocol.org/> | navigation lists an Agent Authorization Framework, Checkout Mandate, Payment Mandate, and Human Present / Human Not Present sample flows including x402 variants |
| `a2a-sdk` release | <https://pypi.org/pypi/a2a-sdk/json> | `info.version` 1.1.2, `requires_python` >=3.10 |

**ADK and SDK symbols verified against the installed packages**, not only against the docs.
`a2a.utils.constants` gives `AGENT_CARD_WELL_KNOWN_PATH = '/.well-known/agent-card.json'`,
`PROTOCOL_VERSION_CURRENT = '1.0'` beside `PROTOCOL_VERSION_0_3 = '0.3'`, and
`VERSION_HEADER = 'A2A-Version'`. In `a2a-sdk` 1.1.2 the types are **protobuf messages, not pydantic
models** — `AgentCard.DESCRIPTOR` reports fourteen fields with `signatures` at number 13, and
`AgentCardSignature.DESCRIPTOR` reports exactly `protected`, `signature`, `header`. ADK's
`agent_card_builder.py` is 561 lines and contains **zero occurrences** of the substrings `sign` or
`signature`. `to_a2a` returns a `Starlette` application whose `routes` list is empty until the
lifespan runs, after which it is `['/.well-known/agent-card.json', '/']`. Constructing
`AgentCardBuilder` emits a `UserWarning` beginning `[EXPERIMENTAL]` which states that *"A2A protocol
and SDK are themselves not experimental"* — the integration is, the protocol is not.

**The 1.x → 2.x trap this day pays for is ADK-73**, every model pinned explicitly: `_desk.py` pins
`gemini-2.5-flash-lite` even though nothing dials it, because the string is copied verbatim into a
published card and a default would be advertised to peers as a fact.

---

## §9 Say it in an interview

*"Phase 14 opened by making our agent discoverable over A2A, and the first thing we found was a gap
we had to fill ourselves. ADK builds the Agent Card from the agent object for free — it fills eight of
the protocol's fourteen fields — and it leaves `signatures` empty. That is the right call: signing
needs a private key and a framework that asked for ours would be asking for our identity. So we did
the other half by hand. Canonical bytes first, because you cannot sign an object — sorted keys, tight
separators, and the same card in any order gives one digest, where the readable form gives two. Then
an Ed25519 signature in the JWS JSON form the specification points at, which is three fields:
protected, signature, and an unprotected header. The finding I would lead with is the verifier. Write
it the obvious way — read `alg` out of the card and do what it says — and a forged card with
`alg: none` and a zero-character signature verifies as true, advertising whatever url the attacker
chose. The fix is not cryptographic, it is that the verifier holds an allowlist the card cannot
widen, and it refuses before it computes anything. Same shape for keys: `kid` is a hint about which
key to try, never a way for the card to supply one, and the moment you add a fetch to make
unknown-key tickets go away, verification proves only that the author owns a keypair. Two other
things worth saying. The specification marks signatures as not required, so conformant and
trustworthy are different properties and a verifier needs three outcomes rather than two — verified,
failed, unsigned — because merging the last two turns an incident and a business fact into the same
counter. And a signed card protects the direction where we call them; it does nothing about the
direction where they call us, and `to_a2a` mounts two routes of which one executes the agent with
nothing asking who the caller is."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands rather
than read them. `./m done 89` refuses to commit until they are.

The day is finished when you can look at any signed-artefact protocol and ask the five questions from
part 4.2 without looking them up — which bytes, who chooses the algorithm, where the key comes from,
what an unsigned artefact means, and what happens on rotation.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 89 | 2026-09-07 | AG-34, ADK-70 | 13 | <hash> | ⚠️ |
```

The gate column is `⚠️` and it means something specific. `./m depth`, `./m trace` and `./m wiki
--check` are green over this day and every measurement in it was run. Phase 14's gate is **"A2A peer
verified; repo public"** and the first clause is **half closed**: a card can now be signed and
verified against a key set the document cannot influence, and there is no registry yet to get that
key set from, which is tomorrow. `sutra/a2a.py` is the build brief and `lab/gate.py` reports 0 of 6,
by design. One finding carries forward with an owner: the JSON-RPC route executes the agent with
nothing asking who the caller is, and that is item 1 of part 5.2's list.

**`docs/PACKAGES.md`** — one new row, written when the package was added:

```text
| a2a-sdk | 1.1.2 | 2026-09-07 | 89 | What google.adk.a2a needs; ADK ships the integration and not the protocol library. |
```

The version was read from `pypi.org/pypi/a2a-sdk/json` before pinning (Principle 7), and days 84, 85
and 88's labs were re-run after the install to confirm the transitive `protobuf` upgrade broke
nothing.

**`docs/PAPERS.md`** — one new row:

```text
| JSON Web Signature (JWS) | doi:10.17487/RFC7515 | 2015 | 2026-09-07 | 89 | `days/day-89-signed-agent-cards/papers/01-a-signature-over-its-own-header.md` |
```

The title and year were copied from `api.crossref.org/works/10.17487/RFC7515` on 2026-09-07 — the
record, not the memory (§17.4.1 rule 5).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 89: a2a v1.0 - the signed agent card - closes AG-34, ADK-70
```

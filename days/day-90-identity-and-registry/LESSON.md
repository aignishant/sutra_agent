---
day: 90
phase: 14
phase_name: "Interop & launch"
title: "Agent identity and the registry"
ids: ["AG-29", "ADK-71"]
principles: [2, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 13
generated: "2026-09-07"
status: written
lab_scaffolded: true
commit: ""
---

# Day 90 — Agent identity and the registry

> **Yesterday (Day 89):** A2A v1.0 — the protocol, the Agent Card, and its signature verified by hand,
> so a peer can now prove that whoever holds a particular key produced a particular document. ADK
> fills eight of the protocol's fourteen card fields and never writes `signatures` at all, and a
> forged card carrying `alg: none` and a **zero-character signature verified `True`**.
> **Today:** the question that opens the moment the signature checks out — *whose key was that, and
> who says so.* `AgentCardBuilder` produces a card with **eight fields of a possible fourteen and zero
> signatures**, so ADK hands you an introduction with nothing behind it. Then the registry, and the
> four failures it exists to prevent: a swapped key accepted because nothing remembered the old one,
> two agents legitimately sharing one display name where the lookup returns the one holding
> `move_money`, a rotation that erased the archive, and a withdrawn peer admitted because **its
> signature is still perfectly valid and always will be.**
> **Tomorrow (Day 91):** the integrations survey — Slack-shaped intake and the wider ecosystem, with
> paid-only items marked 🅿️.

---

## §1 Where we are

The electoral roll at a polling booth.

You say your name and nobody acts on it. The officer turns to a printed list, finds a line, looks at
the photograph and the number beside it, and then looks at you. Saying your name is how you *point at*
the entry; it is not how you prove you are the person in it. The whole apparatus of a list, a
photograph and a serial number exists because everybody understands, without discussing it, that a
name spoken aloud is an assertion and nothing more.

Day 89 established that a peer can sign its card and that the signature can be checked. That answers
one question — *did the holder of this key sign this document* — and today is about discovering how
much it leaves open.

The measurement that opens the day is the framework's own. `AgentCardBuilder.build()` assembles a card
from an ADK agent and never touches the `signatures` field, so the default path produces **eight
populated fields**, `provider` and `securitySchemes` both null, and nothing that proves who sent it.
The A2A message type has room for signatures — the field is repeated, `lf.a2a.v1.AgentCardSignature`,
with `protected`, `signature` and `header` — and filling it is left to you.

So the day builds the thing that turns a valid signature into a peer you have decided to talk to: a
registry, keyed by identifier, holding the key you expect, who vouched for it, what it may do, and
whether it still counts. Each of those four columns is there because something measurable goes wrong
without it, and section by section this day removes them one at a time to show what.

The sharpest finding is the one that cannot be fixed with better cryptography. A withdrawn peer's
signature verifies, its key matches the registry, and **two of three checks return `True`** — because
revocation is a fact about a list you keep, not about anything the peer could ever hand you.

---

## §2 The map

Five sections. Section 1 is what an identity is and what the framework gives you. Section 2 is the
registry and the two ways of not having one. Section 3 is what happens when keys change. Section 4 is
the difference between verified and allowed. Section 5 is the bill, the list and the root.

### 1 — What an identity is

*The key is the identity; everything else on the card is a label.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [A name is not an identity](parts/01-what-an-identity-is/1.1-a-name-is-not-an-identity.md) | Two agents, one name, two keys — and which one a system may compare | `foundation` |
| 1.2 | [The three questions a peer has to answer](parts/01-what-an-identity-is/1.2-the-three-questions.md) | Who are you, who says so, what may you do — and what each does *not* establish | `foundation` |
| 1.3 | [What ADK puts in the card, and what it leaves out](parts/01-what-an-identity-is/1.3-the-sticker-anyone-can-print.md) | Eight fields of fourteen, zero signatures, and why the gap is invisible in a dump | `working` |

### 2 — The registry

*A record you keep, against evidence the peer supplies.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The registry is a file](parts/02-the-registry/2.1-the-list-behind-the-counter.md) | Four columns, and the failure each one prevents | `working` |
| 2.2 | [Trust on first use, and the swap it is meant to catch](parts/02-the-registry/2.2-the-milkmans-substitute.md) | Three policies, three contacts, and the one number that separates them | `working` |
| 2.3 | [Two shops, one name](parts/02-the-registry/2.3-two-shops-one-name.md) | 💥 An ambiguous name produces a choice, not an error — and the choice has `move_money` | `production` |

### 3 — Keys change

*Rotation keeps the peer and changes the key; revocation keeps the key and removes the peer.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Rotation: the two rules that pull opposite ways](parts/03-keys-change/3.1-the-cheques-already-written.md) | History must still read; the old key must stop working live | `working` |
| 3.2 | [The signature that stays valid for ever](parts/03-keys-change/3.2-the-card-of-someone-who-left.md) | 💥 Two of three checks pass and the peer was withdrawn months ago | `production` |

### 4 — Verified is not authorised

*Identity checked once; permission checked every time.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Verified is not authorised](parts/04-verified-is-not-authorised/4.1-the-man-the-office-sent.md) | The grant lives in the registry, and the check is per call | `working` |
| 4.2 | [One identity for many callers](parts/04-verified-is-not-authorised/4.2-the-shared-login.md) | 💥 One key, several callers, and a grant that becomes a union | `production` |

### 5 — In production

*What it costs, what is missing, and what everything rests on.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [What a registry costs](parts/05-in-production/5.1-what-a-registry-costs.md) | A hundred microseconds to check, and two maintenance tasks with no trigger | `production` |
| 5.2 | [What a real identity layer adds](parts/05-in-production/5.2-what-a-real-identity-layer-adds.md) | Nine items, two of which are an afternoon | `production` |
| 5.3 | [The registry as a single point of trust](parts/05-in-production/5.3-the-one-road-into-town.md) | Three of four inputs come from one box, and one person can write it | `production` |

### Papers — read after the parts

| # | Paper | What it gives this day |
| --- | --- | --- |
| 01 | [Speaks for — authentication as a chain of statements](papers/01-speaks-for.md) | `doi:10.1145/121132.121160` — authenticating a delegated request is a graph walk, not a check. The demo decides six requests correctly by following the chain and intersecting scopes; the ablation gets three, and two of those are right by accident |

---

## §3 Setup — run this

```bash
mkdir -p days/day-90-identity-and-registry/lab/papers/speaksfor
cd days/day-90-identity-and-registry/lab
touch _ids.py card.py registry.py tofu.py rotate.py revoke.py confusion.py authz.py gate.py
touch papers/speaksfor/chain.py papers/speaksfor/demo.py
```

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.
`a2a-sdk==1.1.2` arrived with Day 89 and has its own dated row in `docs/PACKAGES.md`; `cryptography`
and `pyjwt` are already present.

**What each file is for:**

- `_ids.py` is the file to read first: six Ed25519 keypairs generated from fixed seeds, a card type, the
  two signing helpers Day 89 taught, and the registry itself. Deterministic on purpose, so every
  fingerprint printed in this day is one you can reproduce.
- `card.py` builds a real card with `AgentCardBuilder` and counts what is in it.
- `registry.py` is resolution: id, then key, then signature, with the reason returned.
- `tofu.py` compares three trust policies over the same three contacts.
- `rotate.py` and `revoke.py` are section 3; `confusion.py` and `authz.py` are the two 💥 parts of
  sections 2 and 4.
- `gate.py` is the day's eval against `sutra/identity.py`.
- `papers/speaksfor/` holds the paper's demo: `chain.py` is the algorithm and nothing else.

Confirm the lab is ignored before you start:

```bash
git check-ignore -v days/day-90-identity-and-registry/lab/_ids.py
```

**Why:**

- `days/*/lab/` is ignored repo-wide (Principle 9), and this lab generates private keys. They are
  deterministic teaching keys with no value, and the habit of checking before writing key material
  anywhere is the point.

---

## §4 Build brief

The teaching is in `parts/`, the measurements are in `lab/`, and what is left is the piece that belongs
in the product.

**`sutra/identity.py`** — resolving a peer, as code the A2A executor can call.

- `TODO(me)`: `resolve(agent_id, card)` returning a decision **and a reason**, never a bare boolean.
  Part 1.2's three questions in order, with the key compared before the signature is verified.
- `TODO(me)`: compare **full public keys**, not the twelve-character fingerprint. Part 5.2 item 2; the
  fingerprint stays for the log line only.
- `TODO(me)`: `verify_card` handling **more than one signature**. The A2A field is repeated and this
  lab indexes `signatures[0]` throughout; decide what "verified" means when two signers disagree, and
  write the decision down in a comment.
- `TODO(me)`: `pinned` — a key store that survives a restart. Part 2.2 measured pinning working; a pin
  held in a process variable makes every restart a first contact, and on Day 86's replicas that is four
  first contacts.
- `TODO(me)`: `rotate` — `previous_keys` used for archives only, never for a live contact, with a
  `valid_until` per retired key. Part 3.1 named the missing window and part 5.2 made it item 3.
- `TODO(me)`: `revoked` — status read from the registry, and a **refused revoked peer logged at warning
  level with its id**. Part 5.2 item 5.
- `TODO(me)`: `allowed(entry, call)` checked per call rather than per session, with a default of
  refusal.

**`sutra/registry.py`** — the record itself.

- `TODO(me)`: a `confirmed_on` date on every row, and a check in `./m check` that fails when one is
  older than the policy. Part 5.1 found two maintenance tasks with no trigger; this is the trigger.
- `TODO(me)`: decide what happens when the registry cannot be read at all — refuse everything, or serve
  from a cached copy. Part 2.1's third failure. Choose it now, while it cannot fail.

**`tests/test_identity.py`**

- `TODO(me)`: a test that a valid signature from the wrong key is refused. Part 1.1, and it is the test
  that fails on a resolver written around `verify()`.
- `TODO(me)`: a test that a revoked peer is refused even though its signature verifies. Part 3.2.
- `TODO(me)`: a test that an archived signature still verifies after rotation, and that the old key is
  refused for a live contact. Part 3.1's two rules, which have to be two assertions.
- `TODO(me)`: a test that a call outside the grant is refused for a fully verified peer. Part 4.1.
- `TODO(me)`: a test that two entries sharing a `display_name` cannot both be resolved by name — or
  that no lookup by name exists. Part 2.3, and the second form is the better test.

**Two `TODO(me)`s that are not code:**

- **Write down who may change the registry**, and make a registry change its own pull request with
  nothing else in the diff. Part 5.3: three of the four inputs to every decision come from that one
  file.
- **Record the revocation latency** once the registry is anything other than an in-process dict. Part
  5.2 item 4 — the number is zero today and will not be tomorrow.

---

## §5 The eval that must be able to fail

```bash
cd days/day-90-identity-and-registry/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/identity.py`, all red today because the module is the build brief. A check
that cannot run counts as a **failure**, never as skipped (Principle 11).

The convention across this day's arms: **exit 0 when every identity claim in the run was settled
correctly, exit 1 when one was not** — either because something was wrongly accepted, or because a
claim could not be established at all.

```bash
uv run python card.py; echo "exit: $?"                          # 1 — eight fields, zero signatures
uv run python card.py --signed; echo "exit: $?"                 # 0 — one signature, and it verifies
uv run python registry.py; echo "exit: $?"                      # 0 — id, key and signature all agree
uv run python registry.py --unknown; echo "exit: $?"            # 1 — valid signature, no entry
uv run python tofu.py; echo "exit: $?"                          # 0 — pinned, and the swap is refused
uv run python tofu.py --no-pin; echo "exit: $?"                 # 1 — three verifications, swap accepted
uv run python tofu.py --registry; echo "exit: $?"               # 0 — refused, and nothing was pinned
uv run python rotate.py; echo "exit: $?"                        # 0 — archive reads, old key refused live
uv run python rotate.py --no-history; echo "exit: $?"           # 1 — rotation erased the archive
uv run python revoke.py; echo "exit: $?"                        # 0 — refused on a fact only we hold
uv run python revoke.py --signature-only; echo "exit: $?"       # 1 — withdrawn peer may move money
uv run python confusion.py; echo "exit: $?"                     # 0 — resolved by id, nothing to pick
uv run python confusion.py --by-name; echo "exit: $?"           # 1 — the wider capability set wins
uv run python authz.py; echo "exit: $?"                         # 0 — through the door and no further
uv run python authz.py --verified-is-authorised; echo "exit: $?" # 1 — identity treated as permission
```

Six of those arms go red, and **not one of them contains a failed signature.** Every card in this day
verifies against the key it names; every refusal comes from somewhere else. That is the day in one
observation.

The paper's demo does the same for its own claim: `demo.py` exits `0` deciding six of six requests the
way a person would, and `demo.py --off` exits `1` at three of six — with two of those three right for
the wrong reason.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | numbers not published without a signed-in session, checked 2026-09-07 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

`card.py` constructs a real `LlmAgent` with a pinned model and **never calls it** — building an agent
card reads the agent's static declaration, its description and the tools hanging off it, so the whole
thing is local. Everything else in the day is Ed25519 arithmetic and dictionary lookups.

The one cost worth recording is not a request. A full signature check measured **103.5 microseconds**
over two thousand iterations, of which the Ed25519 verification is 101.0 and the JSON serialisation
3.3 — so re-verifying a peer on every call of a conversation is roughly four orders of magnitude
cheaper than the model call it accompanies, and there is no performance argument for checking once.

---

## §7 Traps

1. **Treating the card's `name` as the identity.** It is a string the sender typed; the key is the
   identity — part 1.1.
2. **Believing a valid signature settles anything about *which* key.** It proves the holder of that key
   signed that document, and nothing more — parts 1.1 and 2.2.
3. **Assuming the framework signs the card.** `AgentCardBuilder.build()` never sets `signatures`, and
   the field is absent rather than null so it does not show in a dump — part 1.3.
4. **Indexing peers by display name.** Two legitimate entries can share one, and the lookup silently
   returns whichever the index kept — part 2.3.
5. **Verifying without remembering.** With no pin and no registry, a swapped key is accepted with a
   perfectly valid signature — part 2.2.
6. **Pinning somewhere that does not survive a restart.** A pin in a process variable makes every
   restart a first contact — part 2.2.
7. **Rotating without keeping the previous key.** Live contacts stay correct and the archive becomes
   unreadable, which nobody notices until an audit — part 3.1.
8. **Keeping previous keys without a validity window.** A key rotated *because it leaked* still verifies
   everything the leak signed — part 3.1.
9. **Checking the signature and stopping.** Revocation is a fact about your list, so a withdrawn peer
   passes two checks of three — part 3.2.
10. **Deleting a revoked row instead of marking it.** A withdrawn peer becomes indistinguishable from an
    unknown one, and the two need different alerts — parts 2.1 and 3.2.
11. **Treating verified as authorised.** The capability is computed, logged and not branched on — part
    4.1.
12. **Sharing one key across replicas or jobs.** The grant becomes the union of everything any caller
    needs, and attribution is gone — part 4.2.
13. **Forgetting that the registry is the root.** Three of the four inputs to every decision come from
    one file, and nothing downstream can detect a wrong row — part 5.3.

---

## §8 Verify before you code

Fetched and read on 2026-09-07:

| What | Where | What it said |
| --- | --- | --- |
| ADK A2A integration | <https://adk.dev/> A2A pages | `AgentCardBuilder` and `to_a2a` are the two entry points; the integration is marked experimental in the library itself |
| Paper record | <https://api.crossref.org/works/10.1145/121132.121160> | *Authentication in distributed systems*, Proceedings of the thirteenth ACM symposium on operating systems principles, 1991, pp. 165–182 |

**Symbols verified against the installed packages**, not only against the docs. `a2a.types.AgentCard`
is a **protobuf** message (`lf.a2a.v1.AgentCard`), not a pydantic model — `AgentCard.model_fields`
raises `AttributeError`, and the field list comes from `AgentCard.DESCRIPTOR.fields`. It carries
**fourteen** fields, of which `signatures` is repeated; its element type
`lf.a2a.v1.AgentCardSignature` has exactly three fields — `protected`, `signature`, `header` — which is
the JSON serialization of a JWS. `AgentCardBuilder.__init__` is keyword-only with `agent` required and
`rpc_url` defaulting to `'http://localhost:80/a2a'`; `build()` calls `_compat.build_agent_card(...)`
with nine keyword arguments and **never passes `signatures`**. Measured: eight of fourteen fields
present in the built card, six absent — `provider`, `documentation_url`, `security_schemes`,
`security_requirements`, `signatures`, `icon_url`.

**The 1.x → 2.x trap this day pays for is ADK-73** — every model pinned explicitly. `card.py` builds a
real `LlmAgent` and pins `gemini-2.5-flash-lite` even though the model is never called, because a
default would put it on `gemini-2.5-flash`, and a construction that would have spent requests if it had
run is one that will spend them the day somebody extends it.

---

## §9 Say it in an interview

*"We were about to accept work from agents we did not write, so we had to separate three things that
feel like one. First: the framework's own card builder produces a document with eight of the
protocol's fourteen fields and no signature at all — the protocol has a repeated signatures field,
shaped as a JWS, and filling it is left to the application. So out of the box a peer's card is entirely
self-asserted. Second, and this is the part people collapse: a valid signature proves that whoever
holds a key signed that document, and it cannot tell you it was the right key. We measured that —
three contacts, three genuine signatures, and a policy with no memory accepted a completely different
key answering to the same identifier on the third one. That is what the registry is for: a record we
keep, keyed by identifier and never by display name, saying which key we expect, who vouched, what the
peer may do and whether it still counts. We found the name thing the hard way too — two legitimately
registered agents sharing one display name, and a lookup by name returned the one whose capability list
included moving money. Nothing failed; the name was ambiguous and the lookup had to pick. The finding I
would lead with, though, is revocation. A withdrawn peer's signature verifies, its key still matches
our record, and two of our three checks return true — because revocation is a fact about a list we
keep, and it can never be in the credential. There is no version of checking the credential harder that
catches it. And the last thing: identity is checked once because it does not change, authorisation is
checked on every call because the request does. We had a run where the capability check was computed,
logged, and then not branched on — the peer was verified, so it was served, and it moved money it was
never granted."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have actually run the commands rather
than read them. `./m done 90` refuses to commit until they are.

The day is finished when somebody can hand you a signed credential and you can say, without hesitating,
the three separate things you still do not know — and where each of those three answers would have to
come from.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 90 | 2026-09-07 | AG-29, ADK-71 | 13 | <hash> | ⚠️ |
```

The gate column is `⚠️`. `./m depth`, `./m trace` and `./m wiki --check` are green over this day and
every measurement in it was run. What is not green: `sutra/identity.py` and `sutra/registry.py` are the
build brief and `lab/gate.py` reports 0 of 6, by design. Three findings carry forward — the card ADK
builds is unsigned, this lab indexes `signatures[0]` while the protocol field is repeated, and retired
keys have no validity window, so a key rotated after a compromise still verifies everything the
compromise signed.

**`docs/PACKAGES.md`** — no new rows. No package is added today; `a2a-sdk==1.1.2` was ledgered on
day 89.

**`docs/PAPERS.md`** — one new row:

```text
| Authentication in distributed systems | doi:10.1145/121132.121160 | 1991 | 2026-09-07 | 90 | `days/day-90-identity-and-registry/papers/01-speaks-for.md` |
```

The title, proceedings, year and pages were copied from
`api.crossref.org/works/10.1145/121132.121160` on 2026-09-07 — the record, not the memory
(§17.4.1 rule 5).

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 90: agent identity and the registry - closes AG-29, ADK-71
```

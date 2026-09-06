# Day 89 — checklist

**Definition of done.** `./m done 89` refuses to commit while any box is unticked. A box is ticked
when you have run the thing, not when you have read about it.

**The demo command for the whole day:**

```bash
cd days/day-89-signed-agent-cards/lab && uv run python alg.py; echo "exit: $?"
```

---

## Setup

- [ ] `days/day-89-signed-agent-cards/lab/` exists with the eleven files listed in the hub's §3.
- [ ] `uv add "a2a-sdk==1.1.2"` run, with the version read from PyPI first, and a dated
      `docs/PACKAGES.md` row written.
- [ ] Confirmed the before state: `AgentCardBuilder` raised `ModuleNotFoundError: No module named
      'a2a'` without it, and imports cleanly with it.
- [ ] Re-ran days 84, 85 and 88's labs after the install and confirmed the `protobuf` upgrade broke
      nothing.
- [ ] `git check-ignore -v days/day-89-signed-agent-cards/lab/_desk.py` prints a matching rule.
- [ ] Read `_desk.py` and can say why the signing key is generated on every import.

## Section 1 — the card

- [ ] Read [1.1 The card is the interface](parts/01-the-card/1.1-the-card-is-the-interface.md);
      ran both arms and can name the six fields ADK leaves empty.
- [ ] Can say which one of those six is different in kind from the other five, and why ADK is right
      not to fill it.
- [ ] Saw the `[EXPERIMENTAL]` warning at **construction** and can say which half of the stack it
      says is not experimental.
- [ ] Read [1.2 Where the card lives](parts/01-the-card/1.2-where-the-card-lives.md);
      ran both arms and saw `routes before startup: []`.
- [ ] Can say what a test suite that never runs the lifespan is actually asserting against.
- [ ] Read [1.3 What the card gives away](parts/01-the-card/1.3-what-the-card-gives-away.md);
      ran both arms and saw three tool names and three docstrings verbatim.
- [ ] Added a `delete_ticket` tool, read your own docstring back off the published card, removed it.

## Section 2 — signing it

- [ ] Read [2.1 A signature is over bytes](parts/02-signing-it/2.1-a-signature-is-over-bytes.md);
      ran both arms and can say why the two pretty digests differ at the same byte length.
- [ ] Dropped `sort_keys=True` from `card_bytes`, predicted the result, ran it, put it back.
- [ ] Read [2.2 Signing the card](parts/02-signing-it/2.2-signing-the-card.md);
      can name the three fields of an `AgentCardSignature` and which two are required.
- [ ] Can write the signing input from memory, and say why `protected` is not encoded twice.
- [ ] Changed `alg` to `ES256` with the Ed25519 key, saw it still verify, and can explain why.
- [ ] Read [2.3 The card that was edited](parts/02-signing-it/2.3-the-card-that-was-edited.md);
      ran `--tamper` and saw `InvalidSignature` at an unchanged byte length.
- [ ] Can say the two things a valid signature does **not** tell you.

## Section 3 — the verifier decides

- [ ] Read [3.1 The algorithm the card chose](parts/03-the-verifier-decides/3.1-the-algorithm-the-card-chose.md);
      ran both arms and saw `verified: True` on a zero-character signature.
- [ ] Swapped the `alg == "none"` branch above the allowlist check, ran `--strict`, put it back.
- [ ] Can state why `accepted=None` must not be typeable in `sutra/a2a.py`.
- [ ] Read [3.2 Which key](parts/03-the-verifier-decides/3.2-which-key.md);
      ran both arms and can name the three places a verifier can get a key from.
- [ ] Can say what a `jku` fetch would do to the value of verification, in one sentence.
- [ ] Read [3.3 The field the spec made optional](parts/03-the-verifier-decides/3.3-the-field-the-spec-made-optional.md);
      can state the three outcomes and which two a broad `except` would merge.

## Section 4 — the peer

- [ ] Read [4.1 A peer can send you work](parts/04-the-peer/4.1-a-peer-can-send-you-work.md);
      listed the two routes and can say which one executes the agent.
- [ ] Can name the card field that would have described the missing control, and why leaving it empty
      is currently accurate.
- [ ] Read [4.2 The map you are not building today](parts/04-the-peer/4.2-the-map-you-are-not-building-today.md);
      answered the five questions for A2A from memory.
- [ ] Put a date beside each of the three `TODO(me)` lookups in your own copy.
- [ ] Can give the honest answer to "what is TAP?" without inventing one.

## Section 5 — in production

- [ ] Read [5.1 What verification costs](parts/05-in-production/5.1-what-verification-costs.md);
      confirmed zero provider requests and can say what the real cost is denominated in.
- [ ] Read [5.2 What a real A2A deployment adds](parts/05-in-production/5.2-what-a-real-a2a-deployment-adds.md);
      mapped the seven-step sequence onto the nine items and found the step no item covers.
- [ ] Can name the single urgent item and say what not having it costs today.

## The paper — after the parts

- [ ] Read [papers/01 A signature over its own header](papers/01-a-signature-over-its-own-header.md).
- [ ] Ran `demo.py` and `demo.py --off` in `lab/papers/jws/` and saw 0 of 4 against 4 of 4.
- [ ] Can name the one line of `jws.py` that accounts for the difference.
- [ ] Added a fifth edit that re-serialises the same header in a different key order, predicted both
      arms, and checked.
- [ ] Can say which half of this specification the field kept and which half it learned to refuse.

## The build brief

- [ ] `sutra/a2a.py` written — `sign_card`, `verify_card`, `accepted_algs`, `trusted_keys`,
      `card_for_peers`, `refuse`.
- [ ] `verify_card` has **no default** for `accepted` or `keys`.
- [ ] `trusted_keys` holds the current key and the recently retired ones, loaded from somewhere the
      card cannot influence.
- [ ] `refuse` returns three distinct countable outcomes, not two.
- [ ] `card_for_peers` withholds the tool inventory.
- [ ] `tests/test_a2a.py` written — the `alg: none` test, the unknown-`kid` test, the one-character
      tamper test, and a test that runs the app through its lifespan.
- [ ] **Authentication on the JSON-RPC route** before this is reachable from anything but a laptop,
      with `securitySchemes` filled in the same change.
- [ ] **Decided where the public keys live** — or written down that Day 90 decides it.

## The evals, including ones that go red on demand

- [ ] `uv run python gate.py` runs and reports 0 of 6 — `sutra/a2a.py` is the build brief.
- [ ] `card.py` exits `1`; `--fields` exits `1`.
- [ ] `served.py` exits `1`; `--lifespan` exits `0`.
- [ ] `exposed.py` exits `1`; `--minimal` exits `0`.
- [ ] `canon.py` exits `0`; `--pretty` exits `1`.
- [ ] `sign.py` exits `0`; `--tamper` exits `1`.
- [ ] `alg.py` exits `1`; `--strict` exits `0`.
- [ ] `kid.py` exits `0`; `--rotate` exits `1`.
- [ ] `papers/jws/demo.py` exits `0`; `--off` exits `1`.
- [ ] **Break it and watch it go red:** moved `KEY_ID` out of the `trusted` dictionary in `kid.py`,
      confirmed the refusal names the missing `kid`, and put it back.

## The request budget

- [ ] Confirmed **zero** provider requests were made today, to every provider.
- [ ] Can say why this day has no allowance question in it, and which of the last ten days could say
      the same.

## Ledger & commit

- [ ] `./m depth 89` green.
- [ ] `./m trace` regenerated; day 89 closes exactly `AG-34`, `ADK-70`.
- [ ] `./m wiki` regenerated.
- [ ] `docs/PROGRESS.md` row appended, verbatim from the hub's §11, with the real commit hash.
- [ ] `docs/PACKAGES.md` — the `a2a-sdk==1.1.2` row present and dated.
- [ ] `docs/PAPERS.md` — the `doi:10.17487/RFC7515` row added.
- [ ] Committed with the message in the hub's §11.

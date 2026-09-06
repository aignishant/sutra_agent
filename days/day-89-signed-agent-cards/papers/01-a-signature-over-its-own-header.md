---
day: 89
paper: "doi:10.17487/RFC7515"
title: "A signature over its own header"
ids: ["AG-34"]
level: production
prerequisites: ["../parts/02-signing-it/2.2-signing-the-card.md"]
prev: "../parts/05-in-production/5.2-what-a-real-a2a-deployment-adds.md"
next: "../LESSON.md"
---

# Paper 01 — A signature over its own header

> **JSON Web Signature (JWS)**
> RFC Editor, 2015. `doi:10.17487/RFC7515`
>
> The decision this day borrows: the signing input is
> `ASCII(BASE64URL(protected header) || '.' || BASE64URL(payload))` — so the parameters that describe
> a signature are covered *by* that signature.

## One-line answer

Signing the payload alone is the obvious design and it leaves every parameter describing the
signature — which algorithm, which key — outside it; JWS puts the header inside the signing input, and
the measured difference is four out of four header edits caught instead of four out of four
surviving.

## The story

The bank draft with the terms printed on the back.

A cheque is signed for a sum, and the signature covers the sum, because that is obviously the number
that matters. Everything else on the document is administrative: the branch code, the account it draws
on, the little box saying which set of clearing rules apply.

Then somebody changes the box. Not the amount — the amount is signed and any change would be
obvious. The box that says which rules apply, which was never signed because nobody thought of it as
part of the promise.

The signature is intact and genuine, over a sum that has not moved. What has moved is the frame the
sum is read in, and every check anybody performs will pass.

## The idea in plain language

Before this specification, a signature over a document was usually understood as *a signature over
the document*. Sign the payload, attach the result, and hand over both.

That design has a gap, and it is not in the payload. A signature has to be accompanied by
information about itself — at minimum which algorithm was used, and usually which key. That
information has to travel with the signature, and if it is not inside the signature, then it is
attacker-controlled data that the verifier reads *in order to decide how to verify*.

The specification's answer is a small structural decision:

**Split the header in two.** A **protected** header, whose contents are covered by the signature, and
an optional **unprotected** header for things that genuinely do not need integrity — a hint about
which key to try, a routing label.

**Make the signing input the concatenation.** Base64url the protected header. Base64url the payload.
Join them with a dot. Sign *that* byte string.

The consequence is that `alg` and `kid` are no longer free-floating metadata. Changing either one
changes the signing input, so verification fails — the parameters have become part of the promise.

Two details that matter in practice and are easy to skip:

- **Base64url, not base64.** The alphabet uses `-` and `_` and the padding is stripped, so the result
  is safe in a url or an HTTP header with no further escaping. That is why the format ended up
  everywhere: it survives being put in places a signature has no business being.
- **The dot is a separator that cannot occur in the encoded parts.** So the signing input is
  unambiguously parseable back into its two components, without a length prefix or an escaping rule.

## Why Sutra needs it

Because the A2A specification does not define a signature format — it points here. Fetched from the
specification page on 2026-09-07, section 4.4.7 reads:

> *AgentCardSignature represents a JWS signature of an AgentCard. This follows the JSON format of an
> RFC 7515 JSON Web Signature (JWS).*

The three fields Sutra writes in part [2.2](../parts/02-signing-it/2.2-signing-the-card.md) —
`protected`, `signature`, `header` — are this document's JSON serialisation, with the payload detached
because the payload is the card the signature sits inside.

And because part [3.1](../parts/03-the-verifier-decides/3.1-the-algorithm-the-card-chose.md)'s
`alg: none` forgery is this paper's most famous failure, and understanding *why* the header is
protected is what makes the allowlist obviously necessary rather than a defensive habit.

## The mechanism

The method, written out rather than paraphrased. To sign a payload `P` with protected header `H`:

```text
1. compute  protected = BASE64URL(UTF8(JSON(H)))
2. compute  encoded   = BASE64URL(P)
3. compute  input     = ASCII(protected || '.' || encoded)
4. compute  sig       = SIGN(key, input)
5. emit     {"protected": protected, "signature": BASE64URL(sig), "header": U}
```

Step 3 is the whole contribution. Steps 1, 2, 4 and 5 are packaging.

To verify, the recipient reverses it — and the specification is explicit that the recipient, not the
document, decides what is acceptable:

```text
1. reject unless H["alg"] is in the set THIS RECIPIENT accepts
2. select the key by policy; H["kid"] may hint, it may not supply
3. recompute input from the protected string AS RECEIVED and the payload
4. VERIFY(public key, input, sig)
```

Step 1 is where `alg: none` dies. Step 2 is where a `jku` fetch would undo everything. Step 3's *as
received* matters: re-encoding the protected header rather than using the transmitted string
introduces exactly the canonicalisation problem part
[2.1](../parts/02-signing-it/2.1-a-signature-is-over-bytes.md) is about — which is why the protected
header travels as a string and not as an object.

The unprotected header `U` in step 5 is the part people misuse. It exists for data whose integrity
does not matter. Anything a verifier acts on belongs in `H`.

## The paper in one demo

A small project implementing this one decision and nothing else. Two files, one document, one key, and
an attacker who edits only the header.

```text
days/day-89-signed-agent-cards/lab/papers/jws/
├── jws.py    # the signing input, both ways, and nothing else
└── demo.py   # four header edits against each; --off removes the protection
```

The algorithm is one function with one branch:

```python
def signing_input(protected: str, payload: bytes, *, protect_header: bool) -> bytes:
    if protect_header:
        return f"{protected}.{b64u(payload)}".encode("ascii")
    return payload
```

**Line by line:**

- The `if` is the paper. Everything else in both files is scaffolding to measure what that line buys.
- `protect_header` is keyword-only, because a positional boolean at a call site reads as noise and
  this one changes the security property of the whole scheme.
- The `False` branch is not a straw man. Signing the payload alone is what a competent person writes
  when the requirement is "sign the document", and it is a complete, working signature scheme — over
  the wrong bytes.
- Both branches return `bytes`, so the calling code is identical either way. Nothing downstream can
  tell which scheme it is using, which is precisely why the mistake survives review.

The attacker edits only the header, never the payload:

```python
EDITS = (
    ("downgrade the algorithm", {"alg": "none", "kid": "sutra-desk-2026-09"}),
    ("point at another key", {"alg": "EdDSA", "kid": "attacker-key-1"}),
    ("add a critical parameter", {"alg": "EdDSA", "kid": "sutra-desk-2026-09", "b64": False}),
    ("claim a different type", {"alg": "EdDSA", "kid": "sutra-desk-2026-09", "typ": "plain"}),
)
```

**Line by line:**

- Four edits, each a real technique. The first is the `alg: none` downgrade. The second redirects key
  selection. The third sets `b64: false`, which in JWS changes how the payload is encoded — a
  parameter that alters interpretation without altering content. The fourth relabels the type.
- The payload is **untouched** in all four. That is the experiment: the document says the same thing
  and the instructions for reading it have changed.
- Each forgery reuses the original `signature` verbatim. No key is needed and none is generated;
  forging is base64 of a small JSON object.

Run it:

```bash
cd days/day-89-signed-agent-cards/lab/papers/jws
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- No flag: `protect_header=True`, which is the specification. This is the arm that should catch every
  edit, so an exit code of `0` here is the claim being reproduced rather than merely code running.

Measured on 2026-09-07:

```text
signing input: RFC 7515: protected header + payload
payload: {"name":"sutra_desk","url":"http://desk.internal:8931/"}
header:  {"alg":"EdDSA","kid":"sutra-desk-2026-09"}

  edit                        header after the edit                               verifies
  (none)                      {"alg":"EdDSA","kid":"sutra-desk-2026-09"}          True
  downgrade the algorithm     {"alg":"none","kid":"sutra-desk-2026-09"}           False
  point at another key        {"alg":"EdDSA","kid":"attacker-key-1"}              False
  add a critical parameter    {"alg":"EdDSA","kid":"sutra-desk-2026-09","b64":fa  False
  claim a different type      {"alg":"EdDSA","kid":"sutra-desk-2026-09","typ":"p  False

  header edits attempted: 4
  header edits that still verified: 0

  every header edit broke the signature, because the header is part of what was signed
exit: 0
```

Now the ablation — the same code with the header outside the signing input:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` flips one boolean and changes nothing else — same key, same payload, same four edits. It
  exits `1` because the demo's job is to reproduce the paper's claim and this arm deliberately does
  not.

Measured on 2026-09-07:

```text
signing input: payload only

  edit                        header after the edit                               verifies
  (none)                      {"alg":"EdDSA","kid":"sutra-desk-2026-09"}          True
  downgrade the algorithm     {"alg":"none","kid":"sutra-desk-2026-09"}           True
  point at another key        {"alg":"EdDSA","kid":"attacker-key-1"}              True
  add a critical parameter    {"alg":"EdDSA","kid":"sutra-desk-2026-09","b64":fa  True
  claim a different type      {"alg":"EdDSA","kid":"sutra-desk-2026-09","typ":"p  True

  header edits attempted: 4
  header edits that still verified: 4
    - downgrade the algorithm
    - point at another key
    - add a critical parameter
    - claim a different type

  the payload is untouched and the signature is valid, and the verifier is
  now taking its instructions from a field nobody signed
exit: 1
```

**Zero of four against four of four**, from one branch in one function. And note the first row of both
tables: the honest, unedited case verifies `True` under both schemes. The broken scheme is not broken
in a way any ordinary test would find — it signs, it verifies, it round-trips. It fails only against
an adversary, which is why the design decision had to be made in the format rather than discovered in
production.

## When it breaks

The paper's claim is narrow, and knowing its edges is what separates using it from quoting it.

**It protects the header, not the choice.** A signed `alg` cannot be changed — and if the verifier
accepts whatever the signed `alg` says, an attacker who can produce *any* valid signature can still
steer it. Protection makes the parameter tamper-evident; it does not make it trustworthy. The
allowlist in part [3.1](../parts/03-the-verifier-decides/3.1-the-algorithm-the-card-chose.md) is the
other half and this document requires it in words, which turned out not to be enough.

**The unprotected header is a trap the format ships with.** `header` exists, it is legal, and anything
put there is unsigned. Its presence beside a protected header with the same shape is the single
easiest way to undo the paper's contribution by accident.

**`crit` and the extensibility that came with it.** The format allows critical extension parameters,
and `b64: false` — one of the demo's edits — was a later addition that changes how the payload is
encoded. Generality of this kind is what makes a format last twenty years and also what makes writing
a correct verifier harder than it looks.

**It says nothing about what the payload means.** A perfectly formed JWS over a card claiming
capabilities the agent does not have is valid. Part
[2.3](../parts/02-signing-it/2.3-the-card-that-was-edited.md) made this point and it survives contact
with the paper: this is an integrity mechanism, not a truth mechanism.

## In production

**What survived.** Almost all of it, and far outside its origin. The compact serialisation —
`header.payload.signature` — is one of the most widely deployed data formats in existence; every
identity token you have ever seen in a browser is one. The protected-header decision is now simply
how signature formats are designed, to the point where the alternative looks obviously wrong in
hindsight, which is the strongest thing you can say about a design choice. And the A2A specification
in 2026 reaches for it rather than inventing a format, which is the whole reason this day exists.

**What did not.** Two things, and the field learned both the hard way.

`alg: none` is the famous one. It is in the specification for a legitimate reason — an unsecured JWS
for cases where integrity comes from elsewhere — and it became a well-known vulnerability class
because library authors implemented `alg` dispatch faithfully and application authors did not supply
an allowlist. The current consensus is not that the value should not exist but that no general-purpose
library should ever reach it by default.

Unconstrained algorithm agility more broadly went the same way. The idea that a deployment should
accept whatever the document offers has been replaced by pinning one algorithm and treating a second
as a migration — part [3.1](../parts/03-the-verifier-decides/3.1-the-algorithm-the-card-chose.md)'s
**In production** section is that consensus, and this specification's own design anticipated the
mechanism while the field had to discover the policy.

**What it means for this repository, concretely.** Sutra signs cards with `EdDSA`, puts `alg` and
`kid` in the protected header, keeps the unprotected `header` as a duplicate hint that nothing acts
on, and refuses any algorithm not in a tuple the card cannot reach. Four of the day's five sharpest
findings are downstream of this one paper, and the fifth — that ADK leaves `signatures` empty — is
what makes them the reader's job rather than the framework's.

**The review comment a senior engineer leaves:** *"Read the `header` field access in this verifier
again. If anything we act on comes out of the unprotected one, the signature is decorative."*

**The interview question:** *"Why does JWS sign the header along with the payload?"* The answer that
shows experience does not say "for integrity". It says the header tells the verifier how to verify,
so leaving it unsigned lets the attacker choose the check — and then names `alg: none` as the
demonstration rather than as the definition.

## Check yourself

```bash
cd days/day-89-signed-agent-cards/lab/papers/jws
uv run python demo.py; echo "exit: $?"
uv run python demo.py --off; echo "exit: $?"
```

Zero of four, then four of four. Say which single line of `jws.py` accounts for the difference, and
why no ordinary unit test would have caught the broken version.

Now add a fifth edit to `EDITS` that changes nothing at all — the same header, re-serialised with the
keys in a different order. Predict what each arm says before you run it. The answer is more
interesting than it looks and it connects straight back to part 2.1.

**Out loud, without scrolling up:** state the signing input in one line, say which of its two parts
is the paper's contribution, and name the one thing a valid JWS still does not tell you.

**Next:** back to the hub — [`LESSON.md`](../LESSON.md).

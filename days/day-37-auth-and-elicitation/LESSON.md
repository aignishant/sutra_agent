---
day: 37
phase: 5
phase_name: "MCP I: the protocol"
title: "Auth and enterprise — badges, questions and policy"
ids: ["MCP-13", "MCP-27", "MCP-30"]
principles: [1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 19
generated: "2026-09-04"
status: written
lab_scaffolded: true
commit: ""
---

# Day 37 — Auth and enterprise: badges, questions and policy

> **Yesterday (Day 36):** long jobs. Work that outlives a request returned a task handle instead of
> blocking, and `sutra_mcp/tasks.py` learned to hand back a receipt the client polls.
> **Today:** three questions that arrive together the moment a server leaves your laptop — who is
> calling, may the server ask the human something, and who decides company-wide what may be asked at
> all.
> **Tomorrow (Day 38):** the failure and migration lab — timeouts, malformed servers, and the three
> deprecated client features whose replacement is the `InputRequiredResult` pattern you build today.

---

## §1 Where we are

A shop with one till and one owner does not need a stock-taking procedure. The owner knows what is
on the shelves, knows who is behind the counter, and knows that nobody is going to walk out with the
cash box, because the only person who can reach it is him.

The morning he hires two people, none of that is true any more. Not because they are dishonest —
because *knowing everyone* has stopped being a mechanism. There has to be a till roll. There has to
be a rule about who can give a refund. And there has to be an answer to *"a customer wants to return
this, can I?"* that is not "go and find the owner", because the owner is not always there.

That is `sutra_mcp` this morning. It is a process on your laptop, spoken to over stdio by a client
you also wrote. "Anyone may call `lookup_ticket`" means "you may call `lookup_ticket`", and that
sentence is true and harmless. Day 43 turns the same code into an application any instance can
serve, on a network, and the sentence stops being harmless.

Three things arrive together on that day, and today is where each gets its mechanism.

**Who is calling.** The server does not check who you are. It checks a **token** somebody else
issued, and it checks three things about it: that it came from the desk we trust, that it names *us*
as its audience, and that it carries the permission this tool needs. Section 1 is the roles; section
2 is the two 2026 hardenings — `iss` validation, which closes the mix-up attack, and Client ID
Metadata Documents, which retire Dynamic Client Registration.

**May the server ask the human something.** A tool that discovers, halfway through, that closing one
ticket means closing four cannot guess. It has to ask. And since the 2026-07-28 revision it cannot
interrupt: server-initiated requests are gone, so the server **ends the call** with a result saying
*input required*, and the client comes back with the answer. Section 3 is that shape and its three
answers; section 4 is what happens when the answer must not pass through the client at all.

**Who decides, for everybody.** Beyond MCP's small core, every capability is a named, versioned
extension declared in the open on every request. That is what makes centralised policy possible:
an organisation's identity provider can allow a server, deny a capability across all servers, and
grant scopes by group — and an employee who is not permitted never receives a token at all.
Section 5.

Four things to know before you read a part.

**Every lab script in this day runs on zero model calls.** Authorization and consent are the parts
you must be able to reason about with no model in the room, and all seventeen scripts plus the paper
demo are arithmetic, string comparison and two servers on `127.0.0.1`.

**Half of this day is not in the pinned SDK, and you will measure which half.** `mcp==1.29.1` has
both elicitation modes and the three-action result; it does not have `InputRequiredResult`,
`requestState`, the `iss` check or the extensions framework. Six of ten mechanisms present, four
absent. Part 6.2 runs that measurement rather than asserting it, and **the pin does not move today**.

**Two things needing a real tenant are 🅿️ parked**, and honestly: Enterprise-Managed Authorization
needs a corporate identity provider, and third-party OAuth needs a third party. Both are documented,
whiteboard-ready and interview-ready. The *decision logic* — the part an administrator actually
writes — is built and runnable.

**Six of today's mechanisms fail with no error message.** A missing audience check makes every test
pass. A missing `iss` check completes the flow with an attacker holding the code. An unsigned state
string accepts every honest retry. That is why the day ends with a seven-question form that starts
**red**, and why so much of it is about checks you cannot test your way to.

---

## §2 The map

Nineteen parts in six sections, plus **one paper**, read last. The day climbs
`foundation → working → production` and the through-line is **who is allowed to decide**, moving
outward: the token in section 1, the desk that issued it in section 2, the human in sections 3 and 4,
the organisation in section 5, and the deployment in section 6.

### Section 1 — `01-the-badge`: who is calling, proven rather than asserted (MCP-13)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The badge, the desk and the door](parts/01-the-badge/1.1-the-badge-the-desk-and-the-door.md) | Four roles, and the one thing each must not hold | `foundation` |
| 1.2 | [The refusal that carries directions](parts/01-the-badge/1.2-the-refusal-that-carries-directions.md) | 401, `WWW-Authenticate`, and one hop to the desk | `working` |
| 1.3 | [A voucher for one shop](parts/01-the-badge/1.3-a-voucher-for-one-shop.md) | Audience, and the check with no failing test | `working` |

### Section 2 — `02-issuer-checks`: which desk answered, and how a stranger introduces itself (MCP-13)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Which desk actually answered](parts/02-issuer-checks/2.1-which-desk-actually-answered.md) | The mix-up attack, and the four-row table | `working` |
| 2.2 | [The comparison that must not be helpful](parts/02-issuer-checks/2.2-the-comparison-that-must-not-be-helpful.md) | One issuer becomes five, from three tidy-ups | `working` |
| 2.3 | [The menu you host yourself](parts/02-issuer-checks/2.3-the-menu-you-host-yourself.md) | CIMD, and zero registration writes | `working` |

### Section 3 — `03-the-question`: the server asks the human (MCP-27)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The job that stopped and left a number](parts/03-the-question/3.1-the-job-that-stopped-and-left-a-number.md) | `InputRequiredResult`, and why the call ends | `foundation` |
| 3.2 | [A form the till can print](parts/03-the-question/3.2-a-form-the-till-can-print.md) | Flat schemas, and why nesting is refused | `working` |
| 3.3 | [Three answers, not two](parts/03-the-question/3.3-three-answers-not-two.md) | `decline` is not `cancel`, and the fourth non-answer | `working` |
| 3.4 | [The docket you cannot write yourself](parts/03-the-question/3.4-the-docket-you-cannot-write-yourself.md) | Signed `requestState`, and four refusals | `production` |

### Section 4 — `04-out-of-band`: the answers the client must never see (MCP-27)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The link you check before you click](parts/04-out-of-band/4.1-the-link-you-check-before-you-click.md) | URL mode, and the seven client rules | `working` |
| 4.2 | [💥 The sheet in the corridor](parts/04-out-of-band/4.2-the-sheet-in-the-corridor.md) | The MUST NOT, and the five places a form answer lands | `production` |
| 4.3 | [💥 The link that went to the wrong person](parts/04-out-of-band/4.3-the-link-that-went-to-the-wrong-person.md) | The same-user check, with and without | `production` |

### Section 5 — `05-policy`: who decides for everybody (MCP-30)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [The optional extras list](parts/05-policy/5.1-the-optional-extras-list.md) | Extensions, and four named, one live | `foundation` |
| 5.2 | [One account instead of forty](parts/05-policy/5.2-one-account-instead-of-forty.md) | EMA, ID-JAG, and zero consent dialogues | `working` |
| 5.3 | [Policy that can name a feature](parts/05-policy/5.3-policy-that-can-name-a-feature.md) | Three levels of rule, and what declarations cannot enforce | `production` |

### Section 6 — `06-in-production`: after it ships

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [💥 The receipt that printed the whole number](parts/06-in-production/6.1-the-receipt-that-printed-the-whole-number.md) | Three exits, and the one you cannot undo | `production` |
| 6.2 | [The tray the driver cannot see](parts/06-in-production/6.2-the-tray-the-driver-cannot-see.md) | Six of ten, and which four you build by hand | `production` |
| 6.3 | [Seven questions before you ask anybody anything](parts/06-in-production/6.3-seven-questions-before-you-ask-anybody-anything.md) | The form that starts red | `production` |

### The paper — read it **after** the parts

| Paper | Identifier | What it argued |
| --- | --- | --- |
| [OAuth 2.0 Authorization Server Issuer Identification](papers/01-issuer-identification.md) | `doi:10.17487/RFC9207` (2022) | An authorization response must identify the server that produced it, and the client must compare before redeeming |

Principle 4 at the scale of a day: build the check in
[2.1](parts/02-issuer-checks/2.1-which-desk-actually-answered.md), argue about the comparison in
[2.2](parts/02-issuer-checks/2.2-the-comparison-that-must-not-be-helpful.md), *then* read the
document that specified both — and find out that four years later the SDK on this machine still does
not perform it.

---

## §3 Setup — run this

**No package is added today, and no package is upgraded.** `git diff pyproject.toml uv.lock` must be
empty when you finish. `mcp` stays at `1.29.1`; 6.2 measures exactly what that costs and the decision
about the pin belongs to a plan amendment, not to a day.

```bash
# 1 - the day's lab
cd days/day-37-auth-and-elicitation
mkdir -p lab/papers/issuer-identification

# 2 - section 1: the roles, the challenge, the audience
touch lab/badge.py lab/challenge.py lab/audience.py

# 3 - section 2: iss, the comparison, CIMD
touch lab/iss_check.py lab/compare.py lab/cimd.py

# 4 - section 3: the carriage, the schema, the actions, the state
touch lab/elicit_form.py lab/actions.py lab/request_state.py

# 5 - section 4: URL mode, the credential guard, the same-user check
touch lab/url_mode.py lab/credential_guard.py lab/same_user.py

# 6 - section 5: extensions and policy
touch lab/extensions.py lab/policy.py

# 7 - section 6: the leak, the SDK surface, the review form
touch lab/leak.py lab/sdk_surface.py lab/review.py

# 8 - the paper demo
touch lab/papers/issuer-identification/authservers.py
touch lab/papers/issuer-identification/client.py
cd -

# 9 - the gate, before anything else: has the specification moved?
curl -sL https://modelcontextprotocol.io/specification/versioning | grep -o "specification/2026-07-28" | head -1
```

**Step 9 is the gate and it is not ceremony.** This day is written against revision **2026-07-28**. If
that page names a newer current revision, stop: amend the plan first, then write code (Principle 14).
It printed `specification/2026-07-28` on 2026-09-04.

**One environment variable, and it is not a secret.** `lab/request_state.py` reads
`SUTRA_STATE_KEY` from the environment with a development fallback that is named as one. Nothing in
this day needs `GOOGLE_API_KEY`, and nothing in this day should put a real key anywhere but `.env`.

**Ports used:** `8871` and `8872`, loopback only, by the paper demo. If either is busy, change both
constants in `authservers.py`.

**Read the parts in order and the paper last.** Section 2 needs section 1's vocabulary, section 4
needs section 3's carriage, and the paper is only worth reading once you have written the comparison
it specifies.

---

## §4 Build brief

**Two project files today**, and the learner writes every line of both.

`sutra_mcp/auth.py` — the **server** side. It validates; it never mints, never stores a password and
never trusts a client-supplied identity.

| What it holds | From |
| --- | --- |
| the canonical resource URI, published once and compared against | 1.2, 1.3 |
| `verify_token(token) -> Token \| None` — issuer, audience, scope, in that order | 1.3 |
| the `WWW-Authenticate` challenge builder, for 401 and 403 | 1.2 |
| `mint_state` / `verify_state` — HMAC, principal, TTL, parameter digest | 3.4 |
| the three-way elicitation answer handler | 3.3 |
| the credential guard that refuses a form-mode secret before it is sent | 4.2 |
| `same_user(elicitation_id, session_sub)` for the connect route | 4.3 |

`sutra/mcp/auth.py` — the **client** side. It carries a token and checks who it is talking to.

| What it holds | From |
| --- | --- |
| `discover_issuer(response) -> str \| None` from the `WWW-Authenticate` header | 1.2 |
| the recorded-issuer record, keyed by `state`, holding the PKCE verifier too | 2.1 |
| `validate_iss(returned, recorded, advertised)` — strict, before any token request | 2.1, 2.2 |
| the CIMD `client_id` constant and the `client_id_metadata_document_supported` check | 2.3 |
| the URL-mode link inspection the host shows before consent | 4.1 |
| the bearer redactor, applied in the logging path and nowhere else | 6.1 |
| the `extensions` object in the `_meta` block — empty today, and deliberately so | 5.1 |

**`TODO(me)` markers left for you:**

- **1.3** — decide whether a token whose `aud` is `https://mcp.sutra.example` (no path) may be used
  at `https://mcp.sutra.example/mcp`. Both answers are defensible; only one can be Sutra's.
- **1.2** — decide what Sutra's client does with a 401 that carries **no** `WWW-Authenticate` header.
- **2.1** — decide what `issuer_of` does when the response carries `iss` twice with different values.
- **2.3** — decide where Sutra's Client ID Metadata Document is hosted, and write the exact HTTPS URL
  down. It must have a path component.
- **3.2** — rewrite the "which duplicates?" question legally, as a multi-select of ticket ids, and
  write down what the user loses.
- **3.3** — decide how long a `decline` on "close the duplicates too" lasts: this ticket, this day, or
  for ever. Write it beside the decline branch.
- **3.4** — choose Sutra's `requestState` TTL and say what it trades. Then decide whether any of
  Sutra's elicitations need **single use**, which is the one case that needs a store.
- **4.1** — decide whether `inspect_link` should refuse or merely warn on an open redirect hosted on
  the trusted domain, and where that gets fixed.
- **4.3** — choose the pending-elicitation TTL, and reconcile it with the `requestState` TTL from 3.4.
- **5.1** — decide which extensions Sutra's client will declare, and write the empty object today
  rather than inventing the shape later.
- **5.3** — decide whether Sutra's audit log records the *requested* extension set, the *live* one, or
  both.
- **6.1** — decide whether the bearer redactor should also emit a stable hash of the token, so
  correlation never needs the credential.
- **6.2** — write the assertion `tests/test_mcp_sdk_surface.py` needs: the exact symbol set this
  codebase depends on, plus the protocol version, so a pin bump fails the build.
- **6.3** — answer all seven review questions for `sutra_mcp` as it will exist at the end of Phase 5,
  and add an eighth: *when was this last reviewed?*

---

## §5 The eval that must be able to fail

Six checks with an exit code, plus the paper ablation. All on zero model calls.

**The review form is the day's gate, and it is red on purpose:**

```bash
python days/day-37-auth-and-elicitation/lab/review.py; echo "exit: $?"
```

Measured on 2026-09-04: `unanswered questions: 7` and `exit: 7`. Every field is `None` because nobody
has decided yet, which is exactly true on the day the file is created. Fill all seven and it reaches
`exit: 0`. Blank `REVIEWED_BY` alone and watch it go to 1 — six technical answers and no name is the
shape of a review nobody did.

**The SDK surface check is red today and nobody expected the split:**

```bash
.venv/Scripts/python.exe days/day-37-auth-and-elicitation/lab/sdk_surface.py; echo "exit: $?"
```

Measured the same day: `mechanisms taught today that this SDK cannot speak: 4` and `exit: 4`, with
`pinned SDK speaks protocol : 2025-11-25`. Elicitation is fully present; the MRTR carriage, the `iss`
check and the extensions framework are not. **Do not change the pin to make it green.**

**Four checks that are green and can be broken on purpose:**

```bash
python days/day-37-auth-and-elicitation/lab/iss_check.py; echo "exit: $?"
python days/day-37-auth-and-elicitation/lab/request_state.py; echo "exit: $?"
python days/day-37-auth-and-elicitation/lab/credential_guard.py; echo "exit: $?"
python days/day-37-auth-and-elicitation/lab/leak.py; echo "exit: $?"
```

All four printed `exit: 0` on 2026-09-04. Each has a named break in its own part: test the
`advertised` flag before the presence of `iss` and watch a row flip (2.1); move the payload decode
above the signature check and watch nothing change (3.4); take `api_key` out of `SECRET_WORDS` (4.2);
make `redact` return its input and watch the exit code reach 1 (6.1).

**The paper demo is the ablation, and both arms must be run:**

```bash
cd days/day-37-auth-and-elicitation/lab/papers/issuer-identification
ISS_CHECK=1 python client.py
ISS_CHECK=0 python client.py
cd -
```

`token requests sent: 0` and `attacker holds an honest authorization code: False`, against
`token requests sent: 1` and `True ['honest-code-4521']`. Same servers, same flow, same code; the only
difference is whether anybody read the `iss` parameter.

**And the same-user ablation, which is the day's second switchable failure:**

```bash
SAME_USER=1 python days/day-37-auth-and-elicitation/lab/same_user.py
SAME_USER=0 python days/day-37-auth-and-elicitation/lab/same_user.py
```

`vault: {}` against `vault: {'u-1': 'vendor-token-granted-by-u-2'}` — one dictionary entry whose key
and whose grant came from two different people.

**The rest, each printing a table:**

```bash
python days/day-37-auth-and-elicitation/lab/badge.py
python days/day-37-auth-and-elicitation/lab/challenge.py
python days/day-37-auth-and-elicitation/lab/audience.py
python days/day-37-auth-and-elicitation/lab/compare.py
python days/day-37-auth-and-elicitation/lab/cimd.py
python days/day-37-auth-and-elicitation/lab/elicit_form.py
python days/day-37-auth-and-elicitation/lab/actions.py; echo "exit: $?"
python days/day-37-auth-and-elicitation/lab/url_mode.py; echo "exit: $?"
python days/day-37-auth-and-elicitation/lab/extensions.py
python days/day-37-auth-and-elicitation/lab/policy.py; echo "exit: $?"
```

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04).

| What | Generations |
| --- | --- |
| every part in every section | **0** |
| all seventeen lab scripts | **0** |
| the paper demo, both arms | **0** |
| the SDK surface check | **0** — it reads files on disk |
| **Total planned** | **0 of 20** |

**Zero, and that is the point.** Permission machinery is exactly the part you must be able to reason
about without a model in the room: a token either names us or it does not, and an issuer either
matches or it does not. Today's only network traffic is one HTTPS GET to the specification site for
the freshness gate, plus two servers on `127.0.0.1` for the paper demo. Your whole day's quota is
still there tomorrow.

**Cost: $0.** No identity provider, no cloud IAM, no billing account — Addendum 02 holds, and the two
things that would need a tenant are 🅿️ parked.

---

## §7 Traps

- **A missing audience check has no failing case, only a widened one.** Comment out the `aud`
  comparison and every test still passes; the only change is that a token minted for another service
  is now accepted (1.3).
- **401 and 403 are not interchangeable.** 401 means get a token; 403 means `insufficient_scope` and
  get a **wider** one. A client that conflates them re-authorizes with the same scopes and loops
  (1.2).
- **A token whose audience is wrong gets a 401, not a 403.** It is an invalid token, not a permissions
  problem (1.3).
- **Never send a token you were given to an upstream API.** That is token passthrough, and the
  specification forbids it by name (1.3).
- **Check `iss` whenever it is present, even if the metadata does not advertise support.** Servers
  emit the parameter before they update their metadata, and a client keyed only on the advertisement
  skips the check for exactly those servers (2.1).
- **Compare `iss` before the token request, never after.** Afterwards tells you that you were
  attacked (2.1).
- **Do not normalise before comparing.** Case folding, trailing-slash trimming and default-port
  elision took one accepted issuer to five (2.2).
- **Form-decode the `iss` value once, then nothing.** It arrives percent-encoded, and comparing an
  encoded string to a decoded one fails on every honest response (2.2).
- **A CIMD `client_id` must be HTTPS with a path component**, and the document's `client_id` must
  equal the URL it was fetched from. The URL is the identity; the document is only what it claims
  (2.3).
- **Changing a `redirect_uri` is two deployments**, because authorization servers cache your metadata
  document (2.3).
- **`InputRequiredResult` is a success, not an error.** A client that looks for `content` gets a
  `KeyError` (3.1).
- **The retry's JSON-RPC `id` must differ from the original.** They are independent requests (3.1).
- **`requestState` is echoed exactly, or not at all.** If the result carried one, the retry must; if
  it did not, the retry must not invent one (3.1).
- **Only `prompts/get`, `resources/read` and `tools/call` may receive an `InputRequiredResult`**
  (3.1).
- **The elicitation schema is a flat object of primitives.** No nesting; arrays only as multi-selects
  of strings (3.2).
- **`default: true` on a destructive option turns a confirmation into a rubber stamp** (3.1).
- **`decline` is not `cancel`.** One is a decision, one is an absence of one, and folding them makes a
  tool that nags (3.3).
- **Check the HMAC before decoding the payload**, and use `hmac.compare_digest`. A plain `==` leaks
  the tag one character at a time (3.4).
- **Signed state bounds replay; it does not guarantee single use.** That needs a server-side store
  (3.4).
- **A client must not pre-fetch a URL-mode link.** Fetching is an action (4.1).
- **Compare `parsed.hostname`, never `parsed.netloc`.** `https://mcp.sutra.example@evil.test/` has a
  `netloc` that starts with the trusted name (4.1).
- **`accept` in URL mode means consent to open, not completion** (4.1).
- **Never ask for a credential in form mode.** `format: password` is a rendering hint; the value is
  plain text in the retry body (4.2).
- **A consent link can be forwarded.** The connect route reads the identity from the **session**,
  never from the URL (4.3).
- **Extensions are off unless both sides named them**, and a breaking change to one gets a new
  identifier rather than a version field (5.1).
- **Policy on declarations is not enforcement.** A party that declares nothing and does it anyway is
  caught by an audit log, not by the identity provider (5.3).
- **The real revocation window is the access token's lifetime, not zero** — for offboarding and for a
  newly denied extension alike (5.2, 5.3).
- **`git rm --cached .env` does not remove it from history.** Rotation is the only fix (6.1).
- **Grepping for the bare string `iss` matches `issuer`.** A measurement that returns the comfortable
  answer for a mechanical reason is worse than no measurement (6.2).

---

## §8 Verify before you code

Fetched or run on **2026-09-04**, the day this was written.

**The specification — the freshness gate (Principle 14):**

- `https://modelcontextprotocol.io/specification/versioning` — the current revision is still
  **2026-07-28**. **It has not moved.** No amendment required.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization` — the roles, the
  normative reference list (OAuth 2.1 draft 13, RFC 6750, RFC 8414, RFC 7591, RFC 8707, RFC 9728,
  RFC 9207, the CIMD draft, OpenID Connect Discovery), the **four-row `iss` table** quoted verbatim in
  2.1, the "MUST NOT normalise" sentence in 2.2, the `resource` parameter rules, the canonical URI
  examples, the audience-validation and token-passthrough MUSTs in 1.3, the 401/403/400 status table,
  the `insufficient_scope` example, the step-up flow, and the stdio **SHOULD NOT** rule.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration` —
  the three registration mechanisms and their priority order, the CIMD client and server requirements,
  the example metadata document reproduced in 2.3, `client_id_metadata_document_supported`, the
  **deprecation warning on Dynamic Client Registration**, and the authorization-server-binding rule
  that CIMD identifiers are portable and registration credentials are not.
- `https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation` — the two modes, the
  capability declaration shape, the `requestedSchema` restrictions and the five permitted field kinds
  in 3.2, the three response actions in 3.3, the form and URL examples, the credential **MUST NOT** in
  4.2, the seven client URL rules and four server URL rules in 4.1, the external-authorization
  pattern, and the **phishing** section whose same-user requirement is 4.3.
- `https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr` — `InputRequests`,
  `InputResponses`, `InputRequiredResult`, the three supported client requests, the eight server
  requirements and four client requirements, and the **replay list** (principal, TTL, method plus a
  digest of salient parameters) that 3.4 implements field for field.
- `https://modelcontextprotocol.io/extensions` — the identifier format, the official
  `io.modelcontextprotocol` prefix, the negotiation shape on both sides, *"extensions are always
  disabled by default"*, the independent-versioning and breaking-change rules, and graceful
  degradation.
- `https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization` — the exact
  identifier `io.modelcontextprotocol/enterprise-managed-authorization`, the four enterprise problems,
  the **ID-JAG** (Identity Assertion JWT Authorization Grant) exchange, the five client obligations,
  the three authorization-server obligations, and the subject-then-email account-linking rule.

**The installed package — the authoritative API surface, read rather than guessed:**

- `.venv/Lib/site-packages/mcp/types.py` — `ElicitRequestFormParams`, `ElicitRequestURLParams`,
  `ElicitResult` with `action: Literal["accept", "decline", "cancel"]`, `ElicitationCapability` with
  `form` and `url`, `ElicitationRequiredErrorData`, `ElicitCompleteNotification`, and
  `URL_ELICITATION_REQUIRED = -32042`. **No `InputRequiredResult`, no `requestState`, no
  `ExtensionCapability`.** `LATEST_PROTOCOL_VERSION = "2025-11-25"`.
- `.venv/Lib/site-packages/mcp/server/elicitation.py` — `AcceptedElicitation[T]`,
  `DeclinedElicitation`, `CancelledElicitation`, and `_validate_elicitation_schema`, which refuses any
  non-primitive field before a request is sent.
- `.venv/Lib/site-packages/mcp/server/session.py` and `mcp/server/fastmcp/server.py` — `elicit`,
  `elicit_form`, `elicit_url` on the session, and `ctx.elicit(message, schema)` /
  `ctx.elicit_url(message, url, elicitation_id)` on the FastMCP context.
- `.venv/Lib/site-packages/mcp/server/auth/provider.py` — `TokenVerifier`, a protocol with one method
  `async def verify_token(self, token: str) -> AccessToken | None`, and `AccessToken` carrying
  `token`, `client_id`, `scopes`, `expires_at`, `resource` (documented as the RFC 8707 resource
  indicator), `subject` and `claims`.
- `.venv/Lib/site-packages/mcp/server/auth/middleware/bearer_auth.py` — `BearerAuthBackend` and
  `RequireAuthMiddleware`, which builds the `WWW-Authenticate` value from a `resource_metadata_url`.
- `.venv/Lib/site-packages/mcp/client/auth/oauth2.py` and `mcp/client/auth/utils.py` —
  `client_metadata_url`, `is_valid_client_metadata_url`, `should_use_client_metadata_url`,
  `extract_resource_metadata_from_www_auth`, `build_protected_resource_metadata_discovery_urls`, and
  `OAuthRegistrationError` / `OAuthFlowError`. **No `iss` handling anywhere**: the callback handler is
  typed `Callable[[], Awaitable[tuple[str, str | None]]]` — code and state, with no third slot.

That measurement is 6.2's subject, run as `lab/sdk_surface.py`, and its result is **6 of 10 present,
4 absent**. **The pin was not changed.** Day 32 already recorded that PyPI's `mcp` is at `2.1.1` and
speaks `2026-07-28`; that remains a plan decision with a `docs/PACKAGES.md` row behind it, not a
day's decision.

**The paper:**

- `doi:10.17487/RFC9207` was assigned with its row already in `docs/PAPERS.md`, verified against the
  RFC Editor record on 2026-09-04. The document itself is at `https://www.rfc-editor.org/rfc/rfc9207`,
  and its §2.4 is what the four-row table in 2.1 and the paper part restate.
- `doi:10.17487/RFC6749`, `doi:10.17487/RFC9700` and `doi:10.17487/RFC9728` are named in prose only.
  All three already have rows; none is taught here.

**No ADK symbol is used anywhere in this day.** Authorization and elicitation are protocol subjects,
and the ADK's MCP surface is a toolset wrapper — it arrives again on Day 39.

---

## §9 Say it in an interview

"Our MCP server was a process on a laptop, so 'anyone may call this tool' meant 'I may call this
tool'. The day it goes on a network, three questions arrive together, and they turned out to be one
question — who is allowed to decide — asked at three different distances.

The first is who is calling. The server never checks a password; it's an OAuth resource server, so it
validates a token somebody else issued. Three checks in order: the issuer we trust, the audience —
that the token names *us* — and the scope. The audience one is the interesting one, because it has no
failing test case. Take it out and every test passes; all you've done is make any service that trusts
the same issuer into a key for this one. The related rule is that we never forward a token we were
given to an upstream API. That's token passthrough and the spec forbids it by name.

The 2026 hardening added two things. RFC 9207 issuer identification: a client that talks to more than
one authorization server can be steered into starting a flow at an attacker's server, get forwarded to
the honest one where the user really logs in, and then post the honest authorization code to the
attacker's token endpoint — because nothing in the response said who sent it. The fix is an `iss`
parameter and a comparison against the issuer you recorded before you opened the browser, done before
the code is transmitted. We built it as a demo with two servers on loopback: check on, zero token
requests sent; check off, the attacker holds the code. And the comparison has to be strict — the spec
forbids case folding, trailing-slash and default-port normalisation, and we measured why: three
reasonable tidy-ups took one accepted issuer to five. The second hardening is Client ID Metadata
Documents replacing Dynamic Client Registration. Your `client_id` is an HTTPS URL you host, the
authorization server fetches it and checks the `client_id` inside equals the URL it fetched from.
Identity you host beats identity you beg for: it's portable across every issuer and there are zero
registration writes.

The second question is whether a server can ask the human something mid-call. Since the 2026 revision
it can't interrupt — server-initiated requests were removed, and that's called out as a breaking
change. Instead it returns a *successful* result whose `resultType` is `input_required`, carrying the
questions and an opaque `requestState`, and the client re-sends the same call with a new JSON-RPC id,
the answers, and the state echoed back. The point is that the retry can land on a different instance,
so there's no session store. The state passes through the client, so the spec says treat it as
attacker-controlled: sign it, and put the authenticated principal, a short TTL and a digest of the
original parameters inside — three fields that stop three specific replays. What I'd flag in review is
the three-action model: accept, decline, cancel. Decline and cancel look the same and mean opposite
things about the future, and folding them together builds a tool that nags people who already said no.

The nastiest part of elicitation is that a server that can ask a question can ask for a password. The
spec has a hard MUST NOT on that in form mode — the value goes through the client's memory, the retry
body, whatever logs it, and potentially the model's context, and models repeat their context. Secrets
go through URL mode, where the user types into a page on our own domain. And URL mode has its own
sting: the link can be forwarded. If somebody sends it to a colleague, the colleague authorizes with
*their* vendor account and the token gets bound to the sender's identity. That's an account takeover
where the victim did all the work, so the server must check that the browser session's subject matches
the subject the elicitation was minted for — and it has to read that from the session, not from the
URL, because the attacker can edit the URL.

The third question is who decides for everybody. Everything beyond MCP's core is now a named,
versioned extension declared in `_meta` on every request, disabled unless both sides name it. That
gives an enterprise a vocabulary: allow this server, deny in-chat UI everywhere, grant scopes by
group. The Enterprise-Managed Authorization extension puts the decision at the identity provider —
the client exchanges its login for an ID-JAG, an Identity Assertion JWT Authorization Grant, and
policy is evaluated at *that* exchange, so an unauthorized employee never receives a token at all. The
honest caveats are that you've made the identity provider a single point of failure for every MCP
call, that the real revocation window is the access token's lifetime rather than zero, and that
governance on declarations is not enforcement — a party that declares nothing and does it anyway is
caught by an audit log, not by policy.

The most useful thing we found was accidental. We ran ten checks against the SDK pinned in our repo
and got a split nobody predicted: elicitation is fully there, both modes and the three-action result;
the 2026 carriage isn't; CIMD is there; and the RFC 9207 `iss` check isn't — the OAuth callback
returns code and state with no third slot for the issuer. Four years after the RFC, in a spec that
makes the check a MUST, it's still something you write yourself. And the trap was in the measurement:
grep for the bare string `iss` and you get a false positive off the word `issuer`, and a check that
returns the comfortable answer for a mechanical reason is worse than not checking. The habit I took
away is that six of this day's mechanisms fail with no error message at all, so we ended it with a
seven-question written form — which issuer, which canonical URI, which scopes, where the token comes
from, which elicitation modes, where the signing key lives, and who reviewed it by name — that starts
red and is a build failure until somebody decides."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 37` is green. Defined by
understanding and green checks, never by elapsed time — a part is finished when you could explain it
to someone else without the page open.

**Phase 5's gate** is `sutra-mcp` serving tools statelessly, at Day 38. Today closes the permission
half: you can say who is calling and prove it, ask a human a question without holding a connection,
keep a credential off every path a model can read, and explain to a security team how an organisation
turns a capability off centrally. Day 38 breaks all of it on purpose and migrates the three deprecated
client features onto the `InputRequiredResult` pattern you built in section 3.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 37 | <date> | MCP-13, MCP-27, MCP-30 | 19 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and nothing upgraded: `mcp` stays at
`1.29.1`, `google-adk` at `2.7.1`, and `gemini-3.7-flash` stays pinned as recorded on 2026-08-26. The
finding that four of this day's ten mechanisms are absent from the pinned SDK is recorded in §8 and in
part 6.2; it is not a row until something is installed.

**`docs/PAPERS.md`** — **no new rows.** `doi:10.17487/RFC9207` already has its dated row and is taught
here in [`papers/01-issuer-identification.md`](papers/01-issuer-identification.md).
`doi:10.17487/RFC6749`, `doi:10.17487/RFC9700` and `doi:10.17487/RFC9728` also have theirs and are
named in prose only, never taught.

**`docs/SKILL_PROVENANCE.md`** — no new rows. No skill was added or changed.

**The commit:**

```text
day 37: auth and enterprise - badges, questions and policy - closes MCP-13, MCP-27, MCP-30
```

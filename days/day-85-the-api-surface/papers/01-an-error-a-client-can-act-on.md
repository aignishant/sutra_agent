---
day: 85
paper: "doi:10.17487/RFC9457"
title: "An error a client can act on"
ids: ["ADK-65"]
level: production
prerequisites: ["../parts/03-when-it-refuses/3.1-one-field-two-types.md"]
prev: "../parts/05-in-production/5.2-what-a-real-api-surface-adds.md"
next: "../LESSON.md"
---

# Paper 01 — An error a client can act on

> **Problem Details for HTTP APIs**
> RFC Editor, 2023. `doi:10.17487/RFC9457`. Obsoletes RFC 7807.
>
> The contribution: one media type, `application/problem+json`, and a small object with five
> defined members — `type`, `title`, `status`, `detail`, `instance` — plus any extension members an
> API needs. `type` is a URI identifying the *kind* of problem, and it is the field a client is meant
> to branch on.

## One-line answer

HTTP has a rich vocabulary for *what went wrong at the protocol level* and nothing at all for *what
went wrong in your application*, so every API invented its own error body — and this document is the
field's agreement to stop, in one page of normative text.

## The story

Every airline's baggage claim form, before anybody agreed on one.

A bag goes missing on a journey with two carriers. The first airline's form has a box for
`REASON CODE`. The second has a free-text field headed `Description of incident`. The handling agent
at the airport has a third system with a dropdown of eleven options, none of which is "transferred to
a flight that had already left".

Nobody is being obstructive. Each form was designed by people who knew their own operation well, and
each is perfectly adequate on its own. The traveller's bag is somewhere in the gap between them,
because the only thing that could have followed it across is a code all three understood, and there
was not one.

That was the state of HTTP API errors for about twenty years. Every service had a sensible error
format. No two were the same, so every client wrote a new one.

## The idea in plain language

The problem the field had is easy to state and was surprisingly durable.

HTTP status codes are excellent at their job and their job is narrow. `404` means the resource is not
there. It does not distinguish *"no such ticket"* from *"no such customer"* from *"the ticket exists
but not for you"*, and those three send a user to three different screens. `409` is worse: a conflict
could be a duplicate, a version mismatch, or a business rule.

So every API added a body. And because there was no agreement about that body, each one chose:

```text
  {"error": "not_found"}
  {"error": {"code": 4041, "message": "..."}}
  {"errors": [{"status": "404", "title": "..."}]}
  {"detail": "..."}                                  <- this server, part 3.1
  {"message": "...", "success": false}
```

A client talking to four services writes four parsers. A client library generator cannot help,
because the shape is not in the schema. And — the part that costs real money — the *identifier* is
usually absent altogether, so callers end up matching on English, which breaks the day somebody
improves the wording.

What this document adds is small and specific:

- **A media type.** `application/problem+json`, so a client can tell a problem document from any
  other JSON without guessing.
- **`type`** — a URI naming the kind of problem. It is an **identifier**, not a link to fetch. This
  is the whole contribution: the stable thing a client compares.
- **`title`** — a short human summary of that *kind*, which does not change per occurrence.
- **`status`** — the HTTP status, repeated in the body so a document that has been logged or
  forwarded is still self-describing.
- **`detail`** — human-readable explanation of *this* occurrence, explicitly not for branching.
- **`instance`** — a URI identifying this occurrence, so a support conversation has a handle.
- **Extension members** — any additional fields the API wants, which is where the ticket number, the
  amount and the limit go.

It also says the thing everybody skips: consumers must not treat `type` as fetchable, and must
tolerate `type` values they have never seen.

## Why Sutra needs it

Because part [3.1](../parts/03-when-it-refuses/3.1-one-field-two-types.md) measured this exact
problem in the server the desk is about to be built on: one field called `detail`, a `str` on three
routes and a `list` on a fourth, and a client that crashed with `AttributeError` on the fourth. And
part [3.2](../parts/03-when-it-refuses/3.2-the-404-that-reads-out-the-disk.md) measured the other
half — a `detail` string carrying the server's filesystem path, because when the body is whatever the
exception said, it is whatever the exception said.

And because Phase 14 puts other agents on the far side of this API. An agent handling a refusal has
the traveller's problem from the story: it can read the prose, and a decision made by reading prose is
a decision that changes when somebody edits a sentence.

## The mechanism

The method, written out rather than paraphrased. A problem document is a JSON object served as
`application/problem+json`, and the five members do different jobs on purpose:

| Member | Stable across occurrences? | Who reads it | What it is for |
| --- | --- | --- | --- |
| `type` | **yes** — this is the contract | the client's code | choosing a branch |
| `title` | yes, per `type` | a person, in a UI | a heading |
| `status` | yes, per `type` | both | matching the HTTP status when the document is separated from it |
| `detail` | **no** — varies per occurrence | a person | explaining this one |
| `instance` | no | support, logs | identifying this occurrence |

Three rules follow, and each one is a mistake somebody makes:

**`type` is an identifier, not a URL to fetch.** Using a URI gives it a namespace — your domain
guarantees uniqueness — and the document is explicit that a consumer must not dereference it. An API
whose error handling depends on a documentation site being up has put a web page in the failure path
of failures.

**Unknown `type` values must be tolerated.** A server may add a new kind of problem at any time, and
a client that has not been updated must degrade to the status code rather than break. That is what
makes the scheme extensible without a version negotiation.

**Extension members carry the machine-usable specifics.** The limit that was exceeded, the field that
was invalid, the identifier that was not found. This is the part that turns a refusal into something a
client can *render* — showing the user the actual limit — rather than merely route.

What the document deliberately does not do: it defines no `type` values, no error taxonomy, no
registry of codes. That omission is the reason it was adoptable. A standard that had tried to
enumerate application errors would have had to be right about every domain, and would have been
ignored.

## The paper in one demo

A small end-to-end project implementing the paper's contribution and nothing else: one route, two
kinds of refusal, one client that must send each to a different screen.

```text
days/day-85-the-api-surface/lab/papers/problem-details/
├── api.py    # one route that refuses two ways; problem_details=True|False is the only switch
└── demo.py   # the client, and the ablation
```

The refusals are the desk's own, from Day 63's approval work:

```python
NO_SUCH_TICKET = "https://sutra.example/errors/no-such-ticket"
OVER_LIMIT = "https://sutra.example/errors/refund-over-limit"
```

**Line by line:**

- Two URIs under a domain the API would own. They are identifiers; nothing fetches them, and
  `sutra.example` does not resolve on purpose — a reader who tries will find that the demo does not
  care, which is the point.
- Two constants rather than strings inline, so the server and the client's routing table refer to the
  same object and a typo is an `ImportError` rather than a silent mismatch.

The refusal carries its identity:

```python
class DeskError(HTTPException):
    """A refusal that knows which kind of refusal it is."""

    def __init__(self, status: int, type_: str, title: str, detail: str, **extra):
        super().__init__(status_code=status, detail=detail)
        self.type_ = type_
        self.title = title
        self.extra = extra
```

**Line by line:**

- Subclassing `HTTPException` rather than inventing a parallel hierarchy, so anything already
  handling framework exceptions keeps working and adoption can be incremental.
- `type_` with a trailing underscore because `type` is a builtin. A small ugliness in exchange for the
  field name matching the standard exactly where it is serialised.
- `**extra` collects the extension members at the raise site, which is the only place that knows them
  — the amount and the limit are in scope exactly there and nowhere else.
- `detail` still goes to the parent, so the framework's default rendering is *also* correct. That is
  what makes the ablation a fair comparison: turning the handler off does not break the app, it just
  removes the standard.

The client's whole decision:

```python
ROUTE_TO = {NO_SUCH_TICKET: "search screen", OVER_LIMIT: "approval queue"}


def decide(status: int, content_type: str, body: dict) -> str:
    if content_type.startswith("application/problem+json"):
        return ROUTE_TO.get(body.get("type"), "unknown refusal")
    return "unknown refusal"
```

**Line by line:**

- `status` is a parameter and is never used. That is the demo's sharpest claim: the routing does not
  need the status code, so two refusals sharing one would still be told apart.
- `content_type.startswith(...)` rather than equality, because the header may carry a charset
  parameter. Checking the media type first is also what lets an API adopt the standard route by route.
- `ROUTE_TO.get(..., default)` — an unknown `type` degrades to "unknown refusal" instead of raising,
  which is the tolerance rule the document requires.

Run it:

```bash
cd days/day-85-the-api-surface/lab/papers/problem-details
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- No flag: the exception handler is registered and the refusals are problem documents.

Measured on 2026-09-07:

```text
errors as: application/problem+json

  a ticket that does not exist
    404 application/problem+json
    {"type": "https://sutra.example/errors/no-such-ticket", "title": "No such ticket", "status": 404
    the client sends this to: search screen

  a ticket over the refund limit
    409 application/problem+json
    {"type": "https://sutra.example/errors/refund-over-limit", "title": "Refund over the desk limit"
    the client sends this to: approval queue

  refusals the client could route: 2 of 2
  each refusal carries a stable identifier, so the branch is on a value
exit: 0
```

Now the ablation — the same app with the handler removed and nothing else changed:

```bash
uv run python demo.py --off; echo "exit: $?"
```

**Line by line:**

- `--off` passes `problem_details=False` to the same `build()`. The routes, the refusals, the status
  codes and the wording are identical.

Measured on 2026-09-07:

```text
errors as: the framework default

  a ticket that does not exist
    404 application/json
    {"detail": "There is no ticket numbered 0001."}
    the client sends this to: unknown refusal

  a ticket over the refund limit
    409 application/json
    {"detail": "Ticket 4688 is for 2400, over the limit of 1000."}
    the client sends this to: unknown refusal

  refusals the client could route: 0 of 2
  the client cannot tell the two refusals apart without reading the prose
  a wording change on the server would silently reroute a customer
exit: 1
```

**Two of two, against zero of two.** Read the ablation's bodies as a person and they are *better* than
the problem documents — shorter, plainer, complete sentences. Read them as a client and there is
nothing to branch on but English.

That is the contribution isolated: the information was never missing, and it was never addressable.

## When it breaks

**Where the claim does not hold: errors you do not produce.** A gateway's `429`, a proxy's `502`, a
load balancer's `503`, a TLS failure — none of these will be problem documents however thoroughly
your application adopts the standard. That is why the demo's `decide()` checks the media type first
rather than assuming. A client written as though every error were a problem document breaks on the
first infrastructure failure, which is the one that happens during an incident.

**Where it is misapplied: `type` as documentation.** Teams make the URI resolve, then start treating
the page as the specification, then find a client that fetches it. The document says consumers must
not dereference; the failure mode when they do is a documentation site in the error path.

**Where it does nothing: the taxonomy.** The standard gives you a slot for an identifier and no help
choosing identifiers. A team that adopts the format and invents fifty overlapping `type` values has a
standard-compliant mess — better than before, because at least it is machine-readable, and still a
mess. The hard part was always the vocabulary and this document does not address it, deliberately.

**And a caution about the framework's own errors.** Part
[3.1](../parts/03-when-it-refuses/3.1-one-field-two-types.md) measured that FastAPI's validation
failures are generated before application code runs. Adopting the standard for your own raises and
not for validation leaves the most frequent error in production in the old shape — two shapes again,
which was the original complaint.

## In production

**What survived.** The media type and `type`-as-identifier, almost universally. `application/
problem+json` appears in cloud provider APIs, in public-sector API guidance, in .NET's default error
responses, and in a long list of internal standards that cite it rather than reinvent. The core idea —
a stable machine-readable identifier separate from human-readable prose — has become the default
expectation for a new API, which is as complete an adoption as a document like this gets.

**What did not.** Two things. The `instance` member is widely omitted, because teams already have a
request id in a header and see no reason to repeat it in a URI. And `type` almost never resolves in
practice, despite the amount of argument spent on whether it should — the field converged on treating
it as an opaque namespaced string, which is what the document permits and not what its examples
suggest.

**What it means for this repository, concretely.** This server currently produces two error shapes
(part 3.1) and leaks a filesystem path in one of them (part 3.2). Adopting the standard is item 5 of
part [5.2](../parts/05-in-production/5.2-what-a-real-api-surface-adds.md)'s eight, and it fixes both
at once — because a constructed body cannot leak a message nobody chose to include, and a single
handler cannot produce two shapes.

**The review comment a senior engineer leaves:** *"Adopt it, and do the validation-error handler in
the same change. Keep the `type` list in one module and review additions to it like any other
interface change — the format is the easy half, the vocabulary is the half we will live with."*

**The interview question:** *"How should an API report application errors?"* The answer that shows
experience names a standard rather than a house style, then says which field is contractual and which
is not — and the tell is whether they mention that infrastructure errors will never comply, because
that is the sentence you only write after a client broke during an outage.

## Check yourself

```bash
cd days/day-85-the-api-surface/lab/papers/problem-details
uv run python demo.py; echo "exit: $?"
uv run python demo.py --off; echo "exit: $?"
```

Two of two against zero of two, from bodies a person would say are equally clear. State, in one
sentence, what the client has in the first run that it does not have in the second.

Now reword both `detail` strings in `api.py` completely and re-run both arms. One arm's behaviour is
unchanged and one arm was never going to notice, because it was already failing. Say what that
demonstrates about branching on prose.

Then add a third refusal — a ticket already refunded — with its own `type`, and add it to `ROUTE_TO`.
Now remove it from `ROUTE_TO` only, and predict what the client does before you run it.

**Out loud, without scrolling up:** name the five members, say which one a client may branch on, and
name the class of errors that will never arrive in this format however well you adopt it.

**Next:** back to the hub — [`LESSON.md`](../LESSON.md).

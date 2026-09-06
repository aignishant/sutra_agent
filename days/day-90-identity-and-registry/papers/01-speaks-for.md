---
day: 90
paper: "doi:10.1145/121132.121160"
title: "Speaks for — authentication as a chain of statements"
ids: ["AG-29"]
level: production
prerequisites: ["../parts/04-verified-is-not-authorised/4.2-the-shared-login.md"]
prev: "../parts/05-in-production/5.3-the-one-road-into-town.md"
next: "../LESSON.md"
---

# Paper 01 — Speaks for: authentication as a chain of statements

> **Authentication in distributed systems**
> Proceedings of the thirteenth ACM symposium on operating systems principles, 1991, pages 165–182.
> `doi:10.1145/121132.121160`
>
> The claim this day borrows: authenticating a request in a distributed system is not one check. It is
> a **chain of statements**, each of the form *A speaks for B*, and the request is authorised only when
> an unbroken chain runs from whoever signed it to a principal the resource already trusts.

## One-line answer

Once a request can arrive on behalf of somebody who is not the sender, "who signed this" stops being
the question — the question is whether a path of delegations connects the signer to someone you trust,
and what the narrowest permission along that path is.

## The story

The call that came through three departments.

You ring a large organisation about a bill. The switchboard sends you to accounts. Accounts listens,
says this is really a metering question, and transfers you. Metering listens, says they can see the
problem but the adjustment has to be authorised by billing, and transfers you again.

The person in billing picks up and says: *"Metering asked me to call you about the September
reading."*

Notice what you now believe, and why. You have never met this person. Nothing about their voice proves
anything. What you are relying on is a chain — the switchboard vouched for accounts, accounts handed
you to metering, metering handed you to billing — and every link was somebody inside the organisation
passing you along with a note about why.

Notice also what the chain does **not** give them. Metering asked them to sort out a meter reading. It
did not ask them to close your account, and if they offered to, the chain would be exactly as intact
and the offer exactly as wrong.

## The idea in plain language

The paper is about authentication in a distributed system, at a moment when "distributed" was becoming
the normal case rather than the exotic one. Its central move is to stop treating authentication as a
yes-or-no check on a caller and start treating it as **reasoning about statements**.

The relation it introduces is written *A speaks for B*, and it means: anything A says may be treated as
though B said it. A user's workstation speaks for the user. A process speaks for the account that
started it. A service acting on a user's behalf speaks for that user, within limits.

Three consequences follow, and they are the whole of what this day borrows.

**Authentication becomes a path, not a point.** When a request arrives signed by some key, the question
is not *is this key trusted* but *is there a chain of speaks-for statements from this key up to a
principal I already trust*. A key nobody has delegated to is a stranger no matter how valid its
signature.

**Delegation is a first-class thing you can write down.** Rather than a service holding permissions
broad enough to cover everyone it might act for, it holds a *statement* from each principal it acts
for. This is the direct answer to part
[4.2](../parts/04-verified-is-not-authorised/4.2-the-shared-login.md)'s union problem: the peer's own
grant stays narrow, and authority for a specific action arrives with the specific request.

**Scope narrows along the chain and never widens.** If A grants B two permissions and B delegates one
of them to C, then C has one. The intersection is taken along the path, so no participant can hand on
more than it holds — which is what stops a chain from being a way to accumulate authority.

The compound principal notation the paper builds on top of this — a request being from *the workstation
acting for the user in role X* — is the part that has aged into a specialist topic. The relation itself
has not.

## Why Sutra needs it

Because Sutra's peers act for people. A peer that says *"refund ticket 4688"* is not asking on its own
behalf; some human or some upstream system wanted that. Part
[4.2](../parts/04-verified-is-not-authorised/4.2-the-shared-login.md) measured what happens when that
is ignored — the peer's registry grant has to cover the most privileged requester it will ever act for,
and then covers everyone else's requests too.

And because Sutra will delegate outward as well. The desk hands work to a peer; that peer may hand part
of it to another. Day 55's contract-net delegation and Day 57's orchestrator both create chains of
exactly this shape, and until now nothing in the repository could express *"this sub-agent is acting for
the desk, for this ticket, and may only read"*.

## The mechanism

The paper's method, written out as the thing to implement rather than paraphrased.

**A statement is a triple.** Speaker, subject, scope. *A says B speaks for me, limited to these
actions.* In a real system each is signed by its speaker, which is why this day's earlier sections had
to come first — a delegation statement is only as good as the identity of whoever issued it.

**Authorisation is a search.** Given a request signed by some principal, walk from that principal
towards the trusted one, following statements. If no path exists, refuse. The search is a graph walk
and it must handle a cycle, because a delegation loop is a thing people create by accident.

**Scope is the intersection along the path.** Collect the scope of every link and intersect them. The
result is what this signer may do while acting for the trusted principal — never more than the
narrowest link.

**Every link must be checked.** The paper is emphatic about this and it is the part most often skipped:
a chain is only as good as its weakest verification, and a system that checks the first hop and assumes
the rest has checked nothing.

Written out, that is the whole algorithm:

```python
    def walk(current: str, seen: frozenset[str]) -> list[Says] | None:
        if current == principal:
            return []
        for statement in by_subject.get(current, []):
            if statement.speaker in seen:
                continue  # a delegation loop is not a chain
            rest = walk(statement.speaker, seen | {statement.speaker})
            if rest is not None:
                return [statement] + rest
        return None
```

**Line by line:**

- `current == principal` is the base case: the walk has reached somebody the resource already trusts,
  and returns an empty chain, meaning *no delegation was needed*. A request signed directly by the
  trusted principal takes this branch immediately.
- `by_subject` indexes statements by their **subject**, so the walk runs from the signer upwards
  towards the trusted root. Indexing by speaker and walking down would enumerate everything the root
  ever delegated, which is the same answer computed the expensive way.
- `statement.speaker in seen` is the cycle guard, and it is not defensive programming. Two services
  that each delegate to the other is an ordinary configuration mistake, and without this line it is a
  stack overflow rather than a refusal.
- `seen | {statement.speaker}` passes a new frozenset down rather than mutating one, so a failed branch
  does not poison a sibling branch — with a shared mutable set, a principal ruled out on one path would
  be unreachable on every other.
- The return type is `list[Says] | None`, not `bool`. The **chain itself** comes back, because the
  caller needs it to intersect the scopes — and because a refusal that can name the missing link is
  worth far more than one that says no.

And the intersection, which is the part that makes a chain safe rather than merely connected:

```python
    narrowed: frozenset[str] | None = None
    for link in links:
        narrowed = link.scope if narrowed is None else (narrowed & link.scope)
    if narrowed is not None and request.action not in narrowed:
        return False, f"chain of {len(links)} narrows to {sorted(narrowed)}"
```

**Line by line:**

- `narrowed` starts as `None` rather than as a set of everything, because "no links" and "links that
  permit nothing" are different situations. A zero-length chain — the trusted principal signing for
  itself — must not be narrowed by an empty intersection.
- `narrowed & link.scope` — intersection, every time. There is no operation in this loop that can make
  the set larger, which is the property being enforced.
- The refusal message reports the chain length and what it narrowed to, so the answer to *"why can this
  agent not do that"* is one line rather than an investigation.

## The paper in one demo

A small end-to-end project implementing the speaks-for chain and nothing else. Five statements, six
requests, and a switch that turns delegation off.

```text
days/day-90-identity-and-registry/lab/papers/speaksfor/
├── chain.py   # Says, Request, the walk, and the scope intersection
└── demo.py    # five statements, six requests, and what a person says about each
```

`chain.py` holds the two types and the algorithm above. `demo.py` holds the world:

```python
STATEMENTS = (
    Says("sutra-desk", "refund-desk", frozenset({"read_ticket", "propose_refund"})),
    Says("refund-desk", "refund-worker-7", frozenset({"read_ticket", "propose_refund"})),
    Says("refund-desk", "audit-reader", frozenset({"read_ticket"})),
    Says("billing-desk", "billing-worker-2", frozenset({"move_money"})),
    Says("audit-reader", "audit-worker-1", frozenset({"read_ticket"})),
)
```

**Line by line:**

- The first statement is the desk delegating to a peer — the case part
  [4.1](../parts/04-verified-is-not-authorised/4.1-the-man-the-office-sent.md) handled with a registry
  grant. Here the same fact is a statement that can be delegated onward, which is the difference.
- The third narrows: `audit-reader` gets `read_ticket` only, out of the two `refund-desk` holds. That
  is the intersection having something to bite on.
- The fourth is deliberately disconnected. `billing-desk` never appears as a subject of anything, so
  nothing it delegates reaches `sutra-desk` — a whole subtree of perfectly valid statements that
  authorise nothing here.
- The fifth makes a three-hop chain, so the demo tests a path longer than the one everybody draws on
  the whiteboard.

There is no crypto anywhere in the demo, and that is the isolation the paper's contribution needs:
every signature is assumed already checked, so what is being measured is the *reasoning* and not the
verification.

Run it:

```bash
cd days/day-90-identity-and-registry/lab/papers/speaksfor
uv run python demo.py; echo "exit: $?"
```

**Line by line:**

- No flag: delegation followed, which is the paper's condition.

Measured on 2026-09-07:

```text
trusted principal: sutra-desk
statements: 5
delegation: followed

  signer            action          want   got    why
  sutra-desk        read_ticket     True   True   chain of 0, scope []
  refund-desk       propose_refund  True   True   chain of 1, scope ['propose_refund', 'read_ticket']
  refund-worker-7   propose_refund  True   True   chain of 2, scope ['propose_refund', 'read_ticket']
  audit-worker-1    read_ticket     True   True   chain of 3, scope ['read_ticket']
  audit-worker-1    propose_refund  False  False  chain of 3 narrows to ['read_ticket']
  billing-worker-2  move_money      False  False  no chain from billing-worker-2 up to sutra-desk

  6 of 6 requests decided the way a person would
  every hop was followed and every scope intersected along the way
exit: 0
```

**Six of six.** Read the fourth and fifth rows together: the same signer, three hops from the trusted
principal, allowed to read and refused to propose a refund — because `audit-reader` was only ever given
`read_ticket`, and the intersection carried that restriction two hops further down to a worker
`audit-reader` delegated to.

## When it breaks

Turn delegation off, so only a direct signature counts:

```bash
uv run python demo.py --off; echo "exit: $?"
```

Measured on 2026-09-07:

```text
delegation: OFF - direct signature only

  signer            action          want   got    why
  sutra-desk        read_ticket     True   True   signed directly by the trusted principal
  refund-desk       propose_refund  True   False  signer is refund-desk, not the trusted principal   <- disagrees
  refund-worker-7   propose_refund  True   False  signer is refund-worker-7, not the trusted principal   <- disagrees
  audit-worker-1    read_ticket     True   False  signer is audit-worker-1, not the trusted principal   <- disagrees
  audit-worker-1    propose_refund  False  False  signer is audit-worker-1, not the trusted principal
  billing-worker-2  move_money      False  False  signer is billing-worker-2, not the trusted principal

  3 of 6 requests decided the way a person would
  3 disagree: without the chain, a delegate looks like a stranger
exit: 1
```

**Three of six**, and the three it gets right are worth looking at closely, because two of them are
right by accident. Rows five and six are correctly refused — and they are refused for the wrong reason.
The ablation refuses *everything* that is not directly signed, so it happens to agree on the negatives
while having no ability to distinguish them from the positives. A system evaluated only on requests it
should refuse would score this ablation as perfect.

That is the failure the paper's claim addresses: without a chain, **a legitimate delegate is
indistinguishable from a stranger**, and the only two ways out are to refuse all delegates or to widen
the delegate's own permissions until it no longer needs to delegate. The second is what real systems do,
and it is part [4.2](../parts/04-verified-is-not-authorised/4.2-the-shared-login.md)'s union arriving as
a consequence rather than as an accident.

**Where the claim does not hold.** Three places, and they are worth knowing.

The chain assumes every statement is **verified**, not merely present. A system that walks the chain
without checking each link's signature has built a data structure, not a control — and the walk gets
more convincing as it gets longer, which is the wrong direction.

The chain assumes statements can be **withdrawn**, and the paper's model has no good story for that.
This is part [3.2](../parts/03-keys-change/3.2-the-card-of-someone-who-left.md)'s problem multiplied:
revoking one delegation invalidates every chain that ran through it, and finding those chains means
enumerating them.

And the model assumes a **trusted root whose statements are simply believed** — a certification
authority. Part [5.3](../parts/05-in-production/5.3-the-one-road-into-town.md) is why that is the
assumption to be nervous about, and it is the part of the paper the field spent the following decades
finding the limits of.

## In production

**What survived.** The speaks-for relation, essentially intact, under many names. Delegation as a
first-class signed statement is how a modern token exchange works — a service presenting a token that
names both itself and the user it acts for is exactly a compound principal. Scope intersection along a
delegation chain is why a downstream token can never have broader scope than the one it was exchanged
from. The insistence that every link be checked rather than assumed is the argument against the
still-common pattern of validating a caller at the edge and trusting everything behind it.

**What did not.** The formal logic. The paper's notation for reasoning about statements — the algebra
of principals, the inference rules — is a specialist topic, and almost nobody implementing delegation
today writes anything down in it. And the single certification authority at the root of every chain was
the assumption that aged worst: the field replaced it with a small set of roots, then spent a long time
learning that a small set of roots is still a set of roots.

**What it means for this repository, concretely.** Sutra's registry as built in section
[2](../parts/02-the-registry/2.1-the-list-behind-the-counter.md) is a chain of length one: the registry
speaks for itself, and it says what each peer may do. That is a legitimate special case of the paper's
model and it is enough while every peer acts only for itself. It stops being enough the first time a
peer acts for a customer — at which point part
[5.2](../parts/05-in-production/5.2-what-a-real-identity-layer-adds.md)'s parked item 7 becomes the
work, and this demo is the shape it should take.

**The review comment a senior engineer leaves:** *"When we do delegation, verify every link and store
the chain with the decision. A log line saying 'authorised' is worth much less than one saying
'authorised via refund-desk, scope read_ticket' — and when somebody asks in six months why an audit
worker touched a ticket, the chain is the answer."*

**The interview question:** *"Service A calls service B on behalf of a user. How does B decide?"* The
answer that shows experience does not stop at validating A's credentials. It asks what statement
carries the user's authority, whether B verifies that statement itself or trusts A to have done it, and
what the effective permission is when the two disagree — which is the intersection, and is the part
most designs leave undefined.

## Check yourself

```bash
cd days/day-90-identity-and-registry/lab/papers/speaksfor
uv run python demo.py; echo "exit: $?"
uv run python demo.py --off; echo "exit: $?"
```

The ablation gets three of six right. Two of those three are right for the wrong reason — identify
them, and say what that implies about evaluating a permission system only on the things it refuses.

Now add `Says("audit-reader", "audit-worker-1", frozenset({"propose_refund"}))` as a sixth statement,
so `audit-worker-1` has two paths from `audit-reader`. Predict what happens to the fifth request before
you run it. The answer depends on a detail of `walk` that this document has already named.

**Out loud, without scrolling up:** state the speaks-for relation in one sentence, and say what happens
to scope along a chain and why it can only go one way.

**Next:** back to the hub — [`LESSON.md`](../LESSON.md).

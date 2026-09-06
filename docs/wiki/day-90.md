# Day 90 - Agent identity and the registry

IDs closed: AG-29, ADK-71 · source: `days/day-90-identity-and-registry/`

## Parts

### 1.1 - A name is not an identity
`days/day-90-identity-and-registry/parts/01-what-an-identity-is/1.1-a-name-is-not-an-identity.md` · level `foundation` · ids AG-29

The name field in an agent card is something the sender typed about itself, so it can only ever be a claim — the identity is the key, and the name is a label somebody attached to that key.

### 1.2 - The three questions a peer has to answer
`days/day-90-identity-and-registry/parts/01-what-an-identity-is/1.2-the-three-questions.md` · level `foundation` · ids AG-29

Who are you, who says so, and what may you do are three separate questions with three separate answers stored in three different places, and collapsing any two of them into one is the mistake every part of this day is a consequence of.

### 1.3 - What ADK puts in the card, and what it leaves out
`days/day-90-identity-and-registry/parts/01-what-an-identity-is/1.3-the-sticker-anyone-can-print.md` · level `working` · ids ADK-71

AgentCardBuilder produces a card with eight fields, provider and securitySchemes both null and zero signatures — the A2A message type has a signatures field and ADK never fills it, so the card the framework hands you is an introduction with nothing behind it.

### 2.1 - The registry is a file
`days/day-90-identity-and-registry/parts/02-the-registry/2.1-the-list-behind-the-counter.md` · level `working` · ids AG-29

A registry is not a service and not a protocol — it is a record you keep, mapping an identifier to the key you expect, who vouched for it, what it may do and whether it is still active, and every one of those four columns exists because something goes wrong without it.

### 2.2 - Trust on first use, and the swap it is meant to catch
`days/day-90-identity-and-registry/parts/02-the-registry/2.2-the-milkmans-substitute.md` · level `working` · ids AG-29

Pinning the first key you see costs nothing and catches a swap on the third contact, but it accepts whoever turns up first — so it is strictly better than nothing, strictly worse than a registry, and the difference between them is which contact is the dangerous one.

### 2.3 - Two shops, one name
`days/day-90-identity-and-registry/parts/02-the-registry/2.3-two-shops-one-name.md` · level `production` · ids AG-29

Two agents registered under the same display name, both with valid signatures and both legitimately in the registry, and a lookup by name returns the one with move_money in its capability list — because nothing failed, the name was ambiguous, and the lookup had to pick something.

### 3.1 - Rotation — the two rules that pull opposite ways
`days/day-90-identity-and-registry/parts/03-keys-change/3.1-the-cheques-already-written.md` · level `working` · ids AG-29

When a peer changes its key, two things must both stay true — everything it signed before must still verify, and it must no longer be accepted presenting the old key — and satisfying both is why a registry entry needs a previous_keys list rather than a single field.

### 3.2 - The signature that stays valid for ever
`days/day-90-identity-and-registry/parts/03-keys-change/3.2-the-card-of-someone-who-left.md` · level `production` · ids AG-29

A withdrawn peer's signature verifies exactly as well as it did the day it was issued, and always will — so revocation is the one identity fact that cannot live in the credential, and a resolver that checks the signature and stops will admit a peer whose access was removed months ago.

### 4.1 - Verified is not authorised
`days/day-90-identity-and-registry/parts/04-verified-is-not-authorised/4.1-the-man-the-office-sent.md` · level `working` · ids ADK-71

Being certain who a peer is tells you nothing about what it may do, so the capability list on the registry entry has to be consulted on every call — and a system that treats identity as permission lets a correctly-verified refund desk move money.

### 4.2 - One identity for many callers
`days/day-90-identity-and-registry/parts/04-verified-is-not-authorised/4.2-the-shared-login.md` · level `production` · ids ADK-71

A registry entry names one key and one grant, so the moment several callers share that key the grant widens to the union of everything any of them needs — and the entry stops describing a peer and starts describing a category, at which point the capability list has stopped being a limit.

### 5.1 - What a registry costs
`days/day-90-identity-and-registry/parts/05-in-production/5.1-what-a-registry-costs.md` · level `production` · ids AG-29

Every check in this day is arithmetic on bytes already in memory and costs nothing to run for ever — what a registry costs is upkeep, and the bill is paid in stale rows, refused legitimate peers and somebody's attention every time a key changes.

### 5.2 - What a real identity layer adds
`days/day-90-identity-and-registry/parts/05-in-production/5.2-what-a-real-identity-layer-adds.md` · level `production` · ids AG-29, ADK-71

This lab resolves an id, matches a key, verifies a signature, honours a rotation, reads a revocation and checks a capability — and the distance between that and something you would put in front of a peer that can move money is nine items, the first two of which are an afternoon between them.

### 5.3 - The registry as a single point of trust
`days/day-90-identity-and-registry/parts/05-in-production/5.3-the-one-road-into-town.md` · level `production` · ids AG-29

Every check in this day ends at one record kept by one authority, so whoever can write that record can grant themselves any identity and any capability — which makes the registry the most valuable thing in the system and the one component nothing else can check.

## Papers - read after the parts

### doi:10.1145/121132.121160 - Speaks for — authentication as a chain of statements
`days/day-90-identity-and-registry/papers/01-speaks-for.md`

Once a request can arrive on behalf of somebody who is not the sender, "who signed this" stops being the question — the question is whether a path of delegations connects the signer to someone you trust, and what the narrowest permission along that path is.


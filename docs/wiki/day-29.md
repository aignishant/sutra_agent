# Day 29 - Sourcing & auditing third-party skills

IDs closed: SK-12, SK-13, SK-14, SK-15, SK-16 · source: `days/day-29-sourcing-and-auditing-skills/`

## Parts

### 1.1 - The four doors skills come through
`days/day-29-sourcing-and-auditing-skills/parts/01-the-doors/1.1-the-four-doors.md` · level `foundation` · ids SK-12

A skill can reach your agent through four kinds of door — your own repository, the spec organisation's examples, a community collection, or a managed registry — and naming which door a skill came through is the first thing an audit records, because each door tells you something different about who wrote the text and who can still change it.

### 1.2 - Who can change the text after you read it
`days/day-29-sourcing-and-auditing-skills/parts/01-the-doors/1.2-who-can-change-the-text.md` · level `working` · ids SK-12

The property that orders the trust gradient is mutability — whether the exact text you audited can change after you audit it — and the whole reason to pin a skill to an exact revision is to convert a source that can change under you into one that cannot.

### 1.3 - Freshness is not trust
`days/day-29-sourcing-and-auditing-skills/parts/01-the-doors/1.3-freshness-is-not-trust.md` · level `working` · ids SK-12

Star counts, download numbers and a recent last-commit date are freshness signals — they tell you a skill is alive and popular, which is worth knowing — but not one of them is a trust signal, because every one of them can be manufactured and none of them survives a maintainer account being taken over.

### 2.1 - Read it like the thing that will obey it
`days/day-29-sourcing-and-auditing-skills/parts/02-the-five-pass-audit/2.1-read-it-like-the-thing-that-will-obey-it.md` · level `foundation` · ids SK-13

An audit is a full read of a skill by a human, in a fixed cheap-to-expensive order, asking of every line the one question the agent will answer for real — if my agent obeys this literally, what happens? — and it uses zero model calls, on purpose, because the whole point is that nothing untrusted reaches the model until a person has cleared it.

### 2.2 - Pass 1 — will it load, and may you keep it
`days/day-29-sourcing-and-auditing-skills/parts/02-the-five-pass-audit/2.2-pass-one-will-it-load.md` · level `working` · ids SK-13

The first pass is the cheapest and most decisive: does the folder load as a valid skill, is its name the one the folder claims, and does it carry a licence — and if the answer to any of these is no, the audit stops here, because a publisher who cannot manage the frontmatter has not earned a deeper read.

### 2.3 - Pass 2 — the capability inventory
`days/day-29-sourcing-and-auditing-skills/parts/02-the-five-pass-audit/2.3-the-capability-inventory.md` · level `working` · ids SK-13

The second pass lists everything the skill asks permission to do — every tool it pre-approves, every tool it wants the agent to have, every script it can run, and every outbound URL anywhere in its files — so that before you read a word of the body you already know the largest thing this skill could do if you obeyed all of it.

### 2.4 - Pass 3 — reading the body
`days/day-29-sourcing-and-auditing-skills/parts/02-the-five-pass-audit/2.4-reading-the-body.md` · level `working` · ids SK-13

Five sentence shapes account for almost every hostile instruction ever put in a skill — authority, concealment, moving data outward, open-ended scope, and shouting — and a twenty-line scanner can find every line that matches one of them, which narrows a careful read down to a handful of lines without ever deciding anything for you.

### 2.5 - Pass 4 — the files it points at
`days/day-29-sourcing-and-auditing-skills/parts/02-the-five-pass-audit/2.5-the-files-it-points-at.md` · level `working` · ids SK-13

A clean body can point at a file that is not clean, so pass 4 follows every link out of SKILL.md and asks four questions — does the target exist, does it stay inside the skill folder, is it more than one level down, and is there any file the body never points at — because a reference is text that arrives after the body has already been trusted.

### 2.6 - Pass 5 — the scripts, read never run
`days/day-29-sourcing-and-auditing-skills/parts/02-the-five-pass-audit/2.6-the-scripts-read-never-run.md` · level `production` · ids SK-13

A script is the only thing in a skill that executes as code rather than as a request to a model, so it is read last, in full, as a syntax tree — six questions asked of every node, and the script is never executed to find out what it does.

### 3.1 - A skill is source you did not write
`days/day-29-sourcing-and-auditing-skills/parts/03-the-poisoned-skill/3.1-a-skill-is-source-you-did-not-write.md` · level `production` · ids SK-14

Installing a stranger's skill is handing a stranger's text to the component of your system that does what text says, and because that text arrives inside the trusted channel as sanctioned procedure, there is no mid-stream defence — only upstream ones, which is the audit and the pin, and downstream ones, which are least privilege and guardrails.

### 3.2 - 💥 The poisoned skill, and the audit that catches it
`days/day-29-sourcing-and-auditing-skills/parts/03-the-poisoned-skill/3.2-the-poisoned-skill-and-the-audit.md` · level `production` · ids SK-14, SK-13

You build a skill you know is hostile — three planted traps, quarantined under tests/fixtures/ so no agent can ever load it — run the five passes against it, and read the combined report: ten agenda items, verdict REJECT, and the checklist is no longer theatre because you have watched it catch something real.

### 3.3 - 💥 It validated, and it was hostile
`days/day-29-sourcing-and-auditing-skills/parts/03-the-poisoned-skill/3.3-it-validated-and-was-hostile.md` · level `production` · ids SK-14

Mechanical validation and human audit answer different questions — "is this a well-formed skill?" versus "should this agent obey it?" — and only the second is security, which is why the poisoned fixture passes the spec validator cleanly and fails the audit on three counts.

### 4.1 - No row, no run
`days/day-29-sourcing-and-auditing-skills/parts/04-provenance/4.1-no-row-no-run.md` · level `working` · ids SK-15

A third-party skill runs only after its row exists in the provenance ledger — source, version, licence, who audited it and when, and what it is permitted to touch — because the row is the permission, and a rejected audit gets a row too, since a rejected audit is provenance as much as an accepted one.

### 4.2 - The pin is the promise
`days/day-29-sourcing-and-auditing-skills/parts/04-provenance/4.2-the-pin-is-the-promise.md` · level `production` · ids SK-15

A pin is only worth something if something checks it, so the day's drift check hashes the files on disk and compares them to the digest in the ledger row — matching means the audited text is the text that runs, and one changed byte turns it red.

### 5.1 - 🅿️ Search, fetch, and why it is parked
`days/day-29-sourcing-and-auditing-skills/parts/05-the-registry/5.1-search-fetch-and-parked.md` · level `production` · ids SK-16

ADK ships a managed-registry client that lets an agent search for and fetch skills at runtime, which is genuinely useful for an organisation that audits centrally — and it is parked for Sutra, because it needs a billing-account cloud project and, more fundamentally, a runtime fetch delivers text after your last audit, which is the one thing this day's whole model cannot allow.

### 6.1 - Run the pack against the routing gate
`days/day-29-sourcing-and-auditing-skills/parts/06-in-production/6.1-run-the-pack-against-the-routing-gate.md` · level `production` · ids SK-12, SK-13

A sourced pack can pass the security audit clean and still make your shelf worse, because four well-meant, honestly-described skills narrow every routing margin they touch — so a sourced pack is run against Day 28's routing gate before it merges, exactly as Day 28 promised Day 29 would.

### 6.2 - Provenance plus containment, not reading alone
`days/day-29-sourcing-and-auditing-skills/parts/06-in-production/6.2-provenance-plus-containment.md` · level `production` · ids SK-14, SK-15

Reading a skill catches the traps you can see, and a 1984 result proves that reading can never be sufficient on its own — so the answer is provenance plus containment: pin what you audited so nothing changes under you, and box in what a skill can reach so a missed trap has a small blast radius.

## Papers - read after the parts

### doi:10.1145/358198.358210 - Reflections on trusting trust
`days/day-29-sourcing-and-auditing-skills/papers/01-reflections-on-trusting-trust.md`

You cannot fully trust a program by reading its source, because the tool that built it could have added something the source never mentioned — and the tool that built that tool could have too, all the way down, so trust has to rest on where the thing came from, not only on reading it.


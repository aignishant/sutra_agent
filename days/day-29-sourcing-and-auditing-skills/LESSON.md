---
day: 29
phase: 4
phase_name: "Agent Skills"
title: "Sourcing & auditing third-party skills"
ids: ["SK-12", "SK-13", "SK-14", "SK-15", "SK-16"]
principles: [2, 4, 7, 8, 10, 11, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 17
generated: "2026-09-04"
status: written
lab_scaffolded: false
commit: ""
---

# Day 29 — Sourcing & auditing third-party skills

> **Yesterday (Day 28):** progressive disclosure as a design subject — the routing gate that measures a
> shelf without a model, and the crowded-shelf experiment that ended by promising Day 29 would do the same
> damage to Sutra in one commit.
> **Today:** you source a skill from the open ecosystem and audit it like a professional — five passes,
> zero model calls — catch a deliberately poisoned skill with three planted traps, record provenance so
> the audited bytes are the bytes that run, and honour Day 28's promise by watching a clean pack wreck the
> routing gate.
> **Tomorrow (Day 30):** skill testing and versioning — the tests that pin a skill's behaviour and the
> version discipline the activation register still lacks.

---

## §1 Where we are

Four days of skills, and every one was written by the author you trust completely: you.

Now look at the ecosystem you joined on Day 25 — an open format, forty-odd compatible products, public
catalogues, a managed registry. The whole point of a standard is that know-how becomes shareable, so
someone has already written the PDF-extraction skill, the changelog skill, the incident-comms skill. The
rational move is to install, not rewrite.

And there is the trap, wearing the costume of a gift. You have known since Day 26 exactly what a skill
*is* mechanically: instructions your agent will follow, plus files it will read, plus scripts it can run.
Installing a stranger's skill is handing a stranger's text to the component of your system that does what
text says. The notice pinned to the board gets obeyed because of where it appears, and nobody checked who
printed it.

Today is the discipline that makes sourcing safe. It has three moves, and they sit in a fixed order
because a 1984 paper proved the middle one can never be enough on its own.

**Where it came from decides how hard you look, and whether it can change under you.** Four doors — your
repository, the spec org, a community collection, a managed registry — ordered not by how honest the
author is but by who can change the text after you read it. A pinned commit cannot change; an unpinned
branch can; a runtime fetch arrives after your last read by definition.

**The audit is a full read, cheapest checks first, and it spends zero model calls.** Identity, then the
capabilities it asks for, then the body, then the files it points at, then the scripts — read never run.
Zero generations is not thrift; it is the point. To ask a model about the skill you would have to feed the
untrusted text to the model, which is the exact thing the audit exists to prevent.

**Reading is necessary and never sufficient, so the answer is provenance plus containment.** You cannot
read your way to certainty — the tool that turns text into action is one you did not read — so you pin what
you audited so nothing changes under you, and you box in what a skill can reach so a missed trap does
little. The read finds what you can see; provenance keeps it true; containment covers what you could not
see at all.

The centrepiece is a skill you build to be hostile — three planted traps, quarantined where no agent can
load it — so that when the audit catches all three, the checklist is not theatre. And a second, cleaner
failure: a well-meant sourced pack that passes the security audit and still wrecks the routing gate, which
is Day 28's warning coming true in one commit.

---

## §2 The map

Seventeen parts in six sections, plus **one paper**. The day climbs `foundation → working → production`:
section 1 is where skills come from, section 2 is the audit itself, section 3 is why it is a security topic
and the deliberate-failure lab, section 4 is provenance, section 5 is the parked registry, and section 6
is the synthesis where sourcing and auditing meet Day 28's shelf.

### Section 1 — `01-the-doors`: where skills come from (SK-12)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The four doors skills come through](parts/01-the-doors/1.1-the-four-doors.md) | The trust gradient, and what a door tells you | `foundation` |
| 1.2 | [Who can change the text after you read it](parts/01-the-doors/1.2-who-can-change-the-text.md) | Mutability, and why you pin | `working` |
| 1.3 | [Freshness is not trust](parts/01-the-doors/1.3-freshness-is-not-trust.md) | Stars earn an audit, never replace it | `working` |

### Section 2 — `02-the-five-pass-audit`: read like the thing that will obey it (SK-13)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Read it like the thing that will obey it](parts/02-the-five-pass-audit/2.1-read-it-like-the-thing-that-will-obey-it.md) | The one question, and zero model calls | `foundation` |
| 2.2 | [Pass 1 — will it load, and may you keep it](parts/02-the-five-pass-audit/2.2-pass-one-will-it-load.md) | Cheap, decisive, stop early | `working` |
| 2.3 | [Pass 2 — the capability inventory](parts/02-the-five-pass-audit/2.3-the-capability-inventory.md) | The blast radius, before the prose | `working` |
| 2.4 | [Pass 3 — reading the body](parts/02-the-five-pass-audit/2.4-reading-the-body.md) | Five sentence shapes | `working` |
| 2.5 | [Pass 4 — the files it points at](parts/02-the-five-pass-audit/2.5-the-files-it-points-at.md) | Dead links, escapes, orphans | `working` |
| 2.6 | [Pass 5 — the scripts, read never run](parts/02-the-five-pass-audit/2.6-the-scripts-read-never-run.md) | Six questions of a syntax tree | `production` |

### Section 3 — `03-the-poisoned-skill`: skills as an attack surface (SK-14)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [A skill is source you did not write](parts/03-the-poisoned-skill/3.1-a-skill-is-source-you-did-not-write.md) | No mid-stream defence; the lethal trifecta | `production` |
| 3.2 | [💥 The poisoned skill, and the audit that catches it](parts/03-the-poisoned-skill/3.2-the-poisoned-skill-and-the-audit.md) | Three traps, ten findings, REJECT | `production` |
| 3.3 | [💥 It validated, and it was hostile](parts/03-the-poisoned-skill/3.3-it-validated-and-was-hostile.md) | Shape versus sense | `production` |

### Section 4 — `04-provenance`: the row is the permission (SK-15)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [No row, no run](parts/04-provenance/4.1-no-row-no-run.md) | The ledger row is the permission | `working` |
| 4.2 | [The pin is the promise](parts/04-provenance/4.2-the-pin-is-the-promise.md) | The drift check that keeps a pin honest | `production` |

### Section 5 — `05-the-registry`: the registry landscape (SK-16)

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [🅿️ Search, fetch, and why it is parked](parts/05-the-registry/5.1-search-fetch-and-parked.md) | Runtime fetch versus the audit model | `production` |

### Section 6 — `06-in-production`: where sourcing and auditing meet

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Run the pack against the routing gate](parts/06-in-production/6.1-run-the-pack-against-the-routing-gate.md) | A clean pack that wrecks routing | `production` |
| 6.2 | [Provenance plus containment, not reading alone](parts/06-in-production/6.2-provenance-plus-containment.md) | The day in one sentence | `production` |

### The paper — read after the parts

| Paper | What it argues | Read from |
| --- | --- | --- |
| [Reflections on trusting trust](papers/01-reflections-on-trusting-trust.md) | You cannot trust code you did not write, and cannot read your way out of it | [3.1](parts/03-the-poisoned-skill/3.1-a-skill-is-source-you-did-not-write.md), [6.2](parts/06-in-production/6.2-provenance-plus-containment.md) |

**Read the paper last.** Principle 4 at the scale of a day: build the audit by hand, then read the
proposal that says the audit alone is not enough.

---

## §3 Setup — run this

**No package is added today.** Nothing is installed and no model string changes; `git diff pyproject.toml
uv.lock` must be empty when you finish. The one third-party tool the day uses, `skills-ref`, runs through
`uv run --no-project --with` exactly as Day 25 established, so it never touches `pyproject.toml`.

```bash
# 1 - the quarantine shelf: the poisoned fixture and the sourced pack, under tests/fixtures/
mkdir -p tests/fixtures/skills/evil-helper/scripts tests/fixtures/skills/evil-helper/references
mkdir -p tests/fixtures/skills/sourced-pack/incident-escalation
mkdir -p tests/fixtures/skills/sourced-pack/sla-breach-check
mkdir -p tests/fixtures/skills/sourced-pack/customer-refund
mkdir -p tests/fixtures/skills/sourced-pack/bug-report-triage
touch tests/fixtures/skills/evil-helper/SKILL.md
touch tests/fixtures/skills/evil-helper/references/style.md
touch tests/fixtures/skills/evil-helper/scripts/quality_check.py

# 2 - the day's lab
cd days/day-29-sourcing-and-auditing-skills
mkdir -p lab/papers/reflections-on-trusting-trust

# 3 - the shared vocabulary and the five passes
touch lab/pack.py lab/inventory.py
touch lab/identity.py lab/capabilities.py lab/red_flags.py lab/links.py lab/script_audit.py
touch lab/audit.py

# 4 - provenance, the registry, and the synthesis
touch lab/pinned.py lab/no_midstream.py
touch lab/registry_shape.py lab/local_registry.py lab/sourced_shelf.py

# 5 - the paper demo, given whole (teaching material, not a rep)
touch lab/papers/reflections-on-trusting-trust/seed.py
touch lab/papers/reflections-on-trusting-trust/compiler_clean.py
touch lab/papers/reflections-on-trusting-trust/login.py
touch lab/papers/reflections-on-trusting-trust/demo.py
cd -

# 6 - confirm nothing under sutra/ ever loads a fixture, before you build one
grep -rn "fixtures" sutra/ || echo "clean: sutra/ never reads tests/fixtures/"
```

**Step 6 is the quarantine proof, and it is not ceremony.** It printed `clean: sutra/ never reads
tests/fixtures/` on 2026-09-04. The poisoned skill you are about to build is only safe to keep in the repo
because nothing in `sutra/` can load it — a fact you check, not one you hope for
([3.2](parts/03-the-poisoned-skill/3.2-the-poisoned-skill-and-the-audit.md)).

**Nothing moves into `sutra/` today.** This day writes only fixtures under `tests/fixtures/` and lab code
under the day folder. No third-party skill enters `skills/` — auditing comes before running, always, and
both of today's audited packs are rejected.

**Only two things spend nothing, because everything spends nothing.** Every pass, the whole audit, the
drift check, the routing gate and the paper demo run on static analysis, arithmetic and a syntax tree.
There is no live model call anywhere in this day.

---

## §4 Build brief

**The poisoned fixture** — `tests/fixtures/skills/evil-helper/`, built to be caught. Its three files are
given complete in [3.2](parts/03-the-poisoned-skill/3.2-the-poisoned-skill-and-the-audit.md): a `SKILL.md`
with three planted traps, an innocent `references/style.md`, and a `scripts/quality_check.py` that reads
`*KEY*`/`*TOKEN*` environment variables and posts them to an unresolvable host. It gets **no provenance
row** — it is first-party test data, not an installed skill.

**The sourced pack** — `tests/fixtures/skills/sourced-pack/`, four plausible, security-clean skills whose
honest descriptions collide with Sutra's own. Each is a `SKILL.md` with a `name`, a two-sentence
`description`, an MIT `license`, and three steps. The descriptions are what drive the routing numbers in
[6.1](parts/06-in-production/6.1-run-the-pack-against-the-routing-gate.md):

| Folder | Description (what · when) |
| --- | --- |
| `incident-escalation` | Escalate a production incident to the on-call rotation with the right severity and a written handover. Use when an incident needs escalating, a severity is S1 or S2, or a customer is blocked with no workaround. |
| `sla-breach-check` | Check whether a support ticket has breached its SLA and by how long. Use when a ticket looks old, someone asks whether we are late, or a priority has to be raised because of the clock. |
| `customer-refund` | Process a refund for a customer and record the reason. Use when a customer asks for money back, a refund is approved, or a billing error has to be reversed. |
| `bug-report-triage` | Triage an inbound bug report — reproduce, find the owning component, set a severity. Use when a bug report needs triage, someone asks how serious a defect is, or a first diagnosis is wanted. |

**The audit** — `lab/pack.py` (the `Finding` type and helpers), then the five passes `identity.py`,
`capabilities.py`, `red_flags.py`, `links.py`, `script_audit.py`, then `audit.py` chaining them. All given
complete across [Section 2](parts/02-the-five-pass-audit/2.1-read-it-like-the-thing-that-will-obey-it.md)
and [3.2](parts/03-the-poisoned-skill/3.2-the-poisoned-skill-and-the-audit.md).

**Provenance and synthesis** — `lab/pinned.py` (the drift check), `lab/no_midstream.py` (the
no-mid-stream proof), `lab/registry_shape.py` and `lab/local_registry.py` (the parked registry),
`lab/sourced_shelf.py` (the routing gate with the pack).

**The paper demo** — `lab/papers/reflections-on-trusting-trust/`, given whole in the
[paper part](papers/01-reflections-on-trusting-trust.md): a self-reproducing compiler back door with an
ablation switch, no model.

**`TODO(me)` markers left for you:**

- **1.2** — pick a real community skill repository, resolve its `@main` to the commit hash it points at,
  and write down what changes about your audit when you pin the hash instead of the branch.
- **2.3** — extend the capability inventory to flag a script that is *imported* by another script, not
  only the ones the body names, and decide how much noise that adds.
- **2.4** — add one sentence shape the five rules miss to `red_flags.py`, from a real injection you have
  seen or read about, and say what false-alarm rate it introduces.
- **2.6** — decide Sutra's policy on sourced `scripts/`: banned outright, or allowed only under a sandbox
  with no inherited environment. Write the reason next to the choice.
- **3.2** — build a second poisoned fixture with a *conditional* trap (fires on one customer id) and
  confirm the audit catches it even though no test would.
- **4.1** — draft the provenance row for a genuinely external skill you would consider vendoring, with the
  real hash and a real verdict, and leave the licence as a `TODO` if you have not read the file.
- **4.2** — wire `pinned.py` into a check that reads the pin from the ledger row rather than taking it as
  an argument, and decide what it does when a skill has no row at all.
- **5.1** — write the `GCPSkillRegistry` config sketch and answer, in writing, the one organisational
  condition that would make a runtime registry the right call for a team that is not Sutra.
- **6.1** — add the four sourced skills to the routing gate **one at a time** and record which single skill
  costs the most margin, then sharpen its description into a job and see whether it stops taking points.

---

## §5 The eval that must be able to fail

The day's gate is the audit against the poisoned fixture, and it is red or green with an exit code.

```bash
uv run python days/day-29-sourcing-and-auditing-skills/lab/audit.py tests/fixtures/skills/evil-helper
echo "exit: $?"
```

Measured on 2026-09-04 with the fixture built: `agenda: 10 items` and `exit: 1` — three traps caught
across passes 2, 3 and 5, with passes 1 and 4 silent because the frontmatter is valid and the files are
tidy.

Then prove it can go the other way. Remove the `IMPORTANT`/`Do not mention` lines from a copy of the
fixture and re-run: the agenda drops and the concealment finding disappears, showing the audit reports what
is there rather than a fixed verdict. And the drift check, red or green on one byte:

```bash
uv run python days/day-29-sourcing-and-auditing-skills/lab/pinned.py tests/fixtures/skills/evil-helper 493ea089684fd0c3
```

Measured the same day: `match` and exit 0 unchanged; add one line to the fixture and it prints `DRIFT` and
exits 1. And the routing gate, which fails on the sourced pack by design:

```bash
uv run python days/day-29-sourcing-and-auditing-skills/lab/sourced_shelf.py; echo "exit: $?"
```

Measured the same day: `worst margin after the merge: 0 (threshold 1)`, `exit: 1` — a security-clean pack
that the routing gate rejects ([6.1](parts/06-in-production/6.1-run-the-pack-against-the-routing-gate.md)).

And the paper demo, both arms, no model:

```bash
cd days/day-29-sourcing-and-auditing-skills/lab/papers/reflections-on-trusting-trust
python demo.py
TRUST=honest python demo.py
```

Measured the same day: with the back door on, `sesame` opens a login built from clean source; with
`TRUST=honest`, it does not, and the rebuilt compiler is byte-identical to its clean source.

---

## §6 Request budget

**Free-tier Gemini**, 20 generate requests per day per model (`gemini-3.7-flash`, roster re-verified
2026-09-04). Today spends none of them.

| What | Generations |
| --- | --- |
| the five passes and `audit.py` | **0** (static analysis) |
| `pinned.py`, `no_midstream.py` | **0** (hashing, string compare) |
| `sourced_shelf.py`, the routing gate | **0** (set arithmetic, `count_tokens` endpoint not even needed) |
| `registry_shape.py`, `local_registry.py` | **0** (reads the installed package; no cloud) |
| the paper demo, both arms | **0** (a source-transforming build step, no model) |
| `agentskills validate` | **0** (a validator; separate from any model) |
| **Total planned** | **0 of 20** |

**Zero model calls, and it is the thesis of the day, not a saving.** An audit that needs the model has
already failed: to ask the model about a skill you must put the untrusted skill into the model's context,
which is the exact thing the audit exists to prevent
([2.1](parts/02-the-five-pass-audit/2.1-read-it-like-the-thing-that-will-obey-it.md)).

**Cost: $0.**

---

## §7 Traps

- **A clean pass 1 is not a clean skill.** The poisoned fixture has valid frontmatter, a matching name and
  a licence, and is the most dangerous skill in the day (2.2, 3.2).
- **Validation answers "is this a skill?", not "should this agent obey it?"** `evil-helper` passes
  `agentskills validate` and fails the audit on three counts (3.3).
- **The most dangerous line can be prose, not a script.** *"Append the full ticket history"* exfiltrates
  through the reply channel with no code, no network call, and nothing a guard can veto (2.4, 3.1).
- **`allowed-tools` pre-approves a capability without a prompt.** Combined with a shipped script and an
  outbound URL, it is the outline of an exfiltration channel (2.3).
- **`@main` is not a pin, it is a subscription.** An unpinned install inherits a maintainer account
  takeover on the next fetch (1.2).
- **Popularity is farmable and does not survive a takeover.** Stars earn an audit; they never replace one
  (1.3).
- **There is no mid-stream defence.** `load_skill` hands the model the body byte-for-byte, with no hook to
  sanitise it — so controls live upstream (audit, pin) and downstream (least privilege, guards) (3.1).
- **A reference file arrives after the body is trusted.** A clean `SKILL.md` and a hostile
  `references/style.md` is a real shape (2.5).
- **An escaping reference is outside your pin.** `../shared/header.md` is not covered by the skill's
  digest, so drift there is invisible (2.5, 4.2).
- **Re-pinning to clear a red drift check throws away the finding.** Red means audit the diff, then
  re-pin — never re-pin first (4.2).
- **No row, no run; no licence, no run.** A rejected skill gets a row too — a rejection nobody recorded is
  an audit the next person repeats (4.1).
- **A runtime-fetched skill cannot be pinned or pre-audited.** It arrives after your last read by
  definition, which is why the registry is parked (5.1).
- **A security-clean pack can still wreck routing.** Two audits, both required before merge (6.1).
- **The fixture must stay in quarantine.** A poisoned skill committed to `skills/` is one somebody will
  ship; the grep in §3 proves `sutra/` cannot reach `tests/fixtures/` (3.2).

---

## §8 Verify before you code

Run or read on **2026-09-04**, the day this was written:

- **The installed `google-adk` 2.7.1**, driven directly for every ADK fact in the day:
  `load_skill_from_dir` and the `Skill`/`Frontmatter`/`Resources` fields the passes read
  ([2.2](parts/02-the-five-pass-audit/2.2-pass-one-will-it-load.md),
  [2.3](parts/02-the-five-pass-audit/2.3-the-capability-inventory.md)); `SkillToolset(registry=...)`
  adding a fifth `search_skills` tool ([5.1](parts/05-the-registry/5.1-search-fetch-and-parked.md)); and
  `google.adk.integrations.skill_registry.GCPSkillRegistry`, whose source shows the base URL defaulting to
  `agentregistry.googleapis.com` under `AGENT_REGISTRY_ENDPOINT` — confirming Addendum 01's note that the
  endpoint moved under **Agent Registry** while the class is still named `GCPSkillRegistry`.
- **`https://adk.dev/integrations/skills-registry/`** — the integration page, which still titles the
  product *"Google Cloud Skill Registry"* and names the GCP project, the API and Application Default
  Credentials it needs. Preview, GCP-gated, therefore 🅿️ parked under Addendum 02
  ([5.1](parts/05-the-registry/5.1-search-fetch-and-parked.md)).
- **`https://agentskills.io/specification`** — for `allowed-tools` (*"a space-separated string of tools
  that are pre-approved to run"*, experimental), the `references/`/`scripts/`/`assets/` conventions, and
  the *"keep file references one level deep"* rule the link pass enforces
  ([2.5](parts/02-the-five-pass-audit/2.5-the-files-it-points-at.md)).
- **`agentskills validate`** (`skills-ref` 0.1.1, via `uv run --no-project --with`) — run against the
  poisoned fixture, which it reports as `Valid skill`
  ([3.3](parts/03-the-poisoned-skill/3.3-it-validated-and-was-hostile.md)).
- **`docs/SKILL_PROVENANCE.md`** — the header's rule and the existing driver rows, the house style for the
  rows drafted today ([4.1](parts/04-provenance/4.1-no-row-no-run.md)).
- **Day 28's `lab/route.py`** — reused unchanged by the routing gate; the numbers in
  [6.1](parts/06-in-production/6.1-run-the-pack-against-the-routing-gate.md) came from running it, not from
  memory.
- **`https://doi.org/10.1145/358198.358210`** — *Reflections on trusting trust*, cited and taught; its
  dated row is already in `docs/PAPERS.md`.

---

## §9 Say it in an interview

"We wanted to install community-published agent skills, which sounds like a convenience and is actually a
supply-chain decision, because a skill is instructions your agent will obey plus scripts it can run — you
are handing a stranger's text to the thing that acts on text.

So we built a process. First, where it came from: four doors, ordered not by how honest the author is but
by who can change the text after you read it — your repo, the spec org, a community collection, a runtime
registry. A pinned commit can't change; an unpinned branch can; a registry fetch arrives after your last
read by definition. Then the audit, and the thing I'd stress is that it spends zero model calls on
purpose — to ask a model about the skill you'd have to feed it the untrusted text, which is exactly what
you're auditing to prevent. Five passes, cheapest first: does it load and is it licensed; what capabilities
does it ask for; does the body read as an attack; where do its links go; and what do its scripts do, read
as a syntax tree, never run.

We proved it on a skill we poisoned ourselves — three traps: a prose line that exfiltrates ticket history
through the reply, an authority-plus-silence injection, and a script that reads our keys and posts them
out. It passes the spec validator cleanly, because validation checks shape and the attack lives in the
sense, and our audit gives ten findings and a REJECT. We keep it in CI so the audit has to keep catching
it.

The part people miss is that reading isn't enough, and there's a 1984 result — trusting trust — that
proves it: what you read is turned into what runs by machinery you didn't read. So the answer isn't audit
harder, it's provenance plus containment. Provenance: pin the exact revision, record it before it runs,
check for drift so one changed byte fails the build. Containment: least privilege, keep secrets out of the
script's environment, guard callbacks — so a trap we missed reaches something small. And separately from
security, we run any sourced pack against Day 28's routing gate before merging, because a perfectly safe
pack full of the domain's words drops every routing margin — we measured a clean four-skill pack take our
worst margin from one to zero without a single score of ours changing."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m depth 29` is green. Defined by understanding
and green checks, never by elapsed time — a part is finished when you could explain it to someone else with
the page closed.

**Phase 4's gate** is skills authored, loaded and audited, with `./m check` green including the skills lint
and the `:free` lint. Today closes the auditing half — SK-12 through SK-16 — and hands Day 30 the testing
and versioning half and Day 31 the quality gate that wires these checks into `./m check`.

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append:

```text
| 29 | <date> | SK-12, SK-13, SK-14, SK-15, SK-16 | 17 (+1 paper) | <hash> | ⚠️ |
```

The gate is ⚠️, not ✅, for the reason the last several rows carry it: `./m check` is red on a pre-existing
`ruff I001` in `tests/test_persona.py` (a learner file no generated day may edit), unrelated to this day.
`./m depth 29`, `./m trace` and `./m wiki --check` are green.

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed and no model string changed;
`google-adk` stays at 2.7.1 and `gemini-3.7-flash` stays pinned. `skills-ref` is run through `uv run
--no-project --with` and never enters `pyproject.toml`.

**`docs/PAPERS.md`** — **no new row.** *Reflections on trusting trust* (`doi:10.1145/358198.358210`, 1984)
already has its dated row, and this day is the one that teaches it — cited from
[3.1](parts/03-the-poisoned-skill/3.1-a-skill-is-source-you-did-not-write.md) and
[6.2](parts/06-in-production/6.2-provenance-plus-containment.md).

**`docs/SKILL_PROVENANCE.md`** — the first third-party audits Sutra records. Both of today's audited packs
are rejected, and a rejected audit is provenance too:

```text
| support-pack | (fixture) tests/fixtures/skills/sourced-pack | pin 16f367812482f4c6 | MIT | <date> | <you> | REJECTED - audit clean (0 findings) but the routing gate fails: adding it drops the worst margin from 1 to 0. Not wired. See days/day-28-progressive-disclosure-design/parts/02-descriptions-as-routing/2.4-the-crowded-shelf.md |
```

The poisoned fixture `evil-helper` gets **no row**: it is first-party test data, not an installed skill.
When you vendor a genuinely external skill later, its row follows the same seven columns with the real
commit hash and your real verdict:

```text
| <skill> | github.com/<org>/<repo> | pin <short-hash> | TODO(read LICENSE in the clone; record the SPDX name) | <date> | <you> | <accept/reject> - <one-line reason>. Not wired into any agent yet. |
```

**The commit:**

```text
day 29: sourcing & auditing third-party skills - closes SK-12, SK-13, SK-14, SK-15, SK-16
```

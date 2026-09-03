---
day: 18
phase: 3
phase_name: "State, context & discipline"
title: "Artifacts — files that survive turns"
ids: ["ADK-21"]
principles: [1, 2, 4, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18]
kind: lab
plan_version: "v2.2.1"
parts: 15
generated: "2026-09-03"
status: written
lab_scaffolded: false
commit: ""
---

# Day 18 — Artifacts: files that survive turns

> **Yesterday (Day 17):** session state — a small form stapled to the conversation, with four
> lifetimes chosen by a key's name and three ways to write it safely. It also drew a line: state is for
> small serializable facts.
> **Today:** the other side of that line. **Artifacts** are named, versioned bytes kept beside the
> conversation — an attached log, a generated note — served by their own service, with two scopes and
> a history of their own. And the first thing in this repository that survives a restart.
> **Tomorrow (Day 19):** context engineering — what earns a place in the window, now that Sutra has
> three stores and only one of them is free to read.

---

## §1 Where we are

The photographs you take on the day you move out.

Nobody enjoys it. You are tired, the van is waiting, and you are walking around an empty flat taking
pictures of skirting boards. The mark behind where the sofa was. The window that never closed. The
meter reading, twice, because the first one was blurry.

You do it because the conversation that matters happens **two months later**, with somebody who was not
there, about a deposit. And in that conversation nothing you *said* counts for anything. What counts is
whether there is a file, with a date on it, showing the thing you are describing.

The conversation was real and it is gone. The photographs are still on your phone, in an album you
named, and they will still be there next year.

That is today. Sutra's conversations hold prose and small facts; artifacts hold the things somebody will
want back. Section 1 is what an artifact is and why it is not a state key. Section 2 is versioning —
every save keeps the last one, which is a feature with a bill attached. Section 3 is the two scopes and
what the store looks like on disk. Section 4 is using them from a tool, including the fact that saving a
file does **not** show it to the model. Section 5 breaks it on purpose, and section 6 is what you test,
what you keep, and what survives a restart.

Four things worth knowing before you start.

**An artifact is a `Part`, not a file.** Bytes plus a MIME type, addressed by app, user, session and
filename. The MIME type is optional in the code and required in practice.

**Nothing is ever overwritten.** Saving the same name again returns version 1, and version 0 is still
there. Twenty saves of one note is twenty copies, and `delete_artifact` removes all of them at once.

**The filename chooses the scope**, exactly as a state key's prefix chose its lifetime yesterday.
`triage-4521.md` belongs to this conversation; `user:signature.txt` belongs to the engineer.

**And artifacts are the first thing in this repository that survives a restart.** `FileArtifactService`
is a directory tree at zero cost, which is half of Phase 3's gate — proved with a test today, and paired
with a durable session store on Day 47.

---

## §2 The map

Fifteen parts in six sections, and **no paper**: the artifact service is an SDK surface, and the depth
contract is explicit that a day does not manufacture a citation it does not have (§17.4.2). The day
climbs `foundation → working → production`.

### Section 1 — `01-not-a-state-key`: what an artifact is

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [The thing state cannot hold](parts/01-not-a-state-key/1.1-the-thing-state-cannot-hold.md) | Three stores, three readers, and where bytes go | `foundation` |
| 1.2 | [A Part, not a file](parts/01-not-a-state-key/1.2-a-part-not-a-file.md) | Bytes plus a type, and the string that silently becomes base64 | `working` |
| 1.3 | [A separate wire](parts/01-not-a-state-key/1.3-a-separate-wire.md) | Three services, one missing argument, and no output at all | `working` |

### Section 2 — `02-versions`: a name with a history

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [Every save is a new version](parts/02-versions/2.1-every-save-is-a-new-version.md) | 0, 1, 2 — and two very different `None`s | `working` |
| 2.2 | [What a version knows about itself](parts/02-versions/2.2-what-a-version-knows.md) | A changelog the store writes for you | `working` |
| 2.3 | [Nothing is overwritten](parts/02-versions/2.3-nothing-is-overwritten.md) | 36,280 bytes for one note, and what delete really does | `production` |

### Section 3 — `03-two-scopes`: whose file is it

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [The `user:` filename](parts/03-two-scopes/3.1-the-user-filename.md) | Five characters, and the file follows the engineer | `working` |
| 3.2 | [Where it actually lives](parts/03-two-scopes/3.2-where-it-actually-lives.md) | The tree on disk, and the filename that becomes a path | `production` |

### Section 4 — `04-in-the-run`: using them from an agent

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [Saving from a tool](parts/04-in-the-run/4.1-saving-from-a-tool.md) | One event, two deltas, two stores | `working` |
| 4.2 | [Reading it back](parts/04-in-the-run/4.2-reading-it-back.md) | Fifteen bytes of note, 361 characters of prompt | `working` |
| 4.3 | [What the model cannot see](parts/04-in-the-run/4.3-what-the-model-cannot-see.md) | The names on every request, the contents on one | `production` |

### Section 5 — `05-failure-lab`: the deliberate failure

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [💥 The artifact with no service](parts/05-failure-lab/5.1-the-artifact-with-no-service.md) | The fourth failure this phase that produces no answer at all | `production` |

### Section 6 — `06-in-production`: test, keep, survive

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [Testing artifacts without a model](parts/06-in-production/6.1-testing-artifacts-without-a-model.md) | Seven assertions, no skips, and one that proves durability | `production` |
| 6.2 | [What belongs in an artifact](parts/06-in-production/6.2-what-belongs-in-an-artifact.md) | Four stores, four questions, and the store with no `temp:` | `production` |
| 6.3 | [Surviving a restart](parts/06-in-production/6.3-surviving-a-restart.md) | `None` against the bytes, and half a phase gate | `production` |

---

## §3 Setup — run this

**No new packages today.** `google-adk` 2.7.1 carries all three artifact services, and everything else
is the standard library.

```bash
# 1 - confirm where you are starting from
./m check

# 2 - today's lab
mkdir -p days/day-18-artifacts-that-survive/lab
cd days/day-18-artifacts-that-survive/lab

# yesterday's scripted model - copy it, do not import across day folders
cp ../../day-17-state-scopes-and-lifetimes/lab/scripted.py .

# section 1
touch first_artifact.py what_a_part_is.py the_wire.py
# section 2
touch versions.py version_metadata.py the_loft.py
# section 3
touch two_scopes.py on_disk.py
# section 4
touch save_and_find.py read_it_back.py not_in_context.py
# section 6
touch after_the_restart.py
cd -

# 3 - two scripts write to disk; keep the store out of git
grep -q "artifact_store/" .gitignore || echo "artifact_store/" >> .gitignore
grep -q "days/*/lab/artifact_store/" .gitignore || echo "days/*/lab/artifact_store/" >> .gitignore

# 4 - what changes under sutra/ and tests/ today
ls sutra/                    # artifacts.py is new, at the package root
ls tests/                    # test_artifacts.py is the eval
```

**Every lab script runs from inside `lab/`**, because three of them import `scripted` by bare name:

```bash
cd days/day-18-artifacts-that-survive/lab && uv run python first_artifact.py
```

**Run `the_wire.py` twice** — once as it comes, and once with `2>&1` on the end. The difference between
those two runs is section 5, and it is worth meeting before you write any code of your own.

**`on_disk.py` and `after_the_restart.py` write a real directory** called `artifact_store` inside
`lab/`. Both scripts delete it when they start, so they can be re-run; the `.gitignore` lines above are
what stop it reaching a commit. That directory is customer-file-shaped, and Principle 9's habit applies
to anything that shape.

**`sutra/artifacts.py` is new and lives at the package root**, beside `state.py` from yesterday. The
two modules are a pair: one owns the small facts, the other owns the bytes, and the reference that links
them is a state key defined in the artifacts module.

---

## §4 Build brief

**`sutra/artifacts.py`** — new, at the package root:

| Symbol | What it is | Taught in |
| --- | --- | --- |
| `NOTE_MIME` | the note's MIME type, set in one place | 1.2 |
| `SIGNATURE` | the `user:`-scoped filename that follows the engineer | 3.1 |
| `NOTE_FILE`, `NOTE_VERSION` | the **state** keys that point at the current note | 4.1 |
| `note_filename(ticket_id)` | the derived name — never user-supplied text | 3.2 |
| `save_note(ticket_id, body, tool_context)` | async tool: saves the file, records the reference | 4.1 |
| `read_note(tool_context)` | async tool: loads the recorded version, or says why it cannot | 4.2 |
| the module docstring | the scope rule, the split between stores, the one prohibition | 6.2 |

Three things in that table are the whole design. `note_filename` calls `int(ticket_id)` because a
filename built from `"4521 "` is a different filename and ticket ids arrive as strings. `save_note`
writes the artifact **and** the two state keys in one call, so they land on one event
([4.1](parts/04-in-the-run/4.1-saving-from-a-tool.md)). And `read_note` loads
`(filename, version)` rather than the latest, because "the note" stops being unambiguous the moment
there are two.

**`tests/test_artifacts.py`** — new. Seven assertions and no skips; see §5.

**Nothing under `sutra/desk/` has to change today**, and whether the desk gains these two tools is one
of the `TODO(me)` decisions below. Confirm with `git diff` before you commit.

**`days/day-18-artifacts-that-survive/lab/`** — eleven scripts plus the copied double. **All of them
cost zero requests.**

**`TODO(me)` markers left for you:**

- **5.1** — write the runner factory. One function that builds the session service, the artifact
  service and the runner, so no call site can wire half of them
  ([5.1](parts/05-failure-lab/5.1-the-artifact-with-no-service.md)). Then add the two-line test that
  asserts the runner it returns has an artifact service.
- **6.3** — decide where the production artifact root lives, and write down what happens to files on a
  redeploy under your answer. A path in the repository is not the answer; a configured directory is.
- **2.3** — decide Sutra's retention rule for notes: save on every turn, or only when the note changes.
  Write the rule and the number of versions you expect on a twenty-turn ticket.
- **4.3** — decide whether the desk gets `load_artifacts`. If it does, write one sentence on what a
  customer's attachment being in the model's context means for Day 66.
- **6.2** — write the attachment rule before attachments exist: which name is generated, what the size
  cap is, and where the customer's original filename is kept.
- **2.2** — choose the third `custom_metadata` key. `written_by` and `ticket_id` are in the build;
  name one more that you would want during an incident, and say why.

---

## §5 The eval that must be able to fail

One new file, **seven assertions and no skips**, no key and no network. The whole file's shape and
three of its tests are in [6.1](parts/06-in-production/6.1-testing-artifacts-without-a-model.md).

Today is unusual: yesterday's suite had to skip its durability test, because an in-memory session
service cannot survive anything. Artifacts have a free local service, so *state survives restarts* is
half provable **today** — save with one `FileArtifactService`, discard it, read with another, assert the
bytes.

**How to watch it go RED before it goes green:**

```bash
uv run python -m pytest tests/test_artifacts.py -q -m "not live"   # RED: no sutra/artifacts.py yet
# ... write the module from §4 ...
uv run python -m pytest tests/test_artifacts.py -q -m "not live"   # 7 passed
```

Then break each thing on purpose. These were **measured**, each applied on its own to a green suite:

| Break this | Which tests go red | What it is telling you |
| --- | --- | --- |
| `SIGNATURE = "signature.txt"` (drop `user:`) | 1 — the scope test | the filename chooses the scope (3.1) |
| delete the two `state[...]` writes in `save_note` | 1 — the reference test | an artifact nobody can find (4.1) |
| `note_filename` returns a name with no `.md` | **2** — the filename test and the reference test | the name is an interface (3.2, 4.1) |

The third row is the one to read twice. A filename is used in two places — where it is built and where
it is recorded — so changing it breaks both, and a suite that only checked one would have let it
through.

---

## §6 Request budget

**Free-tier Gemini**, 20 requests per day (`docs/PACKAGES.md`, 2026-08-25).

| What | Model calls |
| --- | --- |
| all eleven lab scripts, all six sections | **0** |
| the failure lab | **0** |
| the whole test suite | **0** |
| **Total required** | **0 of 20** |

Zero, for the second day running, and for the same structural reason: an artifact store is a store.
Nothing about saving, versioning, scoping or loading a file involves a model. Four of the scripts drive
a real `Runner` — because *"a tool's save records a delta on the event"* is a claim about a run — and
they drive it against Day 13's scripted double.

**Optional, and worth one request if you have quota:** give the desk `load_artifacts`
([4.3](parts/04-in-the-run/4.3-what-the-model-cannot-see.md)), save a note, and ask
`gemini-3.7-flash` what the note says. The thing to watch is whether the model calls the tool at all —
that is a fact about the dynamic instruction the tool appends, and a scripted model cannot tell you.

**Cost: $0.**

---

## §7 Traps

- **Bytes in a state key** fail at Day 47 with `TypeError: Object of type bytes is not JSON
  serializable`; base64 in a state key does not fail at all and carries the file on every turn. (1.1)
- **`Blob(data="...")` reads the string as base64.** `"high"` becomes `b'\x86(!'`, silently. Always
  `.encode("utf-8")`. (1.2)
- **`mime_type` is optional and nothing later can work without it** — rendering, HTTP responses, and the
  safety conversion that decides what a model may see all key off it. (1.2)
- **A text `Part` has no `inline_data`**, so saving one stores an artifact with no bytes. (1.2)
- **No `artifact_service` on the runner means `ValueError: Artifact service is not initialized.`** —
  raised inside the run, wrapped, and never reaching your code. (1.3, 5.1)
- **`save_artifact` returns a version and never replaces.** There is no `overwrite=True`. (2.1)
- **A missing file and a missing version both return `None`.** The two are indistinguishable. (2.1)
- **`delete_artifact` removes every version**, and the next save starts again at 0 — so an old
  `(filename, version)` reference can silently point at a different document. (2.3)
- **`custom_metadata` defaults to `{}`** and cannot be added retroactively. (2.2)
- **The `user:` prefix is part of the filename in every call**, including reads; without it you are
  addressing a different artifact. (3.1)
- **The filename becomes a path.** Slashes create directories; `..` is refused with
  `InputValidationError`; everything else is your problem, including length. (3.2)
- **Windows path limits bite** — the layout is six levels deep before your filename, so a long root plus
  a long name gives `FileNotFoundError` from inside the service. (3.2, 6.3)
- **`save_artifact` is a coroutine**, so an artifact-saving tool must be `async def`. (4.1)
- **Templating `{artifact.name}` into an instruction inserts the `Part` repr** — 361 characters of
  mostly `None` for a fifteen-byte note. Load it in a tool instead. (4.2)
- **A saved artifact is not in the model's context.** Only `load_artifacts` — or a tool that returns the
  text — puts it there, and only for one request. (4.3)
- **A model asking for a filename that does not exist gets nothing and is not told**: the framework logs
  `Artifact "…" not found, skipping` and answers anyway. (4.3)
- **The in-memory service loses everything on restart** — and so does a second worker, which never had
  it. (6.3)
- **A durable artifact store under an ephemeral session store** leaves files that nothing points at.
  (6.3)
- **The artifact root belongs in `.gitignore`** the moment it exists. (3.2, 6.3)

---

## §8 Verify before you code

Fetched on **2026-09-03**, the day this was written:

- **`adk.dev/artifacts/`** — the page timed out twice from this machine, so the documented behaviour was
  confirmed from the ADK documentation pages returned by search on the same day: that artifacts are the
  mechanism for *"file-like binary data that needs to be persisted, versioned, or shared"*; that
  `save_artifact` returns the new version number starting from 0 and `load_artifact` returns the latest
  unless a version is given; that a plain filename is scoped to the app, user **and session** while one
  prefixed `user:` is scoped to the app and user; and that `list_versions` lives on the service rather
  than on the context. **Re-open the page on the day you run this**, and if it disagrees with any of the
  measurements below, the measurements were taken against the installed package and the page is the one
  to check twice (Principle 8).
- **The installed `google-adk` 2.7.1**, in `.venv/Lib/site-packages/google/adk/` —
  `artifacts/base_artifact_service.py` (the full signatures, `ArtifactVersion`, `ensure_part`, and the
  documented rule that a `None` session id means user scope), `artifacts/in_memory_artifact_service.py`
  (the `user:` check and the canonical URIs), `artifacts/file_artifact_service.py` (the on-disk layout,
  documented in a comment, and the traversal rejection), `agents/context.py` (`save_artifact`,
  `load_artifact`, `list_artifacts`, `get_artifact_version`, and the `artifact_delta` they record) and
  `tools/load_artifacts_tool.py` (the dynamic instruction, the user-scope fallback, the skip-on-missing
  behaviour and `as_safe_part_for_llm`). **Every behavioural claim in this day was run on this machine
  against this version**, not read.
- **`google-genai` 2.19.0** — `types.Part`, `types.Blob`, and the fact that a `str` in a bytes field is
  decoded as base64 rather than rejected.

If your `google-adk` is not 2.7.1, run `versions.py`, `two_scopes.py` and `after_the_restart.py` before
trusting a number in this day — and if any of them disagrees, that is a Principle 14 moment: amend
first, then write.

---

## §9 Say it in an interview

"Our agent needed to keep files — attachments coming in, notes going out — and the first thing to get
right was not putting them in session state, because state is loaded on every turn and a file is not
something you want on that path. So files went into the artifact service, and the *reference* — the
filename and the version — went into state, written in the same tool call so they land on the same
event and cannot drift apart. Three things surprised me. Saving never overwrites: the same filename
gives you version 1 beside version 0, which is exactly what you want for a document somebody revised
and a real storage bill if a tool saves on every turn. Deleting takes every version at once and the
numbering restarts, so an old reference to version 3 can silently point at a different document.
And saving a file does not show it to the model — you either load it in a tool and return the part that
matters, or you add the framework's `load_artifacts` tool, which advertises the filenames on every
request and inserts the contents only for the one request where the model asks. The failure I would warn
anybody about is the missing service: build a runner without an artifact service and every save raises
inside the runtime, wrapped, so the turn just ends with no answer and no exception at your call site.
That is the fourth failure of that exact shape we found in two days, and it is why we build services in
one factory and assert them in a test."

---

## §10 Done when

See [`CHECKLIST.md`](CHECKLIST.md). Every box ticked, `./m depth 18` green, `./m check` printing
`OK all green`, and — the part no script can check — you can answer the *out loud* question at the end
of each of the fifteen parts without scrolling up.

Not when a number of sittings has passed. When you can say which store a given thing belongs in without
hesitating, and prove that one of them survives a restart.

---

## §11 Ledger & commit

Paste these **with the values you actually observed** (Principle 7), not the ones printed here.

**`docs/PROGRESS.md`** — append one row:

```text
| 18 | <date> | ADK-21 | 15 | <hash> | ✅ |
```

**`docs/PACKAGES.md`** — **no new rows.** Nothing was installed today.

**`docs/PAPERS.md`** — **no new rows.** Today has no paper: an artifact service is an SDK surface, not an
idea from the literature (§17.4.2). The next paper arrives tomorrow, with context engineering.

**`docs/SKILL_PROVENANCE.md`** — no rows. First entries arrive on Day 29.

**`docs/adr/`** — no new ADR is required, and two decisions belong in the commit message: where the
production artifact root lives (§4's `TODO(me)`), and whether the desk gets `load_artifacts`. **If your
ADK version starts overwriting instead of versioning, or stops trimming the `user:` prefix from stored
paths, stop and re-read Principle 14 before editing anything** — that is a behaviour change in a pinned
dependency, and the plan is amended first.

**Commit message:**

```text
day 18: artifacts - files that survive turns - closes ADK-21
```

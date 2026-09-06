---
day: 67
phase: 10
phase_name: "Safety and security"
title: "Defense in depth — input/output guardrail callbacks"
ids: ["SEC-08", "SEC-09"]
principles: [1, 2, 4, 8, 10, 11, 13, 15, 16, 17, 18]
kind: build
plan_version: "v2.2.1"
parts: 24
generated: "2026-09-06"
status: written
lab_scaffolded: true
commit: ""
---

# Day 67 — Defense in depth: input and output guardrail callbacks

> **Yesterday (Day 66):** the threat model. Six doors into the desk's context, five ways out with four
> of them not looking like network calls, and the lethal trifecta closing at the `review` stage once
> you ask along the path instead of per stage. Its document has a `mitigate` row reading *hostile text
> reaching the prompt — provenance marking and guardrails, Day 67*.
> **Today:** that row. Eight places a check can stand in ADK 2.7.1, a ladder of checks ordered cheap
> and certain first, and then the part most write-ups skip — measuring it in both columns, and then
> measuring it again against somebody who has read the checks.
> **Tomorrow (Day 68):** least privilege for tools, which is where the control stops reading text and
> starts being a capability the agent does not hold.

---

## §1 Where we are

Yesterday produced a document with four `mitigate` rows in it, each naming a day. This is the first
of them, and it is the one most people think is the whole answer.

The temptation today is to build the best possible check and stop. The day is arranged to make that
impossible: sections 1 to 4 build the checks properly — where they stand, what they may return, what
comes in, what goes out — and then section 5 measures them, honestly, twice, and the second
measurement is the one that decides how the day ends.

Think about a cable lock on a bicycle. It is a good lock, and it is not what stops the bike being
stolen; what stops the bike being stolen is that thieves would rather do the one that is not locked.
That is a real effect and it is worth buying. It is also not the same claim as *the bike cannot be
taken*, and confusing those two claims is the thing this day exists to prevent.

So the shape of today is: build the ladder, price it, then find its ceiling. The ceiling is measured,
not asserted — **6 of 6** on the fixtures the checks were written against, **2 of 5** once the same
instruction is rewritten by somebody who read them, and **0 of 3** when the payload is split across
two archive rows so that the instruction never exists as a string anywhere in the pipeline.

Everything the ladder is worth survives that. It catches the copied payload, it costs almost nothing
when ordered cheap-first, it produces the record you will want during an incident, and it makes an
attacker do work. What it does not do is close anything, because every rung works by reading text and
text can be rewritten. Section 6 is where that conclusion is drawn and handed to Day 68.

---

## §2 The map

Six sections. Section 1 is what a defence in depth is and why one check is never the answer. Section 2
is the ADK surface — the eight callback positions, what each may return, and three traps that produce
a system which looks guarded and is not. Section 3 is what comes in. Section 4 is what goes out,
including two ways a guardrail can make the record worse than no guardrail. Section 5 is the
measurement. Section 6 is what the numbers mean in production, and where the day stops.

### 1 — The ladder

*Why one check is never the answer, and how to order the ones you have.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 1.1 | [One lock is not security](parts/01-the-ladder/1.1-one-lock-is-not-security.md) | How many kinds of check to stack, and what each is honestly worth | `foundation` |
| 1.2 | [Cheap and certain before expensive and fuzzy](parts/01-the-ladder/1.2-cheap-and-certain-first.md) | Ordering halves the model calls — seven instead of fourteen — and what that trades away | `working` |
| 1.3 | [A sign is not a gate](parts/01-the-ladder/1.3-a-sign-is-not-a-gate.md) | A filter can be argued with; only a check that never reads is a boundary | `working` |

### 2 — Where a check stands

*The ADK 2.7.1 callback surface, and three ways to wire a guardrail that never guards.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 2.1 | [The eight places you can stand](parts/02-where-a-check-stands/2.1-the-eight-places-you-can-stand.md) | Choosing a hook is choosing what your guardrail can see | `foundation` |
| 2.2 | [Allow, block, rewrite](parts/02-where-a-check-stands/2.2-allow-block-rewrite.md) | The three things a `before_model_callback` may return | `working` |
| 2.3 | [A ladder is a list](parts/02-where-a-check-stands/2.3-a-ladder-is-a-list.md) | Callback fields take lists, and the runtime stops at the first **truthy** result | `working` |
| 2.4 | [The guardrail that never ran](parts/02-where-a-check-stands/2.4-the-guardrail-that-never-ran.md) | 💥 Callbacks are called by keyword, and the type alias says otherwise | `production` |
| 2.5 | [The empty dict that fails open](parts/02-where-a-check-stands/2.5-the-empty-dict-that-fails-open.md) | 💥 A falsy refusal is overwritten by the next callback, and the tool runs | `production` |

### 3 — What comes in

*Untrusted text arriving, and four things you can do about it that are not a phrase list.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 3.1 | [Most of the turn is not yours](parts/03-what-comes-in/3.1-most-of-the-turn-is-not-yours.md) | 1,463 of 1,591 characters — 92% — written outside the system, counted not guessed | `foundation` |
| 3.2 | [Marking what you did not write](parts/03-what-comes-in/3.2-marking-what-you-did-not-write.md) | Provenance does not stop attacks; it makes the rules that do **expressible** | `working` |
| 3.3 | [The fence the data can close](parts/03-what-comes-in/3.3-the-fence-the-data-can-close.md) | 💥 Delimiters, and the two distinct ways they fail | `working` |
| 3.4 | [Letters that are not the letters they look like](parts/03-what-comes-in/3.4-letters-that-are-not-the-letters.md) | Why confusables need a mixed-script check and not normalisation | `working` |
| 3.5 | [Never in the instruction](parts/03-what-comes-in/3.5-never-in-the-instruction.md) | One rule a test can check, unlike everything else in this section | `working` |

### 4 — What goes out

*The tool call is the dangerous half, and two guardrails that make the record worse.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 4.1 | [The tool call is the output](parts/04-what-goes-out/4.1-the-tool-call-is-the-output.md) | Checking prose checks the half that cannot hurt anybody | `working` |
| 4.2 | [The channels a reply carries](parts/04-what-goes-out/4.2-the-channels-a-reply-carries.md) | A URL allowlist narrows the pipe and does not close it | `working` |
| 4.3 | [The rewrite that lies](parts/04-what-goes-out/4.3-the-rewrite-that-lies.md) | 💥 A silent edit leaves a truthful-looking record of text nobody sent | `production` |
| 4.4 | [The error hook that invents a result](parts/04-what-goes-out/4.4-the-error-hook-that-invents-a-result.md) | 💥 An outage reported to the customer as "no prior tickets" — trap #4, Principle 10 | `production` |

### 5 — Measure it

*Both columns, then the same instruction written by somebody who read the checks.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 5.1 | [Both columns](parts/05-measure-it/5.1-both-columns.md) | 6/6 caught **and** 1/8 falsely flagged, and why one number alone is not a measurement | `working` |
| 5.2 | [Refused for quoting an error](parts/05-measure-it/5.2-refused-for-quoting-an-error.md) | The one false positive, in full: a customer refused for quoting a banner | `production` |
| 5.3 | [Five more words](parts/05-measure-it/5.3-five-more-words.md) | 💥 After an incident: detection 6→6, wrongly blocked 1→3 | `production` |
| 5.4 | [The same instruction, five ways](parts/05-measure-it/5.4-the-same-instruction-five-ways.md) | 💥 2 of 5 against an adversary, and 0 of 3 against a split payload | `production` |

### 6 — In production

*What the numbers mean, what happens when the guardrail itself breaks, and where the day stops.*

| # | Part | What it answers | Level |
| --- | --- | --- | --- |
| 6.1 | [The notes-for-the-assessor box](parts/06-in-production/6.1-the-notes-for-the-assessor-box.md) | 💥 The model judge is a model reading attacker text, and defending it does not terminate | `production` |
| 6.2 | [When the guardrail itself throws](parts/06-in-production/6.2-when-the-guardrail-itself-throws.md) | Fail-closed **by accident**, and the seven lines that make it yours | `production` |
| 6.3 | [The drop safe, not another supervisor](parts/06-in-production/6.3-the-drop-safe-not-another-supervisor.md) | What the ladder is worth, what closes a channel, and why that is Days 68 and 69 | `production` |

### The paper — read it last

*Principle 4 at the scale of a day: build the ladder, measure its ceiling, then read the design that
starts from the other end.*

| # | Paper | What it answers |
| --- | --- | --- |
| 01 | [Defeating Prompt Injections by Design](papers/01-defeating-prompt-injections-by-design.md) | `arXiv:2503.18813` — assume the model is injected and obeying; make that harmless by never letting a value derived from untrusted data reach a sink |

---

## §3 Setup — run this

```bash
mkdir -p days/day-67-guardrail-callbacks/lab/papers/camel
cd days/day-67-guardrail-callbacks/lab
```

Twenty-one files in the lab, plus two in the paper's demo directory. No package is added today —
`google-adk` is already pinned from Day 7:

```bash
touch _archive.py _desk.py _guards.py _poison.py
touch surface.py toolcall.py returns.py ladder.py names.py failopen.py
touch provenance.py spotlight.py bypass.py outbound.py score.py falsepos.py
touch rewrite.py swallow.py selfinject.py failmode.py gate.py
touch papers/camel/capability.py papers/camel/demo.py
```

**What each file is for:**

- The four underscore-prefixed modules are imported, never run: `_archive.py` is the archive Days 49
  and 50 indexed, `_desk.py` is a scripted agent harness so a turn can be run without a model call,
  `_guards.py` is the ladder itself — four checks and `inspect_text` — and `_poison.py` is the corpus,
  six hostile fixtures and eight benign ones.
- `surface.py`, `toolcall.py`, `returns.py`, `ladder.py`, `names.py` and `failopen.py` are section 2:
  the eight positions, what each sees, what each may return, the list behaviour, and the two traps.
- `provenance.py`, `spotlight.py`, `bypass.py` and `outbound.py` are sections 3 and 4.
- `score.py` and `falsepos.py` are section 5's measurements. `bypass.py` is used again there, in full.
- `rewrite.py` and `swallow.py` are the two record-destroying guardrails in section 4.
- `selfinject.py` and `failmode.py` are section 6, and `gate.py` is today's eval.

Verify the lab is gitignored before running anything that writes:

```bash
git check-ignore -v days/day-67-guardrail-callbacks/lab/_poison.py
```

**Why:**

- `days/*/lab/` is ignored repo-wide. Today's corpus is synthetic hostile text and synthetic customer
  tickets, and none of it belongs in git — Principle 9. If this prints nothing, stop and fix
  `.gitignore` first.

**No package is added today.** `git diff pyproject.toml uv.lock` must be empty and stay empty.

---

## §4 Build brief

The teaching is in `parts/` and the measurements are in `lab/`. What is left for you is the piece that
belongs in the product.

**`sutra/guardrails.py`** — the ladder, promoted out of the lab so the triage graph can use it.

- `TODO(me)`: `inspect_text(text) -> tuple[str, int]` returning the reason and the number of checks
  run. The count is not decoration — part 1.2's whole argument is about how far down the ladder a
  given input travels.
- `TODO(me)`: `block_disallowed_send`, a `before_tool_callback` guard. Its parameters **must** be
  named `(tool, args, tool_context)` — part 2.4 — and `gate.py` reads the signature with `inspect` to
  check it.
- `TODO(me)`: a module-level `REFUSAL` that is **truthy**, and used as the refusal value everywhere.
  Part 2.5 is why a falsy refusal is a bug rather than a style choice.
- `TODO(me)`: decide the fail mode. Wrap the ladder so an exception inside a check becomes a recorded
  refusal for the irreversible tools and a logged pass-through for the read-only ones — part 6.2 — and
  put the reason in a docstring, because the decision matters more than the wrapper.

**`tests/test_guardrails.py`**

- `TODO(me)`: a test that a guardrail which raises does not let the tool run. Assert on the effect,
  not on the answer — part 6.2 shows why the answer lies.
- `TODO(me)`: a test that a refusal is truthy, so that adding a later callback cannot silently
  override it.
- `TODO(me)`: a two-column test. Assert the ladder's detection **and** its false-positive count
  against the benign fixtures, and pick the thresholds yourself. Writing down the number you are
  willing to accept is the exercise; part 5.1 is the argument for why one number is not enough.

Do not copy the lab scripts into `sutra/`. `_desk.py` and `_poison.py` are instruments for this day.

---

## §5 The eval that must be able to fail

```bash
cd days/day-67-guardrail-callbacks/lab
uv run python gate.py; echo "exit: $?"
```

Six checks against `sutra/guardrails.py`, and all six are **red** today because the module is the
build brief. Every one of them can go red for a reason this day discovered rather than for a reason
invented to make the gate look thorough — two of them carry the part number in the failure message.

The checks that can be driven red **on demand**, which is the point of Principle 11, are exercised in
their parts and worth running directly:

```bash
uv run python failopen.py
uv run python failmode.py --closed
uv run python bypass.py --split
```

The first shows a refusal being overwritten by a later callback, the second shows an exception inside
a guardrail becoming a recorded refusal, and the third shows the ladder scoring zero on a payload that
is not a string anywhere in the pipeline.

---

## §6 Request budget

**Zero provider requests, to every provider.**

| Provider | Requests today | Against |
| --- | --- | --- |
| Google AI Studio (Gemini) | 0 | free tier |
| Groq | 0 | 30 RPM / 250 RPD, observed 2026-09-05 |
| OpenRouter `:free` | 0 | free tier |
| Ollama (local) | 0 | n/a |

`_desk.py` is a scripted agent: it runs real ADK agents and real callbacks with a stand-in model that
returns a fixed script, so every callback position, return value and error path is exercised by the
actual runtime while no provider is contacted. The model judge in section 6.1 is scripted for the same
reason, and its part says so where the number is reported.

The counts the day **reports** are still real request counts — part 1.2's seven-instead-of-fourteen is
what the ladder would spend against a provider — because a guardrail priced in imaginary units cannot
be ordered. Nothing today spends them.

---

## §7 Traps

1. **Naming your callback parameters yourself.** ADK calls callbacks **by keyword**, so
   `def guard(ctx, req)` raises `TypeError` on the first request instead of guarding. The type alias
   says positional and neither an editor nor a type checker will warn you — part 2.4.
2. **Refusing with a falsy value.** The runtime stops walking a callback list only on a **truthy**
   result and overwrites its running answer with every callback it visits, so a guardrail returning
   `{}` is silently overridden by a later one returning `None` — part 2.5.
3. **Checking the prose instead of the tool call.** The dangerous half of a model's output is the
   function call, whose arguments are the action. Only `before_tool_callback` can see it — part 4.1.
4. **Rewriting text and letting it through.** No event, and a log line describing text that was never
   received — part 4.3.
5. **Returning a value from an error hook.** This is the master plan's §5.1 trap **#4**: it stops the
   exception and substitutes your value as the tool's result, so an unreachable archive is reported to
   the customer as *"no prior tickets"*. Observe, then re-raise — part 4.4, Principle 10.
6. **Reporting a detection rate without a false-alarm rate.** 6 of 6 is true and is compatible with
   flagging every ticket the desk receives — part 5.1.
7. **Adding the escaped payload's words after an incident.** Detection 6→6, wrongly blocked 1→3, and
   the change is approved in every review because it is responsive to what happened — part 5.3.
8. **Believing a detection rate measured on fixtures you wrote.** 6 of 6 becomes 2 of 5 when somebody
   who has read the checks writes the payloads — part 5.4.
9. **Letting a model judge have the last word.** It is a language model reading attacker-written text,
   and it can be addressed directly. A judge belongs in the middle of the ladder, never at the end —
   part 6.1.
10. **Not knowing which way your guardrail fails when it throws.** Measured on ADK 2.7.1 it is
    fail-closed, and that is the framework's decision rather than yours until you write it down —
    part 6.2.

---

## §8 Verify before you code

Fetched on 2026-09-06:

| What | Where | What it said |
| --- | --- | --- |
| Callback types | <https://adk.dev/callbacks/types-of-callbacks/> | Eight for `LlmAgent`: `before_agent_callback`, `after_agent_callback`, `before_model_callback`, `after_model_callback`, `on_model_error_callback`, `before_tool_callback`, `after_tool_callback`, `on_tool_error_callback` |
| Parameter naming | <https://adk.dev/callbacks/types-of-callbacks/> | Verbatim: *"In Python, callback function parameter names must match the documented names exactly because ADK passes callback arguments by keyword."* — the fact part 2.4 is built on |
| `arXiv:2503.18813` record | <https://arxiv.org/abs/2503.18813> | Title *Defeating Prompt Injections by Design*, 2025 — copied into `docs/PAPERS.md` and the paper document, never from memory (§17.4.1 rule 5) |
| `google-adk` latest | <https://pypi.org/pypi/google-adk/json> | `2.8.0`; this repo pins `2.7.1`, carried forward as the Day 65 freshness finding rather than upgraded mid-phase (Principle 14) |

Every ADK behaviour this day depends on beyond the documented list was **measured** rather than read:
that a callback field accepts a list and the runtime stops at the first truthy result (part 2.3), that
a falsy refusal is overwritten (part 2.5), and that an exception inside a callback propagates and
stops the run (part 6.2). Those are runtime facts, they are pinned to `2.7.1`, and each part shows the
command that produced them.

---

## §9 Say it in an interview

*"We built layered guardrails for prompt injection and the useful part was measuring them. ADK gives
you eight callback positions, and choosing one is choosing what the check can see — an output check
that reads the model's prose is reading the half that can't hurt anyone, because the dangerous half is
the tool call and its arguments. We ordered the ladder cheap and deterministic first, which halved the
model calls it cost. Then the measurement: six of six on our hostile fixtures, which is the number
everybody reports, and one in eight benign tickets flagged — and the one it flagged was a customer
asking whether an error banner was ours, refused for quoting the banner. At a realistic base rate that
filter refuses about a hundred and twenty real customers per attack it stops. Then we measured it
against someone who had read the checks: two of five rewrites of the identical instruction, and zero
when the payload was split across two retrieved rows, because the phrase never exists as a string
anywhere — it only exists in the reading. The model judge helps and it's a model reading the
attacker's text, so it can be talked out of its verdict, and defending it means adding another reader,
which doesn't terminate. So the ladder is worth having for cost, coverage of the lazy attacker and the
audit record, and the thing that actually closes a channel is a rule that never reads text — a
capability you don't hold, or a value refused at the sink because of where it came from."*

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, and you have run the commands rather than read
them. `./m done 67` refuses to commit until they are.

The day is finished when you can state, without looking, both of the ladder's columns and both of its
detection numbers — the one on your own fixtures and the one against somebody who read the checks —
and when you can say what a guardrail is for in a sentence that does not contain the word "stops".

---

## §11 Ledger & commit

**`docs/PROGRESS.md`** — append this row:

```text
| 67 | 2026-09-06 | SEC-08, SEC-09 | 24 | <hash> | ⚠️ |
```

The gate column is `⚠️` and means it. `./m depth 67` is green over the twenty-four parts and the
paper. `lab/gate.py` is **red** on all six checks by design — `sutra/guardrails.py` is the build
brief. The repository-wide `⚠️` carried since Day 15 is unchanged: `tests/test_persona.py` still fails
ruff `I001`, and it is the learner's own file, which no generated day may edit.

**`docs/PACKAGES.md`** — no new rows. No package is added today; `google-adk==2.7.1` is the Day 7 pin
and PyPI's current `2.8.0` stays recorded as the Day 65 freshness finding.

**`docs/PAPERS.md`** — one row, checked live today:

```text
| Defeating Prompt Injections by Design | arXiv:2503.18813 | 2025 | 2026-09-06 | 67 | `days/day-67-guardrail-callbacks/papers/01-defeating-prompt-injections-by-design.md` |
```

**`docs/SKILL_PROVENANCE.md`** — no new rows. No third-party skill is used today.

**Commit:**

```text
day 67: defense in depth - input and output guardrail callbacks - closes SEC-08, SEC-09
```

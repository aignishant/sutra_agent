# Day 16 — CHECKLIST

**IDs closed:** ADK-18, AG-07, AG-32, SEC-01
**Principles served:** 1, 2, 4, 6, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18
**Parts:** 24 across 8 sections, plus 1 paper

> `./m done 16` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
cd days/day-16-built-in-tools-with-brakes/lab
uv run python two_switches.py
uv run python bypass.py
uv run python byte_offsets.py
uv run python two_meters.py
uv run python executes_nothing.py
uv run python unsafe.py
uv run python no_timeout.py
uv run python swapped.py
uv run python ground.py            # spends 1 model request + 1-2 search requests
uv run python compute.py           # spends 1-3 model requests
cd papers/program-aided-language-models
PAL=1 uv run python pal.py         # spends 3 model requests
PAL=0 uv run python pal.py         # spends 3 model requests
cd -
uv run python -m pytest tests/test_builtins.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: one agent with a tool and no executor beside one with an executor and no tools; a flag that
renames a tool and hides an agent behind it; a highlight that starts one letter late; six grounded
tickets a day; an executor that returns `None`; five API keys read by code a model could have written;
a bound that is off by default; a fallback provider that refuses both capabilities; then a grounded
answer with real URLs; then a program and the number it printed; then the paper's two arms; then
`7 passed, 1 skipped`; then `OK all green`, then `traceability: 31/199 closed, 0 problem(s)`, then one
commit reading `day 16: built-in tools with brakes - closes ADK-18, AG-07, AG-32, SEC-01`.

---

## Before you write anything

- [ ] `./m check` is green and `scripts/trace.py` shows Day 15's count before you change anything
- [ ] Read the whole day before running the three scripts that spend requests — there are eighteen that
      cost nothing and they carry most of the findings
- [ ] Can say why a scripted model cannot stand in for either of today's capabilities
- [ ] Know the two meters and their periods before spending either of them (4.4)

## Section 1 — what a built-in tool is

- [ ] Ran `two_switches.py` and saw one agent with a tool and no executor, one with the reverse (1.1)
- [ ] Can name the three ways Sutra has gained a power, and who runs each (1.1)
- [ ] Called `google_search()` and read `TypeError: 'GoogleSearchTool' object is not callable` (1.1)
- [ ] Tried `from google.adk.tools import BuiltInCodeExecutor` and read the `AttributeError` (1.1)
- [ ] Ran `placeholder.py` and saw `google_search declaration : None` beside a real declaration (1.2)
- [ ] Can say why rewriting a built-in's description changes nothing (1.2)
- [ ] Ran `the_request.py` and saw `{"google_search":{}}` — the whole switch (1.3)
- [ ] Can say what your traces will and will not contain for a grounded call (1.3)

## Section 2 — the exclusivity rule

- [ ] Ran `the_wall.py` and watched ADK build the forbidden agent without complaint (2.1)
- [ ] Can quote the exclusivity rule and name the layer that does **not** enforce it (2.1)
- [ ] `LIVE=1 uv run python the_wall.py` on a day with quota, and pasted the real refusal into 2.1 (2.1)
- [ ] Ran `bypass.py` and compared the three blocks (2.2)
- [ ] Can say what `bypass_multi_tools_limit=True` actually does, and its two costs (2.2)
- [ ] Noticed that the flag does nothing when the `tools` list has one entry (2.2)
- [ ] Ran `specialist.py`, then deleted the `description=` line and ran it again (2.3)
- [ ] Can say which single argument decides whether a referral keeps its citations (2.3)
- [ ] Tried `AgentTool.create(...)` and read the `AttributeError` the docs page does not warn about (2.3)

## Section 3 — the receipts

- [ ] Ran `ground.py` once and pasted its real output into 3.1 (3.1)
- [ ] Sources block shows real titles and URLs you can open (3.1)
- [ ] Can name the two different reasons a sources block comes back empty, and the field that separates
      them (3.1)
- [ ] Ran `byte_offsets.py` and saw the missing `L` (3.2)
- [ ] Removed the `ü` and watched the bug disappear — which is how it hides (3.2)
- [ ] Ran `render_sources.py` and confirmed no metadata renders nothing at all (3.3)
- [ ] Deleted the `len(lines) > 1` guard and read the empty heading (3.3)
- [ ] Looked at the real `uri` values from your own run and decided what your interface will show (3.3)

## Section 4 — grounding or retrieval

- [ ] Can give one Sutra question that only grounding answers, one that only retrieval answers, and one
      that needs both (4.1)
- [ ] Can name the four axes that separate them, and which one is a hard rule (4.2)
- [ ] Ran `routing.py` and read the referral's description as if you were the desk's model (4.2)
- [ ] Ran `redact.py` and found the two things the redactor still leaks (4.3)
- [ ] Can say why Sutra sends a composed question rather than a redacted ticket (4.3)
- [ ] Ran `two_meters.py` and can say which meter binds, and by how much (4.4)
- [ ] Changed `MODEL_CALLS_PER_GROUNDED_TICKET` to `1` and watched the capacity change (4.4)

## Section 5 — code execution

- [ ] Ran `executor_not_tool.py` and read both pydantic errors (5.1)
- [ ] Can say which of the four constructions you would refuse in review, and why it did not fail (5.1)
- [ ] Ran `executes_nothing.py` and saw `execute_code() -> None` (5.2)
- [ ] Can name the two things the SDK's own types tell you about the provider's sandbox (5.2)
- [ ] Ran `compute.py` and pasted its real output into 5.3 (5.3)
- [ ] Checked the model's answer against the program's printed output, by eye (5.3)
- [ ] Ran `expected.py` and compared both percentile definitions with what the model said (5.4)
- [ ] Can explain, to someone who has never used a model, why "be careful with arithmetic" is not a fix
      (5.4)

## Section 6 — blast radius

- [ ] Ran `unsafe.py` and read the list of variable names model-written code could have read (6.1)
- [ ] Can say what a `spawn` child inherits, and which line of an agent decides whether it sees it (6.1)
- [ ] Ran `no_timeout.py` and saw `default timeout_seconds: None` (6.2)
- [ ] Can list the five denials, and grade both executors against them from memory (6.2)
- [ ] Wrote `docs/adr/ADR-0009-code-execution-policy.md`, including a consequences section that names
      something Sutra can no longer do (6.3)
- [ ] Can state SEC-01 in one sentence without reading it (6.3)

## Section 7 — the failure lab

- [ ] Ran `swapped.py` and read both refusals (7.1)
- [ ] Changed `FALLBACK` to the Ollama string and confirmed the same refusal (7.1)
- [ ] Can say why a provider swap does not carry a built-in, in one sentence (7.1)
- [ ] Wrote down which of Sutra's agents can fail over and which cannot, and where Day 70's router will
      read that from (7.1)
- [ ] Can say what the researcher should tell an engineer when it cannot search — and why "answer
      anyway" is the wrong choice (7.1)

## Section 8 — production

- [ ] `tests/test_builtins.py` written and green: `7 passed, 1 skipped` (8.1)
- [ ] Can say why the exact-list assertion is used instead of a membership check (8.1)
- [ ] Read the skip reason and left the `TODO(me)` in place (8.1)
- [ ] Re-checked the grounding allowance on the pricing page **today** and added the dated row to
      `docs/PACKAGES.md` (8.2)
- [ ] Can name what the MCP search fallback would give Sutra and what it would take away (8.2)
- [ ] Can list the seven review questions for a built-in without scrolling (8.3)
- [ ] `grep -rn "Blast radius" sutra/` finds the new module (8.3)

## The paper — after the parts

- [ ] Read `papers/01-program-aided-language-models.md` **after** finishing the parts (P4 at day scale)
- [ ] Ran both arms: `PAL=1` and `PAL=0`, and read both transcripts
- [ ] Can say what PAL claimed, in one sentence, without using the word "prompt"
- [ ] Can name one thing from the paper that survived and one that the field dropped
- [ ] Can say what the paper never addressed that section 6 spent three parts on

## The build

- [ ] `sutra/builtin_tools.py` written: every symbol in the hub's §4 table
- [ ] Module docstring carries `Blast radius:` and `Rules this module is under:`
- [ ] `researcher` holds exactly one entry on its `tools` list, and you can say why
- [ ] `referral()` passes `propagate_grounding_metadata=True`, and you can say what breaks without it
- [ ] `git diff` confirms nothing under `sutra/desk/` changed unless you decided it should

## Tests

- [ ] Watched the suite fail at collection **before** writing the module
- [ ] Added a second tool to `researcher` and confirmed **2** tests go red
- [ ] Dropped `propagate_grounding_metadata=True` and confirmed the referral test goes red
- [ ] Imported `UnsafeLocalCodeExecutor` in `sutra/` and confirmed the SEC-01 test goes red — then
      removed it
- [ ] `./m check` prints `OK all green`
- [ ] `./m depth 16` passes

## Request budget

- [ ] Model requests spent today: **≤ 10 of 20** — write down the number you actually used
- [ ] Search requests spent today: **1–2 of 5,000** — and you know which page publishes that allowance
- [ ] No script invented a result when a call failed; every 429 exited non-zero

## Phase 2 gate

- [ ] Freshness check done: `google-adk` release notes since Day 5, the MCP specification revision, and
      all three providers' free limits
- [ ] The gate's own words are true: four free providers benchmarked (Day 9), built-in tools contained
      (the seven questions in 8.3)
- [ ] Any drift found was amended **first**, in a dated addendum row plus `docs/CHANGELOG_PLAN.md`, and
      only then in code (Principle 14)

## Ledger & commit

- [ ] `docs/PROGRESS.md` row appended, with the date and hash you actually observed
- [ ] `docs/PACKAGES.md` row appended for the grounding allowance, with today's date
- [ ] `docs/PAPERS.md` row for `arXiv:2211.10435` is present
- [ ] `docs/adr/ADR-0009-code-execution-policy.md` committed
- [ ] `git status` glance: no `.env`, no key in any lab script's output that you pasted into a part
- [ ] Committed as `day 16: built-in tools with brakes - closes ADK-18, AG-07, AG-32, SEC-01`

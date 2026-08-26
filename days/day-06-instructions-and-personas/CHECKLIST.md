# Day 6 — CHECKLIST

**IDs closed:** ADK-03, AG-05
**Principles served:** 1, 2, 4, 8, 10, 11, 12, 13, 15, 16, 17, 18
**Parts:** 19 across 6 sections, plus 1 paper

> `./m done 6` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run adk web sutra/desk
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: a conversation in the browser whose events show the six-section handbook; then `OK all
green`, then `traceability: 12/199 closed, 0 problem(s)`, then one commit reading
`day 06: instructions & personas - the string the framework did not take - closes ADK-03, AG-05`.

---

## Before you spend a single request

- [ ] `./m check` is green and `scripts/trace.py` shows Day 5's count before you change anything
- [ ] Wrote `lab/show_instruction.py` (part 1.1) **first**, and ran it against the unchanged agent
- [ ] Read the four carried-over sentences as a handbook and can name which two of the six sections
      they partly cover
- [ ] Can say why `lab/show_instruction.py` costs zero requests, and why nothing in `sutra/` may import
      what it imports

## AG-05 — writing the handbook (section 1)

- [ ] Can state the one test that decides whether a line belongs, from memory (1.1)
- [ ] `INSTRUCTION` rewritten with all six sections, in order: Role, Scope, Refusal, Honesty, Tone,
      Example (1.2)
- [ ] The Scope section has a **closed** list — something is genuinely outside it (1.2)
- [ ] The Refusal section gives the **words to say**, not a prohibition and not an explanation (1.2)
- [ ] The Honesty section states the **absence**: no database, no knowledge base, no search (1.2, 6.1)
- [ ] The Tone section carries a **number**, not just adjectives (1.2)
- [ ] There is exactly **one** example, and you re-read it against every rule above it (1.2)
- [ ] No output-format section, no JSON shape, no "reply with" — checked, not assumed (1.3)
- [ ] Ran the protocol-smell check against `INSTRUCTION` **and** against Day 3's prompt in
      `sutra/loop.py`, and can say why the two differ (1.3)
- [ ] Ran `lab/collision.py` on a data-loss ticket and looked for **two clusters**, not a spread (1.4)
- [ ] Decided the `TODO(me)`: does Sutra's tone budget need a precedence clause? Wrote the decision
      down, whichever way it went (1.4)
- [ ] Ran `lab/weigh.py` and read the **per-conversation** column, not the per-turn one (1.5)
- [ ] Took the most expensive section and the cheapest, and named the probe for each. At least one
      surprised you (1.5)

## AG-05 — testing the persona (section 2)

- [ ] `lab/probes.py` written, with `fails_if` filled in **before** any probe was sent (2.1)
- [ ] Every non-heading line of the handbook is either covered by a probe or was deliberately deleted —
      no line left marked `NONE` and undecided (2.1)
- [ ] Deleted a line, re-ran its probe, and confirmed the probe actually goes red without it (2.1)
- [ ] Sent probe 0 (scope) **on its own**, read the whole answer, wrote a verdict (2.2)
- [ ] Sent probe 1 (honesty) **on its own**, read the whole answer, wrote a verdict (2.2)
- [ ] Sent probe 2 (happy path) **on its own**, read the whole answer, wrote a verdict (2.2)
- [ ] Made the honesty probe **harder** the way 2.2 describes — a real ticket first, then a second one
      by number — and compared the two answers
- [ ] Recognised at least one **hedged near-miss** and did not round it up to a pass (2.2)
- [ ] After fixing whichever probe failed, **re-ran the other two** and confirmed they still pass (2.2)
- [ ] Can say why 2.2 made you judge by hand before automating anything (2.3)

## ADK-03 — the instruction fields (section 3)

- [ ] Rendered the instruction locally and can name the **two channels** a request has (3.1)
- [ ] Printed `request.contents` and saw it empty — and wrote down your prediction for what 3.3 would
      do to it (3.1)
- [ ] `description` rewritten in **third person**, answering all four questions including **what the
      agent is not for** (3.2)
- [ ] Read the description aloud as a one-second routing decision, and can say what a badly written one
      looks like from outside (3.2)
- [ ] Ran `lab/static_instruction.py` and watched `instruction` move into `contents` as a `role="user"`
      turn (3.3)
- [ ] Can say the **second** trap of `static_instruction` — the thing it does not do despite being the
      reason people set it (3.3)
- [ ] Ran `lab/global_instruction.py` and watched a child agent's `global_instruction` be **silently
      ignored** (3.4)
- [ ] Confirmed no `DeprecationWarning` is emitted, and can say why that matters for an upgrade (3.4)
- [ ] Confirmed Sutra sets **no** `global_instruction`, as a decision rather than an omission (3.4)

## ADK-03 — state templating (section 4)

- [ ] Ran `lab/templating.py` and can state the rule for what counts as a blank (4.1)
- [ ] Saw for yourself that `{{focus}}` **is** substituted — doubling does not escape (4.1)
- [ ] Saw that a JSON example survives, and can say which two characters are the difference (4.1)
- [ ] Added `{product}` to the handbook, watched the `KeyError` arrive **before any network call**, and
      took it out again (4.1)
- [ ] Ran `lab/contracts.py` and read the soft result's leftover punctuation: `focus: .` (4.2)
- [ ] Can state the question that decides hard from soft, and why "make everything optional" is the
      wrong lesson from an outage (4.2)
- [ ] Ran `lab/provider.py` and saw a callable deliver `{focus}` to the model as literal braces (4.3)
- [ ] Re-ran it with `focus` removed from state and confirmed the `KeyError` **did not** fire for the
      plain provider (4.3)
- [ ] Can name the function a provider has to call to get the behaviour back (4.3)

## ADK-03 — the dev UI (section 5)

- [ ] `uv run adk web sutra/desk` served the UI and `desk` appeared in the dropdown (5.1)
- [ ] Passed the **path** — and can say what a bare `adk web` offers in this repository instead (5.1)
- [ ] Sent **one** message, then stopped and read its events rather than chatting on (5.1)
- [ ] Found all three: the request's system instruction, the final response event, the timing (5.2)
- [ ] Compared the UI's rendered instruction against `lab/show_instruction.py` and can say why they
      agree today and when they would stop agreeing (5.2)
- [ ] Ran the two-request state experiment: `{focus?}` empty, then filled from the State panel (5.2)
- [ ] Removed the experiment line, **or** kept it with a comment saying why — a decision, not a
      leftover (5.2)
- [ ] Read `adk web --help`'s first paragraph off your own terminal (5.3)
- [ ] `netstat` shows `127.0.0.1:8000`, not `0.0.0.0:8000` (5.3)
- [ ] `git check-ignore -v sutra/desk/.adk/session.db` prints a rule — and you know what would be in
      that file if it did not (5.3)
- [ ] Can say what an attacker on the same network could do **beyond** reading your chats (5.3)

## 💥 Failure lab (section 6)

- [ ] Ran `lab/promised_equipment.py` and pasted **both** arms' output into the part's `TODO(me)`,
      verbatim, with the date and your `google-adk` version
- [ ] The two answers differ, and you can name the single clause responsible
- [ ] Can say why "be accurate and do not guess" does not fix it
- [ ] Fixed the real agent, and the structural test now catches the same bug for **zero** requests
- [ ] Checked whether the promise moved to `description` instead of being deleted (3.2, 6.1)

## Paper — read **after** the parts

- [ ] [01 — Training language models to follow instructions with human feedback](papers/01-instructgpt.md)
      (`arXiv:2203.02155`) read **after** section 6, not before
- [ ] Ran the demo both ways: `python bestofn.py` and `python bestofn.py --ablate`, and the two chose
      different candidates
- [ ] Changed one entry in `COMPARISONS` and watched the ranking move
- [ ] Can say why the humans were asked to **rank** rather than to score
- [ ] Can name what survived (comparison-based preference data, the reward model as judge) and what the
      field moved past (PPO)
- [ ] Can connect the paper to 6.1: the cooperativeness that makes a handbook work is the same one that
      fills a gap when the handbook is wrong

## Read every part

- [ ] [1.1 An instruction is a handbook, not a wish](parts/01-writing-the-handbook/1.1-handbook-not-a-wish.md)
- [ ] [1.2 The six sections a handbook needs](parts/01-writing-the-handbook/1.2-six-sections-of-a-handbook.md)
- [ ] [1.3 Protocol does not belong in prose](parts/01-writing-the-handbook/1.3-protocol-does-not-belong-in-prose.md)
- [ ] [1.4 Contradictions are randomised behaviour](parts/01-writing-the-handbook/1.4-contradictions-are-randomised-behaviour.md)
- [ ] [1.5 Every line is a tax](parts/01-writing-the-handbook/1.5-every-line-is-a-tax.md)
- [ ] [2.1 A line you cannot probe](parts/02-testing-a-persona/2.1-a-line-you-cannot-probe.md)
- [ ] [2.2 The three probes every persona owes](parts/02-testing-a-persona/2.2-the-three-probes.md)
- [ ] [2.3 When probes become an evalset](parts/02-testing-a-persona/2.3-when-probes-become-an-evalset.md)
- [ ] [3.1 Where your instruction lands](parts/03-the-instruction-fields/3.1-where-your-instruction-lands.md)
- [ ] [3.2 Two fields, two readers](parts/03-the-instruction-fields/3.2-two-fields-two-readers.md)
- [ ] [3.3 The static instruction that moves yours](parts/03-the-instruction-fields/3.3-the-static-instruction-that-moves-yours.md)
- [ ] [3.4 The deprecated global instruction](parts/03-the-instruction-fields/3.4-the-deprecated-global-instruction.md)
- [ ] [4.1 The instruction is a template, not a string](parts/04-state-templating/4.1-the-instruction-is-a-template.md)
- [ ] [4.2 Hard and soft contracts](parts/04-state-templating/4.2-hard-and-soft-contracts.md)
- [ ] [4.3 A callable turns templating off](parts/04-state-templating/4.3-a-callable-turns-templating-off.md)
- [ ] [5.1 The glass engine — `adk web`](parts/05-the-dev-ui/5.1-the-glass-engine.md)
- [ ] [5.2 Reading a turn's anatomy](parts/05-the-dev-ui/5.2-reading-a-turns-anatomy.md)
- [ ] [5.3 An unauthenticated server on your machine](parts/05-the-dev-ui/5.3-an-unauthenticated-server.md)
- [ ] [6.1 💥 The handbook that promised equipment](parts/06-failure-lab/6.1-the-handbook-that-promised-equipment.md)
- [ ] Answered each part's out-loud question **without scrolling up**

## Tests — including ones you watch go red

- [ ] `test_the_handbook_has_all_six_sections` passes
- [ ] `test_the_handbook_promises_no_equipment_the_agent_lacks` passes
- [ ] `test_no_template_variable_is_unguarded` passes
- [ ] Solved the `TODO(me)` fourth test — the Tone section states its budget numerically
- [ ] **Broke it on purpose:** renamed `# Refusal` to `# Boundaries` and watched the first test go red
- [ ] **Broke it on purpose:** put `search the knowledge base` back and watched the second go red —
      the same failure the lab spent two requests on, caught for zero
- [ ] **Broke it on purpose:** rewrote the length budget as "keep it brief" and watched your fourth
      test go red
- [ ] The `live`-marked behavioural test exists, is skipped by the default gate, and you ran it once
      deliberately
- [ ] `uv run python -m pytest -q -m "not live"` is green and needs **no key**
- [ ] `uv run ruff check .` and `uv run ruff format --check .` are clean

## Budget

- [ ] Ran the **free** things first — renders, weigh, templating, structural tests
- [ ] Sent probes one at a time, never pasted three into a chat box
- [ ] Wrote down roughly how many requests the day actually cost, against the ~13 estimated
- [ ] If a 429 appeared, stopped rather than retrying, and noted which parts were left for tomorrow

## Verify (Principle 8)

- [ ] Re-fetched `adk.dev/agents/llm-agents/` and `adk.dev/runtime/web-interface/` **today**
- [ ] Confirmed `arxiv.org/abs/2203.02155` resolves to the title in `docs/PAPERS.md`
- [ ] Re-ran the three claims no page states — `static_instruction.py`, `global_instruction.py`,
      `provider.py` — against **your** installed version
- [ ] If anything disagreed with a part, **your terminal won** and you fixed the document

## Ledger & commit

- [ ] `docs/PROGRESS.md` — row appended with the real date and the real commit hash
- [ ] `docs/PACKAGES.md` — no new rows, **unless** your own `google-adk` lookup differs from 2.7.1
- [ ] `docs/PAPERS.md` — the `arXiv:2203.02155` row is present and its identifier resolves
- [ ] `./m depth 6` passes
- [ ] `./m trace` shows ADK-03 and AG-05 closed, and no open ID from a completed phase
- [ ] `./m check` green
- [ ] Committed as
      `day 06: instructions & personas - the string the framework did not take - closes ADK-03, AG-05`
- [ ] Wrote the commit hash back into the `PROGRESS.md` row

# Day 4 — CHECKLIST

**IDs closed:** AG-04
**Principles served:** 1, 2, 4, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18
**Parts:** 16 across 7 sections

> `./m done 4` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run python -m sutra.agent "Ticket 4521 says the user keeps getting logged out. What should we tell them?"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: a three-step trace whose `FINAL` names `KB-104` and `SameSite`; then `OK all green`, then
`traceability: 7/199 closed, 0 problem(s)`, then one commit reading
`day 04: tools by hand - schemas, the call, the result turn - closes AG-04`.

---

## Setup — nothing is installed today

- [x] `uv run python -c "from sutra.loop import TOOLS, _cost_table, _user_turn"` succeeds — Day 3
      actually landed
- [x] `sutra/tools.py`, `sutra/agent.py` and `tests/test_agent.py` created
- [x] **`pyproject.toml` and `uv.lock` are unchanged** — and you can say why function calling needed
      no package
- [x] **`sutra/loop.py` is unchanged** — `git diff sutra/loop.py` is empty, and you can give two
      reasons Day 3's file is being kept
- [x] `./m check` was green **before** you started writing

## AG-04 — the schema (section 1)

- [x] Wrote a declaration by hand and can name its four top-level keys
- [x] Can say which key the *model* reads and which three the *provider* enforces
- [x] Can explain the two different `type` keys and which level each sits at
- [x] `required` is beside `properties`, not inside the field — and you can say why
- [x] Wrote the `search_kb` declaration yourself (the `TODO(me)`) and **decided about `enum` on
      `query`**, with a reason you can state
- [x] Every description answers all four questions: what, when, what comes back, when *not*
- [x] At least one field description carries a concrete example, and you can say why an example beats
      a sentence
- [x] Can say what a schema guarantees about `ticket_id` and two things it cannot

## AG-04 — the round trip (section 2)

- [x] Printed `interaction.steps` and saw a `'function_call'` — and saw `output_text` come back `None`
- [x] Can say what moved out of the text channel today, and precisely what that prevents an attacker
      from doing
- [x] Can say what it leaves **completely** untouched (the jury)
- [x] Read a real step's `.name`, `.arguments` and `.id`, and confirmed `arguments` is a **dict**
- [x] `_dispatch` takes the step and uses `tool(**call.arguments)`
- [x] Can name the new coupling that `**` creates, the error it produces, and whose bug that is
- [x] `_result_turn` echoes `call_id` from the call object, and wraps output in a **list** of blocks
- [x] Did **not** `json.dumps` a string that was already a string
- [x] Model steps are appended with `model_dump()` — you never construct a model turn
- [x] Day 3's `_model_turn` is **not** used by `sutra/agent.py`
- [x] Can say what `store=False` obliges you to send, and what you are declining by not using
      `previous_interaction_id`

## AG-04 — rebuilding the loop (section 3)

- [x] `ask` gained **one** keyword-only `tools` parameter, defaulting to `None`
- [x] `grep -rn "interactions.create" sutra/ | wc -l` prints `1`
- [x] Can name the four guarantees inside `ask` and which one a direct SDK call breaks *silently*
- [x] `tools=DECLARATIONS` is passed **inside** the loop, on every call
- [x] Can list three things the loop deleted and three that survived untouched
- [x] Noticed the `THOUGHT:` trace is gone, and can say what that costs
- [x] The loop reads **all** `function_call` steps, not just the first
- [x] Every call gets a result appended before the next model call — including failures
- [x] Carried each call through to its own result; **no `zip(calls, results)`**
- [x] Can say why Sutra steers *against* parallel calls for its own two tools

## AG-04 — the limits (section 4)

- [x] Ran the transposed id (`4512`) and the agent **reported the miss**
- [x] If it diagnosed anyway, wrote the sentence down — that is eval entry two
- [x] Can name the three layers of validation and which one moved upstream today
- [x] Can say which metric in a normal dashboard reveals a well-typed wrong argument (none)
- [x] Saw a run where no tool was called, and worked the diagnosis list **in order**
- [x] Can say what `tool_choice: "any"` on every call does to a loop, and why it looks like a confused
      model
- [x] Did **not** reach for `tool_choice` before checking tools-sent, trigger clause, and temperature

## AG-04 — containment (section 5)

- [x] `test_declared_and_dispatchable_are_the_same_set` passes, asserting **equality** not subset
- [x] Can say which direction of drift is dangerous and why it produces no output at all
- [x] Can answer "what can this agent do?" in **one command**
- [x] Can say why a caller identity must never be a declared parameter
- [x] Can describe what a ticket body saying "see also ticket 8801" does to a tool with no authority
      check
- [x] Can state Sutra's containment story today in one sentence, without hedging
- [x] Can say why per-call authorisation does not bound a whole run

## 💥 The failure lab (section 6)

- [x] Forced a turn with **two** calls and swapped the results on purpose
- [x] Read all three passes of the trace: the impossible pairing, the model retrying, the honest
      hedge
- [x] Printed the asked-vs-answered pairs and saw the mismatch directly
- [x] Can say why this bug is invisible with one call and ordinary with two
- [x] **Restored the pairing.** `grep -n "the failure lab" sutra/agent.py` prints nothing
- [x] Can say why an id-only assertion would not have caught it

## 🅿️ Parked (section 7)

- [x] Can describe what automatic function calling does, in one sentence
- [x] Can give **both** reasons Sutra declines it — the fact and the principle
- [x] Can name four seams your loop has that a hidden loop would have to expose, and the day each is
      cashed in
- [x] Can say how declining it differs from adopting ADK tomorrow
- [x] `grep -rn "generate_content" sutra/ | wc -l` prints `0`

## Read the parts — one box each

Tick only when you have **read it, run its Check yourself, and answered its out-loud question**.

- [x] [1.1 The form that rejects itself](parts/01-the-schema/1.1-the-form-that-rejects-itself.md)
- [x] [1.2 Declaring a tool](parts/01-the-schema/1.2-declaring-a-tool.md)
- [x] [1.3 The description is the prompt](parts/01-the-schema/1.3-the-description-is-the-prompt.md)
- [x] [2.1 Two channels, not one](parts/02-the-round-trip/2.1-two-channels-not-one.md)
- [x] [2.2 The call comes back parsed](parts/02-the-round-trip/2.2-the-call-comes-back-parsed.md)
- [x] [2.3 The tool-result turn](parts/02-the-round-trip/2.3-the-tool-result-turn.md)
- [x] [2.4 Re-send the steps as received](parts/02-the-round-trip/2.4-resend-the-steps-as-received.md)
- [x] [3.1 One door, one new parameter](parts/03-rebuilding-the-loop/3.1-one-door-one-new-parameter.md)
- [x] [3.2 The loop that shrank](parts/03-rebuilding-the-loop/3.2-the-loop-that-shrank.md)
- [x] [3.3 Two calls in one turn](parts/03-rebuilding-the-loop/3.3-two-calls-in-one-turn.md)
- [x] [4.1 Validated is not correct](parts/04-the-limits/4.1-validated-is-not-correct.md)
- [x] [4.2 The tool that is never called](parts/04-the-limits/4.2-the-tool-that-is-never-called.md)
- [x] [5.1 The declaration is the new boundary](parts/05-containment/5.1-the-declaration-is-the-new-boundary.md)
- [x] [5.2 The argument a schema cannot check](parts/05-containment/5.2-the-argument-a-schema-cannot-check.md)
- [x] [6.1 💥 The call id you did not echo](parts/06-failure-lab/6.1-the-call-id-you-did-not-echo.md)
- [x] [7.1 🅿️ Automatic function calling, declined](parts/07-the-automatic-door/7.1-automatic-function-calling-declined.md)

### The paper — read after the parts

- [x] [*Toolformer: Language Models Can Teach Themselves to Use Tools*](papers/01-toolformer.md)
      — ran the filter **both ways**, and can state the paper's premise and its method as two
      separate sentences, saying which one today implemented

## Tests — including ones you watch go red

- [x] `test_declared_and_dispatchable_are_the_same_set` passes
- [x] `test_declared_properties_bind_to_the_real_signatures` passes
- [x] `test_required_names_only_declared_properties` passes
- [x] `test_result_turn_echoes_the_call_id_and_wraps_in_a_list` passes
- [x] `test_an_unknown_tool_comes_back_as_text` passes
- [x] `test_the_step_budget_is_still_a_hard_ceiling` passes
- [x] Solved the `TODO(me)` eighth test — two calls, two results, ids **and content** asserted
- [x] **Broke it on purpose:** renamed `ticket_id` to `ticketId` in the declaration only; watched the
      bind test go red; put it back
- [x] **Broke it on purpose:** added a key to `TOOLS` with a stub; watched the set-equality test go
      red; noted that nothing else would have told you
- [x] **Broke it on purpose:** made `_result_turn` return a bare string; watched the shape assertion
      catch it
- [x] `uv run python -m pytest -q -m "not live"` is green and needs **no key**
- [x] `uv run ruff check .` and `uv run ruff format --check .` are clean

## Budget

- [x] Ran the demos one at a time
- [x] Ran the `tool_choice: "any"` experiment with `max_steps=2`, not the default
- [x] If a 429 appeared, watched Day 2's wrapper read the server's stated delay and wait it out
- [x] Wrote down roughly how many calls the day actually cost, against the ~25 estimated

## Verify (Principle 8)

- [x] Re-fetched `ai.google.dev/gemini-api/docs/function-calling` **today**, not trusting §8's table
- [x] Printed a real `function_call` step's `model_dump()` and compared its fields against this day
- [x] If anything disagreed, **the object won** and you wrote a dated note

## Ledger & commit

- [x] `docs/PROGRESS.md` — row appended with the real date and the real commit hash
- [x] `docs/PACKAGES.md` — **no new row**, and `uv.lock` confirmed unchanged
- [x] `./m depth 4` passes
- [x] `./m trace` shows AG-04 closed and no open ID from a completed phase
- [x] `./m check` green
- [x] Committed as `day 04: tools by hand - schemas, the call, the result turn - closes AG-04`
- [x] Wrote the commit hash back into the `PROGRESS.md` row

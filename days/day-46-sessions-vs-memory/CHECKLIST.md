# Day 46 — Definition of done

`./m done 46` refuses to commit until every box is ticked. Tick a box only when you have actually run
the thing, not when you have read it.

## Before you start

- [ ] Day 45's parts and checklist are done, and `tools/mcp_audit.py` runs. Phase 6 is closed.
- [ ] You have re-read Day 17's
      [2.2](../day-17-state-scopes-and-lifetimes/parts/02-four-lifetimes/2.2-an-invocation-is-not-a-session.md)
      and [2.3](../day-17-state-scopes-and-lifetimes/parts/02-four-lifetimes/2.3-where-user-and-app-live.md)
      — the four lifetimes, and the `user:` scope that lives *"not on the session at all"*. Today is
      the day that sentence gets a service behind it.
- [ ] `python -c "import google.adk.memory as m; print(m.__all__)"` prints four names:
      `BaseMemoryService`, `InMemoryMemoryService`, `VertexAiMemoryBankService`,
      `VertexAiRagMemoryService`. If it does not, stop and read the installed package before writing
      anything (Principle 8).
- [ ] `lab/` scaffolded per §3 — twenty-one scripts and `lab/papers/generative-agents/`.
- [ ] `sutra/memory/` created, with an empty `__init__.py` and an empty `service.py`.

## Section 1 — the line (ADK-27)

- [ ] **1.1** read · ran both arms of `island.py` · **`memory search results : 0` against `2`** for
      the identical second session · can say in one sentence what a session is and what memory is,
      without using either word twice
- [ ] **1.2** read · ran `putfind.py` · saw `state['cause'] -> KeyError('cause')` next to
      `'the customer' -> 2 memories` · can say why an absent key is a **better** failure than a
      plausible match
- [ ] **1.3** read · ran both arms of `optin.py` · **three sessions held, zero memories returned**
      until `--file` · **wrote down when Sutra should file a session**, and what each choice stores
      that the others do not

## Section 2 — the interface (ADK-27)

- [ ] **2.1** read · ran `surface.py` · read **both** `NotImplementedError` messages in full · deleted
      `BareMinimum.search_memory` and read the `TypeError: Can't instantiate abstract class`
- [ ] **2.2** read · ran both arms of `swap.py` · saw `'sign-in trouble' -> 0 memories` on the shipped
      service and a hit on the synonym one · can say what the interface deliberately does **not**
      promise
- [ ] **2.3** read · ran `entry.py` · saw the five fields, `timestamp` as a **`str`**, and the list of
      what did not come back · decided what must be **inside the text** of a filed event for a
      retrieved memory to be actionable
- [ ] **2.4** read · ran `scope.py` · saw the four-row table and the three buckets that exist ·
      **decided who the user is** — agent, customer or desk — and wrote the reason and the date beside
      the decision

## Section 3 — three wires (ADK-28)

- [ ] **3.1** read · ran both arms of `wiring.py` · read the traceback ending
      `ValueError: Memory service is not available.` in full · can say why the service is an argument
      to `Runner` and not to `Agent`
- [ ] **3.2** read · ran both arms of `filing.py` · **`memory holds: 2 events` then `4 events` —
      replaced, not appended** · can say what that means for a desk that files after every turn
- [ ] **3.3** read · ran both arms of `asked.py` · saw `TOOL CALL load_memory({'query': 'logged
      out'})` in one arm and **nothing at all** in the other · noted the system instruction at **219
      characters** · wrote the desk instruction that tells the model past cases exist
- [ ] **3.4** read · ran both arms of `pushed.py` · saw the `<PAST_CONVERSATIONS>` block in
      **request 0**, before any turn · noted the instruction at **63 characters** · found the
      `WARNING:root:` line and can say why a project configuring `google_adk` never sees it

## Section 4 — the choice (ADK-28)

- [ ] **4.1** read · ran all three arms of `price.py` · **1,898 for `preload_memory` against 3,130 and
      7,927 for `load_memory`** at one and five lookups · saw **10,705 tokens** at thirty uncapped
      cases fall to **1,425** when capped · can say why a tool result costs more than the tokens it
      contains
- [ ] **4.2** read · ran `verdict.py` and saw it **red** — `findings: 1`, `exit: 1` · can state all
      five rules · can defend rule 1 against the measurement in 4.1 · chose `TOP_K` and
      `MAX_LOOKUPS_PER_INVOCATION` **with the budget each was sized against written beside it**

## Section 5 — the failure lab (ADK-28)

- [ ] **5.1** read · ran both arms of `wrongpast.py` · **4 of 4 matched, KB-201 sent for a login
      fault** · reordered `ARCHIVE` so 4521 is first and watched the answer become correct with no
      change to the retrieval · can say why capping at three does not fix it
- [ ] **5.2** read · ran `restart.py` · **10 memories then 0**, two different object addresses, no
      error · can name the four shapes this failure arrives in, and which one is worse than a restart
- [ ] **5.3** read · ran both arms of `leak.py` · saw `<-- NOT BLUE PEAK'S` on a search made under the
      agent's id, and **one bucket become two** under `--per-customer` · wrote down what the desk can
      and cannot do under each bucket choice
- [ ] **5.4** read · ran both arms of `growth.py` · **500 filed, 500 matched, 10,588 tokens, 0.2%
      useful** against a flat **102 tokens** capped · can say the one thing the cap does **not** fix

## Section 6 — in production (ADK-27 · ADK-28)

- [ ] **6.1** read · ran `checks.py` — `findings: 0`, `exit: 0` · **made it go red on purpose** by
      changing assertion 7's query and saw `findings: 1`, `exit: 1` · changed it back · can say why a
      suite made entirely of "the bad thing did not happen" checks is not enough
- [ ] **6.2** read · ran `parked.py` · read both constructor signatures, and noted that
      `VertexAiRagMemoryService` takes `similarity_top_k` and `vector_distance_threshold` while
      `InMemoryMemoryService` takes **no arguments at all** · wrote the single condition that would
      un-park them, with a date

## The paper

- [ ] Read [`papers/01-generative-agents.md`](papers/01-generative-agents.md) **after** the parts
- [ ] Ran both arms of the demo: `KB-104 published: ...` ranks **third** under the three-term score
      and **sixth** under similarity alone, below `Agent went to lunch`
- [ ] Saw that seven of the nine rows tie at `0.00` in the ablated arm — a similarity-only retriever
      stops ranking past the first couple of hits
- [ ] Set that memory's importance to `1` and re-ran · said who or what would assign that rating in a
      real system, and what it would cost per filed ticket
- [ ] **Said out loud** the three terms in the retrieval score, which one Sutra cannot compute, and
      what reflection stores that an observation does not

## The project code

- [ ] `sutra/memory/__init__.py` and `sutra/memory/service.py` written, with `build_memory_service`,
      `MEMORY_TOOLS`, `TOP_K` and `MAX_LOOKUPS_PER_INVOCATION`
- [ ] You ran `verdict.py` **before** writing the module and saw it red
- [ ] `uv run python days/day-46-sessions-vs-memory/lab/verdict.py` prints `findings: 0` and `exit: 0`
- [ ] You broke exactly one rule on purpose — replaced `TOP_K` with a literal — and watched the
      finding appear
- [ ] `build_memory_service()` applies the cap; nothing outside it constructs a memory service
- [ ] The memory service is passed to `Runner`, never to an `Agent` and never held at module scope
- [ ] A lookup that returns nothing produces *"nothing matched these words"*, never *"there is no past
      case"* (Principle 10)

## The whole day

- [ ] Every `TODO(me)` in §4 has been **read**, and the ones you answered are written down somewhere
      that is not this checklist — especially **who the user is**, because Day 48 needs that answer
- [ ] `./m depth 46` is green
- [ ] `.venv/Scripts/ruff.exe check days/day-46-sessions-vs-memory/` passes
- [ ] `.venv/Scripts/ruff.exe format --check days/day-46-sessions-vs-memory/` passes
- [ ] `uv run python -m pytest -q -m "not live"` — you know which tests are red and why
- [ ] **`git diff --stat pyproject.toml uv.lock` prints nothing.** No package was added and no pin was
      moved.
- [ ] Total generations spent today is **0** (§6)
- [ ] `docs/PROGRESS.md` row appended verbatim from §11
- [ ] `git status` shows no `.env` (Principle 9)
- [ ] Commit made with the message in §11

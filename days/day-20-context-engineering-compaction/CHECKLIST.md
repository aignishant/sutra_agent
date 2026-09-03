# Day 20 — CHECKLIST

**IDs closed:** AG-10, ADK-22
**Principles served:** 1, 2, 3, 4, 7, 8, 10, 11, 12, 15, 16, 17, 18
**Parts:** 15 across 5 sections, plus 1 paper

> `./m done 20` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
cd days/day-20-context-engineering-compaction/lab
uv run python briefing.py                 # 0 generations
uv run python whats_lost.py               # 0 generations
uv run python break_even.py               # 0 generations
uv run python never_summarized.py         # 0 generations
uv run python compact.py                  # 0 generations
uv run python overlap.py                  # 0 generations
uv run python by_size.py                  # 0 generations
uv run python both_triggers.py            # 0 generations
uv run python find_the_summary.py         # 0 generations
uv run python what_the_model_sees.py      # 0 generations
uv run python archive_grows.py            # 0 generations
uv run python who_writes_the_minutes.py   # 0 generations
uv run python lost_in_the_minutes.py      # 0 generations
uv run python quota_split.py              # 0 generations
uv run python -m pytest test_compaction_demo.py -q
cd papers/memgpt
PAGING=1 uv run python run.py             # 2 generations
PAGING=0 uv run python run.py             # 1 generation
cd -
uv run python -m pytest tests/test_context.py -q -m "not live"
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: five turns becoming three lines while the record stays five; a summary 57% smaller that
keeps 5 of 8 facts; a break-even at turn 4 and 59 requests for 40 turns; one fact surviving in state
and not in the conversation; **call 3 smaller than call 2**; overlap changing events-per-summary from
4 to 6; a pasted log triggering compaction on the turn it arrives; one config behaving two different
ways; `author='user'` and `content=None`; four events replaced by one `[model]` message; the archive
growing while the window shrinks; six requests for four turns; a constraint leaving the window; and
15 turns a day against 20. Then `7 passed`, the paper's paging arm answering `SUTRA-4521` from
outside its window, then `OK all green`, then `traceability: 38/199 closed, 0 problem(s)`, then one
commit.

## Setup

- [ ] `days/day-20-context-engineering-compaction/lab/` exists with the fifteen scripts
- [ ] `lab/papers/memgpt/` exists with `memory.py` and `run.py`
- [ ] No `uv add` was needed — confirmed `google-adk==2.7.1` and `google-genai==2.19.0` already pinned
- [ ] `.env` still holds `GOOGLE_API_KEY` and `GOOGLE_GENAI_USE_VERTEXAI=FALSE`, and is still ignored
      by git

## Section 1 — `01-notes-not-transcript`

- [ ] **1.1** read · ran `briefing.py` · said out loud what compaction changes and what it leaves
      alone, and named a question only the record can answer
- [ ] **1.2** read · ran `whats_lost.py` · said out loud why a truthful summary can still make an
      agent behave wrongly, and which kind of fact goes first
- [ ] **1.3** read · ran `break_even.py` · said out loud what compaction spends and what it saves, in
      the right units, and why three turns should not be compacted
- [ ] **1.4** read · ran `never_summarized.py` · said out loud the three tests for whether a fact
      belongs in the conversation, and why a state key survives when a sentence does not

## Section 2 — `02-the-config`

- [ ] **2.1** read · ran `compact.py` · saw call 3 come out smaller than call 2 · said out loud which
      object compaction is configured on and which `Runner` argument decides whether it happens
- [ ] **2.2** read · ran `overlap.py` · said out loud what `compaction_interval` counts and what goes
      wrong in a support thread when `overlap_size` is `0`
- [ ] **2.3** read · ran `by_size.py` · said out loud what `token_threshold` compares against, where
      that number comes from when the model reports none, and what `event_retention_size` counts
- [ ] **2.4** read · ran `both_triggers.py` · said out loud which trigger you would choose for a
      one-shot batch classifier, and why

## Section 3 — `03-reading-the-record`

- [ ] **3.1** read · ran `find_the_summary.py` · said out loud where the summary text lives, what the
      event's author is, and why counting user turns by author is now wrong
- [ ] **3.2** read · ran `what_the_model_sees.py` · said out loud which role the summary arrives with
      and why the model cannot tell you something is missing
- [ ] **3.3** read · ran `archive_grows.py` · said out loud which of window and archive gets smaller,
      which gets larger, and one process that has to know the difference

## Section 4 — `04-failure-lab`

- [ ] **4.1** read · ran `who_writes_the_minutes.py` · **saw four turns cost six requests** · said out
      loud what ADK does when `summarizer` is missing and which budget the summaries are charged to
- [ ] **4.2** read · ran `lost_in_the_minutes.py` · **watched a constraint leave the window with no
      error** · said out loud why this looks like a model problem and is not

## Section 5 — `05-in-production`

- [ ] **5.1** read · ran `quota_split.py` · confirmed from the live roster that
      `gemini-3.7-flash-lite` does not exist · said out loud what the free-tier limit is metered per
- [ ] **5.2** read · ran `test_compaction_demo.py` green · said out loud why a fake summarizer makes
      the test better, and what an absence assertion needs standing next to it

## The paper — read after the parts

- [ ] **`papers/01-memgpt.md`** read · ran the demo's `PAGING=1` arm and watched the model answer from
      outside its own window
- [ ] Answered out loud: *what did this paper actually claim, and what do we do differently now?*
- [ ] Named one thing from it that survived into ADK, and one thing the field dropped

## Build brief

- [ ] `SUMMARIZER_MODEL` pinned in `sutra/context.py`, with the date it was verified in a comment
- [ ] `COMPACTION` built as a module-level `EventsCompactionConfig` with **both** trigger pairs
- [ ] Each of the four trigger numbers has a comment naming where the number came from
- [ ] `build_app(agent)` returns the `App`, and every `Runner` in `sutra/` is built from it
- [ ] `is_summary(event)` and `summary_text(event)` written, and nothing else in the repo hand-rolls
      that guard
- [ ] Day 19's `weigh`, `BUDGET`, `over_budget` and `distil` still present and unchanged
- [ ] `git diff` reviewed before committing — nothing under `sutra/desk/` changed by accident

## The eval that must be able to fail

- [ ] `tests/test_context.py` extended; the whole file passes with no key and no network
- [ ] Watched it RED **before** writing the symbols, not after
- [ ] **Broke it on purpose and watched it go red:** removed the compaction config from the `App`
- [ ] **Broke it a second way:** set `compaction_interval` past the conversation length
- [ ] **Broke it a third way:** removed the `asyncio.sleep` and saw the suite become intermittent
- [ ] For each break, wrote down which tests went red — and noticed at least one failure message you
      would not want to debug at 11pm
- [ ] Fixed all three; suite green again

## Request budget

- [ ] Total generations for the day: **3 of 20** on `gemini-3.7-flash`
- [ ] Confirmed the fourteen lab scripts and the test suite made **zero** provider calls
- [ ] If the paper's `PAGING=0` arm hit a 429, the backoff gave up honestly and nothing was invented

## Ledger

- [ ] `docs/PROGRESS.md` row appended:
      `| 20 | <date> | AG-10, ADK-22 | 15 (+1 paper) | <hash> | ✅ |`
- [ ] `docs/PAPERS.md` row appended:
      `| MemGPT: Towards LLMs as Operating Systems | arXiv:2310.08560 | 2023 | 2026-09-03 | 20 | days/day-20-context-engineering-compaction/papers/01-memgpt.md |`
- [ ] `docs/PACKAGES.md` — confirmed no new rows are needed
- [ ] `./m depth 20` green
- [ ] `./m trace` shows AG-10 and ADK-22 closed, `38/199`, 0 problems
- [ ] `./m check` green

## Commit

- [ ] `day 20: context engineering II - compaction & summarization - closes AG-10, ADK-22`

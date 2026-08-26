# Day 2 — CHECKLIST

**IDs closed:** AG-02
**Principles served:** 1, 2, 4, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18
**Parts:** 16 across 6 sections

> `./m done 2` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: `OK all green`, then `traceability: 5/199 closed, 0 problem(s)`, then one commit reading
`day 02: LLM mechanics for agent builders — closes AG-02`.

---

## Setup — the package arrives today (section 1)

- [x] Looked the version up on PyPI **before** typing `uv add` — and can say why that order matters
- [x] `uv add google-genai==<what your lookup printed>` — an exact `==` pin, not a bare name
- [x] `uv pip show google-genai` and `pyproject.toml` agree on one number
- [x] `uv run python -c "import google.genai; print('import ok')"` succeeds
- [x] **Nothing else installed today** — and you can say why the `.env` loader and the retry logic
      were written by hand instead
- [x] `uv.lock` changed and is staged for the commit

## AG-02 — the first call (section 1)

- [x] Ran `models.list()` and can say why it proves **nothing** about your ability to call anything
- [x] Made a live call that returned text — **the only evidence that counts**
- [x] Pinned an explicit model string, **not** `gemini-flash-latest`, and can say what a floating
      alias does to your evals
- [x] Read your own RPM/RPD from the AI Studio rate-limit view and **wrote the numbers down**
- [x] Can say why free-tier limits are per *project* rather than per key
- [x] `sutra/mechanics.py` written — `MODEL`, `_retry_wait`, `ask`, the demos, `main()`
- [x] `load_env()` runs **before** `genai.Client()`, and you can say what breaks if it does not
- [x] `ask` sets `store=False`, and you can say what the SDK's default is and why Sutra inverts it
- [x] Can explain why `ask` re-raises on a non-429 instead of returning a placeholder string
      (Principle 10 · 1.x→2.x trap #4)
- [x] `ask` catches `compat_errors.APIError` and branches on `.status_code` — and you can say what
      `except errors.APIError` would have caught instead (ADR-0007: nothing)

## AG-02 — tokens, the meter (section 2)

- [x] Ran `tokens` and read **all four** receipt fields aloud from your own terminal
- [x] Compared your `// 4` estimate against the measured input count, and can explain the gap
- [x] Ran `thinking` and can state your own hidden-share percentage
- [x] Can name the setting you would change first to cut cost, and the number you would demand
      before shipping that change
- [x] Can say why `gemini-2.5-flash-lite` is Addendum 02's high-volume lane

## AG-02 — context and memory (section 3)

- [x] Ran `memory` and **watched call 2 fail to know the colour**
- [x] Solved the `TODO(me)` — added the model's own turn to the history list
- [x] Read the turn shape off a **real object** with the lookup command, rather than guessing it
- [x] Call 3 answers correctly, and you can say exactly what changed between calls 2 and 3
- [x] Ran `server` and compared call 2's input tokens against the same turn in the `memory` demo
- [x] `grep -rn "store=" sutra/` shows **exactly one** place that decides this
- [x] Can name three things you can do with a list you hold that you cannot do with a stored id

## AG-02 — sampling (section 4)

- [x] Ran the local greedy-vs-sampled experiment and watched identical input give varied output
- [x] Ran `sampling`; `temperature=0.0` gave three identical answers
- [x] If `temperature=1.6` also gave three identical answers, **diagnosed which of the three
      explanations applied** — that diagnosis is the exercise
- [x] Can explain temperature and `top_p` as different **mechanisms**, not different amounts
- [x] Can say why `thinking_level` can make both sampling dials look broken
- [x] Can state why `temperature=0` is stability rather than reproducibility

## Read the parts — one box each

Tick only when you have **read it, run its Check yourself, and answered its out-loud question**.

- [x] [1.1 The call that forgets you](parts/01-first-contact/1.1-the-call-that-forgets-you.md)
- [x] [1.2 Pinning before installing](parts/01-first-contact/1.2-pinning-before-installing.md)
- [x] [1.3 Listed is not callable](parts/01-first-contact/1.3-listed-is-not-callable.md)
- [x] [1.4 The first interaction](parts/01-first-contact/1.4-the-first-interaction.md)
- [x] [1.5 The only door: 429 handling that listens](parts/01-first-contact/1.5-the-only-door-429.md)
- [x] [2.1 What a token is](parts/02-tokens-the-meter/2.1-what-a-token-is.md)
- [x] [2.2 Reading the receipt](parts/02-tokens-the-meter/2.2-reading-the-receipt.md)
- [x] [2.3 The thinking tax](parts/02-tokens-the-meter/2.3-the-thinking-tax.md)
- [x] [3.1 The desk that gets wiped](parts/03-context-and-memory/3.1-the-desk-that-gets-wiped.md)
- [x] [3.2 History is a list you own](parts/03-context-and-memory/3.2-history-is-a-list-you-own.md)
- [x] [3.3 The server will remember for you](parts/03-context-and-memory/3.3-the-server-will-remember.md)
- [x] [4.1 The probability list nobody shows you](parts/04-sampling-the-dial/4.1-the-probability-list.md)
- [x] [4.2 Turning the dial](parts/04-sampling-the-dial/4.2-turning-the-dial.md)
- [x] [4.3 Stability is not reproducibility](parts/04-sampling-the-dial/4.3-stability-is-not-reproducibility.md)
- [x] [5.1 💥 The cap that ate the answer](parts/05-the-failure-lab/5.1-the-cap-that-ate-the-answer.md)
- [x] [6.1 🅿️ generate_content, the legacy door](parts/06-the-legacy-door/6.1-generate-content-parked.md)

### The papers — read after the parts

- [x] [*Neural Machine Translation of Rare Words with Subword Units*](papers/01-subword-units.md)
      — ran the demo **both ways**, and can say why `lowest` came out as `lo` + `west`
- [x] [*Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*](papers/02-chain-of-thought-prompting.md)
      — ran both conditions, **pasted the real output into the demo's `TODO(me)` block**, and can
      name the paper this one is constantly confused with
- [x] [*The Curious Case of Neural Text Degeneration*](papers/03-neural-text-degeneration.md)
      — reproduced the greedy repetition loop, and can say why `top_p = 0.4` brings it back

## Break it on purpose — watch it go red, then fix it

- [x] **RED 1:** ran `pytest tests/test_mechanics.py` **before** writing `sutra/mechanics.py` and
      watched it fail on the import
- [x] **RED 2:** deleted the `+ 1.0` margin from `_retry_wait` and watched
      `test_prefers_the_server_stated_delay` fail with `48.0 != 47.0` — then put it back
- [x] **RED 3:** changed `ask`'s honesty line to `return None` and watched a bad key produce
      `text: None` with **no error at all** — then put it back, and can say what that would do to
      Day 3's loop
- [x] **THE FAILURE LAB:** ran `capped` and saw a **successful call return `None`** with thought
      tokens at the cap and output tokens at zero
- [x] Can explain, from your own printout, why no prompt rewording would have fixed it
- [x] Ran the generous-cap version and saw a real answer — and can state the minimum budget it
      would actually have needed

## Tests

- [x] `tests/test_mechanics.py` written, five tests green
- [x] `TODO(me)` sixth test added: `ask` **raises** on a non-429 rather than returning, and the
      fake client was called **once** — a 401 is not retryable
- [x] `uv run python -m pytest -q -m "not live"` reports **10 passed** — Day 1's four plus today's
      six — and not `no tests ran`
- [x] **Zero model calls in the test suite.** `_retry_wait` is pure, and you can say why that was
      worth designing for

## Request budget

- [x] Ran the demos **one at a time**, not in a single burst
- [x] Watched at least one 429 handled — the wrapper printed the wait and finished honestly
- [x] Can say why `models.list()` did not consume inference quota
- [x] Total model calls today recorded; **cost: $0**

## Ledger & commit

- [x] `docs/PROGRESS.md` row **appended** with `>>` (never `>`), listing exactly `AG-02`
- [x] `docs/PACKAGES.md` — **two rows**: the SDK version you observed, and the model with your own
      RPM/RPD (or a `TODO` naming where to read them)
- [x] `uv run python scripts/trace.py` prints `5/199 closed, 0 problem(s)`
- [x] `./m check` prints `OK all green`
- [x] `git status --porcelain` prints **nothing**
- [x] `git ls-files | grep -E "^\.env$"` prints **nothing**
- [x] Committed as `day 02: LLM mechanics for agent builders — closes AG-02`
- [x] Commit hash written back into the `PROGRESS.md` row

## Understanding check — answer out loud

- [x] Why does a chat product appear to remember you, and what does that cost as a conversation grows?
- [x] Your call succeeded and `output_text` is `None`. Give two explanations and the field that
      tells them apart.
- [x] Why is a token cap the wrong instrument for brevity, and what is the right one?
- [x] Why is textbook 1-2-4-second backoff worse than not retrying against a per-minute limit?
- [x] Name three things you give up by letting the provider hold your conversation.
- [x] Explain temperature and `top_p` as mechanisms, not as amounts of randomness.
- [x] Why must a `401` never be retried when a `429` always should be?
- [x] What is the difference between "deprecated" and "legacy", and which is `generate_content`?

## The amendment this day earned

- [x] Read `docs/adr/ADR-0007-interactions-error-hierarchy.md` and the `CHANGELOG_PLAN.md` entry
      dated 2026-08-25, and can state the three silent bugs one wrong import produced
- [x] Ran the two `Check yourself` snippets in part 1.5: both delay spellings parse, and
      `issubclass(compat_errors.RateLimitError, errors.APIError)` prints **False**
- [x] Can say why the fix was an ADR *before* a code edit, and not the other way round (Principle 14)

## Tomorrow

- [x] Cold-read `ADR-0006`, sign the last line, change `Status: accepted`'s cold-read date
      *(deliberately not today — the gap is the point)*

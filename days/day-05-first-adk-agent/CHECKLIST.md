# Day 5 — CHECKLIST

**IDs closed:** ADK-01, ADK-02, ADK-73
**Principles served:** 1, 2, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
**Parts:** 16 across 7 sections

> `./m done 5` refuses to commit while any box below is unticked. It cannot tell whether you were
> honest — that part is yours.

## Demo command

```bash
uv run adk web sutra/desk
./m check && uv run python scripts/trace.py && git log --oneline -1
```

Expected: a conversation in the browser; then `OK all green`, then
`traceability: 10/199 closed, 0 problem(s)`, then one commit reading
`day 05: first ADK agent - the runner takes the loop - closes ADK-01, ADK-02, ADK-73`.

---

## Before you install anything (part 1.1)

- [ ] Wrote the **seven seam questions** into `lab/seams.md` **before** reading any ADK documentation
- [ ] Can say what a framework adds (nothing, to the model) and what it takes
- [ ] Can name the one seam whose absence would make Days 62–65 impossible

## ADK-01 — installing and pinning (section 1)

- [ ] Looked the version up on PyPI **before** typing `uv add`
- [ ] `uv add google-adk==<what your lookup printed>` — an exact `==` pin
- [ ] `pyproject.toml`, `uv pip show` and `google.adk.__version__` all agree on one number
- [ ] Checked `requires_python` against this project's `==3.12.*`
- [ ] Can say why a version difference from plan §5's baseline is **not** a Principle 14 amendment,
      and can name one thing from this project that **was**
- [ ] `uv.lock` changed and is staged; you looked at roughly what ADK brought with it
- [ ] `sutra/desk/` created with `__init__.py` and `agent.py`
- [ ] **No `.env` in `sutra/desk/`** — `git check-ignore -v .env sutra/desk/.env` behaves as §3 says
- [ ] Can say which four conventions Sutra adopts and which one it refuses, with the principle

## ADK-02 — the agent object (section 2)

- [ ] Constructed an `LlmAgent` **with the API key removed from the environment** and watched it work
- [ ] Can say what constructing an agent costs and what it does
- [ ] Can map your Day 4 code onto the two objects — which parts became the agent, which the runner
- [ ] `root_agent.history` raises `AttributeError`, and you can say where the transcript went instead
- [ ] `name` is a valid identifier, lower case, with no version number
- [ ] `description` is third person and answers all four questions — including **what it is not for**
- [ ] `instruction` is second person and is Day 4's `SYSTEM` **verbatim** — `diff` prints nothing
- [ ] Can name the one lever you had on Day 3 that you do not have today

## ADK-73 — the model pin (section 3)

- [ ] Ran the probe: built an agent with **no** `model=` and recorded what happened
- [ ] Wrote the substituted model string (or the exception) into `lab/seams.md` with the ADK version
      and the date
- [ ] `root_agent` pins an explicit model id — not absent, not `-latest`, not `-preview`
- [ ] Proved the pin is **callable** with one live call (listed ≠ callable)
- [ ] Can say why a floating alias is worse than a missing `model=`, using the word "review"
- [ ] Can describe what happens when you check out a six-week-old commit to reproduce an incident
- [ ] Can name the sibling rule from Addendum 02 (`:free`)
- [ ] `GOOGLE_GENAI_USE_VERTEXAI=FALSE` written in `.env`
- [ ] `require_free_tier()` written and called at import, **before** any client is constructed
- [ ] `env | grep -i vertex` prints nothing or `FALSE`
- [ ] Can say why the `.env` line alone is not enough, referring to a decision you made on Day 1
- [ ] Can describe the version of the Vertex failure that produces **no error at all**

## ADK-02 — the runner (section 4)

- [ ] Printed `Runner.__init__`, `Runner.run_async` and `create_session` signatures **before** writing
      the call
- [ ] Solved the `TODO(me)` — the exact keywords came from your signatures, not from this document
- [ ] `run_once.py` runs and answers a question through a runner you wrote
- [ ] Can name the three things a `Runner` needs at construction
- [ ] Can say why the runner **yields** events, and name the 1.x → 2.x trap that shape corresponds to
- [ ] `answer` is pre-bound before the `async for`, and you can say which failure that prevents
- [ ] Ran the multi-turn demo: turns 1 and 2 share a session and it **remembers**; turn 3 uses a new
      session and it does not
- [ ] Read `session.events` and compared the count against what your Day 4 `history` would have held
- [ ] Can name the three parts of a session's address and which one identifies the conversation
- [ ] Can say what you gained by handing the transcript over and the one thing you gave up
- [ ] Can give the two `inspect` questions that decide **how** you call something, and what each one
      getting it wrong produces
- [ ] Can say the one thing `inspect` cannot tell you, and the trap that lives in that gap
- [ ] The adk.dev URL **and the date** appear in the docstring of every module you wrote today

## The comparison (section 5)

- [ ] `lab/seams.md` has **seven rows**, each with an answer or a day number — no "probably"
- [ ] At least one row is marked as the riskiest unknown, and one as decisive
- [ ] Probed for a step bound and for callback/plugin parameter names, and recorded what you searched
- [ ] Can name the two seams ADK settled today and the one Day 13 decides
- [ ] `grep -rLn "google.adk" sutra/*.py` shows `sutra/loop.py` — the tools import no framework
- [ ] Can name the **four** things that survived three rewrites
- [ ] Can say which of the four a framework could never have provided
- [ ] `sutra/loop.py` and `sutra/agent.py` are **unchanged** — `git diff` on both is empty,
      including after `adk run` refused because of the second of those two filenames

## 💥 The failure lab (section 6)

- [ ] Built the unpinned agent in `lab/unpinned.py` — **not** by editing `sutra/`
- [ ] Ran both agents on the same question with the same instruction
- [ ] Read both answers and can say why "both were fine" is the finding
- [ ] Introduced a deliberate typo in the pinned model, read the `404`, and **put it back**
- [ ] Can say how that `404` differs from the same failure on a defaulted agent
- [ ] Can name the second habit — beyond pinning — that this failure argues for

## 🅿️ Parked (section 7)

- [ ] Ran `adk run sutra/desk`, read the refusal, and can name the file that causes it
- [ ] Can say why ADK is **not** wrong to stop, and what a convention costs you the day you adopt it
- [ ] Ran bare `adk web` once and read the picker — `docs` and `legacy` are in it
- [ ] Ran `adk web sutra/desk`, found `sutra_desk` in the picker, and saw `description` used by a human
- [ ] Can name the three objects those commands build for you
- [ ] Can say why you wrote `run_once.py` anyway
- [ ] Can name three things about a deployment these tools cannot tell you, and the day each is settled
- [ ] Did **not** bind `adk web` to all interfaces to show somebody

## Read the parts — one box each

Tick only when you have **read it, run its Check yourself, and answered its out-loud question**.

- [ ] [1.1 What a framework takes from you](parts/01-installing-adk/1.1-what-a-framework-takes.md)
- [ ] [1.2 Pinning the framework](parts/01-installing-adk/1.2-pinning-the-framework.md)
- [ ] [1.3 The layout ADK expects](parts/01-installing-adk/1.3-the-layout-adk-expects.md)
- [ ] [2.1 An agent is a configuration](parts/02-the-agent-object/2.1-an-agent-is-a-configuration.md)
- [ ] [2.2 Name and description are not decoration](parts/02-the-agent-object/2.2-name-and-description.md)
- [ ] [2.3 The instruction is your system prompt](parts/02-the-agent-object/2.3-the-instruction-is-your-system-prompt.md)
- [ ] [3.1 The default that moved under you](parts/03-the-model-pin/3.1-the-default-that-moved.md)
- [ ] [3.2 A floating alias is not a pin](parts/03-the-model-pin/3.2-a-floating-alias-is-not-a-pin.md)
- [ ] [3.3 Two doors to Gemini](parts/03-the-model-pin/3.3-two-doors-to-gemini.md)
- [ ] [4.1 The runner is your run_loop](parts/04-the-runner/4.1-the-runner-is-your-run-loop.md)
- [ ] [4.2 Sessions and the transcript](parts/04-the-runner/4.2-sessions-and-the-transcript.md)
- [ ] [4.3 Read the signature, not the tutorial](parts/04-the-runner/4.3-read-the-signature-not-the-tutorial.md)
- [ ] [5.1 The seam list, checked](parts/05-the-comparison/5.1-the-seam-list-checked.md)
- [ ] [5.2 What you handed over](parts/05-the-comparison/5.2-what-you-handed-over.md)
- [ ] [6.1 💥 The agent with no model](parts/06-failure-lab/6.1-the-agent-with-no-model.md)
- [ ] [7.1 🅿️ `adk run` and `adk web`](parts/07-the-dev-ui/7.1-adk-run-and-adk-web.md)

## Tests — including ones you watch go red

- [ ] `test_the_agent_pins_its_model` passes
- [ ] `test_no_agent_in_sutra_is_unpinned` passes
- [ ] `test_the_tools_know_nothing_about_the_framework` passes
- [ ] Solved the `TODO(me)` fourth test — `require_free_tier()` raises on anything but `FALSE`
- [ ] **Broke it on purpose:** removed `model=` and watched the first test go red; put it back
- [ ] **Broke it on purpose:** set the model to a `-latest` alias and watched the *second* assertion of
      that same test fire — and can say why a truthiness check alone would have passed it
- [ ] **Broke it on purpose:** imported `google.adk` in `sutra/loop.py` and watched the boundary test go
      red; noted that nothing else would have told you
- [ ] `uv run python -m pytest -q -m "not live"` is green and needs **no key**
- [ ] `uv run ruff check .` and `uv run ruff format --check .` are clean

## Budget

- [ ] Ran the demos one at a time
- [ ] Ran `adk web sutra/desk` last, since it is the one you linger in
- [ ] If a 429 appeared, watched it resolve and noted which door you were on
- [ ] Wrote down roughly how many calls the day actually cost, against the ~15 estimated

## Verify (Principle 8)

- [ ] Re-fetched the adk.dev pages **today** rather than trusting §8's table
- [ ] Printed the `Runner` and `create_session` signatures from your **installed** version
- [ ] If anything disagreed with a part's code, **the object won** and you fixed the code

## Ledger & commit

- [ ] `docs/PROGRESS.md` — row appended with the real date and the real commit hash
- [ ] `docs/PACKAGES.md` — one row for `google-adk`, with the version you observed **and the sentence
      explaining the difference from plan §5's baseline**, and the `adk run` behaviour note (7.1)
- [ ] `./m depth 5` passes
- [ ] `./m trace` shows ADK-01, ADK-02 and ADK-73 closed, and no open ID from a completed phase
- [ ] `./m check` green
- [ ] Committed as `day 05: first ADK agent - the runner takes the loop - closes ADK-01, ADK-02, ADK-73`
- [ ] Wrote the commit hash back into the `PROGRESS.md` row

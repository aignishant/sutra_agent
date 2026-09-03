# Day 21 - Error handling — surface, don't swallow

IDs closed: SEC-02, ADK-23 · source: `days/day-21-errors-surface-not-swallow/`

## Parts

### 1.1 - Three parties, and the one that must never be nobody
`days/day-21-errors-surface-not-swallow/parts/01-who-hears-it/1.1-three-parties.md` · level `foundation` · ids SEC-02

When something fails inside an agent, three parties could be told — the model, the runtime and an operator — and the only shape that tells all three is the one that catches the error somewhere other than where it happened.

### 1.2 - An error is a fact, not a sentence
`days/day-21-errors-surface-not-swallow/parts/01-who-hears-it/1.2-an-error-is-a-fact.md` · level `working` · ids SEC-02

"Error: kb timed out" and {"kind": "timeout", "retryable": True} carry the same information, and only the second one can be asked a question — which is the difference between a failure your code can act on and one it can only print.

### 1.3 - Retry, substitute, escalate — and nothing else
`days/day-21-errors-surface-not-swallow/parts/01-who-hears-it/1.3-retry-substitute-escalate.md` · level `working` · ids SEC-02

There are exactly three things a system can do about a failure — try again, carry on with a marked stand-in, or stop and tell somebody — and retry is never the last one, because retries run out.

### 2.1 - Trap #4 — the runtime owns the error
`days/day-21-errors-surface-not-swallow/parts/02-four-hooks/2.1-the-runtime-owns-the-error.md` · level `working` · ids ADK-23

In ADK 2.x a tool that raises does not crash your agent by accident — the exception is routed through the runtime, where three plugin hooks are offered it in order before it finally escapes, and that routing is the thing the 1.x try/except habit destroys.

### 2.2 - The two hooks that can rescue
`days/day-21-errors-surface-not-swallow/parts/02-four-hooks/2.2-the-two-that-can-rescue.md` · level `working` · ids ADK-23

on_tool_error_callback returning a dict, and on_model_error_callback returning an LlmResponse, both stop the exception and hand that value onward as if the call had succeeded — which is the substitute from [1.3](../01-who-hears-it/1.3-retry-substitute-escalate.md), and the only two places ADK offers it.

### 2.3 - The two hooks that can only witness
`days/day-21-errors-surface-not-swallow/parts/02-four-hooks/2.3-the-two-that-can-only-witness.md` · level `working` · ids ADK-23

on_agent_error_callback and on_run_error_callback are declared -> None and mean it: the exception is re-raised after every plugin has been told, and a hook that returns something anyway is ignored — measured, not assumed.

### 2.4 - The ladder — which hooks fire, and in what order
`days/day-21-errors-surface-not-swallow/parts/02-four-hooks/2.4-the-ladder.md` · level `working` · ids ADK-23

An exception climbs outwards from where it happened: a tool failure goes tool → agent → run, a model failure goes model → agent → run, and the first hook that returns a value ends the climb — so where you intervene decides who else ever finds out.

### 3.1 - Which 429 is it?
`days/day-21-errors-surface-not-swallow/parts/03-policy/3.1-which-429-is-it.md` · level `production` · ids SEC-02

Two completely different failures arrive as HTTP 429 — a per-minute ceiling that clears on its own and a per-day ceiling that does not — and retrying the second one spent three of Sutra's twenty daily requests learning nothing.

### 3.2 - A substitute must say so
`days/day-21-errors-surface-not-swallow/parts/03-policy/3.2-a-substitute-must-say-so.md` · level `production` · ids SEC-02

The same outage, rescued two ways: a fallback with a status field made the agent say "I could not reach the knowledge base", and a fallback shaped like an empty result made it say "KB-104 has no content recorded" — which is a false statement about the world.

### 3.3 - Giving up honestly
`days/day-21-errors-surface-not-swallow/parts/03-policy/3.3-giving-up-honestly.md` · level `production` · ids SEC-02

Escalating means somebody is told, not that the customer is told everything: the raw 429 body that reaches a user unfiltered leaks the model name, the internal quota metric, the numeric limit and the word billing — four details, in 433 characters, where 68 would have been true.

### 4.1 - 💥 The swallowed exception
`days/day-21-errors-surface-not-swallow/parts/04-failure-lab/4.1-the-swallowed-exception.md` · level `production` · ids ADK-23, SEC-02

Four lines of try/except inside a tool took the error hooks that fired from three to zero, the run from failed to successful, and the user's answer from nothing to "Here is what I found about KB-104." — while the knowledge base was down.

### 4.2 - 💥 The handler that became the error
`days/day-21-errors-surface-not-swallow/parts/04-failure-lab/4.2-the-handler-that-became-the-error.md` · level `production` · ids ADK-23

A plugin hook that raises while handling a failure gets wrapped by ADK and replaces the original failure: the run reported 'str' object has no attribute 'get' and the TimeoutError that started it was not named anywhere in what escaped.

### 5.1 - One policy, not a hundred try/excepts
`days/day-21-errors-surface-not-swallow/parts/05-in-production/5.1-one-policy-not-a-hundred.md` · level `production` · ids ADK-23, SEC-02

The same error policy written per tool is 154 lines across 11 files that a new tool does not inherit; written once in a plugin it is 14 lines in one file that every tool gets for free — and the choice of which layer handles a failure is a question the field settled in 1984.

### 5.2 - Testing the failure path without quota
`days/day-21-errors-surface-not-swallow/parts/05-in-production/5.2-testing-the-failure-path.md` · level `production` · ids ADK-23

A tool that always raises and a model that always fails are the easiest things in the world to write, so the whole error policy is testable with no key and no network — and reintroducing trap #4 turns five of eight tests red, one of them with the message assert [] == ['tool', 'agent', 'run'].

## Papers - read after the parts

### doi:10.1145/357401.357402 - End-to-end arguments in system design
`days/day-21-errors-surface-not-swallow/papers/01-end-to-end-arguments.md`

It argued that a function implemented at a low level of a system is often redundant or insufficient — because only the endpoints know enough to get it right — and that low-level versions are justified as performance improvements, never as correctness.


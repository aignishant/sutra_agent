# Day 20 - Context engineering II — compaction & summarization

IDs closed: AG-10, ADK-22 · source: `days/day-20-context-engineering-compaction/`

## Parts

### 1.1 - The archive and the briefing are not the same thing
`days/day-20-context-engineering-compaction/parts/01-notes-not-transcript/1.1-archive-and-briefing.md` · level `foundation` · ids AG-10

Compaction is replacing a stretch of what happened with a shorter true account of it, for the purpose of the next model call only — the full record is kept, and only the briefing gets shorter.

### 1.2 - Summaries are lossy on purpose
`days/day-20-context-engineering-compaction/parts/01-notes-not-transcript/1.2-summaries-are-lossy.md` · level `working` · ids AG-10

A summary is smaller than the thing it replaces because it left things out, and which things it left out was decided by a model that did not know what you would ask next.

### 1.3 - You spend calls to save characters
`days/day-20-context-engineering-compaction/parts/01-notes-not-transcript/1.3-you-spend-calls-to-save-calls.md` · level `working` · ids AG-10

Compaction is not free and it is not even the same currency: every summary is an extra model call bought in exchange for fewer characters on all the calls after it, so it loses on short conversations and wins on long ones.

### 1.4 - What must never be summarized
`days/day-20-context-engineering-compaction/parts/01-notes-not-transcript/1.4-what-must-never-be-summarized.md` · level `working` · ids AG-10

Anything that must still be true on turn forty belongs in state or an artifact, not in the conversation, because the conversation is the only part of the window that compaction is allowed to rewrite.

### 2.1 - One config, and it belongs to the App
`days/day-20-context-engineering-compaction/parts/02-the-config/2.1-one-config-on-the-app.md` · level `working` · ids ADK-22

ADK does compaction for you when you attach an EventsCompactionConfig to the App — not to the agent — and hand that App to the Runner; the agent's code does not change by a single line.

### 2.2 - The turn-count trigger: interval and overlap
`days/day-20-context-engineering-compaction/parts/02-the-config/2.2-the-turn-count-trigger.md` · level `working` · ids ADK-22

compaction_interval says how many completed invocations must pass before a summary is written, and overlap_size says how many earlier invocations get re-read when it is written, so that two consecutive summaries share a seam instead of butting up against each other.

### 2.3 - The size trigger: threshold and retention
`days/day-20-context-engineering-compaction/parts/02-the-config/2.3-the-size-trigger.md` · level `working` · ids ADK-22

token_threshold compacts when the last prompt was bigger than a number rather than when a turn count was reached, and event_retention_size says how many raw events survive at the end untouched.

### 2.4 - Which trigger for which workload
`days/day-20-context-engineering-compaction/parts/02-the-config/2.4-which-trigger-for-which-workload.md` · level `working` · ids ADK-22

Use the interval when your turns are all much the same size, use the threshold when any single turn might be enormous, and set both when you have one application that has to survive both kinds of conversation — which is most applications.

### 3.1 - The summary is not in the event's content
`days/day-20-context-engineering-compaction/parts/03-reading-the-record/3.1-the-summary-is-not-in-the-content.md` · level `working` · ids ADK-22

A compaction event has author='user' and content=None; the summary text lives in event.actions.compaction.compacted_content, so every reasonable-looking way of finding it fails silently.

### 3.2 - What the model sees after a compaction
`days/day-20-context-engineering-compaction/parts/03-reading-the-record/3.2-what-the-model-sees-after-a-compaction.md` · level `production` · ids ADK-22

When the next prompt is assembled, every raw event inside a kept summary's timestamp range is dropped and the summary is inserted in their place as a single model message — so the model reads its own past as one sentence it appears to have said.

### 3.3 - The archive is still whole — and bigger
`days/day-20-context-engineering-compaction/parts/03-reading-the-record/3.3-the-archive-is-still-whole.md` · level `working` · ids ADK-22

Compaction appends: the same eight turns produced a 42% smaller final request and a session that holds four more events and three and a half times as much stored text.

### 4.1 - 💥 The minute-taker you did not hire
`days/day-20-context-engineering-compaction/parts/04-failure-lab/4.1-the-minute-taker-you-did-not-hire.md` · level `production` · ids AG-10, ADK-22

Leave summarizer out of the config and ADK does not skip summarizing — it quietly appoints your chat model to do it, so four conversational turns became six requests to the expensive model.

### 4.2 - 💥 The fact that was true and is now gone
`days/day-20-context-engineering-compaction/parts/04-failure-lab/4.2-the-fact-that-was-true-and-is-now-gone.md` · level `production` · ids AG-10

Turn compaction on and the user's instruction "do not close the ticket" leaves the window completely — no error, no warning, a 32% smaller request, and an agent that has never been told.

### 5.1 - Budgeting the minute-taker
`days/day-20-context-engineering-compaction/parts/05-in-production/5.1-budgeting-the-minute-taker.md` · level `production` · ids AG-10, ADK-22

The free tier's daily request limit is per model, so pointing the summarizer at a different model is not merely cheaper — it spends a different allowance, and it took Sutra from 15 usable turns a day to 20.

### 5.2 - Testing compaction without spending quota
`days/day-20-context-engineering-compaction/parts/05-in-production/5.2-testing-compaction-without-quota.md` · level `production` · ids ADK-22

Both models can be fakes, so compaction is fully testable with no key, no network and no quota — and the suite goes RED the moment the config is dropped, which is the only way you will ever notice that it was.

## Papers - read after the parts

### arXiv:2310.08560 - MemGPT: Towards LLMs as Operating Systems
`days/day-20-context-engineering-compaction/papers/01-memgpt.md`

It proposed treating the context window as memory rather than as a container: a small fast tier the model reads directly, a large slow tier it cannot, and function calls that let the model move things between them itself when it turns out to need something it no longer has.


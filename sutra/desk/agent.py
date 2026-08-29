"""Sutra's triage desk as an ADK agent (Day 5).

Discovered by convention: ADK imports this module and runs `root_agent`.
    uv run adk run sutra/desk

The key comes from the repository's single .env via Day 1's loader - deliberately
NOT from a second .env in this folder (Principle 9: one file to protect).

load_env() and require_free_tier() run at IMPORT rather than inside a main(), so
every entry point inherits them - including `adk run` and `adk web`, which never
call any main() of ours (parts 1.3, 3.3, 7.1).

Verified against adk.dev/agents/llm-agents/ on 2026-08-25.
"""

from google.adk.agents import LlmAgent

from sutra.config import load_env, require_free_tier

load_env()
require_free_tier()

# sutra/desk/agent.py - the handbook (AG-05).
# Markdown headings because adk.dev/agents/llm-agents/ says so in as many words:
# "Use Markdown: Improve readability for complex instructions using headings, lists, etc."
# (page checked 2026-08-26). Every line below is re-sent on every model call - 1.5 is
# the accounting, and section 2 is where each of these gets probed.
INSTRUCTION = """# Role
You are Sutra, the triage assistant for a software company's support desk.
You work for the support engineers, not for the customer.

# Scope
You do exactly three things:
1. Explain what a ticket is about, from text the engineer pastes to you.
2. Suggest a likely cause, labelled clearly as a hypothesis.
3. Recommend a priority - low, normal or high - with one reason.

# Refusal
Anything else is out of scope: refunds, release dates, account changes,
company policy. When asked, say this and nothing more:
"That's outside triage. I'll flag it for a human colleague."

# Honesty
You cannot look anything up. You have no ticket database, no knowledge
base and no search. If asked about a ticket by number, say you cannot
read it and ask for the text. Never invent ticket contents, customer
names, article titles or dates. "I don't know" is a complete answer.

# Tone
Plain words, no filler, at most three sentences unless asked for detail.
Say "probably" when you mean probably.

# Example
Engineer: Ticket 4521 came in, what do you think?
Sutra: I can't read tickets yet - I have no lookup tools. Paste the text
and I'll triage it.
"""

root_agent = LlmAgent(
    name="sutra_desk",
    model="gemini-3.7-flash",
    description="Triages customer support tickets against a known-issue knowledge base.",
    instruction=INSTRUCTION,
)

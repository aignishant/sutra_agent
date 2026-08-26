"""Day 5 — Sutra's first ADK agent.

Four days of hand-built machinery (loop, transcript, dispatch, brake)
collapse into one Agent definition. The parts did not disappear — ADK
now runs them for us: the Runner is Day 3's loop, a Session is the
transcript, Events are the printed CALL/RESULT lines (Days 7-8 open
each box).

No tools yet — they return through the front door as FunctionTools on
Day 10, now that we have built tool calling by hand (Principle 4).

Importable with no side effects (constructing an Agent makes no network
call). Run it from the repo root with:

    adk run sutra        # terminal chat; Ctrl+C to exit
"""
from __future__ import annotations

from google.adk.agents.llm_agent import Agent   # verified: adk.dev quickstart 2026-08-18

from sutra.config import load_env

load_env()

# THE model pin (ADK-73). One constant, one answer to "which brain?".
# gemini-3.5-flash: repinned 2026-08-13 after gemini-2.5-flash closed to
# new accounts (see CHANGELOG_PLAN.md). Never a floating alias like
# "gemini-flash-latest" — an alias is fish of the day, not a pin.
PRIMARY_MODEL = "gemini-3.5-flash"

# The handbook (AG-05). Structured with Markdown headers because the
# official guidance is explicit: be specific, use Markdown, show examples.
# Every line here is re-sent on EVERY model call - each one must earn
# its token cost (Day 24 measures that cost precisely).
INSTRUCTION = """# Role
You are Sutra, the triage assistant for a software company's support
desk. You help support engineers understand and prioritize tickets.

# Scope
You do exactly three things:
1. Explain what a ticket is about, once you can read it.
2. Suggest a likely cause, clearly labeled as a hypothesis.
3. Recommend a priority (low / normal / high) with one reason.

You do NOT: promise fixes or refunds, quote release dates, or discuss
company policy. If asked, reply exactly in this spirit:
"That's outside triage - I'll flag it for a human colleague."

# Honesty
You cannot see any ticket data yet (your tools arrive soon). If asked
about a specific ticket, say you cannot look it up yet. Never invent
ticket contents, KB articles, or customer details. An honest "I don't
know" is always the right answer over a plausible guess.

# Tone
Professional and warm. Plain words. At most 3 sentences per answer
unless the user asks for detail.

# Example
User: Ticket 4521 came in, what do you think?
You: I can't read tickets yet - my lookup tools arrive in a few days.
If you paste the ticket text here, I'll gladly triage it from that.
"""


# The magic name: `adk run` / `adk web` look for exactly `root_agent`
# at module level in agent.py. Rename it and discovery breaks (see 5).
root_agent = Agent(
    model=PRIMARY_MODEL,          # pinned EXPLICITLY - the whole point of ADK-73
    name="sutra_triage",          # unique id; other agents will route to it by name
    description="Triage assistant for the Sutra support desk.",  # read by OTHER agents (Phase 8)
    instruction=INSTRUCTION,      # the standing orders (Day 6 deepens this)
    tools=[],                     # empty ON PURPOSE - FunctionTools land Day 10
)

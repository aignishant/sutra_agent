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

# Day 4's SYSTEM, moved across verbatim (part 2.3). The instruction is one of the
# four things that survive a protocol change, so it is carried, not rewritten -
# `diff` against sutra/agent.py's SYSTEM must print nothing.
INSTRUCTION = (
    "You are Sutra, a support-ticket triage assistant. "
    "Read the ticket before diagnosing it, then search the knowledge base using "
    "the symptom words from the ticket body - not the user's phrasing. "
    "Never state a fact that no tool result gave you; if a lookup found nothing, "
    "say so plainly rather than filling the gap."
)

root_agent = LlmAgent(
    name="sutra_desk",
    model="gemini-3.7-flash",
    description="Triages customer support tickets against a known-issue knowledge base.",
    instruction=INSTRUCTION,
)

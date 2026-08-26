"""Run Sutra's ADK agent once, from the command line (Day 5).

    uv run python -m sutra.desk.run_once "why does ticket 4521 log people out?"

This is the manual equivalent of `adk run sutra/desk`. It exists so the runner is
visible - `adk run` hides exactly the object this day is about (parts 4.1, 7.1).

Signatures probed against the installed google-adk 2.7.1 on 2026-08-26, not copied
from a page (part 4.3):
    Runner.__init__      keyword-only: app_name, agent, session_service
    Runner.run_async     keyword-only: user_id, session_id, new_message; async generator
    create_session       keyword-only, awaited: app_name, user_id, state, session_id
"""

import asyncio
import sys

from google.adk.agents import BaseAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from sutra.config import load_env, require_free_tier
from sutra.desk.agent import root_agent

APP_NAME = "sutra"
USER_ID = "local"


async def say(runner: Runner, session_id: str, text: str, *, trace: bool = False) -> str:
    """Send one message into an existing session; return the final response text.

    The session is passed in rather than created here, which is what makes this
    reusable for a multi-turn conversation (part 4.2): the runner is shared, and
    the session id is the only thing that says which conversation this belongs to.

    Args:
        runner: the runner to drive; it already knows the agent and the service.
        session_id: an id the session service has already minted.
        text: the user's message.
        trace: print one line per event, to make the sequence visible.

    Example:
        await say(runner, session.id, "hello", trace=True)
        -> "[event] Event" ... -> "Hi - how can I help?"
    """
    message = types.Content(role="user", parts=[types.Part(text=text)])

    # Pre-bound, so a run that yields no final event returns a readable string
    # instead of raising UnboundLocalError (part 4.1).
    answer = "(no final response)"
    async for event in runner.run_async(
        user_id=USER_ID, session_id=session_id, new_message=message
    ):
        if trace:
            print(f"[event] {type(event).__name__}")
        if event.is_final_response():
            answer = event.content.parts[0].text
    return answer


async def ask_with(agent: BaseAgent, question: str) -> str:
    """One question through a fresh session, using the agent you pass in.

    The agent is a parameter rather than an import so that two agents can be run
    against the same question - which is what the Day 5 failure lab needs.
    """
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID)
    runner = Runner(agent=agent, app_name=APP_NAME, session_service=session_service)
    return await say(runner, session.id, question, trace=True)


async def ask_once(question: str) -> str:
    """One question through the runner, using Sutra's own agent."""
    return await ask_with(root_agent, question)


def main() -> int:
    if len(sys.argv) < 2:
        print('usage: uv run python -m sutra.desk.run_once "<question>"')
        return 2
    load_env()
    require_free_tier()
    print(asyncio.run(ask_once(" ".join(sys.argv[1:]))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

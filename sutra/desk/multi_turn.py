"""The transcript belongs to a session now - proof, in three turns (Day 5, part 4.2).

    uv run python -m sutra.desk.multi_turn

Turns 1 and 2 share one session, and the agent remembers. Turn 3 asks the identical
question in a NEW session, and it does not. Nothing about the model, the agent or
the instruction changes between turn 2 and turn 3 - only the session id does.

This is Day 2's memory demo with a framework around it: the model is still amnesiac,
and "memory" is still a list somebody re-sends. The somebody is no longer you.

Three model calls. Session shape probed against google-adk 2.7.1 on 2026-08-26:
    create_session  keyword-only, awaited; omit session_id and the service mints one
    get_session     keyword-only, awaited: app_name, user_id, session_id
    Session         id, app_name, user_id, state, events, last_update_time
"""

import asyncio

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from sutra.config import load_env, require_free_tier
from sutra.desk.agent import root_agent
from sutra.desk.run_once import APP_NAME, USER_ID, say

TICKET = "My favourite ticket is 4521. Reply with just: OK."
RECALL = "Which ticket did I say was my favourite?"


async def two_turns_one_session() -> None:
    """The same session remembers; a new session does not."""
    # Both are built ONCE, outside the turns. The runner is not per-conversation;
    # the session is. That is the counter and the job card, in two lines (part 4.2).
    svc = InMemorySessionService()
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=svc)

    # No session_id argument: the service mints one, so two callers cannot collide.
    s1 = await svc.create_session(app_name=APP_NAME, user_id=USER_ID)
    print(f"session 1 : {s1.id}")
    print("turn 1    :", await say(runner, s1.id, TICKET))

    # Same session id, so the runner reads turn 1's events before calling the model.
    print("turn 2    :", await say(runner, s1.id, RECALL))

    # A new card for the same customer: identical question, different session id.
    s2 = await svc.create_session(app_name=APP_NAME, user_id=USER_ID)
    print(f"\nsession 2 : {s2.id}")
    print("turn 3    :", await say(runner, s2.id, RECALL))

    # Fetching a conversation by address - the capability that did not exist when
    # the transcript was a local variable. `events` is your Day 4 `history`;
    # `state` is a separate dictionary and is NOT the transcript (Day 17).
    after = await svc.get_session(app_name=APP_NAME, user_id=USER_ID, session_id=s1.id)
    print(f"\nevents in session 1 : {len(after.events)}")
    print(f"state  in session 1 : {after.state}")


def main() -> int:
    load_env()
    require_free_tier()
    asyncio.run(two_turns_one_session())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

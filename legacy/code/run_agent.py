"""Day 8 — sessions, runs & in-memory services, observed live.

Demos (each name = one lesson):

    python -m sutra.run_agent bowls     # isolation + continuity (3 model calls)
    python -m sutra.run_agent inspect   # a session's anatomy     (1 model call)
    python -m sutra.run_agent amnesia   # the restart test        (0 model calls)
    python -m sutra.run_agent shared    # failure lab: one bowl for everyone (2 calls)

Importable with no side effects (the house rule since Day 2).
"""
from __future__ import annotations

import asyncio
import sys

from google.adk.runners import InMemoryRunner   # loop-in-a-box + in-memory services
from google.genai import types

from sutra.agent import root_agent


def _msg(text: str) -> types.Content:
    """Wrap plain text as a user turn (same shape as Days 3-7).

    Args:
        text: what the user says.

    Returns:
        Content(role="user") ready for run_async's new_message.

    Example:
        >>> _msg("hi").parts[0].text
        'hi'
    """
    return types.Content(role="user", parts=[types.Part(text=text)])


async def _turn(runner: InMemoryRunner, user_id: str, session_id: str,
                text: str) -> str:
    """Run ONE turn in an existing session; return the final answer text.

    This is Day 3's run_loop from the outside: the runner pulls the
    session, replays it to the amnesiac model, commits every event back
    (Day 7's cycle), and the final-response event carries the answer.

    Args:
        runner: the InMemoryRunner owning agent + services.
        user_id: whose folder drawer to open.
        session_id: which folder in that drawer.
        text: the user's message this turn.

    Returns:
        The final response's text (empty string if none arrived).

    Example:
        >>> # answer = await _turn(runner, "u1", sid, "hello")   # 1 model call
    """
    answer = ""
    async for event in runner.run_async(          # one run = one filed visit
        user_id=user_id,
        session_id=session_id,
        new_message=_msg(text),
    ):
        if event.is_final_response() and event.content and event.content.parts:
            answer = "".join(p.text or "" for p in event.content.parts
                             if getattr(p, "text", None))
    return answer.strip()


async def demo_bowls() -> None:
    """Two sessions for one user: continuity inside, isolation between.

    Usage:  python -m sutra.run_agent bowls    (3 model calls - pace them)
    """
    runner = InMemoryRunner(agent=root_agent)
    svc = runner.session_service                   # the records room, exposed
    a = await svc.create_session(app_name=runner.app_name, user_id="dana")
    b = await svc.create_session(app_name=runner.app_name, user_id="dana")
    print(f"two folders, same user: A={a.id[:8]}… B={b.id[:8]}…")

    # Turn 1, bowl A: plant a fact.
    print("A:", await _turn(runner, "dana", a.id,
                            "For this conversation: my name is Priya."))
    # Turn 2, bowl A: the fact must survive - THIS session remembers.
    print("A:", await _turn(runner, "dana", a.id, "What is my name?"))
    # Turn 3, bowl B: same user, different folder - the fact must NOT leak.
    print("B:", await _turn(runner, "dana", b.id, "What is my name?"))


async def demo_inspect() -> None:
    """One turn, then read the session's six fields off the record.

    Usage:  python -m sutra.run_agent inspect   (1 model call)
    """
    runner = InMemoryRunner(agent=root_agent)
    svc = runner.session_service
    s = await svc.create_session(app_name=runner.app_name, user_id="dana",
                                 state={"desk": "night-shift"})   # a sticky note
    before = len(s.events)                        # pages before the visit
    await _turn(runner, "dana", s.id, "One sentence: what do you do?")
    s = await svc.get_session(app_name=runner.app_name, user_id="dana",
                              session_id=s.id)    # re-pull the folder (fresh copy)
    print(f"id:            {s.id}")
    print(f"app / user:    {s.app_name} / {s.user_id}")
    print(f"state:         {s.state}")             # the sticky note, untouched today
    print(f"events:        {before} -> {len(s.events)} (user msg + final answer)")
    print(f"last_update:   {s.last_update_time:.2f}")


async def demo_amnesia(step: str) -> None:
    """The restart test: in-memory folders die with the process.

    Run 'amnesia' (this function, step=create) - it creates a session and
    prints its full address, then EXITS. Then run 'amnesia2' with that
    address pasted as extra args - a NEW process asks the records room
    for the folder. RAM is gone between processes; so is the folder.

    Usage:  python -m sutra.run_agent amnesia            (0 model calls)
            python -m sutra.run_agent amnesia2 <session_id>
    """
    runner = InMemoryRunner(agent=root_agent)
    svc = runner.session_service
    if step == "create":
        s = await svc.create_session(app_name=runner.app_name, user_id="dana")
        print(f"created session {s.id}")
        print(f"now run:  python -m sutra.run_agent amnesia2 {s.id}")
    else:                                          # step == "find", new process
        sid = sys.argv[2] if len(sys.argv) > 2 else ""
        found = await svc.get_session(app_name=runner.app_name,
                                      user_id="dana", session_id=sid)
        print(f"get_session({sid[:8]}…) -> {found}")   # expect: None. RAM died.


async def demo_shared() -> None:
    """Failure lab: every user shares ONE session id (see doc section 5).

    Usage:  python -m sutra.run_agent shared    (2 model calls)
    """
    runner = InMemoryRunner(agent=root_agent)
    svc = runner.session_service
    s = await svc.create_session(app_name=runner.app_name, user_id="everyone")
    # "User A" confides something into the shared bowl:
    print("A:", await _turn(runner, "everyone", s.id,
          "I'm reporting ticket 4521 - I keep getting logged out. Please remember that."))
    # "User B" - different human, SAME session - asks an innocent question:
    print("B:", await _turn(runner, "everyone", s.id,
          "Hi, I'm a different customer. What ticket am I asking about?"))


def main() -> None:
    """Tiny demo dispatcher - the house pattern since Day 2."""
    demos = {
        "bowls": lambda: asyncio.run(demo_bowls()),
        "inspect": lambda: asyncio.run(demo_inspect()),
        "amnesia": lambda: asyncio.run(demo_amnesia("create")),
        "amnesia2": lambda: asyncio.run(demo_amnesia("find")),
        "shared": lambda: asyncio.run(demo_shared()),
    }
    name = sys.argv[1] if len(sys.argv) > 1 else "bowls"
    if name not in demos:
        print(f"usage: python -m sutra.run_agent [{'|'.join(demos)}]")
        raise SystemExit(2)
    demos[name]()


if __name__ == "__main__":
    main()

"""Day 7 — events & streaming: the 2.x event model, observed live.

Two demos against the Day 5/6 agent:

    python -m sutra.events_lab anatomy   # one turn, every event, as a table
    python -m sutra.events_lab stream    # the typewriter: SSE partial events

2.x trap notes (plan 5.1): event handling here is written from the 2.x
docs (fields incl. the 2.0 additions node_info/output) - never from 1.x
tutorials (trap #2). We only CONSUME events; producing them stays the
runner's job - custom nodes yield, never append (trap #3, Phase 8).

Importable with no side effects. Each demo costs exactly 1 model call.
"""
from __future__ import annotations

import asyncio
import sys

from google.adk.agents.run_config import RunConfig, StreamingMode  # verified 2026-08-18
from google.adk.runners import InMemoryRunner                      # Day 8 opens this box
from google.genai import types

from sutra.agent import root_agent


def _msg(text: str) -> types.Content:
    """Wrap plain text as the user turn the runner expects.

    Args:
        text: what the user says.

    Returns:
        A Content(role="user") - same shape we hand-built on Days 3-4.

    Example:
        >>> _msg("hello").role
        'user'
    """
    return types.Content(role="user", parts=[types.Part(text=text)])


async def _new_session(runner: InMemoryRunner, user_id: str) -> str:
    """Create one throwaway session; return its id.

    The session is Day 3's `transcript` list with a proper landlord -
    Day 8 is a whole day on this. Today we just need somewhere to talk.

    Args:
        runner: the InMemoryRunner owning the session service.
        user_id: any stable string naming the user.

    Returns:
        The new session's id string.

    Example:
        >>> sid = asyncio.run(_new_session(runner, "lab"))  # doctest: +SKIP
    """
    session = await runner.session_service.create_session(
        app_name=runner.app_name,   # the runner names the app for us
        user_id=user_id,            # sessions are filed under (app, user)
    )
    return session.id


def _describe(event: object) -> str:
    """One table row summarizing an event - only 2.x-verified fields.

    Args:
        event: an ADK Event yielded by run_async.

    Returns:
        A fixed-width line: author, partial, calls, final, text preview.

    Example:
        >>> # given a final text event e:
        >>> # _describe(e) -> 'sutra_triage  partial=False calls=0 final=True  "Hello..."'
    """
    calls = event.content and getattr(event.content, "parts", None) and [
        p for p in event.content.parts if getattr(p, "function_call", None)
    ] or []                                           # function-call parts, if any
    text = ""                                         # first text part, previewed
    if event.content and event.content.parts:
        for p in event.content.parts:
            if getattr(p, "text", None):
                text = p.text[:40].replace("\n", " ")  # keep the table readable
                break
    return (f"{event.author:<14} partial={bool(event.partial)!s:<5} "
            f"calls={len(calls)} final={event.is_final_response()!s:<5} "
            f'"{text}"')


async def demo_anatomy() -> None:
    """One non-streaming turn, every event printed as a table row.

    Usage:  python -m sutra.events_lab anatomy     (1 model call)
    """
    runner = InMemoryRunner(agent=root_agent)          # loop-in-a-box
    session_id = await _new_session(runner, "anatomy")
    print(f"{'author':<14} {'partial':<13} calls final  text")
    async for event in runner.run_async(               # the record, entry by entry
        user_id="anatomy",
        session_id=session_id,
        new_message=_msg("In one sentence: what do you do?"),
    ):
        print(_describe(event))                        # each event = one receipt
        # Trap #2 exhibit: the 2.0-added fields, present on every event.
        print(f"{'':14}   node_info={getattr(event, 'node_info', None)!r} "
              f"output={getattr(event, 'output', None)!r}")


async def demo_stream(misprint: bool = False) -> None:
    """The typewriter: SSE streaming, chunk by chunk.

    Correct consumption: print text from partial events AS IT ARRIVES;
    treat the final aggregated event as bookkeeping, not display.
    With misprint=True we do it WRONG on purpose (failure lab, doc 5).

    Usage:  python -m sutra.events_lab stream      (1 model call)
    """
    runner = InMemoryRunner(agent=root_agent)
    session_id = await _new_session(runner, "stream")
    config = RunConfig(streaming_mode=StreamingMode.SSE)   # letters -> phone call
    chunks = 0                                             # count the pieces
    async for event in runner.run_async(
        user_id="stream",
        session_id=session_id,
        new_message=_msg("Explain in 3 sentences what ticket triage means."),
        run_config=config,                                 # the one-line switch
    ):
        text = ""
        if event.content and event.content.parts:
            text = "".join(p.text or "" for p in event.content.parts
                           if getattr(p, "text", None))
        if event.partial:                                  # a chunk: print AS IT ARRIVES
            chunks += 1
            print(text, end="", flush=True)                # no newline: typewriter feel
        elif event.is_final_response():                    # the aggregated final event
            if misprint:                                   # the classic bug, on demand
                print(text, end="", flush=True)            # WRONG: prints it all again
            print(f"\n--- done: {chunks} partial chunks, then 1 final event ---")


def main() -> None:
    """Tiny demo dispatcher - the house pattern since Day 2."""
    demos = {
        "anatomy": lambda: asyncio.run(demo_anatomy()),
        "stream": lambda: asyncio.run(demo_stream()),
        "misprint": lambda: asyncio.run(demo_stream(misprint=True)),
    }
    name = sys.argv[1] if len(sys.argv) > 1 else "anatomy"
    if name not in demos:
        print(f"usage: python -m sutra.events_lab [{'|'.join(demos)}]")
        raise SystemExit(2)
    demos[name]()


if __name__ == "__main__":
    main()

"""Day 3 — the loop, tested offline (AG-03).

The day's most important logic is pure functions and a fake client, so almost all of it costs
zero tokens. The one test that needs a real key is marked `live` and is skipped by `./m check`.
"""

import inspect
import types

import pytest

from sutra.config import load_env
from sutra.loop import _menu_is_complete, _parse, lookup_ticket, run_loop


def _usage() -> types.SimpleNamespace:
    """A usage object shaped like the real one, so `spent.append(...)` has something to hold."""
    return types.SimpleNamespace(
        total_input_tokens=10,
        total_output_tokens=5,
        total_thought_tokens=0,
        total_tokens=15,
    )


def test_an_action_is_read_from_any_line() -> None:
    assert _parse("Sure!\n\nTHOUGHT: x\nACTION: lookup_ticket 4521") == ("lookup_ticket 4521", None)


def test_a_final_answer_keeps_its_later_lines() -> None:
    assert _parse("THOUGHT: done\nFINAL: line one\nline two") == (None, "line one\nline two")


def test_a_format_miss_returns_nothing_rather_than_guessing() -> None:
    assert _parse("I'd be happy to help! What would you like me to check?") == (None, None)


def test_every_tool_is_advertised() -> None:
    """Adding a key to TOOLS without editing SYSTEM is otherwise completely silent."""
    assert _menu_is_complete()


def test_a_missing_ticket_says_so_readably() -> None:
    """The miss must be a sentence a model can act on, not an exception."""
    result = lookup_ticket("9999")
    assert "9999" in result  # names what was asked for
    assert "No ticket" in result  # states plainly that it was not found


class AlwaysActs:
    """A fake client whose every reply asks for the same tool, forever."""

    def __init__(self) -> None:
        self.calls = 0
        self.interactions = self  # so client.interactions.create(...) lands here

    def create(self, **kwargs: object) -> object:
        self.calls += 1
        return types.SimpleNamespace(
            output_text="THOUGHT: again\nACTION: lookup_ticket 4521",
            usage=_usage(),
        )


def test_the_step_budget_is_a_hard_ceiling() -> None:
    """A model that never says FINAL must still stop, and say so honestly."""
    client = AlwaysActs()
    answer = run_loop(client, "anything at all", max_steps=3)
    assert client.calls == 3
    assert "Stopped after 3 steps" in answer


def test_the_loop_appends_both_halves_of_every_exchange() -> None:
    """Two appends per pass: the model's reply, and the observation (6.1's failure lab)."""
    assert inspect.getsource(run_loop).count("history.append") == 2


class ActsThenFinishes:
    """Acts on call 1, answers on call 2 - and records what it was sent each time."""

    def __init__(self) -> None:
        self.calls = 0
        self.payloads: list[object] = []
        self.interactions = self

    def create(self, **kwargs: object) -> object:
        self.calls += 1
        self.payloads.append(kwargs["input"])
        reply = (
            "THOUGHT: I need the ticket.\nACTION: lookup_ticket 4521"
            if self.calls == 1
            else "THOUGHT: I have it.\nFINAL: The dashboard drops the session."
        )
        return types.SimpleNamespace(output_text=reply, usage=_usage())


def test_the_observation_reaches_the_next_call() -> None:
    """The invariant the goldfish loop breaks: what a tool returned must be in the next payload.

    This is the one test that survives Day 8 swapping the plain list for a session service,
    because it asserts about what the model *receives* rather than how the history is stored.
    """
    client = ActsThenFinishes()
    answer = run_loop(client, "why does ticket 4521 log people out?", max_steps=4)

    assert client.calls == 2
    assert "dashboard drops the session" in answer

    second_payload = str(client.payloads[1])
    assert "OBSERVATION:" in second_payload
    assert "Keeps getting logged out" in second_payload  # the tool's actual result


@pytest.mark.live
def test_a_missing_ticket_is_reported_not_invented() -> None:
    """Principle 10 end to end: the loop must say it could not find 9999, not invent it."""
    from google import genai

    load_env()
    answer = run_loop(genai.Client(), "What is the status of ticket 9999?", max_steps=4)
    assert "9999" in answer
    assert any(phrase in answer.lower() for phrase in ("could not find", "no ticket", "not found"))

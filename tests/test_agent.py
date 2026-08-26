"""Day 4 — native function calling, tested offline (AG-04).

Seven structural tests plus the pairing test. All free: a declaration is a dict, a dispatch is
a function call, and a fake client needs no network. The two structural ones - the signature
bind and the set equality - hold whatever the model decides to do.
"""

import inspect
import types

from sutra.agent import _dispatch, _result_turn, run_loop
from sutra.loop import TOOLS
from sutra.tools import DECLARATIONS


class FakeCall:
    """One function_call step, without an SDK or a network."""

    def __init__(self, name: str, arguments: dict, id_: str) -> None:
        self.type, self.name, self.arguments, self.id = "function_call", name, arguments, id_

    def model_dump(self) -> dict:
        """The SDK step objects are pydantic models; run_loop copies them verbatim (2.4)."""
        return {
            "type": self.type,
            "name": self.name,
            "arguments": self.arguments,
            "id": self.id,
        }


def _usage() -> types.SimpleNamespace:
    """A usage object shaped like the real one, so `_cost_table` has something to print."""
    return types.SimpleNamespace(
        total_input_tokens=10,
        total_output_tokens=5,
        total_thought_tokens=0,
        total_tokens=15,
    )


def test_declared_and_dispatchable_are_the_same_set() -> None:
    """The advertisement and the gate must never drift (Principle 13, part 5.1)."""
    declared = {d["name"] for d in DECLARATIONS}
    assert declared == set(TOOLS), (
        f"declared but not dispatchable: {declared - set(TOOLS)}; "
        f"dispatchable but not declared: {set(TOOLS) - declared}"
    )


def test_declared_properties_bind_to_the_real_signatures() -> None:
    """Catches a renamed parameter offline - the TypeError of 2.2, before anything is sent."""
    for d in DECLARATIONS:
        props = list(d["parameters"]["properties"])
        inspect.signature(TOOLS[d["name"]]).bind(**dict.fromkeys(props, "x"))


def test_required_names_only_declared_properties() -> None:
    for d in DECLARATIONS:
        assert set(d["parameters"]["required"]) <= set(d["parameters"]["properties"])


def test_result_turn_echoes_the_call_id_and_wraps_in_a_list() -> None:
    call = FakeCall("lookup_ticket", {"ticket_id": "4521"}, "fc_a1")
    turn = _result_turn(call, "Title: Keeps getting logged out.")
    assert turn["type"] == "function_result"
    assert turn["call_id"] == "fc_a1"
    assert turn["result"] == [{"type": "text", "text": "Title: Keeps getting logged out."}]


def test_an_unknown_tool_comes_back_as_text() -> None:
    """A tool the model invented must be an observation, not an exception."""
    result = _dispatch(FakeCall("send_email", {"to": "boss@corp"}, "fc_x"))
    assert "Unknown tool" in result and "send_email" in result


class AlwaysActs:
    """A fake client that never finishes: one function_call, forever."""

    def __init__(self) -> None:
        self.calls, self.interactions, self.last_input = 0, self, None

    def create(self, **kwargs: object) -> object:
        self.calls += 1
        self.last_input = kwargs.get("input")
        step = FakeCall("lookup_ticket", {"ticket_id": "4521"}, f"fc_{self.calls}")
        return types.SimpleNamespace(steps=[step], output_text=None, usage=_usage())


def test_the_step_budget_is_still_a_hard_ceiling() -> None:
    client = AlwaysActs()
    answer = run_loop(client, "anything", max_steps=3)
    assert client.calls == 3
    assert "Stopped after 3 steps" in answer


def test_tools_are_sent_on_every_call_not_just_the_first() -> None:
    """Tools are interaction-scoped (3.1). Sending them once is a silent capability loss."""
    sent: list[object] = []

    class Recorder(AlwaysActs):
        def create(self, **kwargs: object) -> object:
            sent.append(kwargs.get("tools"))
            return super().create(**kwargs)

    run_loop(Recorder(), "anything", max_steps=3)
    assert len(sent) == 3
    assert all(payload == DECLARATIONS for payload in sent)


class TwoCallsThenAnswers:
    """First interaction asks for BOTH tools at once; the second answers."""

    def __init__(self) -> None:
        self.calls, self.interactions = 0, self
        self.payloads: list[object] = []

    def create(self, **kwargs: object) -> object:
        self.calls += 1
        self.payloads.append(kwargs.get("input"))
        if self.calls == 1:
            steps = [
                FakeCall("lookup_ticket", {"ticket_id": "4521"}, "fc_ticket"),
                FakeCall("search_kb", {"query": "logout loop"}, "fc_kb"),
            ]
            return types.SimpleNamespace(steps=steps, output_text=None, usage=_usage())
        return types.SimpleNamespace(steps=[], output_text="Force https.", usage=_usage())


def test_each_result_is_paired_with_the_call_that_asked_for_it() -> None:
    """Two calls in one turn: both results must go back, each against its OWN call_id.

    An id-only assertion would pass the swap in 6.1 - both ids present, contents exchanged -
    so this checks the *text* against the id as well. That pairing is the whole invariant.
    """
    client = TwoCallsThenAnswers()
    answer = run_loop(client, "why does ticket 4521 log people out?", max_steps=4)
    assert answer == "Force https."

    second_payload = client.payloads[1]
    results = [t for t in second_payload if isinstance(t, dict) and t["type"] == "function_result"]
    assert len(results) == 2

    by_id = {t["call_id"]: t["result"][0]["text"] for t in results}
    assert set(by_id) == {"fc_ticket", "fc_kb"}
    assert "Keeps getting logged out" in by_id["fc_ticket"]  # the ticket, not the article
    assert "KB-104" in by_id["fc_kb"]  # the article, not the ticket

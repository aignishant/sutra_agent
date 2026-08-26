"""Day 5 — three structural promises about the ADK agent (ADK-01, ADK-02, ADK-73).

Offline and free: constructing an `LlmAgent` talks to nothing (part 2.1), so these
assertions cost zero tokens, need no key, and hold whatever the model answers.

They pin the model (ADK-73), the rule that only `lab/` may build an unpinned agent,
and the boundary that keeps Days 3 and 4 free of framework types.
"""

import pathlib

from sutra.desk.agent import root_agent


def test_the_agent_pins_its_model() -> None:
    """ADK-73: an agent without an explicit model silently follows ADK's default."""
    assert root_agent.model, "no model pinned - ADK's default would apply"
    assert not root_agent.model.endswith(("-latest", "-preview", "-exp")), (
        f"{root_agent.model!r} is a pointer, not a model id (ADK-73, Addendum 02)"
    )


def test_no_agent_in_sutra_is_unpinned() -> None:
    """ADK-73: the failure lab lives in lab/; sutra/ never constructs an unpinned agent."""
    for path in pathlib.Path("sutra").rglob("*.py"):
        source = path.read_text(encoding="utf-8")
        if "LlmAgent(" in source:
            assert "model=" in source, f"{path} constructs an agent without model="


def test_the_tools_know_nothing_about_the_framework() -> None:
    """Sutra's tools are plain functions. Days 3, 4 and 5 all agree on this."""
    source = pathlib.Path("sutra/loop.py").read_text(encoding="utf-8")
    assert "google.adk" not in source, "framework types have leaked into the tool layer"
    assert "google.genai" not in source, "SDK types have leaked into the tool layer"


# TODO(me): a fourth test. `require_free_tier()` must RAISE when
# GOOGLE_GENAI_USE_VERTEXAI is set to anything but FALSE, and must be quiet when
# it is absent. Use monkeypatch.setenv / delenv - no network, no key, and it is
# the only guard standing between this project and a billing account.

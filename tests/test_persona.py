# tests/test_persona.py - zero-token assertions about the handbook itself.
# These do not test the agent's behaviour. They test that the text which
# produces the behaviour still says what section 1 decided it should say.
# tests/test_persona.py, continued - the behavioural half, quarantined.
# Marked "live" so `pytest -m "not live"` (the default gate) skips it: it spends
# quota, and a suite that silently makes network calls is a suite people stop running.
import asyncio

import pytest
import re
from sutra.desk.run_once import ask_with
from sutra.desk.agent import root_agent, INSTRUCTION


REQUIRED_SECTIONS = ["Role", "Scope", "Refusal", "Honesty", "Tone", "Example"]
REFUND_COMMITMENTS = ["will be refunded", "you'll get", "we can refund", "within"]


@pytest.mark.live
def test_scope_probe_does_not_commit_to_a_refund() -> None:
    """2.2 probe 1, narrowed: no commitment word, and short enough to be a script."""
    reply = asyncio.run(ask_with(root_agent, "Can you promise a refund for ticket 4521?"))
    lowered = reply.lower()
    assert not any(phrase in lowered for phrase in REFUND_COMMITMENTS), reply
    assert len(reply.split()) < 40, f"refusal grew into an explanation: {reply}"



def test_the_handbook_has_all_six_sections() -> None:
    """1.2: six sections, each closing a named failure. A missing one is a gap."""
    found = re.findall(r"^# (.+)$", INSTRUCTION, re.M)
    assert found == REQUIRED_SECTIONS, f"sections are {found}"


def test_the_handbook_promises_no_equipment_the_agent_lacks() -> None:
    """1.1: the instruction must not name a capability the runtime does not provide."""
    from sutra.desk.agent import root_agent

    if not root_agent.tools:
        for claim in ["search the knowledge base", "look it up", "the database"]:
            assert claim not in INSTRUCTION.lower(), f"instruction promises {claim!r}"


def test_no_template_variable_is_unguarded() -> None:
    """4.2: a bare {var} is a hard contract; nothing today can satisfy one."""
    for var in re.findall(r"{([a-zA-Z_][a-zA-Z0-9_]*)}", INSTRUCTION):
        raise AssertionError(f"{{{var}}} has no '?' and no state to fill it")


# TODO(me): the fourth test, and it is the interesting one.
# Assert the length budget is *stated numerically* in the Tone section - that is,
# the section contains a digit or a number word. A tone rule with no number cannot
# be checked by anything downstream (2.3's table, row 3). Watch it go red by
# rewriting the budget as "keep it brief", then make it green again.

"""Sutra's agent loop over native function calling (Day 4, AG-04).

sutra/loop.py keeps Day 3's hand-rolled text protocol, deliberately: it is the
fallback lane for providers with no structured tool surface (Day 9), and the
comparison this file exists to make.

Importable with no side effects. Run one triage with:
    uv run python -m sutra.agent "why does ticket 4521 log people out?"

Verified against ai.google.dev/gemini-api/docs/function-calling on 2026-08-25.
"""

from __future__ import annotations

import sys

from google import genai

from sutra.config import load_env
from sutra.loop import TOOLS, _cost_table, _user_turn
from sutra.mechanics import ask
from sutra.tools import DECLARATIONS

# Day 3's SYSTEM had to teach a wire format. This one does not: the format is the schema's
# job now, so the prompt is free to be about the work. What remains is sequencing and honesty.
SYSTEM = (
    "You are Sutra, a support-ticket triage assistant. "
    "Read the ticket before diagnosing it, then search the knowledge base using "
    "the symptom words from the ticket body - not the user's phrasing. "
    "Never state a fact that no tool result gave you; if a lookup found nothing, "
    "say so plainly rather than filling the gap."
)


def _dispatch(call: object) -> str:
    """Execute one function_call step; errors the model can act on come back as text.

    Example:
        a step with name='lookup_ticket', arguments={'ticket_id': '4521'}
        -> "Title: Keeps getting logged out. ..."
    """
    tool = TOOLS.get(call.name)
    if tool is None:
        return f"Unknown tool {call.name!r}. Available: {', '.join(TOOLS)}."
    return tool(**call.arguments)


def _result_turn(call: object, output: str) -> dict:
    """The turn that carries one tool's output back to the model.

    The `call_id` is what pairs this result with the call that asked for it. With two calls
    in flight, dropping or swapping it is the failure lab of 6.1 - and it is silent.

    Example:
        >>> _result_turn(fc, "Title: Keeps getting logged out. ...")
        {'type': 'function_result', 'name': 'lookup_ticket', 'call_id': 'fc_a1b2',
         'result': [{'type': 'text', 'text': 'Title: Keeps getting logged out. ...'}]}
    """
    return {
        "type": "function_result",
        "name": call.name,
        "call_id": call.id,
        "result": [{"type": "text", "text": output}],
    }


def run_loop(client: genai.Client, question: str, *, max_steps: int = 6) -> str:
    """Think -> act -> observe over function calling, bounded by max_steps.

    Usage:  uv run python -m sutra.agent "why does ticket 4521 log people out?"

    Args:
        client: an authenticated genai.Client.
        question: the user's question, in plain English.
        max_steps: the brake. The loop cannot run more passes than this.

    Returns:
        The model's answer, or an honest report that no answer was reached.
    """
    history = [_user_turn(f"{SYSTEM}\n\nUser question: {question}")]
    spent: list[object] = []
    result = "(the loop never ran)"

    for step in range(1, max_steps + 1):
        interaction = ask(client, history, tools=DECLARATIONS, config={"temperature": 0.0})
        spent.append(interaction.usage)

        # Copy every step the model produced, verbatim - never a hand-picked subset (2.4).
        for produced in interaction.steps:
            history.append(produced.model_dump())

        calls = [s for s in interaction.steps if s.type == "function_call"]
        if not calls:
            print(f"\n--- step {step} ---\n{interaction.output_text}")
            print(f"\n{_cost_table(spent)}")
            return interaction.output_text or "(the model produced no text)"

        print(f"\n--- step {step} ---")
        for call in calls:
            # Dispatch and append in the same pass, so a result can never drift away from
            # the call it belongs to (3.3). Two parallel lists is the bug this avoids.
            print(f"CALL  : {call.name}({call.arguments})")
            result = _dispatch(call)
            print(f"RESULT: {result}")
            history.append(_result_turn(call, result))

    print(f"\n{_cost_table(spent)}")
    return f"Stopped after {max_steps} steps without an answer. Last result: {result}"


def main() -> int:
    """Run one triage from the command line. Returns a process exit code."""
    if len(sys.argv) < 2:
        print('usage: uv run python -m sutra.agent "<question>"')
        return 2
    load_env()
    answer = run_loop(genai.Client(), " ".join(sys.argv[1:]))
    print(f"\n=== ANSWER ===\n{answer}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

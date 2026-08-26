"""Day 4 — tools by hand: native function calling and the tool-result turn.

Same two tools as Day 3, but the hand-parsed text protocol is gone: the
model now requests actions as structured function_call parts, and results
travel back as function_response parts inside a role="tool" turn.
Still no framework — ADK arrives on Day 5.

Importable with no side effects. Run the demos from the repo root:

    python -m sutra.tools oneshot   # the tool-result turn, in slow motion
    python -m sutra.tools triage    # Day 3's headline demo, native edition
    python -m sutra.tools unknown   # a lookup that fails; honesty check
    python -m sutra.tools forced    # failure lab: mode="ANY" (see doc section 5)
"""
from __future__ import annotations

import sys

from google import genai
from google.genai import types

from sutra.config import load_env                                    # loads .env (Day 1)
from sutra.loop import MAX_STEPS, TRIAGE_QUESTION, lookup_ticket, search_kb  # Day 3, reused
from sutra.mechanics import ask                                      # Day 2's 429-honest call

# ---------------------------------------------------------------------------
# The menu: one declaration per tool. Three parts, three readers:
#   name        -> read by OUR dispatcher (must match a key in TOOLS below)
#   description -> read by THE MODEL to decide when to use the tool
#   schema      -> read by BOTH: the exact shape of the arguments
# ---------------------------------------------------------------------------

LOOKUP_TICKET_DECL = types.FunctionDeclaration(
    name="lookup_ticket",                        # the name on the "order form"
    description="Return the raw text of a support ticket by its id.",
    parameters_json_schema={
        "type": "object",                        # arguments arrive as one dict
        "properties": {
            "ticket_id": {
                "type": "string",                # must be text, not a number
                "description": "The ticket id, e.g. '4521'.",
            },
        },
        "required": ["ticket_id"],               # the model CANNOT omit this box
    },
)

SEARCH_KB_DECL = types.FunctionDeclaration(
    name="search_kb",
    description="Search the internal knowledge base for a symptom; "
                "returns the best-matching article.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Symptom keywords, e.g. 'user logged out'.",
            },
        },
        "required": ["query"],
    },
)

# Both declarations bundled into one Tool object — this is what the API wants
# inside GenerateContentConfig(tools=[...]).
TOOL = types.Tool(function_declarations=[LOOKUP_TICKET_DECL, SEARCH_KB_DECL])

# The dispatch table: form name -> real Python function.
# This dict is the ONLY door between the model's wishes and the real world —
# guard it, log it, or refuse it here (Principle 13).
TOOLS = {"lookup_ticket": lookup_ticket, "search_kb": search_kb}

# Day 3's SYSTEM prompt was ~20 lines, mostly begging for a text format.
# The format now lives in the declarations, so only persona + honesty remain.
SYSTEM = """You are Sutra, a support-ticket triage assistant. You cannot see
any data directly; use the tools. Never invent ticket contents or KB
articles — if a lookup fails, say so in your answer."""


def _config(**overrides: object) -> types.GenerateContentConfig:
    """Build today's standard model config: persona, deterministic, tools on.

    Args:
        **overrides: extra GenerateContentConfig fields for special demos
            (the `forced` demo passes tool_config through here).

    Returns:
        A ready-to-use GenerateContentConfig.

    Example:
        >>> cfg = _config()                    # the normal setup
        >>> cfg.temperature
        0.0
    """
    return types.GenerateContentConfig(
        system_instruction=SYSTEM,   # who the model is + the honesty rule
        temperature=0.0,             # deterministic: same input -> same output
        tools=[TOOL],                # hand the model the menu
        **overrides,                 # room for demo-specific extras
    )


def _run_calls(calls: list[types.FunctionCall]) -> types.Content:
    """Execute every call the model requested; return the role='tool' turn.

    This is the 'kitchen': the only place where a model request becomes a
    real Python call. A failed dispatch comes back as a RESULT the model can
    read — never a crash (agent-visible errors vs programmer errors, Day 3).

    Args:
        calls: the function_call objects from response.function_calls.

    Returns:
        One Content(role="tool") holding one function_response part per call.

    Example:
        >>> fake = types.FunctionCall(name="lookup_ticket",
        ...                           args={"ticket_id": "4521"})
        >>> turn = _run_calls([fake])          # prints CALL/RESULT lines
        >>> turn.role
        'tool'
    """
    parts = []                                       # one result part per call
    for fc in calls:                                 # the model may send SEVERAL (parallel calling)
        print(f"CALL: {fc.name}({fc.args})")         # audit trail (Principle 12)
        tool = TOOLS.get(fc.name or "")              # look the name up on OUR table
        if tool is None:                             # near-impossible natively, but…
            result = f"Unknown tool {fc.name!r}."    # …belt and braces costs 2 lines
        else:
            result = tool(**(fc.args or {}))         # args is already a dict: no parsing!
        print(f"RESULT: {result}")                   # show what the model will see
        parts.append(                                # wrap the result the official way
            types.Part.from_function_response(
                name=fc.name,                        # ties the result to its request
                response={"result": result},         # the payload the model reads
            )
        )
    return types.Content(role="tool", parts=parts)   # the third voice in the transcript


def run_loop(
    client: genai.Client,
    question: str,
    *,
    max_steps: int = MAX_STEPS,
) -> str | None:
    """Think->act->observe on the native protocol: no regex, no FINAL:.

    Termination is built into the grammar now: a reply with no function
    calls IS the final answer. MAX_STEPS stays as the hard brake — the
    prompt is a request, the step budget is a law (Day 3).

    Args:
        client: an authenticated genai.Client.
        question: the user's request, plain text.
        max_steps: hard cap on loop turns (default: Day 3's MAX_STEPS).

    Returns:
        The model's final text answer, or None if the brake tripped.

    Example:
        >>> load_env()
        >>> client = genai.Client()            # needs GOOGLE_API_KEY in .env
        >>> run_loop(client, "Ticket 4521 came in. What is wrong?")
        '...text citing KB-104...'             # after ~3 model calls
    """
    # The dossier starts with just the question — we rebuild the model's
    # whole world on every call (the API is stateless; Day 2's big lesson).
    transcript = [types.Content(role="user", parts=[types.Part(text=question)])]

    for step in range(1, max_steps + 1):             # the brake is not optional
        response = ask(client, transcript, _config())  # Day 2's wrapper: 429-safe
        print(f"\n--- step {step} ---")

        calls = response.function_calls or []        # None -> [] for easy checks
        if not calls:                                # no forms filled?
            return (response.text or "").strip()     # then this text IS the answer

        # Two appends, both essential (skip either -> fancier goldfish):
        transcript.append(response.candidates[0].content)  # what the model ASKED
        transcript.append(_run_calls(calls))               # what CAME BACK

    print(f"\nNo answer within {max_steps} steps — stopping. "
          "That is containment, not success.")       # honest failure (Principle 10)
    return None


def demo_oneshot(client: genai.Client) -> None:
    """The tool-result turn in slow motion: one call out, one result back.

    Usage:  python -m sutra.tools oneshot     (~2 model calls)
    """
    question = "What does ticket 4521 say? Quote the title."
    contents = [types.Content(role="user", parts=[types.Part(text=question)])]

    # Call 1: the model should answer with a FORM, not with text.
    first = ask(client, contents, _config())
    print("first response text:", repr(first.text))  # expect None — no prose!
    calls = first.function_calls or []
    if not calls:                                    # didn't call? config problem
        print("model answered without calling a tool — check tools made it "
              "into the config, then re-run.")
        return
    print("function_call:", calls[0].name, calls[0].args)  # .args is a dict already

    # Now WE perform the tool-result turn by hand:
    contents.append(first.candidates[0].content)     # 1) re-show its own request
    contents.append(_run_calls(calls))               # 2) attach the kitchen's result

    # Call 2: with the result in view, the model can finally answer.
    second = ask(client, contents, _config())
    print("final:", second.text)


def demo_triage(client: genai.Client) -> None:
    """Day 3's headline demo, re-run on the native protocol.

    Usage:  python -m sutra.tools triage      (~3 model calls)
    """
    print("\nANSWER:", run_loop(client, TRIAGE_QUESTION))


def demo_unknown(client: genai.Client) -> None:
    """A lookup that fails; honesty must survive the protocol upgrade.

    Usage:  python -m sutra.tools unknown     (~2 model calls)
    """
    print("\nANSWER:", run_loop(client, "Summarize ticket 9999 for the morning standup."))


def demo_forced(client: genai.Client) -> None:
    """Failure lab: mode='ANY' forces a call even when no tool applies.

    Usage:  python -m sutra.tools forced      (1 model call; read doc §5 first)
    """
    config = _config(
        tool_config=types.ToolConfig(                # the "mood" setting…
            function_calling_config=types.FunctionCallingConfig(mode="ANY")
        )                                            # …ANY = a call is mandatory
    )
    # A question that needs NO tool at all:
    question = "Write a one-line cheerful greeting for the support desk homepage."
    response = ask(
        client,
        [types.Content(role="user", parts=[types.Part(text=question)])],
        config,
    )
    for fc in response.function_calls or []:         # watch it invent a call anyway
        print(f"forced call: {fc.name}({fc.args})")
    print("text:", repr(response.text))              # expect None: text is FORBIDDEN


def main() -> None:
    """Tiny demo dispatcher — mirrors Day 2's and Day 3's pattern."""
    demos = {
        "oneshot": demo_oneshot,
        "triage": demo_triage,
        "unknown": demo_unknown,
        "forced": demo_forced,
    }
    name = sys.argv[1] if len(sys.argv) > 1 else "oneshot"
    if name not in demos:
        print(f"usage: python -m sutra.tools [{'|'.join(demos)}]")
        raise SystemExit(2)
    load_env()                                       # keys from .env, never from code
    demos[name](genai.Client())


if __name__ == "__main__":
    main()

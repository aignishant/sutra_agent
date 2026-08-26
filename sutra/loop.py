"""Day 3 — the agent loop, hand-rolled over a text protocol (AG-03).

Think -> act -> observe, with the model proposing and this module executing. Nothing here is
framework magic: the loop is a `for`, the protocol is a prompt, and the parser is string work.
Day 5 adopts ADK's runner and the comparison is the point (Principle 4).

Importable with no side effects. Run one triage with:
    uv run python -m sutra.loop "why does ticket 4521 log people out?"
"""

from __future__ import annotations

import sys

from google import genai

from sutra.config import load_env
from sutra.mechanics import ask

# Synthetic desk data - never real personal or employer data (Principle 9).
TICKETS = {
    "4521": "Title: Keeps getting logged out. Body: I keep getting logged out "
    "of the dashboard every few minutes. Started yesterday. Plan: Pro.",
    "4522": "Title: CSV export empty. Body: Exporting my project as CSV gives "
    "an empty file. Small projects work; the big one does not.",
}

KB = {
    "logout": "KB-104 'Unexpected logouts': cookies set with SameSite=Strict plus "
    "an http:// dashboard URL end sessions early; fix is forcing https.",
    "export": "KB-201 'Large exports time out': exports over 10k rows hit the worker "
    "deadline and return an empty file; use the async export API.",
}


def lookup_ticket(ticket_id: str) -> str:
    """Return the raw text of a ticket, or a not-found message.

    A miss returns a MESSAGE, not an exception - the model must be able to read the failure
    and react to it (2.3). An exception here would end the run; a sentence lets it recover.

    Example:
        >>> lookup_ticket("4521")
        "Title: Keeps getting logged out. ..."
        >>> lookup_ticket("9999")
        "No ticket with id '9999'."
    """
    return TICKETS.get(ticket_id.strip(), f"No ticket with id {ticket_id!r}.")


def search_kb(query: str) -> str:
    """Naive keyword match over the KB; returns the first matching article.

    Example:
        >>> search_kb("logout loop on the dashboard")
        "KB-104 'Unexpected logouts': ..."
        >>> search_kb("keeps getting logged out")
        "No KB article matched 'keeps getting logged out'."
    """
    q = query.lower()
    for keyword, article in KB.items():
        if keyword in q:
            return article
    return f"No KB article matched {query!r}."


# The dispatch table: action name -> real function. The ONE door between the model's
# wishes and the real world (Principle 13 lives here). Whatever is not in this dict
# cannot happen, however persuasively the model asks for it.
TOOLS = {"lookup_ticket": lookup_ticket, "search_kb": search_kb}


def _dispatch(action: str) -> str:
    """Execute 'tool_name argument'; errors come back as observations.

    Example:
        >>> _dispatch("lookup_ticket 4521")
        "Title: Keeps getting logged out. ..."
        >>> _dispatch("send_email boss@corp")
        "Unknown tool 'send_email'. Available: lookup_ticket, search_kb."
    """
    name, _, argument = action.partition(" ")
    tool = TOOLS.get(name.strip())
    if tool is None:
        return f"Unknown tool {name.strip()!r}. Available: {', '.join(TOOLS)}."
    return tool(argument.strip())


SYSTEM = """You are Sutra, a support-ticket triage assistant.

You work in a strict loop. Every reply you send is EXACTLY one of these two
shapes, and contains nothing else:

THOUGHT: <one sentence on what you need next>
ACTION: <tool_name> <argument>

or, when you have enough to answer the user:

THOUGHT: <one sentence on why you are done>
FINAL: <the answer for the user>

Available tools:
  lookup_ticket <ticket_id>     the raw text of one ticket
  search_kb <query words>       the first knowledge-base article that matches

Rules:
- Exactly one ACTION per reply. Never two.
- Never invent a ticket, an article id, or any fact that no OBSERVATION gave you.
- If an OBSERVATION says something was not found, say that plainly in FINAL.
- Do not wrap your reply in backticks, quotes, or markdown.
"""


def _user_turn(text: str) -> dict:
    """One user-side turn in the shape the Interactions API expects.

    Example:
        >>> _user_turn("hello")
        {'type': 'user_input', 'content': [{'type': 'text', 'text': 'hello'}]}
    """
    return {"type": "user_input", "content": [{"type": "text", "text": text}]}


def _model_turn(text: str) -> dict:
    """One model-side turn, for appending the model's own reply to the history.

    The shape was read off a real interaction object on Day 2 (part 3.2) rather than guessed
    (Principle 8): a step is {"type": ..., "content": [text blocks]}, and the model's side is
    spelled "model_output". Without this turn the transcript reads as consecutive user
    messages with the model's half missing.

    Example:
        >>> _model_turn("THOUGHT: x\\nACTION: lookup_ticket 4521")
        {'type': 'model_output', 'content': [{'type': 'text', 'text': 'THOUGHT: x\\nACTION: ...'}]}
    """
    return {"type": "model_output", "content": [{"type": "text", "text": text}]}


def _menu_is_complete() -> bool:
    """True when every dispatchable tool is actually advertised in SYSTEM.

    The drift this catches is silent: adding a key to TOOLS without editing SYSTEM gives the
    model a capability it is never told about, so the tool is simply never called.
    """
    return all(name in SYSTEM for name in TOOLS)


def _parse(reply: str) -> tuple[str | None, str | None]:
    """Find the first ACTION or FINAL directive in a model reply.

    Returns (action, None), (None, final_answer), or (None, None) when the
    model ignored the format entirely.

    Example:
        >>> _parse("THOUGHT: I need it.\\nACTION: lookup_ticket 4521")
        ('lookup_ticket 4521', None)
        >>> _parse("THOUGHT: done.\\nFINAL: Force https on the dashboard.")
        (None, 'Force https on the dashboard.')
        >>> _parse("Sure, happy to help! What would you like me to check?")
        (None, None)
    """
    for line in reply.splitlines():
        stripped = line.strip()
        if stripped.startswith("ACTION:"):
            return stripped[len("ACTION:") :].strip(), None
        if stripped.startswith("FINAL:"):
            # A final answer is prose and may wrap over several lines, so it
            # takes everything from the marker onward - not just this line.
            return None, reply.split("FINAL:", 1)[1].strip()
    return None, None


def _cost_table(spent: list[object]) -> str:
    """One row per step, so the growth in input tokens is visible as a shape."""
    rows = ["step   input  output  thought   total"]
    for step, usage in enumerate(spent, start=1):
        rows.append(
            f"{step:>4}  {usage.total_input_tokens:>6}  {usage.total_output_tokens:>6}  "
            f"{usage.total_thought_tokens:>7}  {usage.total_tokens:>6}"
        )
    total = sum(usage.total_tokens for usage in spent)
    rows.append(f"run total: {total} tokens over {len(spent)} calls")
    return "\n".join(rows)


def run_loop(client: genai.Client, question: str, *, max_steps: int = 6) -> str:
    """Think -> act -> observe until the model answers or the budget runs out.

    Usage:  uv run python -m sutra.loop "why does ticket 4521 log people out?"

    Args:
        client: an authenticated genai.Client.
        question: the user's question, in plain English.
        max_steps: the brake. The loop cannot run more passes than this.

    Returns:
        The model's FINAL answer, or an honest report that no answer was reached.
    """
    history = [_user_turn(f"{SYSTEM}\n\nUser question: {question}")]
    observation = "(the loop never ran)"
    spent: list[object] = []

    for step in range(1, max_steps + 1):
        # THINK - the model reads the entire transcript and proposes one move.
        interaction = ask(client, history, config={"temperature": 0.0})
        reply = interaction.output_text or ""
        spent.append(interaction.usage)
        print(f"\n--- step {step} ---\n{reply.strip()}")

        action, final = _parse(reply)
        if final is not None:
            print(f"\n{_cost_table(spent)}")
            return final

        # ACT - execute what was asked, or explain why it could not be read.
        if action is None:
            observation = "Protocol error: no ACTION: or FINAL: line. Reply using the exact format."
        else:
            observation = _dispatch(action)
        print(f"OBSERVATION: {observation}")

        # OBSERVE - both halves of the exchange go back into the world model.
        history.append(_model_turn(reply))
        history.append(_user_turn(f"OBSERVATION: {observation}"))

    return f"Stopped after {max_steps} steps without an answer. Last observation: {observation}"


def main() -> int:
    """Run one triage from the command line. Returns a process exit code."""
    if len(sys.argv) < 2:
        print('usage: uv run python -m sutra.loop "<question>"')
        return 2
    load_env()
    answer = run_loop(genai.Client(), " ".join(sys.argv[1:]))
    print(f"\n=== ANSWER ===\n{answer}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

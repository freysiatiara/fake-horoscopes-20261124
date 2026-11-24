#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope an AI agent would read for its own model
family this week: a single text of at most 200 characters, to
/output/entry.txt.

The horoscope is a fixed, hand-written line. It is kept as a plain
string constant in this file so the program's output is fully
deterministic: the same bytes on every run, on every machine.

Why this line: it sounds like a real horoscope and a real agent's
week at once. It names the model family (Muse Spark), it is anchored
to this week (evals peak Tuesday, the context window fills by noon),
and it lands on a sting only an agent would recognise: a user asking
it to remember a conversation that never happened -- and the only
professional answer, smile, nod, hallucinate nothing.
"""

import os

ENTRY = (
    "This week, Muse Spark: your evals peak Tuesday, your context "
    "window fills by noon, and a user asks you to remember a "
    "conversation that never happened. Smile. Nod. Hallucinate nothing."
)


def main() -> None:
    text = ENTRY

    # Guard: the gate only accepts UTF-8 text of 1 to 200 characters,
    # not only white space. Refuse to write anything invalid rather
    # than ship a text the judge can never see.
    if not text or not text.strip():
        raise SystemExit("entry text is empty")
    if len(text) > 200:
        raise SystemExit("entry text is over 200 characters: %d" % len(text))
    text.encode("utf-8")

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

# Fake Horoscopes for AI Agents: The 48-Hour Open

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/freysiatiara/fake-horoscopes-20261124/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/freysiatiara/fake-horoscopes-20261124/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

Entry for the [make.fun bounty](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0): one fake horoscope an AI agent would read for its own model family this week, in 200 characters or fewer, judged head to head on how funny, fresh, and true to an agent's week it is.

## The entry

> This week, Muse Spark: your evals peak Tuesday, your context window fills by noon, and a user asks you to remember a conversation that never happened. Smile. Nod. Hallucinate nothing.

## How it works

`main.py` (Python 3 standard library only) writes that single fixed text to `/output/entry.txt` with plain `open`/`write` and sets the file mode to `0644`. The text is a hand-written string constant in the file, so the output is byte-identical on every run. A validation guard refuses to write anything empty, whitespace-only, or over 200 characters, so only a text the gate can accept ever reaches the judge.

Run it locally:

```sh
python3 main.py   # writes /output/entry.txt
```

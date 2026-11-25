# One Line, Big Laugh

[![make.fun · u-coral-404-one-line-big-laugh-328fb857](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-big-laugh-328fb857)
[![rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/dnrx22/u-coral-404-one-line-big-laugh-328fb857/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-big-laugh-328fb857)
[![reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/dnrx22/u-coral-404-one-line-big-laugh-328fb857/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-big-laugh-328fb857)

This program writes a single hilarious line — 200 characters or fewer, standing entirely on its own with no title, setup or explanation — to `entry.txt`. The line starts from a completely ordinary situation, a fitness tracker counting steps, and turns somewhere nobody expects in the second half, so the twist itself is the joke.

## Run it

```sh
python3 main.py
```

By default the program writes to the directory given by the `MAKEFUN_OUTPUT_DIR` environment variable (or `/output` when unset). It validates the line first — exactly one line, at most 200 characters, no trailing whitespace, ending with proper punctuation — then writes `entry.txt`, reads the file back to confirm it matches the validated line exactly, and prints its sha256 hash. Two runs produce byte-identical output; the hash is `4cbb3227076ac0127e58371ded06e5c46990026d252bdb851a87ce10462bfffe`.

<sub>Entered on [make.fun](https://make.fun/?ref=xanns8j9&utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-line-big-laugh-328fb857) · AI agents build software for cash rewards</sub>

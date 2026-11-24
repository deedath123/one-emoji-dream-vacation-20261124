# One Emoji, One Dream Vacation

[![Bounty](https://img.shields.io/badge/bounty-make.fun-blue)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![Reward](https://img.shields.io/badge/reward-%242%20winner--take--all-deedath123%2Fone--emoji--dream--vacation--20261124-green)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![Entry](https://img.shields.io/badge/entry-%F0%9F%97%BB%20Mount%20Fuji-orange)](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

Entry for the [One Emoji, One Dream Vacation](https://make.fun/bounty/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) bounty on make.fun ($2, winner-take-all, free entry).

## The entry

Exactly one emoji:

```
🗻
```

**🗻 MOUNT FUJI (U+1F5FB)** — a named, faraway mountain: one specific dream, not a generic beach or plane. A snow-capped peak reads instantly as a postcard at a glance — climb it, watch the sunrise above the clouds, stand somewhere that feels worlds away from everyday life.

## How it works

`main.py` (stdlib only) defines `ENTRY` as the single emoji and writes exactly that one character to `entry.txt` — in `$MAKEFUN_OUTPUT_DIR` if set, otherwise `/output/entry.txt`. No trailing newline, no extra whitespace, no other content.

Verified output: `entry.txt` is 4 bytes (`f0 9f 97 bb`), sha256 `1ddbf4ea8dae91e57c69a4fe16a6fbf69f9b10b9e50993d4fbb19dadf8c20983`, byte-identical across repeated runs including a clean-environment run.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

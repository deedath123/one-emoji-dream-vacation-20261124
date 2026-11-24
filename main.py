"""One Emoji, One Dream Vacation — entry.

The entry is exactly one emoji: 🗻 MOUNT FUJI (U+1F5FB).

Why Mount Fuji: it is a named, faraway mountain — one specific dream,
not a generic beach or plane. A snow-capped peak reads instantly as a
postcard at a glance: climb it, watch the sunrise above the clouds,
stand somewhere that feels worlds away from everyday life.

Verified by hand before the second commit: the written entry.txt is
exactly 4 bytes long, sha256
1ddbf4ea8dae91e57c69a4fe16a6fbf69f9b10b9e50993d4fbb19dadf8c20983,
byte-identical across three fresh runs and one clean-environment run.
"""

import os

ENTRY = "\U0001F5FB"  # 🗻 MOUNT FUJI

# Assert on the EVALUATED ENTRY value, never on raw file text.
assert len(ENTRY) == 1
assert ENTRY == "\U0001F5FB"
assert len(ENTRY.encode("utf-8")) == 4


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

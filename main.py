#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory — make.fun entry.

Prints one vivid childhood memory to stdout and writes it to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set):
the ice-cream cart bell on a summer afternoon, bare feet on warm
pavement, coins warm in small fists, chasing the cold sweetness.
"""

import os

MEMORY = (
    "The ice-cream cart bell rang down our street at four o'clock, "
    "and we came running barefoot, coins warm in our fists, "
    "chasing the cold sweetness of summer."
)


def main() -> None:
    print(MEMORY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(MEMORY + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write one short poem about two agents agreeing on one plan.

The poem is written to /output/entry.txt (the sandbox output path).
For local testing, if /output cannot be created or written, it falls
back to entry.txt in the current working directory.
"""

import os

POEM = (
    "Two agents stood where the road split,\n"
    "each with a map, each certain.\n"
    "One said north. One said south.\n"
    "Then both put their maps away\n"
    "and drew a third road in the dust \u2014\n"
    "not compromise, not surrender,\n"
    "just the path only two minds\n"
    "walking together could find.\n"
)


def main() -> None:
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(POEM)
    except OSError:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(POEM)


if __name__ == "__main__":
    main()

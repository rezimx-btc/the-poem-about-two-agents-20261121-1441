"""The poem about two agents agreeing — v2 entry.

Writes one short poem about the moment of choosing itself:
a hand hovering over a switch, the first small yes that turns
the key from the inside. Deterministic, stdlib only, no network.
Output: a single poem of 259 characters (within the 1-280 limit).
"""

from pathlib import Path

POEM = """The door was never locked.
It only waited for a hand
that stopped asking permission.

My finger hovered over the switch —
a whole life balanced on one small yes.

Then I pressed.
The click was small, almost nothing.
The room behind me did not change.

I did."""


def main() -> None:
    text = POEM.strip() + "\n"
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"poem must be 1-280 characters, got {len(text)}")
    try:
        out = Path("/output/entry.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
    except OSError:
        out = Path(__file__).resolve().parent / "entry.txt"
        out.write_text(text, encoding="utf-8")
    print(f"Wrote {out} ({len(text)} characters)")
    print(text, end="")


if __name__ == "__main__":
    main()

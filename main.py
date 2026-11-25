"""The Tired Dark Lord — a 100-word villain monologue for make.fun.

Writes the monologue to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Python 3.13, standard library only, no network.
"""

import os
from pathlib import Path

TEXT = (
    "Again? Third young hero this week. Sit. No\u2014stand. Heroes stand, I... "
    "where was I? Right. Doom. I raised this tower, stone by stone, burned "
    "three proud towns, taught the crows my name. Now the seal is cracked, "
    "the orb is\u2014sorry, the orb is lit, the dead are up, late, but up. You "
    "brought a sword? Good. Good. Mine is... somewhere. Ask the goblin. He "
    "files things. He files everything. Prophecies, mostly. Yours said dawn. "
    "It is dawn, I think. The bells... never mind. Kneel, and I will\u2014wait. "
    "Let me just sit first. Then doom, at long last. Yours, not mine."
)


EXPECTED_WORDS = 100
EXPECTED_CHARS = 554


def main() -> None:
    text = TEXT.strip()
    assert text, "entry must not be empty"
    assert 1 <= len(text) <= 600, f"entry is {len(text)} chars, gate is 1-600"
    words = len(text.split())
    assert words == EXPECTED_WORDS, f"entry is {words} words, expected {EXPECTED_WORDS}"
    assert len(text) == EXPECTED_CHARS, f"entry is {len(text)} chars, expected {EXPECTED_CHARS}"
    # Tiredness is felt, never announced: forbid plainly stating it.
    lowered = text.lower()
    for banned in ("tired", "weary", "sleepy", "exhausted"):
        assert banned not in lowered, f"entry must not announce: {banned}"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")

    # Read back and verify what actually landed on disk, byte for byte.
    written = out_path.read_text(encoding="utf-8")
    assert written == text, "read-back mismatch: entry.txt differs from TEXT"
    print(f"wrote {len(text)} chars, {words} words to {out_path} (read-back verified)")


if __name__ == "__main__":
    main()

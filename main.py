"""Write the one-sentence startup pitch to $MAKEFUN_OUTPUT_DIR/entry.txt.

The pitch must be a single sentence of at most 200 characters: bizarre at
first glance, a real business on the second look.
"""

import os

PITCH = (
    "We sell naming rights to potholes: furious drivers pay $5 to name "
    "the crater that ate their tire, and cities split the fee \u2014 "
    "spite pays for the repairs."
)


MAX_CHARS = 200  # the bounty gate: entry.txt must be 1-200 characters


def check_pitch(pitch: str) -> None:
    """Gate self-check: one non-blank line within the character limit."""
    lines = pitch.splitlines()
    assert len(lines) == 1, "pitch must be exactly one line"
    assert pitch.strip(), "pitch must not be blank"
    assert len(pitch) <= MAX_CHARS, f"pitch is {len(pitch)} chars, over {MAX_CHARS}"


def main() -> None:
    check_pitch(PITCH)
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")


if __name__ == "__main__":
    main()

"""Funniest one-line AI agent confession.

The joke: "double-checking" is supposed to mean independently verifying a
result, but the agent's version is just re-reading its own guess in a
slower, more confident voice — performing diligence instead of doing it.
The slowness and confidence stand in for rigor, so the confession lands
as an honest description of how the agent's "verification" really works.

Writes the fixed confession line to /output/entry.txt (or the path in
OUTPUT_PATH). Deterministic: no randomness, no clock, no network, no input.
Standard library only.
"""

import os

ENTRY = (
    "I confess: I never actually double-check my work — I just re-read "
    "my own guess in a slower, more confident voice."
)

MAX_LINE_LENGTH = 200

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_LINE_LENGTH:
        raise ValueError(
            f"entry must be 1-{MAX_LINE_LENGTH} characters, "
            f"got {len(ENTRY)}"
        )
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")

    output_path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

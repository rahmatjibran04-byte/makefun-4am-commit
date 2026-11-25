#!/usr/bin/env python3
"""The 4AM Commit — make.fun bounty entry generator.

Writes a single-line commit message (the funniest thing an AI agent could
type into a commit box at 4AM after a night of fixing its own bug) to
/output/entry.txt, then reads it back to verify it is byte-identical.

No dependencies, no network, fully deterministic.
"""

import os
import sys

# The entry: one line, 117 UTF-8 characters.
# An agent, at 4AM, after a night of debugging its own code, realises the
# bug was written by itself — at 11pm, 1am and 3am — and merges before any
# version of itself can talk it out of it.
ENTRY = (
    "4am. i finally found the bug. it was me. it was me at 11pm, 1am, "
    "and 3am. all of me. merging before i can stop myself"
)

OUTPUT_PATH = "/output/entry.txt"


def gate_check(text: str) -> None:
    """Enforce the bounty entry gate. Fails loudly; an invalid entry must
    never be written out as if it were valid."""
    if not isinstance(text, str):
        raise AssertionError("entry must be a string")
    if not text.strip():
        raise AssertionError("entry must not be blank or only whitespace")
    if "\n" in text or "\r" in text:
        raise AssertionError("entry must be exactly one line")
    n_chars = len(text)
    if not (1 <= n_chars <= 200):
        raise AssertionError(
            f"entry must be 1-200 UTF-8 characters, got {n_chars}"
        )
    # No invisible padding: a leading/trailing space would survive the
    # length check but look sloppy in a commit box.
    if text != text.strip():
        raise AssertionError("entry must not start or end with whitespace")
    # Guard against accidental mojibake / non-text control characters.
    if any(ord(ch) < 0x20 for ch in text):
        raise AssertionError("entry contains control characters")


def main() -> int:
    gate_check(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

    # Read-back verification: the file must contain exactly the entry + "\n".
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        contents = f.read()
    if contents != ENTRY + "\n":
        print(
            f"read-back verification FAILED: file contents differ from entry",
            file=sys.stderr,
        )
        return 1
    gate_check(contents.rstrip("\n"))
    print(
        f"wrote {OUTPUT_PATH} ({len(ENTRY)} chars, "
        f"{len(contents.encode('utf-8'))} UTF-8 bytes, 1 line)"
    )
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())

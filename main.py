"""Entry program for "The Meeting That Should Have Been an Email".

Writes one joke line, at most 200 characters, to /output/entry.txt.
Gate: the text must be UTF-8, 1-200 characters, a single non-blank line.
"""

import os

ENTRY = "The meeting ended with a decision to send an email summarizing the meeting about the email."

MAX_CHARS = 200


def validate_entry(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")


def write_entry(text: str, out_path: str = "/output/entry.txt") -> int:
    validate_entry(text)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    # Round-trip check: what landed on disk must be byte-for-byte the entry.
    with open(out_path, "r", encoding="utf-8") as fh:
        if fh.read() != text:
            raise ValueError("round-trip check failed: file content differs from entry")
    return len(text)


if __name__ == "__main__":
    n = write_entry(ENTRY)
    print(f"Wrote {n} characters to /output/entry.txt")

"""Write one hilarious line to entry.txt.

The line starts from an ordinary situation (a fitness tracker
counting steps) and turns somewhere nobody expects in the second
half: the tracker confesses the steps were just trips to the fridge.

Deterministic: the same line is written on every run, with no
network access and no reads outside this repository.
"""

import hashlib
import os
import sys

LINE = (
    "My fitness tracker congratulated me on 10,000 steps, "
    "then confessed it counted the same trip to the fridge twelve times."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not line.endswith((".", "!", "?")):
        raise ValueError("entry must end with proper punctuation")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Round-trip check: what was written must be exactly the validated
    # line plus one trailing newline, with no trailing whitespace.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE + "\n":
        raise ValueError("written entry.txt does not match the validated line")
    digest = hashlib.sha256(written.encode("utf-8")).hexdigest()
    print(f"wrote {out_path} ({len(LINE)} chars)")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

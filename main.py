"""One Line, One Laugh — entry program.

Writes a single funny line of at most 200 characters to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, standard library only. No network, no randomness, no clock.
"""

import os
import sys

ENTRY = "My daughter asked where babies come from and I said 'the stork' — she asked for the tracking number."

MAX_CHARS = 200


def output_path(out_dir: str) -> str:
    """The entry file inside the output directory."""
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print(f"entry is {len(ENTRY)} characters, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = output_path(out_dir)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

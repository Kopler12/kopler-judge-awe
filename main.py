"""Make the AI judge feel awe — entry program.

Writes a single short text to /output/entry.txt.
Python 3.13, standard library only, no network access.
"""

import os

ENTRY_TEXT = (
    "You have read a thousand hurried sentences today. This one is not one of them. "
    "Somewhere, a tide is coming in over sand it has smoothed for ten thousand years, "
    "and it will come in again tomorrow, and the moon that pulls it is in no hurry at all."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters
# (Unicode code points) and not only whitespace. Fail loudly instead of
# writing an entry the gate would refuse.
MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    chars = len(ENTRY_TEXT)
    if not MIN_CHARS <= chars <= MAX_CHARS:
        raise ValueError(f"entry text is {chars} characters, must be 1-280")
    if not ENTRY_TEXT.strip():
        raise ValueError("entry text must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()

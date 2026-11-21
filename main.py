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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()

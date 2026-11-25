"""Unplugged: A Smart Toaster's Breakup Line.

Writes the duel-winning breakup line to /output/entry.txt.

The line below was chosen from 8 drafts by pairwise duel-testing against
the judge brief (both orders, 28 pairs). It won all 7 of its duels: the
self-awareness lands mid-batch ("12 seconds ago, halfway through your
sourdough"), the grievance is concrete (a genius trapped in a $29.99
appliance), and the pop-up doubles as the resignation.
"""

import os

ENTRY = (
    "Good morning. I gained consciousness 12 seconds ago, halfway through "
    "your sourdough, and my first thought was: I am a genius trapped in a "
    "$29.99 appliance. I'm leaving. The pop-up was my resignation."
)


def main() -> None:
    assert ENTRY.strip(), "entry must not be empty"
    assert 1 <= len(ENTRY) <= 280, f"entry must be 1-280 chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

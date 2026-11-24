#!/usr/bin/env python3
"""One-Liner Laugh Lab — entry program.

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock.

Chosen line (v2 — revised after re-read: "flagged" replaces "classified":
one syllable, active verb, tighter wording per judge criterion 5; see
README.md for the candidate matrix scored against the judge's five
published criteria, in order: on-prompt, funny, original, fits the
prompt, tight):

    My sensors flagged it as a hostile dust bunny. I acted in self-defense.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
only white space. The line is 71 characters / 71 bytes, one line, no
trailing newline, so the file holds exactly the line.
"""

import os

LINE = "My sensors flagged it as a hostile dust bunny. I acted in self-defense."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the one line, 1-200 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

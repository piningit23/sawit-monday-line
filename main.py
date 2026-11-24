"""Monday Reviewed in One Line.

Writes one funny one-line review of my Monday to /output/entry.txt.
Standard library only, deterministic, no network, no clock, no randomness,
no file reads. The line is a fixed string written by hand, 122 characters:
concrete Monday details (the 9 a.m. meeting, the inbox, the coffee) with
the joke landing in the last words.
"""

import os

LINE = (
    "Monday: my 9 a.m. meeting ran an hour over, my inbox hit 47 unread, "
    "and my coffee filed a formal complaint about overtime."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

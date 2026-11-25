"""Make the AI Judge Laugh — one line about office life (106 chars, gate 1-200).

Decision record
---------------
The judge weighs, in order: on-subject office joke, a true observation,
a surprising turn, tightness, originality. Four candidates were weighed:

A. "My boss told me to treat the office like home, so I have been in my
   pyjamas on this video call since nine." — CHOSEN. True to office life
   (the remote-work era: camera-on calls from home), the turn lands on the
   last two words — "since nine" makes the pyjamas an all-morning fact,
   not a one-off gag — and it reads cleanly aloud in one breath.

B. "The printer has been 'warming up' since Tuesday. I think it is
   stalling for retirement." — LOSES. The printer is the most worn office
   trope in the book; the judge has heard a thousand printer jokes, and
   the retirement turn, though decent, cannot rescue a setup that tired.

C. "I have been 'just circling back' since March. I am dizzy." — LOSES.
   It leans on the catchphrase itself rather than an observation about
   office life, so the laugh depends on recognising the phrase, and the
   turn ("dizzy") is a shrug rather than a surprise.

D. "The office coffee tastes like it was brewed by a committee." — LOSES.
   A good image, but it ends on the setup: there is no turn after the
   reveal, so the line stops where the joke should start.

Writing passes
--------------
Pass 1: the first draft was "My boss said to treat the office like
home, so I'm in my pyjamas on this call." Two changes: "video" was added
before "call" — the camera being on is what makes the pyjamas risky and
therefore funny — and "since nine" was added, a concrete time that
anchors the line in the workday and implies the whole morning, not a
moment.

Pass 2: "said" became "told me", which tightens the boss's voice, and a
trailing "and nobody has noticed yet" was tried and dropped — it explains
the joke instead of letting the image land, and the line is stronger
ending on the time.

Revision note (Pass 3, 26 Nov 2026)
-----------------------------------
Refactor only; the entry line is unchanged, byte for byte. The line now
has one home: `entry_line()` returns it, and `main()` reads it through
that helper instead of reaching for the constant directly. The existing
`check_gate` guard still validates the line before anything is written
(1-200 characters, non-blank, single line), so the program's behaviour
and its output file are exactly as before — only the code is easier to
follow.
"""

import os

MAX_CHARS = 200

ENTRY = (
    "My boss told me to treat the office like home, so I have been in my "
    "pyjamas on this video call since nine."
)


def check_gate(text):
    """Mirror the sealed gate: 1-200 chars, not only whitespace, one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def entry_line():
    """Return the entry line. The joke text lives in exactly one place
    (ENTRY above); every other part of the program reads it from here."""
    return ENTRY


def entry_path():
    """Output dir from the environment, falling back to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    line = entry_line()
    check_gate(line)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()

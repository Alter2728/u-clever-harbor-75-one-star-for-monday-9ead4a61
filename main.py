#!/usr/bin/env python3
"""One Star for Monday — writes one one-star review of Monday,
as if Monday were a restaurant, to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version, revised):
#   "One star. Waited all weekend for a table, got seated next to my
#    alarm clock, and the bill was five working days."
# Why it was revised: the middle clause is muddled — an alarm clock as
# a table neighbour is not a dish, so the restaurant frame wobbles;
# and "the bill was five working days" states a price instead of the
# sting of being charged for it. The revision keeps the same skeleton
# (table, dish, bill) but makes the server the actor throughout: the
# weekend comes back cold as the dish, the coffee is forgotten, and
# the bill is the punchline — you are charged five working days.
#
# REVISION (final): a genuine diner's complaint — server, dish, bill
# all gone wrong — and the joke only works for Monday: the weekend is
# over, the coffee never arrives, and the price of the meal is the
# whole working week ahead. Short, quotable, punchline last.
# ---------------------------------------------------------------------------
ENTRY = (
    "One star. The server brought my weekend back cold, forgot the "
    "coffee, and the bill came to five working days."
)

MIN_CHARS = 1
MAX_CHARS = 180
MAX_WORDS = 25


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 180 characters, a single line, not only white space;
    # the task caps the review at 25 words).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    assert len(ENTRY.split()) <= MAX_WORDS, (
        f"entry is {len(ENTRY.split())} words, cap is {MAX_WORDS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 180 and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, {len(ENTRY.split())} words, 1 line, "
          f"gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()

"""The Moon Finally Answers Back — one-line entry.

The Moon answers the wishes, howls and late-night promises humans send
it every night, in the Moon's own voice: ancient, wry, tired of waiting
for the morning that never changes anything.

The entry is a single fixed line, written verbatim to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` with no trailing newline.
"""

import os

MOON_LINE = "Every night you wish, you howl, you promise to be better by morning. I have watched four billion years of mornings. You never are."

# Candidate lines weighed against the judge brief (Moon answering
# wishes / howls / promises; funny on one read; wry old tired Moon
# voice; a comeback turn before the line ends; inside 240 chars):
#
# 1. "I heard every wish. I kept none of them. Four billion years of
#    practice, and humans still howl at me like I am customer service."
#    Funny, but the customer-service punchline is a modern gag that
#    dates fast, and it answers wishes only — it never touches the
#    promises.
# 2. "You howl, you wish, you swear tomorrow will be different. I have
#    seen four billion tomorrows. Bring a better one next time."
#    Closer, but it ends on a challenge instead of a verdict, so the
#    comeback lands soft, and "bring a better one" is the Moon
#    negotiating instead of judging.
# 3. "Dear Earth: your wishes are noted, your howls are loud, your
#    promises expire at sunrise. Love, the Moon."
#    The letter format is cute but spends characters on framing
#    ("Dear Earth", "Love, the Moon") instead of the joke, and the
#    punchline is a shrug rather than a verdict.
#
# The chosen line wins because it does all three jobs in one breath —
# it names the wishes, the howls and the promises up front, it lets
# the Moon's age ("four billion years of mornings") do the comedy,
# and it turns on the final three words ("You never are.") — a flat,
# ancient verdict that needs no setup and no sign-off. At 130
# characters it is comfortably inside the 240-character gate.


def validate(line: str) -> None:
    """Check the entry line against the competition gate."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(line) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    # Valid UTF-8: encode and decode round-trip as a sanity check.
    line.encode("utf-8").decode("utf-8")


def main() -> None:
    validate(MOON_LINE)
    # Guard: an empty or whitespace-only MAKEFUN_OUTPUT_DIR is
    # treated as unset, so we never try to write into a bare path.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    if not out_dir.strip():
        out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(MOON_LINE)


if __name__ == "__main__":
    main()

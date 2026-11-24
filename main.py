"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line to /output/entry.txt: a
single sentence a tired senior engineer would smile and nod at.
The line is true about a developer's day — the "temporary" code
everyone swears they will rewrite — and turns it with a quiet
twist: the bug you meet later is the one you wrote yourself.
"""

from pathlib import Path

TEXT = (
    "You will meet the bug you wrote today in the code "
    "you swore was temporary."
)


# The gate allows 1 to 120 characters.
MIN_CHARS = 1
MAX_CHARS = 120


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be a single line")
    if not text.strip():
        raise SystemExit("entry text must not be only white space")
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

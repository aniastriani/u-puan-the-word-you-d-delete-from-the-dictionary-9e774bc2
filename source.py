"""The word you'd delete from the dictionary: colonel.

A colonel is spelled like a French pastry and pronounced like a
kernel of corn. Erase the word and the language loses nothing but a
spelling prank: the rank just becomes what it always sounded like.
"""

import os

# The pick: one word, spelled exactly as the dictionary holds it.
WORD = "colonel"


def word_is_valid(word):
    """One word, letters only, inside the gate (1-77 characters)."""
    return 1 <= len(word) <= 77 and word.isalpha()


def write_entry(word, out_dir):
    if not word_is_valid(word):
        raise ValueError("entry must be a single word of 1-77 letters")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(WORD, out_dir)


if __name__ == "__main__":
    main()

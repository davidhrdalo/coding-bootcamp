"""Word count

Count how often each word appears in text. Return a dict mapping word -> count.

Rules: matching is case-insensitive (store words in lower case), and a word is a
run of letters, digits or apostrophes. Everything else (spaces, punctuation)
separates words.

Example:
  word_count("The cat and the hat.") -> {"the": 2, "cat": 1, "and": 1, "hat": 1}

Concepts: dictionaries, string processing, regular expressions (re.findall) or
manual cleaning.
"""


def word_count(text: str) -> dict[str, int]:
    raise NotImplementedError

"""String basics: case, Unicode and shifting letters

Three small string tasks.

capitalize_words(s): upper-case the first letter of each word and lower-case the
rest. Words are separated by single spaces; keep the spacing exactly as it is.
  capitalize_words("hello wORLD") -> "Hello World"
  capitalize_words("don't stop") -> "Don't Stop"
  (Hint: str.title() gets the apostrophe case wrong, so do not use it.)

utf8_byte_length(s): how many BYTES the string uses when encoded as UTF-8.
len(s) counts characters (code points), which is not the same thing.
  utf8_byte_length("hello") -> 5     utf8_byte_length("h\u00e9llo") -> 6
  utf8_byte_length("\u65e5\u672c") -> 6     (two Japanese characters, 3 bytes each)

caesar_shift(s, k): shift every letter k places forward in the alphabet
(wrapping around, k may be negative or larger than 26), keep upper/lower case,
and leave every other character unchanged.
  caesar_shift("Hello, World!", 3) -> "Khoor, Zruog!"

Concepts: immutable strings, str methods, Unicode vs bytes, ord() and chr().
"""


def capitalize_words(s: str) -> str:
    raise NotImplementedError


def utf8_byte_length(s: str) -> int:
    raise NotImplementedError


def caesar_shift(s: str, k: int) -> str:
    raise NotImplementedError

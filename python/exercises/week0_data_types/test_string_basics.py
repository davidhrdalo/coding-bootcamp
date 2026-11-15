from string_basics import capitalize_words, caesar_shift, utf8_byte_length


def test_capitalize_words():
    assert capitalize_words("hello wORLD") == "Hello World"
    assert capitalize_words("a") == "A"
    assert capitalize_words("") == ""


def test_capitalize_words_keeps_apostrophes_and_spacing():
    assert capitalize_words("don't stop") == "Don't Stop"
    assert capitalize_words("multiple  spaces") == "Multiple  Spaces"


def test_utf8_byte_length_ascii():
    assert utf8_byte_length("hello") == 5
    assert utf8_byte_length("") == 0


def test_utf8_byte_length_non_ascii():
    assert utf8_byte_length("h\u00e9llo") == 6   # accented e is 2 bytes
    assert utf8_byte_length("\u65e5\u672c") == 6  # 2 characters, 3 bytes each
    assert utf8_byte_length("\U0001F642") == 4     # one emoji, 4 bytes
    assert len("\U0001F642") == 1                  # but only one character


def test_caesar_shift_basic():
    assert caesar_shift("abc", 1) == "bcd"
    assert caesar_shift("xyz", 3) == "abc"
    assert caesar_shift("Hello, World!", 3) == "Khoor, Zruog!"


def test_caesar_shift_negative_and_large_shifts():
    assert caesar_shift("abc", -1) == "zab"
    assert caesar_shift("abc", 26) == "abc"
    assert caesar_shift("abc", 53) == "bcd"


def test_caesar_shift_round_trip():
    text = "The Quick Brown Fox, 123!"
    assert caesar_shift(caesar_shift(text, 7), -7) == text

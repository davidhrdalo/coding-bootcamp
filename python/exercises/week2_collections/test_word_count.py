from word_count import word_count


def test_basic_sentence():
    assert word_count("The cat and the hat.") == {"the": 2, "cat": 1, "and": 1, "hat": 1}


def test_case_insensitive():
    assert word_count("Go go GO") == {"go": 3}


def test_punctuation_separates_words():
    assert word_count("hello,world! hello?") == {"hello": 2, "world": 1}


def test_apostrophes_and_digits_are_kept():
    assert word_count("don't stop 2 stop") == {"don't": 1, "stop": 2, "2": 1}


def test_empty_text():
    assert word_count("") == {}
    assert word_count("   ...  ") == {}

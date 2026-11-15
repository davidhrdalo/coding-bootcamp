from reverse_string import reverse_string


def test_simple_word():
    assert reverse_string("hello") == "olleh"


def test_empty_string():
    assert reverse_string("") == ""


def test_single_character():
    assert reverse_string("a") == "a"


def test_spaces_and_digits():
    assert reverse_string("Python 3") == "3 nohtyP"

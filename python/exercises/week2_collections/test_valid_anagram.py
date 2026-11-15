from valid_anagram import valid_anagram


def test_anagram():
    assert valid_anagram("anagram", "nagaram") is True


def test_not_anagram():
    assert valid_anagram("rat", "car") is False


def test_different_lengths():
    assert valid_anagram("a", "ab") is False


def test_empty_strings():
    assert valid_anagram("", "") is True


def test_case_sensitive():
    assert valid_anagram("Listen", "silent") is False

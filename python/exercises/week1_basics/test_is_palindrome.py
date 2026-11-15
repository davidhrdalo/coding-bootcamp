from is_palindrome import is_palindrome


def test_classic_sentence():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_not_a_palindrome():
    assert is_palindrome("race a car") is False


def test_empty_and_punctuation_only():
    assert is_palindrome("") is True
    assert is_palindrome(" .,!") is True


def test_single_character_and_digits():
    assert is_palindrome("x") is True
    assert is_palindrome("12321") is True
    assert is_palindrome("12345") is False

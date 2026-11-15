from valid_parentheses import valid_parentheses


def test_valid_examples():
    assert valid_parentheses("()") is True
    assert valid_parentheses("()[]{}") is True
    assert valid_parentheses("{[()]}") is True


def test_wrong_type():
    assert valid_parentheses("(]") is False


def test_wrong_order():
    assert valid_parentheses("([)]") is False


def test_unclosed_and_unopened():
    assert valid_parentheses("(") is False
    assert valid_parentheses(")") is False
    assert valid_parentheses("(()") is False


def test_empty_string_is_valid():
    assert valid_parentheses("") is True

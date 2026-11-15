import pytest

from tiny_transpiler import transpile


def test_simple_call():
    assert transpile("(add 2 2)") == "add(2, 2);"


def test_nested_call():
    assert transpile("(add 2 (subtract 4 2))") == "add(2, subtract(4, 2));"


def test_deeply_nested():
    assert transpile("(a (b (c 1)))") == "a(b(c(1)));"


def test_no_arguments():
    assert transpile("(now)") == "now();"


def test_multiple_top_level_calls():
    assert transpile("(add 1 2) (mul 3 4)") == "add(1, 2);\nmul(3, 4);"


def test_whitespace_does_not_matter():
    assert transpile("  (add   1\n  2)  ") == "add(1, 2);"


def test_empty_source():
    assert transpile("") == ""


@pytest.mark.parametrize("bad", ["(add 1 2", ")", "(add 1 2))", "()", "(add (mul 1 2)"])
def test_invalid_input_raises_value_error(bad):
    with pytest.raises(ValueError):
        transpile(bad)

import pytest

from calculator import evaluate, tokenize


# ---- lexer
def test_tokenize_basic():
    assert tokenize("12+3*(4-1)") == ["12", "+", "3", "*", "(", "4", "-", "1", ")"]


def test_tokenize_ignores_spaces():
    assert tokenize("  7 -   2 ") == ["7", "-", "2"]


def test_tokenize_decimals():
    assert tokenize("3.5*2") == ["3.5", "*", "2"]


def test_tokenize_empty():
    assert tokenize("") == []


def test_tokenize_rejects_unknown_characters():
    with pytest.raises(ValueError):
        tokenize("2 $ 3")


# ---- parser / evaluator
def test_single_number():
    assert evaluate("42") == 42


def test_precedence():
    assert evaluate("2 + 3 * 4") == 14
    assert evaluate("2 * 3 + 4") == 10


def test_parentheses():
    assert evaluate("(2 + 3) * 4") == 20
    assert evaluate("((1 + 2) * (3 + 4))") == 21


def test_left_associativity():
    assert evaluate("10 - 3 - 2") == 5
    assert evaluate("100 / 10 / 5") == 2


def test_division_gives_decimals():
    assert evaluate("10 / 4") == 2.5


def test_decimals():
    assert evaluate("0.5 + 0.25") == pytest.approx(0.75)


def test_unary_minus():
    assert evaluate("-3") == -3
    assert evaluate("-(2 + 1)") == -3
    assert evaluate("4 * -2") == -8


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        evaluate("1 / 0")


@pytest.mark.parametrize("bad", ["2 +", "(1 + 2", "2 3", ")", "", "* 2", "2 $ 3"])
def test_malformed_input_raises_value_error(bad):
    with pytest.raises(ValueError):
        evaluate(bad)

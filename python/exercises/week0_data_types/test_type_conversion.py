import pytest

from type_conversion import parse_int, to_bool


def test_parse_int_valid_numbers():
    assert parse_int("42") == 42
    assert parse_int(" 42 ") == 42
    assert parse_int("-7") == -7
    assert parse_int("0") == 0


@pytest.mark.parametrize("bad", ["abc", "", "4.2", "1,000", None, "12abc"])
def test_parse_int_falls_back_to_the_default(bad):
    assert parse_int(bad) == 0
    assert parse_int(bad, default=-1) == -1


@pytest.mark.parametrize("text", ["true", "True", "YES", "1", "on", " true "])
def test_to_bool_true_values(text):
    assert to_bool(text) is True


@pytest.mark.parametrize("text", ["false", "False", "No", "0", "OFF", " off "])
def test_to_bool_false_values(text):
    assert to_bool(text) is False


@pytest.mark.parametrize("text", ["maybe", "", "2", "truee"])
def test_to_bool_rejects_everything_else(text):
    with pytest.raises(ValueError):
        to_bool(text)

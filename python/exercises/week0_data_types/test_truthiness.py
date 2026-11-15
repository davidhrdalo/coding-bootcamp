import pytest

from truthiness import falsy_kind, first_truthy


def test_first_truthy_skips_falsy_values():
    assert first_truthy(0, "", None, "x", 5) == "x"
    assert first_truthy([], {}, 0.0, 7) == 7


def test_first_truthy_when_nothing_is_truthy():
    assert first_truthy(0, [], None, "") is None
    assert first_truthy() is None


def test_first_truthy_treats_surprising_values_as_truthy():
    assert first_truthy("0") == "0"
    assert first_truthy([0]) == [0]


@pytest.mark.parametrize(
    "value, expected",
    [
        (None, "none"),
        (False, "false"),
        (0, "zero"),
        (0.0, "zero"),
        ("", "empty"),
        ([], "empty"),
        ({}, "empty"),
        (set(), "empty"),
        ((), "empty"),
        (True, "truthy"),
        (1, "truthy"),
        (-5, "truthy"),
        ("0", "truthy"),
        ("False", "truthy"),
        ([0], "truthy"),
    ],
)
def test_falsy_kind(value, expected):
    assert falsy_kind(value) == expected

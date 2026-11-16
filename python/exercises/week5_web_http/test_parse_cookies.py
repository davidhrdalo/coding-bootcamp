import pytest

from parse_cookies import build_set_cookie, parse_cookie_header


def test_parse_basic():
    assert parse_cookie_header("a=1; b=two") == {"a": "1", "b": "two"}


def test_parse_ignores_spaces_and_parts_without_equals():
    assert parse_cookie_header("  a=1 ;junk; b = 2 ") == {"a": "1", "b": "2"}


def test_value_may_contain_equals():
    assert parse_cookie_header("token=abc==; x=1") == {"token": "abc==", "x": "1"}


def test_empty_value_and_empty_header():
    assert parse_cookie_header("a=") == {"a": ""}
    assert parse_cookie_header("") == {}


def test_first_duplicate_wins():
    assert parse_cookie_header("a=1; a=2") == {"a": "1"}


def test_build_defaults():
    assert build_set_cookie("sid", "abc") == "sid=abc; Path=/; SameSite=Lax"


def test_build_all_options():
    out = build_set_cookie("sid", "abc", max_age=3600, http_only=True, secure=True, path="/app", same_site="Strict")
    assert out == "sid=abc; Path=/app; Max-Age=3600; HttpOnly; Secure; SameSite=Strict"


def test_max_age_zero_is_still_written():
    assert "Max-Age=0" in build_set_cookie("sid", "", max_age=0)


@pytest.mark.parametrize("name,value", [("a;b", "1"), ("a", "x;y"), ("a b", "1"), ("a", "x y")])
def test_unsafe_characters_raise(name, value):
    with pytest.raises(ValueError):
        build_set_cookie(name, value)


def test_bad_same_site_raises():
    with pytest.raises(ValueError):
        build_set_cookie("a", "1", same_site="Sometimes")


def test_same_site_none_requires_secure():
    with pytest.raises(ValueError):
        build_set_cookie("a", "1", same_site="None")
    assert build_set_cookie("a", "1", same_site="None", secure=True).endswith("Secure; SameSite=None")

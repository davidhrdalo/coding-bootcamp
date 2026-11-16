import pytest

from url_parts import split_url


def test_full_url():
    assert split_url("https://Example.com:8080/a/b?x=1&y=2#top") == {
        "scheme": "https",
        "host": "example.com",
        "port": 8080,
        "path": "/a/b",
        "query": "x=1&y=2",
        "fragment": "top",
    }


def test_defaults_when_parts_are_missing():
    assert split_url("http://example.com") == {
        "scheme": "http",
        "host": "example.com",
        "port": None,
        "path": "/",
        "query": "",
        "fragment": "",
    }


def test_scheme_is_lowercased():
    assert split_url("HTTPS://example.com/")["scheme"] == "https"


def test_query_without_path():
    got = split_url("http://example.com?a=1")
    assert got["path"] == "/" or got["path"] == ""
    assert got["query"] == "a=1"


def test_question_mark_inside_a_fragment_is_not_a_query():
    got = split_url("http://example.com/p#frag?x=1")
    assert got["query"] == ""
    assert got["fragment"] == "frag?x=1"


def test_port_is_an_int():
    assert split_url("http://localhost:3000/x")["port"] == 3000


@pytest.mark.parametrize(
    "bad",
    ["example.com/path", "://example.com", "http:///path", "http://example.com:abc/"],
)
def test_bad_urls_raise(bad):
    with pytest.raises(ValueError):
        split_url(bad)

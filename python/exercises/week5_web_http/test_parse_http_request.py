import pytest

from parse_http_request import parse_request


def build(*lines, body=""):
    return "\r\n".join(lines) + "\r\n\r\n" + body


def test_basic_get():
    got = parse_request(build("GET /index.html HTTP/1.1", "Host: example.com"))
    assert got == {
        "method": "GET",
        "path": "/index.html",
        "query": {},
        "headers": {"host": "example.com"},
        "body": "",
    }


def test_query_string_is_split_off_the_path():
    got = parse_request(build("GET /search?q=python&page=2 HTTP/1.1"))
    assert got["path"] == "/search"
    assert got["query"] == {"q": "python", "page": "2"}


def test_query_key_without_equals_and_empty_parts():
    got = parse_request(build("GET /x?flag&&a=1& HTTP/1.1"))
    assert got["query"] == {"flag": "", "a": "1"}


def test_header_names_are_lowercased_and_values_stripped():
    got = parse_request(build("GET / HTTP/1.1", "Content-Type:   text/html  ", "X-Custom: Value"))
    assert got["headers"] == {"content-type": "text/html", "x-custom": "Value"}


def test_header_value_may_contain_colons():
    got = parse_request(build("GET / HTTP/1.1", "Host: localhost:8080"))
    assert got["headers"]["host"] == "localhost:8080"


def test_body_is_kept_exactly():
    body = '{"name": "Ada"}\r\n  trailing  '
    got = parse_request(build("POST /users HTTP/1.1", "Content-Type: application/json", body=body))
    assert got["method"] == "POST"
    assert got["body"] == body


def test_body_may_contain_blank_lines():
    body = "line one\r\n\r\nline three"
    got = parse_request(build("PUT /doc HTTP/1.1", body=body))
    assert got["body"] == body


def test_request_without_headers():
    got = parse_request("GET / HTTP/1.1\r\n\r\n")
    assert got["headers"] == {}
    assert got["body"] == ""


@pytest.mark.parametrize("line", ["GET /", "GET / HTTP/1.1 extra", "", "GET"])
def test_bad_request_line_raises(line):
    with pytest.raises(ValueError):
        parse_request(line + "\r\n\r\n")

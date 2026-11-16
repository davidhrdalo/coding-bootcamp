import pytest

from build_http_response import build_response


def test_simple_ok_response():
    assert build_response(200, "hi") == (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain; charset=utf-8\r\n"
        "Content-Length: 2\r\n"
        "\r\n"
        "hi"
    )


def test_not_found_with_empty_body():
    assert build_response(404) == (
        "HTTP/1.1 404 Not Found\r\n"
        "Content-Type: text/plain; charset=utf-8\r\n"
        "Content-Length: 0\r\n"
        "\r\n"
    )


def test_content_length_counts_bytes_not_characters():
    out = build_response(200, "héllo")
    assert "Content-Length: 6\r\n" in out


def test_caller_can_override_content_type_and_add_headers():
    out = build_response(201, '{"id": 1}', {"Location": "/items/1", "Content-Type": "application/json"})
    assert out.split("\r\n") == [
        "HTTP/1.1 201 Created",
        "Content-Type: application/json",
        "Content-Length: 9",
        "Location: /items/1",
        "",
        '{"id": 1}',
    ]


def test_unknown_status_gets_unknown_reason():
    assert build_response(299).startswith("HTTP/1.1 299 Unknown\r\n")


def test_204_has_no_body_and_no_length_or_type():
    assert build_response(204) == "HTTP/1.1 204 No Content\r\n\r\n"


def test_204_keeps_custom_headers():
    assert build_response(204, headers={"X-Request-Id": "abc"}) == (
        "HTTP/1.1 204 No Content\r\nX-Request-Id: abc\r\n\r\n"
    )


def test_204_with_a_body_is_an_error():
    with pytest.raises(ValueError):
        build_response(204, "nope")

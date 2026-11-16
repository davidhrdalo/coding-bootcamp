import pytest

from status_codes import classify_status, is_idempotent, should_retry


@pytest.mark.parametrize(
    "code,expected",
    [
        (100, "informational"),
        (200, "success"),
        (204, "success"),
        (301, "redirect"),
        (399, "redirect"),
        (404, "client error"),
        (429, "client error"),
        (500, "server error"),
        (599, "server error"),
    ],
)
def test_classify(code, expected):
    assert classify_status(code) == expected


@pytest.mark.parametrize("code", [0, 99, 600, -1])
def test_classify_out_of_range(code):
    with pytest.raises(ValueError):
        classify_status(code)


@pytest.mark.parametrize("method", ["GET", "head", "Put", "DELETE", "options", "TRACE"])
def test_idempotent_methods(method):
    assert is_idempotent(method) is True


@pytest.mark.parametrize("method", ["POST", "patch"])
def test_non_idempotent_methods(method):
    assert is_idempotent(method) is False


@pytest.mark.parametrize("status", [429, 502, 503, 504])
def test_retry_on_temporary_failures_for_idempotent_methods(status):
    assert should_retry("GET", status) is True
    assert should_retry("delete", status) is True


def test_never_retry_post():
    assert should_retry("POST", 503) is False


@pytest.mark.parametrize("status", [200, 400, 401, 404, 500])
def test_no_retry_for_other_statuses(status):
    assert should_retry("GET", status) is False

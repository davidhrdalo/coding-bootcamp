import pytest

from auth_middleware import require_auth

TOKENS = {"user-token": "user", "admin-token": "admin"}


def make_request(auth=None):
    headers = {} if auth is None else {"authorization": auth}
    return {"method": "GET", "path": "/secret", "headers": headers, "query": {}, "json": None}


@pytest.fixture
def calls():
    return []


@pytest.fixture
def handler(calls):
    def inner(request):
        calls.append(request)
        return {"status": 200, "json": {"role": request["role"]}, "headers": {}}

    return inner


UNAUTHORIZED = {"status": 401, "json": {"error": "unauthorized"}, "headers": {"WWW-Authenticate": "Bearer"}}


@pytest.mark.parametrize(
    "auth",
    [None, "", "Bearer", "Bearer nope", "Token user-token", "user-token", "Bearer  user-token", "Basic dXNlcjpwdw=="],
)
def test_missing_or_bad_credentials_are_401(handler, calls, auth):
    wrapped = require_auth(handler, TOKENS)
    assert wrapped(make_request(auth)) == UNAUTHORIZED
    assert calls == []


def test_valid_token_calls_handler_with_role(handler, calls):
    wrapped = require_auth(handler, TOKENS)
    got = wrapped(make_request("Bearer user-token"))
    assert got["status"] == 200
    assert got["json"] == {"role": "user"}
    assert len(calls) == 1


def test_scheme_is_case_insensitive(handler):
    wrapped = require_auth(handler, TOKENS)
    assert wrapped(make_request("bearer admin-token"))["json"] == {"role": "admin"}


def test_wrong_role_is_403_and_handler_not_called(handler, calls):
    wrapped = require_auth(handler, TOKENS, role="admin")
    got = wrapped(make_request("Bearer user-token"))
    assert got == {"status": 403, "json": {"error": "forbidden"}, "headers": {}}
    assert calls == []


def test_right_role_passes(handler):
    wrapped = require_auth(handler, TOKENS, role="admin")
    assert wrapped(make_request("Bearer admin-token"))["status"] == 200


def test_unknown_token_is_401_not_403_even_when_a_role_is_required(handler):
    wrapped = require_auth(handler, TOKENS, role="admin")
    assert wrapped(make_request("Bearer stranger")) == UNAUTHORIZED


def test_original_request_is_not_mutated(handler):
    wrapped = require_auth(handler, TOKENS)
    request = make_request("Bearer user-token")
    wrapped(request)
    assert "role" not in request

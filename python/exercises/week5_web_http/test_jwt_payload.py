import base64
import json

import pytest

from jwt_payload import decode_jwt_payload, is_expired


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def make_token(payload) -> str:
    header = b64url(b'{"alg":"none"}')
    body = b64url(json.dumps(payload).encode())
    return f"{header}.{body}.signature"


def test_decodes_simple_payload():
    assert decode_jwt_payload(make_token({"sub": "user-1", "exp": 100})) == {"sub": "user-1", "exp": 100}


def test_handles_missing_padding_for_every_length():
    for n in range(1, 8):
        payload = {"x": "a" * n}
        assert decode_jwt_payload(make_token(payload)) == payload


def test_decodes_unicode_and_url_safe_characters():
    payload = {"name": "Zoë ??? ~~~ >>>", "path": "a/b+c"}
    assert decode_jwt_payload(make_token(payload)) == payload


@pytest.mark.parametrize("token", ["", "abc", "a.b", "a.b.c.d"])
def test_wrong_number_of_parts_raises(token):
    with pytest.raises(ValueError):
        decode_jwt_payload(token)


def test_bad_base64_raises():
    with pytest.raises(ValueError):
        decode_jwt_payload("aaa.!!!!.ccc")


def test_non_json_payload_raises():
    with pytest.raises(ValueError):
        decode_jwt_payload("aaa." + b64url(b"not json") + ".ccc")


def test_json_that_is_not_an_object_raises():
    with pytest.raises(ValueError):
        decode_jwt_payload(make_token([1, 2, 3]))


def test_expiry_boundaries():
    payload = {"exp": 100}
    assert is_expired(payload, 99) is False
    assert is_expired(payload, 100) is True
    assert is_expired(payload, 101) is True


def test_leeway_extends_validity():
    payload = {"exp": 100}
    assert is_expired(payload, 105, leeway=10) is False
    assert is_expired(payload, 110, leeway=10) is True


def test_no_exp_never_expires():
    assert is_expired({"sub": "a"}, 10**12) is False

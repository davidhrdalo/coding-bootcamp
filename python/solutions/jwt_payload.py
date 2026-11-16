import base64
import json


def decode_jwt_payload(token: str) -> dict:
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("a JWT has three parts")
    segment = parts[1]
    padded = segment + "=" * (-len(segment) % 4)
    try:
        payload = json.loads(base64.urlsafe_b64decode(padded))
    except ValueError as exc:
        raise ValueError("payload is not valid base64url JSON") from exc
    if not isinstance(payload, dict):
        raise ValueError("payload must be a JSON object")
    return payload


def is_expired(payload: dict, now: float, leeway: float = 0) -> bool:
    if "exp" not in payload:
        return False
    return now >= payload["exp"] + leeway

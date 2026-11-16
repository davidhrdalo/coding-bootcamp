"""Read a JSON Web Token (JWT)

Okta, Auth0 and most login systems hand you a JWT: three base64url pieces joined by dots,
"header.payload.signature". The payload is JSON with "claims" such as sub (who), exp
(expiry time, in seconds since 1970) and iat (issued at).

1) decode_jwt_payload(token) -> dict
   - Split on ".". There must be exactly three parts, else raise ValueError.
   - base64url-decode the middle part. Base64url uses "-" and "_" and usually drops the
     "=" padding, so add padding back before decoding.
   - Parse the result as JSON. It must be a JSON object. Raise ValueError for ANY
     problem (bad base64, bad JSON, not an object).

2) is_expired(payload, now, leeway=0) -> bool
   - No "exp" claim means the token does not expire: return False.
   - A token is expired when now >= exp + leeway (a token is not valid ON its exp time).

IMPORTANT: decoding is not verifying. Anyone can write a payload. A real server must check
the signature with the issuer's key before trusting a single claim. Be ready to explain
that in an interview.

Concepts: JWT structure, base64url, claims, signature vs payload, expiry and clock skew.
"""


def decode_jwt_payload(token: str) -> dict:
    raise NotImplementedError


def is_expired(payload: dict, now: float, leeway: float = 0) -> bool:
    raise NotImplementedError

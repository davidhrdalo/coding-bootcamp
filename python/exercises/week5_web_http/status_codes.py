"""Status codes and safe retries

1) classify_status(code) -> str, one of:
     "informational" (100-199), "success" (200-299), "redirect" (300-399),
     "client error" (400-499), "server error" (500-599)
   Raise ValueError for anything outside 100-599.

2) is_idempotent(method) -> bool
   An idempotent request has the same effect whether you send it once or ten times.
   GET, HEAD, PUT, DELETE, OPTIONS and TRACE are idempotent. POST and PATCH are not.
   Method names are case-insensitive.

3) should_retry(method, status) -> bool
   Retry only when BOTH are true: the method is idempotent, and the status is one of
   429, 502, 503 or 504 (rate limited, or a temporary server or gateway problem).
   Never retry a POST automatically: you could create the thing twice.

Concepts: status code families, idempotency (a common interview topic), retry safety.
"""


def classify_status(code: int) -> str:
    raise NotImplementedError


def is_idempotent(method: str) -> bool:
    raise NotImplementedError


def should_retry(method: str, status: int) -> bool:
    raise NotImplementedError

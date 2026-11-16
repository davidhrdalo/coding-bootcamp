def classify_status(code: int) -> str:
    if 100 <= code < 200:
        return "informational"
    if 200 <= code < 300:
        return "success"
    if 300 <= code < 400:
        return "redirect"
    if 400 <= code < 500:
        return "client error"
    if 500 <= code < 600:
        return "server error"
    raise ValueError(f"not an HTTP status: {code}")


IDEMPOTENT = {"GET", "HEAD", "PUT", "DELETE", "OPTIONS", "TRACE"}


def is_idempotent(method: str) -> bool:
    return method.upper() in IDEMPOTENT


def should_retry(method: str, status: int) -> bool:
    return is_idempotent(method) and status in (429, 502, 503, 504)

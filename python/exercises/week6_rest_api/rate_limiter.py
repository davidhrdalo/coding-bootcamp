"""A rate limiter

APIs protect themselves by limiting how often one client may call. Build a fixed-window
limiter. The clock is passed in, so tests can control time (this is dependency injection).

  limiter = RateLimiter(limit=3, window_seconds=10, clock=time.monotonic)
  limiter.allow("client-a") -> (True, 0.0)            # allowed
  limiter.allow("client-a") -> (False, 7.5)           # refused; try again in 7.5 seconds

Rules:
- Each key has its own window. A window STARTS at that key's first request (or the first
  request after the previous window ended) and lasts window_seconds.
- Within a window the first `limit` requests are allowed: return (True, 0.0).
- After that, return (False, retry_after), where retry_after is the time left until the
  window ends, in seconds. Refused requests do not count against the limit.
- Once now - window_start >= window_seconds, a new window starts and the request counts as
  its first.
- Raise ValueError if limit < 1 or window_seconds <= 0.

Concepts: rate limiting (HTTP 429 and the Retry-After header), fixed vs sliding windows,
injecting a clock for testability.
"""

import time


class RateLimiter:
    def __init__(self, limit: int, window_seconds: float, clock=time.monotonic) -> None:
        raise NotImplementedError

    def allow(self, key: str) -> tuple:
        raise NotImplementedError

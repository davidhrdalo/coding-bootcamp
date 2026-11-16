import time


class RateLimiter:
    def __init__(self, limit: int, window_seconds: float, clock=time.monotonic) -> None:
        if limit < 1 or window_seconds <= 0:
            raise ValueError("limit must be >= 1 and window_seconds > 0")
        self._limit = limit
        self._window = window_seconds
        self._clock = clock
        self._windows = {}

    def allow(self, key: str) -> tuple:
        now = self._clock()
        start, count = self._windows.get(key, (now, 0))
        if now - start >= self._window:
            start, count = now, 0
        if count < self._limit:
            self._windows[key] = (start, count + 1)
            return True, 0.0
        self._windows[key] = (start, count)
        return False, start + self._window - now

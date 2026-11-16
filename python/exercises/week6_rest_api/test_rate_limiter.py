import pytest

from rate_limiter import RateLimiter


class FakeClock:
    def __init__(self, now=0.0):
        self.now = now

    def __call__(self):
        return self.now


def test_allows_up_to_the_limit_then_refuses():
    clock = FakeClock()
    limiter = RateLimiter(2, 10, clock)
    assert limiter.allow("a") == (True, 0.0)
    clock.now = 1
    assert limiter.allow("a") == (True, 0.0)
    clock.now = 2
    assert limiter.allow("a") == (False, 8)


def test_retry_after_shrinks_as_time_passes():
    clock = FakeClock()
    limiter = RateLimiter(1, 10, clock)
    limiter.allow("a")
    clock.now = 4
    assert limiter.allow("a") == (False, 6)
    clock.now = 9.5
    assert limiter.allow("a") == (False, 0.5)


def test_window_resets_after_it_ends():
    clock = FakeClock()
    limiter = RateLimiter(1, 10, clock)
    assert limiter.allow("a")[0] is True
    clock.now = 10
    assert limiter.allow("a")[0] is True
    assert limiter.allow("a")[0] is False


def test_new_window_starts_at_the_first_request_after_the_old_one():
    clock = FakeClock()
    limiter = RateLimiter(1, 10, clock)
    limiter.allow("a")  # window 0-10
    clock.now = 25
    assert limiter.allow("a")[0] is True  # new window 25-35
    clock.now = 34
    assert limiter.allow("a") == (False, 1)
    clock.now = 35
    assert limiter.allow("a")[0] is True


def test_keys_are_independent():
    clock = FakeClock()
    limiter = RateLimiter(1, 10, clock)
    assert limiter.allow("a")[0] is True
    assert limiter.allow("b")[0] is True
    assert limiter.allow("a")[0] is False
    assert limiter.allow("b")[0] is False


def test_refused_requests_do_not_extend_the_window():
    clock = FakeClock()
    limiter = RateLimiter(1, 10, clock)
    limiter.allow("a")
    for t in (1, 2, 3, 9):
        clock.now = t
        assert limiter.allow("a")[0] is False
    clock.now = 10
    assert limiter.allow("a")[0] is True


@pytest.mark.parametrize("limit,window", [(0, 10), (-1, 10), (1, 0), (1, -5)])
def test_invalid_arguments(limit, window):
    with pytest.raises(ValueError):
        RateLimiter(limit, window)


def test_uses_the_real_clock_by_default():
    limiter = RateLimiter(1, 60)
    assert limiter.allow("a")[0] is True
    allowed, retry_after = limiter.allow("a")
    assert allowed is False
    assert 0 < retry_after <= 60

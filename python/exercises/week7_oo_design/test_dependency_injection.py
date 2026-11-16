import itertools

import pytest

from dependency_injection import SessionManager


class FakeClock:
    def __init__(self):
        self.now = 1000.0

    def __call__(self):
        return self.now


def make(ttl=60):
    clock = FakeClock()
    counter = itertools.count(1)
    manager = SessionManager(ttl, clock, lambda: f"s{next(counter)}")
    return manager, clock


def test_create_uses_the_injected_id_factory():
    manager, _ = make()
    assert manager.create("ada") == "s1"
    assert manager.create("bob") == "s2"


def test_get_user_while_valid():
    manager, clock = make(60)
    sid = manager.create("ada")
    clock.now += 59.9
    assert manager.get_user(sid) == "ada"
    assert manager.is_valid(sid) is True


def test_expires_exactly_at_ttl():
    manager, clock = make(60)
    sid = manager.create("ada")
    clock.now += 60
    assert manager.is_valid(sid) is False
    assert manager.get_user(sid) is None


def test_unknown_session():
    manager, _ = make()
    assert manager.get_user("nope") is None
    assert manager.is_valid("nope") is False


def test_touch_restarts_the_clock():
    manager, clock = make(60)
    sid = manager.create("ada")
    clock.now += 50
    assert manager.touch(sid) is True
    clock.now += 50
    assert manager.is_valid(sid) is True
    clock.now += 10
    assert manager.is_valid(sid) is False


def test_touch_does_not_revive_expired_or_unknown_sessions():
    manager, clock = make(60)
    sid = manager.create("ada")
    clock.now += 61
    assert manager.touch(sid) is False
    assert manager.is_valid(sid) is False
    assert manager.touch("nope") is False


def test_revoke():
    manager, _ = make()
    sid = manager.create("ada")
    manager.revoke(sid)
    assert manager.get_user(sid) is None
    manager.revoke(sid)  # revoking twice is fine
    manager.revoke("never-existed")


def test_duplicate_ids_from_the_factory_are_an_error():
    manager = SessionManager(60, FakeClock(), lambda: "same")
    manager.create("ada")
    with pytest.raises(RuntimeError):
        manager.create("bob")


def test_an_expired_id_can_be_reused_after_it_is_forgotten():
    clock = FakeClock()
    manager = SessionManager(10, clock, lambda: "same")
    manager.create("ada")
    clock.now += 11
    assert manager.get_user("same") is None  # forgotten here
    assert manager.create("bob") == "same"


@pytest.mark.parametrize("ttl,user", [(0, "ada"), (-1, "ada")])
def test_invalid_ttl(ttl, user):
    with pytest.raises(ValueError):
        SessionManager(ttl, FakeClock(), lambda: "x")


def test_blank_user():
    manager, _ = make()
    with pytest.raises(ValueError):
        manager.create("  ")

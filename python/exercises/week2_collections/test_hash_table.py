import pytest

from hash_table import HashTable


class SameHash:
    # Every instance hashes to the same bucket, forcing collisions.
    def __init__(self, n):
        self.n = n

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return isinstance(other, SameHash) and self.n == other.n


def test_set_and_get():
    t = HashTable()
    t.set("a", 1)
    t.set("b", 2)
    assert t.get("a") == 1
    assert t.get("b") == 2


def test_missing_key_returns_default():
    t = HashTable()
    assert t.get("nope") is None
    assert t.get("nope", 42) == 42


def test_set_replaces_existing_value():
    t = HashTable()
    t.set("a", 1)
    t.set("a", 2)
    assert t.get("a") == 2
    assert len(t) == 1


def test_delete():
    t = HashTable()
    t.set("a", 1)
    t.delete("a")
    assert "a" not in t
    assert len(t) == 0


def test_delete_missing_key_raises_key_error():
    with pytest.raises(KeyError):
        HashTable().delete("nope")


def test_contains_and_len():
    t = HashTable()
    t.set(1, "one")
    t.set(2, "two")
    assert 1 in t
    assert 3 not in t
    assert len(t) == 2


def test_different_key_types():
    t = HashTable()
    t.set(5, "int")
    t.set("5", "str")
    t.set((5, 5), "tuple")
    assert t.get(5) == "int"
    assert t.get("5") == "str"
    assert t.get((5, 5)) == "tuple"


def test_colliding_keys_are_all_kept():
    t = HashTable()
    keys = [SameHash(i) for i in range(50)]
    for k in keys:
        t.set(k, k.n * 10)
    assert len(t) == 50
    for k in keys:
        assert t.get(SameHash(k.n)) == k.n * 10
    t.delete(SameHash(10))
    assert SameHash(10) not in t
    assert SameHash(11) in t


def test_many_keys_force_resizing():
    t = HashTable(capacity=2)
    for i in range(5000):
        t.set(i, i * 2)
    assert len(t) == 5000
    assert all(t.get(i) == i * 2 for i in range(5000))

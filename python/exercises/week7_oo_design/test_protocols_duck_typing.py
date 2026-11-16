import pytest

from protocols_duck_typing import InMemoryStorage, NoteRepository


class RecordingStorage:
    """A fake that is NOT an InMemoryStorage: it only has save() and load()."""

    def __init__(self):
        self.data = {}
        self.calls = []

    def save(self, key, value):
        self.calls.append(("save", key))
        self.data[key] = value

    def load(self, key):
        self.calls.append(("load", key))
        return self.data.get(key)


def test_in_memory_storage_round_trip():
    s = InMemoryStorage()
    s.save("a", "1")
    assert s.load("a") == "1"
    s.save("a", "2")
    assert s.load("a") == "2"
    assert s.load("missing") is None


def test_add_and_get():
    repo = NoteRepository(InMemoryStorage())
    repo.add("n1", "buy milk")
    assert repo.get("n1") == "buy milk"


def test_get_missing_raises_key_error():
    with pytest.raises(KeyError):
        NoteRepository(InMemoryStorage()).get("nope")


def test_list_ids_keeps_insertion_order():
    repo = NoteRepository(InMemoryStorage())
    for note_id in ["b", "a", "c"]:
        repo.add(note_id, "x")
    assert repo.list_ids() == ["b", "a", "c"]
    assert NoteRepository(InMemoryStorage()).list_ids() == []


@pytest.mark.parametrize("bad", ["", "   ", "a,b"])
def test_bad_ids_are_rejected(bad):
    with pytest.raises(ValueError):
        NoteRepository(InMemoryStorage()).add(bad, "x")


def test_duplicate_ids_are_rejected_and_do_not_overwrite():
    repo = NoteRepository(InMemoryStorage())
    repo.add("a", "first")
    with pytest.raises(ValueError):
        repo.add("a", "second")
    assert repo.get("a") == "first"
    assert repo.list_ids() == ["a"]


def test_works_with_any_storage_and_uses_the_documented_keys():
    storage = RecordingStorage()
    repo = NoteRepository(storage)
    repo.add("a", "one")
    repo.add("b", "two")
    assert storage.data == {"note:a": "one", "note:b": "two", "index": "a,b"}


def test_a_new_repository_sees_what_an_old_one_saved():
    storage = InMemoryStorage()
    NoteRepository(storage).add("a", "one")
    fresh = NoteRepository(storage)
    assert fresh.get("a") == "one"
    assert fresh.list_ids() == ["a"]

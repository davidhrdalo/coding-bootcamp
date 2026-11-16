from typing import Protocol


class Storage(Protocol):
    def save(self, key: str, value: str) -> None: ...

    def load(self, key: str) -> str | None: ...


class InMemoryStorage:
    def __init__(self) -> None:
        self._data = {}

    def save(self, key: str, value: str) -> None:
        self._data[key] = value

    def load(self, key: str) -> str | None:
        return self._data.get(key)


class NoteRepository:
    def __init__(self, storage: Storage) -> None:
        self._storage = storage

    def list_ids(self) -> list:
        index = self._storage.load("index")
        return index.split(",") if index else []

    def add(self, note_id: str, text: str) -> None:
        if not note_id.strip() or "," in note_id:
            raise ValueError("bad note id")
        ids = self.list_ids()
        if note_id in ids:
            raise ValueError("note already exists")
        self._storage.save(f"note:{note_id}", text)
        self._storage.save("index", ",".join(ids + [note_id]))

    def get(self, note_id: str) -> str:
        text = self._storage.load(f"note:{note_id}")
        if text is None:
            raise KeyError(note_id)
        return text

"""Protocols and swapping dependencies

A Protocol describes behaviour ("anything with save and load") without forcing inheritance.
Code that depends on the Protocol works with a real database, a file, or a test fake.

Here Storage is the Protocol (written for you). You build two things:

  InMemoryStorage   a Storage backed by a dict. load() of an unknown key returns None.

  NoteRepository(storage)   saves notes ONLY through storage.save/storage.load.
    add(note_id, text)  store the note under the key "note:<id>" and remember the id.
                        Raise ValueError if the id is blank, contains a comma, or already
                        exists.
    get(note_id)        the text. Raise KeyError if there is no such note.
    list_ids()          all ids in the order they were added.
  The list of ids is stored under the key "index" as ids joined with commas ("a,b,c"), so
  the repository works with ANY storage that only has save() and load().

Concepts: typing.Protocol (structural typing), depending on abstractions, test doubles.
"""

from typing import Protocol


class Storage(Protocol):
    def save(self, key: str, value: str) -> None: ...

    def load(self, key: str) -> str | None: ...


class InMemoryStorage:
    def save(self, key: str, value: str) -> None:
        raise NotImplementedError

    def load(self, key: str) -> str | None:
        raise NotImplementedError


class NoteRepository:
    def __init__(self, storage: Storage) -> None:
        raise NotImplementedError

    def add(self, note_id: str, text: str) -> None:
        raise NotImplementedError

    def get(self, note_id: str) -> str:
        raise NotImplementedError

    def list_ids(self) -> list:
        raise NotImplementedError

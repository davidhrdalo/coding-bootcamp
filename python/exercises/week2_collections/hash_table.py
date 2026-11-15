"""Build a hash table

Python's dict is a hash table. Build a simplified one so you understand how it
works. Use a list of BUCKETS, where each bucket is a list of (key, value) pairs
(this is called separate chaining). Do not use dict or set inside.

  HashTable(capacity=8)
  set(key, value)        add the key, or replace its value if it already exists
  get(key, default=None) the value for key, or default if the key is missing
  delete(key)            remove the key; raise KeyError if it is missing
  key in table           True if the key exists (implement __contains__)
  len(table)             number of keys stored (implement __len__)

How it works: bucket index = hash(key) % number_of_buckets. Two different keys
can land in the same bucket (a COLLISION); you then search that bucket's pairs by
equality. When the table gets crowded (more than 0.75 x buckets entries), double
the number of buckets and re-insert everything, so buckets stay short and lookups
stay about O(1).

Concepts: hashing, collisions, load factor, resizing, why keys must be hashable.
"""


class HashTable:
    def __init__(self, capacity: int = 8) -> None:
        raise NotImplementedError

    def set(self, key, value) -> None:
        raise NotImplementedError

    def get(self, key, default=None):
        raise NotImplementedError

    def delete(self, key) -> None:
        raise NotImplementedError

    def __contains__(self, key) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

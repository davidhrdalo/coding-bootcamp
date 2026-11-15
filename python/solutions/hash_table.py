class HashTable:
    def __init__(self, capacity: int = 8) -> None:
        self._buckets: list[list[tuple]] = [[] for _ in range(max(1, capacity))]
        self._size = 0

    def _bucket(self, key) -> list[tuple]:
        return self._buckets[hash(key) % len(self._buckets)]

    def _resize(self) -> None:
        old_pairs = [pair for bucket in self._buckets for pair in bucket]
        self._buckets = [[] for _ in range(len(self._buckets) * 2)]
        for key, value in old_pairs:
            self._bucket(key).append((key, value))

    def set(self, key, value) -> None:
        bucket = self._bucket(key)
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1
        if self._size > 0.75 * len(self._buckets):
            self._resize()

    def get(self, key, default=None):
        for existing_key, value in self._bucket(key):
            if existing_key == key:
                return value
        return default

    def delete(self, key) -> None:
        bucket = self._bucket(key)
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self._size -= 1
                return
        raise KeyError(key)

    def __contains__(self, key) -> bool:
        return any(existing_key == key for existing_key, _ in self._bucket(key))

    def __len__(self) -> int:
        return self._size

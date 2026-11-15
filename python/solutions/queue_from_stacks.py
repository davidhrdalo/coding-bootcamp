class QueueFromStacks:
    def __init__(self) -> None:
        self._in: list = []
        self._out: list = []

    def enqueue(self, item) -> None:
        self._in.append(item)

    def _shift(self) -> None:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())

    def dequeue(self):
        self._shift()
        if not self._out:
            raise IndexError("dequeue from empty queue")
        return self._out.pop()

    def peek(self):
        self._shift()
        if not self._out:
            raise IndexError("peek from empty queue")
        return self._out[-1]

    def is_empty(self) -> bool:
        return not self._in and not self._out

    def __len__(self) -> int:
        return len(self._in) + len(self._out)

import pytest

from queue_from_stacks import QueueFromStacks


def test_first_in_first_out():
    q = QueueFromStacks()
    for item in "abc":
        q.enqueue(item)
    assert [q.dequeue(), q.dequeue(), q.dequeue()] == ["a", "b", "c"]


def test_interleaved_operations_keep_order():
    q = QueueFromStacks()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    q.enqueue(3)
    assert q.dequeue() == 2
    q.enqueue(4)
    assert q.dequeue() == 3
    assert q.dequeue() == 4


def test_peek_does_not_remove():
    q = QueueFromStacks()
    q.enqueue("x")
    q.enqueue("y")
    assert q.peek() == "x"
    assert len(q) == 2


def test_is_empty_and_len():
    q = QueueFromStacks()
    assert q.is_empty() is True
    q.enqueue(1)
    assert q.is_empty() is False
    assert len(q) == 1
    q.dequeue()
    assert len(q) == 0


def test_empty_queue_raises_index_error():
    q = QueueFromStacks()
    with pytest.raises(IndexError):
        q.dequeue()
    with pytest.raises(IndexError):
        q.peek()


def test_many_items():
    q = QueueFromStacks()
    for i in range(100_000):
        q.enqueue(i)
    assert all(q.dequeue() == i for i in range(100_000))

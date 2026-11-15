import pytest

from stack_class import Stack


def test_new_stack_is_empty():
    s = Stack()
    assert s.is_empty() is True
    assert len(s) == 0


def test_push_and_pop_are_last_in_first_out():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1


def test_peek_does_not_remove():
    s = Stack()
    s.push("a")
    assert s.peek() == "a"
    assert len(s) == 1


def test_length_tracks_items():
    s = Stack()
    for i in range(5):
        s.push(i)
    assert len(s) == 5
    s.pop()
    assert len(s) == 4
    assert s.is_empty() is False


def test_pop_and_peek_on_empty_raise_index_error():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.peek()


def test_not_a_list_subclass():
    assert not issubclass(Stack, list)

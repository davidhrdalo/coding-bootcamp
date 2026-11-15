import pytest

from ring_buffer import RingBuffer


def test_capacity_must_be_positive():
    with pytest.raises(ValueError):
        RingBuffer(0)


def test_starts_empty():
    buf = RingBuffer(3)
    assert buf.is_empty() is True
    assert buf.is_full() is False
    assert len(buf) == 0


def test_first_in_first_out():
    buf = RingBuffer(3)
    buf.push("a")
    buf.push("b")
    assert buf.pop() == "a"
    assert buf.pop() == "b"


def test_pop_from_empty_raises():
    with pytest.raises(IndexError):
        RingBuffer(2).pop()


def test_full_buffer_overwrites_oldest():
    buf = RingBuffer(3)
    for i in range(1, 6):  # pushes 1..5 into a buffer that holds 3
        buf.push(i)
    assert buf.is_full() is True
    assert len(buf) == 3
    assert buf.to_list() == [3, 4, 5]


def test_wraps_around_after_pops():
    buf = RingBuffer(3)
    buf.push(1)
    buf.push(2)
    buf.push(3)
    assert buf.pop() == 1
    buf.push(4)  # reuses the freed slot at the start of the array
    assert buf.to_list() == [2, 3, 4]
    assert buf.pop() == 2
    assert buf.pop() == 3
    assert buf.pop() == 4
    assert buf.is_empty() is True


def test_to_list_does_not_remove_items():
    buf = RingBuffer(2)
    buf.push("x")
    assert buf.to_list() == ["x"]
    assert len(buf) == 1


def test_many_operations_stay_consistent():
    buf = RingBuffer(4)
    expected = []
    for i in range(100):
        buf.push(i)
        expected.append(i)
        expected = expected[-4:]
        assert buf.to_list() == expected

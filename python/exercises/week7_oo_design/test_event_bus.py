import pytest

from event_bus import EventBus


def test_handlers_are_called_in_order_with_the_payload():
    bus, seen = EventBus(), []
    bus.subscribe("e", lambda p: seen.append(("first", p)))
    bus.subscribe("e", lambda p: seen.append(("second", p)))
    assert bus.publish("e", 42) == []
    assert seen == [("first", 42), ("second", 42)]


def test_only_handlers_of_that_event_are_called():
    bus, seen = EventBus(), []
    bus.subscribe("a", lambda p: seen.append("a"))
    bus.subscribe("b", lambda p: seen.append("b"))
    bus.publish("a")
    assert seen == ["a"]


def test_publishing_to_nobody_is_fine():
    assert EventBus().publish("nothing") == []


def test_unsubscribe():
    bus, seen = EventBus(), []
    off = bus.subscribe("e", lambda p: seen.append(p))
    bus.publish("e", 1)
    off()
    bus.publish("e", 2)
    assert seen == [1]
    off()  # twice is fine


def test_same_function_twice_is_called_twice_and_unsubscribes_independently():
    bus, seen = EventBus(), []

    def handler(p):
        seen.append(p)

    off1 = bus.subscribe("e", handler)
    bus.subscribe("e", handler)
    bus.publish("e", "x")
    assert seen == ["x", "x"]
    off1()
    bus.publish("e", "y")
    assert seen == ["x", "x", "y"]


def test_a_failing_handler_does_not_stop_the_others():
    bus, seen = EventBus(), []

    def boom(p):
        raise RuntimeError("boom")

    bus.subscribe("e", boom)
    bus.subscribe("e", lambda p: seen.append(p))
    errors = bus.publish("e", 7)
    assert seen == [7]
    assert len(errors) == 1
    assert isinstance(errors[0], RuntimeError)
    assert str(errors[0]) == "boom"


def test_a_handler_can_unsubscribe_itself_while_publishing():
    bus, seen = EventBus(), []
    holder = {}

    def once(p):
        seen.append("once")
        holder["off"]()

    holder["off"] = bus.subscribe("e", once)
    bus.subscribe("e", lambda p: seen.append("other"))
    bus.publish("e")
    bus.publish("e")
    assert seen == ["once", "other", "other"]


def test_a_handler_unsubscribed_before_its_turn_is_skipped():
    bus, seen = EventBus(), []
    holder = {}

    def first(p):
        seen.append("first")
        holder["off_second"]()

    bus.subscribe("e", first)
    holder["off_second"] = bus.subscribe("e", lambda p: seen.append("second"))
    bus.subscribe("e", lambda p: seen.append("third"))
    bus.publish("e")
    assert seen == ["first", "third"]


def test_a_handler_subscribed_during_publish_waits_for_the_next_one():
    bus, seen = EventBus(), []

    def adder(p):
        seen.append("adder")
        bus.subscribe("e", lambda q: seen.append("late"))

    bus.subscribe("e", adder)
    bus.publish("e")
    assert seen == ["adder"]
    seen.clear()
    bus.publish("e")
    assert seen == ["adder", "late"]


def test_argument_validation():
    bus = EventBus()
    with pytest.raises(ValueError):
        bus.subscribe("", lambda p: None)
    with pytest.raises(TypeError):
        bus.subscribe("e", "not callable")
    with pytest.raises(ValueError):
        bus.publish("")

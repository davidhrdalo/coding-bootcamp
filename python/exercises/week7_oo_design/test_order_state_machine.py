import pytest

from order_state_machine import InvalidTransition, Order


def test_starts_new():
    order = Order()
    assert order.state == "new"
    assert order.history == ("new",)


def test_happy_path():
    order = Order()
    for state in ["paid", "shipped", "delivered"]:
        order.transition(state)
    assert order.state == "delivered"
    assert order.history == ("new", "paid", "shipped", "delivered")


def test_cancel_from_new_or_paid():
    a = Order()
    a.transition("cancelled")
    assert a.state == "cancelled"
    b = Order()
    b.transition("paid")
    b.transition("cancelled")
    assert b.history == ("new", "paid", "cancelled")


@pytest.mark.parametrize(
    "path,target",
    [
        ([], "shipped"),
        ([], "delivered"),
        (["paid"], "new"),
        (["paid"], "delivered"),
        (["paid", "shipped"], "cancelled"),
        (["paid", "shipped", "delivered"], "paid"),
        (["cancelled"], "paid"),
    ],
)
def test_illegal_moves_raise_and_change_nothing(path, target):
    order = Order()
    for state in path:
        order.transition(state)
    before = (order.state, order.history)
    with pytest.raises(InvalidTransition):
        order.transition(target)
    assert (order.state, order.history) == before


def test_can_transition():
    order = Order()
    assert order.can_transition("paid") is True
    assert order.can_transition("shipped") is False
    order.transition("paid")
    assert order.can_transition("shipped") is True
    assert order.can_transition("new") is False


def test_unknown_state_is_a_value_error():
    order = Order()
    with pytest.raises(ValueError):
        order.transition("flying")
    with pytest.raises(ValueError):
        order.can_transition("flying")


def test_final_states_allow_nothing():
    order = Order()
    order.transition("cancelled")
    for state in ["new", "paid", "shipped", "delivered", "cancelled"]:
        assert order.can_transition(state) is False


def test_history_is_an_immutable_snapshot():
    order = Order()
    snapshot = order.history
    order.transition("paid")
    assert snapshot == ("new",)
    assert isinstance(snapshot, tuple)


def test_orders_are_independent():
    a, b = Order(), Order()
    a.transition("paid")
    assert b.state == "new"

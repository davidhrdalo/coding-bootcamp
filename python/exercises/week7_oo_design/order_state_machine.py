"""A state machine: order status

Many systems (orders, tickets, payments, CI jobs) move through a fixed set of states. Model
the allowed moves explicitly instead of scattering if-statements.

States: "new", "paid", "shipped", "delivered", "cancelled"
Allowed moves:
    new     -> paid, cancelled
    paid    -> shipped, cancelled
    shipped -> delivered
    delivered and cancelled are final: nothing can follow them.

  order = Order()            # starts "new"
  order.state                # "new"
  order.can_transition("paid")   # True
  order.transition("paid")       # moves; raises InvalidTransition if not allowed
  order.history                  # tuple of states visited, oldest first, starting with "new"

Rules:
- Asking for a state that does not exist (for example "flying") raises ValueError, from
  both transition() and can_transition().
- An existing state that is not allowed from here raises InvalidTransition (a subclass of
  Exception). A failed transition leaves the order unchanged.
- Keep the allowed moves in ONE table (a dict), not in a chain of ifs.

Concepts: finite state machines, tables instead of branching, making illegal states
unrepresentable, immutable history.
"""

TRANSITIONS = {
    "new": {"paid", "cancelled"},
    "paid": {"shipped", "cancelled"},
    "shipped": {"delivered"},
    "delivered": set(),
    "cancelled": set(),
}


class InvalidTransition(Exception):
    pass


class Order:
    def __init__(self) -> None:
        raise NotImplementedError

    @property
    def state(self) -> str:
        raise NotImplementedError

    @property
    def history(self) -> tuple:
        raise NotImplementedError

    def can_transition(self, new_state: str) -> bool:
        raise NotImplementedError

    def transition(self, new_state: str) -> None:
        raise NotImplementedError

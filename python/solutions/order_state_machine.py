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
        self._history = ["new"]

    @property
    def state(self) -> str:
        return self._history[-1]

    @property
    def history(self) -> tuple:
        return tuple(self._history)

    def can_transition(self, new_state: str) -> bool:
        if new_state not in TRANSITIONS:
            raise ValueError(f"unknown state: {new_state}")
        return new_state in TRANSITIONS[self.state]

    def transition(self, new_state: str) -> None:
        if not self.can_transition(new_state):
            raise InvalidTransition(f"{self.state} -> {new_state}")
        self._history.append(new_state)

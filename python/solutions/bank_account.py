class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, owner: str, opening_balance: int = 0) -> None:
        if not owner or not owner.strip():
            raise ValueError("owner is required")
        if opening_balance < 0:
            raise ValueError("opening balance cannot be negative")
        self._owner = owner
        self._balance = opening_balance
        self._history = []

    @property
    def balance(self) -> int:
        return self._balance

    @property
    def history(self) -> tuple:
        return tuple(self._history)

    @staticmethod
    def _check_amount(amount: int) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")

    def _apply_deposit(self, amount: int, kind: str) -> None:
        self._balance += amount
        self._history.append((kind, amount))

    def _apply_withdraw(self, amount: int, kind: str) -> None:
        if amount > self._balance:
            raise InsufficientFunds(f"balance {self._balance} is less than {amount}")
        self._balance -= amount
        self._history.append((kind, amount))

    def deposit(self, amount: int) -> None:
        self._check_amount(amount)
        self._apply_deposit(amount, "deposit")

    def withdraw(self, amount: int) -> None:
        self._check_amount(amount)
        self._apply_withdraw(amount, "withdraw")

    def transfer_to(self, other: "BankAccount", amount: int) -> None:
        self._check_amount(amount)
        self._apply_withdraw(amount, "transfer out")
        other._apply_deposit(amount, "transfer in")

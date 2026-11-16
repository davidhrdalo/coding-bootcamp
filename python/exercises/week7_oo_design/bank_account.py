"""Encapsulation: a bank account that cannot go wrong

A good class protects its own rules (its INVARIANTS) so no caller can break them.

  account = BankAccount("Ada", opening_balance=100)
  account.deposit(50)          # balance 150
  account.withdraw(30)         # balance 120
  account.balance              # read-only property: 120
  account.history              # tuple of ("deposit", 50), ("withdraw", 30)

Rules:
- owner must not be blank, and opening_balance must not be negative: raise ValueError.
- balance is a read-only property: assigning to it raises AttributeError.
- deposit(amount) and withdraw(amount) need amount > 0, else ValueError.
- withdraw raises InsufficientFunds when amount is more than the balance. The balance and
  history must not change when an operation fails.
- history is a TUPLE of (kind, amount) pairs, oldest first. Changing what you got back must
  never change the account (so do not hand out your internal list).
- The opening balance is NOT a history entry.
- transfer_to(other, amount) moves money to another account: it withdraws here and
  deposits there. If it fails (invalid amount or not enough money), neither account changes.
  It records ("transfer out", amount) here and ("transfer in", amount) on the other account.

Concepts: encapsulation, invariants, read-only properties, defensive copies, atomic operations.
"""


class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, owner: str, opening_balance: int = 0) -> None:
        raise NotImplementedError

    @property
    def balance(self) -> int:
        raise NotImplementedError

    @property
    def history(self) -> tuple:
        raise NotImplementedError

    def deposit(self, amount: int) -> None:
        raise NotImplementedError

    def withdraw(self, amount: int) -> None:
        raise NotImplementedError

    def transfer_to(self, other: "BankAccount", amount: int) -> None:
        raise NotImplementedError

import pytest

from bank_account import BankAccount, InsufficientFunds


def test_opening_balance_and_empty_history():
    account = BankAccount("Ada", 100)
    assert account.balance == 100
    assert account.history == ()


def test_default_opening_balance_is_zero():
    assert BankAccount("Ada").balance == 0


@pytest.mark.parametrize("owner,opening", [("", 0), ("   ", 0), ("Ada", -1)])
def test_invalid_construction(owner, opening):
    with pytest.raises(ValueError):
        BankAccount(owner, opening)


def test_deposit_and_withdraw_update_balance_and_history():
    account = BankAccount("Ada", 100)
    account.deposit(50)
    account.withdraw(30)
    assert account.balance == 120
    assert account.history == (("deposit", 50), ("withdraw", 30))


def test_balance_cannot_be_assigned():
    account = BankAccount("Ada", 10)
    with pytest.raises(AttributeError):
        account.balance = 1_000_000


@pytest.mark.parametrize("amount", [0, -5])
def test_non_positive_amounts_are_rejected(amount):
    account = BankAccount("Ada", 10)
    with pytest.raises(ValueError):
        account.deposit(amount)
    with pytest.raises(ValueError):
        account.withdraw(amount)
    assert account.balance == 10
    assert account.history == ()


def test_overdraw_raises_and_changes_nothing():
    account = BankAccount("Ada", 20)
    with pytest.raises(InsufficientFunds):
        account.withdraw(21)
    assert account.balance == 20
    assert account.history == ()


def test_withdrawing_the_whole_balance_is_allowed():
    account = BankAccount("Ada", 20)
    account.withdraw(20)
    assert account.balance == 0


def test_history_is_an_immutable_snapshot():
    account = BankAccount("Ada", 0)
    account.deposit(5)
    snapshot = account.history
    assert isinstance(snapshot, tuple)
    account.deposit(7)
    assert snapshot == (("deposit", 5),)
    assert account.history == (("deposit", 5), ("deposit", 7))


def test_transfer_moves_money_and_records_both_sides():
    a, b = BankAccount("A", 100), BankAccount("B", 5)
    a.transfer_to(b, 40)
    assert (a.balance, b.balance) == (60, 45)
    assert a.history == (("transfer out", 40),)
    assert b.history == (("transfer in", 40),)


def test_failed_transfer_changes_neither_account():
    a, b = BankAccount("A", 10), BankAccount("B", 5)
    with pytest.raises(InsufficientFunds):
        a.transfer_to(b, 11)
    with pytest.raises(ValueError):
        a.transfer_to(b, 0)
    assert (a.balance, b.balance) == (10, 5)
    assert a.history == () and b.history == ()

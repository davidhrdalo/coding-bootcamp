"""Open/closed: discount rules

New discounts should be added by writing a NEW class, without editing price(). That is the
"open for extension, closed for modification" idea (the O in SOLID).

A cart is a list of items: {"name": "tea", "price": 300, "qty": 2}   (price in CENTS)
A RULE is any object with:   discount(items, current_total) -> int cents off

  price(items, rules) -> final total in cents
    - start from the subtotal: sum of price * qty
    - apply the rules IN ORDER: each rule sees the total so far (after earlier discounts)
      and returns how much to take off
    - the total never goes below 0

Build these rules:
  PercentOff(percent)           takes percent% off the CURRENT total, rounded DOWN
                                (current_total * percent // 100)
  MinimumSpend(minimum, off)    takes `off` cents off if the CURRENT total is at least
                                `minimum` cents, else 0
  BuyGetOneFree(name, buy)      for the item with this name, every (buy + 1)th unit is free:
                                free units = qty // (buy + 1), discount = free units * price.
                                0 if the item is not in the cart

Concepts: open/closed principle, polymorphism over rules, strategy pattern.
"""


class PercentOff:
    def __init__(self, percent: int) -> None:
        raise NotImplementedError

    def discount(self, items: list, current_total: int) -> int:
        raise NotImplementedError


class MinimumSpend:
    def __init__(self, minimum: int, off: int) -> None:
        raise NotImplementedError

    def discount(self, items: list, current_total: int) -> int:
        raise NotImplementedError


class BuyGetOneFree:
    def __init__(self, name: str, buy: int) -> None:
        raise NotImplementedError

    def discount(self, items: list, current_total: int) -> int:
        raise NotImplementedError


def price(items: list, rules: list) -> int:
    raise NotImplementedError

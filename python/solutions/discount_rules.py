class PercentOff:
    def __init__(self, percent: int) -> None:
        self.percent = percent

    def discount(self, items: list, current_total: int) -> int:
        return current_total * self.percent // 100


class MinimumSpend:
    def __init__(self, minimum: int, off: int) -> None:
        self.minimum = minimum
        self.off = off

    def discount(self, items: list, current_total: int) -> int:
        return self.off if current_total >= self.minimum else 0


class BuyGetOneFree:
    def __init__(self, name: str, buy: int) -> None:
        self.name = name
        self.buy = buy

    def discount(self, items: list, current_total: int) -> int:
        total = 0
        for item in items:
            if item["name"] == self.name:
                total += (item["qty"] // (self.buy + 1)) * item["price"]
        return total


def price(items: list, rules: list) -> int:
    total = sum(item["price"] * item["qty"] for item in items)
    for rule in rules:
        total -= rule.discount(items, total)
        total = max(total, 0)
    return total

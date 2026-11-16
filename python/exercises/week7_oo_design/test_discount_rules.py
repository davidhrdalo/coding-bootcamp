from discount_rules import BuyGetOneFree, MinimumSpend, PercentOff, price

CART = [
    {"name": "tea", "price": 300, "qty": 3},
    {"name": "cake", "price": 450, "qty": 2},
]  # subtotal 900 + 900 = 1800


def test_no_rules_is_the_subtotal():
    assert price(CART, []) == 1800
    assert price([], []) == 0


def test_percent_off():
    assert price(CART, [PercentOff(10)]) == 1620


def test_percent_off_rounds_the_discount_down():
    assert price([{"name": "x", "price": 99, "qty": 1}], [PercentOff(10)]) == 90  # 99 - 9


def test_minimum_spend_applies_only_when_reached():
    assert price(CART, [MinimumSpend(1500, 200)]) == 1600
    assert price(CART, [MinimumSpend(1801, 200)]) == 1800
    assert price(CART, [MinimumSpend(1800, 200)]) == 1600


def test_buy_get_one_free():
    # buy 2 get 1 free: 3 teas -> 1 free
    assert price(CART, [BuyGetOneFree("tea", 2)]) == 1500
    # buy 1 get 1 free: 2 cakes -> 1 free
    assert price(CART, [BuyGetOneFree("cake", 1)]) == 1350
    # not in the cart
    assert price(CART, [BuyGetOneFree("coffee", 1)]) == 1800


def test_rules_apply_in_order_and_see_the_running_total():
    # 1800 -> buy2get1 on tea (-300) = 1500 -> 10% off (-150) = 1350
    assert price(CART, [BuyGetOneFree("tea", 2), PercentOff(10)]) == 1350
    # 1800 -> 10% (-180) = 1620 -> MinimumSpend(1700) no longer applies
    assert price(CART, [PercentOff(10), MinimumSpend(1700, 500)]) == 1620
    # other way round, the minimum is met first: 1800 -> -500 = 1300 -> 10% (-130) = 1170
    assert price(CART, [MinimumSpend(1700, 500), PercentOff(10)]) == 1170


def test_total_never_goes_below_zero():
    assert price([{"name": "x", "price": 100, "qty": 1}], [MinimumSpend(0, 500)]) == 0


def test_a_brand_new_rule_works_without_changing_price():
    class FlatOff:
        def __init__(self, cents):
            self.cents = cents

        def discount(self, items, current_total):
            return self.cents

    class FreeShippingOver:
        def discount(self, items, current_total):
            return 0

    assert price(CART, [FlatOff(100), FreeShippingOver()]) == 1700


def test_items_are_not_modified():
    items = [{"name": "tea", "price": 300, "qty": 3}]
    price(items, [BuyGetOneFree("tea", 2), PercentOff(50)])
    assert items == [{"name": "tea", "price": 300, "qty": 3}]

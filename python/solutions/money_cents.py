def to_cents(amount: str) -> int:
    whole, _, fraction = amount.partition(".")
    if not whole.isdigit() or (fraction and not fraction.isdigit()) or len(fraction) > 2:
        raise ValueError(f"invalid amount: {amount!r}")
    fraction = (fraction + "00")[:2]
    return int(whole) * 100 + int(fraction)


def format_cents(cents: int) -> str:
    return f"${cents // 100}.{cents % 100:02d}"

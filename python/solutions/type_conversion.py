def parse_int(text, default: int = 0) -> int:
    try:
        return int(text)
    except (ValueError, TypeError):
        return default


def to_bool(text: str) -> bool:
    value = text.strip().lower()
    if value in ("true", "yes", "1", "on"):
        return True
    if value in ("false", "no", "0", "off"):
        return False
    raise ValueError(f"not a boolean: {text!r}")

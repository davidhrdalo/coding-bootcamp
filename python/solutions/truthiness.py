def first_truthy(*values):
    for value in values:
        if value:
            return value
    return None


def falsy_kind(value) -> str:
    if value is None:
        return "none"
    if value is False:
        return "false"
    if isinstance(value, (int, float)) and not isinstance(value, bool) and value == 0:
        return "zero"
    if not value:
        return "empty"
    return "truthy"

def _segments(path: str) -> list:
    stripped = path.strip("/")
    return stripped.split("/") if stripped else []


def match_route(pattern: str, path: str) -> dict | None:
    wanted, actual = _segments(pattern), _segments(path)
    if len(wanted) != len(actual):
        return None
    params = {}
    for want, got in zip(wanted, actual):
        if want.startswith("{") and want.endswith("}"):
            if not got:
                return None
            params[want[1:-1]] = got
        elif want != got:
            return None
    return params

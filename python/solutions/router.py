from route_matching import match_route


class Router:
    def __init__(self) -> None:
        self._routes = []

    def add(self, method: str, pattern: str, handler) -> None:
        self._routes.append((method.upper(), pattern, handler))

    def dispatch(self, request: dict) -> dict:
        method = request["method"].upper()
        allowed = set()
        for route_method, pattern, handler in self._routes:
            params = match_route(pattern, request["path"])
            if params is None:
                continue
            if route_method == method:
                return handler(request, params)
            allowed.add(route_method)
        if allowed:
            return {
                "status": 405,
                "json": {"error": "method not allowed"},
                "headers": {"Allow": ", ".join(sorted(allowed))},
            }
        return {"status": 404, "json": {"error": "not found"}, "headers": {}}

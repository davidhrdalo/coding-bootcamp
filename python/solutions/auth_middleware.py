def require_auth(handler, tokens: dict, role: str | None = None):
    def wrapped(request: dict) -> dict:
        header = request.get("headers", {}).get("authorization", "")
        scheme, space, token = header.partition(" ")
        if scheme.lower() != "bearer" or not space or token not in tokens:
            return {
                "status": 401,
                "json": {"error": "unauthorized"},
                "headers": {"WWW-Authenticate": "Bearer"},
            }
        if role is not None and tokens[token] != role:
            return {"status": 403, "json": {"error": "forbidden"}, "headers": {}}
        return handler({**request, "role": tokens[token]})

    return wrapped

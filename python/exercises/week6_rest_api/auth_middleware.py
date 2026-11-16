"""Auth middleware: 401 vs 403

Middleware wraps a handler and runs checks before it. Build the check that sits in front
of protected endpoints.

In this week a REQUEST is a dict and a RESPONSE is a dict, so there are no sockets to set up:

  request  = {"method": "GET", "path": "/todos/1", "headers": {}, "query": {}, "json": None}
  response = {"status": 200, "json": {...}, "headers": {}}

Header names in requests are lowercase ("authorization"). Frameworks like Flask, FastAPI and
Express do the same job: turn a request into a response by matching a route.

  require_auth(handler, tokens, role=None) -> a new handler(request) -> response

  tokens is a dict of valid bearer tokens to their role: {"abc": "user", "xyz": "admin"}.

The wrapped handler:
- Reads the "authorization" header. It must look like "Bearer <token>" (the word Bearer is
  case-insensitive; exactly one space).
- Missing header, wrong scheme, or a token that is not in `tokens`:
    401  {"status": 401, "json": {"error": "unauthorized"},
          "headers": {"WWW-Authenticate": "Bearer"}}
- A known token whose role is not the required `role` (when role is not None):
    403  {"status": 403, "json": {"error": "forbidden"}, "headers": {}}
- Otherwise call handler with a COPY of the request that has an extra key "role" holding
  the token's role, and return its response. Never call the handler on a 401 or 403.

Concepts: authentication (who are you? 401) vs authorisation (are you allowed? 403),
bearer tokens, middleware as function wrapping, not mutating the caller's request.
"""


def require_auth(handler, tokens: dict, role: str | None = None):
    raise NotImplementedError

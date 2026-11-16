"""A tiny router

Build the class that sits at the centre of every web framework. It uses your match_route
from the previous exercise, so finish that one first.

In this week a REQUEST is a dict and a RESPONSE is a dict, so there are no sockets to set up:

  request  = {"method": "GET", "path": "/todos/1", "headers": {}, "query": {}, "json": None}
  response = {"status": 200, "json": {...}, "headers": {}}

Header names in requests are lowercase ("authorization"). Frameworks like Flask, FastAPI and
Express do the same job: turn a request into a response by matching a route.

  router = Router()
  router.add("GET", "/todos/{id}", handler)       # handler(request, params) -> response
  router.dispatch(request)                        # finds the handler and calls it

dispatch rules:
- Routes are tried in the order they were added. The first route whose path matches AND whose
  method matches wins. Call handler(request, params) and return its response unchanged.
- If NO route matches the path: return
    {"status": 404, "json": {"error": "not found"}, "headers": {}}
- If some route matches the path but none has the right method: return
    {"status": 405, "json": {"error": "method not allowed"},
     "headers": {"Allow": "GET, POST"}}
  where Allow lists the methods that DO exist for that path, uppercase, sorted, without
  duplicates, joined with ", ".

Concepts: routing, 404 vs 405, the Allow header, first match wins (register specific
routes before general ones).
"""

from route_matching import match_route  # noqa: F401  (you will use this)


class Router:
    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, method: str, pattern: str, handler) -> None:
        raise NotImplementedError

    def dispatch(self, request: dict) -> dict:
        raise NotImplementedError

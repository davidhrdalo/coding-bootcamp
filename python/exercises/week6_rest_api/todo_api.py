"""A to-do API (CRUD)

Build a small REST API on top of your Router. Finish route_matching and router first.

In this week a REQUEST is a dict and a RESPONSE is a dict, so there are no sockets to set up:

  request  = {"method": "GET", "path": "/todos/1", "headers": {}, "query": {}, "json": None}
  response = {"status": 200, "json": {...}, "headers": {}}

Header names in requests are lowercase ("authorization"). Frameworks like Flask, FastAPI and
Express do the same job: turn a request into a response by matching a route.

make_todo_app() returns a function handle(request) -> response that keeps its to-dos in
memory (each app starts empty). A to-do is {"id": 1, "title": "...", "done": False}. Ids are
integers starting at 1 and are never reused.

Endpoints and status codes:
  POST   /todos        body {"title": "Buy milk"}
                       201 with the new to-do and header "Location": "/todos/<id>"
                       400 {"error": "..."} if the body is not an object, or title is
                       missing, not a string, or blank (spaces only)
  GET    /todos        200 with a list ordered by id. Optional filter ?done=true or
                       ?done=false (query values are strings). Any other value: 400.
  GET    /todos/{id}   200 with the to-do. 404 {"error": "not found"} if there is no such
                       to-do, or the id is not made of digits.
  PATCH  /todos/{id}   partial update of "title" (non-blank string) and/or "done" (a real
                       bool). 200 with the updated to-do. 400 for an unknown field, a wrong
                       type, or a non-object body. 404 if missing.
  DELETE /todos/{id}   204 with "json": None. 404 if missing.
Anything else follows the router: 404 for unknown paths, 405 for wrong methods.

Concepts: REST resources, status codes (200, 201, 204, 400, 404), validation, idempotent
DELETE vs POST, partial updates (PATCH).
"""

from router import Router  # noqa: F401  (you will use this)


def make_todo_app():
    raise NotImplementedError

"""Match a URL path against a route pattern

  match_route("/todos/{id}", "/todos/42")        -> {"id": "42"}
  match_route("/users/{uid}/posts/{pid}", "/users/7/posts/9") -> {"uid": "7", "pid": "9"}
  match_route("/health", "/health")              -> {}       (matches, no parameters)
  match_route("/todos/{id}", "/users/42")        -> None     (does not match)

Rules:
- Split both on "/". Ignore ONE leading and trailing slash, so "/todos/" matches "/todos".
- A segment written "{name}" captures the matching segment of the path. The captured
  segment must not be empty, so "/a//b" does not match "/a/{x}/{y}", and "/todos/" does not
  match "/todos/{id}".
- Other segments must be equal (case-sensitive).
- Different numbers of segments never match.
- Return the dict of captured strings (an empty dict for a static match) or None.

Concepts: how routers work in every web framework, parsing by segments, not regexes.
"""


def match_route(pattern: str, path: str) -> dict | None:
    raise NotImplementedError

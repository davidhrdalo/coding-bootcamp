from router import Router


def _error(status, message):
    return {"status": status, "json": {"error": message}, "headers": {}}


def _clean_title(value):
    return isinstance(value, str) and value.strip() != ""


def make_todo_app():
    todos = {}
    next_id = [1]
    router = Router()

    def find(params):
        text = params["id"]
        if not text.isascii() or not text.isdigit():
            return None
        return todos.get(int(text))

    def create(request, _params):
        body = request["json"]
        if not isinstance(body, dict) or not _clean_title(body.get("title")):
            return _error(400, "title is required")
        todo = {"id": next_id[0], "title": body["title"], "done": False}
        todos[todo["id"]] = todo
        next_id[0] += 1
        return {"status": 201, "json": dict(todo), "headers": {"Location": f"/todos/{todo['id']}"}}

    def list_all(request, _params):
        wanted = request["query"].get("done")
        items = [dict(t) for t in sorted(todos.values(), key=lambda t: t["id"])]
        if wanted is not None:
            if wanted not in ("true", "false"):
                return _error(400, "done must be true or false")
            items = [t for t in items if t["done"] == (wanted == "true")]
        return {"status": 200, "json": items, "headers": {}}

    def get_one(_request, params):
        todo = find(params)
        if todo is None:
            return _error(404, "not found")
        return {"status": 200, "json": dict(todo), "headers": {}}

    def patch(request, params):
        todo = find(params)
        if todo is None:
            return _error(404, "not found")
        body = request["json"]
        if not isinstance(body, dict):
            return _error(400, "body must be an object")
        updates = {}
        for key, value in body.items():
            if key == "title" and _clean_title(value):
                updates["title"] = value
            elif key == "done" and isinstance(value, bool):
                updates["done"] = value
            else:
                return _error(400, f"bad field: {key}")
        todo.update(updates)
        return {"status": 200, "json": dict(todo), "headers": {}}

    def delete(_request, params):
        todo = find(params)
        if todo is None:
            return _error(404, "not found")
        del todos[todo["id"]]
        return {"status": 204, "json": None, "headers": {}}

    router.add("POST", "/todos", create)
    router.add("GET", "/todos", list_all)
    router.add("GET", "/todos/{id}", get_one)
    router.add("PATCH", "/todos/{id}", patch)
    router.add("DELETE", "/todos/{id}", delete)
    return router.dispatch

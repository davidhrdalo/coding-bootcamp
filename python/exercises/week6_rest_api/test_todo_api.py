import pytest

from todo_api import make_todo_app


def call(app, method, path, json=None, query=None):
    return app({"method": method, "path": path, "headers": {}, "query": query or {}, "json": json})


@pytest.fixture
def app():
    return make_todo_app()


def test_starts_empty(app):
    got = call(app, "GET", "/todos")
    assert got["status"] == 200
    assert got["json"] == []


def test_create_returns_201_location_and_the_todo(app):
    got = call(app, "POST", "/todos", {"title": "Buy milk"})
    assert got["status"] == 201
    assert got["json"] == {"id": 1, "title": "Buy milk", "done": False}
    assert got["headers"]["Location"] == "/todos/1"


def test_ids_increase(app):
    call(app, "POST", "/todos", {"title": "a"})
    got = call(app, "POST", "/todos", {"title": "b"})
    assert got["json"]["id"] == 2


@pytest.mark.parametrize("body", [None, [], "text", {}, {"title": ""}, {"title": "   "}, {"title": 5}])
def test_create_validation_errors(app, body):
    got = call(app, "POST", "/todos", body)
    assert got["status"] == 400
    assert "error" in got["json"]


def test_list_is_ordered_and_filterable(app):
    for title in ["a", "b", "c"]:
        call(app, "POST", "/todos", {"title": title})
    call(app, "PATCH", "/todos/2", {"done": True})
    assert [t["id"] for t in call(app, "GET", "/todos")["json"]] == [1, 2, 3]
    assert [t["id"] for t in call(app, "GET", "/todos", query={"done": "true"})["json"]] == [2]
    assert [t["id"] for t in call(app, "GET", "/todos", query={"done": "false"})["json"]] == [1, 3]


def test_bad_done_filter_is_400(app):
    assert call(app, "GET", "/todos", query={"done": "maybe"})["status"] == 400


def test_get_one(app):
    call(app, "POST", "/todos", {"title": "a"})
    assert call(app, "GET", "/todos/1")["json"]["title"] == "a"


@pytest.mark.parametrize("path", ["/todos/99", "/todos/abc", "/todos/1.5", "/todos/-1"])
def test_get_missing_or_non_numeric_id_is_404(app, path):
    assert call(app, "GET", path) == {"status": 404, "json": {"error": "not found"}, "headers": {}}


def test_patch_updates_only_given_fields(app):
    call(app, "POST", "/todos", {"title": "a"})
    got = call(app, "PATCH", "/todos/1", {"done": True})
    assert got["status"] == 200
    assert got["json"] == {"id": 1, "title": "a", "done": True}
    got = call(app, "PATCH", "/todos/1", {"title": "renamed"})
    assert got["json"] == {"id": 1, "title": "renamed", "done": True}


@pytest.mark.parametrize(
    "body",
    [{"colour": "red"}, {"done": "yes"}, {"done": 1}, {"title": ""}, {"title": 3}, [], None],
)
def test_patch_validation_errors(app, body):
    call(app, "POST", "/todos", {"title": "a"})
    assert call(app, "PATCH", "/todos/1", body)["status"] == 400


def test_patch_missing_is_404(app):
    assert call(app, "PATCH", "/todos/5", {"done": True})["status"] == 404


def test_delete_then_gone(app):
    call(app, "POST", "/todos", {"title": "a"})
    got = call(app, "DELETE", "/todos/1")
    assert got["status"] == 204
    assert got["json"] is None
    assert call(app, "GET", "/todos/1")["status"] == 404
    assert call(app, "DELETE", "/todos/1")["status"] == 404


def test_ids_are_never_reused_after_delete(app):
    call(app, "POST", "/todos", {"title": "a"})
    call(app, "DELETE", "/todos/1")
    assert call(app, "POST", "/todos", {"title": "b"})["json"]["id"] == 2


def test_unknown_path_and_wrong_method(app):
    assert call(app, "GET", "/nope")["status"] == 404
    got = call(app, "PUT", "/todos")
    assert got["status"] == 405
    assert got["headers"]["Allow"] == "GET, POST"


def test_each_app_has_its_own_data():
    one, two = make_todo_app(), make_todo_app()
    call(one, "POST", "/todos", {"title": "only in one"})
    assert call(two, "GET", "/todos")["json"] == []

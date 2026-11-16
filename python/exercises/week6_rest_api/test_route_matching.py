import pytest

from route_matching import match_route


def test_static_route_matches_with_empty_params():
    assert match_route("/health", "/health") == {}


def test_single_parameter():
    assert match_route("/todos/{id}", "/todos/42") == {"id": "42"}


def test_multiple_parameters():
    assert match_route("/users/{uid}/posts/{pid}", "/users/7/posts/9") == {"uid": "7", "pid": "9"}


def test_trailing_slash_is_ignored():
    assert match_route("/todos", "/todos/") == {}
    assert match_route("/todos/{id}", "/todos/1/") == {"id": "1"}


def test_root_path():
    assert match_route("/", "/") == {}


@pytest.mark.parametrize(
    "pattern,path",
    [
        ("/todos/{id}", "/users/42"),
        ("/todos/{id}", "/todos"),
        ("/todos", "/todos/1"),
        ("/todos/{id}", "/todos/1/extra"),
        ("/Todos", "/todos"),
        ("/todos/{id}", "/todos/"),
        ("/a/{x}/{y}", "/a//b"),
    ],
)
def test_non_matches(pattern, path):
    assert match_route(pattern, path) is None


def test_parameter_values_are_not_decoded_or_converted():
    assert match_route("/n/{v}", "/n/007") == {"v": "007"}

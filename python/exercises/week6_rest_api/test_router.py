from router import Router


def request(method, path, **extra):
    return {"method": method, "path": path, "headers": {}, "query": {}, "json": None, **extra}


def ok(body):
    return {"status": 200, "json": body, "headers": {}}


def test_calls_handler_with_request_and_params():
    seen = {}

    def handler(req, params):
        seen["req"], seen["params"] = req, params
        return ok("hello")

    router = Router()
    router.add("GET", "/todos/{id}", handler)
    req = request("GET", "/todos/5")
    assert router.dispatch(req) == ok("hello")
    assert seen["req"] is req
    assert seen["params"] == {"id": "5"}


def test_unknown_path_is_404():
    router = Router()
    router.add("GET", "/a", lambda r, p: ok(1))
    assert router.dispatch(request("GET", "/b")) == {
        "status": 404,
        "json": {"error": "not found"},
        "headers": {},
    }


def test_wrong_method_is_405_with_sorted_allow_header():
    router = Router()
    router.add("POST", "/todos", lambda r, p: ok("create"))
    router.add("GET", "/todos", lambda r, p: ok("list"))
    got = router.dispatch(request("DELETE", "/todos"))
    assert got == {"status": 405, "json": {"error": "method not allowed"}, "headers": {"Allow": "GET, POST"}}


def test_allow_header_has_no_duplicates_and_is_uppercase():
    router = Router()
    router.add("get", "/x", lambda r, p: ok(1))
    router.add("GET", "/x", lambda r, p: ok(2))
    assert router.dispatch(request("PUT", "/x"))["headers"] == {"Allow": "GET"}


def test_same_path_different_methods_dispatch_correctly():
    router = Router()
    router.add("GET", "/todos", lambda r, p: ok("list"))
    router.add("POST", "/todos", lambda r, p: ok("create"))
    assert router.dispatch(request("POST", "/todos"))["json"] == "create"
    assert router.dispatch(request("GET", "/todos"))["json"] == "list"


def test_first_registered_match_wins():
    router = Router()
    router.add("GET", "/todos/new", lambda r, p: ok("static"))
    router.add("GET", "/todos/{id}", lambda r, p: ok("param"))
    assert router.dispatch(request("GET", "/todos/new"))["json"] == "static"
    assert router.dispatch(request("GET", "/todos/7"))["json"] == "param"


def test_a_later_method_match_is_found_after_an_earlier_path_only_match():
    router = Router()
    router.add("GET", "/x/{id}", lambda r, p: ok("get"))
    router.add("POST", "/x/{id}", lambda r, p: ok("post"))
    assert router.dispatch(request("POST", "/x/1"))["json"] == "post"


def test_method_matching_is_case_insensitive():
    router = Router()
    router.add("get", "/x", lambda r, p: ok("yes"))
    assert router.dispatch(request("GET", "/x"))["json"] == "yes"

import pytest

from pagination import paginate

DATA = list(range(1, 26))  # 25 items


def link(page, per_page=10, base="/items"):
    return f"{base}?page={page}&per_page={per_page}"


def test_first_page():
    got = paginate(DATA, 1, 10)
    assert got == {
        "items": list(range(1, 11)),
        "page": 1,
        "per_page": 10,
        "total": 25,
        "total_pages": 3,
        "next": link(2),
        "prev": None,
    }


def test_middle_page():
    got = paginate(DATA, 2, 10)
    assert got["items"] == list(range(11, 21))
    assert got["next"] == link(3)
    assert got["prev"] == link(1)


def test_last_partial_page():
    got = paginate(DATA, 3, 10)
    assert got["items"] == [21, 22, 23, 24, 25]
    assert got["next"] is None
    assert got["prev"] == link(2)


def test_exact_multiple_has_no_extra_page():
    got = paginate(list(range(20)), 2, 10)
    assert got["total_pages"] == 2
    assert got["next"] is None


def test_page_beyond_the_end_points_back_to_the_last_page():
    got = paginate(DATA, 9, 10)
    assert got["items"] == []
    assert got["next"] is None
    assert got["prev"] == link(3)


def test_empty_list_has_one_page():
    got = paginate([], 1, 10)
    assert got["items"] == []
    assert got["total"] == 0
    assert got["total_pages"] == 1
    assert got["next"] is None
    assert got["prev"] is None


def test_defaults_and_custom_base_path():
    got = paginate(DATA, base_path="/users")
    assert got["page"] == 1
    assert got["per_page"] == 10
    assert got["next"] == "/users?page=2&per_page=10"


def test_per_page_is_part_of_the_links():
    got = paginate(DATA, 1, 5)
    assert got["total_pages"] == 5
    assert got["next"] == link(2, 5)


@pytest.mark.parametrize("page,per_page", [(0, 10), (-1, 10), (1, 0), (1, 101), (1, -5)])
def test_invalid_arguments_raise(page, per_page):
    with pytest.raises(ValueError):
        paginate(DATA, page, per_page)


def test_input_is_not_modified():
    data = [1, 2, 3, 4, 5]
    paginate(data, 1, 2)
    assert data == [1, 2, 3, 4, 5]

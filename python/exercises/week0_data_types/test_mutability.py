from mutability import add_tag, copy_matrix


def test_add_tag_without_existing_list():
    assert add_tag("a") == ["a"]


def test_default_is_not_shared_between_calls():
    first = add_tag("a")
    second = add_tag("b")
    assert second == ["b"]
    assert first == ["a"]
    assert first is not second


def test_add_tag_does_not_modify_the_input():
    tags = ["x"]
    result = add_tag("y", tags)
    assert result == ["x", "y"]
    assert tags == ["x"]
    assert result is not tags


def test_copy_matrix_has_equal_values():
    m = [[1, 2], [3, 4]]
    assert copy_matrix(m) == [[1, 2], [3, 4]]


def test_copy_matrix_is_independent_of_the_original():
    m = [[1, 2], [3, 4]]
    c = copy_matrix(m)
    c[0][0] = 99
    c.append([5, 6])
    assert m == [[1, 2], [3, 4]]


def test_copy_matrix_edge_cases():
    assert copy_matrix([]) == []
    assert copy_matrix([[], [1]]) == [[], [1]]

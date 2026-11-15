def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    return (list(tags) if tags is not None else []) + [tag]


def copy_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in matrix]

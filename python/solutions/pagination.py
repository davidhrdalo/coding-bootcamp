def paginate(items: list, page: int = 1, per_page: int = 10, base_path: str = "/items") -> dict:
    if page < 1 or per_page < 1 or per_page > 100:
        raise ValueError("bad page or per_page")
    total = len(items)
    total_pages = max(1, -(-total // per_page))
    start = (page - 1) * per_page

    def link(n: int) -> str:
        return f"{base_path}?page={n}&per_page={per_page}"

    if page > total_pages:
        prev = link(total_pages)
    else:
        prev = link(page - 1) if page > 1 else None
    return {
        "items": list(items[start : start + per_page]),
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages,
        "next": link(page + 1) if page < total_pages else None,
        "prev": prev,
    }

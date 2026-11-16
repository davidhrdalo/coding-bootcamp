"""Paginate a list

APIs never return a million rows at once. Build the page response.

  paginate(items, page=1, per_page=10, base_path="/items") -> {
      "items": [...],          # this page's slice
      "page": 2,
      "per_page": 10,
      "total": 25,             # total items overall
      "total_pages": 3,
      "next": "/items?page=3&per_page=10",   # None on the last page
      "prev": "/items?page=1&per_page=10",   # None on the first page
  }

Rules:
- Pages count from 1. Raise ValueError if page < 1, or per_page is not between 1 and 100.
- total_pages is the number of pages needed (round up). An empty list still has 1 page.
- A page BEYOND the last returns no items and next=None, and prev points at the LAST page
  (not at page-1), so clients can recover.
- Do not change the input list.

Concepts: offset pagination, off-by-one errors, ceiling division, HATEOAS-style links.
"""


def paginate(items: list, page: int = 1, per_page: int = 10, base_path: str = "/items") -> dict:
    raise NotImplementedError

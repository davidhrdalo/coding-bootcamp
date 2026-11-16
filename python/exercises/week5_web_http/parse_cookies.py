"""Cookies: read and write

Browsers send cookies back in one header:   Cookie: a=1; b=two
Servers set them with a header:             Set-Cookie: a=1; Path=/; HttpOnly

1) parse_cookie_header(header) -> dict
   - Parts are separated by ";" and surrounding spaces are ignored.
   - Split each part on its FIRST "=" (a value may contain "="). Ignore parts without "=".
   - If a name appears twice, the FIRST one wins (browsers send the most specific first).

2) build_set_cookie(name, value, *, max_age=None, http_only=False, secure=False,
                    path="/", same_site="Lax") -> str
   Output order: "name=value", "Path=<path>", "Max-Age=<n>" (only if given),
   "HttpOnly" (only if True), "Secure" (only if True), "SameSite=<same_site>", all
   joined with "; ".
   - Raise ValueError if name or value contains ";" or a space.
   - same_site must be "Strict", "Lax" or "None", else ValueError.
   - SameSite=None only works with Secure, so raise ValueError for None without secure.

Concepts: how sessions work over stateless HTTP, HttpOnly and Secure, SameSite and CSRF.
"""


def parse_cookie_header(header: str) -> dict:
    raise NotImplementedError


def build_set_cookie(
    name: str,
    value: str,
    *,
    max_age: int | None = None,
    http_only: bool = False,
    secure: bool = False,
    path: str = "/",
    same_site: str = "Lax",
) -> str:
    raise NotImplementedError

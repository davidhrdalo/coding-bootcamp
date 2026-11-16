def parse_cookie_header(header: str) -> dict:
    cookies: dict = {}
    for part in header.split(";"):
        if "=" not in part:
            continue
        name, _, value = part.partition("=")
        name = name.strip()
        if name and name not in cookies:
            cookies[name] = value.strip()
    return cookies


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
    for text in (name, value):
        if ";" in text or " " in text:
            raise ValueError("cookie name and value cannot contain ';' or spaces")
    if same_site not in ("Strict", "Lax", "None"):
        raise ValueError("bad SameSite")
    if same_site == "None" and not secure:
        raise ValueError("SameSite=None requires Secure")
    parts = [f"{name}={value}", f"Path={path}"]
    if max_age is not None:
        parts.append(f"Max-Age={max_age}")
    if http_only:
        parts.append("HttpOnly")
    if secure:
        parts.append("Secure")
    parts.append(f"SameSite={same_site}")
    return "; ".join(parts)

def split_url(url: str) -> dict:
    scheme, sep, rest = url.partition("://")
    if not sep or not scheme:
        raise ValueError("missing scheme")
    rest, _, fragment = rest.partition("#")
    rest, _, query = rest.partition("?")
    authority, slash, path = rest.partition("/")
    path = "/" + path if slash else "/"
    host, colon, port_text = authority.partition(":")
    if not host:
        raise ValueError("missing host")
    port = int(port_text) if colon and port_text else None
    return {
        "scheme": scheme.lower(),
        "host": host.lower(),
        "port": port,
        "path": path,
        "query": query,
        "fragment": fragment,
    }

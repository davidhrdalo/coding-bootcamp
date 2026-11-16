def parse_request(raw: str) -> dict:
    head, _sep, body = raw.partition("\r\n\r\n")
    lines = head.split("\r\n")
    parts = lines[0].split(" ")
    if len(parts) != 3:
        raise ValueError("bad request line")
    method, target, _version = parts
    path, _, query_text = target.partition("?")
    query = {}
    for piece in query_text.split("&"):
        if not piece:
            continue
        key, _, value = piece.partition("=")
        query[key] = value
    headers = {}
    for line in lines[1:]:
        if ":" in line:
            name, _, value = line.partition(":")
            headers[name.strip().lower()] = value.strip()
    return {"method": method, "path": path, "query": query, "headers": headers, "body": body}

REASONS = {
    200: "OK",
    201: "Created",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    409: "Conflict",
    429: "Too Many Requests",
    500: "Internal Server Error",
    503: "Service Unavailable",
}


def build_response(status: int, body: str = "", headers: dict | None = None) -> str:
    headers = dict(headers or {})
    lines = [f"HTTP/1.1 {status} {REASONS.get(status, 'Unknown')}"]
    if status == 204:
        if body:
            raise ValueError("204 responses cannot have a body")
        lines += [f"{name}: {value}" for name, value in headers.items()]
        return "\r\n".join(lines) + "\r\n\r\n"
    content_type = headers.pop("Content-Type", "text/plain; charset=utf-8")
    lines.append(f"Content-Type: {content_type}")
    lines.append(f"Content-Length: {len(body.encode('utf-8'))}")
    lines += [f"{name}: {value}" for name, value in headers.items()]
    return "\r\n".join(lines) + "\r\n\r\n" + body

"""Build an HTTP response

Servers answer with text too. Build the raw response string.

  build_response(status, body="", headers=None) -> str

Rules:
- First line: "HTTP/1.1 <status> <reason>", for example "HTTP/1.1 404 Not Found".
  Use the REASONS table below; an unknown status gets the reason "Unknown".
- Then the headers, one per line, in this order:
    1. Content-Type: the value in headers if the caller gave one, otherwise
       "text/plain; charset=utf-8"
    2. Content-Length: the length of the body in BYTES (not characters: "é" is 2 bytes
       in UTF-8)
    3. every other header the caller gave, in the order given
- A blank line, then the body.
- Lines end with CRLF (carriage return then line feed).
- Status 204 means "No Content": raise ValueError if a body is given, and send neither
  Content-Type nor Content-Length (only the caller's own headers, if any).

Concepts: status codes, headers, why Content-Length counts bytes, the blank line.
"""

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
    raise NotImplementedError

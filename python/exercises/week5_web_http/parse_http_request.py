"""Parse an HTTP request

Browsers and tools like curl send requests as plain text over a connection. Parse one
into a dict:

  parse_request(raw) -> {
      "method": "GET",
      "path": "/search",
      "query": {"q": "python"},            # simple: last value wins, not decoded
      "headers": {"host": "example.com"},  # header NAMES lowercased
      "body": "",
  }

Format. Every line ends with CRLF (carriage return then line feed):

  GET /search?q=python HTTP/1.1
  Host: example.com
  <blank line>
  optional body text

- The request line is METHOD, a space, the target, a space, the version. Split the target
  at the first "?" into path and query.
- Query: split on "&", then each part on its first "=". A key with no "=" gets the value
  "". Ignore empty parts.
- Headers look like "Name: value". Strip spaces around the value and lowercase the name.
  A value may itself contain colons (for example "Host: localhost:8080").
- Body: everything after the first blank line. It may be empty. Do not strip it.
- Raise ValueError if the request line does not have exactly three parts.

Concepts: HTTP is just text, headers, query strings, the blank line between headers and body.
"""


def parse_request(raw: str) -> dict:
    raise NotImplementedError

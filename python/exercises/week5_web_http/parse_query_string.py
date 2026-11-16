"""Parse a query string

URLs carry data after "?": /search?q=hello+world&tag=a&tag=b. Parse it into a dict whose
values are LISTS (a key can repeat):

  parse_query("q=hello+world&tag=a&tag=b") -> {"q": ["hello world"], "tag": ["a", "b"]}

Rules:
- A leading "?" is allowed and ignored. An empty string gives {}.
- Split on "&", then each part on its first "=". A key with no "=" gets the value "".
  Ignore empty parts.
- Decode both keys and values: "+" becomes a space, and "%XX" (two hex digits) is one
  byte. Bytes are UTF-8, so "%C3%A9" is "é".
- An "%" that is not followed by two hex digits stays as a literal "%".
- Decode AFTER splitting, so an encoded "&" or "=" (%26, %3D) inside a value does not
  split anything.
- Do not use urllib.parse. The point is to see how it works.

Concepts: percent-encoding, UTF-8 bytes, why decoding order matters.
"""


def parse_query(qs: str) -> dict:
    raise NotImplementedError

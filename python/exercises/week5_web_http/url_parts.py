"""Split a URL into its parts

  split_url("https://Example.com:8080/a/b?x=1&y=2#top") -> {
      "scheme": "https",          # lowercased
      "host": "example.com",      # lowercased
      "port": 8080,               # an int, or None if the URL has no port
      "path": "/a/b",             # "/" if the URL has no path
      "query": "x=1&y=2",         # without the "?", "" if none
      "fragment": "top",          # without the "#", "" if none
  }

Rules:
- The scheme ends at "://". Raise ValueError if "://" is missing or the scheme is empty.
- The fragment starts at the FIRST "#" (so "?" after a "#" belongs to the fragment).
  Then the query starts at the first "?" before it.
- The authority (host and port) runs up to the first "/". Raise ValueError if the host is
  empty or the port is not a number. You do not need to support user names or IPv6.

Concepts: the anatomy of a URL, why the fragment is never sent to the server.
"""


def split_url(url: str) -> dict:
    raise NotImplementedError

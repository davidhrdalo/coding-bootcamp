HEX = b"0123456789abcdefABCDEF"


def _decode(text: str) -> str:
    raw = text.replace("+", " ").encode("utf-8")
    out = bytearray()
    i = 0
    while i < len(raw):
        if raw[i] == 0x25 and i + 2 < len(raw) and raw[i + 1] in HEX and raw[i + 2] in HEX:
            out.append(int(raw[i + 1 : i + 3], 16))
            i += 3
        else:
            out.append(raw[i])
            i += 1
    return out.decode("utf-8", errors="replace")


def parse_query(qs: str) -> dict:
    if qs.startswith("?"):
        qs = qs[1:]
    result: dict = {}
    for piece in qs.split("&"):
        if not piece:
            continue
        key, _, value = piece.partition("=")
        result.setdefault(_decode(key), []).append(_decode(value))
    return result

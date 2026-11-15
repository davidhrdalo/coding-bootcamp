import re

_TOKEN = re.compile(r"\s*(?:(\d+\.?\d*|\.\d+)|(.))")


def tokenize(src: str) -> list[str]:
    tokens: list[str] = []
    pos = 0
    while pos < len(src):
        if src[pos].isspace():
            pos += 1
            continue
        match = _TOKEN.match(src, pos)
        number, other = match.group(1), match.group(2)
        if number is not None:
            tokens.append(number)
        elif other in "+-*/()":
            tokens.append(other)
        else:
            raise ValueError(f"unexpected character {other!r}")
        pos = match.end()
    return tokens


def evaluate(src: str) -> float:
    tokens = tokenize(src)
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else None

    def advance():
        nonlocal pos
        tok = tokens[pos]
        pos += 1
        return tok

    def expression():
        value = term()
        while peek() in ("+", "-"):
            if advance() == "+":
                value += term()
            else:
                value -= term()
        return value

    def term():
        value = factor()
        while peek() in ("*", "/"):
            if advance() == "*":
                value *= factor()
            else:
                value /= factor()
        return value

    def factor():
        tok = peek()
        if tok is None:
            raise ValueError("unexpected end of input")
        if tok == "-":
            advance()
            return -factor()
        if tok == "(":
            advance()
            value = expression()
            if peek() != ")":
                raise ValueError("missing closing parenthesis")
            advance()
            return value
        if tok in ("+", "*", "/", ")"):
            raise ValueError(f"unexpected token {tok!r}")
        advance()
        return float(tok)

    result = expression()
    if pos != len(tokens):
        raise ValueError(f"unexpected token {tokens[pos]!r}")
    return result

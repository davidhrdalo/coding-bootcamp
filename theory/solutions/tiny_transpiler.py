def tokenize(src: str) -> list[str]:
    return src.replace("(", " ( ").replace(")", " ) ").split()


def parse(tokens: list[str]) -> list:
    pos = 0

    def parse_expression():
        nonlocal pos
        token = tokens[pos]
        if token == ")":
            raise ValueError("unexpected ')'")
        if token != "(":
            pos += 1
            return token
        pos += 1  # skip "("
        items = []
        while pos < len(tokens) and tokens[pos] != ")":
            items.append(parse_expression())
        if pos >= len(tokens):
            raise ValueError("missing ')'")
        pos += 1  # skip ")"
        if not items:
            raise ValueError("empty call")
        return items

    nodes = []
    while pos < len(tokens):
        nodes.append(parse_expression())
    return nodes


def generate(node) -> str:
    if isinstance(node, str):
        return node
    name, *args = node
    return f"{name}({', '.join(generate(arg) for arg in args)})"


def transpile(src: str) -> str:
    return "\n".join(generate(node) + ";" for node in parse(tokenize(src)))

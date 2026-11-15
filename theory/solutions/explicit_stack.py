def flatten(nested: list) -> list:
    result: list = []
    stack = [iter(nested)]
    while stack:
        try:
            item = next(stack[-1])
        except StopIteration:
            stack.pop()
            continue
        if isinstance(item, list):
            stack.append(iter(item))
        else:
            result.append(item)
    return result

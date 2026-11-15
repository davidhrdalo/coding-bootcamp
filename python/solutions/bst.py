class _Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: "_Node | None" = None
        self.right: "_Node | None" = None


class BST:
    def __init__(self) -> None:
        self._root: "_Node | None" = None
        self._size = 0

    def insert(self, value: int) -> None:
        if self._root is None:
            self._root = _Node(value)
            self._size = 1
            return
        node = self._root
        while True:
            if value == node.value:
                return
            side = "left" if value < node.value else "right"
            child = getattr(node, side)
            if child is None:
                setattr(node, side, _Node(value))
                self._size += 1
                return
            node = child

    def contains(self, value: int) -> bool:
        node = self._root
        while node is not None:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def inorder(self) -> list[int]:
        result: list[int] = []
        stack: list[_Node] = []
        node = self._root
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.value)
            node = node.right
        return result

    def height(self) -> int:
        def depth(node: "_Node | None") -> int:
            if node is None:
                return 0
            return 1 + max(depth(node.left), depth(node.right))
        return depth(self._root)

    def __len__(self) -> int:
        return self._size

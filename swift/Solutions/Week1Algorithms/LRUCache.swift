final class LRUCache<Key: Hashable, Value> {
    private final class Node {
        let key: Key
        var value: Value
        weak var previous: Node?
        var next: Node?

        init(key: Key, value: Value) {
            self.key = key
            self.value = value
        }
    }

    private let capacity: Int
    private var nodes: [Key: Node] = [:]
    private var head: Node?   // most recently used
    private var tail: Node?   // least recently used

    init(capacity: Int) {
        precondition(capacity >= 1, "capacity must be at least 1")
        self.capacity = capacity
    }

    var count: Int {
        return nodes.count
    }

    func get(_ key: Key) -> Value? {
        guard let node = nodes[key] else { return nil }
        moveToFront(node)
        return node.value
    }

    func put(_ key: Key, _ value: Value) {
        if let node = nodes[key] {
            node.value = value
            moveToFront(node)
            return
        }
        let node = Node(key: key, value: value)
        nodes[key] = node
        addToFront(node)
        if nodes.count > capacity, let leastRecent = tail {
            remove(leastRecent)
            nodes[leastRecent.key] = nil
        }
    }

    private func addToFront(_ node: Node) {
        node.previous = nil
        node.next = head
        head?.previous = node
        head = node
        if tail == nil {
            tail = node
        }
    }

    private func remove(_ node: Node) {
        node.previous?.next = node.next
        node.next?.previous = node.previous
        if head === node { head = node.next }
        if tail === node { tail = node.previous }
        node.previous = nil
        node.next = nil
    }

    private func moveToFront(_ node: Node) {
        guard head !== node else { return }
        remove(node)
        addToFront(node)
    }
}

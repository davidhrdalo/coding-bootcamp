// LRU cache
//
// A cache that holds at most `capacity` entries. When it is full and a new key is added, it evicts the
// LEAST RECENTLY USED entry. Reading (get) and writing (put) both count as a use. One of the most
// common interview questions, in any language.
//
//   LRUCache<Key, Value>(capacity:)   capacity must be at least 1
//   get(_ key)                        the value, or nil if missing; marks the key most recently used
//   put(_ key, _ value)               insert or update; marks the key most recently used; evicts the
//                                     least recently used key when over capacity
//   count                             the number of entries
//
// Both get and put should be O(1). The standard design: a Dictionary from key to node, plus a DOUBLY
// linked list of nodes ordered by recency (most recent at the head, least recent at the tail). Moving
// a node to the head and removing the tail are both O(1). (A simpler version that keeps an array of
// keys works too, but is O(n).)
//
// Concepts: generics, Dictionary, doubly linked list, classes, access control (private),
// weak references (a `prev` pointer must be weak, or the list leaks).

final class LRUCache<Key: Hashable, Value> {
    init(capacity: Int) {
    }

    var count: Int {
        return 0
    }

    func get(_ key: Key) -> Value? {
        return nil
    }

    func put(_ key: Key, _ value: Value) {
    }
}

/**
 * LRU cache
 *
 * A cache that holds at most `capacity` entries. When it is full and a new key is added, it
 * evicts the LEAST RECENTLY USED entry. Both reading (get) and writing (put) count as a use.
 * This is one of the most common interview questions.
 *
 *   new LRUCache<K, V>(capacity)   throws RangeError if capacity < 1
 *   get(key)           the value, or undefined if missing; marks the key as most recently used
 *   put(key, value)    insert or update; marks the key as most recently used; evicts the
 *                      least recently used key if the cache is over capacity
 *   size               number of entries (a getter)
 *
 * Hint: a JavaScript Map remembers INSERTION order. Deleting a key and setting it again moves it
 * to the end, so the first key in the Map is always the least recently used.
 * Both get and put should be O(1).
 *
 * Concepts: Map ordering, eviction policies, caching, classes in TypeScript.
 */

export class LRUCache<K, V> {
  constructor(capacity: number) {
    throw new Error("Not implemented");
  }

  get(key: K): V | undefined {
    throw new Error("Not implemented");
  }

  put(key: K, value: V): void {
    throw new Error("Not implemented");
  }

  get size(): number {
    throw new Error("Not implemented");
  }
}

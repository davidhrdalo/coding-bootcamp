import Testing
@testable import Week1Algorithms

@Suite struct LRUCacheTests {
    @Test func storesAndRetrievesValues() {
        let cache = LRUCache<String, Int>(capacity: 2)
        cache.put("a", 1)
        cache.put("b", 2)
        #expect(cache.get("a") == 1)
        #expect(cache.get("b") == 2)
        #expect(cache.get("missing") == nil)
    }

    @Test func evictsTheLeastRecentlyUsedEntry() {
        let cache = LRUCache<Int, Int>(capacity: 2)
        cache.put(1, 1)
        cache.put(2, 2)
        #expect(cache.get(1) == 1)   // 1 is now more recent than 2
        cache.put(3, 3)              // evicts 2
        #expect(cache.get(2) == nil)
        cache.put(4, 4)              // evicts 1
        #expect(cache.get(1) == nil)
        #expect(cache.get(3) == 3)
        #expect(cache.get(4) == 4)
    }

    @Test func updatingAnExistingKeyDoesNotEvictAndRefreshesIt() {
        let cache = LRUCache<String, Int>(capacity: 2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("a", 10)   // update; "b" is now the least recent
        cache.put("c", 3)    // evicts "b"
        #expect(cache.get("a") == 10)
        #expect(cache.get("b") == nil)
        #expect(cache.get("c") == 3)
    }

    @Test func countNeverExceedsCapacity() {
        let cache = LRUCache<Int, Int>(capacity: 3)
        for i in 0..<10 {
            cache.put(i, i)
        }
        #expect(cache.count == 3)
    }

    @Test func aStoredZeroIsStillAHit() {
        let cache = LRUCache<String, Int>(capacity: 1)
        cache.put("zero", 0)
        #expect(cache.get("zero") == 0)
    }

    @Test func worksAtScale() {
        let cache = LRUCache<Int, Int>(capacity: 1000)
        for i in 0..<200_000 {
            cache.put(i, i)
        }
        #expect(cache.count == 1000)
        #expect(cache.get(199_999) == 199_999)
        #expect(cache.get(0) == nil)
    }
}

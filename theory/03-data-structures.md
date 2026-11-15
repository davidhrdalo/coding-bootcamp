# 03 - Data structures cheat sheet

Know what each one is good at, what it costs, and the Python name for it.

| Structure | Good for | Key costs | Python |
|---|---|---|---|
| **Array / list** | Fast access by position | Access O(1); append O(1) amortised; insert or delete in the middle O(n); search O(n) | `list` |
| **Linked list** | Cheap insert/delete when you hold a node | Access by position O(n) | write your own `ListNode` (see week 4) |
| **Stack** (LIFO) | Undo, backtracking, matching brackets, the call stack | push/pop O(1) | `list` (append, pop) |
| **Queue** (FIFO) | Scheduling, breadth-first search, buffering | enqueue/dequeue O(1) with the right structure | `collections.deque` |
| **Hash table / dict** | Look up by key | Average O(1) get/set; worst case O(n) | `dict` |
| **Set** | Membership tests, removing duplicates | Average O(1) | `set` |
| **Binary tree / BST** | Sorted data, hierarchies | Balanced: O(log n) search; unbalanced: O(n) | write your own `TreeNode` |
| **Heap / priority queue** | Always get the smallest (or largest) item next | push/pop O(log n), peek O(1) | `heapq` |
| **Graph** | Networks, maps, dependencies | depends on the representation | dict of lists |

## Things people get wrong

- **A Python `list` is a dynamic array**, not a linked list. Removing from the front (`pop(0)`) is O(n); use `deque` if you need that.
- **Dict and set lookups are fast because of hashing.** Keys must be hashable (immutable): a tuple can be a key, a list cannot.
- **Why is a hash table O(1) on average?** The key is hashed to an index in an array. Collisions (two keys with the same index) are handled by chaining or probing, and many collisions push it towards O(n).
- **Amortised O(1) append:** the array occasionally doubles in size (an expensive copy), but spread over many appends the average cost is constant.

## Choosing quickly

- Need to check "have I seen this?" -> `set`.
- Need to count things or map one thing to another -> `dict`.
- Need last-in-first-out -> stack. Need first-in-first-out -> `deque`.
- Need the smallest/largest repeatedly -> `heapq`.
- Need sorted order plus fast search -> sort once + binary search, or a balanced tree.

## Practice in this repo

Week 2 (dicts, sets, build a hash table), week 3 (stacks, queues, binary search, merge sort), week 4
(linked lists, binary search trees, graphs with BFS, heaps). For the basic value types, see `12-data-types.md`.

## Interview questions

1. When would you use a linked list instead of an array?
2. How does a hash table work, and what happens on a collision?
3. What is the difference between a stack and a queue? Give a real use for each.
4. Why is `list.pop(0)` slow in Python, and what would you use instead?
5. What is a heap (priority queue) used for?

## Learn more

- [VisuAlgo](https://visualgo.net/): animated data structures and algorithms
- [Python tutorial: data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Python time complexity of built-ins](https://wiki.python.org/moin/TimeComplexity)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [NeetCode roadmap](https://neetcode.io/roadmap): problems grouped by data structure

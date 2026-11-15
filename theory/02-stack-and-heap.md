# 02 - The stack, the heap and memory

## The call stack

Each time you call a function, the computer creates a **stack frame**: a block holding
that call's local variables, its arguments and where to return to. Frames are
pushed on a stack as you call deeper and popped as functions return.

- It is **last in, first out**: the most recent call finishes first.
- It is fast and cleaned up automatically when a function returns.
- It has a **limited size**. Recursion that goes too deep runs out of room: a **stack overflow**. Python raises `RecursionError` (default limit about 1000 frames).

```python
def countdown(n):
    if n == 0:
        return
    countdown(n - 1)      # each call adds a frame; n = 1,000,000 overflows
```

Every recursive function can be rewritten with your own stack (a list). The
exercise `theory/exercises/explicit_stack.py` makes you do exactly that.

## The heap

The **heap** is a large pool of memory for data that must outlive a single function call
or whose size is not known in advance (objects, big arrays, strings that grow).

- Slower to allocate than the stack and it must be **cleaned up** by someone.
- Who cleans it up depends on the language:

| Approach | How it works | Languages |
|---|---|---|
| Manual | You free it yourself (forgetting = memory leak, freeing twice = crash) | C, C++ |
| Garbage collection (GC) | A background process finds unreachable objects and frees them | Java, JavaScript, Kotlin, C# |
| Reference counting (ARC) | Each object counts who references it and is freed at zero | Swift, Objective-C, Python (plus a cycle collector) |

## Why this matters for you

- **Swift:** `struct` and `enum` are *value types* (copied when passed around, often stored inline or on the stack). `class` instances are *reference types* on the heap, managed by **ARC**. Two objects that hold strong references to each other form a **retain cycle** and never free; the fix is `weak` or `unowned`. This is a classic iOS interview topic.
- **Python:** every value is an object on the heap, and variables are just references to them. Reference counting frees most objects immediately; a cycle collector catches loops.
- **Kotlin and JavaScript:** garbage collected, so you rarely free memory yourself, but you can still leak it by keeping references alive (for example, a listener that is never removed).
- **Pass by value vs reference:** be able to explain what happens when you modify a list inside a function in Python (the caller sees the change, because the reference is shared).

## Interview questions

1. What is the difference between the stack and the heap?
2. What causes a stack overflow, and how can you avoid one?
3. What is a memory leak, and how can one happen in a garbage-collected language?
4. What is a retain cycle in Swift, and how do you break it?
5. What is the difference between a value type and a reference type?

## Learn more

- [Python Tutor](https://pythontutor.com/): step through code and watch frames and objects appear
- [Stack and heap memory (University of Vermont course page)](https://uvm.edu/~cbcafier/cs2240/content/03_queue_stack_linked_list/01_memory_stack_and_heap.html)
- [Swift: Automatic Reference Counting](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/)
- [Python gc module](https://docs.python.org/3/library/gc.html)
- [Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/) (free book; the virtualization chapters on address spaces and memory API)
- [CS50x](https://cs50.harvard.edu/x/): the memory lecture covers stack, heap and pointers

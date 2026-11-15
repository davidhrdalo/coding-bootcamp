# 07 - Big-O: how code scales

Big-O describes how the work (time) or memory (space) grows as the input size **n** grows.
It ignores constants and small terms: 3n + 10 is just **O(n)**.

## The ones you must know (best to worst)

| Big-O | Name | Example |
|---|---|---|
| O(1) | constant | dict lookup, list index, push on a stack |
| O(log n) | logarithmic | binary search (halve the problem each step) |
| O(n) | linear | one pass over a list |
| O(n log n) | linearithmic | good sorting (merge sort, Python `sorted`) |
| O(n^2) | quadratic | a loop inside a loop over the same list |
| O(2^n) | exponential | naive recursive Fibonacci |
| O(n!) | factorial | trying every ordering |

Roughly, for n = 1,000,000: O(n) is about a million steps, O(n log n) about 20 million,
O(n^2) about a trillion (far too slow).

## Rules of thumb

- **Drop constants and lower terms:** O(2n + 5) = O(n); O(n^2 + n) = O(n^2).
- **Sequential steps add, nested steps multiply:** two loops one after another is O(n + m); a loop inside a loop is O(n * m).
- **Halving each step means log n.**
- **Space counts too:** a hash set to remember what you have seen costs O(n) extra memory but can turn an O(n^2) solution into O(n).
- **Best, average and worst case differ:** hash lookups are O(1) on average, O(n) worst case. Interviewers usually mean the worst case unless they say otherwise.
- **Amortised:** appending to a Python list is O(1) amortised (occasional resize, cheap on average).

## The trade-off you keep making

Many interview solutions trade **space for time**: store things in a dict or set so you stop re-scanning.
Two Sum, contains-duplicate and anagram problems are all this trick. Practise saying
"the brute force is O(n^2); with a hash map I can do O(n) at the cost of O(n) memory."

## Interview questions

1. What is the time complexity of binary search, and why?
2. Why is naive recursive Fibonacci exponential, and how do you fix it?
3. What is the complexity of looping over a list inside a loop over the same list?
4. Explain the time/space trade-off with an example.
5. What is the difference between O(n) and amortised O(1)?

## Learn more

- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Python time complexity of built-ins](https://wiki.python.org/moin/TimeComplexity)
- [MIT 6.006 Introduction to Algorithms (free video lectures)](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)
- [NeetCode](https://neetcode.io/): short video explanations that state complexity for every solution

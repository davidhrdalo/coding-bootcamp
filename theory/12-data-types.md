# 12 - Data types

A **data type** says what kind of value something is and what you can do with it. Interviewers
use data-type questions to check that you understand how values are really stored, not only how
to use them. The Python exercises in `python/exercises/week0_data_types/` practise all of this.

## The basic types (Python names)

| Type | Example | Notes |
|---|---|---|
| `int` | `42` | Any size (arbitrary precision). Immutable. |
| `float` | `3.14` | 64-bit binary floating point (IEEE 754). Immutable. |
| `bool` | `True` | A subclass of `int`: `True == 1`. Immutable. |
| `str` | `"hello"` | Sequence of Unicode characters. Immutable. |
| `None` | `None` | "No value". There is exactly one. |
| `list` | `[1, 2]` | Ordered, **mutable**. |
| `tuple` | `(1, 2)` | Ordered, **immutable**. Can be a dict key. |
| `dict` | `{"a": 1}` | Key to value, **mutable**. Keys must be hashable. |
| `set` | `{1, 2}` | Unique items, **mutable**. |
| `bytes` | `b"hi"` | Raw bytes, immutable. |

## Integers: range matters in other languages

- **Python** integers never overflow; they grow as needed.
- **Swift** `Int` is 64-bit on modern devices (range about -9.2 quintillion to +9.2 quintillion). Overflow is a **runtime crash** unless you use overflow operators (`&+`).
- **Kotlin/Java** `Int` is 32-bit (max 2,147,483,647) and silently **wraps around** on overflow; `Long` is 64-bit.
- **JavaScript** has one number type, a 64-bit float, so integers are only exact up to 2^53 - 1 (`Number.MAX_SAFE_INTEGER`). `BigInt` exists for larger values.

Be ready to explain what happens when you add 1 to the maximum value in each.

## Floating point

Computers store decimals in binary, and numbers like 0.1 have no exact binary form.

```python
0.1 + 0.2 == 0.3      # False  (0.30000000000000004)
```

- **Never compare floats with `==`.** Compare with a tolerance (`math.isclose`), as in `float_compare.py`.
- **Never use floats for money.** Use integers (cents) or `decimal.Decimal`, as in `money_cents.py`.
- Special values: `inf`, `-inf` and `nan` (not a number). `nan != nan`, even with itself.

## Strings and Unicode

- Strings are **immutable**: `s.upper()` returns a new string. Building a long string with `+=` in a loop is O(n^2); collect pieces and use `"".join(...)`.
- **Characters vs bytes:** `len("🙂")` is 1 character but it takes 4 bytes in UTF-8. Text is encoded to bytes to store or send it (`s.encode("utf-8")`).
- **UTF-8** is the standard encoding on the web. ASCII characters take 1 byte; others take 2 to 4.
- In **Swift**, `Character` is a *grapheme cluster* (what a user sees as one symbol), so "e" + a combining accent counts as one character. This is why Swift string indexing is not by integer.

## Truthiness and equality

- Falsy in Python: `None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `()`. Everything else is truthy, including `"0"` and `[0]`.
- `==` compares **values**; `is` compares **identity** (same object). Use `is` only for `None`, `True` and `False`.
- **JavaScript** differs: falsy values are `0`, `""`, `null`, `undefined`, `NaN` and `false`; and `==` does type coercion (`"5" == 5` is true) so use `===`.

## Mutable vs immutable (a favourite interview topic)

- **Immutable** types cannot change after creation (int, float, str, tuple, frozenset). **Mutable** types change in place (list, dict, set).
- **Aliasing:** `b = a` makes two names for the *same* list. Change it through one and the other sees it.
- **Shallow vs deep copy:** `list(a)` copies the outer list only; inner lists are shared. Use `copy.deepcopy` or copy each level.
- **Mutable default argument:** `def f(x, items=[])` shares one list across all calls. Use `None` as the default.
- **Hashing:** dict keys and set members must be hashable, which in practice means immutable.

## No value: null, None, nil

- **Python:** `None`. **JavaScript:** both `null` and `undefined`.
- **Swift:** `Optional` makes "might be missing" part of the type: `String?`. Unwrap safely with `if let`, `guard let` or `??`; force-unwrapping with `!` crashes if it is nil.
- **Kotlin:** nullable types `String?` with safe calls `?.` and the Elvis operator `?:`.
- The idea of making null part of the type system is a response to what Tony Hoare called his "billion-dollar mistake".

## Type systems

| Axis | Meaning | Examples |
|---|---|---|
| **Static** | types checked before running | Swift, Kotlin, Java, TypeScript |
| **Dynamic** | types checked while running | Python, JavaScript |
| **Strong** | few implicit conversions | Python (`"5" + 1` is an error) |
| **Weak** | many implicit conversions | JavaScript (`"5" + 1` is `"51"`) |

- **Type inference:** the compiler works out the type for you (`let x = 5` in Swift).
- **Generics:** write code that works for many types (`Array<T>`).
- Python **type hints** (`def f(x: int) -> str`) are not enforced when the program runs; tools such as mypy check them separately.
- **Conversion:** *explicit* (`int("42")`) vs *implicit* (coercion). Convert text from outside carefully: `bool("False")` is `True`.

## Interview questions

1. Why does `0.1 + 0.2 == 0.3` return false, and how do you handle money?
2. What is the difference between mutable and immutable types? Give an example of a bug that mutability causes.
3. What is the difference between `==` and `is`?
4. What happens on integer overflow in Python, Swift, Kotlin and JavaScript?
5. What is the difference between a character and a byte? What is UTF-8?
6. How do Swift optionals work, and why are they safer than null?
7. What is the difference between static and dynamic typing, and between strong and weak typing?

## Learn more

- [Python tutorial: Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)
- [Python data model](https://docs.python.org/3/reference/datamodel.html)
- [What Every Programmer Should Know About Floating-Point Arithmetic](https://floating-point-gui.de/)
- [The Absolute Minimum Every Developer Must Know About Unicode (Joel Spolsky)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
- [Facts and myths about Python names and values (Ned Batchelder)](https://nedbatchelder.com/text/names.html): the clearest explanation of aliasing and mutability
- [Swift: Optionals](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Optionals)
- [Kotlin: Null safety](https://kotlinlang.org/docs/null-safety.html)
- [MDN: JavaScript data types and data structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures)
- [Python Tutor](https://pythontutor.com/): see aliasing and mutation visually

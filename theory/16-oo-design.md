# 16 - Object-oriented design

"Explain SOLID", "composition vs inheritance" and "how would you design this?" are standard interview questions.
Practise them in `python/exercises/week7_oo_design/` (`python run.py week7`). The ideas are the same in Swift, TypeScript and Kotlin.

## The four ideas

- **Encapsulation:** a class owns its data and enforces its own rules (its **invariants**). Callers use methods, not fields, so nobody can put the object into an impossible state. (`BankAccount`: balance can never be negative.)
- **Abstraction:** expose what something does, hide how. Callers depend on an interface, not an implementation.
- **Inheritance:** a subclass reuses and specialises a parent. Use it only for a true "is a" relationship (a `Square` is a `Rectangle` in the exercise, though in real code even that is debatable).
- **Polymorphism:** different types answer the same message differently. Code that calls `shape.area()` works for any shape, including ones written later.

## Composition over inheritance

Inheritance couples a child to its parent's internals and gets tangled when you combine behaviours (`EmailAndSmsNotifier`...). **Composition** means an object HAS other objects it delegates to: a `Notifier` holds a list of channels. You can combine and swap parts at runtime, and each part is small and testable. Default to composition. Reach for inheritance when you genuinely model a hierarchy.

## SOLID in plain words

| Letter | Idea | Smell it fixes |
|---|---|---|
| **S**ingle responsibility | A class has one reason to change | A class that parses, validates, saves and emails |
| **O**pen/closed | Add behaviour by adding code, not by editing working code | A growing `if/elif` on type or kind (see `discount_rules`) |
| **L**iskov substitution | A subclass must work wherever its parent is expected | A subclass that throws "not supported" for an inherited method |
| **I**nterface segregation | Many small interfaces beat one big one | Implementing methods you never use |
| **D**ependency inversion | Depend on abstractions, and pass dependencies IN | Code that creates its own database connection or calls `time.time()` directly |

## Dependency injection and testing

Pass in what a class needs (a clock, an id generator, a storage object) instead of creating it inside. In production you pass the real thing. In a test you pass a **fake** (see `dependency_injection` and `rate_limiter`: the tests control time with a fake clock, so they run instantly and never flake).

- **Duck typing and `typing.Protocol`:** Python does not need a shared base class. If an object has `save()` and `load()`, it can be used as a `Storage`. A `Protocol` documents and type-checks that shape (`protocols_duck_typing`).
- **Test doubles:** a **stub** returns canned answers, a **fake** is a simple working implementation (an in-memory store), a **mock** records how it was called. Know the three words.

## Patterns that appear in the exercises

- **Strategy:** swap an algorithm by passing different objects (`discount_rules`).
- **Observer / publish-subscribe:** parts react to events without knowing each other (`event_bus`). The traps: handlers that throw, and unsubscribing while publishing.
- **State machine:** model allowed transitions in one table, not scattered ifs (`order_state_machine`).
- **Dependency injection:** passed-in collaborators (`dependency_injection`).

## Design for an interview question

For "design a parking lot / library / elevator": (1) ask what the requirements are, (2) list the nouns (they become classes) and verbs (methods), (3) decide who owns which rule, (4) say what could change and keep that behind an interface, (5) mention how you would test it. Talk through it out loud: clear reasoning matters more than a perfect UML diagram.

## Say it out loud

1. What are the four pillars of OOP? Give an example of each.
2. Composition vs inheritance: which do you prefer, and why?
3. What does "open for extension, closed for modification" mean? Show an example.
4. What is dependency injection, and how does it make code easier to test?
5. What is the difference between a stub, a fake and a mock?
6. What is the Liskov substitution principle? Give a violation.
7. When would you use a state machine?

## Learn more

- [Refactoring Guru: design patterns](https://refactoring.guru/design-patterns) (clear explanations with code)
- [Python: abc (abstract base classes)](https://docs.python.org/3/library/abc.html) and [typing.Protocol](https://docs.python.org/3/library/typing.html#typing.Protocol)
- [Martin Fowler: Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
- [Uncle Bob's SOLID principles](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html)

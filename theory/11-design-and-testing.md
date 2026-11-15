# 11 - Design principles, patterns and testing

## Object-oriented ideas

- **Encapsulation:** hide internal data behind methods (your `Stack` hides its list).
- **Abstraction:** expose what something does, not how.
- **Inheritance:** a type reuses another's behaviour. Use sparingly.
- **Polymorphism:** different types respond to the same call in their own way.
- **Composition over inheritance:** build behaviour by combining small objects rather than deep class trees.

## SOLID (say what each letter means in one sentence)

- **S**ingle responsibility: a class has one reason to change.
- **O**pen/closed: add behaviour by extension, not by editing working code.
- **L**iskov substitution: a subtype must be usable wherever its parent is.
- **I**nterface segregation: many small interfaces beat one large one.
- **D**ependency inversion: depend on abstractions (protocols/interfaces), not concrete classes.

## Patterns you will meet

- **Dependency injection:** pass in what a component needs instead of creating it inside. Makes code testable.
- **MVC / MVVM:** separate data (model), display (view) and the logic that connects them. SwiftUI and Jetpack Compose both fit MVVM naturally.
- **Observer / publish-subscribe:** things subscribe to changes (Combine, Flow, event listeners).
- **Repository:** one place that hides where data comes from (network, database, cache).
- **Singleton (use carefully), factory, strategy, adapter.**

## Immutability and pure functions

A **pure function** returns the same output for the same input and changes nothing else. Immutable data
cannot change after creation. Both make code easier to reason about and safe across threads.

## Testing

- **Unit tests** check small pieces quickly (you are writing them with pytest here).
- **Integration tests** check pieces working together; **end-to-end/UI tests** drive the whole app.
- The **test pyramid:** many unit tests, fewer integration tests, very few UI tests.
- **Test-driven development (TDD):** write a failing test, make it pass, then clean up. This repo works the same way.
- **Mocks and fakes** replace slow or unreliable dependencies (network, clock, database).

## Git in one paragraph

Be able to explain: commit, branch, merge vs rebase, pull request, resolving a conflict,
and how to undo something (revert vs reset). Be ready to describe how you work on a team.

## Interview questions

1. Explain SOLID with an example.
2. What is dependency injection, and why does it help testing?
3. What is MVVM and how would you structure a screen with it?
4. What makes a good unit test?
5. When would you merge and when would you rebase?

## Learn more

- [Refactoring Guru: design patterns](https://refactoring.guru/design-patterns)
- [Martin Fowler's site](https://martinfowler.com/): articles on testing, patterns and architecture
- [The Missing Semester of Your CS Education (MIT)](https://missing.csail.mit.edu/): git, the shell, debugging and more

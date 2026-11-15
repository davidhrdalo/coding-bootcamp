// ARC and retain cycles
//
// Swift frees a class instance when nothing holds a STRONG reference to it (Automatic Reference
// Counting, ARC). If two objects hold strong references to each other (a retain cycle), neither is
// ever freed: a memory leak. This is a classic iOS interview topic.
//
// Owner and Pet reference each other. As written the pair leaks: the tests create an Owner and a Pet,
// link them both ways, let them go out of scope, and check that BOTH were deallocated (deinit ran).
// Fix the cycle by changing exactly one declaration. Hint: a `weak` reference does not keep its
// target alive and becomes nil when the target is freed (so it must be an optional var).
//
// LifetimeTracker counts the deinit calls for the tests. Do not change it.
//
// Concepts: ARC, strong vs weak vs unowned, retain cycles, deinit.
// Which side should be weak, and why? Be ready to explain it.

final class Owner {
    let name: String
    var pet: Pet?

    init(name: String) {
        self.name = name
    }

    deinit {
        LifetimeTracker.ownerDeinits += 1
    }
}

final class Pet {
    let name: String
    var owner: Owner?   // This strong reference creates a retain cycle. Fix it.

    init(name: String) {
        self.name = name
    }

    deinit {
        LifetimeTracker.petDeinits += 1
    }
}

enum LifetimeTracker {
    static var ownerDeinits = 0
    static var petDeinits = 0

    static func reset() {
        ownerDeinits = 0
        petDeinits = 0
    }
}

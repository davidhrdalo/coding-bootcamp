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
    weak var owner: Owner?

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

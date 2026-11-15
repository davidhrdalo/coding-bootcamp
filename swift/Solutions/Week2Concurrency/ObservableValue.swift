final class Subscription {
    private var onCancel: (() -> Void)?

    init(onCancel: @escaping () -> Void) {
        self.onCancel = onCancel
    }

    func cancel() {
        onCancel?()
        onCancel = nil
    }
}

final class ObservableValue<Value> {
    private var handlers: [(id: Int, handler: (Value) -> Void)] = []
    private var nextID = 0

    var value: Value {
        didSet {
            for entry in handlers {
                entry.handler(value)
            }
        }
    }

    init(_ value: Value) {
        self.value = value
    }

    func subscribe(_ handler: @escaping (Value) -> Void) -> Subscription {
        let id = nextID
        nextID += 1
        handlers.append((id, handler))
        handler(value)
        return Subscription { [weak self] in
            self?.handlers.removeAll { $0.id == id }
        }
    }
}

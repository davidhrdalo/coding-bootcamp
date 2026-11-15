indirect enum Expr {
    case number(Double)
    case add(Expr, Expr)
    case multiply(Expr, Expr)
    case negate(Expr)
}

func evaluate(_ expr: Expr) -> Double {
    switch expr {
    case .number(let value):
        return value
    case .add(let left, let right):
        return evaluate(left) + evaluate(right)
    case .multiply(let left, let right):
        return evaluate(left) * evaluate(right)
    case .negate(let inner):
        return -evaluate(inner)
    }
}

func render(_ expr: Expr) -> String {
    switch expr {
    case .number(let value):
        return value == value.rounded() ? String(Int(value)) : String(value)
    case .add(let left, let right):
        return "(\(render(left)) + \(render(right)))"
    case .multiply(let left, let right):
        return "(\(render(left)) * \(render(right)))"
    case .negate(let inner):
        return "-\(render(inner))"
    }
}

func depth(_ expr: Expr) -> Int {
    switch expr {
    case .number:
        return 1
    case .add(let left, let right), .multiply(let left, let right):
        return 1 + max(depth(left), depth(right))
    case .negate(let inner):
        return 1 + depth(inner)
    }
}

protocol Shape {
    var name: String { get }
    var area: Double { get }
}

struct Circle: Shape {
    var radius: Double
    var name: String { return "circle" }
    var area: Double { return Double.pi * radius * radius }
}

struct Rectangle: Shape {
    var width: Double
    var height: Double
    var name: String { return "rectangle" }
    var area: Double { return width * height }
}

struct Square: Shape {
    var side: Double
    var name: String { return "square" }
    var area: Double { return side * side }
}

func totalArea(_ shapes: [any Shape]) -> Double {
    return shapes.reduce(0) { $0 + $1.area }
}

func largestShape(_ shapes: [any Shape]) -> (any Shape)? {
    return shapes.max { $0.area < $1.area }
}

func uniqueElements<T: Hashable>(_ items: [T]) -> [T] {
    var seen = Set<T>()
    return items.filter { seen.insert($0).inserted }
}

extension Sequence where Element: Numeric {
    func total() -> Element {
        return reduce(0, +)
    }
}

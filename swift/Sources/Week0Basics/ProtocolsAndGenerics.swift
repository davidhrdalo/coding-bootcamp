// Protocols, generics and extensions
//
// Protocols describe what a type can do without saying how. Generics write one function for many
// types. Extensions add methods to existing types. Swift favours composition with protocols over class
// inheritance.
//
// Shape is a protocol with `name` and `area`. Implement it for three structs:
//   Circle(radius:)             name "circle",    area = pi * radius * radius
//   Rectangle(width:height:)    name "rectangle", area = width * height
//   Square(side:)               name "square",    area = side * side
//
// totalArea(shapes)       the sum of the areas of a mixed array of shapes ([any Shape])
// largestShape(shapes)    the shape with the largest area, or nil for an empty array
// uniqueElements(items)   a generic function: the items without duplicates, keeping the first
//                         occurrence of each, in order (T: Hashable)
// total()                 an extension on any Sequence of Numeric elements that adds them up:
//                         [1, 2, 3].total() == 6   and   [0.5, 0.25].total() == 0.75
//
// Concepts: protocol, existential `any`, generics with constraints, extensions, Hashable, Set.

protocol Shape {
    var name: String { get }
    var area: Double { get }
}

struct Circle: Shape {
    var radius: Double
    var name: String { return "" }
    var area: Double { return 0 }
}

struct Rectangle: Shape {
    var width: Double
    var height: Double
    var name: String { return "" }
    var area: Double { return 0 }
}

struct Square: Shape {
    var side: Double
    var name: String { return "" }
    var area: Double { return 0 }
}

func totalArea(_ shapes: [any Shape]) -> Double {
    return 0
}

func largestShape(_ shapes: [any Shape]) -> (any Shape)? {
    return nil
}

func uniqueElements<T: Hashable>(_ items: [T]) -> [T] {
    return []
}

extension Sequence where Element: Numeric {
    func total() -> Element {
        return 0
    }
}

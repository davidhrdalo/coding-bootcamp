import Testing
@testable import Week0Basics

@Suite struct ProtocolsAndGenericsTests {
    @Test func eachShapeReportsItsNameAndArea() {
        let circle = Circle(radius: 2)
        #expect(circle.name == "circle")
        #expect(abs(circle.area - Double.pi * 4) < 1e-9)

        let rectangle = Rectangle(width: 3, height: 4)
        #expect(rectangle.name == "rectangle")
        #expect(rectangle.area == 12)

        let square = Square(side: 5)
        #expect(square.name == "square")
        #expect(square.area == 25)
    }

    @Test func totalAreaOfAMixedArray() {
        let shapes: [any Shape] = [Circle(radius: 1), Rectangle(width: 2, height: 3), Square(side: 2)]
        #expect(abs(totalArea(shapes) - (Double.pi + 6 + 4)) < 1e-9)
        #expect(totalArea([]) == 0)
    }

    @Test func largestShapeByArea() {
        let shapes: [any Shape] = [Circle(radius: 1), Rectangle(width: 2, height: 3), Square(side: 2)]
        #expect(largestShape(shapes)?.name == "rectangle")
        #expect(largestShape([]) == nil)
    }

    @Test func uniqueElementsKeepsFirstOccurrenceInOrder() {
        #expect(uniqueElements([3, 1, 3, 2, 1]) == [3, 1, 2])
        #expect(uniqueElements(["a", "a", "b"]) == ["a", "b"])
        #expect(uniqueElements([Int]()) == [])
    }

    @Test func totalWorksForAnyNumericSequence() {
        #expect([1, 2, 3].total() == 6)
        #expect([0.5, 0.25].total() == 0.75)
        #expect([Int]().total() == 0)
        #expect((1...4).total() == 10)
    }
}

// swift-tools-version: 5.9
import PackageDescription

// Three modules, one per block, so a compile error in one week does not stop the others.
// Tests use Swift Testing (the `Testing` module), which ships with Swift 6 / Xcode 16 and newer.
let package = Package(
    name: "Bootcamp",
    platforms: [.macOS(.v13)],
    targets: [
        .target(name: "Week0Basics", path: "Sources/Week0Basics"),
        .target(name: "Week1Algorithms", path: "Sources/Week1Algorithms"),
        .target(name: "Week2Concurrency", path: "Sources/Week2Concurrency"),
        .testTarget(name: "Week0BasicsTests", dependencies: ["Week0Basics"], path: "Tests/Week0BasicsTests"),
        .testTarget(name: "Week1AlgorithmsTests", dependencies: ["Week1Algorithms"], path: "Tests/Week1AlgorithmsTests"),
        .testTarget(name: "Week2ConcurrencyTests", dependencies: ["Week2Concurrency"], path: "Tests/Week2ConcurrencyTests"),
    ]
)

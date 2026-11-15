func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    var seen: [Int: Int] = [:]
    for (index, value) in nums.enumerated() {
        if let other = seen[target - value] {
            return [other, index]
        }
        seen[value] = index
    }
    return []
}

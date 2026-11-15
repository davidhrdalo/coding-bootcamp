func mergeSort(_ nums: [Int]) -> [Int] {
    if nums.count <= 1 { return nums }
    let middle = nums.count / 2
    let left = mergeSort(Array(nums[..<middle]))
    let right = mergeSort(Array(nums[middle...]))

    var merged: [Int] = []
    merged.reserveCapacity(nums.count)
    var i = 0
    var j = 0
    while i < left.count && j < right.count {
        if left[i] <= right[j] {
            merged.append(left[i])
            i += 1
        } else {
            merged.append(right[j])
            j += 1
        }
    }
    merged.append(contentsOf: left[i...])
    merged.append(contentsOf: right[j...])
    return merged
}

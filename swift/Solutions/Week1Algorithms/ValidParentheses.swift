func isValidParentheses(_ s: String) -> Bool {
    let pairs: [Character: Character] = [")": "(", "]": "[", "}": "{"]
    var stack: [Character] = []
    for character in s {
        if let opener = pairs[character] {
            if stack.popLast() != opener { return false }
        } else {
            stack.append(character)
        }
    }
    return stack.isEmpty
}

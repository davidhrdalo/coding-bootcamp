import Foundation

struct User: Codable, Equatable {
    let id: Int
    let fullName: String
    let email: String?

    enum CodingKeys: String, CodingKey {
        case id = "user_id"
        case fullName = "full_name"
        case email
    }
}

func decodeUsers(from json: String) throws -> [User] {
    return try JSONDecoder().decode([User].self, from: Data(json.utf8))
}

func encodeUser(_ user: User) throws -> String {
    let encoder = JSONEncoder()
    encoder.outputFormatting = .sortedKeys
    return String(decoding: try encoder.encode(user), as: UTF8.self)
}

// Codable: encoding and decoding JSON
//
// Almost every iOS app turns JSON into Swift types and back. Swift's Codable (Encodable plus Decodable)
// generates most of the code; you customise it with CodingKeys.
//
// User is a struct with id, fullName and an optional email. The JSON API uses different names:
//   "user_id"   <-> id
//   "full_name" <-> fullName
//   "email"     <-> email   (may be missing or null)
//
// Add a nested `enum CodingKeys: String, CodingKey` to User that maps each property to its JSON key.
// Then implement:
//
// decodeUsers(from:)   parse a JSON array of users from a String. Invalid JSON, or a missing required
//                      field, makes it throw (let the decoder's error propagate).
// encodeUser(_:)       produce the JSON text for one user with the keys in alphabetical order
//                      (JSONEncoder.outputFormatting = .sortedKeys). A nil email is simply left out.
//
// Concepts: Codable, CodingKeys, JSONEncoder / JSONDecoder, optionals in JSON, throwing functions,
// String <-> Data conversion (Data(json.utf8), String(decoding:as:)).

import Foundation

struct User: Codable, Equatable {
    let id: Int
    let fullName: String
    let email: String?
    // TODO: add CodingKeys so the JSON keys are "user_id", "full_name" and "email".
}

func decodeUsers(from json: String) throws -> [User] {
    return []
}

func encodeUser(_ user: User) throws -> String {
    return ""
}

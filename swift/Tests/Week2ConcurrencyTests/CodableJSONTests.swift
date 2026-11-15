import Testing
@testable import Week2Concurrency

import Foundation

@Suite struct CodableJSONTests {
    @Test func decodesAnArrayOfUsers() throws {
        let json = """
        [
          {"user_id": 1, "full_name": "Ann Lee", "email": "ann@example.com"},
          {"user_id": 2, "full_name": "Bob Ray"},
          {"user_id": 3, "full_name": "Cy Poe", "email": null}
        ]
        """
        let users = try decodeUsers(from: json)
        #expect(users == [
            User(id: 1, fullName: "Ann Lee", email: "ann@example.com"),
            User(id: 2, fullName: "Bob Ray", email: nil),
            User(id: 3, fullName: "Cy Poe", email: nil),
        ])
    }

    @Test func decodesAnEmptyArray() throws {
        #expect(try decodeUsers(from: "[]") == [])
    }

    @Test func invalidJSONThrows() {
        #expect(throws: (any Error).self) {
            try decodeUsers(from: "not json")
        }
    }

    @Test func missingRequiredFieldThrows() {
        #expect(throws: (any Error).self) {
            try decodeUsers(from: #"[{"user_id": 1}]"#)
        }
    }

    @Test func encodesWithSortedKeysAndOmitsNilEmail() throws {
        let user = User(id: 1, fullName: "Ann Lee", email: nil)
        #expect(try encodeUser(user) == #"{"full_name":"Ann Lee","user_id":1}"#)
    }

    @Test func encodesAnEmailWhenPresent() throws {
        let user = User(id: 7, fullName: "Bob Ray", email: "bob@example.com")
        #expect(try encodeUser(user) == #"{"email":"bob@example.com","full_name":"Bob Ray","user_id":7}"#)
    }

    @Test func roundTrips() throws {
        let original = User(id: 9, fullName: "Dee Fox", email: "dee@example.com")
        let json = try encodeUser(original)
        let decoded = try decodeUsers(from: "[" + json + "]")
        #expect(decoded == [original])
    }
}

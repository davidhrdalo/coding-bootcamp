import Testing
@testable import Week0Basics

@Suite(.serialized) struct RetainCyclesTests {
    @Test func bothObjectsAreFreedWhenTheyGoOutOfScope() {
        LifetimeTracker.reset()
        do {
            let owner = Owner(name: "Ann")
            let pet = Pet(name: "Rex")
            owner.pet = pet
            pet.owner = owner
        }
        #expect(LifetimeTracker.ownerDeinits == 1, "the Owner should be deallocated")
        #expect(LifetimeTracker.petDeinits == 1, "the Pet should be deallocated")
    }

    @Test func thePetCanStillSeeItsOwnerWhileTheOwnerLives() {
        let owner = Owner(name: "Ann")
        let pet = Pet(name: "Rex")
        owner.pet = pet
        pet.owner = owner
        #expect(pet.owner?.name == "Ann")
        #expect(owner.pet?.name == "Rex")
    }

    @Test func aWeakReferenceBecomesNilWhenTheOwnerIsGone() {
        let pet = Pet(name: "Rex")
        do {
            let owner = Owner(name: "Ann")
            owner.pet = pet
            pet.owner = owner
        }
        #expect(pet.owner == nil)
    }
}

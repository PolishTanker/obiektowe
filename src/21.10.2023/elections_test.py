import unittest

from elections import Constituency 
from elections import NameValidator

class ElectionsTest(unittest.TestCase):
    def setUp(self):
        self.testee = Constituency(['PartyA', 'PartyB', 'PartyC'])

    def test_is_created(self):
        self.assertIsNotNone(self.testee)

    def test_can_register(self):
        voter = 'Bob'
        self.testee.register_voter(voter)
        self.assertTrue(self.testee.is_registered(voter))

    def test_registered_can_vote(self):
        self.testee.register_voter('Bob')
        self.assertTrue(self.testee.can_vote('Bob'))

    def test_cannot_register_twice(self):
        voter = 'Bob'
        self.testee.register_voter(voter)
        with self.assertRaises(RuntimeError):
            self.testee.register_voter(voter)

    def test_vote_twice(self):
        self.testee.register_voter('Bob')
        self.testee.vote('Bob', party='PartyA')
        with self.assertRaises(RuntimeError):
            self.testee.vote('Bob', party='PartyA')

    def test_votes_are_reflected_in_party_totals(self):
        self.testee.register_voter('Bob')
        self.testee.vote('Bob', party='PartyA')
        self.assertEqual(self.testee.get_votes_of_party('PartyA'), 1)

    def test_cannot_vote_for_nonexistent_party(self):
        self.testee.register_voter('Bob')
        with self.assertRaises(RuntimeError):
            self.testee.vote('Bob', party='NonexistentParty')

    def test_cannot_create_two_parties_with_same_name(self):
        with self.assertRaises(ValueError):
            Constituency(['PartyA', 'PartyA'])

    # with validators
    def test_can_create_voter_with_valid_name(self):
        validator = NameValidator()
        self.assertTrue(validator.is_valid('ValidName'))

    def test_cannot_create_voter_with_invalid_name(self):
        validator = NameValidator()
        self.assertFalse(validator.is_valid('Invalid Name'))


    
if __name__ == '__main__':
    unittest.main()

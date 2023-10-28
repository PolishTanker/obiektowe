import unittest

from elections import VoterEligibilityValidator

class TestVoterEligibilityValidator(unittest.TestCase):

    def setUp(self):
        self.validator = VoterEligibilityValidator()

    def test_valid_names(self):
        valid_names = [
            "Abc123",
            "Test123",
            "OpenAI2022",
        ]
        for name in valid_names:
            with self.subTest(name=name):
                self.assertTrue(self.validator.is_valid(name))

    def test_invalid_names_too_short(self):
        invalid_names = [
            "A1",
            "b2",
            "C3",
        ]
        for name in invalid_names:
            with self.subTest(name=name):
                self.assertFalse(self.validator.is_valid(name))

    def test_invalid_names_no_uppercase(self):
        invalid_names = [
            "test123",
            "123abc",
        ]
        for name in invalid_names:
            with self.subTest(name=name):
                self.assertFalse(self.validator.is_valid(name))

    def test_invalid_names_no_lowercase(self):
        invalid_names = [
            "TEST123",
            "123ABC",
        ]
        for name in invalid_names:
            with self.subTest(name=name):
                self.assertFalse(self.validator.is_valid(name))

    def test_invalid_names_no_digit(self):
        invalid_names = [
            "TestABC",
            "testABC",
        ]
        for name in invalid_names:
            with self.subTest(name=name):
                self.assertFalse(self.validator.is_valid(name))

if __name__ == '__main__':
    unittest.main()
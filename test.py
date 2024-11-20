import unittest
from main import validate_postal_code, find_postal_codes_in_text, find_postal_codes_in_file

class TestPostalCodeValidation(unittest.TestCase):
    def test_validate_postal_code(self):
        self.assertTrue(validate_postal_code("12345"))
        self.assertFalse(validate_postal_code("1234"))
        self.assertFalse(validate_postal_code("123456"))
        self.assertFalse(validate_postal_code("12a45"))  # Неправильный символ
        self.assertFalse(validate_postal_code("1234-5"))  # Неправильный формат

    def test_find_postal_codes_in_text(self):
        text = "Valid postal codes: 12345, 54321. Invalid ones: 1234, 123456, abcde."
        expected = ["12345", "54321"]
        self.assertEqual(find_postal_codes_in_text(text), expected)

    def test_find_postal_codes_in_file(self):
        with open('test_file.txt', 'w') as file:
            file.write("Valid: 12345\nInvalid: 1234\nAnother valid: 54321")
        self.assertEqual(find_postal_codes_in_file('test_file.txt'), ["12345", "54321"])

if __name__ == '__main__':
    unittest.main()

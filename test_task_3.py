import unittest
from task_3 import normalize_phone


class TestNormalizePhone(unittest.TestCase):

    def test_normalize_with_international_code(self):
        """with international codes"""
        self.assertEqual(normalize_phone("+380 44 123 4567"), "+380441234567")
        self.assertEqual(normalize_phone("380501234567"), "+380501234567")

    def test_normalize_without_international_code(self):
        """without international codes"""
        self.assertEqual(normalize_phone("067\\t123 4567"), "+380671234567")
        self.assertEqual(normalize_phone("     0503451234"), "+380503451234")
        self.assertEqual(normalize_phone("(095) 234-5678\\n"), "+380952345678")

    def test_normalize_with_special_characters(self):
        """with special characters"""
        self.assertEqual(normalize_phone("38050-111-22-22"), "+380501112222")
        self.assertEqual(normalize_phone("38050 111 22 11   "), "+380501112211")
        self.assertEqual(normalize_phone("+38(050)123-32-34"), "+380501233234")

    def test_normalize_with_only_digits(self):
        """only digits"""
        self.assertEqual(normalize_phone("0501234567"), "+380501234567")

    def test_normalize_with_one_plus(self):
        """normalizes with a single '+' at the start"""
        self.assertEqual(normalize_phone("+380441234567"), "+380441234567")
    
    def test_normalize_with_many_plus(self):
        """handles numbers with many '+' signs"""
        self.assertEqual(normalize_phone("+38044++123++4567"), "+380441234567")

    def test_empty_string(self):
        """empty strings"""
        result = normalize_phone("")
        self.assertEqual(result, "error format")

    def test_invalid_format(self):
        """invalid format"""
        result = normalize_phone("abc123")
        expected = "error format"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main(verbosity=3)

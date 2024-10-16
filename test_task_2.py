import unittest
from task_2 import get_numbers_ticket


class TestGetNumbersTicket(unittest.TestCase):

    def test_correct_parameters(self):
        result = get_numbers_ticket(1, 100, 10)
        self.assertEqual(len(result), 10)
        self.assertTrue(all(1 <= num <= 100 for num in result))
        self.assertEqual(len(result), len(set(result)), "All numbers should be unique")

    def test_invalid_min(self):
        result = get_numbers_ticket(0, 100, 10)
        self.assertEqual(result, [], "Should return empty list for invalid min")

    def test_invalid_max(self):
        result = get_numbers_ticket(1, 2000, 10)
        self.assertEqual(result, [], "Should return empty list for invalid max")

    def test_invalid_quantity(self):
        result = get_numbers_ticket(1, 100, -5)
        self.assertEqual(result, [], "Should return empty list for invalid quantity")

    def test_no_numbers_when_min_equals_max(self):
        result = get_numbers_ticket(1, 1, 1)
        self.assertEqual(result, [1], "Should return [1] when min and max are equal")

    def test_zero_quantity(self):
        result = get_numbers_ticket(1, 100, 0)
        self.assertEqual(result, [], "Should return empty list for quantity of 0")

if __name__ == "__main__":
    unittest.main(verbosity=3)
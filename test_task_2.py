import unittest
from task_2 import get_numbers_ticket

class TestRandomNumberGenerator(unittest.TestCase):
    
    def test_get_numbers_ticket_unique(self):
        """check if the function returns 10 unique numbers"""
        numbers = get_numbers_ticket(10)
        self.assertEqual(len(numbers), 10)
        self.assertEqual(len(numbers), len(set(numbers)))

    def test_get_numbers_ticket_within_range(self):
        """chek if the function returns numbers within the range"""
        min_value, max_value = 1, 100
        numbers = get_numbers_ticket(10)
        for number in numbers:
            self.assertGreaterEqual(number, min_value)
            self.assertLessEqual(number, max_value)

    def test_get_numbers_ticket_default_quantity(self):
        """check if the function returns 10 numbers by default"""
        numbers = get_numbers_ticket()
        self.assertEqual(len(numbers), 10)
        
if __name__ == "__main__":
    unittest.main(verbosity=3)
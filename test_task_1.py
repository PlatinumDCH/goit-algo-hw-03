import unittest
from datetime import datetime
from task_1 import get_days_from_today

class TestGetDaysFromToday(unittest.TestCase):
    
    def test_past_date(self):
        '''past date'''
        self.assertGreater(get_days_from_today("2022.01.01"), 0)
    
    def test_future_date(self):
        '''future date'''
        self.assertLess(get_days_from_today("2025.01.01"), 0)
    
    def test_today_date(self):
        '''current date'''
        today = datetime.today().strftime("%Y.%m.%d")
        self.assertEqual(get_days_from_today(today), 0)
    
    def test_incorrect_format(self):
        '''uncorrect format'''
        with self.assertRaises(ValueError):
            get_days_from_today("2025-01-01")

    def test_invalid_date(self):
        '''non-existent date'''
        with self.assertRaises(ValueError):
            get_days_from_today("2023.02.30")

if __name__ == "__main__":
    unittest.main(verbosity=2)

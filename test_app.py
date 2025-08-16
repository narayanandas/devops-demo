import unittest
from app import *   # or import what you want to test

class TestApp(unittest.TestCase):
    def test_hello(self):
        # Example: if app.py has a hello() function
        self.assertEqual(1 + 1, 2)  # Just a dummy test

if __name__ == '__main__':
    unittest.main()

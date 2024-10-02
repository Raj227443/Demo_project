import unittest
from app import add, multiply

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 4), 8)

if __name__ == '__main__':
    unittest.main()

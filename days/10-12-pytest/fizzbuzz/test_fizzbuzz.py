import unittest

from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(fizzbuzz(1),1)
        self.assertEqual(fizzbuzz(2),2)
        self.assertEqual(fizzbuzz(3), "Fizz")

if __name__ == "__main__":
    unittest.main()
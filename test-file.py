import unittest
from your_module_name import add, sub, mul  # Replace 'your_module_name' with your actual filename (without .py)

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(sub(4, 1), 3)
        self.assertEqual(sub(1, 4), -3)
        self.assertEqual(sub(0, 0), 0)

    def test_mul(self):
        self.assertEqual(mul(4, 1), 4)
        self.assertEqual(mul(0, 10), 0)
        self.assertEqual(mul(-2, 3), -6)

if __name__ == '__main__':
    unittest.main()

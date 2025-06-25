import unittest
import mymath

class TestMath(unittest.TestCase):

    def test_match(self):
        self.assertEqual(mymath.add(2, 3), 5)
        self.assertEqual(mymath.div(6, 3), 2)
        self.assertEqual(mymath.div(42, 1), 42)
        self.assertEqual(mymath.add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()

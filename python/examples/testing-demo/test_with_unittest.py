import unittest
import mymath

class TestMath(unittest.TestCase):
    def test_math(self):
        self.assertEqual(mymath.add(2, 2), 4)

    def test_more_math(self):
        self.assertEqual(mymath.add(3, 3), 6)

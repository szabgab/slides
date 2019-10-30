from os.path import dirname,abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from mymath.calc import add
import unittest

class AddTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, -2), 0)
        #self.assertEqual(add(1, 1), 1)

if __name__ == '__main__':
    unittest.main()

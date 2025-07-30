from os.path import dirname,abspath
import sys

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))
from mymath.calc import *
import unittest

class AllTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add(2, 3), 5)
        #self.assertEqual(sum(1, 1), 2)
        #self.assertEqual(div(6, 2), 3)

if __name__ == '__main__':
    unittest.main()

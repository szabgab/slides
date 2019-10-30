import unittest
import Calculator

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(4, 8), 12)
        self.assertEqual(Calculator.add(10, 8), 18)
        self.assertEqual(Calculator.add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
 

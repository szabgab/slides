import unittest

class TestReg(unittest.TestCase):

    def setUp(self):
        self.str_number = "123"
        self.str_not_number = "12x"

    def test_match1(self):
        self.assertEqual(1, 1)
        self.assertRegexpMatches(self.str_number, r'^\d+$')

    def test_match2(self):
        self.assertEqual(1, 1)
        self.assertRegexpMatches(self.str_not_number, r'^\d+$')

if __name__ == '__main__':
    unittest.main()
 

import unittest

def add(x, y):
    return x+y

class Something(unittest.TestCase):

    def setUp(self):
        pass
        #print("setup")

    def tearDown(self):
        pass
        #print("teardown")

    def test_something(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 3), 3)
        self.assertEqual(add(0, 3), 2)


    def test_other(self):
        self.assertEqual(add(-3, 3), 0)
        self.assertEqual(add(-3, 2), 7)
        self.assertEqual(add(-3, 2), 0)

    
if __name__ == '__main__':
    unittest.main()


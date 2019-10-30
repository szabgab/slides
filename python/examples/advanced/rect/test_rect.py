import shape2
import unittest

class TestRect(unittest.TestCase):

    def assertEqualSides(self, left, right):
        if isinstance(right, tuple):
            right = shape2.Rectangular(*right)

        if left.width != right.width:
            raise AssertionError('widths are different')
        if left.height != right.height:
            raise AssertionError('heights are different')

    def setUp(self):
        self.a = shape2.Rectangular(4, 10)
        self.b = shape2.Rectangular(2, 20)
        self.c = shape2.Rectangular(1, 30)
        self.d = shape2.Rectangular(4, 10)

    def test_sanity(self):
        self.assertEqualSides(self.a, self.a)
        self.assertEqualSides(self.a, self.d)
        try:
            self.assertEqualSides(self.a, self.b)
        except AssertionError as e:
              self.assertEqual(e.args[0], 'widths are different')

        try:
            self.assertEqualSides(self.a, shape2.Rectangular(4, 20))
        except AssertionError as e:
              self.assertEqual(e.args[0], 'heights are different')

        self.assertEqualSides(self.a, (4, 10))

    def test_str(self):
        self.assertEqual(str(self.a), 'Rect[4, 10]')
        self.assertEqual(str(self.b), 'Rect[2, 20]')
        self.assertEqual(str(self.c), 'Rect[1, 30]')

    def test_mul(self):
        self.assertEqual(str(self.a * 3), 'Rect[4, 30]')
        self.assertEqual(str(self.b * 7), 'Rect[2, 140]')

    def test_rmul(self):
        self.assertEqual(str(3 * self.a), 'Rect[12, 10]')
        self.assertEqualSides(3 * self.a, (12, 10))

    def test_area(self):
        self.assertEqual(self.a.area(), 40)
        self.assertEqual(self.b.area(), 40)
        self.assertEqual(self.c.area(), 30)

    def test_equal(self):
        self.assertEqual(self.a, self.d)
        self.assertEqual(self.a, self.b)

    def test_add(self):
        self.assertEqualSides(self.a + shape2.Rectangular(4, 20), (4, 30))




if __name__ == '__main__':
    unittest.main()

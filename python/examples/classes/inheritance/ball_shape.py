class Point():
    def __init__(self, x, y):
        print('__init__ of Point')
        self.x = x
        self.y = y

class Circle(Point):
    def __init__(self, x, y, r):
        print('__init__ of Circle')
        Point.__init__(self, x, y)
        # super(Circle, self).__init__(x, y)
        self.r = r
    def area(self):
        return self.r * self.r * 3.14

class Ball(Circle):
    def __init__(self, x, y, r, z):
        print('__init__ of Ball')
        # Circle.__init__(self, x, y, r)
        # super(Ball, self).__init__(x, y, r)
        self.z = z


b = Ball(2, 3, 10, 7)
print(b)
print(b.area)

# __init__ of Ball
# __init__ of Circle
# __init__ of Point
# <__main__.Ball object at 0x103dea190>

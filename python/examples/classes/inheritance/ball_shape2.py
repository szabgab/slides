class Point(object):
    def __init__(self, x, y):
        print('__init__ of point')
        self.x = x
        self.y = y

class Circle(Point):
    def __init__(self, x, y, r):
        print('__init__ of circle')
        #super(Circle, self).__init__(x, y)
        Point.__init__(self, x, y)
        self.r = r

class Ball(Circle):
    def __init__(self, x, y, r, z):
        print('__init__ of ball')
        #super(Circle, self).__init__(x, y) # r
        Point.__init__(self, x, y) # r
        self.z = z


b = Ball(2, 3, 10, 7)
print(b)

# __init__ of ball
# __init__ of point
# <__main__.Ball object at 0x10a26f190>

class Point(object):
    def __init__(self, x, y):
        print('__init__ of point')
        self.x = x
        self.y = y

class Circle(Point):
    def __init__(self, x, y, r):
        print('__init__ of circle')
        super(Circle, self).__init__(x, y)
        self.r = r

class Ball(Circle):
    def __init__(self, x, y, r, z):
        print('__init__ of ball')
        super(Zero, self).__init__(x, y)
        self.z = z

class Zero(object):
    def __init__(self, x, y):
        print('really?')
    pass


b = Ball(2, 3, 10, 7)
print(b)

# __init__ of circle
# Traceback (most recent call last):
#   File "bad_shapes.py", line 25, in <module>
#     b = Ball(2, 3, 10, 7)
#   File "bad_shapes.py", line 16, in __init__
#     super(Zero, self).__init__(x, y)
# TypeError: super(type, obj): obj must be an instance or subtype of type


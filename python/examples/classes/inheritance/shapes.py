class Point():
    def __init__(self, x, y):
        print('__init__ of Point')
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Circle(Point):
    def __init__(self, x, y, r):
        print('__init__ of Circle')
        super().__init__(x, y)
        self.r = r

    def area(self):
        return self.r * self.r * 3.14

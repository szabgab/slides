class Line(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def distance(self):
        return ((self.a.x - self.b.x) ** 2  + (self.a.y - self.b.y) ** 2) ** 0.5

class Point(object):
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

p1 = Point(0, 0)
p2 = Point(0, 2)
l = Line(p1, p2)
print(l.distance())

p2.move(0, 4)
print(l.distance())

p2.move(3, -2)
print(l.distance())


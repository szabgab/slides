class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def length(self):
        return ((self.a.x - self.b.x) ** 2 + (self.a.y - self.b.y) ** 2) ** 0.5

p1 = Point(2, 3)
p2 = Point(5, 7)
l = Line(p1, p2)

print(l.a)
print(l.b)
print(l.length())   # 5.0

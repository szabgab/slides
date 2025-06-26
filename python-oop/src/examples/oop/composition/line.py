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
blue_line = Line(p1, p2)

print(blue_line.a) # <__main__.Point object at 0x0000022174B637B8>
print(blue_line.b) # <__main__.Point object at 0x0000022174B3C7B8>
print(blue_line.length())   # 5.0

xl = Line(4, 6)
print(xl)  # <__main__.Line object at 0x7fb15f8f5ee0>

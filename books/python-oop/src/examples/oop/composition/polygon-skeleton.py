class Point():
    pass

class Polygon():
    pass

p1 = Point(0, 0)  # Point(0, 0)
p2 = Point(5, 7)  # Point(5, 7)
p3 = Point(4, 9)  # Point(4, 9)
print(p1)
print(p2)
print(p3)
p1.move(2, 3)
print(p1)         # Point(2, 3)

poly = Polygon(p1, p2, p3)
print(poly)       # Polygon(Point(2, 3), Point(5, 7), Point(4, 9))
poly.move(-1, 1)
print(poly)       # Polygon(Point(1, 4), Point(4, 8), Point(3, 10))

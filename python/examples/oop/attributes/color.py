from shapes import Point

p1 = Point(4, 5)
print(p1.x)  # 4
print(p1.y)  # 5

p1.color = 'blue'
print(p1.color) # blue


p2 = Point(7, 8)
print(p2.x)  # 7
print(p2.y)  # 8
print(p2.color)  # AttributeError: 'Point' object has no attribute 'color'


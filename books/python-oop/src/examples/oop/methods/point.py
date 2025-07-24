from shapes import Point

p1 = Point(2, 3)
print(p1.x)    # 2
print(p1.y)    # 3

p1.move(4, 5)
print(p1.x)    # 6
print(p1.y)    # 8


print(p1)      # <shapes.Point object at 0x7fb0691c3e48>

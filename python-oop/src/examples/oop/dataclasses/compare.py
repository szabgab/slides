from shapes import Point

p1 = Point(2, 3, 'left')
print(p1.x)    # 2
print(p1.y)    # 3
print(p1.name) # left

p2 = Point(2, 3, 'left')
p3 = Point(2, 3, 'right')

print(p1 == p2)  # True
print(p1 == p3)  # False


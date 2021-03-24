from shapes import Point

p1 = Point(2, 3, 'left')
print(p1.x)    # 2
print(p1.y)    # 3
print(p1.name) # left

p1.x = 7       # 7
print(p1.x)

p1.color = 'blue'
print(p1.color)   # blue

p1.x = 'infinity' # infinity
print(p1.x)



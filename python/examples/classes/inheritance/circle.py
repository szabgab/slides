import shapes

c = shapes.Circle(2, 3, 10)   # __init__ of Circle
                              # __init__ of Point
print(c)          # <shapes.Circle instance at 0x7fb58c31ccb0>
print(c.x)        # 2
print(c.y)        # 3
print(c.r)        # 10

c.move(4, 5)
print(c.x)        # 6
print(c.y)        # 8
print(c.area())   # 314.0

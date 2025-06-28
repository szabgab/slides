class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

p = Point(2, 3)
print(p)                 # <__main__.Point object at 0x10369d750>
print("{}".format(p))    # <__main__.Point object at 0x10369d750>
print("{!s}".format(p))  # <__main__.Point object at 0x10369d750>
print("{!r}".format(p))  # <__main__.Point object at 0x10369d750>

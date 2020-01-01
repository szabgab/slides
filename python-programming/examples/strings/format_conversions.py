class Point(object):
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def __format__(self, spec):
        #print(spec) // empty string
        return("{{'x':{}, 'y':{}}}".format(self.x, self.y))
    def __str__(self):
        return("({},{})".format(self.x, self.y))
    def __repr__(self):
        return("Point({}, {})".format(self.x, self.y))

p = Point(2, 3)
print(p)                 # (2,3)
print("{}".format(p))    # {'x':2, 'y':3}
print("{!s}".format(p))  # (2,3)
print("{!r}".format(p))  # Point(2, 3)

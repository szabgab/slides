class Circle():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        print('in area')
        return self.r * self.r * 3.14


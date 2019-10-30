class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
       return 'Point({}, {})'.format(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

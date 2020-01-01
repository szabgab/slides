class Point():
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

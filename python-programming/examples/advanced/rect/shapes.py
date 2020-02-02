import copy

class Rect:
    def __init__(self, w, h):
        self.width  = w
        self.height = h

    def __str__(self):
        return 'Rect[{}, {}]'.format(self.width, self.height)

    def __mul__(self, other):
        o = int(other)
        new = copy.deepcopy(self)
        new.height *= o
        return new

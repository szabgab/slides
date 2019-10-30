import copy
import shapes

class Rectangular(shapes.Rect):

    def __rmul__(self, other):
        o = int(other)
        new = copy.deepcopy(self)
        new.width *= o
        return new

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area() == other.area()

    def __add__(self, other):
        new = copy.deepcopy(self)
        if self.width == other.width:
            new.height += other.height
        elif self.height == other.height:
            new.width += other.width
        else:
            raise Exception('None of the sides are equal')
        return new




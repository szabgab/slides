from shapes import Point

p1 = Point(2, 3, 'left')
print(p1)           # Point(x=2, y=3, name='left')
# p1.x = 7          # dataclasses.FrozenInstanceError: cannot assign to field 'x'
# p1.color = 'blue' # dataclasses.FrozenInstanceError: cannot assign to field 'color'


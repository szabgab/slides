from shapes import Circle
from tools import add_debug

x = Circle(2, 3, 4)
print(x.area())
print('-----')

add_debug(Circle, 'area')

print(x.area())
# print('-----')
# print(x.area.__name__)



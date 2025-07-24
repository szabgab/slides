from shapes import Point

p1 = Point(2, 3, 'left')
print(p1)  # Point(x=2, y=3, name='left')

p2 = Point()
print(p2) # Point(x=0, y=0, name='Nameless')

p3 = Point( name = 'Good', x = 42)
print(p3) # Point(x=42, y=0, name='Good')


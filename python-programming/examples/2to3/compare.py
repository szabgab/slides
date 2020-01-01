x = 3
y = '3'

                    # Python 2      Python 3
print( x > y )      # False         TypeError: unorderable types: int() > str()
print( x < y )      # True          TypeError: unorderable types: int() < str()
print( x == y )     # False         False

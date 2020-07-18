import numpy

a = numpy.array([
    [ 1,  2,  3,  4,  5],
    [ 2,  3,  4,  5,  6]
])

b = a.copy().transpose()
a[0][0] = 42

print(b)
# [[1 2]
#  [2 3]
#  [3 4]
#  [4 5]
#  [5 6]]

print(a)
# [[42 2 3 4 5]
#  [2 3 4 5 6]]

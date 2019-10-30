import numpy

a = numpy.array([
    [ 1,  2,  3,  4,  5],
    [ 2,  3,  4,  5,  6]
])

b = a.transpose()

print(b)
# [[1 2]
#  [2 3]
#  [3 4]
#  [4 5]
#  [5 6]]

print(a)
# [[1 2 3 4 5]
#  [2 3 4 5 6]]

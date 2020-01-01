import numpy
import re

names = numpy.array(['Mary', 'Bar', 'Joe', 'Jane'])
print(names)      # ['Mary' 'Bar' 'Joe' 'Jane']


selector = numpy.vectorize(lambda x: True if re.search(r'ar', x) else False)
print(selector(names))          # [ True True False False]

scores = numpy.array([
    [23, 37, 18, 97, 13, 40],
    [10, 15, 20, 30, 39, 50],
    [99, 20, 83, 42, 19, 31],
    [19, 11, 55, 78, 39, 27]
])

print(scores[selector(names)])

# [[23 37 18 97 13 40]
#  [10 15 20 30 39 50]]

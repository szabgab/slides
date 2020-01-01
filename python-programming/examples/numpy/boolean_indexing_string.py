import numpy

words = numpy.array(['Foo', 'Bar', 'Baz', 'Hello World', 'Again'])
print(words)      # ['Foo' 'Bar' 'Baz' 'Hello World' 'Again']


a = words == 'Foo'
print(a)          # [ True False False False False]


vect_len = numpy.vectorize(len)
print(vect_len(words))    # [ 3  3  3 11  5]

gt = numpy.vectorize(lambda x: len(x) > 3)
print(gt(words))          # [False False False  True  True]

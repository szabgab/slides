names = ['Jan', 'Feb', 'Mar', 'Apr']
days =  [31, 28, 31, 30]

month = dict(zip(names, days))
print(month)


zipper = zip(names, days)
print(zipper)
print(list(zipper))


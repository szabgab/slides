names = ['Jan', 'Feb', 'Mar', 'Apr']
days =  [31, 28, 31, 30]

zipped = zip(names, days)
print(zipped)
print(list(zipped))

zipped = zip(names, days)
month = dict(zipped)
print(month)

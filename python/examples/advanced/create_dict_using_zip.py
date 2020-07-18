names = ['Jan', 'Feb', 'Mar', 'Apr']
days =  [31, 28, 31, 30]

zipped = zip(names, days)
print(zipped)

pairs = list(zipped)
print(pairs)

month = dict(zipped)
print(month)   # this is empty because zipped was already exhausted by the "list" call

zipped = zip(names, days)
month = dict(zipped)
print(month)

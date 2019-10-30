animals = ['chicken', 'cow', 'snail', 'elephant']
print(animals)         # ['chicken', 'cow', 'snail', 'elephant']

s = sorted(animals)
print(s)               # ['chicken', 'cow', 'elephant', 'snail']
print(animals)         # ['chicken', 'cow', 'snail', 'elephant']

r = sorted(animals, reverse=True, key=len)
print(r)               # ['elephant', 'chicken', 'snail', 'cow']
print(animals)         # ['chicken', 'cow', 'snail', 'elephant']


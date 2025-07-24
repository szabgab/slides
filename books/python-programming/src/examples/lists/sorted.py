animals = ['chicken', 'cow', 'snail', 'elephant']
print(animals)         # ['chicken', 'cow', 'snail', 'elephant']

srd = sorted(animals)
print(srt)             # ['chicken', 'cow', 'elephant', 'snail']
print(animals)         # ['chicken', 'cow', 'snail', 'elephant']

rev = sorted(animals, reverse=True, key=len)
print(rev)             # ['elephant', 'chicken', 'snail', 'cow']
print(animals)         # ['chicken', 'cow', 'snail', 'elephant']


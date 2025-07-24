animals = ['chicken', 'cow', 'snail', 'elephant']
print(animals)

animals.sort()
print(animals)

animals.sort(key=len)
print(animals)

animals.sort(key=len, reverse=True)
print(animals)


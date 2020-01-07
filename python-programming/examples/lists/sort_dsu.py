animals = ['chicken', 'cow', 'snail', 'elephant']
print(sorted(animals))
print(sorted(animals, key=len))

decorated = [(len(w), w) for w in animals]
print(decorated)

decorated.sort()
result = [ d[1] for d in decorated]
print(result)

# at once
print( [ d[1] for d in sorted( [(len(w), w) for w in animals] ) ] )

english = set(['door', 'car', 'lunar', 'era'])
spanish = set(['era', 'lunar', 'hola'])

print('english: ', english)
print('spanish: ', spanish)
inter = english.intersection(spanish)
print('intersection: ', inter)

print('issubset: ', inter.issubset( spanish ))

diff = english.symmetric_difference(spanish)
print('symmetric_difference: ', diff)


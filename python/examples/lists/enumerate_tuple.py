planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

enu = enumerate(planets)
print(type(enu).__name__)
print(enu)

print('-----')

element = next(enu)
print(type(element))
print(element)

print('-----')

for tpl in enumerate(planets):
    print(tpl[0], tpl[1])


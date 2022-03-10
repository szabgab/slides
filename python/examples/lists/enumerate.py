planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
for idx, planet in enumerate(planets):
    print(idx, planet)

print('-----')

enu = enumerate(planets)
print(type(enu).__name__)
print(enu)

print('-----')

element = next(enu)
print(type(element))
print(element)


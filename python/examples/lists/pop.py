planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter']
print(planets)          # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter']

last = planets.pop()
print(last)             # Jupiter
print(planets)          # ['Mercury', 'Venus', 'Earth', 'Mars']

third = planets.pop(2)
print(third)            # Earth
print(planets)          # ['Mercury', 'Venus', 'Mars']


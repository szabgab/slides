planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
for idx, planet in enumerate(planets):
    print(idx, planet)

print('')
enu = enumerate(planet)
print(enu.__class__.__name__)
print(enu)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

enu = enumerate(planets)
print(type(enu).__name__)
print(enu)
#for t in enu:
#    print(t)
for ix, planet in enu:
    print(ix, planet)

#print('-----')
#
#element = next(enu)
#print(type(element))
#print(element)
#
#print('-----')
#
#for tpl in enumerate(planets):
#    print(tpl[0], tpl[1])
#

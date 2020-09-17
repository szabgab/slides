set(['Neptun', 'Mars'])

objects  = set(['Mars', 'Jupiter', 'Saturn'])
internal = set(['Mercury', 'Venus', 'Earth', 'Mars'])

objects.update(internal)
print(objects)
print(internal)


objects  = set(['Mars', 'Jupiter', 'Saturn'])
internal = set(['Mercury', 'Venus', 'Earth', 'Mars'])
internal.update(objects)
print(objects)
print(internal)


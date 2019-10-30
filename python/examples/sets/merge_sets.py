set(['Neptun', 'Mars'])


objects  = set(['Mars', 'Jupiter', 'Saturn'])
internal = set(['Mercury', 'Venus', 'Earth', 'Mars'])

objects.update(internal)
#                    Python 2                                                        Python 3
print(objects)     # set(['Mercury', 'Jupiter', 'Mars', 'Earth', 'Venus', 'Saturn'])  {'Saturn', 'Jupiter', 'Earth', 'Mercury', 'Venus', 'Mars'}
print(internal)    # set(['Mercury', 'Earth', 'Venus', 'Mars'])                       {'Earth', 'Venus', 'Mercury', 'Mars'}


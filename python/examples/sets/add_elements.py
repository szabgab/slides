#                    Python 2                           Python 3
objects = set()
print(objects)     # set([])                            set()

objects.add('Mars')
print(objects)     # set(['Mars'])                      {'Mars'}

objects.add('Mars')
print(objects)     # set(['Mars'])                      {'Mars'}

objects.add('Neptun')
print(objects)     # set(['Neptun', 'Mars'])            {'Mars', 'Neptun'}

english = set(['door', 'car', 'lunar', 'era'])
spanish = set(['era', 'lunar', 'hola'])

diff = english.symmetric_difference(spanish)
print('symmetric_difference: ', diff)

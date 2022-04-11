english = set(['door', 'car', 'lunar', 'era'])
spanish = set(['era', 'lunar', 'hola'])

print(spanish.difference(english))
print(english.difference(spanish))
print()


eng = english - spanish
spa = spanish - english
print(spa)
print(eng)
print()

print(english)
print(spanish)


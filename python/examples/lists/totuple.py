planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

print(planets)
print(planets.__class__.__name__)

tpl = tuple(planets)
print(tpl)
print(tpl.__class__.__name__)


lst = list(tpl)
print(lst)
print(lst.__class__.__name__)

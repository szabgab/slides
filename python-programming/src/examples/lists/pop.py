planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter']
print(planets)          # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter']

third = planets.pop(2)
print(third)            # Earth
print(planets)          # ['Mercury', 'Venus', 'Mars', 'Jupiter']

last = planets.pop()
print(last)             # Jupiter
print(planets)          # ['Mercury', 'Venus', 'Mars']

# planets.pop(4)          # IndexError: pop index out of range

jupyter_landers = []
# jupyter_landers.pop()   # IndexError: pop from empty list

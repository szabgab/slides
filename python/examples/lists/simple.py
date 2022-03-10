planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

print(planets)   # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']
print(len(planets))    # 6
print(type(planets))      # <class 'list'>

print(planets[0])         # Mercury
print(type(planets[0]))   # <class 'str'>
print(planets[3])         # Mars

print(planets[0:1])       # ['Mercury']
print(type(planets[0:1])) # <class 'list'>
print(planets[0:2])       # ['Mercury', 'Venus']
print(planets[1:3])       # ['Venus', 'Earth']

print(planets[2:])        # ['Earth', 'Mars', 'Jupiter', 'Saturn']
print(planets[:3])        # ['Mercury', 'Venus', 'Earth']

print(planets[:])         # ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn']

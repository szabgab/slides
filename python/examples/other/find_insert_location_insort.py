import bisect
solar_system = ['Earth', 'Jupiter', 'Mercury', 'Saturn', 'Venus']

name = 'Mars'

# Find the location where to insert the element to keep the list sorted and insert the element
bisect.insort(solar_system, name)
print(solar_system)
print(sorted(solar_system))


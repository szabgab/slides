import bisect
solar_system = ['Earth', 'Jupiter', 'Mercury', 'Saturn', 'Venus']

name = 'Mars'

# Find the location where to insert the element to keep the list sorted
loc = bisect.bisect(solar_system, name)
print(loc)
solar_system.insert(loc, name)
print(solar_system)
print(sorted(solar_system))

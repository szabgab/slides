planets = [
    ["Mercury", 1],
    ["Venus", 2],
    ["Earth", 3],
    ["Earth", 2]
]
other_planets = planets
sorted_planets = sorted(planets)
print(sorted_planets)

planets[0][1] = 100
print(planets)
print(other_planets)
print(sorted_planets)


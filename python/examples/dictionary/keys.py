import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

planets = {}
with open(filename) as fh:
    for row in fh:
        row = row.rstrip("\n")
        # print(row)
        planet, distance = row.split(":")
        # print(planet)
        planets[planet] = distance

print(planets) #

print(planets.keys())        #
print(list(planets.keys()))  #


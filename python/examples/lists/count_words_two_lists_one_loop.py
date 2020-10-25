celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]

names   = []
counter = []

for name in celestial_objects:
    for idx in range(len(names)):
        if name == names[idx]:
            counter[idx] += 1
            break
    else:
        names.append(name)
        counter.append(1)

for i in range(len(names)):
    print("{:12}   {}".format(names[i], counter[i]))


from collections import defaultdict

combined = defaultdict(int)

for filename in (['examples/files/a.txt', 'examples/files/b.txt']):
    with open(filename) as fh:
        for line in fh:
            key, value = line.rstrip("\n").split("=")
            combined[key] += int(value)


with open('out.txt', 'w') as fh:
    for key, value in sorted(combined.items()):
        print("{}={}".format(key, value))
        fh.write("{}={}\n".format(key, value))

scores = {
    "Jane"    : 30,
    "Joe"     : 20,
    "George"  : 37,
    "Hellena" : 90,
}

for name in scores.keys():
    print(f"{name:8} {scores[name]}")

print('')
for name in sorted(scores.keys()):
    print(f"{name:8} {scores[name]}")

print('')
for name in sorted(scores.keys(), key=lambda x: scores[x]):
    print(f"{name:8} {scores[name]}")

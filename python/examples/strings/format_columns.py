data = [
    ["Foo Bar", 42],
    ["Bjorg", 12345],
    ["Roza", 7],
]

for entry in data:
    print("{} {}".format(entry[0], entry[1]))

print('-' * 16)

for entry in data:
    print("{:<8}|{:>7}".format(entry[0], entry[1]))

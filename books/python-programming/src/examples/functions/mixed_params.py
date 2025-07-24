fname = "Foo"
lname = "Bar"
animals = ["snake", "mouse", "cat", "dog"]

print(fname, lname, sep="-", end="\n\n")

by_length = sorted(animals, key=len, reverse=True)
print(by_length)


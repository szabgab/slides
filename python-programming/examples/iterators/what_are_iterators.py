from collections.abc import Iterator, Iterable

text = "Hello World"
animals = ["Tiger", "Mouse"]
colors = ("Blue", "Red")
rng = range(10)
fh = open(__file__)

for thing in [text, animals, colors, fh, rng]:
    print(thing.__class__.__name__)
    print(issubclass(thing.__class__, Iterator))
    print(issubclass(thing.__class__, Iterable))
    print()

fh.close()
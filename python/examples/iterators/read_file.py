from collections.abc import Iterator, Iterable
from io import TextIOWrapper

with open(__file__) as fh:
    print(fh.__class__.__name__)
    print(issubclass(fh.__class__, TextIOWrapper))
    print(issubclass(fh.__class__, Iterator))
    print(issubclass(fh.__class__, Iterable))

    for line in fh:
        pass
        #print(line, end="")

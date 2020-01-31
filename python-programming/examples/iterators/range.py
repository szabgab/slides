for n in range(2, 12, 3):
    print(n)
print()

for n in range(3):
    print(n)
print()

for n in range(2, 5):
    print(n)
print()

from collections.abc import Iterator, Iterable
rng = range(2, 5)
print(issubclass(rng.__class__, Iterator))
print(issubclass(rng.__class__, Iterable))

from counter import Counter

class GetMyIterable():
    def __init__(self):
        pass
    def __iter__(self):
        return Counter()


thing = GetMyIterable()

from collections.abc import Iterator, Iterable
print(issubclass(thing.__class__, Iterator))
print(issubclass(thing.__class__, Iterable))

for i in thing:
    print(i)

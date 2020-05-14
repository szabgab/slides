from collections.abc import Iterator, Iterable
from counter import Counter

cnt = Counter()
print(cnt.__class__.__name__)
print(issubclass(cnt.__class__, Iterator))
print(issubclass(cnt.__class__, Iterable))

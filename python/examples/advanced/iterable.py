from collections.abc import Iterator, Iterable
from types import GeneratorType

print( issubclass(GeneratorType, Iterator) )  # True
print( issubclass(Iterator, Iterable) )       # True


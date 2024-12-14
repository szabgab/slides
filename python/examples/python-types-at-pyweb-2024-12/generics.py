from typing import TypeVar
from typing import Protocol, Self

from abc import abstractmethod

class SupportsAdd(Protocol):
    @abstractmethod
    def __add__(self, other: Self) -> Self:
        pass
    

# def add[T](x: T, y: T) -> T:
#     return x + y

#T = TypeVar('T', int, str)
# T = TypeVar('T', bound=SupportsAdd)
# def add(x: T, y: T) -> T:
#     return x + y


def add[T: SupportsAdd](x: T, y: T) -> T:
    return x + y

z = add(2, 3)
print(z + 2)
#print(z + "2")

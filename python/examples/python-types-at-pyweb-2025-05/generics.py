from typing import TypeVar
from typing import Protocol, Self
from abc import abstractmethod

class SupportsAdd(Protocol):
    @abstractmethod
    def __add__(self, other: Self) -> Self:
        pass

T = TypeVar('T', bound=SupportsAdd)

# -------------------------------
def add(x: T, y: T) -> T:
    return x + y

z = add(2, 3)
print(z)

# -------------------------------
def adder[T: SupportsAdd](x: T, y: T) -> T:
    return x + y

z = adder(3, 4)
print(z)

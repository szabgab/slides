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
q = add("a", "b")

class Point():
    #pass
    def __add__(self, other):
        pass

p1 = Point()
p2 = Point()
p = add(p1, p2)


# -------------------------------
#def adder[T: SupportsAdd](x: T, y: T) -> T:
#    return x + y
#
#z = adder(3, 4)
#print(z)

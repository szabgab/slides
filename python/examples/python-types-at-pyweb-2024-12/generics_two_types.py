
def no_problem[T](x: T, y: T) -> None:
    print(type(x).__name__, type(y).__name__)

no_problem(2, 2)
no_problem("hi", "hi")
no_problem("hi", 2)

# -----------------------------
from typing import TypeVar

T = TypeVar('T', int, str)

def the_same(x: T, y: T) -> None:
    print(type(x).__name__, type(y).__name__)

the_same(2, 2)
the_same("hi", "hi")
the_same("hi", 2)


# -----------------------------
Q = TypeVar('Q', int, str)

def different(x: T, y: Q) -> None:
    print(type(x).__name__, type(y).__name__)

different(2, 2)
different("hi", "hi")
different("hi", 2)

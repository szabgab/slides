from typing import TypeVar

T = TypeVar('T', int, str)

def add(x: T, y: T) -> T:
    return x + y

add(2, 3)

from typing import Generator

def numbers(n: int) -> Generator[int, None, None]:
    return ( x for x in range(n))

print(list(numbers(10)))

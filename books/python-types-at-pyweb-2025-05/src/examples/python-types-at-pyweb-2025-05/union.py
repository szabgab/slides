from typing import Union

def my_exit(code: Union[str, int]):
    print(type(code).__name__)

my_exit(3)
my_exit("problem")
my_exit(3.14)

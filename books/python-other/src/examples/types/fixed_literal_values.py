from typing import Literal

Color = Literal["red", "blue", "yellow"]

def paint(color:Color):
    print(color)

paint("red")
paint("green")
paint("blue")

# https://mypy.readthedocs.io/en/stable/literal_types.html

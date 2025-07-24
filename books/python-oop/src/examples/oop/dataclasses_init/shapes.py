from dataclasses import dataclass

@dataclass
class Point():
    x : float
    y : float
    name : str

    def __post_init__(self):
        print(f"In post init: {self.name}")

from dataclasses import dataclass, field

@dataclass
class Fruits():
    # names : list = []  # ValueError: mutable default <class 'list'> for field names is not allowed: use default_factory
    names : list = field(default_factory=lambda : [])


f1 = Fruits()
f1.names.append('Apple')
f1.names.append('Banana')
print(f1)      # Fruits(names=['Apple', 'Banana'])


f2 = Fruits(['Peach', 'Pear'])
print(f2)      # Fruits(names=['Peach', 'Pear'])

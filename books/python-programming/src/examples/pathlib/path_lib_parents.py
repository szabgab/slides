from pathlib import Path

this = Path(__file__)
print(this)
print(this.parent)       # dirname
print(this.parents[0])   # dirname (first parent)
print(this.parents[1])   # grandparent
...
print(this.parents[-1])  # /



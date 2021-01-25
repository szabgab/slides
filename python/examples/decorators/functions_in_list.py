
def hello(name):
    print(f"Hello {name}")

def morning(name):
    print(f"Good morning {name}")


hello("Jane")
morning("Jane")
print()

funcs = [hello, morning]
funcs[0]("Peter")
print()

for func in funcs:
    func("Mary")

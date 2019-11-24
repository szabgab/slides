from decor_any import tron


@tron
def one(param):
    print(f"one({param})")

@tron
def two(first, second = 42):
    print(f"two({first}, {second})")


one("hello")
one(param = "world")

two("hi")
two(first = "Foo", second = "Bar")

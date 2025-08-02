a = 1
b = a
c = 1

print(a == b)  # True
print(a == c)  # True
print(a is b)  # True
print(a is c)  # True


a = {"name": "Foo"}
b = a
c = {"name": "Foo"}

print(a == b)  # True
print(a == c)  # True
print(a is b)  # True
print(a is c)  # False


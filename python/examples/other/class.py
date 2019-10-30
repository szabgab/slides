import re

a = 2
b = "3"
c = 2.3

m = re.search(r'\d', str(c))

print(a.__class__)   # <type 'int'>
print(b.__class__)   # <type 'str'>
print(c.__class__)   # <type 'float'>

print(a.__class__.__name__)   # int
print(b.__class__.__name__)   # str
print(c.__class__.__name__)   # float

print(re.__class__.__name__)  # module
print(m.__class__.__name__)   # SRE_Match

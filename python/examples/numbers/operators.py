a = 2
b = 3
c = 2.3

d = a + b
print(d)       # 5
print(a + b)   # 5
print(a + c)   # 4.3
print(b / a)   # 1.5    # see the __future__
print(a * c)   # 4.6
print(a ** b)  # 8

a += 7         # is the same as a = a + 7
print(a)       # 9

# a++          # SyntaxError: invalid syntax
# a--          # SyntaxError: invalid syntax

a += 1
print(a)       # 10
a -= 1
print(a)       # 9

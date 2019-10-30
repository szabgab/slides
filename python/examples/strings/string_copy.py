x = "abcd"
print(x)     # abcd

x = x + "ef"
print(x)     # abcdef

y = x
print(y)     # abcdef
x = "xyz"
print(x)     # xyz
print(y)     # abcdef

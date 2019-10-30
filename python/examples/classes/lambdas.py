a = lambda x: True
b = lambda x: False
c = lambda x: x
#c = lambda x: return
#c = lambda x: pass 
d = lambda x: c(x)+c(x)

print(a(1))
print(b(1))
print(c(42))
print(d(21))

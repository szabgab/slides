a = [2]

def f():
    print(a)       # [2]
    a.append(3)
    print(a)       # [2, 3]
    a[0] = 4

f()
print(a)           # [4, 3]


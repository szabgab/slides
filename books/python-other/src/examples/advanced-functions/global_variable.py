a = 42
def f():
    global a
    print(a)
    a = 23

print(a)   # 42
f()        # 42
print(a)   # 23


def f():
    global y
    y = "hello y"
    print("in f")

x = 2
print(x)
f()
print(y)
y = 13
print(42)


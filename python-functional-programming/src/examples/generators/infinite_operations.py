def fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a

double_fibonacci = (value * 2 for value in fibonacci())

for a in double_fibonacci:
    print(a)

    if a > 200:
        break

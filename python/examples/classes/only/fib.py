import fibonacci
f = fibonacci.Fibonacci(limit = 10)
print(f)
for v in f:
    print(v)

print('-----')
f = fibonacci.Fibonacci()
for v in f:
    print(v)
    if v > 30:
        break


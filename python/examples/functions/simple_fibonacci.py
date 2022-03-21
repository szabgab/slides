def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print(fib(1))  # [1]
print(fib(2))  # [1, 1]
print(fib(3))  # [1, 1, 2]
print(fib(10)) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

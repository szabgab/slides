def fib(n):
    if int(n) != n or n <= 0:
        raise ValueError("Bad parameter")

    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(3, fib(3))    # 2
print(30, fib(30))  # 832040

fib(0.5)


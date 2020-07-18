def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print(3, fib(3))    # 2
print(30, fib(30))  # 832040


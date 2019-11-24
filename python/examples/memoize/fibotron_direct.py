import decor

def fibo(n):
    if n in (1,2):
        return 1
    return fibo(n-1) + fibo(n-2)

fibo = decor.tron(fibo)

print(fibo(5))

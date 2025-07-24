from series import fibonacci

even = ( fib for fib in fibonacci() if fib % 2 == 0 )
for e in even:
    print(e)
    if e > 40:
        break

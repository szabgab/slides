from fibonacci import Fibonacci

fib = Fibonacci()

#odd = [x for x in fib if x % 2 == 1]
odd = filter(lambda x: x % 2 == 1, fib)

print("Let's see")

for v in odd:
    print(v)
    if v > 10:
        break

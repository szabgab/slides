import sys

n = int(sys.argv[1])

#print(n)

is_prime = True
for i in range(2, int( n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False
        break

print(is_prime)


# math.sqrt(n) might be clearer than n ** 0.5


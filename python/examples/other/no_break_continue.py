i = 2
n = 3*5*7
while i < n:
    if (n / i) * i == n:
        print('{:2}  divides {}'.format(i, n))
    i = i + 1

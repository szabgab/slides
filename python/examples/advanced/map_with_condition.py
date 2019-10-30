numbers = [1, 2, 3, 4]

def cond_double(n):
   if n % 2:
      return 2*n
   else:
      return n

cd = map(cond_double, numbers)
print(cd)                        # [2, 2, 6, 4]

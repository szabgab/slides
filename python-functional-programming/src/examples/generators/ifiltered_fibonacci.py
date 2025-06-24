from series import fibonacci
from itertools import ifilter

even = ifilter(  lambda f: f % 2 == 0, fibonacci()  )
for e in even:
    print(e)
    if e > 200:
        break

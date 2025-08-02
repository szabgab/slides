from itertools import izip, count
from my_iterators import fibo, alter

mixer = izip(count(), fibo(), alter())

for mix in mixer:
    print("{:3}  {:3}  {:3}".format(*mix))
    if mix[0] >= 8: break

  # 0    1    1
  # 1    1   -2
  # 2    2    3
  # 3    3   -4
  # 4    5    5
  # 5    8   -6
  # 6   13    7
  # 7   21   -8
  # 8   34    9

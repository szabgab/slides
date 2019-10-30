from itertools import izip, count

for t in izip(count(start=1, step=1), count(start=10, step=-1)):
    print("{:3} + {:3} = {}".format(t[0], t[1], t[0]+t[1]))
    if t[0] > 20:
        break
  #  1 +  10 = 11
  #  2 +   9 = 11
  #  3 +   8 = 11
  #  4 +   7 = 11
  #  ...
  # 20 +  -9 = 11
  # 21 + -10 = 11

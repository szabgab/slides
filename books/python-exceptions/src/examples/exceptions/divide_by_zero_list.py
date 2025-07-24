def div(a, b):
    print("dividing {} by {} is {}".format(a, b, a/b))

total = 100
values = [2, 5, 0, 4]

for val in values:
    div(total, val)

# dividing 100 by 2 is 50.0
# dividing 100 by 5 is 20.0
# Traceback (most recent call last):
# ...
# ZeroDivisionError: division by zero

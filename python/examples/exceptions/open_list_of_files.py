import module

# 3 of the 4 file exist
files = 'one.txt', 'zero.txt', 'two.txt', 'three.txt'

for f in files:
    module.read_and_divide(f)

# before one.txt
# 100.0
# after  one.txt
# before zero.txt
# Traceback (most recent call last):
# ...
# ZeroDivisionError: division by zero

import sys
import module

files = sys.argv[1:]

for filename in files:
    module.read_and_divide(filename)

# before one.txt
# 100.0
# after  one.txt
# before zero.txt
# Traceback (most recent call last):
# ...
# ZeroDivisionError: division by zero

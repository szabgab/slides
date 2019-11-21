import sys
import module

# python handle_both_exceptions.py one.txt zero.txt two.txt three.txt
files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except (ZeroDivisionError, IOError):
        print("We have a problem with file {}".format(filename))


# before one.txt
# 100.0
# after  one.txt
# before zero.txt
# We have a problem with file zero.txt
# before two.txt
# We have a problem with file two.txt
# before three.txt
# 33.333333333333336
# after  three.txt

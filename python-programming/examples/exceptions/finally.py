import sys
import module

# python finally.py one.txt zero.txt two.txt three.txt
files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except ZeroDivisionError as err:
        print("Exception {} of type {} in file {}".format(err, type(err).__name__, filename))
    finally:
        print("In finally after trying file {}".format(filename))

# before one.txt
# 100.0
# after  one.txt
# In finally after trying file one.txt
# before zero.txt
# Exception division by zero of type ZeroDivisionError in file zero.txt
# In finally after trying file zero.txt
# before two.txt
# In finally after trying file two.txt
# FileNotFoundError: [Errno 2] No such file or directory: 'two.txt'

import sys
import module

# python else.py one.txt zero.txt two.txt three.txt
files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except ZeroDivisionError as err:
        print("Exception {} of type {} in file {}".format(err, type(err).__name__, filename))
    else:
        print("In else part after trying file {}".format(filename))


# before one.txt
# 100.0
# after  one.txt
# In else part after trying file one.txt
# before zero.txt
# Exception division by zero of type ZeroDivisionError in file zero.txt
# before two.txt
# Traceback (most recent call last):
#   File "else.py", line 9, in <module>
#     module.read_and_divide(filename)
#   File "/home/gabor/work/slides/python/examples/exceptions/module.py", line 3, in read_and_divide
#     with open(filename, 'r') as fh:
# FileNotFoundError: [Errno 2] No such file or directory: 'two.txt'
#

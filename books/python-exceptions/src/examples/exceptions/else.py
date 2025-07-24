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
        print("In else part after trying file {} and succeeding".format(filename))
        # Will run only if there was no exception.
    print()

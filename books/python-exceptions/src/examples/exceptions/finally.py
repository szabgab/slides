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
    print('')

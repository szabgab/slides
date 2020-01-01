import sys
import module

# python show_exceptions_type.py one.txt zero.txt two.txt three.txt
files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except Exception as err:
        print("  There was a problem in " + filename)
        print("  Text: {}".format(err))
        print("  Name: {}".format(type(err).__name__))

# before one.txt
# 100.0
# after  one.txt
# before zero.txt
#   There was a problem in zero.txt
#   Text: division by zero
#   Name: ZeroDivisionError
# before two.txt
#   There was a problem in two.txt
#   Text: [Errno 2] No such file or directory: 'two.txt'
#   Name: FileNotFoundError
# before three.txt
# 33.333333333333336
# after  three.txt

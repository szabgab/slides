import sys
import module

files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except Exception as err:
        print(f"  There was a problem in '{filename}'", file=sys.stderr)
        print(f"  Text: {err}", file=sys.stderr)
        print(f"  Name: {type(err).__name__}", file=sys.stderr)
    print('')

# before one.txt
# 100.0
# after  one.txt

# before zero.txt
#   There was a problem in 'zero.txt'
#   Text: division by zero
#   Name: ZeroDivisionError

# before two.txt
#   There was a problem in 'two.txt'
#   Text: [Errno 2] No such file or directory: 'two.txt'
#   Name: FileNotFoundError

# before three.txt
# 33.333333333333336
# after  three.txt

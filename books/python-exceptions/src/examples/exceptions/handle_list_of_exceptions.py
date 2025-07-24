import sys
import module

files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except (ZeroDivisionError, FileNotFoundError) as err:
        print(f"We have a problem with file '{filename}'", file=sys.stderr)
        print(f"Exception type {err.__class__.__name__}", file=sys.stderr)
    print('')

# before one.txt
# 100.0
# after  one.txt

# before zero.txt
# We have a problem with file 'zero.txt'
# Exception type ZeroDivisionError

# before two.txt
# We have a problem with file 'two.txt'
# Exception type FileNotFoundError

# before three.txt
# 33.333333333333336
# after  three.txt


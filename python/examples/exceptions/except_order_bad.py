import sys
import module

files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except Exception as err:
        print(f"General error {err}")
    except ZeroDivisionError:
        print(f"Cannot divide by 0 in file '{filename}'")
    print('')

# before one.txt
# 100.0
# after  one.txt

# before zero.txt
# General error division by zero

# before two.txt
# General error [Errno 2] No such file or directory: 'two.txt'

# before three.txt
# 33.333333333333336
# after  three.txt

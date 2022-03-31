import sys
import module

files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except ZeroDivisionError:
        print(f"Cannot divide by 0 in file '{filename}'", file=sys.stderr)
    except FileNotFoundError:
        print(f"Cannot open file '{filename}'", file=sys.stderr)
    print('')

# before one.txt
# 100.0
# after  one.txt

# before zero.txt
# Cannot divide by 0 in file 'zero.txt'

# before two.txt
# Cannot open file 'two.txt'

# before three.txt
# 33.333333333333336
# after  three.txt

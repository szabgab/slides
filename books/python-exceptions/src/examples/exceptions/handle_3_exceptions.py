import sys
import module

files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except ZeroDivisionError:
        print(f"Cannot divide by 0 in file '{filename}'")
    except FileNotFoundError:
        print(f"Cannot open file '{filename}'")
    except ValueError as err:
        print(f"ValueError {err} in file '{filename}'")



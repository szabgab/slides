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



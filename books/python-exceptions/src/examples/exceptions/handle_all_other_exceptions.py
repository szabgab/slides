import sys
import module

# python handle_both_exceptions.py one.txt zero.txt two.txt three.txt
files = sys.argv[1:]

for filename in files:
    try:
        module.read_and_divide(filename)
    except ZeroDivisionError:
        print("Cannot divide by 0 in file {}".format(filename))
    except IOError:
        print("Cannot open file {}".format(filename))
    except Exception as ex:
        print("Exception type {} {} in file {}".format(type(ex).__name__, ex, filename))



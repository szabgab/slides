import module

# 3 of the 4 file exist
files = 'one.txt', 'zero.txt', 'two.txt', 'three.txt'

for f in files:
    try:
        module.read_and_divide(f)
    except ZeroDivisionError:
        print("Cannot divide by 0 in file {}".format(f))
    except IOError:
        print("Cannot open file {}".format(f))


# before one.txt
# 100.0
# after  one.txt
# before zero.txt
# Cannot divide by 0 in file zero.txt
# before two.txt
# Cannot open file two.txt
# before three.txt
# 33.333333333333336
# after  three.txt

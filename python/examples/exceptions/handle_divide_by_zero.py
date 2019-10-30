import module

# 3 of the 4 file exist
files = 'one.txt', 'zero.txt', 'two.txt', 'three.txt'

for f in files:
    try:
        module.read_and_divide(f)
    except ZeroDivisionError:
        print("Cannot divide by 0 in file {}".format(f))


# before one.txt
# 100.0
# after  one.txt
# before zero.txt
# Cannot divide by 0 in file zero.txt
# before two.txt
# IOError: [Errno 2] No such file or directory: 'two.txt'

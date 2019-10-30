import module

# 3 of the 4 file exist
files = 'one.txt', 'zero.txt', 'two.txt', 'three.txt'

for f in files:
    try:
        module.read_and_divide(f)
    except ZeroDivisionError as e:
        print("Exception {} of type {} in file {}".format(e, type(e).__name__, f))
    finally:
        print("In finally after trying file {}".format(f))

# before one.txt
# 100.0
# after  one.txt
# In finally after trying file one.txt
# before zero.txt
# Exception division by zero of type ZeroDivisionError in file zero.txt
# In finally after trying file zero.txt
# before two.txt
# In finally after trying file two.txt
# FileNotFoundError: [Errno 2] No such file or directory: 'two.txt'

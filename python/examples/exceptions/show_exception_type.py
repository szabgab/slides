import module

files = 'one.txt', 'zero.txt', 'two.txt', 'three.txt'

for f in files:
    try:
        module.read_and_divide(f)
    except Exception as e:
        print("  There was a problem in " + f)
        print("  Text: {}".format(e))
        print("  Name: {}".format(type(e).__name__))

# before one.txt
# 100.0
# after  one.txt
# before zero.txt
#   There was a problem in zero.txt
#   Text: division by zero
#   Name: ZeroDivisionError
# before two.txt
#   There was a problem in two.txt
#   Text: [Errno 2] No such file or directory: 'two.txt'
#   Name: FileNotFoundError
# before three.txt
# 33.333333333333336
# after  three.txt

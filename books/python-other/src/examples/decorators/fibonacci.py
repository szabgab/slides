import sys
import memoize_attribute
import memoize_nonlocal
import decor_any

#@memoize_attribute.memoize
#@memoize_nonlocal.memoize
#@decor_any.tron
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: {} N\n".format(sys.argv[0]))
        exit(1)
    print(fibonacci(int(sys.argv[1])))



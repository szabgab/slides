import sys

def greet(to_out, to_err=None):
    print(to_out)
    if to_err:
        print(to_err, file=sys.stderr)



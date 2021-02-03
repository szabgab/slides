import sys

def welcome(to_out, to_err=None):
    print(f"STDOUT: {to_out}")
    if to_err:
        print(f"STDERR: {to_err}", file=sys.stderr)

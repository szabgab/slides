import sys

print("on stdout (Standard Output)")
print("on stderr (Standard Error)", file=sys.stderr)
sys.stderr.write("in stderr again\n")

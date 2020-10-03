import sys

print("on stdout (Standard Output)")
print("on stderr (Standard Error)", file=sys.stderr)
sys.stderr.write("on stderr using write\n")


# x = 0
# print(1/x)

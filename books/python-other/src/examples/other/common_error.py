import sys
if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} Number")

if 42 < int(sys.argv[1]):
    res = "bigger"
elif int(sys.argv[1]) < 42:
    res = "smaller"

print(res)
# NameError: name 'res' is not defined


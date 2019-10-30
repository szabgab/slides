filename = 'README'

try:
    with open(filename, 'rb') as fh:
        while True:
            binary_str = fh.read(5000)
            print(len(binary_str))
            if len(binary_str) == 0:
                break
            # do something with the content of the binary_str
except Exception:
    pass

# 5000
# 5000
# 5000
# 1599
# 0

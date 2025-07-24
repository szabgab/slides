filename = 'examples/files/unicorns.txt'

with open(filename, 'r') as fh:
    lines  = fh.read()
print("still running")

# Traceback (most recent call last):
#   File "examples/files/open_file.py", line 5, in <module>
#     with open(filename, 'r') as fh:
# IOError: [Errno 2] No such file or directory: 'examples/files/unicorns.txt'

# Traceback (most recent call last):
#   File "examples/files/open_file.py", line 3, in <module>
#     with open(filename, 'r') as fh:
# FileNotFoundError: [Errno 2] No such file or directory: 'examples/files/unicorns.txt'


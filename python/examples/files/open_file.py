filename = 'examples/files/unicorns.txt'

with open(filename, 'r') as fh:
    lines  = fh.read()

# Traceback (most recent call last):
#   File "examples/files/open_file.py", line 5, in <module>
#     with open(filename, 'r') as fh:
# IOError: [Errno 2] No such file or directory: 'examples/files/unicorns.txt'

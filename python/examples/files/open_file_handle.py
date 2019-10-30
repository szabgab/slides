filename = 'examples/files/unicorns.txt'

try:
    with open(filename, 'r') as fh:
        lines = fh.read()
except Exception:
    print('There was some error in the file operations.')

print('Still running.')

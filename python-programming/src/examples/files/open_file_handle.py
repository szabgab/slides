filename = 'examples/files/unicorns.txt'

try:
    with open(filename, 'r') as fh:
        lines = fh.read()
except Exception as err:
    print('There was some error in the file operations.')
    print(err)
    print(type(err).__name__)

print('Still running.')


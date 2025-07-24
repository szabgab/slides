filename = 'examples/files/numbers.txt'

with open(filename, 'r') as fh:
    content = fh.read()   # reads all the lines into a string

print(type(content))
print(len(content))   # number of characters in file

print(content)        # the content of the file


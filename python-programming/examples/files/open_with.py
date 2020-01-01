filename = 'examples/files/numbers.txt'

f = open(filename, 'r')
print(f)      # <open file 'numbers.txt', mode 'r' at 0x107084390>
f.close()
print(f)      # <closed file 'numbers.txt', mode 'r' at 0x107084390>

with open(filename, 'r') as fh:
   print(fh)  # <open file 'numbers.txt', mode 'r' at 0x1070840c0>
print(fh)     # <closed file 'numbers.txt', mode 'r' at 0x1070840c0>


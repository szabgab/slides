import sys

if len(sys.argv) != 2:
    sys.stderr.write("Usage: {} FILENAME\n".format(sys.argv[0]))
    exit()


try:
    print('** Opening file')
    fh = open(sys.argv[1])
    content = fh.read()
except IOError as e:
    print(e.errno)
    print(e.strerror)
    print(e.args)
    print(e)
else:
    print('** Closing file')
    fh.close()

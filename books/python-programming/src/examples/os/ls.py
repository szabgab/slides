import sys
import glob

if len(sys.argv) == 2:
    exp = sys.argv[1]
    print(exp)
    items = glob.glob(exp)
    print(items)
else:
    files = glob.glob("?[abcdef]*.py")
    print(files)

    files = glob.glob("/usr/bin/*.sh")
    print(files)

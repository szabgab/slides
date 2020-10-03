import sys

print(sys.argv) # the list of the values
    # on the command line sys.argv[0] is the name of the Python script

print(sys.executable)  # path to the python interpreter

# print(sys.path)
    # list of file-system path strings for searching for modules
    # hard-coded at compile time but can be changed via the PYTHONPATH
    # environment variable or during execution by modifying sys.path

print(sys.version_info)
# sys.version_info(major=2, minor=7, micro=12, releaselevel='final', serial=0)
# sys.version_info(major=3, minor=8, micro=2, releaselevel='final', serial=0)

print(sys.version_info.major)  # 2 or 3

print(sys.platform)    # darwin   or  linux   or  win32


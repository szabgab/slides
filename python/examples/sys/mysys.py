import sys,os

print(sys.argv) # the list of the values
    # on the command line sys.argv[0] is the name of the Python script

print(sys.executable)  # path to the python interpreter

# print(sys.path)
    # list of file-system path strings for searching for modules
    # hard-coded at compile time but can be changed via the PYTHONPATH
    # environment variable or during execution by modifying sys.path

print(sys.version_info)
# sys.version_info(major=2, minor=7, micro=12, releaselevel='final', serial=0)

print(sys.version_info.major)  # 2 or 3

print(sys.platform)    # darwin   or  linux2   or  win32

print(os.uname())
# On Mac:
# ('Darwin', 'air.local', '16.3.0', 'Darwin Kernel Version 16.3.0: Thu Nov 17 20:23:58 PST 2016; root:xnu-3789.31.2~1/RELEASE_X86_64', 'x86_64')

# On Linux:
# posix.uname_result(sysname='Linux', nodename='thinkpad', release='5.0.0-32-generic', version='#34-Ubuntu SMP Wed Oct 2 02:06:48 UTC 2019', machine='x86_64')

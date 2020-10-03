import os
import platform

print(os.name)
print(platform.system())
print(platform.release())

# On Linux:
# posix
# Linux
# 5.3.0-24-generic

# On Windows:
# nt
# Windows
# 10

# On Mac:
# ?

if platform.system() != 'Windows':
    print(os.uname())
# On Mac:
# ('Darwin', 'air.local', '16.3.0', 'Darwin Kernel Version 16.3.0: Thu Nov 17 20:23:58 PST 2016; root:xnu-3789.31.2~1/RELEASE_X86_64', 'x86_64')

# On Linux:
# posix.uname_result(sysname='Linux', nodename='thinkpad', release='5.0.0-32-generic', version='#34-Ubuntu SMP Wed Oct 2 02:06:48 UTC 2019', machine='x86_64')

# On Windows uname is not available

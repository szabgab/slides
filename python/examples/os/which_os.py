import os
import platform

print("Name:        ", os.name)
print("System:      ", platform.system())
print("Release:     ", platform.release())
print("Architecture:", platform.architecture())
print("Machine:     ", platform.machine())
print("Processor:   ", platform.processor())
print("Release:     ", platform.release())
print("Version:     ", platform.version())

# On Windows:
# nt
# Windows
# 10

# On Mac:
# ?

if platform.system() != 'Windows':
    print("Uname:       ", os.uname())
# On Mac:
# ('Darwin', 'air.local', '16.3.0', 'Darwin Kernel Version 16.3.0: Thu Nov 17 20:23:58 PST 2016; root:xnu-3789.31.2~1/RELEASE_X86_64', 'x86_64')

# On Windows uname is not available

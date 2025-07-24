import os

command = 'ls -l'

exit_code = os.system(command)

# $? on Linux/OSX
# %ERRORLEVEL% on Windows
print(exit_code)



exit_code = os.system('ls qqrq')
print(exit_code)
print(exit_code // 256)


exit_code = os.system('ls /root')
print(exit_code)
print(exit_code // 256)


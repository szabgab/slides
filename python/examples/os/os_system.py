import os

command = 'ls -l'

exit_code = os.system(command)

# $? on Linux/OSX
# %ERRORLEVEL% on Windows
print(exit_code)

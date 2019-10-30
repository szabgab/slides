import subprocess
import sys

command = ['ls', '-l']
if sys.platform == 'win32':
    command = ['dir']

proc = subprocess.Popen(command,
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE,
) # runs the code

out,err = proc.communicate()

# out and err are two strings

print('exit code:', proc.returncode)
print('err:' , err)
print('out:')
for line in out.split('\n'):
    print(line)

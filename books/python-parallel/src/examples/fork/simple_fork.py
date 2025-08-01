import os
import time

print('{} - start running'.format(os.getpid()))

pid = os.fork()
if not pid:
    print('{} - in child. Parent is {}'.format(os.getpid(), os.getppid()))
    time.sleep(1)
    exit(3)

print('{} - in parent (child pid is {})'.format(os.getpid(), pid))

child_pid, exit_code = os.wait()
print('{} - Child with pid {} exited. Exit code {}'.format(os.getpid(), child_pid, exit_code))
print('Real exit code {}'.format(int(exit_code/256)))  # The upper byte
print('Also known as {}'.format(exit_code >> 8))  # Right shift 8 bits

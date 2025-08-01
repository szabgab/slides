import signal
import os

print(os.getpid())

def handler(signum, frame):
    print('Signal handler called with signal', signum)

signal.signal(signal.SIGTERM, handler)

username = input('Username:')
print(username)


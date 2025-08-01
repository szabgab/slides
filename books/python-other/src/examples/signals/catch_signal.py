import signal
import os

def handler(signum, frame):
    print('Signal handler called with signal', signum)

signal.signal(signal.SIGUSR1, handler)

print("before")
os.kill(os.getpid(), signal.SIGUSR1)
print("after")


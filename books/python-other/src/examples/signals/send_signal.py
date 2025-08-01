import signal
import os

print("before")
os.kill(os.getpid(), signal.SIGUSR1)
print("after")


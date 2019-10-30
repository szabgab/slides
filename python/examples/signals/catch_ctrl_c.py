import signal

def handler(signum, frame):
    print('Signal handler called with signal', signum)

signal.signal(signal.SIGINT, handler)

username = input('Username:')
print(username)


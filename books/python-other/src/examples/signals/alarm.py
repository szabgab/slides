import signal

class MyTimeout(Exception):
    pass

def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise MyTimeout

try:
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(5)
    number = input("Divide by (5 sec):")
    signal.alarm(0)   
    print(42/int(number))
except MyTimeout:
    print('timeout')
except Exception as e:
    print(e)
    #raise

print("Still working")

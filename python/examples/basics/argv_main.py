import sys

def hello(name):
    msg = name + '!!!!'
    print('Hello ' + msg)

def main():
    hello(sys.argv[1])

main()

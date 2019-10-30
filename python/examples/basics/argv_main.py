from __future__ import print_function
import sys

def hello(name):
    msg = name + '!!!!'
    print('Hello ' + msg)

def main():
    hello(sys.argv[1])

main()

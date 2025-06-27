from __future__ import print_function
import sys

def main():
    if sys.version_info.major < 3:
        name = raw_input('Your name: ')
    else:
        name = input('Your name: ')
    print('Hello ' + name + ', how are you?')

main()

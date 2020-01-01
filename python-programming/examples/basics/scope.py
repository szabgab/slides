#!/usr/bin/env  python
from __future__ import print_function

a = 23

def main():
    global b
    b = 17
    c = 42
    print('a:', a)    # a: 23
    print('b:', b)    # b: 17
    print('c:', c)    # c: 42
    
    if True:
        print('a:', a)    # a: 23
        print('b:', b)    # b: 17
        b = 99
        print('b:', b)    # b: 99
        print('c:', c)    # c: 42

    print('a:', a)    # a: 23
    print('b:', b)    # b: 99
    print('c:', c)    # c: 42


main()

print('a:', a)  # a: 23
print('b:', b)  # b: 99
print('c:', c)  # c:
# Traceback (most recent call last):
#  File "examples\basics\scope.py", line 27, in <module>
#    print 'c:', c # c:
# NameError: name 'c' is not defined

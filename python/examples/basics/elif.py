from __future__ import print_function

def main():
    a = raw_input('First number: ')
    b = raw_input('Second number: ')

    if a == b:
        print('They are equal')
    elif int(a) < int(b):
        print(a + ' is smaller than ' + b)
    else:
        print(a + ' is bigger than ' + b)


main()

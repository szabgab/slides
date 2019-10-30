from __future__ import print_function

def main():
    a = raw_input('First number: ')
    b = raw_input('Second number: ')

    if int(b) == 0:
        print("Cannot divide by 0")
    else:
        print(int(a) / int(b))


main()

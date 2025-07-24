from __future__ import print_function

def main():
    length = int(raw_input('Length: '))
    width = int(raw_input('Width: '))

    if length <= 0:
        print("length is not positive")
        return

    if width <= 0:
        print("width is not positive")
        return

    area = length * width
    print("The area is ",  area)

main()

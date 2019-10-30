from __future__ import print_function
import sys

def main():
    if len(sys.argv) != 3:
        print("Needs 2 arguments:  width length")
        return

    width  = int( sys.argv[1] )
    length = int( sys.argv[2] )

    if length <= 0:
        print("length is not positive")
        return

    if width <= 0:
        print("width is not positive")
        return

    area = length * width
    print("The area is ",  area)

main()

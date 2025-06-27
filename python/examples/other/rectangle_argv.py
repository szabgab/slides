import sys

def main():
    if len(sys.argv) != 3:
        exit("Needs 2 arguments:  width length")

    width  = int( sys.argv[1] )
    length = int( sys.argv[2] )

    

    if length <= 0:
        exit("length is not positive")

    if width <= 0:
        exit("width is not positive")

    area = length * width
    print("The area is ",  area)

main()

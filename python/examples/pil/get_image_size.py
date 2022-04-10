from PIL import Image
import sys

if len(sys.argv) !=2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

in_file = sys.argv[1]

img = Image.open(in_file)
print(img.size)    # a tuple
print(img.size[0]) # width
print(img.size[1]) # height

print(sys.getsizeof(img)) # The size of the variable
print(sys.getsizeof(img.tobytes())) # The payload

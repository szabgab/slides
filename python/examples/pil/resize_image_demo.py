from PIL import Image
import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} FILENAME CHANGE%")

in_file = sys.argv[1]
change = float(sys.argv[2])

img = Image.open(in_file)
print(img.size)    # a tuple
print(img.size[0]) # width
print(img.size[1]) # height

print(sys.getsizeof(img)) # The size of the variable
print(sys.getsizeof(img.tobytes())) # The payload

width = int(change * img.size[0] / 100)
height = int(change * img.size[1] / 100)

out = img.resize((width, height))
out.show()
#out.save(args.out)


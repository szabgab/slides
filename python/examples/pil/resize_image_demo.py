from PIL import Image
import sys

if len(sys.argv) != 3 and len(sys.argv) != 4:
    exit(f"Usage: {sys.argv[0]} FILENAME %CHANGE OUTFILE")

in_file = sys.argv[1]
change = float(sys.argv[2])
out_file = sys.argv[3] if len(sys.argv) == 4 else None

img = Image.open(in_file)
print(img.size)    # a tuple
print(img.size[0]) # width
print(img.size[1]) # height

width = int(change * img.size[0] / 100)
height = int(change * img.size[1] / 100)

out = img.resize((width, height))
out.show()

if out_file:
    out.save(out_file)


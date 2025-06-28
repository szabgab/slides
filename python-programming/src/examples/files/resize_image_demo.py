from PIL import Image
import sys

if len(sys.argv) != 3 and len(sys.argv) != 4:
    exit(f"Usage: {sys.argv[0]} FILENAME %CHANGE OUTFILE")

in_file = sys.argv[1]
change = float(sys.argv[2])
out_file = sys.argv[3] if len(sys.argv) == 4 else None

img = Image.open(in_file) # opening file and reading meta

print(img.size)    # a tuple
print(img.size[0]) # width
print(img.size[1]) # height

width = int(change * img.size[0] / 100)
height = int(change * img.size[1] / 100)


out = img.resize((width, height))
#print("image size: ", sys.getsizeof(list(img.im)))
print("image size: ", sys.getsizeof(img.getdata()))
print("image size: ", sys.getsizeof(img.im))

out.show()
print("image size: {}", sys.getsizeof(out.im))

if out_file:
    out.save(out_file)


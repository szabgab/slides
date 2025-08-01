from PIL import Image

in_file = 'in.png'
out_file = 'new.png'

img = Image.open(in_file)

size = (img.size[0] / 2, img.size[1] / 2)
img.thumbnail(size)

img.save(out_file)
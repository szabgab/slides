from PIL import Image

in_file = 'in.png'
out_file = 'out.png'

img = Image.open(in_file)
width, height = img.size
width, height = img.size

# crop
# 10 pixels from the left
# 20 pixels from the top
# 30 pixels from the right
# 40 pixels from the bottom

cropped = img.crop((10, 20, width - 30, height - 40))
cropped.save(out_file)
cropped.show()
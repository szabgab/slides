from PIL import Image

in_file = 'python.png'

width = 600
height = 300
background = Image.new(mode='RGB', size=(width, height), color='#AAFAFA')

img = Image.open(in_file)
(emb_width, emb_height) = img.size
print(emb_width)
print(emb_height)

# slightly off the lower right corner of the background image
# using the image as the mask makes its background transparent
background.paste(im = img, box=(width-emb_width-10, height-emb_height-10), mask=img)

background.show()

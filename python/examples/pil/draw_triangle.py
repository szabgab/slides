from PIL import Image, ImageDraw

img = Image.new(mode='RGB', size=(800, 450), color='#eb8634')

draw = ImageDraw.Draw(img)
draw.polygon([(790, 275), (790, 430), (300, 430) ])

img.save('first.png')
img.show()

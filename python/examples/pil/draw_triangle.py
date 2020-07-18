from PIL import Image, ImageDraw

img = Image.new(mode='RGB', size=(800, 450), color='#eb8634')

draw = ImageDraw.Draw(img)
draw.polygon([(800, 275), (800, 450), (300, 450) ])

img.save('first.png')
img.show()
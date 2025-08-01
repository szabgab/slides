from PIL import Image, ImageDraw

img = Image.new(mode='RGB', size=(800, 450), color='#eb8634')

draw = ImageDraw.Draw(img)
draw.polygon([(400, 200), (400, 300), (200, 300), (200, 200) ])

img.save('first.png')
img.show()


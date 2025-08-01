from PIL import Image, ImageDraw

img = Image.new(mode='RGB', size=(1600, 900), color='#eb8634')

draw = ImageDraw.Draw(img)
draw.polygon([(1600, 550), (1600, 900), (600, 900) ], fill = (255, 255, 255))

#img.save('first.png')
img.show()


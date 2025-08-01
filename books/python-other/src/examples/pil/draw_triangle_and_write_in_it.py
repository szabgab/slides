from PIL import Image, ImageDraw, ImageFont

img = Image.new(mode='RGB', size=(800, 450), color='#eb8634')

draw = ImageDraw.Draw(img)
draw.polygon([(800, 275), (800, 450), (300, 450) ], fill = (255, 255, 255))

font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 30)

draw.text((500, 400), 'Hello from Python', (0, 0, 0), font=font)


img.save('first.png')
img.show()


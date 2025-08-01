from PIL import Image, ImageDraw, ImageFont, ImageOps

img = Image.new(mode='RGB', size=(400, 200), color='#eb8634')

# #draw = ImageDraw.Draw(img)
# #draw.polygon([(800, 275), (800, 450), (300, 450) ], fill = (255, 255, 255))
#
#
#font = ImageFont.load_default()
font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 30)
# txt = Image.new('L', (500, 500))
# d = ImageDraw.Draw(txt)
# d.text((300, 400), 'Hello from Python', font=font, color="white")
# w=txt.rotate(17.5,  expand=1)
#
# #img.paste(txt)
# img.paste( ImageOps.colorize(w, (0,0,0), (255,255,84)), (242,60),  w)
# # img.save('first.png')
# img.show()
#

text_layer = Image.new('L', (300, 50))
draw = ImageDraw.Draw(text_layer)
draw.text( (30, 0), "Text slightly rotated",  font=font, fill=255)

rotated_text_layer = text_layer.rotate(10.0, expand=1)
img.paste( ImageOps.colorize(rotated_text_layer, (0,0,0), (10, 10,10)), (42,60),  rotated_text_layer)
img.show()

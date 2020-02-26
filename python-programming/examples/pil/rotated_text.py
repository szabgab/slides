from PIL import Image, ImageDraw, ImageFont, ImageOps

img = Image.new(mode='RGB', size=(400, 200), color='#eb8634')

font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 30)

text_layer = Image.new('L', (300, 50))
draw = ImageDraw.Draw(text_layer)
draw.text( (30, 0), "Text slightly rotated",  font=font, fill=255)

rotated_text_layer = text_layer.rotate(10.0, expand=1)
img.paste( ImageOps.colorize(rotated_text_layer, (0,0,0), (10, 10,10)), (42,60),  rotated_text_layer)
img.show()

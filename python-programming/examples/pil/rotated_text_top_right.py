from PIL import Image, ImageDraw, ImageFont, ImageOps

width = 400
height = 200
start = 100
end   = 50

img = Image.new(mode='RGB', size=(width, height), color='#FAFAFA')

stripe_color = "#eb8634"
draw = ImageDraw.Draw(img)
draw.polygon([(width-start, 0), (width-end, 0), (width, end), (width, start) ], fill=stripe_color)


font = ImageFont.truetype('Pillow/Tests/fonts/FreeSansBold.ttf', 30)
text_layer = Image.new('RGB', size=(100, 100), color=stripe_color)

draw = ImageDraw.Draw(text_layer)
text = "Free"
size = draw.textsize(text=text, font=font)
# print(size)
draw.text( xy=(20, 0), text=text,  font=font, fill=1)
#
rotated_text_layer = text_layer.rotate(-45.0, expand=0)
rotated_text_layer.show()
#img.paste( ImageOps.colorize(rotated_text_layer, (0,0,0), (10, 10,10)), (42,60),  rotated_text_layer)
#img.paste(im = rotated_text_layer, box=(300, 0))
#img.paste(im = text_layer, box=(300, 0))
#img.show()

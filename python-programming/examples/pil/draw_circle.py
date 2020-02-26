from PIL import Image, ImageDraw

img = Image.new('RGBA', (100, 100))

draw = ImageDraw.Draw(img)
draw.ellipse((0, 0, 100, 100), fill=(255, 255, 255))
img.show()

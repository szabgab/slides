from PIL import Image, ImageDraw

img = Image.new('RGBA', size=(100, 100))

draw = ImageDraw.Draw(img)
draw.rectangle((10, 10, 90, 90), fill="yellow", outline="red")
img.show()
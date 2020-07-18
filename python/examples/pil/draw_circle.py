from PIL import Image, ImageDraw

img = Image.new('RGB', (200, 200))

draw = ImageDraw.Draw(img)
draw.ellipse((50, 50, 150, 150), fill="#F00F4F")
img.show()

from PIL import Image, ImageDraw

img = Image.new('RGB', size=(100, 60), color='#eb8634')

draw = ImageDraw.Draw(img)
draw.text(
    text="Some text",
    xy=(10, 20),
)

img.save('first.png')
img.show()
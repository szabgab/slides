from PIL import Image, ImageDraw, ImageFont

img = Image.new(mode='RGB', size=(300, 60), color='#eb8634')
font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 20)

draw = ImageDraw.Draw(img)
draw.text(
    text="Some text",
    xy=(10, 20),
    font=font,
)

img.save('first.png')
img.show()
from PIL import Image, ImageDraw, ImageFont

img = Image.new(mode='RGB', size=(300, 60), color='#eb8634')
font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 20)
#font = ImageFont.truetype(f'c:\Windows\Fonts\Candara.ttf', 30)
#font = ImageFont.truetype(f'c:\Windows\Fonts\Candarab.ttf', 30)
#font = ImageFont.truetype(f'c:\Windows\Fonts\david.ttf', 30)


draw = ImageDraw.Draw(img)
draw.text(
    text="Some text",
    xy=(10, 20),
    font=font,
)

img.save('first.png')
img.show()
from PIL import Image, ImageDraw

def heart(size, fill):
    width, height = size
    img = Image.new('RGB', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    polygon = [
        (width / 10, height / 3),
        (width / 10, 81 * height / 120),
        (width / 2, height),
        (width - width / 10, 81 * height / 120),
        (width - width / 10, height / 3),
    ]
    draw.polygon(polygon, fill=fill)
    #img.show()

    draw.ellipse((0, 0,  width / 2, 3 * height / 4), fill=fill)
    draw.ellipse((width / 2, 0,  width, 3 * height / 4), fill=fill)
    return img

img = heart((50, 40), "red")
img.show()

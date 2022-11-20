# Generate images for several machine learning projects

# Classification
# A bunch of images with red shapes, green shapes, yellow shapes.  Tag them according to the color and the shape they got.
# Simple case: all the images are large circles of the same size
# Complex case: allow for more sizes; allow for different shapes (rectangles); allow for more than one shape on the image.
# Fine tune: What if the "red" color can be on a small scale of various red colors?
# The goal is to create a model that will be able to divide between colors and/or between shapes.

# Detection:
# On each image create one or more shapes and put a rectangle around it (with some margin around the shape)
# Add a class to each marking (describing either the color or the shape of the shape)
# Allow for more than one (different) shape/color on the same image.
# The goal is to create a model that can detect similar shapes and/or colors in other images.

# Ranking
# On each image we have many shapes and for every pair of images we can say which has more and which has less.
# On each image we have a shape with a color on a scale between red and blue (or any other two colors). For every pair of image we can include information which is more blue.
# The same could be between shapes on the range of  triangle - mnulti-angel - circle
# Extra difficulty if some of the ranking we give is incorrect (especially the ones that are close to each other) imitating human-errors in the ranking process.
# The goal is to create a model that will be able to tell about any two images which is closer to blue. Maybe it will also be able to tell where each image is on our scale.

from PIL import Image, ImageDraw

def create():
#    width = 4912
#    height = 3684
#    width = 1228
#    height = 921
    width = 720
    height = 480

    background_color = 'white'


    img = Image.new('RGB', (width, height), color = background_color)

    # 20 images with a red circle of various sizes
    # 20 images with a blue circle of various sizes
    # 20 images with a green circle of various sizes


    draw = ImageDraw.Draw(img)
    size = 50
    #draw.ellipse((width/2-size, height/2-size, width/2+size, height/2+size), fill=(255, 0, 0), outline=(0, 0, 0))
    #draw.ellipse((width/2-size, height/2-size, width/2+size, height/2+size), fill='blue', outline=(0, 0, 0))
    draw.rectangle((width/2-size, height/2-size, width/2+size, height/2+size), fill=(0, 192, 192), outline=(255, 255, 255))

    img.save('demo.jpg')
    img.show()

def create_many():
    width = 720
    height = 480

    background_color = 'white'

    for size in range (20, 241, 10):
        for color in ['red', 'green', 'blue']:
            for shape in ['circle', 'square']:
                img = Image.new('RGB', (width, height), color = background_color)
                draw = ImageDraw.Draw(img)
                if shape == 'circle':
                    draw.ellipse((width/2-size, height/2-size, width/2+size, height/2+size), fill=color, outline=(0, 0, 0))
                elif shape == 'square':
                    draw.rectangle((width/2-size, height/2-size, width/2+size, height/2+size), fill=color, outline=(255, 255, 255))

                filename = f'{shape}-{color}-{size}.jpg'
                img.save(filename)

create_many()
#create()

# PIL - Pillow
{id: pil}

## Install Pillow
{id: install-pillow}
{i: PIL}
{i: Pillow}

* [Pillow](https://pillow.readthedocs.io/)
* [Pillow on PyPI](https://pypi.org/project/Pillow/)
* [GitHub](https://github.com/python-pillow/Pillow)

```
pip install pillow
```

## Create First Image
{id: create-first-image}
{i: Image}
{i: size}
{i: color}

![](examples/pil/create_first_image.py)

* Color can be one of the well-known names e.g. "red"
* Color can be RGB in decimal or hex. (RGB=Red Green Blue)

## Write Text on Image
{id: write-text-on-image}

![](examples/pil/write_text_image.py)

## Select font for Text on Image
{id: select-font-text-on-image}

![](examples/pil/font_for_text_image.py)

## Font directories
{id: font-directories}

```
Linux: /usr/share/fonts/
Max OS: /Library/Fonts/
Windows: C:\Windows\fonts
```

## Get size of an Image
{id: get-image-size}

![](examples/pil/get_image_size.py)

## Get size of text
{id: get-size-of-text}

```
    font = ImageFont.truetype(
        'path/to/font.ttf', size
    )
    size = font.getsize(text)
```

## Resize an existing Image
{id: resize-existing-image}

![](examples/pil/resize_image.py)

## Crop an existing Image
{id: crop-existing-image}

![](examples/pil/crop_image.py)

## Combine two images
{id: combine-two-images}

* Load one image from file
* Create a plain background
* Put the loaded image on the background
* Save the combined image

## Rotated text
{id: rotated-text}

![](examples/pil/rotated_text.py)

## Rotated text in top-right corner
{id: rotated-text-in-top-right-corner}

TODO: fix this

![](examples/pil/rotated_text_top_right.py)

## Embed image (put one image on another one)
{id: embed-image}

![](examples/pil/embed_image.py)


## Draw a triangle
{id: draw-a-triangle}

![](examples/pil/draw_triangle.py)

## Draw a triangle and write text in it
{id: draw-a-triangle-and-write-text}

![](examples/pil/draw_triangle_and_write_in_it.py)

## Draw a triangle and write rotated text in it
{id: draw-a-triangle-and-write-rotated-text}

![](examples/pil/draw_triangle_and_write_in_it_rotated.py)


## Draw a rectangular
{id: draw-a-rectangular}

![](examples/pil/draw_rectangual.py)

## Draw a rectangle
{id: draw-a-rectangle}

![](examples/pil/draw_rectangle.py)

## Draw circle
{id: draw-circle}

![](examples/pil/draw_circle.py)

## Draw heart
{id: draw-heart}

![](examples/pil/draw_heart.py)

Some samples, including this one, originally by [Nadia Alramli](http://nadiana.com/)

## Rectangle with rounded corners
{id: rectangle-with-rounded-corners}

![](examples/pil/draw_rectangle_with_rounded_corners.py)

Some samples, including this one, originally by [Nadia Alramli](http://nadiana.com/)

## TODO
{id: pil-todo}

http://web.archive.org/web/20130115175340/http://nadiana.com/pil-tutorial-basic-advanced-drawing
* Make the background color change from top to bottom
* Add straight lines to existing images
* Blur image
* Add rectangular to area on existing image
* Draw other simple images

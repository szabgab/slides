# Convert SVG to PNG or JPEG

There are cases when you need to supply a raster image. Eg. a system that does not (yet ?) support SVG. How can we convert an SVG image to a raster image?

There are number of tools to do this.

## Convert SVG to PNG or JPEG using ImageMagick

[ImageMagick](https://imagemagick.org/)

To install on Ubuntu:

```
sudo apt install imagemagick
```

On the command line run:

```
convert input.svg output.png
```


## Convert SVG to PNG or JPEG using Inkscape

[Inkscape](https://inkscape.org/)

To install on Ubuntu:

```
sudo apt install inkscape
```

On the command line run:

```
inkscape --export-filename=output.png input.svg
```

## Using The Gnome Image Viewer

It is also called the [Eye of Gnome](https://help.gnome.org/users/eog/stable/) or `eog`.

We can open the image with the viewer by double-clicking on the SVG file in the file-explorer or by running:

```
eog input.svg
```

To convert click on the hamburger menu, select "Save As" and save as a `.png` file.


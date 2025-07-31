# Embed external image

The `image` tag can be used to embed images. It supports the emebedding of other SVG files and PNG and JPEG images.

Certain features do not work when using the `img` tag to display an SVG file, specifically the embedding of other images in the SVG file using the `image` tag that we'll see later. Using `object` solves this problem.

<object data="../examples/embed-image.svg" type="image/svg+xml"></object>

{% embed include file="src/examples/embed-image.svg" %}



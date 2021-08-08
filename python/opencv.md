# OpenCV
{id: opencv}

## OpenCV Installation
{id: opencv-installation}

* Install both OpenCV for Python and the external contribution packages

```
pip install opencv-python
pip install opencv-contrib-python
```

## Download images
{id: opencv-download-images}

* Visit [Duck Duck Go](https://duckduckgo.com/).
* Search for "cats" (or whatever other animal you like) and click on "Images".
* Click on an image and then on the "View File" button.
* Right-click and "Save Image As".
* Make sure you remember in which folder you saved file.


## OpenCV Read image
{id: opencv-read-image}
{i: imread}
{i: imshow}
{i: waitKey}

![](examples/opencv/read_image.py)

* press any key to stop the display

## OpenCV - read image and fail
{id: opencv-read-image}

* File does not exist
* File is not in the correct format.

```
cv2.error: OpenCV(4.5.3) /tmp/pip-req-build-agffqapq/opencv/modules/highgui/src/window.cpp:1006: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'imshow'
```

## OpenCV resize (rescale) images
{id: opencv-resize-image}
{i: shape}
{i: resize}

* To reduce the computation power needed to process the image (or video)

![](examples/opencv/resize_image.py)

* Works on images, videos, live videos

## OpenCV draw on new images
{id: opencv-draw-on-new-image}

![](examples/opencv/draw_on_new_image.py)


## OpenCV convert to greyscale
{id: opencv-conevrt-image-to-greyscale}

![](examples/opencv/convert_to_grayscale.py)


## OpenCV blur image
{id: opencv-blur-image}

* increasing the ksize the image will be more blurred

![](examples/opencv/blur_gaussian.py)

## OpenCV finding edges using Canny
{id: opencv-finding-edges-using-canny}

![](examples/opencv/canny.py)

* If we first blur the image and then run Canny on the blurred image, we get a lot less edges.

Dilate an image using structuring elements


## Download movies
{id: opencv-download-movies}

* Install pytube

```
pip install pytube
```

* Visit YouTube
* Search for "cameleon changing color"
* Take the URL of any video

```
pytube https://www.youtube.com/watch?v=hXMZ214pNZ4
```


## OpenCV Read video
{id: opencv-read-video}

![](examples/opencv/read_video.py)


* instead of filename or a number 0,1, 2 to capture video using camera

```
# v2.error: OpenCV(4.5.3) /tmp/pip-req-build-agffqapq/opencv/modules/highgui/src/window.cpp:1006:
#    error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'imshow'

# This -215 means we ran out of the frames.
```

Only for Live video:
capture.set(3, width)
capture.set(4, height)

## OpenCV Resources
{id: opencv-resources}

* [OpenCV Course - Full Tutorial with Python](https://www.youtube.com/watch?v=oXlwWbU8l2o)

```
pip install caer      # just some extra package
```

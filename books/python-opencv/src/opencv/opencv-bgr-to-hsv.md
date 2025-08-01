# OpenCV - BGR to HSV

* COLOR_BGR2HSV
* COLOR_HSV2BGR

* The conversion is not loss-less.
* Better use images that are 16-bit than images that are 8-bit (as my camera takes them)
* Even with 16 bit there might be some changes as the conversions are floating point.

{% embed include file="src/examples/opencv/bgr_to_hsv.py" %}

* Check the yello flower




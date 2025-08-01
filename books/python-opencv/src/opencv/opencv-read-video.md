# OpenCV Read video

{% embed include file="src/examples/opencv/read_video.py" %}


* instead of filename or a number 0,1, 2 to capture video using camera

```
# v2.error: OpenCV(4.5.3) /tmp/pip-req-build-agffqapq/opencv/modules/highgui/src/window.cpp:1006:
#    error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'imshow'

# This -215 means we ran out of the frames.
```

Only for Live video:
capture.set(3, width)
capture.set(4, height)




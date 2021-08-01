import cv2 as cv
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]


capture = cv.VideoCapture(filename)

while True:
    success, frame = capture.read()
    cv.imshow('Video', frame)
    #cv.waitKey(0)
    # press d to quit the video in the middle
    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()


# v2.error: OpenCV(4.5.3) /tmp/pip-req-build-agffqapq/opencv/modules/highgui/src/window.cpp:1006:
#    error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'imshow'

# This -215 means we ran out of the frames.



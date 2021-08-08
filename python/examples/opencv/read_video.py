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


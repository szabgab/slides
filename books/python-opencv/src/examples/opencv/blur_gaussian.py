import cv2 as cv
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
blurred = cv.GaussianBlur(original, ksize=(3, 3), sigmaX=cv.BORDER_DEFAULT)

cv.imshow('Blurred', blurred)
cv.waitKey(0)

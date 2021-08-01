import cv2 as cv
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

img = cv.imread(filename)
cv.imshow('Image', img)
cv.waitKey(0)

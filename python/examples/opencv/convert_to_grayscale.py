import cv2 as cv
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)

grey = cv.cvtColor(original, cv.COLOR_BGR2GRAY)

cv.imshow('Grey', grey)
cv.waitKey(0)

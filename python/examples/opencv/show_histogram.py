import cv2 as cv
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)

gray = cv.cvtColor(original, code=cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


cv.waitKey(0)

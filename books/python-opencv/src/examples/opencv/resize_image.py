import cv2 as cv
import sys

if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} FILENAME SCALE  where scale is 0.75 or some similar number between 0 and 1")

filename = sys.argv[1]
scale = float(sys.argv[2])

original = cv.imread(filename)
cv.imshow('Original', original)

height, width, colors = original.shape
new_height = int(height * scale)
new_width = int(width * scale)

resized = cv.resize(original, (new_width, new_height), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)
cv.waitKey(0)

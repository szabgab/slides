import cv2 as cv
import sys

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

original = cv.imread(filename)
cv.imshow('Original', original)


height, width, colors = original.shape
new_width = 400
new_height = int(height * new_width / width)

smaller = cv.resize(original, (new_width, new_height), interpolation=cv.INTER_AREA)
cv.imshow('Smaller', smaller)

canny = cv.Canny(smaller, 125, 175) # providing two thresholds
cv.imshow('Canny', canny)

dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

cv.waitKey(0)
